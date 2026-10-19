

# Generated at 2022-06-13 08:31:36.256754
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():

    # unit test for ansible.playbook.play_context.PlayContext.set_attributes_from_plugin
    # (test_shippable/test_ansible_playbook/test_play_context.py)
    #
    # Testing:
    #      class PlayContext(object):
    #         def set_attributes_from_plugin(self, plugin):
    #
    #
    pass

    pytest.skip("skipping test in './test_ansible_playbook/test_play_context.py'")


# Generated at 2022-06-13 08:31:43.570904
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # FIXME: Write a proper test for this function
    from ansible.plugins.loader import get_plugin_class
    plugin = get_plugin_class('paramiko')
    play = Play()
    play_context = PlayContext(play)
    play_context.set_attributes_from_plugin(plugin)
    assert play_context._attributes['connection'] == 'paramiko'


# Generated at 2022-06-13 08:31:53.477817
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    play = MagicMock()

    PC = PlayContext(play=play)
    PC.set_attributes_from_plugin('shell')

    if 'accelerate' in C.config.get_configuration_definitions(get_plugin_class('shell'), C.DEFAULT_SHELL):
        assert PC._accelerate is False
    else:
        assert PC._accelerate is None

    assert PC._executable is None
    assert PC._no_log is None
    assert PC._shell is None
    assert PC._su is False
    assert PC._su_user is None
    assert PC._su_pass is None
    assert PC._su_exe is None
    assert PC._sudo is False
    assert PC._sudo_user is None
    assert PC._sudo_pass is None
    assert PC._sudo_exe is None
   

# Generated at 2022-06-13 08:31:57.116936
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    '''
    Unit test for method PlayContext.set_attributes_from_cli
    '''
    args = {'verbosity': 0, 'start_at_task': None}
    context.CLIARGS = args
    pc = PlayContext(play=None, passwords=None, connection_lockfd=None)
    pc.set_attributes_from_cli()


# Generated at 2022-06-13 08:32:11.355247
# Unit test for method update_vars of class PlayContext
def test_PlayContext_update_vars():
    module = AnsibleModule(argument_spec=dict())
    play_context = PlayContext()
    variables = dict()

    # update_vars should not fail if there are no properties

    # test empty properties
    play_context.update_vars(variables)
    module.exit_json(changed=False)

    # test individual property
    ports = C.MAGIC_VARIABLE_MAPPING.get('port')
    play_context.port = 1
    play_context.update_vars(variables)
    assert variables[ports[0]] == 1

    # test all properties

# Generated at 2022-06-13 08:32:21.674301
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from ansible.plugins.connection.ssh import Connection as ssh
    from ansible.plugins.connection.docker import Connection as docker
    from ansible.plugins.connection.winrm import Connection as winrm
    from ansible.plugins import connection_loader
    from ansible.config.manager import ConfigManager
    config_data = {
                    'ssh_args': "-o ForwardAgent=yes -o ControlMaster=auto -o ControlPersist=60s",
                    'pipelining': 'True',
                    'ssh_executable': '/usr/bin/ssh',
                    'scp_executable': '/usr/bin/scp',
                    'docker.docker_extra_args': '-D',
                    'winrm.ssl': 'False',
                    'winrm.port': '5985'
                    }
    variables = dict()
    loader = DataLoader

# Generated at 2022-06-13 08:32:36.883358
# Unit test for method set_attributes_from_plugin of class PlayContext

# Generated at 2022-06-13 08:32:45.192544
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    def test(data, check_mode=False, diff=False, delegate_to=None, remote_user=None,
             task_vars=dict(ansible_user='root', ansible_port=22,
                            ansible_host='127.0.0.1', ansible_ssh_pass='password', ansible_ssh_private_key_file=b_('/abc/id_rsa'))):
        loader = DictDataLoader(data)
        inventory = InventoryManager(loader=loader, sources=['localhost'])
        variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 08:32:55.139237
# Unit test for constructor of class PlayContext
def test_PlayContext():
    ''' test the PlayContext constructor '''

    # Create empty PlayContext()
    play_context = PlayContext()

    # Confirm the constructor set values correctly
    assert play_context.remote_addr is None
    assert play_context.remote_user == ''
    assert play_context.password == ''
    assert play_context.connection == 'smart'
    assert play_context.port is None
    assert play_context.timeout == C.DEFAULT_TIMEOUT
    assert play_context.connection_user == ''
    assert play_context.private_key_file == C.DEFAULT_PRIVATE_KEY_FILE
    assert play_context.pipelining == C.ANSIBLE_PIPELINING
    assert play_context.network_os is None
    assert play_context.docker_extra_args is None
    assert play_context

# Generated at 2022-06-13 08:33:01.865905
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    #test case 1
    my_task = AnsibleTask()
    my_dict = {'host': {'hostname': 'hostname'}}
    test_playcontext = PlayContext()
    t = test_playcontext.set_task_and_variable_override(my_task,my_dict,None)
    assert isinstance(t,PlayContext)
    assert t._attributes['remote_addr'] == 'hostname'
    assert t._attributes['verbosity'] == 0
    assert t._attributes['start_at_task'] == None
    assert t._attributes['force_handlers'] == False
    assert t._attributes['connection'] == 'smart'

# Generated at 2022-06-13 08:33:31.681186
# Unit test for constructor of class PlayContext

# Generated at 2022-06-13 08:33:47.516497
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    data  = {}
    data["version_added"] = "2.8"
    data["version_removed"] = None
    data["description"] = "Specify the timeout in seconds for communicating with the container. If the timeout expires before the operation is completed, the module will error."
    data["required"] = False
    data["choices"] = None
    data["aliases"] = []
    data["type"] = "int"

    context.CLIARGS = {"timeout" : True}
    play = None
    passwords = {"0": "0"}
    connection_lockfd = None

    play_context_object = PlayContext(play,passwords,connection_lockfd)
    play_context_object.set_attributes_from_cli()

    assert play_context_object._timeout == data["version_added"]
# test_Play

# Generated at 2022-06-13 08:33:55.232586
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    play1 = Play()
    passwords = {}
    #
    play_context_inst = PlayContext(play1, passwords)
    task1 = Task()
    variables = {}
    templar = AnsibleTemplar()
    #
    play_context_inst.set_task_and_variable_override(task1, variables, templar)
    # check results
    assert play_context_inst is not None

# Generated at 2022-06-13 08:34:03.037806
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    play=None
    passwords=None
    connection_lockfd=None
    pc=PlayContext(play=None, passwords=None, connection_lockfd=None)
    task=None
    variables=None
    templar={}
    pc.set_task_and_variable_override(task=task, variables=variables, templar=templar)
    p=play
    p=task
    p=variables
    p=templar
    p=pc


# =================================================================================
# LINK
# =================================================================================


# Generated at 2022-06-13 08:34:15.077070
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from ansible.plugins.loader import get_plugin_class
    from ansible.plugins.connection.ssh import Connection
    
    fake_plugin = get_plugin_class(Connection)('ssh')
    fake_plugin.set_options({'host_key_checking': False, 'paramiko_use_agent': True})
    
    
    
    play_context = PlayContext()
    assert play_context is not None,"PlayConext object is None"
    assert play_context.host_key_checking == False,"PlayConext host_key_checking value is not set properly"
    assert play_context.paramiko_use_agent == True,"PlayConext paramiko_use_agent value is not set properly"
    
    
    
    
    

# Generated at 2022-06-13 08:34:24.958661
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from ansible.module_utils.connection import Connection
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import connection_loader

    '''
    Unit test case to check if set_attributes_from_plugin method of class PlayContext
    works correctly.
    '''
    playcontext = PlayContext()
    plugin = connection_loader.get('local')()
    plugin.set_options({'ansible_shell_type': 'powershell'})
    playcontext.set_attributes_from_plugin(plugin)
    assert playcontext.shell_type == 'powershell'

# Generated at 2022-06-13 08:34:37.568008
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from units.mock.loader import DictDataLoader
    
    data_loader = DictDataLoader(dict())
    inventory = InventoryManager(loader=data_loader, sources='')
    variable_manager = VariableManager(loader=data_loader, inventory=inventory)
    #Test with play
    play_source =  dict(
            name = "Ansible Play v2",
            hosts = 'localhost',
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module='debug', args=dict(msg='{{playbook_dir}}')))
            ]
        )

# Generated at 2022-06-13 08:34:38.691941
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # TODO: implement this test
    pass # nothing to test here?

# Generated at 2022-06-13 08:34:52.589307
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    class TestPlayContext(unittest.TestCase):
        def test_playcontext_set_attributes_from_plugin(self):
            # Create necessary mock objects
            module_name = 'ansible.plugins.connection.network_cli'
            plugin_name = 'ansible.plugins.connection.network_cli'
            class_name = 'C.ANSIBLE_LIBRARY/ansible/plugins/connection/network_cli.ConnectionModule'
            plugin = Mock(spec=C.config.DEFAULT_MODULE_PATH + plugin_name)
            plugin._load_name = 'network_cli'
            plugin.get_option.return_value = 'network_os_result'

            # Configure the test
            pc = PlayContext()
            pc.set_attributes_from_plugin(plugin)

            # Test the result

# Generated at 2022-06-13 08:35:00.672502
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    pass
    # create an instance of the class to test
    test_obj = PlayContext()

    # TODO: test the exceptions raised by this method
    # test passing the wrong type for 'plugin'
    #with pytest.raises(TypeError):
    #    test_obj.set_attributes_from_plugin(plugin='badtype')

    # test passing the wrong type for 'options'
    #with pytest.raises(TypeError):
    #    test_obj.set_attributes_from_plugin(options='badtype')


# Generated at 2022-06-13 08:35:57.510404
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # load fake plugin
    plugin_loader._implicit_import_modules('connection')
    # load fake plugin
    plugin_loader._implicit_import_modules('become')
    import ansible.plugins.connection
    # load fake plugin
    plugin_loader._implicit_import_modules('become')
    import ansible.plugins.become

    # create a fake task
    task = Task()

    # create a fake play
    play = Play()

    # create a fake inventory
    inventory = Inventory('fake')

    # create a var manager
    var_manager = VariableManager()

    # create a fake runner
    runner = Runner()

    # create a fake templar
    templar = Templar(loader=None, variables=var_manager)

    # create a fake play context

# Generated at 2022-06-13 08:36:03.319586
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    play_context= PlayContext()
    variables_list = [{'host': 'host'}, None]
    task_list = [{'port': 'port', 'remote_user': 'remote_user', 'become_user': 'become_user', 'delegate_to': 'delegate_to', 'tags': 'tags', 'sudo_user': 'sudo_user', 'become': 'become'}, None]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    variables = variables_list[i]
                    templar = Templar(variables=variables)
                    task = task_list[j]
                    if task is None:
                        task_object = None
                    else:
                        task_object = Task()
                        task

# Generated at 2022-06-13 08:36:11.111029
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():

    # setup test
    host = 'my_host'
    my_task = Task()
    my_task.delegate_to = host
    my_task.remote_user = 'some_user'
    my_vars = dict()
    my_vars[host] = dict()
    my_vars[host]['ansible_user'] = 'some_other_user'
    my_vars[host]['ansible_port'] = 22
    my_vars[host]['ansible_host'] = 'my_host.com'
    my_vars['ansible_connection'] = 'smart'

    # test
    my_play_context = PlayContext()

# Generated at 2022-06-13 08:36:22.549058
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    t = PlayContext()
    t.set_attributes_from_plugin('dummy')

# Generated at 2022-06-13 08:36:31.324020
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # create a dummy task
    task_args = dict(action=dict(module='test'), delegate_to=None, delegate_facts=None, run_once=False, no_log=False, check_mode=False, when=None, loop=None)
    task = Task().load(task_args, variable_manager=None, loader=None)

    # create a playcontext
    context_args = dict(play=None, passwords=None, connection_lockfd=None)
    play_context = PlayContext(**context_args)

    # call the method with a set of default args
    variables = dict()
    templar = Templar(loader=None, variables=variables)
    play_context.set_task_and_variable_override(task, variables, templar)

    orig_values = play_context.copy()



# Generated at 2022-06-13 08:36:45.857163
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    hpc = PlayContext()
    # task not specified
    info = hpc.set_task_and_variable_override(task=None, variables={}, templar=None)
    assert info.force_handlers is False
    assert info.start_at_task == 0
    assert info.step is False
    assert info.timeout is 10
    assert info.verbosity is 0
    assert info.connection_lockfd is None
    assert info.private_key_file == '/path/to/identity'
    assert info.network_os is None
    assert info.remote_addr is None
    assert info.remote_user is 'root'
    assert info.port is 22
    assert info.is_smart is False
    assert info.ssh_executable is None
    assert info.shell is None
    assert info.system_known

# Generated at 2022-06-13 08:36:54.644407
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    test_config_file = "./ansible_module_config.ini"
    config = configparser.ConfigParser()
    config.read(test_config_file)
    
 
    variable_manager = VariableManager()
    variable_manager.extra_vars = {}
    variable_manager._extra_vars = load_extra_vars({'config': config})

    inventory = InventoryManager(loader=None, variable_manager=variable_manager, host_list='./tests_data/hosts_test')
    variable_manager.set_inventory(inventory)

    task = AnsibleTask()
    play = Play()
    play.hosts = 'localhost'

    pc = PlayContext()
    pc.set_attributes_from_play(play)
    pc.set_attributes_from_cli()

    task.delegate

# Generated at 2022-06-13 08:36:56.642950
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    PlayContext.set_attributes_from_plugin(plugin)


# Generated at 2022-06-13 08:37:05.693821
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from ansible_collections.ansible.community.tests.unit import t_module

    pc = PlayContext()

    mock_plugin = t_module.MockPlugin('paramiko', 'network/ios')
    mock_plugin_args = dict(timeout=120, foo='bar')
    mock_plugin.set_options(mock_plugin_args)
    pc.set_attributes_from_plugin(mock_plugin)

    assert pc.timeout is 120
    assert pc.foo == 'bar'


# Generated at 2022-06-13 08:37:06.443564
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    pass



# Generated at 2022-06-13 08:38:35.391445
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    playcontext = PlayContext(play=None, passwords=None, connection_lockfd=None)
    # Set context.CLIARGS with the values
    # ASSUME that this is only used for Python 2.7
    context.CLIARGS = {
        'timeout': 50
    }
    playcontext.set_attributes_from_cli()
    assert playcontext.timeout == 50


# Generated at 2022-06-13 08:38:43.462638
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    # Reset the CLI context, we only want the options we set here (and we need to recreate the object because it can only be instantiated once)
    context.CLIARGS = AttributeDict()

    # Setting within the range of valid values
    context.CLIARGS['timeout'] = 45
    context.CLIARGS['verbosity'] = 3

    # Setting values outside of valid range, should be forced to range
    context.CLIARGS['timeout'] = -1
    context.CLIARGS['verbosity'] = 100

    # Resetting to default values
    context.CLIARGS['timeout'] = None
    context.CLIARGS['verbosity'] = None



# Generated at 2022-06-13 08:38:57.166911
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # SETUP VARS FOR UNIT TESTS
    #############################################################################################
    class MockTask:
        def __init__(self, delegate_to=None, remote_user=None, check_mode=None, diff=None):
            self.delegate_to = delegate_to
            self.remote_user = remote_user
            self.check_mode = check_mode
            self.diff = diff

    class MockConnection:
        def __init__(self):
            self.transport = 'ssh'
            self.connection = 'smart'
            self.remote_addr = '127.0.0.1'
            self.port = None
            self.proxy = None
            self.remote_user = None
            self.timeout = 10
            self.accelerate_port = None
            self.accelerate_ip

# Generated at 2022-06-13 08:39:03.449651
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    """
    Test to set task and variable override
    """
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars import VariableMgr

    p = PlayContext()
    hv = HostVars('127.0.0.1')
    vmgr = VariableMgr(loader=None, inventory=None)
    vmgr.clear_vars_cache()
    vmgr.set_host_variable(host='127.0.0.1', variable=hv)
    variable_manager = VariableManager(loader=None, inventory=None, variable_manager=vmgr)

    t = Task()
    x = p.set_

# Generated at 2022-06-13 08:39:14.245253
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    #
    # PlayContext.set_attributes_from_plugin(plugin)
    #

    # TODO: Remove this test once set_attributes_from_plugin() is removed

    # Set up a test inventory plugin
    class TestInventoryPlugin(InventoryPlugin):

        def __init__(self, inventory, loader, hostlist=None):
            super(TestInventoryPlugin, self).__init__(inventory, loader, hostlist)

        def parse(self, inventory, loader, hosts=None, host_list=None):
            return super(TestInventoryPlugin, self).parse(inventory, loader, hosts, host_list)

    class DummyCLIArgs:
        def __init__(self):
            self.connection = 'smart'
            self.timeout = 5
            self.verbosity = 5

    # Create a fake plugin


# Generated at 2022-06-13 08:39:26.059278
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    p = Play()
    p.vars['ansible_connection'] = 'winrm'
    p.vars['ansible_winrm_server_cert_validation'] = 'ignore'
    p.vars['ansible_winrm_transport'] = 'certificate'

    task = PlaybookExecutor._task_class()()
    task.vars['ansible_port'] = '5963'
    task.vars['ansible_winrm_port'] = 5963
    task.vars['ansible_connection'] = 'winrm'

    pc = PlayContext(play=p)
    pc.set_task_and_variable_override(task=task, variables=p.vars, templar=None)
    assert pc.connection == 'winrm'
    assert pc.port == 5963


# Generated at 2022-06-13 08:39:35.683149
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # Create a PlayContext object with standard key attributes
    playcontext = PlayContext()
    playcontext.set_attributes_from_cli()
    context.CLIARGS['connection'] = 'docker'
    context.CLIARGS['docker_extra_args'] = ["-p 8888:22"]
    playcontext.set_attributes_from_cli()
    # The connection attribute is set to docker
    assert playcontext.connection == 'docker'
    # The docker_extra_args is set to a list of a string.
    # This the value of the attribute in the object
    assert playcontext.docker_extra_args == '-p 8888:22'
    # A PlayContext object is created and the connection attribute is set using the function
    # set_attributes_from_plugin of class PlayContext. This is passed a plugin which has the

# Generated at 2022-06-13 08:39:47.808693
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from ansible.errors import AnsibleError
    mock_plugin = MagicMock()
    mock_plugin._load_name = 'test'
    mock_plugin._attributes = {'_test': None}
    p = PlayContext()

    with patch.object(C.config, 'get_configuration_definitions'):
        with pytest.raises(AnsibleError):
            p.set_attributes_from_plugin(mock_plugin)
        C.config.get_configuration_definitions.return_value = {'test': {'name': '_test'}}
        p.set_attributes_from_plugin(mock_plugin)

    assert p._test is None

# Generated at 2022-06-13 08:39:53.353826
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from ansible.plugins import connection_loader
    connection_plugins = connection_loader.all()
    plugin = [plugin for name, plugin in iteritems(connection_plugins) if name == 'local'][0]
    play = Play()
    play._validate_deprecated_vars()
    play_context = PlayContext(play=play)
    play_context.set_attributes_from_plugin(plugin)
    assert getattr(play_context, 'executable') == '/bin/sh'


# Generated at 2022-06-13 08:39:55.307166
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    p = PlayContext()
    p.set_attributes_from_plugin('shell')

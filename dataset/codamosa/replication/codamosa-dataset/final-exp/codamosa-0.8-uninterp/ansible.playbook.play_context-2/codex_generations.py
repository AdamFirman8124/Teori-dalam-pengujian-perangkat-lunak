

# Generated at 2022-06-13 08:31:33.530099
# Unit test for constructor of class PlayContext
def test_PlayContext():
    play = Play().load(dict(
        name = "Ansible Play",
        hosts = 'webservers',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='raw', args='whoami')),
        ]
    ))

    pc = PlayContext(play=play, passwords={})
    assert pc


# Generated at 2022-06-13 08:31:34.993442
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    PlayContext.set_attributes_from_plugin(self, plugin)

# Generated at 2022-06-13 08:31:42.781021
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    play = Play()
    play.connection = "smart"
    play.force_handlers = True
    task = Task()
    task.connection = "winrm"
    task.remote_user = "test_user"
    task.delegate_to = "test_delegate"
    play_context = PlayContext(play)
    variables = {}
    templar = Templar(loader=None, variables=variables)
    play_context.set_task_and_variable_override(task, variables, templar)
    assert play_context.connection == "winrm"
    assert play_context.remote_user == "test_user"
    assert play_context.delegate_to == "test_delegate"



# Generated at 2022-06-13 08:31:48.577273
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    # Initiate a PlayContext object with its input as a "play"
    with pytest.raises(AssertionError):
        PlayContext(play=None)

    # Initiate a PlayContext object with its input as a "play", and the
    #  inputs for its two variables as "passwords" and "connection_lockfd"
    with pytest.raises(AssertionError):
        PlayContext(play=None, passwords=None, connection_lockfd=None)

    # Create a PlayContext object with its input as a "play"
    play_context_obj = PlayContext(play=None)

    # Create a PlayContext object with its input as a "play" and the
    #  inputs for its two variables as "passwords" and "connection_lockfd"

# Generated at 2022-06-13 08:31:53.476285
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    m = MagicMock(spec=dict)
    pc = PlayContext()
    pc.set_attributes_from_plugin(m)
    assert pc._password == 'conn_pass'
    assert pc._become_pass == 'become_pass'



# Generated at 2022-06-13 08:32:01.322518
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    '''Unit test for method set_task_and_variable_override of class PlayContext'''

    import copy
    import types
    import unittest

    import ansible.constants as C
    import ansible.playbook.play as play
    import ansible.playbook.task as task
    import ansible.playbook.block as block
    import ansible.utils.template as template
    import ansible.vars.manager as vars_manager
    import ansible.vars.hostvars as hostvars

    from ansible.parsing.vault import VaultLib
    from ansible.template import Templar

    class DummyPlay(object):
        ''' Dummy class for play '''
        def __init__(self):
            self.connection = 'ssh'
            self.hosts = ['localhost']

   

# Generated at 2022-06-13 08:32:15.369701
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    import os
    import sys
    import time
    import unittest

    from ansible.constants import DEFAULT_TIMEOUT
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY3
    from ansible.playbook.play_context import PlayContext

    class TestPlayContext(unittest.TestCase):

        def setUp(self):
            self._cleanups = []
            self.pc = PlayContext()

        def tearDown(self):
            for cleanup_func in self._cleanups:
                cleanup_func()


# Generated at 2022-06-13 08:32:17.221987
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # try to set attributes from a plugin
    PlayContext._get_attr_connection()




# Generated at 2022-06-13 08:32:25.854618
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
# Init Fixtures
    config_file = 'test/units/plugins/test_playbook.cfg'
    localhost = Host('localhost')
    task = Task()
    new_info = PlayContext()
    variables = dict()
    templar = Templar()
    localhost.set_variable('ansible_user', 'ansible_user')
# Init
    config = ConfigParser.ConfigParser(defaults=dict(here='.'))
    config.read(config_file)
    C.CONFIG_FILE = config_file
    context.CLIARGS = dict(fork=5, verbosity=2, timeout=23)
    # [defaults]
    # hostfile      = /etc/ansible/hosts
    # library       = /usr/share/ansible
    # module_utils  = /usr/share/ans

# Generated at 2022-06-13 08:32:28.415975
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    obj = PlayContext(play={})

    assert obj is not None


# Generated at 2022-06-13 08:32:49.557325
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from ansible import context
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.plugins import connection_loader, module_loader
    from ansible.utils.vars import combine_vars

    # FIXME: need to mock get_connection_loader and get_module_loader() and context.CLIARGS
    # FIXME: need to mock config and get_config_definitions()

    # set up and return a connection plugin subclass

# Generated at 2022-06-13 08:32:57.730079
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    """
    Test setting attributes with attributes from a plugin
    """
    # Init vars
    play_context = PlayContext()

    # Setup mock plugin
    mocker = patch('insights.client.insights_config.get_plugin_class')
    mock_plugin_class = mocker.start()
    plugin = mock_plugin_class.return_value.return_value
    plugin._load_name = '_load_name'
    plugin.get_option.return_value = '_expected_result'

    # Setup mock config definitions
    mock_config_definitions = {'_option': {'name': '_flag'}}
    mocker = patch('insights.client.insights_config.get_configuration_definitions')
    mock_get_config_definitions = mocker.start()
    mock_get_config

# Generated at 2022-06-13 08:33:00.172542
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    """
    Test setting attributes from plugin
    """

# Generated at 2022-06-13 08:33:02.500580
# Unit test for method update_vars of class PlayContext
def test_PlayContext_update_vars():
    instance = PlayContext()
    variables = {}
    instance.update_vars(variables)

# Generated at 2022-06-13 08:33:04.435597
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():

    class TestPlugin(ConnectionBase):
        pass

    plugin = TestPlugin(play_context=PlayContext())
    plugin.get_option = lambda x: 'test'

    pc = PlayContext()
    pc.set_attributes_from_plugin(plugin=plugin)

    assert getattr(pc, 'test'), "Test attribute not set"


# Generated at 2022-06-13 08:33:05.163433
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    pass

# Generated at 2022-06-13 08:33:14.079762
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    args = ['./ansible-playbook', '-i', 'hosts.ini', '-t', 'tag', 'playbook', '-M', 'modules']
    context.CLIARGS = context.CLI.parse(args)[0]
    passwords = {}
    pc = PlayContext(play=None, passwords=passwords, connection_lockfd=None)

    # set_attributes_from_cli adds the following fields:
    # self.timeout = int(context.CLIARGS['timeout'])
    # self.private_key_file = context.CLIARGS.get('private_key_file')  # Else default
    # self.verbosity = context.CLIARGS.get('verbosity')  # Else default
    # self.start_at_task = context.CLIARGS.get('start_

# Generated at 2022-06-13 08:33:29.481146
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    with patch('ansible.playbook.play_context.C.config.get_configuration_definitions') as m_get_configuration_definitions:
        with patch('ansible.playbook.play_context.get_plugin_class') as m_get_plugin_class:
            with patch('ansible.playbook.play_context.Base') as m_Base:
                with patch('ansible.playbook.play_context.FieldAttribute') as m_FieldAttribute:
                    with patch('ansible.playbook.play_context.PlayContext') as m_PlayContext:
                        # Setup test data
                        # Setup mock objects
                        x_plugin = MagicMock()
                        x_plugin._load_name = 'disk_plugin'
                        m_get_plugin_class.return_value = 'get_plugin_class_result'
                       

# Generated at 2022-06-13 08:33:30.403124
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    pass

# Generated at 2022-06-13 08:33:46.350389
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    context._init_global_context(['ansible'])

    play = Play()

    context.CLIARGS = {'timeout': '60'}
    playcontext = PlayContext(play)

    # Assert that the correct timeout of 60s has been set
    assert playcontext.timeout == 60
    # Assert that the default verbosity of 0 is set
    assert playcontext.verbosity == 0
    # Assert that the default start_at_task is None
    assert playcontext.start_at_task is None

    context.CLIARGS = {'timeout': '60'}
    context.CLIARGS['verbosity'] = '3'
    context.CLIARGS['start_at_task'] = 'task3'
    playcontext = PlayContext(play)

    # Assert that the correct timeout of 60s has

# Generated at 2022-06-13 08:34:17.194355
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.template import Templar
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager,  host_list=[])
    play_context = PlayContext()
    play_source =  dict(
            name = "Ansible Play",
            hosts = 'all',
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module='command', args='ls'))
            ]
        )
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 08:34:27.860779
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    test_file = 'test/test_play.yml'
    test_hosts = 'hosts/test_hosts'
    test_vars = 'test/test_vars.yml'
    test_inventory = Inventory(loader=DataLoader(), sources=test_hosts)
    test_loader = DataLoader()
    test_variable_manager = VariableManager(loader=test_loader, inventory=test_inventory)
    test_play = Play.load(test_file, variable_manager=test_variable_manager, loader=TestLoader())
    test_play_context = PlayContext(play=test_play)
    test_play_context.set_attributes_from_cli()
    task = test_play.tasks[0]
    host = test_inventory.get_host(task.host)
    variables = test_

# Generated at 2022-06-13 08:34:30.967000
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    '''
    Unit test for method set_attributes_from_plugin of class PlayContext
    '''
    # create a PlayContext object and assign attributes to it
    # TODO
    # PC = PlayContext()
    # PC.set_attributes_from_plugin()
    # TODO
    # assert PC.attributes == expected_attributes
    pass

# Generated at 2022-06-13 08:34:32.361899
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    plcontext = PlayContext()
    plugin = object()
    plcontext.set_attributes_from_plugin(plugin)


# Generated at 2022-06-13 08:34:38.111030
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
	self = PlayContext()
	self.set_attributes_from_plugin(plugin)
	assert self.private_key_file == context.CLIARGS.get('private_key_file')
	assert self.verbosity == context.CLIARGS.get('verbosity')
	assert self.start_at_task == context.CLIARGS.get('start_at_task', None)


# Generated at 2022-06-13 08:34:43.342414
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    from test.unit.callback_plugins.test_action_default import TestActionDefaultCallbackModule
    from test.unit.callback_plugins.test_cache import TestCacheCallbackModule
    from test.unit.callback_plugins.test_logger import TestLoggingCallbackModule
    from test.unit.callback_plugins.test_mail import TestMailCallbackModule
    from test.unit.callback_plugins.test_stats import TestAggregateStatsCallbackModule
    from test.unit.callback_plugins.test_timer import TestTimerCallbackModule
    from test.unit.callback_plugins.test_tree import TestTreeCallbackModule
    from test.unit.plugins.loader import DictLoader
    CONN_LOCKFD = 1

# Generated at 2022-06-13 08:34:50.993885
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    context.CLIARGS = dict()
    context.CLIARGS['verbosity'] = None
    context.CLIARGS['private_key_file'] = None
    context.CLIARGS['timeout'] = None
    context.CLIARGS['start_at_task'] = None
    assert not PlayContext().set_task_and_variable_override()
    
    

# Generated at 2022-06-13 08:35:05.579582
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # setup mocks
    fake_play = create_autospec(play.Play)
    fake_variables = {}
    fake_templar = create_autospec(templar.Templar)

    # set up code test
    play_context = PlayContext(play=fake_play)
    play_context.set_task_and_variable_override(task=None, variables=fake_variables, templar=fake_templar)
    play_context.set_task_and_variable_override(task=create_autospec(task.Task), variables=fake_variables, templar=fake_templar)


fake_result = create_autospec(ResultBase)
fake_result.is_changed = False
fake_result.is_failed = False

fake_result_failed

# Generated at 2022-06-13 08:35:06.476834
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    pass


# Generated at 2022-06-13 08:35:15.977767
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    with Context() as ctx:
        ctx.var = {
            'one': {'ansible_port': '22', 'ansible_user': 'jeff', 'ansible_host': '127.0.0.1'},
                'two': {'ansible_port': '33', 'ansible_user': 'jeff', 'ansible_host': '127.0.0.1'}
        }

        pc = PlayContext()
        plugin = {'ansible_port': '33', 'ansible_user': 'jeff', 'ansible_host': '127.0.0.1'}
        pc.set_attributes_from_plugin(plugin)

        assert pc.port == 33
        assert pc.remote_user == "jeff"

# Generated at 2022-06-13 08:35:52.600439
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    context.CLIARGS = ImmutableDict({'verbosity': 0, 'timeout': 10, 'private_key_file': 'file'})
    play_context = PlayContext()
    plugin = object()
    mock_plugin = Mock()
    with patch('ansible.plugins.loader.get_plugin_class', return_value=mock_plugin):
        mock_plugin.get_configuration_definitions.return_value = {'timeout': {'name': 'timeout'}}
        mock_plugin.get_option.return_value = '10'
        play_context.set_attributes_from_plugin(plugin)
        assert play_context.timeout == 10


# Generated at 2022-06-13 08:35:54.192643
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    PlayContext.set_attributes_from_cli()



# Generated at 2022-06-13 08:36:04.992021
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # initialize a barebones plugin

    class test_plugin:
        pass

    p = test_plugin()
    p._load_name = 'p'

    # instantiate a new PlayContext

    pc = PlayContext()

    # set all of the options for the plugin

    for option, default in C.config.get_configuration_definitions(get_plugin_class(p), p._load_name).items():
        if p._load_name == 'netconf' and option == 'hostkey_verify':
            continue
        if option not in ('name', 'options', '_get_config_option'):
            p.set_option(option, 'test')

    # set the attributes on the PlayContext

    pc.set_attributes_from_plugin(p)

    # check to make sure that the PlayContext has all of the options

# Generated at 2022-06-13 08:36:12.087069
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # Setup Ansible structure
    options = {'connection': 'ssh'}
    playbook = 'dummy_playbook_path'
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager,  host_list='tests/inventory')
    variable_manager.set_inventory(inventory)
    passwords = dict()

    # Setup module
    fail_json = MagicMock(return_value={})
    module = MagicMock()
    module.fail_json = fail_json
    module.check_mode = False
    module.no_log = False
    module.params = options

    #  Setup Play

# Generated at 2022-06-13 08:36:24.186320
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    # Test with task.delegate_to is not None
    play_context = PlayContext()
    task = Task()
    task.delegate_to = "localhost"
    task.remote_user = None
    variables = {}
    templar = None

    new_context = play_context.set_task_and_variable_override(task, variables, templar)
    assert new_context.remote_user == "remote_user"

    # Test with task.delegate_to is None
    task.delegate_to = None
    new_context = play_context.set_task_and_variable_override(task, variables, templar)
    assert new_context.remote_user == "remote_user"

# Generated at 2022-06-13 08:36:30.295992
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    expected = 'expected'
    class MockCliArgs:
        def __getitem__(self, name):
            if name == 'timeout':
                return expected
            elif name == 'private_key_file':
                return expected
            else:
                raise KeyError()

    mock_context = MockCliArgs()
    pc = PlayContext()
    pc._set_context(mock_context)
    pc.set_attributes_from_cli()
    assert pc.timeout == expected
    assert pc.private_key_file == expected


# Generated at 2022-06-13 08:36:44.913676
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from ansible.plugins import connection_loader

    play_context = PlayContext()
    local_connection = connection_loader.get('local')
    play_context.set_attributes_from_plugin(local_connection)
    assert play_context._attributes['executable'] == '/bin/sh'
    # check that if we set the attribute of a plugin, this attribute will be overwritten
    local_connection._executable = '/bin/bash'
    assert local_connection._executable == '/bin/bash'
    play_context.set_attributes_from_plugin(local_connection)
    assert play_context._attributes['executable'] == '/bin/bash'

    # check that if we set an attribute of a plugin not in the configuration definition, it will not be set

# Generated at 2022-06-13 08:36:50.410817
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    """ test setting attributes from plugin.
    """
    # create a plugion
    plugin = {}

    # create a playcontext instance with no data
    pc = PlayContext()

    # set attributes from plugin
    pc.set_attributes_from_plugin(plugin)

    # assert playcontext attributes
    assert pc._verbosity == 0
    assert pc._private_key_file == '/path/to/file'

# Generated at 2022-06-13 08:37:05.199212
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # create the object instance
    p = PlayContext()

    #
    # Testing set_attributes_from_plugin
    #
    #  - TODO

    #
    # Testing set_attributes_from_play
    #
    #  - TODO

    #
    # Testing set_attributes_from_cli
    #
    #  - TODO

    #
    # Testing set_task_and_variable_override
    #
    #  - TODO

    #
    # Testing set_become_plugin
    #
    #  - TODO

    #
    # Testing update_vars
    #
    #  - TODO

    #
    # Testing _get_attr_connection
    #
    #  - TODO

    return True

#

# Generated at 2022-06-13 08:37:09.417943
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    my_play = Play()
    my_play_context = PlayContext(play=my_play)
    my_play_context.set_attributes_from_plugin(my_class)
    assert my_play_context.attributes is not None


# Generated at 2022-06-13 08:38:00.925410
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # This method is used complicated, so it is hard to write unit test, the method will be modified in future.
    pass

# Generated at 2022-06-13 08:38:02.730943
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # FIXME: Check if the function is working
    pass

# Generated at 2022-06-13 08:38:11.171081
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    """
    Test the method PlayContext.set_attributes_from_plugin
    """

    # The arguments have already been mocked, so we don't need to pass values in
    # the call to set_attributes_from_plugin.

    # Create a mock PlayContext instance.
    pcontext = PlayContext()

    # Create a mock options dictionary.
    options = dict()

    # Perform the method call and assert that the value returned is as expected.
    assert pcontext.set_attributes_from_plugin(options) is None

# Generated at 2022-06-13 08:38:11.803613
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    assert True == True

# Generated at 2022-06-13 08:38:18.870605
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    play = MagicMock(spec=Play)
    variables = {
        'connection_variable': '',
        'ansible_connection': 'ssh',
        'ansible_user': 'saksham',
        'ansible_ssh_host': '127.0.0.1',
        'ansible_ssh_port': '2022',
        'ansible_ssh_pass': 'geektrust',
        'ansible_ssh_user': 'saksham'
    }
    templar = MagicMock(spec=Templar)
    task = MagicMock(spec=Task)
    p = PlayContext(play=play, passwords=variables, connection_lockfd=None)
    p.set_attributes_from_cli()
    p.set_attributes_from_play(play)
    p

# Generated at 2022-06-13 08:38:24.475992
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    """
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.action.network import ActionModule as networkActionModule
    from ansible.plugins.loader import get_plugin_class
    options = C.config.get_configuration_definitions(get_plugin_class(networkActionModule), 'action')
    print options
    {'use_ssl': {'name': 'use_ssl', 'type': 'bool', 'default': True, 'desc': 'Use SSL for the connection.'}, 'validate_certs': {'name': 'validate_certs', 'type': 'bool', 'default': True, 'desc': 'Validate certs.'}}
    """
    #setup test

# Generated at 2022-06-13 08:38:36.938345
# Unit test for method set_attributes_from_cli of class PlayContext

# Generated at 2022-06-13 08:38:44.697488
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    args = dict(connection='local', verbosity=5)
    context.CLIARGS = argparse.Namespace(**args)
    play_context = PlayContext()
    play_context.set_attributes_from_cli()
    assert play_context._attributes['connection'] == 'local'
    assert play_context._attributes['verbosity'] == 5
    #Test the private_key_file is set to default
    assert play_context._attributes['private_key_file'] == C.DEFAULT_PRIVATE_KEY_FILE
    args = dict(timeout=10)
    context.CLIARGS = argparse.Namespace(**args)
    play_context = PlayContext()
    play_context.set_attributes_from_cli()
    assert play_context._attributes['timeout'] == 10

#

# Generated at 2022-06-13 08:38:50.738746
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    context = PlayContext()

    context.set_attributes_from_cli()
    assert context.private_key_file == '/path/to/file'
    assert context.timeout == 10
    assert context.verbosity == 3
    assert context.start_at_task == 'another_task'



# Generated at 2022-06-13 08:39:00.186528
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    p = PlayContext()
    plugin = Mock()
    plugin.get_option.return_value = "my_value"
    options = {"my_option_name" : {"name" : "my_option_name"}}
    with patch("ansible.config.get_configuration_definitions", return_value=options):
        p.set_attributes_from_plugin(plugin)
    assert p._attributes["my_option_name"] == "my_value"
    plugin.get_option.assert_called_with("my_option_name")

# Generated at 2022-06-13 08:40:44.429937
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    my_p = PlayContext()
    #my_p.set_attributes_from_plugin(plugin)
    assert my_p.get_attributes() == {}


# Generated at 2022-06-13 08:40:55.506207
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():

    from ansible.plugins import connection_loader

    class TestConnection(ConnectionBase):
        add_args_from_plugin = ['from_plugin']

        def __init__(self, play_context, new_arg, *args, **kwargs):
            self.has_pipelining = False
            super(TestConnection, self).__init__(play_context, new_arg, *args, **kwargs)

        def connect(self, port=None, **kwargs):
            pass


    connection_loader.add('test_connection', TestConnection, 'test_connection', False)
    connection_loader.add('test_connection', TestConnection, 'test_connection', True)

    pc = PlayContext()
    pc.set_attributes_from_plugin('test_connection')
    assert pc.from_plugin is True


# Unit test

# Generated at 2022-06-13 08:41:03.440272
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    '''
    Test for method set_task_and_variable_override of class PlayContext
    '''
    play = get_play()
    connection = PlayContext(play=play)
    task = get_task()
    variables = dict()
    templar = get_templar()
    connection.set_task_and_variable_override(task, variables, templar)

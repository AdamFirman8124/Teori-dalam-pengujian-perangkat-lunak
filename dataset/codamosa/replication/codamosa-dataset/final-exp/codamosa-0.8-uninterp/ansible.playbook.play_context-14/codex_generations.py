

# Generated at 2022-06-13 08:31:48.197185
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    class FakeTask(object):
        pass

    class FakeTemplar(object):
        def __init__(self, variables):
            self.variables = variables
        
        def template(self, value):
            return value.replace('{{ ', '').replace(' }}', '')

    # Arrange
    hostvars = dict()
    hostvars['ansible_ssh_pass'] = 'ssh'
    hostvars['ansible_port'] = 22
    hostvars['ansible_user'] = 'ansible-user'
    hostvars['ansible_host'] = 'host'
    hostvars['ansible_connection'] = 'ssh'

    context.CLIARGS = dict()
    context.CLIARGS['verbosity'] = 5  # to avoid invalid default

    play = FakeTask()
    play

# Generated at 2022-06-13 08:31:51.678328
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
      test_PlayContext_obj = PlayContext()
      assert type(test_PlayContext_obj) is not None

# Generated at 2022-06-13 08:31:54.035057
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    connection = Connector(None, None, None)
    connection.set_attributes_from_plugin("paramiko")
    connection.set_attributes_from_plugin("netconf")

# Generated at 2022-06-13 08:32:05.983911
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    pc = PlayContext()
    pc.set_attributes_from_cli()

    task = Task()
    task._uuid = "test_uuid"
    task.sudo = "test_sudo"
    task.sudo_user = "test_sudo_user"
    task.su = "test_su"
    task.su_user = "test_su_user"
    task.run_once = "test_run_once"
    task.remote_user = "test_remote_user"


# Generated at 2022-06-13 08:32:10.334489
# Unit test for constructor of class PlayContext
def test_PlayContext():

    # Verify constructor of class PlayContext
    context = PlayContext()
    assert context.become is False
    assert context.become_method is None
    assert context.become_user is None
    assert context.verbosity == 0



# Generated at 2022-06-13 08:32:16.613796
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    options = C.config.get_configuration_definitions(get_plugin_class(connection_loader.get('docker', class_only=True)), 'docker')

    assert options

    new_context = PlayContext()
    new_context.set_attributes_from_plugin('docker')

    assert new_context._docker_extra_args



# Generated at 2022-06-13 08:32:25.387053
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    testcase = unittest.TestCase()

    # test without fail
    # create an instance of PlayContext() class
    pc1 = PlayContext(play=None, passwords=None, connection_lockfd=None)

    option_pass_inactive_timeout = C.config.configuration.Option(
        name='pass_inactive_timeout',
        default=None,
        type='string',
        section='ssh_connection',
        description='seconds of inactivity before a password prompt times out',
        ini=False,
        env=False,
        vars=False,
    )

# Generated at 2022-06-13 08:32:39.524317
# Unit test for constructor of class PlayContext
def test_PlayContext():
    '''
    This is intended to be a unit test of the constructor of the PlayContext
    class.  The only real thing here is to ensure that defaults are assigned
    correctly.

    Tests for methods of the PlayContext class are NOT included here.
    '''
    pc = PlayContext()

    assert pc.connection == 'smart'
    assert not pc._become
    assert pc._become_method == 'sudo'
    assert pc._become_user == 'root'
    assert not pc._become_pass
    assert not pc._become_exe
    assert not pc._become_flags
    assert len(pc._become_plugin) == 0
    assert pc._remote_addr is None
    assert not pc._remote_user
    assert not pc._password
    assert pc._port is None
    assert not pc._private_key_

# Generated at 2022-06-13 08:32:44.324324
# Unit test for method set_attributes_from_plugin of class PlayContext

# Generated at 2022-06-13 08:32:53.160292
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    import ansible
    from ansible import context
    from ansible.module_utils.common.collections import ImmutableDict
    context.CLIARGS = ImmutableDict({'timeout': 57, 'private_key_file': '/home/vagrant/ansible', 'verbosity': 5})
    pc = PlayContext()
    if pc._timeout != 57:
        raise Exception('failed to set timeout from CLI')
    if pc._private_key_file != '/home/vagrant/ansible':
        raise Exception('failed to set private_key_file from CLI')
    if pc._verbosity != 5:
        raise Exception('failed to set verbosity from CLI')


# Generated at 2022-06-13 08:33:15.555287
# Unit test for constructor of class PlayContext
def test_PlayContext():

    # ConnectionInfo object
    context = PlayContext()
    assert context is not None


# Generated at 2022-06-13 08:33:27.252692
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    import pytest
    from unittest.mock import patch
    from ansible.parsing.vault import VaultLib
    import ansible.template
    class Host:
        name=None
    host = Host()
    host.vars = dict()
    host.name = 'host1'
    host.vars['ansible_connection'] = 'smart'
    host.vars['ansible_user'] = 'testuser'
    host.vars['ansible_host'] = 'host1.example.com'
    host.vars['ansible_port'] = 22
    host.vars['ansible_ssh_user'] = 'testuser'
    host.vars['ansible_ssh_pass'] = 'password'
    host.vars['ansible_ssh_extra_args'] = ''

# Generated at 2022-06-13 08:33:30.587824
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    class FakeModule(object):
        def get_option(self, x):
            return ""
    module = FakeModule()
    pc = PlayContext()
    pc.set_attributes_from_plugin(module)

# Generated at 2022-06-13 08:33:43.190960
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    delegate_to = 'fake_host'
    remote_user = 'fake_user'
    task = None
    variables = None
    templar = None
    play = None
    passwords = None
    connection_lockfd = None
    
    playcontext = PlayContext(play = play, passwords = passwords, connection_lockfd = connection_lockfd)
    playcontext.set_attributes_from_cli()
    playcontext.set_attributes_from_play(play)
    playcontext.set_task_and_variable_override(task = task, variables = variables, templar = templar)
    playcontext.set_become_plugin(plugin = None)
    playcontext.update_vars(variables = variables)
    playcontext.copy()

# Generated at 2022-06-13 08:33:56.811865
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():

    args = []
    kwargs = {}

    context = PlayContext()

    context.set_attributes_from_cli()
    assert context.as_dict() == {"verbosity": 0,
                                 "private_key_file": C.DEFAULT_PRIVATE_KEY_FILE}

    context = PlayContext()

# Generated at 2022-06-13 08:33:57.482020
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    pass

# Generated at 2022-06-13 08:33:58.474015
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    return


# Generated at 2022-06-13 08:34:09.424248
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    import ansible.plugins.connection

    play = lambda: None
    play.force_handlers = False
    play.become_method = 'sudo'
    play.become_user = 'root'
    play.vars = dict(ansible_connection='local')
    play_context = PlayContext(play)
    plugin = ansible.plugins.connection.local.ConnectionModule()
    play_context.set_attributes_from_plugin(plugin)
    assert play_context.connection == 'local'
    assert play_context.become_method is None
    assert play_context.become_user is None


# Generated at 2022-06-13 08:34:18.508847
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # idempotent test
    p = Play().load({'name': 'test', 'hosts': 'all', 'task': [{'name': 'foo', 'connection': 'local'}]}, variable_manager=VariableManager(), loader=DictDataLoader())
    t = p.get_task_by_name('foo')
    pc = PlayContext(p, passwords={'vault_password': 'secret'})
    pc.update_vars({'ansible_connection': 'local'})
    res = pc.set_task_and_variable_override(t, {'ansible_connection': 'local'}, Templar(variables={}))
    assert res._attributes['connection'] == 'local'
    assert res._attributes['connection_user'] == res._attributes['remote_user']

# Generated at 2022-06-13 08:34:28.290284
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    c = PlayContext()
    d = PlayContext()
    e = PlayContext()
    f = PlayContext()
    g = PlayContext()
    h = PlayContext()
    i = PlayContext()
    j = PlayContext()
    k = PlayContext()
    l = PlayContext()
    m = PlayContext()

    # set attributes from play
    c.set_attributes_from_play("play")
    a = c.copy()

    # set other attributes
    c.become = False
    c.become_method = 'become_method'
    c.become_user = 'become_user'
    c.become_pass = 'become_pass'
    c.prompt = 'prompt'
    c.connection_lockfd = None
    c.ssh_key = 'ssh_key'

# Generated at 2022-06-13 08:34:43.135172
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    PlayContext(play=None, passwords=None, connection_lockfd=None)
    PlayContext.set_task_and_variable_override(task=None, variables=None, templar=None)

# Generated at 2022-06-13 08:34:56.918911
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    task = FakeAnsibleTask()
    variables = {}
    templar = FakeTemplar()
    play_context = PlayContext()
    play_context.set_task_and_variable_override(task, variables, templar)
    assert play_context.remote_user == 'root'
    assert play_context.port == 22
    assert play_context.host_string == '127.0.0.1'
    assert play_context.connection == 'ssh'
    assert play_context.timeout == 10
    assert play_context.executable == '/usr/bin/python'
    task = FakeAnsibleTask(facts = { 'ansible_port': 1234 })
    play_context = PlayContext()
    play_context.set_task_and_variable_override(task, variables, templar)


# Generated at 2022-06-13 08:34:59.520799
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    '''
    Unit test for set_attributes_from_plugin
    '''
    pass



# Generated at 2022-06-13 08:35:08.767041
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    module_name = 'com.github.ansible.test.ansible.modules.test_play_context.test_PlayContext_set_attributes_from_plugin'
    module_args = ''

    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # These are the module parameters, the values will be set from the test case
    module.params = {}

    # This is the object that will be tested
    pc = PlayContext()
    pc.set_attributes_from_plugin(AnsibleModule(argument_spec=dict(
        a=dict(type='str'),
        b=dict(type='str'),
        c=dict(type='str'),
        d=dict(type='str'),
    )))

# Generated at 2022-06-13 08:35:10.080046
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    play_context = PlayContext()
    play_context.set_attributes_from_plugin("test")


# Generated at 2022-06-13 08:35:18.385529
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # Create an instance of ansible.executor.PlayContext
    module = ansible.executor.PlayContext()

    # Create an instance of ansible.plugins.loader.ConnectionLoader
    plugin = ansible.plugins.loader.ConnectionLoader()

    # set options for plugins by calling set_attributes_from_plugin
    module.set_attributes_from_plugin(plugin)

    # assert the created instance is an instance of ansible.executor.PlayContext
    assert isinstance(module, ansible.executor.PlayContext)


# Generated at 2022-06-13 08:35:28.336171
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # create a fake instance, with fake data from a plugin
    plugin_data = dict(argument_spec = dict(
        first_var = dict(name='first_flag'),
        second_var = dict(name='second_flag'),
        third_var = dict(name='third_flag'),
        fourth_var = dict(name='fourth_flag')
    ))

    class FakePlugin(object):
        _load_name = 'fake_plugin'
        def __init__(self, an_option=None, another_option=None, third_option=None, fourth_option=None):
            self.first_var = an_option
            self.second_var = another_option
            self.third_var = third_option
            self.fourth_var = fourth_option
        def get_option(self, key=None):
            return

# Generated at 2022-06-13 08:35:40.682213
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from ansible.module_utils.connection import Connection
    from yaml.constructor import ConstructorError

    play_context = PlayContext()

    # Bad option_keys in options
    plugin_name = 'test_plugin'
    options = {'test_option': {'test_key': 'test_value'}}
    plugin = Connection(play_context, plugin_name, options)

    with pytest.raises(Exception, match="option_keys in options must be one of.*") as e:
        play_context.set_attributes_from_plugin(plugin)

    # Bad type of option_key
    plugin_name = 'test_plugin'
    options = {'option_keys': 123}
    plugin = Connection(play_context, plugin_name, options)


# Generated at 2022-06-13 08:35:50.820025
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():

    #must call setup_loader before any Ansible plugins are loaded
    setup_loader()

    # prepare test data
    global_vars = dict()
    host_vars = dict()
    inventory = dict()
    vars_manager = VarsManager(loader=None)

    # task obj
    display.verbosity = 2 # this will display debug msg
    task = Task()
    task.action = 'setup'
    task.register = 'shell'
    task.args = None
    task.delegate_to = None
    task.tags.add('setup')
    task.args = dict(gather_subset='all', gather_timeout=10)

    # ansible connection plugin
    class Plugin:

        def __init__(self):
            self._load_name = 'win_ping.ps1'
            self._options

# Generated at 2022-06-13 08:36:01.858085
# Unit test for constructor of class PlayContext
def test_PlayContext():
    passwords = {
        "conn_pass": "pass1",
        "become_pass": "pass2"
    }
    pc = PlayContext(passwords=passwords)
    assert pc.password == "pass1"
    assert pc.become_pass == "pass2"
    assert pc._become_plugin is None
    assert pc._attributes.get('password', None) is None
    assert pc._attributes.get('become_pass', None) is None
    assert pc.prompt == ''
    assert pc.success_key == ''
    assert pc.connection_lockfd is None
    assert pc._attributes.get('force_handlers', False) is False
    assert pc.force_handlers is False

    # Test default values
    assert pc.timeout == C.DEFAULT_TIMEOUT

# Generated at 2022-06-13 08:36:26.252848
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    pass

# Generated at 2022-06-13 08:36:29.837098
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    PlayContext().set_task_and_variable_override({"connection": "local"}, {"ansible_connection": 'local', "ansible_port": 22}, None)

# Generated at 2022-06-13 08:36:37.037779
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    runner = PlayContext()
    assert runner._pipelining is None
    class FakePlugin(object):
        def __init__(self):
            self.pipelining = 1
    runner.set_attributes_from_plugin(FakePlugin())
    assert runner._pipelining == 1

### module tests
# TODO: find a better way to test properly this class and the class ConnectionInformation

# Generated at 2022-06-13 08:36:47.788217
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    context_manager = injector.make('context')
    play = Play()
    passwords = {}
    connection_lockfd = None
    instance = PlayContext(play, passwords, connection_lockfd)


# Generated at 2022-06-13 08:36:48.410709
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    pass

# Generated at 2022-06-13 08:37:03.080816
# Unit test for constructor of class PlayContext
def test_PlayContext():
    context = PlayContext()
    assert isinstance(context, PlayContext)
    assert context.timeout == C.DEFAULT_TIMEOUT
    assert context.connection == 'smart'
    assert context.remote_addr == C.DEFAULT_REMOTE_ADDR
    assert context.remote_user == C.DEFAULT_REMOTE_USER
    assert context.port == C.DEFAULT_REMOTE_PORT
    assert context.private_key_file == C.DEFAULT_PRIVATE_KEY_FILE
    assert context.verbosity == 0
    assert context.check_mode == False
    assert context.no_log is None
    assert context.only_tags == set()
    assert context.skip_tags == set()
    assert context.start_at_task == None
    assert context.force_handlers == False
    assert context.step is False

# Generated at 2022-06-13 08:37:14.775939
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    context = PlayContext()
    # Give some values to attributes of class PlayContext
    context.port = 123
    context.remote_user = 'expected'
    context.become = True
    context.no_log = False
    context.check_mode = False
    context.diff = True
    context.start_at_task = 'expected'
    context.verbosity = 2
    context.private_key_file = 'expected'
    context.timeout = 10
    context.connection_user = 'expected'
    context.force_handlers = True
    context.become_method = 'expected'
    context.become_user = 'expected'
    context.become_pass = 'expected'
    context.pipelining = False
    context.executable = 'expected'
    context.only_tags = 'expected'
   

# Generated at 2022-06-13 08:37:24.526499
# Unit test for constructor of class PlayContext
def test_PlayContext():
    from units.mock.loader import DictDataLoader

    # test constructor
    play_context = PlayContext()

    # test set_attributes_from_play
    play_context.set_attributes_from_play(dict())

    # test passwords
    _password = {'conn_pass': 'test_password'}
    play_context = PlayContext(passwords = _password)
    assert play_context.password == 'test_password'

    # test set_attributes_from_play and set_attributes_from_task
    task = dict(
        delegate_to = 'test_delegate',
        remote_user = 'test_user',
        port = 'test_port',
    )
    play_context = PlayContext()
    play_context.set_attributes_from_play(task)
    play_

# Generated at 2022-06-13 08:37:27.495226
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    PlayContext.set_task_and_variable_override(task, variables, templar)


# FIXME: remove this?

# Generated at 2022-06-13 08:37:34.600052
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    args = dict(
        ansible_connection="ansible.netcommon.network_cli",
        ansible_network_os="ios",
        ansible_options="",
    )
    plugin = Connection(args)
    play_context = PlayContext(password="pass", passwords={'conn_pass': 'pass'})
    play_context.set_attributes_from_plugin(plugin)
    assert play_context.connection == 'ansible.netcommon.network_cli'
    assert play_context.network_os == 'ios'
    assert play_context.options == ''

# Generated at 2022-06-13 08:38:26.216875
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    pass

# Generated at 2022-06-13 08:38:40.789869
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    attrs_to_set = {
      '_network_os': '_network_os',
      '_docker_extra_args': '_docker_extra_args',
    }

    class FakeOptions(object):
        pass
    class FakePlugin(object):
        def __init__(self):
            self.options = FakeOptions()
            self.options.name = 'name'
            self.options._load_name = '_load_name'
            self.options._load_prio = '_load_prio'
            self._load_name = '_load_name'
            self._loaded_by = '_loaded_by'
            self._play_context = PlayContext()
            for (option, attr) in attrs_to_set.items():
                setattr(self.options, option, option)
               

# Generated at 2022-06-13 08:38:56.083768
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    # Testing setting attributes from the cli
    class MockCLIARGS(dict):
        def __getattr__(self, attr):
            return self[attr]
    cli = MockCLIARGS()

    # Test default timeout and private_key_file
    cli['timeout'] = False
    pc = PlayContext()
    pc.set_attributes_from_cli()
    assert pc.timeout == C.DEFAULT_TIMEOUT
    assert pc.private_key_file == C.DEFAULT_PRIVATE_KEY_FILE

    # Test non-default timeout and private_key_file
    cli['timeout'] = 23
    cli['private_key_file'] = 'my_key_file'
    pc = PlayContext()
    pc.set_attributes_from_cli()
    assert pc.timeout == 23

# Generated at 2022-06-13 08:39:02.467355
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    plugin = create_connection()
    plugin_options = {'host_key_checking': True, 'ansible_host': 'localhost', 'ansible_port': 1234, 'ansible_connection': 'local'}
    for option in plugin_options:
        plugin.set_option(option, plugin_options[option])

    pc = PlayContext()
    # test set_attributes_from_plugin()
    pc.set_attributes_from_plugin(plugin)
    assert pc.host_key_checking == plugin_options['host_key_checking'], "host_key_checking is not set correctly"
    assert pc.remote_addr == plugin_options['ansible_host'], "remote_addr is not set correctly"

# Generated at 2022-06-13 08:39:13.779553
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # Setup play
    fake_loader = DictDataLoader({
        "test.yml": """
        - hosts: localhost
          gather_facts: no
          tasks:
          - ping:
        """
    })
    fake_inventory = Inventory(loader=fake_loader,
                               variable_manager=VariableManager(),
                               host_list='localhost')
    my_play = Play().load(play_source="test.yml",
                          variable_manager=fake_inventory.get_variable_manager(),
                          loader=fake_loader)
    # Setup play context
    my_play_context = PlayContext(play=my_play)
    # Setup task
    my_task = Task()
    my_task._role = None  # this is needed to test a special condition in the method

# Generated at 2022-06-13 08:39:17.468102
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # Run unit test for class PlayContext.set_task_and_variable_override
    # FIXME: Implement this!
    raise NotImplementedError()

# Generated at 2022-06-13 08:39:27.380290
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    from ansible.module_utils import basic
    from ansible.module_utils.connection import Connection as _Connection
    from ansible.module_utils.connection import ConnectionError
    from ansible.module_utils.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    class ConnectionMock(_Connection):
        def connect(self, params, **kwargs):
            pass

        def exec_command(self, cmd, **kwargs):
            pass

        def set_host_overrides(self, host, var_options=dict()):
            pass


# Generated at 2022-06-13 08:39:30.053555
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # Check that we can set the attributes from the plugin

    # TODO
    pass


# Generated at 2022-06-13 08:39:45.296428
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
  from ansible.utils.display import Display
  from ansible.module_utils.basic import AnsibleModule, get_exception
  from ansible.module_utils._text import to_bytes, to_native
  from ansible.module_utils.parsing.convert_bool import boolean
  from ansible.module_utils.six.moves import shlex_quote
  from ansible.module_utils.connection import Connection, ConnectionError, ConnectionFailure
  from ansible.playbook.play_context import PlayContext
  import json
  import pytest
  from collections import namedtuple, Mapping
  # AnsibleModule test object
  class AnsibleModule_fake(object):
    def __init__(self, *args, **kwargs):
      self.params = kwargs

# Generated at 2022-06-13 08:39:53.739086
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    print("")
    print("###### test_PlayContext_set_task_and_variable_override ######")
    print("")

    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)

    inventory = Inventory(loader=loader)
    inventory.add_host(Host('test_host'))
    variable_manager.set_inventory(inventory)

    # set task
    task = Task()
    task.remote_user = 'root'

    # set variable_manager
    variable_manager.extra_vars = {"ansible_user": "default_user"}

    # set templar
    templar = Templar(loader=loader, variables=variable_manager.get_vars(play=Play().load(dict(), variable_manager=variable_manager)))
    templar._available_variables = variable
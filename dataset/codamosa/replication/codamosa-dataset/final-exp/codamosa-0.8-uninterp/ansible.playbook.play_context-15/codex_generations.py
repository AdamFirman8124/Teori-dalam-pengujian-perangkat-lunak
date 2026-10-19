

# Generated at 2022-06-13 08:31:50.870507
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # PlayContext set_task_and_variable_override() requires a real task object

    # Basic usage
    """
    pc = PlayContext(play=play, passwords=passwords)
    pc.set_task_and_variable_override(task=task, variables=variables)
    """

    # Advanced usage
    """
    pc = PlayContext(play=play, passwords=passwords)
    pc.set_task_and_variable_override(task=task, variables=variables, templar=templar)
    """

    pass

# Generated at 2022-06-13 08:31:56.616005
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # Case 1:
    # Check if method works as expected when no task and
    # variables are given

    # initialization
    play_context = PlayContext()
    variables = {}

    # execution
    _ = play_context.set_task_and_variable_override(None, variables, None)

    # verification
    assert True

    # Case 2:
    # Check if method works as expected when task and
    # variables are given.

    # initialization
    play_context = PlayContext()
    variables = {}
    variables['ansible_user'] = 'vagrant'
    variables['ansible_host'] = '192.168.1.1'
    variables['ansible_port'] = 22

    # execution

    # variables is not going to change after execution of
    # set_task_and_variable_override
    play_

# Generated at 2022-06-13 08:31:59.024262
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    pass
# END unit test for method set_attributes_from_cli of class PlayContext


# Generated at 2022-06-13 08:32:12.763771
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    play_context = PlayContext()
    class DummyPlugin():
        def get_option(self, name):
            return name

    dummy_plugin = DummyPlugin()
    play_context.set_attributes_from_plugin(dummy_plugin)

    obj = play_context
    call_setter('connection', obj, 'conn_type')
    obj.set_attributes_from_plugin(dummy_plugin)
    assert obj._connection

    call_setter('network_os', obj, 'network_os')
    obj.set_attributes_from_plugin(dummy_plugin)
    assert obj._network_os

    call_setter('become', obj, True)
    obj.set_attributes_from_plugin(dummy_plugin)


# Generated at 2022-06-13 08:32:15.009322
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    '''
    Unit test for method set_task_and_variable_override
    of class PlayContext
    '''
    pass

# Generated at 2022-06-13 08:32:17.637834
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():

    my_PlayContext_obj = PlayContext()
    my_PlayContext_obj.set_attributes_from_plugin(my_PlayContext_obj)

# Generated at 2022-06-13 08:32:24.496140
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    play = Play()
    play.load(dict(name="the play",
                   hosts = ['myhost'],
                   gather_facts='no'))
    # TODO: how to mock this?
    # play._variable_manager = MagicMock()
    p = PlayContext(play=play)
    plugin = Mock()
    plugin.get_option.return_value = "value"
    plugin.DEFAULT_PORT = 100
    p.set_attributes_from_plugin(plugin)
    assert p._port == 100
    plugin.get_option.assert_called_with("port")


# Generated at 2022-06-13 08:32:39.159281
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    _host_vars = {'ansible_host': 'localhost', 'ansible_port': 22, 'ansible_user': 'vagrant', 'ansible_ssh_pass': 'vagrant'}
    _task = MagicMock()
    _task.connection = ''
    _task._role_params = dict()
    _task.delegate_to = ''

    _task.become = False
    playcontext_obj = PlayContext(passwords=dict())
    playcontext_obj.set_attributes_from_plugin(get_plugin_class('Connection')())
    assert playcontext_obj.remote_user == 'vagrant'
    assert playcontext_obj.remote_addr == 'localhost'
    assert playcontext_obj.port == 22

    _task.connection = 'winrm'

# Generated at 2022-06-13 08:32:50.322553
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    import unittest

    class TestPlayContext(unittest.TestCase):
        class A(object):
            pass

        class B(object):
            pass

        class C(object):
            pass

        def setUp(self):
            self.a = self.A()
            self.b = self.B()
            self.c = self.C()

            self.a.b = self.b
            self.b.c = self.c


# Generated at 2022-06-13 08:32:58.104922
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    
    # Create an instance of PlayContext
    context = PlayContext()

    # Create a play to set attributes from
    play = Play.load(dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='debug', args=dict(msg='{{ansible_eth0.ipv4.address}}')))
        ]
    ), variable_manager=VariableManager(), loader=None)

    # Create a Host to set attributes from
    host = Host(name="foobar")
    host.vars = dict()

    #

# Generated at 2022-06-13 08:33:28.144116
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    class MockTemplar(object):

        def __init__(self):
            pass

        def template(self, delegate_to):
            return delegate_to

    class MockTask(Task):

        def __init__(self):
            Task.__init__(self)
            self.delegate_to = "localhost"
            self.remote_user = "foo"

    class MockPlayContext(PlayContext):
        def __init__(self):
            PlayContext.__init__(self)
            self.remote_user = "foo"
            self.port = None


# Generated at 2022-06-13 08:33:29.797268
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    play_context = PlayContext()
    play_context.set_attributes_from_plugin('plugin')


# Generated at 2022-06-13 08:33:45.631272
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    ### Unit test for method PlayContext.set_attributes_from_plugin
    #   This method is used to configure properties on PlayContext instances which are typically
    #   used in setting up a connection.
    #   Because the method uses get_plugin_class and _load_name to get the plugin class, this test
    #   only exercises the code path using the 'local' plugin.  Even so, it does test the calling
    #   function and the call into ansible/config.py for the plugin options.

    # create a new PlayContext instance
    p = PlayContext()

    # get the connection plugin class
    plugin_class = get_plugin_class('connection', 'local')

    # create an instance of the connection plugin
    plugin = plugin_class()

    # call the method under test
    p.set_attributes_from_plugin(plugin)

# Generated at 2022-06-13 08:33:58.298572
# Unit test for constructor of class PlayContext

# Generated at 2022-06-13 08:34:08.901269
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # test with non-existing plugin
    test_playcontext = PlayContext()
    test_playcontext.set_attributes_from_plugin("notapugin")
    # test with existing plugin
    test_playcontext = PlayContext()
    test_playcontext.set_attributes_from_plugin("command")
    # test with existing plugin
    test_playcontext = PlayContext()
    test_playcontext.set_attributes_from_plugin("shell")
    # both plugins have 'chdir' option, so we can check if it is also set
    assert test_playcontext.chdir is None


# Generated at 2022-06-13 08:34:18.292126
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    attr_file_name = 'test_playcontext_attr.json'
    if os.path.exists(attr_file_name):
        os.remove(attr_file_name)

    play = MagicMock()
    p = PlayContext(play)
    cmd_line_args = dict()
    cmd_line_args['start_at_task'] = False
    cmd_line_args['verbosity'] = False
    cmd_line_args['check'] = False
    cmd_line_args['force_handlers'] = False
    cmd_line_args['private_key_file'] = "test_data/private_key"
    cmd_line_args['timeout'] = False
    with patch.dict(ansible.utils.context.CLIARGS, cmd_line_args):
        p.set_attributes_

# Generated at 2022-06-13 08:34:27.063323
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    p = Play()
    c = PlayContext(play=p)
    p.remote_user = "max"
    p.port = 1234
    p.connection = "local"
    p.become = True
    p.become_method = "sudo"
    p.become_user = "sudo_user"
    p.become_pass = "abc"
    p.become_exe = "/bin/true"
    p.become_flags = "--ask-sudo-pass"
    p.prompt = ""
    p.verbosity = 1
    p.no_log = False
    p.check_mode = False
    p.diff = False
    p.start_at_task = None
    p.force_handlers = False
    p.step = False
    p.private_key_file

# Generated at 2022-06-13 08:34:39.181305
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    class CliArgs(object):
        def __init__(self):
            self.verbosity = None
            self.timeout = None
            self.private_key_file = None
            self.start_at_task = False

    class InventoryVariable(object):
        def __init__(self, host_name):
            self.host_name = host_name
            self.get_vars = MagicMock(return_value=self)
            self.get_host = MagicMock(return_value=self)
            self.get = MagicMock()
            self.items = MagicMock()

    class Runner(object):
        def __init__(self):
            self.host_name = 'host_name'
            self.inventory = MagicMock(return_value=InventoryVariable(self.host_name))


# Generated at 2022-06-13 08:34:52.209900
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    '''
    Unit test for method set_attributes_from_plugin
    '''
    from ansible.plugins.loader import get_all_plugin_loaders

    # This should find the plugin in the resource_modules directory
    plugin_name = 'network_cli'
    plugins = get_all_plugin_loaders()

    # In plugins collection find plugin for module
    for plugin in plugins:
        name = plugin.name
        plugin_class, plugin_instance = plugin.get_plugin(plugin_name)
        if name == plugin_name:
            break
        else:
            continue

    pc = PlayContext(None, None, None)
    pc.set_attributes_from_plugin(plugin_instance)
    assert pc._network_os is not None


# Generated at 2022-06-13 08:34:56.193177
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    play_context = PlayContext()
    variables = None
    templar = None
    play_context.set_task_and_variable_override(None, variables, templar)


# Generated at 2022-06-13 08:35:23.820585
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    import ansible.plugins.connection
    import ansible.plugins.connection.connection_loader

    loader = ansible.plugins.connection.connection_loader
    plugin = loader.get('local')

    res = PlayContext()
    res.set_attributes_from_plugin(plugin)

    assert res._executable == '/bin/sh'

# Instanciation for a test of class PlayContext
play = Play()
play_context = PlayContext(play)


# Generated at 2022-06-13 08:35:26.131714
# Unit test for constructor of class PlayContext
def test_PlayContext():
    # Make sure that no exception is raised if connection is not set.
    pc = PlayContext()
    assert isinstance(pc, PlayContext)

# Unit test PlayContext.set_attributes_from_play

# Generated at 2022-06-13 08:35:26.707485
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    pass

# Generated at 2022-06-13 08:35:27.580598
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    play_context = PlayContext({},{})
    pass



# Generated at 2022-06-13 08:35:28.226473
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    pass # TODO



# Generated at 2022-06-13 08:35:40.639029
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    args = dict(
        connection='smart',
        remote_user='test',
        acl_inherit='test',
        become=True,
        become_method='sudo',
        become_user='root',
        check=False,
        diff=False,
        executable='test',
        inventory=None,
        private_key_file='test',
        remote_addr='test',
        remote_port='test',
        scp_extra_args='test',
        sftp_extra_args='test',
        ssh_common_args='test',
        ssh_extra_args='test',
        timeout=5,
        verbosity=0,
        connection_lockfd=5,
        network_os='test'
    )

    pc = PlayContext()

# Generated at 2022-06-13 08:35:48.376198
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    p = PlayContext()
    variables = dict()
    templar = Templar(loader=None, variables=variables)
    task = Task()
    task.delegate_to = 'localhost'
    host_name = 'host1'
    task.remote_user = 'user1'
    variables['ansible_user'] = 'user'
    variables['ansible_ssh_host'] = 'host'
    variables['ansible_winrm_host'] = 'host'
    variables['ansible_host'] = 'host'
    variables['ansible_port'] = 23
    variables['ansible_connection'] = 'connection'
    variables['ansible_network_os'] = 'network_os'
    variables['ansible_become_method'] = 'become_method'

# Generated at 2022-06-13 08:36:00.503344
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    my_task = MagicMock(spec=Task())
    my_task.delegate_to = None
    my_task.remote_user = None
    my_task.check_mode = None
    my_task.diff = None
    my_task.name = 'first_task'

    my_vars = dict()
    my_vars['ansible_connection'] = 'local'
    my_vars['ansible_python_interpreter'] = '/usr/bin/python'
    my_vars['ansible_port'] = 5986
    my_vars['ansible_shell_type'] = 'csh'
    my_vars['ansible_shell_executable'] = '/bin/tcsh'
    my_vars['ansible_user'] = 'root'

# Generated at 2022-06-13 08:36:09.392153
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    delegate_vars = dict(dict(ansible_user='delegate_user1', ansible_port='delegate_port', ansible_host='delegate_host', ansible_ssh_user='delegate_ssh_user', ansible_ssh_port='delegate_ssh_port', ansible_ssh_host='delegate_ssh_host', ansible_winrm_user='delegate_winrm_user', ansible_winrm_port='delegate_winrm_port', ansible_winrm_host='delegate_winrm_host') for i in enumerate(range(4)))

# Generated at 2022-06-13 08:36:12.684270
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    pc = PlayContext()
    plugin = 'test'
    pc.set_attributes_from_plugin(plugin)

    assert pc is pc
    assert plugin is plugin



# Generated at 2022-06-13 08:37:06.085455
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # Test setting attributes on the PlayContext from a plugin
    from ansible.plugins.loader import get_plugin_class
    from ansible.plugins.connection import ConnectionBase
    from ansible.module_utils.six import iteritems
    class FakePlugin(ConnectionBase):
        def __init__(self):
            self._load_name = 'test.load.name'
    fake_plugin = FakePlugin()
    # Create the PlayContext
    p = PlayContext()
    # Set the attributes
    p.set_attributes_from_plugin(fake_plugin)
    # Check that the attributes are set
    assert p.network_os == 'test.load.name'
    # A dict of attribute names and default values for the fake plugin

# Generated at 2022-06-13 08:37:13.319858
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    class TestFailed(Exception):
        pass

    class MockConnectionPlugin(ConnectionBase):
        module_utils_path = None
        def get_option(self, flag):
            if flag == 'test':
                return 42
            return None


    try:
        pc = PlayContext()
        pc.set_attributes_from_plugin(MockConnectionPlugin())
        if pc.test != 42:
            raise TestFailed()
    except TestFailed:
        raise AssertionError('set_attributes_from_plugin() failed')

# Generated at 2022-06-13 08:37:18.996322
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # Arrange
    task = MagicMock()
    variables = MagicMock()
    templar = MagicMock()
    obj = PlayContext(None, None, None)

    # Act
    result = obj.set_task_and_variable_override(task, variables, templar)

    # Assert
    print(result)


# Generated at 2022-06-13 08:37:26.709700
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # create a stub "Play" object to pass in
    class Play:
        def __init__(self, data):
            self.__dict__ = data
            self.force_handlers = False

# Generated at 2022-06-13 08:37:36.527034
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # prefix and arguments should be handled by the plugin (although
    # nothing prevents us from doing it here).
    #
    # Note: ceph_volume was chosen because it doesn't require any
    # other plugins to be loaded to return from get_option_info.
    plugin = cliconf_util.get_plugin("ceph_volume")

    # Create a new PlayContext and populate it with data from the
    # plugin chosen above.
    play_context = PlayContext(play=None, passwords=None, connection_lockfd=None)
    play_context.set_attributes_from_plugin(plugin)
    # Now we have enough info to inspect the PlayContext to ensure
    # that the prefix and arguments plugin options have been
    # properly set.
    assert play_context._prefix == plugin.get_option('prefix')
    assert play_context

# Generated at 2022-06-13 08:37:49.014310
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    class MockPlugin(object):
        def __init__(self, loader, name):
            self._loader_name = name
            self._options = dict(
                timeout=dict(name='timeout'),
                ssh_key_file=dict(name='private_key_file'),
                verbose=dict(name='verbosity'),
                start_at_task=dict(name='start_at_task'),
            )
        def get_option(self, option):
            return self._options.get(option)
    plugin = MockPlugin(None, '')
    play_context = PlayContext(passwords={})
    play_context.set_attributes_from_plugin(plugin)
    assert 0 == play_context.verbosity
    assert not play_context.start_at_task
    assert not play_context.private_key_file


# Generated at 2022-06-13 08:37:58.279242
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # Instantiate a (very simple) implementation of a connection plugin
    mock_plugin = MockCnx()

    # Instantiate a PlayContext object
    pc = PlayContext()

    # Call the method we want to test
    pc.set_attributes_from_plugin(mock_plugin)

    # And check that the attributes have been set accordingly
    assert(pc.network_os == 'test_network_os')
    assert(pc.module_path == 'test_module_path')

    # Let's also check that if we invoke it again, the attributes are
    # reset since they have been set in a connection plugin
    mock_plugin._network_os = 'network_os_again'
    pc.set_attributes_from_plugin(mock_plugin)
    assert(pc.network_os == 'network_os_again')



# Generated at 2022-06-13 08:38:10.127329
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    play = MagicMock()
    passwords = {'conn_pass': 'mock_conn_pass', 'become_pass': 'mock_become_pass'}
    connection_lockfd = MagicMock()
    ctx = PlayContext(play=play, passwords=passwords, connection_lockfd=connection_lockfd)

    # Case 1: ssh_connection plugin
    plugin = MagicMock(type=Connection, spec=ssh_connection)
    plugin._load_name = 'plugin_name'
    plugin.get_option = MagicMock(side_effect=['conn_pass', 'become_pass'])
    ctx.set_attributes_from_plugin(plugin)
    assert ctx.password == plugin.get_option('password')

# Generated at 2022-06-13 08:38:20.768026
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    from ansible import context
    from ansible.vars.manager import VariableManager

    context._init_global_context()

    # Prepare default variables
    variables = VariableManager()
    variables.extra_vars = {'not_used': 1, 'random_value': 'abc'}

    # Test options
    play = object()
    task = object()
    templar = object()

    # Test set_task_and_variable_override
    context.CLIARGS = dict(connection='smart', timeout=30,
                           private_key_file='/tmp/test_key', verbosity=3)
    play_context = PlayContext(play)
    assert play_context.connection == 'smart'
    assert play_context.timeout == 30

# Generated at 2022-06-13 08:38:26.910583
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from ansible.plugins.loader import connection_loader
    p = PlayContext(play=None, passwords=None, connection_lockfd=None)

    for i in connection_loader.all():
        if getattr(i, '_load_name', None):
            p.set_attributes_from_plugin(i())

        assert isinstance(p, PlayContext)



# Generated at 2022-06-13 08:39:55.280962
# Unit test for method set_task_and_variable_override of class PlayContext

# Generated at 2022-06-13 08:39:55.956551
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    pass

# Generated at 2022-06-13 08:40:05.671300
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    import ansible.inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.playbook.play import Play
    from ansible.template import Templar


    # Load data from YAML file
    data = None
    with open(os.path.join(os.path.dirname(__file__), "./PlayContext/test_PlayContext_set_task_and_variable_override.yml")) as f:
        data = yaml.load(f)


    # Create dummy variables
    options = data['options']
    options['connection'] = 'local'
    connection = 'local'
    passwords = None
    connection_lockfd = '10'

    # Create inventory, loader and variable_manager
    host = ansible.inventory.host

# Generated at 2022-06-13 08:40:13.572848
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # try to create a PlayContext object
    play_context = PlayContext()

    # try to get a plugin with a dummy name
    plugin = get_plugin_class('some_dummy_plugin_name')
    assert plugin is not None

    # try to set attributes from plugin
    play_context.set_attributes_from_plugin(plugin)

    # check if the connection was set to local
    assert play_context.remote_user is None
    assert play_context.password is None
    assert play_context.private_key_file is None



# Generated at 2022-06-13 08:40:23.314087
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    task = Task()
    task.delegate_to = 'test'
    task.delegate_facts = False
    task.remote_user = 'ansible'

    variables = dict(ansible_become='true')
    variables['ansible_become_user'] = 'root'
    variables['ansible_become_pass'] = '1'
    variables['ansible_become_method'] = 'su'
    variables['ansible_executable'] = '/bin/bash'

    templar = Templar()

    play_context = PlayContext()
    play_context.set_task_and_variable_override(task, variables, templar)

    assert play_context.become_user == variables['ansible_become_user']

# Generated at 2022-06-13 08:40:24.695705
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    assert False


# Generated at 2022-06-13 08:40:32.855114
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    playcontext = PlayContext(None)
    playcontext.set_attributes_from_cli()
    # unit test of method set_attributes_from_cli of class PlayContext
    assert playcontext.timeout == C.DEFAULT_TIMEOUT if C.DEFAULT_TIMEOUT else None
    assert playcontext.private_key_file == C.DEFAULT_PRIVATE_KEY_FILE
    assert playcontext.verbosity == 0
    assert playcontext.start_at_task is None


# Generated at 2022-06-13 08:40:33.631843
# Unit test for method set_task_and_variable_override of class PlayContext

# Generated at 2022-06-13 08:40:34.376844
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    pass

# Generated at 2022-06-13 08:40:37.763863
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    """
    Test to set attributes from plugins
    """
    ob = PlayContext()
    ob.set_attributes_from_plugin('ping')
    assert not ob #FIXME: Should we have more test cases for this?

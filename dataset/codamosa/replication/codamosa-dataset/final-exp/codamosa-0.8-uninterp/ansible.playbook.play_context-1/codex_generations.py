

# Generated at 2022-06-13 08:31:37.982147
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    '''
    Unit test for method: ansible.playcontext.PlayContext.set_task_and_variable_override
    '''
    m = PlayContext()
    t = Task()
    m.set_task_and_variable_override(t, {}, templar={})

    pass


# Generated at 2022-06-13 08:31:44.475025
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # default tasks and variables
    task = Task()
    variables = {'ansible_connection': 'ssh'}
    playcontext = PlayContext()

    # Use set_task_and_variable_override to override the defaults
    playcontext_test = PlayContext()
    playcontext_test.set_task_and_variable_override(task, variables, templar=MockTemplar())

    # check if the values from variable and task are properly set
    assert playcontext_test.connection == 'ssh'
    assert playcontext_test.remote_addr == '127.0.0.1'
    assert playcontext_test.remote_user == 'user1'



# Generated at 2022-06-13 08:31:49.619113
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    module_name = 'ping'
    module_args = 'data=testdata'
    option_name = 'test'

    m = Mock()
    m.test = option_name

    pc = PlayContext(m)

    # Test if option is set correctly or not
    pc.set_attributes_from_plugin(m)
    assert pc.test == option_name



# Generated at 2022-06-13 08:31:52.777768
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    context = PlayContext()
    context.set_attributes_from_cli()
    assert context.private_key_file == None
    assert context.verbosity == None
    assert context.start_at_task == None

# Generated at 2022-06-13 08:32:00.969400
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():

    # Initialize options for test
    # Arrange
    play = Play()
    play.force_handlers = True
    connection_lockfd = 1
    passwords = {
        'conn_pass': 'secret',
        'become_pass': 'secret'
    }
    play_context = PlayContext(play=play, passwords=passwords, connection_lockfd=connection_lockfd)
    task = Task()
    task.delegate_to = 'remote_host'
    # Act
    play_context.set_attributes_from_cli()
    task_info = play_context.set_task_and_variable_override(task=task, variables={}, templar=None)
    # Assert
    assert play_context.force_handlers is True
    assert play_context.password == 'secret'

# Generated at 2022-06-13 08:32:11.078097
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    print('Testing PlayContext.set_attributes_from_plugin')

    one_host = Mock(host=Mock(), port=Mock())
    one_play = Mock(hosts=[one_host], remote_user='ansible', become_user='ansible', become_method='sudo', become='yes')
    plugin = Mock(get_option=Mock(return_value='ssh'))

    c = PlayContext(play=one_play)
    c.set_attributes_from_plugin(plugin)

    assert c.connection == 'ssh'


# Generated at 2022-06-13 08:32:11.503361
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    pass

# Generated at 2022-06-13 08:32:21.711003
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():

    # A PlayContext object can also be constructed without play, for deserialization purposes.
    #
    # DESCRIPTION:
    #       Creates PlayContext object without Play object
    #       for deserialization purposes.
    #
    # RETURN VALUE:
    #       An empty PlayContext object.
    #
    # TEST SCRIPT:

    # setup context
    obj = PlayContext()

    assert isinstance(obj, PlayContext)

    assert obj.__class__.__base__ == BaseContext

    # Fields that are not on the base context
    #
    # NOTE:  This is not a complete test

    assert obj._verbosity == 0

    assert len(obj._only_tags) == 0

    assert len(obj._skip_tags) == 0

    assert obj._start_at_task == None


# Generated at 2022-06-13 08:32:22.562490
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    assert False, "Not implemented"


# Generated at 2022-06-13 08:32:30.853604
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    '''
    test PlayContext.set_attributes_from_plugin method
    '''
    # AttributeError() raises
    test_obj = PlayContext()
    try:
        test_obj.set_attributes_from_plugin(None)
    except AttributeError as test_except:
        assert test_except.args[0] == "unexpected attribute '_load_name' to plugin instance"


# Generated at 2022-06-13 08:32:51.264216
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
   
    # Testing default case
    pc = PlayContext()
    pc.set_attributes_from_plugin(pc)
    assert(pc.verbosity == 0)
    
    # Testing custom case 
    pc2 = PlayContext()
    pc2.verbosity = 1
    pc2.set_attributes_from_plugin(pc2)
    assert(pc2.verbosity == 1)


# Generated at 2022-06-13 08:32:53.344557
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
  PlayContext_instance = PlayContext()
  plugin = 'test'
  PlayContext_instance.set_attributes_from_plugin( plugin)

# unit tests for PlayContext

# Generated at 2022-06-13 08:32:54.259560
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    assert False



# Generated at 2022-06-13 08:33:02.224658
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # Assert parameters exist
    play = {}
    variables = {}
    templar = {}
    task = {}
    task.delegate_to = None
    task.remote_user = None
    playcontext = PlayContext(play, passwords={}, connection_lockfd=None)
    playcontext.set_attributes_from_cli()
    playcontext.set_attributes_from_play(play)
    playcontext2 = playcontext.set_task_and_variable_override(task, variables, templar)

    # Assert attributes on new object
    assert hasattr(playcontext2, 'connection') == True
    assert hasattr(playcontext2, 'port') == True
    assert hasattr(playcontext2, 'remote_user') == True
    assert hasattr(playcontext2, 'executable') == True
   

# Generated at 2022-06-13 08:33:04.666099
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # DEPRECATED: to be removed with PlayContext, same functionality in TaskExecutor, not yet tested
    pass

# Generated at 2022-06-13 08:33:13.964285
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    """
    init ansible enum for testing
    """
    test_enum = enum.Enum(value='test_enum', names={'test1': 1, 'test2': 2})
    ansible_commands = enum.Enum(value='ansible_commands', names={'test1': 1, 'test2': 2})
    """
    setup test args
    """
    test_play = MagicMock()
    test_play.force_handlers = True
    test_play.tags = ['tag1', 'tag2']
    test_play.tasks = ['task1', 'task2']

    test_password = {'pass1': 'pass1', 'pass2': 'pass2'}
    test_connection_lockfd = 1

    test_plugin = MagicMock()
    test_plugin.port = 5985

# Generated at 2022-06-13 08:33:25.820527
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from ansible.template.template import Templar

    loader = DictDataLoader({
        "foo": """
        ---
        - hosts: localhost
          tasks:
            - shell: echo "{{ansible_port}}"
        """
    })
    inventory = InventoryManager([], loader=loader)
    play_data = loader.load_from_file("foo")[0]


# Generated at 2022-06-13 08:33:32.218110
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # Test normal scenarios
    task = MagicMock()
    variables = MagicMock()
    templar = MagicMock()
    pc = PlayContext(None, passwords=None, connection_lockfd=None)
    # test for ssh_args
    plugin = ActionBase(task, pc, templar, variables)
    pc.set_attributes_from_plugin(plugin)
    assert pc.ssh_args == "-o ControlMaster=auto -o ControlPersist=60s -o ControlPath=/opt/app/ansible/playbooks/workdir/ansible-ssh-%h-%p-%r"



# Generated at 2022-06-13 08:33:37.899681
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    class Test_PlayContext:
        def __init__(self):
            self.force_handlers = None
    class Test_BaseConnection:
        def __init__(self, play_context):
            self.play_context = play_context
    class Test_Plugin:
        def __init__(self, play_context):
            self.play_context = play_context
        def get_option(self, option):
            return getattr(self.play_context, option)

# Generated at 2022-06-13 08:33:40.529989
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    pc = PlayContext()
    pc.set_attributes_from_plugin(None)

# Generated at 2022-06-13 08:33:56.463381
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    c = PlayContext()
    #TODO


# Generated at 2022-06-13 08:34:02.799875
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    '''
    Unit test for method set_task_and_variable_override of class PlayContext
    '''
    context.CLIARGS = None
    obj = PlayContext()
    test_task = None
    test_variables = None
    test_templar = None
    res = obj.set_task_and_variable_override(test_task, test_variables, test_templar)

# Generated at 2022-06-13 08:34:15.232222
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # Test with a valid plugin
    pc = PlayContext()
    pc.set_attributes_from_plugin('ssh')
    assert pc.remote_addr == None
    assert pc.remote_user == None
    assert pc.port == None
    assert pc.password == None
    assert pc.private_key_file == None
    assert pc.connection == None
    assert pc.timeout == None
    assert pc.shell == None
    assert pc.accelerate_port == None
    assert pc.accelerate_ipv6 == None
    assert pc.accelerate_password == None
    assert pc.accelerate_timeout == None
    assert pc.no_log == None
    assert pc.ssh_common_args == None
    assert pc.ssh_extra_args == None
    assert pc.sftp_extra_args == None

# Generated at 2022-06-13 08:34:17.002022
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    pass


# Generated at 2022-06-13 08:34:27.732356
# Unit test for constructor of class PlayContext
def test_PlayContext():
    from ansible.constants import CLIARGS
    from ansible.utils.display import Display

    # Need to mock up some objects for PlayContext to instantiate.  In
    # particular, we need a Play, a Inventory object and a Display object.  We
    # create these objects here and then pass them in when creating the
    # PlayContext object.
    class FakePlay:
        pass

    class FakeInventory:
        def get_host(self, hostname):
            return FakeHost(hostname)

    class FakeHost:
        def __init__(self, name):
            self.name = name

        def get_vars(self):
            return dict()

    class FakeDisplay(Display):
        def __init__(self):
            pass

    fake_play = FakePlay()
    fake_inventory = FakeInventory()
   

# Generated at 2022-06-13 08:34:34.100957
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    new_info = PlayContext(C.DEFAULT_TRANSPORT, C.DEFAULT_REMOTE_PORT, C.DEFAULT_USER, C.DEFAULT_BECOME_METHOD, C.DEFAULT_BECOME_USER, C.DEFAULT_BECOME_FLAGS, False, False)
    new_info.connection = 'smart'
    new_info.remote_addr = 'abc'
    new_info.remote_user = ''
    new_info.port = None
    task = MagicMock()
    task.delegate_to = None
    templar = MagicMock()
    templar.template.return_value = 'abc'

# Generated at 2022-06-13 08:34:34.824229
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    pass

# Generated at 2022-06-13 08:34:43.128647
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    pc = PlayContext(play=None, passwords=None, connection_lockfd=None)
    assert pc._attributes[u'remote_addr'] == u'.'
    assert pc._attributes[u'connection'] == u'local'
    assert pc._attributes[u'remote_user'] == u'root'
    assert pc._attributes[u'no_log'] == False
    assert pc._attributes[u'remote_pass'] == u''
    assert pc._attributes[u'port'] == 22
    assert pc._attributes[u'private_key_file'] == u'~/.ssh/id_rsa'
    assert pc._attributes[u'network_os'] == u''
    assert pc._attributes[u'become'] == None

# Generated at 2022-06-13 08:34:45.383900
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    PlayContext().set_task_and_variable_override(None, None, None)


# Generated at 2022-06-13 08:34:49.934755
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    import sys
    import os
    import json
    import StringIO
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import connection_loader, become_loader
    from ansible.plugins.callback import CallbackBase
    from ansible import constants as C
    import ansible.constants as C

    class TestCallbackModule(CallbackBase):
        def __init__(self):
            self.host_ok = {}
            self.host_unreachable = {}
            self.host_failed = {}

    # initialize needed objects
    loader = DataLoader()


# Generated at 2022-06-13 08:35:05.082126
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    assert True

# Generated at 2022-06-13 08:35:12.282999
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # create an instance of the class we want to test
    test_variables = dict()
    test_play = Play()
    test_play.force_handlers = 'some_handlers'
    test_task = Task()
    test_task.delegate_to = 'some_delegation'
    test_task.remote_user = 'some_remote_user'
    test_task.delegate_to = 'some_delegation'
    test_task.delegate_to = 'some_delegation'
    test_task.delegate_to = 'some_delegation'
    test_task.delegate_to = 'some_delegation'
    test_task.delegate_to = 'some_delegation'
    test_play_context = PlayContext()
    test_play_context.set

# Generated at 2022-06-13 08:35:17.291018
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    for x in range(20):
        play = dict()
        cur_context = PlayContext("127.0.0.1", 22, play)

        method = 'ssh'
        cur_context.set_attributes_from_plugin(method)


# Generated at 2022-06-13 08:35:27.896115
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # PlayContext.__init__() sets attributes
    # PlayContext.set_attributes_from_plugin() sets attributes

    # Test with no arguments
    # Ensure no exceptions are thrown
    try:
        PlayContext()
    except Exception:
        assert False, "Unexpected Exception was raised"

    # Test with valid arguments
    x = PlayContext()

    # Test to make sure the attributes on an instance of PlayContext are being set
    # Find a valid connection plugin to test
    connection_plugins = get_all_plugin_loaders('Connection')
    for plugin_name, plugin_loader in iteritems(connection_plugins):
        valid_plugin = True
        try:
            plugin_loader.get_plugin()
        except AnsibleLookupError:
            # Not a plugin
            valid_plugin = False

# Generated at 2022-06-13 08:35:40.543898
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # create task object
    task = mock.Mock()
    task.delegate_to = None
    task.remote_user = 'root'
    task.force_handlers = None
    task.no_log = False
    task.delegate_facts = False
    task.run_once = False
    task.check_mode = None

    # create PlayContext object
    play = mock.Mock()
    play.force_handlers = False

    var_manager = mock.Mock()
    var_manager.extra_vars = dict()
    var_manager.host_vars = dict()
    var_manager.group_vars = dict()

    play_context_obj = PlayContext(play)
    play_context_obj.set_attributes_from_plugin(send_file())
    play_context_obj

# Generated at 2022-06-13 08:35:50.705845
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from importlib import import_module
    from ansible.plugins.loader import get_all_plugin_loaders
    # inventory = InventoryManager(loader=CLI.config.loader, sources=['localhost,127.0.0.1,::1']) # FIXME: see if this is needed
    # call_args = {'inventory': inventory, 'variable_manager': VariableManager()}
    call_args = {}
    result = {}
    plugins = {}
    for name, plugin_loader in iteritems(get_all_plugin_loaders()):
        d = import_module("ansible.plugins.%s" % name)
        for attr in dir(d):
            item = getattr(d, attr)

# Generated at 2022-06-13 08:36:00.839522
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    p = PlayContext()
    c = SSHConnection()
    c.set_options({'host_key_checking': True, 'pipelining': False})
    p.set_attributes_from_plugin(c)
    assert p.remote_addr == u'localhost'
    assert p.remote_user == u'root'
    assert p.port == 22
    assert isinstance(p.password, AnsibleUnsafeText)
    assert p.private_key_file == u'~/.ssh/id_rsa'
    assert p.timeout == 10
    assert p.host_key_checking is True
    assert p.pipelining is False

# Generated at 2022-06-13 08:36:03.152125
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    '''
    PlayContext set_task_and_variable_override() unit test stub.
    '''
    pass

# Generated at 2022-06-13 08:36:06.289314
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    pc = PlayContext()
    assert pc

    pc.set_attributes_from_plugin(None)
    assert pc

if __name__ == '__main__':
    test_PlayContext_set_attributes_from_plugin()

# Generated at 2022-06-13 08:36:15.530948
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from units.mock.loader import DictDataLoader
    from units.mock.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor

    variable_manager = VariableManager()
    loader = DataLoader()

    pbex = PlaybookExecutor(playbooks=[CONN_PLUGIN_PATH], inventory=Inventory(loader=loader, variable_manager=variable_manager), variable_manager=variable_manager, loader=loader, passwords={})

    play_context = PlayContext()
    play_context.set_attributes_from_plugin(pbex._tqm.get_connection_info(None)._play_context.connection)


# Generated at 2022-06-13 08:36:47.671290
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    x = Play()
    y = dict()
    z = 1
    PlayContext(x,y,z)


# Generated at 2022-06-13 08:36:51.998549
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    context = PlayContext()
    context.set_attributes_from_cli()
    conn = 'connection'
    if conn in context._attributes:
        print('%s: %s' % (conn, context._attributes[conn]))
    else:
        print('%s: not found' % conn)
# Unit test suite

# Generated at 2022-06-13 08:36:58.127001
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    '''
    Unit test for method set_attributes_from_cli of class PlayContext
    '''
    _playcontext = PlayContext(play=None, passwords=None, connection_lockfd=None)
    _playcontext.set_attributes_from_cli()


# Generated at 2022-06-13 08:37:08.492522
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    p = PlayContext()
    # When there is no plugin, the method does nothing
    p.set_attributes_from_plugin(None)

# Generated at 2022-06-13 08:37:20.121216
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    context_for_set_task_and_variable_override = PlayContext()
    context_for_set_task_and_variable_override.set_attributes_from_cli()
    context_for_set_task_and_variable_override.set_attributes_from_play(play=None)
    context_for_set_task_and_variable_override.set_task_and_variable_override(task=task, variables=variables, templar=templar)

    # test if connection_type == 'ssh' and paramiko == None
    context_for_set_task_and_variable_override.connection = 'ssh'
    assert context_for_set_task_and_variable_override.connection == 'ssh'

    # test if connection_type == 'smart' and paramiko == None

# Generated at 2022-06-13 08:37:32.104938
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # Test the case in which plugin is None.
    #
    # Input Parameters:
    #   plugin: None
    # Expected Output:
    #   No exceptions should be thrown.
    try:
        new_pc = PlayContext()
        new_pc._become_plugin = None
        new_pc.set_attributes_from_plugin(None)
        ret_val1 = ""
    except Exception as e:
        ret_val1 = "exception: %s" % str(e)

    # Test the case in which plugin is a test string.
    #
    # Input Parameters:
    #   plugin: 'blah'
    # Expected Output:
    #   No exceptions should be thrown.

# Generated at 2022-06-13 08:37:44.694349
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    p = Play()
    p._included_file = "test/test_PlayContext.yml"
    p.vars = dict(foo="foo")
    p.play_hosts = ["localhost"]

    hst = Host("localhost")
    inv = Inventory(loader=None)
    inv.add_group("testgroup")
    inv._hosts_cache["localhost"] = hst
    inv.get_group("testgroup").add_host(hst)

# Generated at 2022-06-13 08:37:54.537671
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    # Stub
    context.CLIARGS = dict()
    # Unit test
    pc = PlayContext()
    pc.set_attributes_from_cli()
    # Assertions
    assert pc.verbosity == 0
    assert pc.start_at_task == None
    # Set the fixture
    context.CLIARGS['timeout'] = 5
    context.CLIARGS['verbosity'] = 3
    context.CLIARGS['start_at_task'] = 'command'
    # Unit test
    pc.set_attributes_from_cli()
    # Assertions
    assert pc.timeout == 5
    assert pc.verbosity == 3
    assert pc.start_at_task == 'command'
    return


# Generated at 2022-06-13 08:38:05.570218
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    temp = dict()
    var = dict()
    pc = PlayContext()
    pc.set_task_and_variable_override(temp, var, temp)
    assert pc
    assert pc.remote_addr is None
    assert pc.transport is None
    assert pc.remote_user is None
    assert pc.connection is None
    assert pc.port is None
    assert pc.timeout is None
    assert pc.accelerate is None
    assert pc.no_log is None
    assert pc.network_os is None
    assert pc.pipelining is None
    assert pc._become is None
    assert pc.become_method is None
    assert pc.become_user is None
    assert pc.become_exe is None
    assert pc.become_flags is None

# Generated at 2022-06-13 08:38:11.876820
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    """ Unit test for method 'set_attributes_from_plugin' """
    # Test case 1
    play_context = PlayContext()
    plugin = 'file'
    # pylint: disable=W0212
    play_context.set_attributes_from_plugin(plugin)
    assert play_context is not None, "Play context has not been created"
    print("PlayContext: %s", play_context)


# Generated at 2022-06-13 08:39:21.991387
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    ctx = PlayContext(play=None, passwords=None, connection_lockfd=None)
    assert ctx._attributes.get('connection') == 'smart'
    assert ctx._attributes.get('verbosity') == 0
    assert ctx._attributes.get('timeout') == C.DEFAULT_TIMEOUT
    assert ctx._attributes.get('private_key_file') == C.DEFAULT_PRIVATE_KEY_FILE


# Generated at 2022-06-13 08:39:29.371151
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    """Test PlayContext.set_task_and_variable_override"""
    ansible_facts = dict()
    ansible_facts['ansible_ssh_host'] = '127.0.0.1'
    ansible_facts['ansible_ssh_port'] = 22
    ansible_facts['ansible_ssh_user'] = 'root'
    ansible_facts['ansible_ssh_pass'] = None
    ansible_facts['ansible_ssh_private_key_file'] = None
    ansible_facts['ansible_ssh_executable'] = None
    ansible_facts['ansible_ssh_common_args'] = None
    ansible_facts['ansible_ssh_extra_args'] = None
    ansible_facts['ansible_ssh_extra_args'] = None

# Generated at 2022-06-13 08:39:37.251014
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # Initialize and set the instance variables of PlayContext
    fake_play_context = PlayContext()
    fake_play_context.set_attributes_from_cli()
    # Initialize and set the instance variables of task
    fake_task = Task()
    fake_task.delegate_to = "dummy_delegate_to"
    fake_task.remote_user = "dummy_remote_user"
    # Initialize and set the instance variables of templar
    fake_templar = Templar()
    fake_templar.template = MagicMock(return_value="dummy_delegate_to")
    # Initialize and set the instance variables of variables
    fake_variables = {}
    # Call the method set_task_and_variable_override and store the returned object
    new_info = fake_play_

# Generated at 2022-06-13 08:39:45.765824
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    fake_task = Mock()
    fake_task.connection = None
    fake_task.become_user = None
    fake_task.scp_extra_args = None
    fake_task.ssh_extra_args = None
    fake_task.sftp_extra_args = None
    fake_task.scp_executable = None
    fake_task.timeout = None
    fake_task.remote_user = None
    fake_task.always_run = False
    fake_task.serial = None
    fake_task.delegate_to = None

    fake_variables = dict()
    fake_variables['connection'] = None
    fake_variables['ansible_become_user'] = None
    fake_variables['ansible_ssh_common_args'] = None

# Generated at 2022-06-13 08:39:48.600875
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    play_context = PlayContext()
    # TODO: test that plugin is a connection plugin
    plugin = None
    play_context.set_attributes_from_plugin(plugin)
    assert play_context



# Generated at 2022-06-13 08:39:55.795855
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    mock_cliargs = {'timeout': 'timeout_val', 
                    'verbosity': 'verbosity_val', 
                    'private_key_file': 'private_key_file_val',
                    'start_at_task': 'start_at_task_val'}
    args = namedtuple('args', mock_cliargs.keys())(*mock_cliargs.values())
    context.CLIARGS = args

    pc = PlayContext()

    with mock.patch.object(context, 'CLIARGS', mock_cliargs):
        pc.set_attributes_from_cli()
        assert pc.timeout == 'timeout_val'
        assert pc.verbosity == 'verbosity_val'
        assert pc.private_key_file == 'private_key_file_val'
        assert pc.start_at

# Generated at 2022-06-13 08:40:05.559281
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    play_context = PlayContext()
    # task is really not optional.  The only time it could be omitted is when we create
    # a PlayContext just so we can invoke its deserialize method to load it from a serialized
    # data source.
    task = None  # type: Task
    variables = dict()
    templar = Templar(None)

    # test exceptions
    with pytest.raises(AnsibleError):
        play_context.set_task_and_variable_override(task, variables, templar)

    # test the method normally
    task = Task()
    variables = dict(ansible_ssh_host='192.168.0.1', ansible_ssh_port='22')
    templar = Templar(None)


# Generated at 2022-06-13 08:40:06.706730
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    PlayContext(play=None, passwords=None, connection_lockfd=None)

# Generated at 2022-06-13 08:40:09.867297
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    instance = PlayContext()
    # Since set_attributes_from_plugin is complicated and may be not really tested by Ansible, it should be covered by automated unit tests.
    assert False


# Generated at 2022-06-13 08:40:12.401497
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    context = PlayContext()
    context.set_attributes_from_plugin(ModuleLoader.get('copy'))
    assert context.copy == 'no'

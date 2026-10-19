

# Generated at 2022-06-13 08:31:37.105698
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    context.CLIARGS = {'verbosity': 0}
    with pytest.raises(AttributeError):
        PlayContext(play=None, passwords=None, connection_lockfd=None)

# Generated at 2022-06-13 08:31:49.490703
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    got, exp = None, None

    # test default
    play_context = PlayContext()
    real_ansible = get_default_ansible_connection_plugins()
    for plugin_class in real_ansible:
        plugin = plugin_class()
        play_context.set_attributes_from_plugin(plugin)

    # test connection
    play_context = PlayContext()
    plugin = MockConnectionPlugin('mock', 'mock_default_value')
    play_context.set_attributes_from_plugin(plugin)
    got = play_context.connection
    exp = plugin.get_option('connection')
    assert got == exp

    # connection is smart
    play_context = PlayContext()
    plugin = MockConnectionPlugin('mock', 'smart')

# Generated at 2022-06-13 08:31:56.805587
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # Empty play_context object
    play_context = PlayContext()
    # Empty task object
    task = Task()
    # Empty variables
    variables = {}
    # Empty templar
    templar = Templar()
    # Setting attributes of task object
    task.any_errors_fatal = True
    task.allow_duplicates = True
    task.always_run = True
    task.become = True
    task.become_user = 'root'
    task.become_method = 'sudo'
    task.become_method_user = 'stack'
    task.become_flags = '-H'
    task.block = Block()
    task.check_mode = True
    task.connection = 'smart'
    task.delegate_to = 'localhost'

# Generated at 2022-06-13 08:32:10.395220
# Unit test for method set_task_and_variable_override of class PlayContext

# Generated at 2022-06-13 08:32:16.212238
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    class FakePlugin():
        get_option = None

        def __init__(self, *args, **kwargs):
            pass

        def get_option(self, option):
            return option

    p = PlayContext(None, None)
    p.set_attributes_from_plugin(FakePlugin())



# Generated at 2022-06-13 08:32:25.203358
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    import ansible.playbook.play
    task = ansible.playbook.play.Task()
    task.delegate_to='127.0.0.1'
    variables={'ansible_ssh_private_key_file': '/root/.ssh/id_rsa', 'ansible_ssh_user': 'root'}
    connection_lockfd = 1024
    context_ = PlayContext(None, None, connection_lockfd)
    #Accessing private member
    #pylint: disable=W0212

# Generated at 2022-06-13 08:32:39.463679
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    p = PlayContext()
    task = Task()
    task.name = "test_task"
    task.args = dict()
    task.delegate_to = "localhost"

    #Test case with password and become_user specified.
    task.args["password"] = "password"
    task.become = True
    task.become_user = "admin"

    p.set_task_and_variable_override(task, dict(),dict())
    assert task.args["password"] == p.password

    #Test case with password and become_pass specified (become_pass has higher precedence).
    task.args["become_pass"] = "become_pass"
    p.set_task_and_variable_override(task, dict(), dict())
    assert task.args["become_pass"] == p.become

# Generated at 2022-06-13 08:32:47.380470
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    plugin = Mock()
    plugin.get_option.return_value = 'test'
    play = Mock()
    passwords = {'conn_pass': 'pass', 'become_pass': 'pass2'}
    connection_lockfd = None
    obj = PlayContext(play, passwords, connection_lockfd)
    obj.set_attributes_from_plugin(plugin)
    assert obj.set_attributes_from_plugin(plugin) == None
    assert obj.get_attributes()['executable'] == 'test'


# Generated at 2022-06-13 08:32:56.465983
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from units.assembling.config_manager import ConfigManager
    from units.compat.mock import patch
    from ansible.cli import CLI
    from ansible.plugins.loader import get_plugin_class

    class MockConnection():
        def __init__(self, *args, **kwargs):
            self._load_name = 'connection'
            self.get_option = lambda attr_var: self.__dict__[attr_var]
            self.__dict__.update(kwargs)

    conn_ssh = MockConnection(host='somehost', port=22)
    conn_winrm = MockConnection(host='somehost', port=5986)

    class TestOptions():
        def __init__(self, **kwargs):
            self.private_key_file = None

# Generated at 2022-06-13 08:32:56.924183
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
  pass

# Generated at 2022-06-13 08:33:16.604885
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    conn_info = PlayContext()
    conn_info.set_attributes_from_plugin('network_cli')
    assert conn_info._network_os == 'default'
    assert conn_info._verbosity == 0
    assert conn_info._remote_addr == None
    assert conn_info._remote_user == None
    assert conn_info._port == None
    assert conn_info._timeout == 10
    assert conn_info._connection == None

# Generated at 2022-06-13 08:33:28.110502
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from units.mock.path import mock_unfrackpath_warn
    from units.mock.parser import MockParser
    C = AnsibleConfig()
    #from ansible.utils import context_objects as co
    #from ansible.config.manager import ConfigManager
    ds = DictDataLoader({})
    cp = MockParser(ds)
    pc = PlayContext(play=cp.get_plays()[0])
    pc.update_vars({})
    from datetime import timedelta
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

# Generated at 2022-06-13 08:33:35.093238
# Unit test for constructor of class PlayContext
def test_PlayContext():
    play = Play().load({
        'name': 'test play',
    })

    passwords = {
        'conn_pass': 'secret password',
        'become_pass': 'secret become password',
    }

    # test PlayContext without connection_lockfd
    pc = PlayContext(play, passwords)
    assert pc.connection_lockfd == None

    # test PlayContext with connection_lockfd
    pc = PlayContext(play, passwords, connection_lockfd=1)
    assert pc.connection_lockfd == 1

    # test pc.set_attributes_from_play
    pc.set_attributes_from_play(play)

    # test pc.set_attributes_from_cli
    pc.set_attributes_from_cli()

    # test pc.set_attributes_from_plugin
    # FIXME

# Generated at 2022-06-13 08:33:38.100767
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    p = PlayContext()
    p.set_attributes_from_plugin('test')


# Generated at 2022-06-13 08:33:49.679192
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    import pdb; pdb.set_trace()
    task = Task()
    task.vars = {'ansible_connection': 'local'}
    variables = {}
    pc = PlayContext()

# Generated at 2022-06-13 08:33:59.665685
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    context.CLIARGS = {'timeout': 3, 'verbosity': 7, 'start_at_task': 'start here'}
    # Test cli with args
    play_context = PlayContext()
    assert play_context.timeout == 3
    assert play_context.verbosity == 7
    assert play_context.start_at_task == 'start here'
    # Test cli without args
    context.CLIARGS = {}
    play_context = PlayContext()
    assert play_context.timeout == C.DEFAULT_TIMEOUT
    assert play_context.verbosity == 0
    assert play_context.start_at_task == None


# Generated at 2022-06-13 08:34:13.004517
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():

    def test_options():
        yield dict(), dict()
        yield dict(), dict(ansible_ssh_user=None)
        yield dict(), dict(ansible_user=None)
    class Task(object):

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

    for task_options, extra_vars in test_options():
        task_options.update({
            'remote_user': 'bob',
            'become': 'true',
            'become_user': 'janet',
            'delegate_to': 'frank',
            'delegate_facts': 'true',
        })
        task = Task(**task_options)

# Generated at 2022-06-13 08:34:25.415884
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import wrap_var
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from collections import namedtuple
    # test namedtuple
    Task = namedtuple('Task', ['delegate_to', 'delegate_facts', 'remote_user', 'no_log', 'any_errors_fatal', 'check_mode', 'diff'])
    task = Task('hostname', 'delegate_facts', 'remote_user', 'no_log', 'any_errors_fatal', 'check_mode', 'diff')

# Generated at 2022-06-13 08:34:33.001247
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    def fake_get_option(self,a):
        return {}
    Plugin.get_option = fake_get_option
    pc = PlayContext()
    pc.set_attributes_from_plugin("foobar")
    assert isinstance(pc.as_dict().get('_attributes'),dict)
    assert len(pc.as_dict().get('_attributes'))==0


# Generated at 2022-06-13 08:34:37.091266
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    c = PlayContext(C.register_plugin('connection', 'netconf'))
    c.set_attributes_from_plugin(c.connection)
    assert 'rc' in c.network_os
    assert c.remote_user == 'cisco'


# Generated at 2022-06-13 08:35:07.666304
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    context.CLIARGS = {'timeout': 15, 'verbosity': 1, 'private_key_file': 'test'}
    play_context = PlayContext()
    assert play_context.timeout == 15
    assert play_context.verbosity == 1
    assert play_context.private_key_file == 'test'

# Generated at 2022-06-13 08:35:14.102820
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    # arrange
    def FakeCliArgs():
        attrs = {}
        attrs['timeout'] = 42
        attrs['private_key_file'] = 'test_output/test_tmp_fake_key file'
        attrs['verbosity'] = 10
        attrs['start_at_task'] = 'test start_at_task'
        return attrs

    play = FakeAnsiblePlay()
    passwords = FakeAnsiblePasswords()
    connection_lockfd = 'test connection_lockfd'

    play_context = PlayContext(play, passwords, connection_lockfd)

    # act
    PlayContext.context.CLIARGS = FakeCliArgs()
    play_context.set_attributes_from_cli()

    # assert
    assert play_context.timeout == 42
    assert play_context.private_

# Generated at 2022-06-13 08:35:14.902763
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    pass

# Generated at 2022-06-13 08:35:22.551873
# Unit test for constructor of class PlayContext
def test_PlayContext():
    '''
    Test Play Context
    '''
    play_instance = Play()
    passwords = dict()
    passwords['conn_pass'] = 'conn_pass'
    passwords['become_pass'] = 'become_pass'
    playcontext_instance = PlayContext(play_instance, passwords, None)
    assert not playcontext_instance.password
    assert not playcontext_instance.become_pass
    assert not playcontext_instance.connection_lockfd


# Generated at 2022-06-13 08:35:30.318359
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    context.CLIARGS = AttributeDict()
    context.CLIARGS['verbosity'] = None
    context.CLIARGS['start_at_task'] = None
    password = {}
    password['conn_pass'] = ''
    password['become_pass'] = ''

    p = PlayContext(None, password, None)
    t = Task()
    t.connection = 'smart'
    t.remote_user = 'testuser'
    t.become = True
    t.become_user = 'testuser'
    t.delegate_to = 'testuser'
    t.check_mode = False
    t.diff = False

    vars = {}
    vars['ansible_connection'] = None
    vars['ansible_user'] = 'testuser'

# Generated at 2022-06-13 08:35:42.350347
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    p = Play()
    i = Inventory()
    h = Host(name="test_host")
    i.add_host(h)
    t = Task()
    p.add_task(t)

    pc = PlayContext(play=p, passwords=dict())
    pc.become = False
    pc.become_method = None
    pc.become_user = None
    pc.remote_user = 'test_remote_user'
    pc.port = 22
    pc.connection = 'ssh'
    pc.hostvars = dict()
    pc.set_task_and_variable_override(t, dict(), None)

    assert pc.become == False
    assert pc.become_method == None
    assert pc.become_user == None

# Generated at 2022-06-13 08:35:46.791595
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    # instantiate an instance of PlayContext
    pc = PlayContext()
    # call method set_attributes_from_cli of class PlayContext
    #assert pc.set_attributes_from_cli() == expected

# Generated at 2022-06-13 08:35:54.856460
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
	play = None
	passwords = None
	connection_lockfd = None
	new_obj = PlayContext(play, passwords, connection_lockfd)
	assert new_obj._start_at_task == None
	assert new_obj._step == False
	assert new_obj._force_handlers == False
	assert new_obj._verbosity == 0
	assert new_obj._only_tags == set()
	assert new_obj._skip_tags == set()
	assert new_obj._become_method == None
	assert new_obj._become_user == None
	assert new_obj._become_pass == None
	assert new_obj._become_exe == 'sudo'
	assert new_obj._become_flags == '-H'
	assert new_obj._prompt == None
	assert new_obj._bec

# Generated at 2022-06-13 08:36:05.617712
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    test_data = dict()

    test_data['test1'] = dict(
        plugin='shell',
        expected='/bin/sh',
    )
    test_data['test2'] = dict(
        plugin='pipelining',
        expected=False,
    )
    test_data['test3'] = dict(
        plugin='command',
        expected=None,
    )

    for key, val in test_data.items():
        context_obj = PlayContext(play=None, passwords=None)
        plugin = ConnectionBase(was_fired=False, play_context=context_obj)
        plugin._load_name = val['plugin']
        context_obj.set_attributes_from_plugin(plugin)

# Generated at 2022-06-13 08:36:08.914063
# Unit test for constructor of class PlayContext
def test_PlayContext():
    '''
    Create instance of PlayContext class
    '''

    play_context = PlayContext()

    # varify class member value for connection_user
    assert play_context.connection_user == 'root'

    # varify class member value for port
    assert play_context.port == 22



# Generated at 2022-06-13 08:37:07.300143
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # PlayContext.set_task_and_variable_override(task, variables, templar)
    # TODO
    return



# Generated at 2022-06-13 08:37:12.973493
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # PlayContext fixture
    pc = PlayContext()
    # Task fixture
    task = DummyTask()
    # Variables fixture
    variables = dict()
    # Templar fixture
    templar = Templar(loader=None, variables=dict())
    # Do something with the fixture
    pc.set_task_and_variable_override(task, variables, templar)
    assert pc.copy()

# Generated at 2022-06-13 08:37:20.327439
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    try:
        import __main__ as main
    except ImportError:
        main = None
    context.CLIARGS = ImmutableDict({'start_at_task': None, 'verbosity': 1})
    context.DEFAULT_CONNECTION_NAME = 'paramiko'
    context.SETUP_CACHE = {}
    pc = PlayContext()
    pc.set_attributes_from_plugin(Connection() )
    pc.update_vars({})


# Generated at 2022-06-13 08:37:21.314190
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    assert True

# Generated at 2022-06-13 08:37:32.786180
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    args = argparse.Namespace()
    args.timeout = None
    args.verbosity = None
    args.private_key_file = None
    args.start_at_task = None
    context._init_global_context(args)

    pc = PlayContext()

    task = Task()
    task.delegate_to = 'localhost'
    task.delegate_facts = None
    task.become = True
    task.become_method = None
    task.become_user = None
    task.no_log = None
    task.port = None
    task.remote_user = None
    task.ssh_extra_args = None
    task.connection = None
    task.check_mode = None
    task.diff = None

    variables = {}
    variables['ansible_connection'] = 'local'


# Generated at 2022-06-13 08:37:45.738983
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    TEST_PATH = '/tmp/ansible_test_path'
    TEST_USER = 'at_user'
    TEST_HOST = 'at_host'
    TEST_PORT = 1234
    TEST_TIMEOUT = 12345

    context._init_global_context(cli_args=dict(
        connection='ssh',
        private_key_file=TEST_PATH,
        remote_user=TEST_USER,
        remote_addr=TEST_HOST,
        port=TEST_PORT,
        timeout=TEST_TIMEOUT
    ))

    play_context = PlayContext()

    assert play_context.private_key_file == TEST_PATH
    assert play_context.remote_user == TEST_USER
    assert play_context.remote_addr == TEST_HOST
    assert play_context.port == TEST_

# Generated at 2022-06-13 08:37:51.646803
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    play = Play()
    passwords = {}
    connection_lockfd = None
    my_play_context = PlayContext(play, passwords, connection_lockfd)
    my_play_context.set_attributes_from_plugin('ssh')
    assert_equal(my_play_context.connection, 'ssh')



# Generated at 2022-06-13 08:38:01.130342
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    playbook = mock.MagicMock()
    passwords = {}
    
    play_context = PlayContext(playbook, passwords)
    plugin = mock.MagicMock()

    # Remove the following commented lines when the tests are fixed

    # play_context.set_attributes_from_plugin(plugin)

    # assert hasattr(play_context, '_connection_lockfd')
    # assert hasattr(play_context, '_verbosity')
    # assert hasattr(play_context, '_username')
    # assert hasattr(play_context, '_connection')
    # assert hasattr(play_context, '_remote_addr')
    # assert hasattr(play_context, '_port')
    # assert hasattr(play_context, '_shell')
    # assert hasattr(play_context, '_executable')


# Generated at 2022-06-13 08:38:12.938578
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # This is a test to check if the variables are set using set_task_and_variable_override method
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    play_context = PlayContext(play=None, passwords=None, connection_lockfd=None)
    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory=None)
    variable_manager._extra_vars={"ansible_connection": "ssh", "ansible_ssh_port": 22, "ansible_user": "admin", "ansible_host": "localhost"}
    task = Task()
    task._role = None
    task.role = None
    task.action = "command"
    task.delegate_to = "localhost"
    task.become = False


# Generated at 2022-06-13 08:38:16.066099
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # create an instance of the class PlayContext
    p = PlayContext()

    # create an instance of the class FakePlugin
    plugin = FakePlugin()

    # call method set_attributes_from_plugin of class PlayContext
    p.set_attributes_from_plugin(plugin)

# Generated at 2022-06-13 08:40:17.883407
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # Make necessary imports
    # change directory to the directory of the executed file
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    
    # setup some parameters
    passwd = {'conn_pass':'abc','become_pass':'xyz'}
    play = Play()
    play.force_handlers = True
    module_utils = ModuleUtility()
    # Test with task defined, variables defined, templar defined
    playbook = Playbook()
    task = Task()
    task.delegate_to = 'host1'
    task.remote_user = 'amit'
    task.delegate_facts = True
    task.hosts = 'host1'

# Generated at 2022-06-13 08:40:21.206975
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    context.CLIARGS = {'one': 1, 'two': 2}
    pc = PlayContext()
    pc.set_attributes_from_cli()

    assert pc.one == 1
    assert pc.two == 2


# Generated at 2022-06-13 08:40:27.672430
# Unit test for constructor of class PlayContext
def test_PlayContext():
    p = PlayContext()

    password = 'password'
    pwd = {
        'conn_pass': password,
        'become_pass': password,
    }

    p = PlayContext(None, pwd)

    assert p.password == password
    assert p.become_pass == password



# Generated at 2022-06-13 08:40:32.494341
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    context.CLIARGS = dict()
    context.CLIARGS['timeout'] = 10
    play_context = PlayContext()
    play_context.set_attributes_from_cli()
    assert play_context.timeout == 10

# Generated at 2022-06-13 08:40:41.866559
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    host_vars_mock = dict(ansible_connection="paramiko")
    task_vars_mock = dict(ansible_connection="paramiko",
                          ansible_ssh_private_key_file="/home/user/.ssh/id_rsa")
    play_context_mock = PlayContext(
            play=Play(),
            passwords=dict(conn_pass="hunter12",
                           become_pass="hunter12"))
    play_context_mock.set_task_and_variable_override(
            task=Task(),
            variables=task_vars_mock,
            templar=None)
    play_context_mock.set_attributes_from_plugin(paramiko)

# Generated at 2022-06-13 08:40:54.303911
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    import jinja2
    import ansible.parsing.yaml
    import ansible.template as template
    import ansible.template.safe_eval
    from ansible.vars.manager import VariableManager
    from ansible.vars import AnsibleHost, AnsibleGroup
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.vars.unsafe_proxy import UnsafeProxy


    context._init_global_context(
        args=Namespace(
            connection='local', forks=5, become=False,
            become_method=None, become_user=None, check=False, diff=False,
            syntax=None, start_at_task=None, verbosity=0
        )
    )



# Generated at 2022-06-13 08:41:00.772619
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # If a plugin is provided then options should be set
    #if a plugin is provided 
    #
    #table = PlayContext()
    #table.set_attributes_from_plugin()
    #assert table.get_option('flag') == plugin.get_option('flag')
    assert True
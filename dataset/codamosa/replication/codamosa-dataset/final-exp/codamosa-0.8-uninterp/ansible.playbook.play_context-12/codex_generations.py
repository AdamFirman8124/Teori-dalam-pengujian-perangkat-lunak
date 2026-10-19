

# Generated at 2022-06-13 08:31:32.382381
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    p = PlayContext()
    p.set_attributes_from_plugin(Facts())
    assert p.timeout == 10


# Generated at 2022-06-13 08:31:41.689094
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    import os
    import tempfile
    def mock_get(path, params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=10,
                 allow_redirects=True, proxies=None, verify=True, stream=None, cert=None):
        return path

    def mock_post(path, data=None, json=None, files=None, params=None, headers=None, cookies=None, auth=None, timeout=10,
                  allow_redirects=True, proxies=None, verify=True, stream=None, cert=None):
        return path


# Generated at 2022-06-13 08:31:47.082413
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    plugin = get_plugin_loader('nxos_facts').get(get_plugin_class('nxos_facts'))

    PlayContext_obj = PlayContext()

    PlayContext_obj.set_attributes_from_plugin(plugin)

    return '{}'.format(PlayContext_obj)

# Generated at 2022-06-13 08:31:55.452290
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import TASK_ATTRIBUTE_OVERRIDES
    from ansible.template import Templar
    from ansible.template.vars import VariableManager
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.dataloader import DataLoader
    # Testing the method set_task_and_variable_override with the class PlayContext.
    options = None
    play = None
    host = 'localhost'
    hostv

# Generated at 2022-06-13 08:32:08.073820
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from ansible.plugins.loader import connection_loader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.playbook import Playbook
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

    plugin = connection_loader.get('smart')
    plugin.set_options(direct={'ansible_ssh_common_args': 'test_args'})

    dl = DataLoader()
    pc = PlayContext()
    play = Play().load({}, variable_manager=dl, loader=dl)
    play._file_name = 'test'
    pc.set_attributes_from_plugin(plugin)

# Generated at 2022-06-13 08:32:13.053089
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():

    my_play_context = PlayContext()

    # We do not have a valid option for timeout but it is a field so should get set to default
    my_play_context.set_attributes_from_cli()
    assert my_play_context.timeout == 'unset-timeout'
    # Overload CLIARGS with some good values
    context.CLIARGS = {'timeout': 10} # timeout is set to 10
    my_play_context.set_attributes_from_cli()
    assert my_play_context.timeout == 10
    # Now we need to make sure the private_key_file works
    context.CLIARGS = {'private_key_file': '/home/my_user/.ssh/id_rsa'} # private_key_file is set to a valid path
    my_play_context.set_

# Generated at 2022-06-13 08:32:21.347785
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    class TestPlayContext(PlayContext):
        _test = FieldAttribute(isa='string')

        def __init__(self):
            super(TestPlayContext, self).__init__(play=None, passwords=None, connection_lockfd=None)

    plugin = mock.MagicMock()
    plugin.get_option.side_effect = lambda name: getattr(self, name) if name == 'flag' else None
    test_instance = TestPlayContext()
    test_instance.flag = 'test_flag'

    test_instance.set_attributes_from_plugin(plugin)

    assert test_instance.test == 'test_flag'



# Generated at 2022-06-13 08:32:22.674896
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    # TODO
    pass

# Generated at 2022-06-13 08:32:34.363318
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # creating a PlayContext and setting the task connection is local
    pc1 = PlayContext()
    # checking that the task connection is local
    assert pc1.connection == 'paramiko'
    # checking the default value of remote_user
    assert pc1.remote_user == 'paramiko'
    # creating a PlayContext, overridding the task connection and setting the remote_user
    pc2 = PlayContext()
    # checking that the task connection is now smart ssh
    assert pc2.connection == 'smart'
    # checking that the remote_user has been changes
    assert pc2.remote_user == 'smart'


# Generated at 2022-06-13 08:32:39.971341
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from ansible.plugins.loader import get_plugin_class

    path = '/home/hongkliu/ansible/lib/ansible/plugins/connection/ssh.py'
    plugin_class = get_plugin_class(path)

    play_context = PlayContext()
    play_context.set_attributes_from_plugin(plugin_class)
    return dir(play_context)

# Generated at 2022-06-13 08:32:57.617661
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # Test the PlayContext class
    p = mock.MagicMock()
    t = mock.MagicMock()
    t.tags = []
    t.tags.append('tag1')
    t.tags.append('tag2')
    p.tasks = [t]
    p.roles = 'roles'
    p.handlers = 'handlers'
    p.force_handlers = False
    pc = PlayContext(p, None)
    pc.set_attributes_from_cli()
    # create a PluginLoader object and set a few attributes
    pl = mock.MagicMock()
    pl._options = {}
    pl._options['test_attr'] = 50
    pl._options['test_attr2'] = 10
    pl._load_name = 'shell.py'
    pl.get_option = mock

# Generated at 2022-06-13 08:33:10.145799
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # Testing the PlayContext method set_attributes_from_plugin()
    #
    # Given: A PlayContext object
    # When: set_attributes_from_plugin() called with plugin
    # Then: Connection parameters are set using plugin attributes

    # Arrange
    pc = PlayContext()
    expected_ssh_common_args = {'ldap_state': False, 'control_path': None, 'ssh_common_args': "", 'set_ssh_param': False, '_play_context': None, 'remote_addr': '1.1.1.1', 'remote_user': 'vagrant', 'password': '', 'port': 2222, 'timeout': 10, 'network_os': None, 'private_key_file': '~/.ssh/id_rsa'}

    # Act
    pc.set_attributes_from

# Generated at 2022-06-13 08:33:26.217861
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    import copy
    import os
    import sys
    import unittest

    # Patch
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import get_plugin_class

    setattr(PlayContext, '_valid_attrs', dict())
    setattr(PlayContext, '_attributes', dict())

    class TestPlayContext(unittest.TestCase):

        def setUp(self):
            context._init_global_context()
            self.play_context = PlayContext(play=None)

        def tearDown(self):
            pass

        def test_set_attributes_from_plugin_usage_of_get_configuration_definitions(self):
            self.play_context.set_attributes_from_plugin('dummy')


# Generated at 2022-06-13 08:33:32.396091
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    play = setup_play_context()

    # Pass
    play.set_attributes_from_plugin(fixture_loader.load_fixture('connection/mock_connection_plugin.py'))

    # Fail
    play.set_attributes_from_plugin(fixture_loader.load_fixture('connection/mock_connection_plugin.py'))

# Generated at 2022-06-13 08:33:37.272882
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    task = Task()
    variables = dict()
    templar = Templar()
    play_context_object = PlayContext()

    play_context_object.set_task_and_variable_override(task, variables, templar)
    assert not play_context_object

# Generated at 2022-06-13 08:33:52.321659
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():

    # asserting test case #6
    newinfo1 = PlayContext()
    task1 = TaskInclude()
    task1.vars = dict(ansible_become_pass='pass1', ansible_port=1234, ansible_connection='connection_smart', ansible_remote_user='user2', become_user='test_become_user')
    variables = dict(ansible_become_pass='pass1', ansible_port=1234, ansible_connection='connection_smart', ansible_remote_user='user1', ansible_user='user1')
    templar = Templar()
    res1 = newinfo1.set_task_and_variable_override(task1, variables, templar)
    assert res1._become_pass == 'pass1'
    assert res1._port == 1234


# Generated at 2022-06-13 08:33:57.731668
# Unit test for method set_task_and_variable_override of class PlayContext

# Generated at 2022-06-13 08:34:02.399836
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    # Test with no CLIARGS
    context.CLIARGS = {}

    pc = PlayContext()

    # Test with CLIARGS
    context.CLIARGS = {"timeout": "42"}
    pc = PlayContext()
    assert pc.timeout == 42


# Generated at 2022-06-13 08:34:06.218213
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():

    new_info = PlayContext()
    new_info.set_task_and_variable_override(task, variables, templar)
    return



# Generated at 2022-06-13 08:34:16.999469
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    task_name = 'test_task'
    delegate_to = None
    no_log = False
    connection = 'connection'
    remote_user = 'remote_user'
    a_port = 0
    private_key_file = 'private_key_file'
    timeout = 0
    become = False
    verbosity = 0
    other_variables = {'key1': value1,
                      'key2': value2,
                      'remote_user': value3,
                      'port': value4}

# Generated at 2022-06-13 08:34:49.475194
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
  pass

# Generated at 2022-06-13 08:34:51.698254
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    mock_plugin = MagicMock()
    pc = PlayContext(play=None, passwords=None)
    pc.set_attributes_from_plugin(plugin=mock_plugin)

# Generated at 2022-06-13 08:34:54.069934
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # stub for test_PlayContext_set_attributes_from_plugin
    assert True


# Generated at 2022-06-13 08:35:05.340090
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    my_ansible_vars = dict()
    my_ansible_vars['ansible_private_key_file'] = 'super secret key file'
    my_ansible_vars['ansible_verbosity'] = 2
    cli_args = dict()
    cli_args['verbosity'] = 3
    cli_args['private_key_file'] = 'not so secret key file'
    cli_args['timeout'] = 11
    context.CLIARGS = cli_args
    pc = PlayContext(connection_lockfd = 0)
    pc.set_task_and_variable_override(None, my_ansible_vars, None)
    assert pc.private_key_file == 'not so secret key file'
    assert pc.timeout == 11
    assert pc.verbosity == 3




# Generated at 2022-06-13 08:35:11.938662
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # make sure we can get the attributes of a plugin
    p = PlayContext()
    p.set_attributes_from_plugin(MySQLSession())
    assert p._mysql_user == None
    assert p._mysql_pass == None
    assert p._mysql_port == None
    p._attributes['mysql_user'] = 'foo'
    p._attributes['mysql_pass'] = 'bar'
    p._attributes['mysql_port'] = 'baz'
    assert p._mysql_user == 'foo'
    assert p._mysql_pass == 'bar'
    assert p._mysql_port == 'baz'

# Generated at 2022-06-13 08:35:24.429579
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # params
    play = 'test_play'
    passwords = 'test_passwords'
    connection_lockfd = 'test_connection_lockfd'

    test_os_path_sep = os.path.sep

    # arrange
    # original_get_configuration_definitions = C.config.get_configuration_definitions
    C.config.get_configuration_definitions = MagicMock()

    # act
    sut = PlayContext(play, passwords, connection_lockfd)
    # assert
    assert sut.connection == ''
    assert sut.remote_addr == ''
    assert sut.remote_user == 'root'
    assert sut.password == ''
    assert sut.port == None
    assert sut.private_key_file == '~/.ssh/id_rsa'


# Generated at 2022-06-13 08:35:31.211909
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # Setup mocks
    # pylint: disable=W0613,W0612
    class MockClass(object):
        def __init__(self, **kwargs):
            for k, v in iteritems(kwargs):
                setattr(self, k, v)
    plugin = MockClass(get_option=lambda x: None)
    # pylint: disable=W0612
    def get_plugin_class(inp):
        return MockClass(
            get_option=lambda x, y=None: None,
            _load_name="plugins/connection"
        )

    play = MockClass(
        connection=MockClass(),
        serialize=MockClass(),
        serialize_attrs=['connection', 'serialize']
    )


# Generated at 2022-06-13 08:35:43.189558
# Unit test for method set_task_and_variable_override of class PlayContext

# Generated at 2022-06-13 08:35:48.471150
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    play_context = PlayContext()
    task = MagicMock()
    variables = MagicMock()
    templar = MagicMock()
    new_info = play_context.set_task_and_variable_override(task, variables, templar)
    assert isinstance(new_info, PlayContext)
    assert isinstance(task, PlayContext)


# Generated at 2022-06-13 08:35:54.766021
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    from ansible.plugins import connection_loader
    from ansible.plugins.loader import connection_loader as plugin_loader
    pc = PlayContext()
    plugin = connection_loader.get('local')
    testconfig = C.config
    testconfig.data = {'plugins': {'connection': {}}}
    testconfig.set_config_type('connection_plugins')
    testconfig.set_config_type('connection')
    testconfig.set_config_type('ssh_args')
    testconfig.load()
    pc.set_attributes_from_plugin(plugin)
    assert isinstance(pc, PlayContext)



# Generated at 2022-06-13 08:37:05.818467
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # Unittest 01: Set task and variable override of PlayContext class
    play = Play()
    play.remote_user = "test_remote_user"
    play.become_method = "test_become_method"
    play.become = "test_become"
    play.force_handlers = "test_force_handlers"
    play.verbosity = "test_verbosity"
    play.connection = "test_connection"
    play.timeout = "test_timeout"
    task = Task()
    task.remote_user = "test_remote_user"
    task.become_method = "test_become_method"
    task.become = "test_become"
    task.force_handlers = "test_force_handlers"

# Generated at 2022-06-13 08:37:11.329954
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    class FakePlay(object):
        def __init__(self):
            self.force_handlers = False

    class FakeOptions(object):
        def __init__(self, name, value=None, module_class=None, module_name=None):
            self.name = name
            self.value = value
            self.module_class = module_class
            self.module_name = module_name

    class FakePlugin(object):
        def __init__(self, load_name, name, option_list=[]):
            self._load_name = load_name
            self.name = name
            self.options = dict()
            for option in option_list:
                self.options[option.name] = option
            self.method_names = option_list

        def get_option(self, name):
            return self

# Generated at 2022-06-13 08:37:22.579519
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    mock_connection_plugins = {
        'local': Mock(get_option=Mock(return_value=True)),
        'paramiko': {'ssh': Mock(get_option=Mock(return_value=True))},
        'ssh': Mock(get_option=Mock(return_value=True))
    }

    pc = PlayContext(Mock())
    pc.set_attributes_from_plugin(mock_connection_plugins['local'])
    assert pc._pipelining is True, "_pipelining is not True on PlayContext"
    assert pc._connection == 'local', "_connection is not 'local' on PlayContext"

    pc = PlayContext(Mock())
    pc.set_attributes_from_plugin(mock_connection_plugins['ssh'])

# Generated at 2022-06-13 08:37:23.754348
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    pass  # Nothing to do here

# Generated at 2022-06-13 08:37:28.602521
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    play_context = PlayContext(play=None, passwords=None, connection_lockfd=None)
    variables = {}
    task = Task()
    play_context.set_task_and_variable_override(task, variables, "templar")


# Generated at 2022-06-13 08:37:36.775528
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # Create a class 'MyClass'
    class MyClass():
        pass

    my_class_instance = MyClass()
    my_class_instance.test_attribute = "Test Attribute"

    # Construct an instance of PlayContext
    c = PlayContext()

    # Assert the attribute 'test_attribute' is set to a default value
    assert getattr(c, test_attribute) == "Test Attribute"

    # Call method set_attributes_from_plugin of PlayContext
    c.set_attributes_from_plugin(my_class_instance)

    # Assert the attribute 'test_attribute' is set to 
    assert getattr(c, test_attribute) == "Test Attribute"



# Generated at 2022-06-13 08:37:49.308713
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # noinspection PyUnresolvedReferences
    from ansible.module_utils.six.moves import builtins

    class AnsibleModule(object):
        def __init__(self, *args, **kwargs):
            pass

    class AnsibleModule_fail_json(AnsibleModule):
        def fail_json(self, *args, **kwargs):
            raise BaseException('AnsibleModule.fail_json called')

    class AnsibleModule_exit_json(AnsibleModule):
        def exit_json(self, *args, **kwargs):
            raise BaseException('AnsibleModule.exit_json called')

    class AnsibleModule_no_exit_or_fail(AnsibleModule):
        pass


# Generated at 2022-06-13 08:37:58.566951
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    import ansible.plugins.connection as connection_plugins
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.utils.display import Display
    context.CLIARGS = {
        'timeout': False
    }

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()
    templar = Templar(loader=loader, variables=variable_manager.get_vars(play=None))
    display = Display()


# Generated at 2022-06-13 08:38:00.681223
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    my_info = PlayContext()
    my_info.set_attributes_from_plugin(my_info)


# Generated at 2022-06-13 08:38:09.606279
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    obj = PlayContext(play=None, passwords=None, connection_lockfd=None)

    obj.set_attributes_from_cli()
    assert isinstance(obj._attributes['timeout'], int)
    assert isinstance(obj._attributes['private_key_file'], basestring)
    assert isinstance(obj._attributes['verbosity'], int)
    assert isinstance(obj._attributes['start_at_task'], basestring)
    assert obj._attributes['verbosity'] == 0

# Generated at 2022-06-13 08:39:15.974253
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    """
    Test that set_task_and_variable_override() method
    of PlayContext class works as expected.
    """
    # initialize PlayContext instance
    play = None
    passwords = {}
    connection_lockfd = None
    play_context = PlayContext(play, passwords, connection_lockfd)

    # initialize task object with some valid values
    task = Mock()
    task.port = 8080
    task.check_mode = True
    task.delegate_to = "localhost"
    task.diff = False
    task.remote_user = "local"

    # initialize variables
    variables = dict()
    variables["ansible_user"] = "delegated_user"
    variables["ansible_pass"] = "delegated_pass"
    variables["ansible_port"] = "22"

# Generated at 2022-06-13 08:39:18.233723
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    p = PlayContext()
    assert p is not None


# Generated at 2022-06-13 08:39:27.751938
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    p = PlayContext()
    with patch('ansible.module_utils.common.set_module_args', return_value=None, autospec=True) as mock_set_module_args:
        with patch.object(p, 'get_option', return_value='sample_value', autospec=True) as mock_get_option:
            p.set_attributes_from_cli()

# Generated at 2022-06-13 08:39:30.105027
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # TODO: make sure this is tested by a unit test
    pass


# Generated at 2022-06-13 08:39:31.143107
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    pass

# Generated at 2022-06-13 08:39:39.885859
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    play_context = PlayContext(play=None, passwords=None, connection_lockfd=None)
    task = None
    variables = None
    templar = None
    new_info = play_context.set_task_and_variable_override(task=task, variables=variables, templar=templar)
    if new_info is None:
        assert False, "Expected an exception to be thrown"



# Generated at 2022-06-13 08:39:48.900895
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    ansible = Ansible()
    ansible._initialize()
    play = Play().load(dict(
        name="foobar",
        gather_facts="no",
        hosts="all",
        remote_user="remote_user",
        remote_port=22,
        connection='local',
        tasks=[],
    ), variable_manager=ansible.vars)
    task = Task()
    task._variable_manager = ansible.vars
    play.set_loader(ansible._loader)
    task.load(dict(
        name="dummy",
        action=dict(module="dummy"),
    ))
    vars = dict()
    pc = PlayContext(play=play, passwords={})
    # set up variables for use in tests
    ansible.vars.extra_vars = dict()
    ansible

# Generated at 2022-06-13 08:40:00.275289
# Unit test for constructor of class PlayContext
def test_PlayContext():
    play = Play().load({
        'name': 'test play',
        'hosts': 'all',
        'connection': 'local',
        'gather_facts': 'no',
        'tasks': []
    }, variable_manager=VariableManager())
    play_context = PlayContext(play=play)
    assert play_context.connection == 'local', 'connection is not local'
    assert play_context.remote_addr is None, 'remote_addr is not None'
    assert play_context.remote_user == C.DEFAULT_REMOTE_USER, 'remote_user is not root'

    assert play_context.remote_port is None, 'remote_port is not None'
    assert play_context.timeout == C.DEFAULT_TIMEOUT, 'timeout is not default'

# Generated at 2022-06-13 08:40:08.195059
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    # PlayContext = collections.namedtuple('PlayContext', ['host', 'name', 'port', 'remote_user', 'password', 'private_key_file', 'connection', 'timeout', 'shell', 'ssh_executable', 'ssh_args', 'sftp_extra_args', 'scp_extra_args', 'become', 'become_method', 'become_user', 'become_pass', 'become_exe', 'become_flags', 'verbosity', 'only_tags', 'skip_tags', 'check', 'syntax', 'diff', 'force_handlers', 'start_at_task', 'step', 'start_at_task'])
    ssh_executable = 'ssh'
    ssh_args = '-C -o ControlMaster=auto -o ControlPersist=60s'
    pipelining = False


# Generated at 2022-06-13 08:40:19.532380
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    # Private copy of C.CLIARGS for unit testing
    _CLIARGS = {"timeout": None, "private_key_file": None, "verbosity": None, "start_at_task": None}
    with patch.dict(context.__dict__, {"CLIARGS": _CLIARGS}), patch.dict(C.__dict__, {"DEFAULT_TIMEOUT": None, "DEFAULT_PRIVATE_KEY_FILE": None, "ANSIBLE_PIPELINING": None, "DEFAULT_BECOME_EXE": "sudo", "DEFAULT_BECOME_FLAGS": "-H"}):
        pc = PlayContext(play=None, passwords=None, connection_lockfd=None)
        assert not hasattr(pc, "_connection_lockfd")
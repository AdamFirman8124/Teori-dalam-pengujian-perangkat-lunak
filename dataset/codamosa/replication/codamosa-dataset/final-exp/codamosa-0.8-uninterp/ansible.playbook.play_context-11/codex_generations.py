

# Generated at 2022-06-13 08:31:30.394247
# Unit test for method update_vars of class PlayContext
def test_PlayContext_update_vars():
    # PlayContext.update_vars() == unittest
    return None


# Generated at 2022-06-13 08:31:39.921042
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():

    class TestPlayContext(PlayContext):
        def __init__(self):
            pass

    class TestPlayContext_set_attributes_from_play(BaseTest):
        playbook_name = 'test_PlayContext_set_attributes_from_play.yml'
        playbook_path = ""
        task_name = 'test_PlayContext_set_attributes_from_play'

    class TestPlayContext_set_attributes_from_task(BaseTest):
        playbook_name = 'test_PlayContext_set_attributes_from_task.yml'
        playbook_path = ""
        task_name = 'test_PlayContext_set_attributes_from_task'


# Generated at 2022-06-13 08:31:47.337861
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    p = PlayContext()
    try:
        if p.set_attributes_from_plugin is not None:
            p.set_attributes_from_plugin(connection=None)
            p.set_attributes_from_plugin(connection='smart')
            p.set_attributes_from_plugin('smart')
    except Exception as e:
        assert False, "Unable to call set_attributes_from_plugin on PlayContext"

# Generated at 2022-06-13 08:31:49.229742
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    context._init_global_context(CONFIG_OPTIONS)
    play_context = PlayContext()
    plugin_class = None
    plugin = None
    play_context.set_attributes_from_plugin(plugin)

# Generated at 2022-06-13 08:31:56.666360
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    playbook = Playbook()
    play = Play()
    plays = [play]
    playbook._entries = plays

    # Now we set up the test data for class AnsiblePlaybookExecutor
    #
    # class AnsiblePlaybookExecutor(object):
    #
    #     def __init__(self,
    #                  playbooks,
    #                  inventory,
    #                  variable_manager,
    #                  loader,
    #                  options,
    #                  passwords,
    #                  ):
    #
    # We need a Play() object
    #
    # class Play(object):
    #     def __init__(self,
    #                  play=None,
    #                  hosts='all',
    #                  name=None,
    #                  strategy='',
    #                  vars=None,
    #                  ports=

# Generated at 2022-06-13 08:32:04.253445
# Unit test for constructor of class PlayContext
def test_PlayContext():
    play = Play()
    play.load = dict(
        connection='ssh',
        remote_user='nobody',
        port='22',
        become_user='Bob',
    )
    pc = PlayContext(play, dict())
    assert pc.connection == 'ssh'
    assert pc.remote_user == 'nobody'
    assert pc.port == 22
    assert pc.become_user == 'Bob'



# Generated at 2022-06-13 08:32:09.751210
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    #test for remote_user variable
    play_context = PlayContext()
    play_context.remote_user = 'test_user'
    task = Task()
    task.remote_user = 'new_user'
    variable = dict()
    variable['ansible_ssh_user'] = 'ansible_ssh_user'
    variable['ansible_user'] = 'ansible_user'
    play_context.set_task_and_variable_override(task, variable)
    assert play_context.remote_user == 'new_user'
    task = Task()
    task.remote_user = None
    play_context.set_task_and_variable_override(task, variable)
    assert play_context.remote_user == 'ansible_ssh_user'
    task.remote_user = None

# Generated at 2022-06-13 08:32:10.520674
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    assert 1==1

# Generated at 2022-06-13 08:32:12.862105
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    args = {'ssh_extra_args': 'extra_args', 'timeout': '60', 'private_key_file': 'some_file.pem', 'verbosity': 55}
    context.CLIARGS = args
    con_info = PlayContext()
    assert con_info.timeout == 60
    assert con_info.private_key_file == 'some_file.pem'
    assert con_info.verbosity == 55



# Generated at 2022-06-13 08:32:22.514154
# Unit test for method set_attributes_from_cli of class PlayContext

# Generated at 2022-06-13 08:32:43.384202
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    p = PlayContext()
    p.set_attributes_from_plugin(provider="local")
    assert p.connection == "local"
    

# Generated at 2022-06-13 08:32:53.730458
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    from ansible.vars import VariableManager
    variable_manager = VariableManager()
    variable_manager._extra_vars = {}

    variable_manager._extra_vars = {'ansible_connection': 'local'}
    play_context = PlayContext(play=None)
    play_context.set_task_and_variable_override(task=None, variables=variable_manager._extra_vars, templar=None)

    assert 'ansible_connection' in play_context._attributes
    assert 'connection' in play_context._attributes
    assert play_context._attributes['ansible_connection'] == 'local'
    assert play_context._attributes['connection'] == 'local'

    variable_manager._extra_vars = {'ansible_user': 'test_user'}
    play_context = Play

# Generated at 2022-06-13 08:33:00.133770
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.context import _init_context
    from ansible.playbook.play import Play
    from ansible.executor import module_common
    from ansible.plugins.loader import load_plugin

    _init_context()
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, sources=['localhost,'])
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 08:33:01.920279
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # TODO Add test for set_task_and_variable_override
    pass

# Generated at 2022-06-13 08:33:12.799795
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # First lets instantiate the class
    instance = PlayContext()
    # now lets set some values on the class

    # test with no task
    instance.set_task_and_variable_override(None, dict(), dict())

    # test with no variables
    instance.set_task_and_variable_override(True, None, dict())

    # test with no templar
    instance.set_task_and_variable_override(True, dict(), None)

    # test with all values
    instance.set_task_and_variable_override(True, dict(), dict())

    # play context should never have a value from the task, since the play has a higher precedence
    assert getattr(instance, 'become', None) == None

    # this shows what you can expect from setting values on task
    test_task = Task()

# Generated at 2022-06-13 08:33:14.966051
# Unit test for constructor of class PlayContext
def test_PlayContext():
    play_context = PlayContext(play=object)
    assert play_context is not None

# Generated at 2022-06-13 08:33:29.930433
# Unit test for method update_vars of class PlayContext
def test_PlayContext_update_vars():
    '''
    Unit test for method update_vars of class PlayContext of ansible/playbook/__init__.py
    '''

    context.CLIARGS = ImmutableDict()
    context.CLIARGS['verbosity'] = 0
    context.CLIARGS['no_log'] = True
    context.CLIARGS['inventory'] = os.path.abspath("../../../test/integration/inventory/hosts")

    play = Play().load("../../../test/integration/playbooks/playbook_test.yml", variable_manager=VariableManager(), loader=DataLoader())
    playcontext = PlayContext(play=play)
    task = play.get_iterator()._playbook[0]
    variable_manager = VariableManager()

# Generated at 2022-06-13 08:33:31.030827
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # Can`t be tested because of _load_name
    pass


# Generated at 2022-06-13 08:33:32.933405
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # instantiate from class
    data = PlayContext()


# Generated at 2022-06-13 08:33:35.213757
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    """ test_PlayContext_set_attributes_from_plugin """

    


# Generated at 2022-06-13 08:34:19.871493
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    assert True

# Generated at 2022-06-13 08:34:20.985746
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    check_connections_not_overridden()


# Generated at 2022-06-13 08:34:27.665449
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    v = ansible.module_utils.basic.AnsibleModule(
        argument_spec={'a': dict(required=True)},
        supports_check_mode=True
    )

    context.CLIARGS = dict()

    class DummyPlugin(object):
        @staticmethod
        def get_option(x):
            return 42 if x == 'a' else None

    p = PlayContext()

    p.set_attributes_from_plugin(DummyPlugin())
    assert p.a == 42



# Generated at 2022-06-13 08:34:39.523143
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # Method set_attributes_from_plugin of class PlayContext with args plugin
    play = Play()
    passwords = {}
    connection_lockfd = None
    pc = PlayContext(play, passwords, connection_lockfd)
    plugin = 'basic'
    try:
        pc.set_attributes_from_plugin(plugin)
    except Exception as e:
        print(str(e))
        assert False

    # Method set_attributes_from_play of class PlayContext with args play
    play = Play()
    passwords = {}
    connection_lockfd = None
    pc = PlayContext(play, passwords, connection_lockfd)
    try:
        pc.set_attributes_from_play(play)
    except Exception as e:
        print(str(e))
        assert False

    # Method set_attributes_

# Generated at 2022-06-13 08:34:41.535748
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    context = PlayContext()
    new_plugin = 'new_plugin'
    context.set_attributes_from_plugin(new_plugin)


# Generated at 2022-06-13 08:34:53.325629
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # Test whether a plugin will be able to link to Playcontext.
    plugin = AnsiblePlugin()
    play = Play()
    play.set_attribute('tasks', [])
    plugin.connection = PlayContext(play)
    plugin.set_attributes_from_play()
    plugin.set_attributes_from_cli()
    plugin.set_attributes_from_plugin()
    try:
        assert plugin.connection.connection is initialized
        assert plugin.connection.connection_user is initialized
        assert plugin.connection.network_os is initialized
    except Exception as e:
        print("Error in setting up attributes for the plugin.\nError:\n{}".format(e))

# Generated at 2022-06-13 08:35:07.215074
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    task = Task()
    task.delegate_to = "localhost"
    task.remote_user = ""
    task.check_mode = ""
    task.diff = ""
    variables = {}
    play = Play()
    play.hostvars = {}
    play.extra_vars = {}
    play.vars = {}
    play.handlers = []
    play.roles = []
    ansible_connection=""
    ansible_executable=""
    ansible_port=""
    templar = Templar(variables=variables)
    play_context = PlayContext(play=play)
    assert isinstance(play_context, PlayContext)
    #check for a class variable
    assert play_context.force_handlers
    #check that the method from_play has been called
    play_context.from_play

# Generated at 2022-06-13 08:35:11.006287
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # Arrange
    task = Task()
    variables = {}
    templar = Templar(loader=None)
    play_context = PlayContext()

    # Act
    new_info = play_context.set_task_and_variable_override(task, variables, templar)

    # Assert
    assert new_info.as_dict() == play_context.as_dict()


# Generated at 2022-06-13 08:35:23.618672
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():

    class MockPlay(object):
        def __init__(self):
            self.force_handlers = False
    class MockTask(object):
        def __init__(self):
            self.delegate_to = None
            self.become = False
            self.become_user = None
            self.become_method = None
            self.remote_user = None
            self.check_mode = None
            self.diff = None
            self.serial = None
            self.tags = None
            self.skip_tags = None
            self.any_errors_fatal = False
            self.no_log = None
            self.environment = None
            self.connection = None
            self.port = None
            self.transport = None

    context.CLIARGS = dict()

    templar = MockTempl

# Generated at 2022-06-13 08:35:33.556509
# Unit test for constructor of class PlayContext
def test_PlayContext():
    # Constructor(play=None, options=None, passwords=None)
    pc = PlayContext(play=None, options=None, passwords=None)
    assert pc.password == ''
    assert pc.become_pass == ''
    assert pc.remote_addr == ''
    assert pc.connection == 'smart'
    assert pc.remote_user == 'root'
    assert pc.port == 22
    assert pc.timeout == C.DEFAULT_TIMEOUT
    assert pc.private_key_file == C.DEFAULT_PRIVATE_KEY_FILE
    assert pc.verbosity == 0
    assert pc.start_at_task == None
    assert pc.step == False
    assert pc.force_handlers == False

    # Constructor(play=None, options=None, passwords=None)

# Generated at 2022-06-13 08:36:54.397530
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # Check that a delegation host has the correct variables
    # Check that a loop on a delegation host has the correct variables
    pass


# Generated at 2022-06-13 08:37:06.944110
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    # create template object to create host object
    templar = Templar(loader=None)

    # create play object and set vars
    play_obj = Play()

# Generated at 2022-06-13 08:37:16.560359
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    play_context = PlayContext()
    task = Task(name='test')
    task.delegate_to = 'localhost'
    task.delegate_facts = False
    variables = dict()
    templar = Templar(loader=None, variables=None)
    play_context.set_task_and_variable_override(task=task, variables=variables, templar=templar)
    print(play_context.connection)
    print(play_context.connection_user)
    print(play_context.remote_user)
    print(play_context.remote_addr)


test_PlayContext_set_task_and_variable_override()

# Generated at 2022-06-13 08:37:21.448825
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    plugin = _MockPlugin()
    play = _MockPlay()
    passwords = dict()
    connection_lockfd = None
    play_context = PlayContext(play, passwords, connection_lockfd)
    play_context.set_attributes_from_plugin(plugin)
    assert play_context.play_uid == 1


# Generated at 2022-06-13 08:37:32.917811
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    """
    Test that PlayContext.set_attributes_from_cli
    1. sets timeout from context.CLIARGS
    2. sets private_key_file from context.CLIARGS
    3. sets verbosity from context.CLIARGS
    4. sets start_at_task from context.CLIARGS
    """
    
    context.CLIARGS = {'timeout': '12345',
                       'private_key_file': 'my_pem_file',
                       'verbosity': '2',
                       'start_at_task': 'mytask'}
    pc = PlayContext()
    pc.set_attributes_from_cli()
    
    assert pc.timeout == 12345
    assert pc.private_key_file == 'my_pem_file'
    assert pc.verbosity == 2

# Generated at 2022-06-13 08:37:45.956604
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():
    import ansible.playbook.task
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.six import string_types
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    # testing is_local_become
    p = PlayContext()
    p.become = True
    p.become_method = 'pbrun'
    p.become_user = 'root'
    assert not p.is_local_become()
    p.become_method = 'su'
    assert p.is_local_become()
    p.become = False
    assert not p.is_local_become()

    # setting/getting attributes

# Generated at 2022-06-13 08:37:53.880657
# Unit test for method set_task_and_variable_override of class PlayContext
def test_PlayContext_set_task_and_variable_override():

    ############################################################################
    # Test cases for when task is not a delegate_to task
    ############################################################################
    play_context = PlayContext(play=None, passwords=None, connection_lockfd=None)
    play_context.set_attributes_from_cli()
    play_context.set_attributes_from_play(namedtuple('play', 'vars')(vars=dict()))
    # case 1

# Generated at 2022-06-13 08:37:58.066913
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    play_context = PlayContext()
    play_context.set_attributes_from_plugin(play_context)
    assert_equal(play_context.network_os, None)
    assert_equal(play_context.verbosity, 0)

# Unit tests for method update_vars of class PlayContext

# Generated at 2022-06-13 08:38:00.040306
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    context = PlayContext()
    context.set_attributes_from_plugin("name")
# Test case for PlayContext class

# Generated at 2022-06-13 08:38:11.976443
# Unit test for method set_attributes_from_cli of class PlayContext
def test_PlayContext_set_attributes_from_cli():
    context.CLIARGS = {'timeout': 123, 'private_key_file': 'my_key'}
    instance = PlayContext(play=None, passwords=None, connection_lockfd=None)
    instance.set_attributes_from_cli()
    assert instance.timeout == 123
    assert instance.private_key_file == 'my_key'
    assert instance.verbosity == 0
    assert instance.start_at_task == None

    context.CLIARGS = {'verbosity': 4}
    instance = PlayContext(play=None, passwords=None, connection_lockfd=None)
    instance.set_attributes_from_cli()
    assert instance.verbosity == 4

    context.CLIARGS = {'start_at_task': 'test_task'}

# Generated at 2022-06-13 08:41:11.126583
# Unit test for method set_attributes_from_plugin of class PlayContext
def test_PlayContext_set_attributes_from_plugin():
    # Test no plugin_class
    try:
        pc = PlayContext()
        pc.set_attributes_from_plugin(None)
    except Exception as e:
        assert isinstance(e, AttributeError)
    # Test plugin_load_name
    try:
        pc = PlayContext()
        pc.set_attributes_from_plugin(PluginLoader(''))
    except Exception as e:
        assert isinstance(e, AttributeError)
    # Test plugin_class
    try:
        pc = PlayContext()
        pc.set_attributes_from_plugin(get_plugin_class('action'))
    except Exception as e:
        raise e
    # Test no option
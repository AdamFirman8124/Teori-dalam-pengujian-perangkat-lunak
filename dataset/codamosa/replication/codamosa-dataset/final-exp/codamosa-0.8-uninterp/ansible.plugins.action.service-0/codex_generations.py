

# Generated at 2022-06-13 10:26:55.763359
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=dict(async_val=0, args=dict(), async_seconds=0), connection=dict(host='10.0.0.1', port=22, user='ansible'))

# Generated at 2022-06-13 10:26:56.875632
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 'ActionModule'


# Generated at 2022-06-13 10:26:59.144416
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialization
    am = ActionModule(task=dict(), connection=dict())

    # Test normal operation
    assert am.run(tmp=None, task_vars=None) == {}

# Generated at 2022-06-13 10:27:00.236392
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False, "No tests written for %s" % __file__

# Generated at 2022-06-13 10:27:08.131177
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # initialize request
    data = {
        'use': 'auto',
        'name': 'a',
        'state': 'a',
        'enabled': 'a',
    }
    shared_loader_obj = None

    # initialize test module
    test_module = ActionModule(
        task=data,
        connection=None,
        _play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=shared_loader_obj)

    # initialize test module with variables
    test_module.run(tmp=None, task_vars={'aaa': 'aaa'})

# Generated at 2022-06-13 10:27:18.643810
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module.task_vars = {}
    module.task_vars['ansible_service_mgr'] = 'auto'
    module.task_vars['ansible_facts']['service_mgr'] = 'auto'
    module.task_vars['hostvars'] = {}
    module.task_vars['hostvars']['delegate_to'] = 'auto'
    module.task_vars['hostvars']['ansible_facts'] = {'service_mgr': 'auto'}
    module.task_vars['hostvars']['ansible_service_mgr'] = 'auto'
    module.shared_loader_obj = {}
    module.shared_loader_obj.module_loader = {}
    module.shared_loader_obj.module_loader

# Generated at 2022-06-13 10:27:27.549247
# Unit test for constructor of class ActionModule
def test_ActionModule():
   kv = {"use": 'auto'}
   kv.update({"args": None}) 
   kv.update({"delegate_to": None})
   kv.update({"async_val": None})
   kv.update({"async_pid": None})
   kv.update({"async_jid": None})
   kv.update({"action": "service", "name": "my_service", "state": "started"})
   kv.update({"tmp": None}) 
   kv.update({"task_vars": None})
   kv.update({"notified_by": None})
   kv.update({"notify_timeout": None})
   kv.update({"notify_flag": None})

# Generated at 2022-06-13 10:27:30.390372
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    self = None
    tmp = None
    task_vars = None
    obj = ActionModule()
    obj.run(tmp, task_vars)


# Generated at 2022-06-13 10:27:32.260447
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule({}, {}, {})
    assert am.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:27:40.060940
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    class MockModule(object):
        def __init__(self, lib_b):
            self.lib_b = lib_b

        def get_action_args_with_defaults(self, a, b, c, d):
            return {'key1':'value1'}

        def has_plugin(self, act):
            return 'has_plugin' == act

    class MockModuleLoader(object):
        def __init__(self, lib_b):
            self.lib_b = lib_b

        def find_plugin_with_context(self, a, b):
            class MockContext(object):
                def __init__(self, lib_b):
                    self.lib_b = lib_b
                    self.resolved_fqcn = 'resolved_fqcn'


# Generated at 2022-06-13 10:27:55.810198
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager.set_inventory(inventory)
    options = Options()
    variable_manager.extra_vars = {'inventory_hostname': 'localhost'}


# Generated at 2022-06-13 10:28:08.536389
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:28:16.745059
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import sys
    if sys.version_info[0] >= 3:
        from io import StringIO
    else:
        from StringIO import StringIO

    backup_stdout = sys.stdout
    try:
        sys.stdout = StringIO()

        import ansible.plugins.loader
        import ansible.plugins.action

        ansible.plugins.loader.find_plugins()
        for name, cls in ansible.plugins.action.ActionModule._plugins.items():
            if cls.__mode__ == 'passthru':
                continue
            module = cls()
            assert module
    finally:
        sys.stdout = backup_stdout

# Generated at 2022-06-13 10:28:19.999464
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(loader=None, task=None, connection=None, play_context=None, loader_cache=None, variable_manager=None, templar=None)
    assert action.name == 'auto'
    assert action.short_description == 'Common module for managing services'

# Generated at 2022-06-13 10:28:26.452903
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import mock
    from ansible.plugins.action import ActionModule
    from ansible.plugins.loader import load_plugin_to_bytecode_cache
    load_plugin_to_bytecode_cache('action', 'setup', None)
    load_plugin_to_bytecode_cache('action', 'service', None)
    load_plugin_to_bytecode_cache('action', 'raw', None)
    load_plugin_to_bytecode_cache('action', 'ping', None)

    shared_loader = mock.MagicMock()
    shared_loader.module_loader = mock.MagicMock()
    shared_loader.module_loader.has_plugin = mock.MagicMock()
    shared_loader.module_loader.has_plugin.return_value = True
    connection = mock.MagicMock()
    connection._shell = mock

# Generated at 2022-06-13 10:28:31.219004
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import sys
    import os

    # Code here to initialize and set attributes of the module object (module)
    # e.g. module.name = 'asdf'
    action_module = ActionModule()
    #assert action_module.__init__() == None, "Action Module Constructor does not return None type. This is bad!"

# Generated at 2022-06-13 10:28:41.613638
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.plugins.loader import action_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    from ansible.module_utils.facts.system.service_mgr import ServiceMgrLinuxSystemd
    import os

    # Preparing some values to be used in the test
    data_path = os.path.join(os.path.dirname(__file__), '../../lib/ansible/plugins/action')
    loader = action_loader.ActionModuleLoader(data_path, '', False)

# Generated at 2022-06-13 10:28:42.687467
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    return True

# Generated at 2022-06-13 10:28:46.438332
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Constructor of class ActionModule should set the required
    attributes of the object.
    """
    my_action = ActionModule()
    assert my_action._connection.connection

# Generated at 2022-06-13 10:28:58.387184
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MockActionBase:
        def __init__(self):
            self._supports_check_mode = None
            self._supports_async = None
            self._task = None
            self._templar = None
            self._shared_loader_obj = None
            self._connection = None
            self._display = None
            self._remove_tmp_path = MockRemoveTmpPath()

    class MockTemplar:
        def __init__(self):
            self._task = None
            self._templar = None

        def template(self, template_string):
            return template_string

    class MockTask:
        def __init__(self):
            self._parent = None
            self._task = None
            self._play = None
            self.async_val = None

# Generated at 2022-06-13 10:29:11.820776
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()

# Generated at 2022-06-13 10:29:20.612451
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Pre-requisites
    pip install pytest pytest-mock
    py.test test_ansible_action_module.py -s -v
    """
    # hack to make sure that we are using ansible.module_utils.basic otherwise mock.patch will fail
    import ansible.module_utils.basic
    import ansible.modules.system.service
    import ansible.utils.display
    import ansible.legacy.service
    from ansible.executor.task_result import TaskResult

    from mock import Mock, patch
    from collections import namedtuple
    from ansible.plugins.action import ActionBase

    # Test module ansible.plugins.action.service

# Generated at 2022-06-13 10:29:29.018356
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with a reasonable example
    task_vars_dict = dict(ansible_check_mode=False)
    task_vars = TaskVars(vars=task_vars_dict)

    module = ActionModule(task=Task(
        dict(
            action=dict(module_name='service', args=dict(name='systemd-hostnamed', state='started', enabled=True))
        )
    ), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    module.run(tmp=None, task_vars=task_vars)

    # Test with a invalid module name
    module_dict = dict(name='systemd-hostnamed', state='started', enabled=True)


# Generated at 2022-06-13 10:29:38.909752
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test with a simple argument
    argument = 'TestString'
    a = ActionModule(argument)
    assert a._task.args == {'_raw_params': 'TestString'}

    # test with a more complex argument
    argument = {'use': 'TestDict'}
    b = ActionModule(argument)
    assert b._task.args == {'use': 'TestDict', '_raw_params': ''}
    print('ActionModule constructors tests passed!')

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:29:47.965956
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible import context
    from ansible.utils.display import Display
    from ansible.utils.loader import AnsibleLoader
    from ansible.utils.vars import combine_vars
    from ansible.template import Templar

    # initialize
    options = context.CLIOptions()
    options.tags = ['all']
    options.skip_tags = ['never']
    display = Display()

    loader = AnsibleLoader(None, '', '', None)
    templar = Templar(loader=loader, variables={})
    shared_loader_obj = AnsibleLoader(None, None, None, None)

    # create task

# Generated at 2022-06-13 10:30:02.068670
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    fake_loader = DictDataLoader(dict(
        my_defaults={"use": "auto", "name": "httpd"},
        my_task_vars=dict(),
        my_facts=dict(
            ansible_facts=dict(service_mgr="auto"))
    ))
    fake_play_context = PlayContext()
    fake_play_context._plugin_loader = fake_loader

    fake_task = Task()
    fake_task._attributes = dict()
    fake_task._parent = fake_play_context
    fake_task._loader = fake_loader
    fake_task.args = dict(use="auto", name="httpd")

    fake_action = ActionModule()
    fake_action._task = fake_task
    fake_action._connection = Connection()
    fake_action._templar = Templar

# Generated at 2022-06-13 10:30:02.589636
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:30:06.503501
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(
        task=dict(args=dict(name='sample', state='absent')),
        connection=dict(host='sample', port=1234),
        shell=dict(),
        become=dict(user='sample', exe='/usr/bin/sample'),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )
    assert action is not None

# Generated at 2022-06-13 10:30:07.334018
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:30:07.777265
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 10:30:43.466204
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:30:54.922872
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import ansible.plugins.action.service as serv
    from ansible.module_utils.facts.system.service_mgr import ServiceMgr
    import ansible.modules.system.service
    from ansible.module_utils._text import to_text

    sm = ServiceMgr()
    sm.init()

    # Test expected module to be chosen for service
    task = DummyTask()
    task.args = {"name":"httpd", "state":"started"}
    task.async_val = 0
    task.delegate_to = False
    task._parent = DummyParentTask()
    task_vars = dict()

    # Setup initial module state
    mod = sm.module_name()
    task_vars['service_mgr'] = mod
    task_vars['ansible_facts'] = dict()
    task

# Generated at 2022-06-13 10:31:05.596853
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up a mock task.
    mock_task = MagicMock()

    mock_task.args = {'use': 'auto', 'src': '/path/to/src'}
    mock_task.delegate_to = None

    # Set up a mock config.
    mock_config = MagicMock()
    mock_config.get_config_value.return_value = False

    # Set up a mock display.
    mock_display = MagicMock()

    # Set up a mock loader with a mocked "find_plugin" method.
    mock_loader = MagicMock()
    mock_loader.find_plugin.return_value.resolved_fqcn.return_value = True

    # Set up a mock templar.
    mock_templar = MagicMock()

    # Set up a mock shared loader obj with

# Generated at 2022-06-13 10:31:12.316330
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, None)
    assert am.TRANSFERS_FILES is False
    assert am.UNUSED_PARAMS == {
        'systemd': ['pattern', 'runlevel', 'sleep', 'arguments', 'args'],
    }
    assert am.BUILTIN_SVC_MGR_MODULES == set(['openwrt_init', 'service', 'systemd', 'sysvinit'])

# Generated at 2022-06-13 10:31:18.110804
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_result = {}
    test_task_vars = {}

    test_action = ActionModule(
        task=dict(
            action=dict(
                args=dict()
            )
        ),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )

    assert test_action is not None

# Generated at 2022-06-13 10:31:23.625738
# Unit test for constructor of class ActionModule
def test_ActionModule():
    host = '127.0.0.1'
    task = dict(
        action=dict(
            module_name='service',
            module_args=dict(name='nginx')
        )
    )
    task_vars = {
        'service_mgr': 'auto'
    }

    actionModule = ActionModule(host, task, task_vars)
    assert actionModule.run(task_vars=task_vars)

# Generated at 2022-06-13 10:31:26.327697
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Tests constructor with default arguments
    action_module = ActionModule(None, None, None, None, None)
    assert action_module._supports_check_mode == True
    assert action_module._supports_async == True
    assert action_module.BUILTIN_SVC_MGR_MODULES == set(['openwrt_init', 'service', 'systemd', 'sysvinit'])

# Generated at 2022-06-13 10:31:28.773605
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create a module
    module = ActionModule(task=dict(), connection=dict(), play_context=dict())

    # verify no exceptions are raised
    module.run(None, None)

# Generated at 2022-06-13 10:31:39.431206
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # this method returns a list of modules sorted by their name
    # list of modules found in action_plugins directory
    # list is generated by parsing plugin files
    # in this test, there is a test_plugin.py file, but no
    # test_plugin.pyc file, so this method retrieves
    # only one module, test_plugin
    def get_modules():
        modules_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'action_plugins')
        modules_list = []

# Generated at 2022-06-13 10:31:47.054183
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("test ActionModule.run")
    
    class Host:
        def __init__(self, name):
            self.name = name
    
    class Task:
        def __init__(self):
            self.async_val = 0

    class ActionModule:
        def __init__(self):
            self._task = Task()
            self._task.delegate_to = Host('testhost')
    
    am = ActionModule()
    assert am._task.delegate_to

    am._task.delegate_to = Host('testhost')
    assert am._task.delegate_to

    am._task.delegate_to = Host(None)
    assert not am._task.delegate_to

    # This should not throw an exception, even when calling delegator_host = None
    #assert am.run

# Generated at 2022-06-13 10:32:47.648819
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
       Unit test for method run of class ActionModule
    '''
    # Create a ActionModule instance
    action_module_instance = ActionModule(connection=None,
                                              action_loader=None,
                                              action_results=None,
                                              action_plugins=None,
                                              action_original_file=None,
                                              action_context=None)
    # Create a test task
    task = MockTask()
    # Call the run method

    result = action_module_instance.run(tmp=None,
                                           task_vars=None)
    print(result)


# Generated at 2022-06-13 10:32:50.257538
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None, None)
    assert action_module is not None

# Generated at 2022-06-13 10:32:57.659409
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(
        task=dict(args={"use": "service"}, delegate_to="1.1.1.1"),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    result = a.run()
    assert result['failed'] is False

# Generated at 2022-06-13 10:33:01.443307
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' test callback '''

    # TODO: construct test to verify 'systemd' is used on Fedora and OpenWrt, 'openwrt_init' is used on OpenWrt, and 'service' is used everywhere else
    assert True

# Generated at 2022-06-13 10:33:10.660366
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:33:17.535754
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._collections_compat import Mapping

    # TypeError: load_module() missing 1 required keyword-only argument: '_original_path'
    # <FakeModule name='ansible.module_service.py' path='/home/reach/devel/ansible/lib/ansible/modules/core/system/service.py'>
    # <FakeModule name='ansible.module_service.pyc' path='/home/reach/devel/ansible/lib/ansible/modules/core/system/service.pyc'>
    # <FakeModule name='ansible.module_service.pyo' path='/home/reach/devel/ansible/lib/ansible/modules/core/system/service.pyo'>


# Generated at 2022-06-13 10:33:18.108492
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:33:19.950389
# Unit test for constructor of class ActionModule
def test_ActionModule():
    connection = Mock()
    connection._shell.tmpdir = ""

    module = ActionModule(
        connection=connection,
        task_vars={"test_task_vars": "test_task_vars"})
    assert module is not None


# Generated at 2022-06-13 10:33:28.409576
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_args = {}
    task_vars = {}
    connection = 'local'
    tmp = '/file'
    task_uuid = 'uuid'

    ### Check the cases using 'service' module ###

    # Check case where async = true, delegating to different host
    module = ActionModule(task=MockTask('auto', module_args, async_val=True, delegate_to='other_host'),
                          connection=connection,
                          play_context={'remote_addr': 'localhost'},
                          loader=None,
                          templar=None,
                          shared_loader_obj=None)
    result = module.run(tmp, task_vars)

# Generated at 2022-06-13 10:33:38.943745
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create a mock task
    task_original = dict(use="auto", name="test_service_name")
    task = dict(name="test_service_name")  # 'use' is removed from args before task is passed to _execute_module
    task_vars = dict()
    results = dict(failed=False, changed=False)
    results.update(dict(msg="Test msg"))  # this is used to pass msg to the results
    results.update(task_vars)  # add task_vars to the results
    module_name = "ansible.legacy.service"

    # create mock objects
    templar = MockTemplar()
    module_loader = MockModuleLoader()
    display = MockDisplay()
    connection = MockConnection()
    task_copy = task.copy()
    task_copy.update

# Generated at 2022-06-13 10:35:45.692537
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print('Testing ActionModule constructor')
    try:
        action_module_obj = ActionModule()
        print('PASS')
    except NotImplementedError as e:
        print('FAIL')


# Generated at 2022-06-13 10:35:52.234143
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from . import ModuleTestCase
    from .testdata import TestServiceManager

    # Test case to check the functionality of ActionModule.run
    class TestActionModuleRun(ModuleTestCase):

        # Test case to check service operation
        def test_run(self):
            # Run the with test data
            result = TestActionModuleRun.module.run(
                tmp=None,
                task_vars=dict(ansible_facts=dict(service_mgr=TestServiceManager.FACTS))
            )

            # Verify the result of the operation
            self.assertResult(
                dict(
                    msg='service operation successful',
                    changed=False,
                    ansible_facts={},
                    meta={}
                ),
                result
            )

        # Test case to check the service operation failure

# Generated at 2022-06-13 10:36:00.413723
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json
    import os

    # Set up parameters.
    tmp = ""
    task_vars = {}
    task_vars['ansible_facts'] = {}
    task_vars['ansible_facts']['service_mgr'] = "auto"

    # Create and initialize ActionModule class.
    am = ActionModule(tmp, task_vars)

    # Get current directory and set up file name.
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    file_name = cur_dir + "/files/test_action_module_data.json"

    # Open file and read test data.
    with open(file_name, 'r') as fp:
        test_data = json.load(fp)

    # Test run method.

# Generated at 2022-06-13 10:36:01.053737
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:36:02.295603
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module._task = None
    module.run()

# Generated at 2022-06-13 10:36:06.955501
# Unit test for constructor of class ActionModule
def test_ActionModule():
    tmp = None
    task_vars = None
    action_module = ActionModule(tmp, task_vars)

    assert action_module.TRANSFERS_FILES == False
    assert action_module.BUILTIN_SVC_MGR_MODULES == set(['openwrt_init', 'service', 'systemd', 'sysvinit'])

# Generated at 2022-06-13 10:36:09.061185
# Unit test for constructor of class ActionModule
def test_ActionModule():
    act = ActionModule()
    assert act.run is not None

# Generated at 2022-06-13 10:36:10.780584
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None, None, None)
    module.run()

# Generated at 2022-06-13 10:36:23.536281
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible import context

    options = context.CLIOptions()
    host = context.CLI.make_inventory_host('')
    fm = context.CLIFactoryLoader()
    tqm = fm.create_tqm(host, options)
    task = tqm.load()._tasks[0]
    task.loop = 'test'
    task_vars = dict(
        ansible_service_mgr='auto',
    )

    am = ActionModule(task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    am.run(tmp='/tmp', task_vars=task_vars)

# Generated at 2022-06-13 10:36:29.061868
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule(None, {"name": "test"}, '', '', '', '', '', '', [], {})
    m._connection = None
    m._task = None
    m._shared_loader_obj = None
    m._display = None
    m._templar = None

    with pytest.raises(AnsibleActionFail):
        m.run()
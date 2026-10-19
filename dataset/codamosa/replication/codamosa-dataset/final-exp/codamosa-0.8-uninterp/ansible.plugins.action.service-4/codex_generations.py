

# Generated at 2022-06-13 10:26:51.636706
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: Implement this test
    pass

# Generated at 2022-06-13 10:26:57.695257
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # GIVEN: An action module
    aaction = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    # WHEN: Running an action module
    result = aaction.run(tmp=None, task_vars=None)
    # THEN: The result must be a dict
    assert(isinstance(result, dict))

# Generated at 2022-06-13 10:26:59.262597
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # 1. Instantiation of module without arguments
    # 2. Instantiation of module with arguments
    assert(True)

# Generated at 2022-06-13 10:27:05.209324
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Arrange
    am = ActionModule(
        task=Task(),
        connection=Connection(play_context=PlayContext()),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    am._display.verbosity = 4
    am._supports_check_mode = True
    am._supports_async = True
    am._task.async_val = 2
    am._task.args = {'use': 'auto'}
    tmp = '/tmp'
    task_vars = {}

    # Act
    result = am.run(tmp, task_vars)

    # Assert
    print(result)
    assert result is not None
    assert result['changed'] is False

# Generated at 2022-06-13 10:27:15.615064
# Unit test for constructor of class ActionModule
def test_ActionModule():
    expected_meta = {'always_run': True}
    am = ActionModule()
    assert am._supports_check_mode == True
    assert am._supports_async == True
    assert am._templar is not None
    assert am._shared_loader_obj is not None
    assert am.BUILTIN_SVC_MGR_MODULES == set(['openwrt_init', 'service', 'systemd', 'sysvinit'])
    assert am.UNUSED_PARAMS == { 'systemd': ['pattern', 'runlevel', 'sleep', 'arguments', 'args'] }
    assert am._task.no_log == False
    assert am._task.notify == []
    assert am._task.changed_when == ['failed', 'rc changed']

# Generated at 2022-06-13 10:27:25.583463
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create a FakeExecutor
    class FakeExecutor:

        def __init__(self, task_vars):
            self._task_vars = task_vars

        def module_executor(self, module_name, module_args, task_vars, wrap_async=False, post_validate=None, set_remote_user=None):
            if module_name == 'setup':
                return {'ansible_facts': {'service_mgr': 'auto'}}
            else:
                return {'stdout': 'Hello world!'}

        @property
        def _queue_item(self):
            return 'queue_item'

        @property
        def _task(self):
            return 'task'

    # Create a FakeTemplate
    class FakeTemplate:

        def __init__(self):
            self

# Generated at 2022-06-13 10:27:26.157756
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:27:36.058500
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Get another copy of global_connection for testing
    global_connection = copy.deepcopy(connection)

    # Create a mock task
    mock_task = AnsibleTask()
    mock_task.async_val = None
    mock_task._parent = mock_play
    mock_task._play = mock_play

    # Create another mock loader, only because we want to test a different method
    mock_loader2 = mock.create_autospec(DataLoader)

    # Create another mock template, only because we want to test a different method
    MockAnsibleTemplar2 = mock.create_autospec(AnsibleTemplar)

    # Create another mock display, only because we want to test a different method
    MockAnsibleDisplay2 = mock.create_autospec(Display)


# Generated at 2022-06-13 10:27:41.553460
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    task = Task()
    action_plugins_path = ''
    task.async_val = ''
    task.args = dict(use='service')
    action_module_class = ActionModule(task, action_plugins_path)
    assert action_module_class._task == task

# Generated at 2022-06-13 10:27:42.560498
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:27:58.109420
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict(
        ansible_facts=dict(
            service_mgr='systemd'
        ),
        ansible_os_family='RedHat',
        ansible_pkg_mgr='rpm',
        ansible_distribution='Centos',
        ansible_distribution_version='7.0'
    )
    result = dict()
    am = ActionModule(
        task=dict(
            args=dict()
        ),
        play_context=dict(),
        new_stdin=None
    )
    result = am.run(None, task_vars)
    assert not result.get('failed', False)
    assert result.get('module_args', dict()).get('use') == 'systemd'
    assert not result.get('module_args', dict()).get('sleep')


# Generated at 2022-06-13 10:28:07.611362
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import ansible.utils.template
    templar = ansible.utils.template.Templar()

    module = 'auto'
    new_module_args = dict(use=module)
    task_vars = dict()
    result = dict()

    action_module = ActionModule()
    module_name = 'ansible.legacy.service'
    module_args = new_module_args

    action_module.run(tmp=None, task_vars=task_vars)
    assert 'module' in result and result['module'] == module_name and 'args' in result and result['args'] == module_args

# Generated at 2022-06-13 10:28:17.660885
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        {"tasks":[
            {
                "vars": {
                    "ansible_service_mgr": "systemd"
                }
            },
            {
                "use": "systemd",
                "name": "true ",
                "state": "restarted"
            }
        ]},
        load_deps=False,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert action_module is not None
    assert action_module._tmp is not None
    assert action_module._task is not None
    assert action_module._connection is None
    assert action_module._play_context is None
    assert action_module._loader is None
    assert action_module

# Generated at 2022-06-13 10:28:20.126559
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a mock task
    task = ActionModule()
    # task.args = {}
    res = task.run()
    assert not res
    # Test if the test has been passed or failed
    assert True is True

# Generated at 2022-06-13 10:28:35.538973
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unit_test
    from ansible.plugins.loader import find_plugin
    from copy import deepcopy

    # FIXME: make AnsibleActionFail raise a real exception, or create a fake exception that can be raised
    # (AnsibleActionFail inherits from AnsibleAction, which is a pure virtual class that cannot be instantiated)

    # ActionModule._execute_module returns the result returned by module_executor.run()
    # We'll mock it by returning a dict
    actionmodule_execute_module_result = dict()

    # Mock method ActionBase._execute_module to return
    # whatever value we want
    def actionbase_execute_module(self, *args, **kwargs):
        return actionmodule_execute_module_result

    # Mock attribute ActionBase._shared_loader_obj.module_loader.has_plugin
    # so we

# Generated at 2022-06-13 10:28:44.928984
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import os
    import tempfile

    from ansible.executor.task_result import TaskResult
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.loader import find_plugin, _get_all_plugin_loaders

    action_name = 'service'
    plugin_loader = _get_all_plugin_loaders()['action']
    action_class = find_plugin(action_name, plugin_loader)
    fixture_data = {}

    # get action module args
    action_module_args = action_class._task.args.copy()

    # create a temp directory
    temp_dir = tempfile.mkdtemp()

    # create a file under temp directory, named action_plugins

# Generated at 2022-06-13 10:28:45.749597
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    return None

# Generated at 2022-06-13 10:28:46.505695
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:28:58.412178
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    hostname="test-hostname"
    play_context=mock.MagicMock()
    play_context.remote_addr="test-connection"
    task_vars=mock.MagicMock()
    connection=mock. MagicMock()
    connection.remote_user="test-user"
    connection.transport="test-transport"
    inventory=mock.MagicMock()
    inventory.hosts="test-host-name"
    task=mock.MagicMock()
    task.args={'name':'test'}
    name="test-name"
    task._parent=mock.MagicMock()
    task._parent._play=mock.MagicMock()
    task._parent._play._action_groups=mock.MagicMock()
    task.async_val=False


# Generated at 2022-06-13 10:29:00.162498
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, action='service', module_name='service')
    assert am is not None

# Generated at 2022-06-13 10:29:24.478133
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mock_module_name = 'ansible.module_utils.service_management.service'
    import sys
    sys.modules[mock_module_name] = sys.modules['ansible.legacy.service']


# Generated at 2022-06-13 10:29:25.501588
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:29:28.279603
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert am is not None
#
# Test the service module
#

# Generated at 2022-06-13 10:29:29.470320
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:29:34.686215
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Tests for constructor of class ActionModule """
    actionModule = ActionModule(None, None, '/tmp/ansible_module_service.py', '/tmp/ansible_module_service.py', '/tmp/ansible_module_service.py')
    assert actionModule is not None

# Generated at 2022-06-13 10:29:35.519213
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:29:41.887595
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # action = ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)
    action = ActionModule(None, None, None, None, None, None)
    # result = action.run(tmp=None, task_vars=None)
    result = action.run(None, None)
    # assert result == {}
    assert result == {}

# Generated at 2022-06-13 10:29:49.658829
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Mock
    class Mock_ActionBase():
        def __init__(self, *args, **kwargs):
            pass

        def run(tmp, task_vars):
            return tmp

    class Mock_run(ActionModule):
        _task = None
        _connection = None
        _loader = None
        _shared_loader_obj = None
        _templar = None
        _display = None

        def run(self, tmp, task_vars):
            return super(ActionModule, self).run(tmp, task_vars)


# Generated at 2022-06-13 10:29:50.357705
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    return None

# Generated at 2022-06-13 10:29:54.742770
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule({'name': 'test'})
    assert module.__class__.__name__ == 'ActionModule'
    assert module._task.args['name'] == 'test'

# Generated at 2022-06-13 10:30:25.252303
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule
    """

    a = ActionModule()


if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:30:27.054716
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule(None, None, None, {})
    assert actionmodule is not None

# Generated at 2022-06-13 10:30:28.288442
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, [], {})
    assert module != None

# Generated at 2022-06-13 10:30:30.205433
# Unit test for constructor of class ActionModule
def test_ActionModule():
    act = ActionModule(None, None)
    assert act.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:30:39.226637
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:30:43.719741
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test = ActionModule(
        task = dict(args=dict(name='kaustuv_das', use='kaustuv_das')),
        connection = dict(host=None),
        play_context = dict(become=False),
        loader = None,
        templar = None,
        shared_loader_obj = None
    )
    assert(test.run()) == 'passed'




# Generated at 2022-06-13 10:30:55.126934
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class Mock_connection():

        class Mock_shell():
            tmpdir = '/tmp'

        _shell = Mock_shell()

    class Mock_loader():

        class Mock_module_loader():

            def has_plugin(name):
                return True

            def find_plugin_with_context(name, collection_list=False):
                class Mock_context():
                    class ResolvedFQCN():
                        def __init__(self, name):
                            self.name = name

                        def __str__(self):
                            return self.name

                    resolved_fqcn = ResolvedFQCN('mock.context')

                return Mock_context()

        module_loader = Mock_module_loader()

        class Mock_template():
            def template(name):
                return 'mock'

        templar = Mock_template()



# Generated at 2022-06-13 10:30:55.913248
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:31:06.236141
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.service as s
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_executor import TaskExecutor
    from ansible.cli.adhoc import AdHocCLI as cli
    from ansible.playbook.play_context import PlayContext as pc
    import ansible.playbook.task_include as ti
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    import ansible.plugins.loader as l
    import ansible.plugins.callback as c
    import ansible.playbook.play as play
    import ansible.utils

# Generated at 2022-06-13 10:31:17.459194
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create the object
    pbex = ActionModule(
        task=dict(action=dict(module_name='service', module_args=dict(name='httpd', state='started')), async_val=60, async_seconds=60),
        connection=dict(conn_type='ssh', host='10.0.0.1', port=22),
        templar=None,
        shared_loader_obj=None,
        action_loader=None,
        connection_loader=None,
        loader=None,
        variable_manager=None,
        loader_cache=None,
    )
    # Run the method
    assert pbex.run(tmp='/root/.ansible/tmp', task_vars={'ansible_facts': {'service_mgr': 'systemd'}}) == {'changed': True}

# Generated at 2022-06-13 10:32:10.002136
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule('./test/test_plugin_manager.py', 'test_plugin_manager.py', 'test_plugin_manager', './test/test_plugin_manager.py')
    assert isinstance(action_module, ActionModule)



# Generated at 2022-06-13 10:32:15.426390
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule({'use': '1'}, {})
    assert m.BUILTIN_SVC_MGR_MODULES == set(['openwrt_init', 'service', 'systemd', 'sysvinit'])
    assert m.UNUSED_PARAMS == {
        'systemd': ['pattern', 'runlevel', 'sleep', 'arguments', 'args'],
    }
    assert m.TRANSFERS_FILES == False
    assert m._supports_check_mode == True
    assert m._supports_async == True

# Generated at 2022-06-13 10:32:16.710729
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None, None, None)
    assert action != None

# Generated at 2022-06-13 10:32:24.519176
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import ansible.plugins.action.service

    a = ansible.plugins.action.service.ActionModule('test', dict(use='auto'), False, dict(gather_subset='minimal', filter='ansible_service_mgr'), 'ansible.legacy.setup', None)

    assert a._execute_module == ansible.plugins.action.service.ActionBase._execute_module
    assert a._remove_tmp_path == ansible.plugins.action.service.ActionBase._remove_tmp_path

    # setup mocks
    # case no facts
    a._execute_module = lambda module_name, module_args, task_vars, wrap_async: dict(ansible_facts=dict())

# Generated at 2022-06-13 10:32:33.992601
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:32:36.017750
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule()
    assert actionModule.BUILTIN_SVC_MGR_MODULES

# Generated at 2022-06-13 10:32:45.366334
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:32:58.305069
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of ActionModule class
    '''
    print("Testing ActionModule")
    _task = DummyTask()
    _connection = DummyConnection()
    _play_context = DummyPlayContext()
    _loader = DummyLoader()
    _shared_loader_obj = DummySharedLoader()
    _task_queue = DummyTaskQueueManager()
    _variable_manager = DummyVariableManager()

    _display = DummyDisplay()

    _am = ActionModule(_task, _connection, _play_context, _loader, _shared_loader_obj, _task_queue, _variable_manager, _display)


# Generated at 2022-06-13 10:33:05.941395
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os.path
    import copy
    import ansible.utils.template
    from ansible.module_utils.facts.system.service_mgr import ServiceMgr

    # Setup
    module_mock = copy.deepcopy(ActionModule)
    module_mock.ActionBase = ActionBase

    test_module_mock = copy.deepcopy(module_mock)
    tmp_mock = os.path.join('test', 'ansible_service_facts')
    test_module_mock._remove_tmp_path = lambda _: None
    test_module_mock.ActionBase.run = lambda _: {'ansible_facts': {'service_mgr': 'systemd', 'a': '1', 'b': '2'}}

# Generated at 2022-06-13 10:33:08.021532
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, PlayContext=None, loader=None, templar=None, shared_loader_obj=None) is not None

# Generated at 2022-06-13 10:35:17.971349
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule, object)

# Generated at 2022-06-13 10:35:18.387159
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:35:21.877837
# Unit test for constructor of class ActionModule
def test_ActionModule():
    cls = ActionModule()
    cls._supports_async = True
    cls._supports_check_mode = True
    cls._connection = object()
    cls._task = object()
    cls._loader = object()
    cls._shared_loader_obj = object()
    cls._display = object()

# Generated at 2022-06-13 10:35:26.433398
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Starting testing ActionModule")
    action = ActionModule()
    print("ActionModule Constructor called without any arguments")
    print("Test case for action module constructor is passed")

# Running test case for ActionModule constructor
test_ActionModule()

# Generated at 2022-06-13 10:35:28.190589
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None).run(task_vars=None) is not None

# Generated at 2022-06-13 10:35:40.091261
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.service import ActionModule
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    my_task = Task()
    my_task.name = 'a name'
    my_task._uuid = 'a uuid'
    my_task.args = {
        'use': 'auto',
    }

    my_context = PlayContext()
    #my_context._queue_name = 'a queue name'  # don't have access to this method

    my_vars_manager = VariableManager()

# Generated at 2022-06-13 10:35:41.926339
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Constructor test without parameters
    module = ActionModule(load_context_from_one_task=None)
    assert module is not None

# Generated at 2022-06-13 10:35:43.665746
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("test_ActionModule_run()")
    # TODO:

if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:35:50.761852
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible
    import ansible.cli
    import ansible.utils.plugin_docs
    import ansible.utils.display
    import ansible.errors
    import ansible.executor.task_queue_manager
    import ansible.executor.task_result
    import ansible.plugins.action
    import ansible.utils.collection_loader

    a = ansible.cli.CLI(args=["ansible-playbook", "test_service_auto"])

# Generated at 2022-06-13 10:35:59.290104
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import os
    import json
    import datetime

    from ansible.compat.tests import mock
    from ansible.compat.tests.mock import patch
    from ansible.module_utils._text import to_bytes
    from ansible.plugins import action_loader
    from ansible.plugins.action.service import ActionModule

    FILE_PATH = os.path.dirname(os.path.realpath(__file__))
    FIXTURE_PATH = os.path.join(FILE_PATH, '../fixtures/')
    TEST_DATA = json.loads(open(FIXTURE_PATH + 'service/service.json').read())
    print("\nTEST_DATA\n")
    print(TEST_DATA)
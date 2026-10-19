

# Generated at 2022-06-13 09:55:24.894692
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #GIVEN

    #WHEN
    am = ActionModule()

    #THEN
    assert am is not None

# Generated at 2022-06-13 09:55:36.080013
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.loader import action_loader
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook import Play
    import json

    # Load plugins
    plugin_loader = action_loader.ActionModuleLoader(None, '.')
    plugin_loader._package_paths = ['./lib/ansible/plugins/action']
    plugin_loader.find_plugin('action_plugin_loader', 'gather_facts', './lib/ansible/plugins/action/')

    # Create task
    task_t = Task()
    task_t._role = None
    task_t._parent = Play()
    task_t.action = 'action_plugin_loader'
    task_t.module_name = 'gather_facts'


# Generated at 2022-06-13 09:55:40.764372
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule(None, None)
    result = mod.run(None, {'ansible_facts_parallel': True})
    assert result['ansible_facts'] == {'_ansible_facts_gathered': True}
    assert result['_ansible_verbose_override'] is True


# Generated at 2022-06-13 09:55:45.349814
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with a non-existent module and check if the correct exception is raised
    try:
        a = ActionModule()
    except NotImplementedError as e:
        assert "AnsibleModule not implemented" in str(e)
    else:
        assert False

# Generated at 2022-06-13 09:55:50.760845
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(
        task=dict(
            args=dict(),
            action=dict(
                args=dict(),
                module_defaults=dict()
            )
        ),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict(),
        # TODO: Find out how to give a fake "display"
        display=dict()
    )
    assert am._supports_check_mode is True

# Generated at 2022-06-13 09:55:58.461269
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest.mock as mock
    from ansible.executor.task_result import TaskResult

    # setup patcher for patching only the target method of interest, so
    # we can use the same test for all classes derived from object
    patcher = mock.patch.object(ActionModule, 'run', autospec=True)

    # start patcher
    m_run = patcher.start()

    # perform test
    m_run.assert_called_once_with()

    # stop patcher
    patcher.stop()

# Generated at 2022-06-13 09:55:59.137836
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 09:56:03.979052
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Some random variables, just to pass the test
    task_vars = {'a': True, 'b': True, 'c': 'some_str'}
    job_vars = {'d': True}
    tmp = ['/home/user/tmp_path']

    # test __init__ action_module instance
    action_module = ActionModule(
        task=None, connection=None,
        play_context=None, loader=None, templar=None, shared_loader_obj=None
    )

    # test run method of class ActionModule
    # get the result for the run method excution
    # and assert the result
    result = action_module.run(tmp, task_vars)
    assert result == {'ansible_facts': {}}

    # result = action_module.run(tmp, task_v

# Generated at 2022-06-13 09:56:04.663928
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 1

# Generated at 2022-06-13 09:56:14.337472
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from units.compat.mock import MagicMock
    from units.compat.mock import patch

    # Mock objects
    task = MagicMock()
    task.args = {}

    # Setup the module loader
    mock_loader = MagicMock()
    mock_loader.find_plugin_with_context = MagicMock(return_value=
                                                     MagicMock(return_value="mocked_fact_module"))

    # Setup a task object
    task.args = {}
    task_vars = {}
    task.module_defaults = {}
    task._parent = MagicMock()
    task._parent._play = MagicMock()
    task._parent._play._action_groups = {}
    task.action = "setup"
    task.collections = []

    # Setup the action module
    action_module

# Generated at 2022-06-13 09:56:28.526611
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )
    assert actionmodule._supports_check_mode == True

# Generated at 2022-06-13 09:56:39.507734
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    action_module.set_loader(DictDataLoader({}))
    action_module.set_connection(MockConnection())

    action_module.set_runner(MockRunner())
    mock_task = MockTask()
    action_module.set_task(mock_task)
    mock_task._datastore = {}
    mock_task._parent = MockTask()
    mock_task._parent._play = MockPlay()
    mock_task._parent._play._action_groups = {}
    mock_task.args = {'parallel': 'true'}
    action_module._result = {'ansible_facts': {}, 'failed': False, 'skipped': False, 'warnings': []}
    action_module._task.collections = []

    result = action_module.run

# Generated at 2022-06-13 09:56:42.462199
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test ActionModule creation with valid data
    m = ActionModule(host="host", task=dict(),connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(m, ActionModule)
    # test ActionModule creation with invalid data
    try:
        m = ActionModule(host="host", task=None)
        assert isinstance(m, ActionModule)
    except AssertionError:
        pass

# Generated at 2022-06-13 09:56:43.537706
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()


# Generated at 2022-06-13 09:56:46.135509
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    tmp = '/root/tmp'
    module.run(tmp=tmp, task_vars={})

# Generated at 2022-06-13 09:56:55.790472
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.module_utils.common._collections_compat import MutableMapping
    loader, inventory, variable_manager, loader_module, path_finder = TaskQueueManager._load_ansible_galaxy(None)
    loader._add_directory(loader_module._get_path())
    variable_manager.extra_vars = {"foo": "bar"}

# Generated at 2022-06-13 09:56:56.549655
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 09:56:59.069480
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule_test = ActionModule()
    assert bool(actionModule_test) == True


# Generated at 2022-06-13 09:57:00.727548
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 09:57:01.649526
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:57:34.081788
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import mock

    from ansible.plugins.action import ActionModule

    class ArgumentSpec(object):
        def __init__(self):
            self.argument_spec = {}

    action_module = ActionModule(task=mock.Mock(), connection=mock.Mock(), play_context=mock.Mock(), loader=mock.Mock(),
                                 templar=mock.Mock(), shared_loader_obj=mock.Mock())

    # normal path with successful execution
    def get_config_value(key, variables):
        if key == 'FACTS_MODULES':
            return ['module1', 'module2']
        return None
    C.config.get_config_value = get_config_value

    mock_module = mock.Mock()
    mock_module.argument_

# Generated at 2022-06-13 09:57:35.187444
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule, object)


# Generated at 2022-06-13 09:57:44.177123
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import PluginLoader

    tqm = TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=PluginLoader(),
        options=None,
        passwords=None,
        stdout_callback=None,
        run_additional_callbacks=False,
        run_tree=False,
    )

    play_context = PlayContext()
    play_context.become = True

    action_module = ActionModule(
        tqm,
        play_context,
        None,
        None,
        None,
    )

    assert action_module is not None

# Generated at 2022-06-13 09:57:45.667513
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is ActionBase

# Generated at 2022-06-13 09:57:59.339361
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create a fake task object
    task = dict()

    # set the args of the task object
    task['args'] = dict()
    task['args']['network_os'] = 'ios'

    # create a fake module_defaults object
    module_defaults = dict()

    # create a fake task_vars object
    task_vars = dict()

    # set the config_dir of the task_vars object
    task_vars['config_dir'] = '/usr/lib/python2.7/site-packages/ansible/config'

    # create a fake config object
    config = dict()

    # set the string of the config object
    config['FACTS_MODULES'] = '''extras,ansible.legacy.setup'''

    # set the string of the config object

# Generated at 2022-06-13 09:58:06.892037
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()

    class connection_plugin():
        class _load_name():
            def split():
                return ['name']

    class display():
        class vvvv():
            pass

    class config():
        class get_config_value():
            def __call__(self, value1, value2):
                return ['smart']

    class task():
        args = {}
        def __init__(self):
            self.collections = []

    class loader_shared():
        module_loader = 'module_loader'

    class templar():
        def __init__(self):
            self.template = "template"

    class task_vars():
        ansible_facts = {}

    class task_ex():
        _task = task()
        _shared_loader_obj = loader_shared()
        _connection

# Generated at 2022-06-13 09:58:13.617387
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(
        task=dict(args=dict(var1='test_arg')),
        connection=dict(
            _load_name='test_connection',
            _connection=None,
            tmpdir='test_tmp_dir',
            _shell=dict(tmpdir='test_shell_tmp_dir')
        ),
        shared_loader_obj=None,
        templar=None,
        display=None,
        task_vars=dict(),
        variables=dict(),
        loader=None
    )

# Generated at 2022-06-13 09:58:15.194065
# Unit test for constructor of class ActionModule
def test_ActionModule():
    obj = ActionModule(1, 2)
    assert obj != None


# Generated at 2022-06-13 09:58:24.539996
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.vars import merge_hash
    from ansible.executor.task_result import TaskResult
    from ansible.module_utils.six import PY2
    import shutil
    import tempfile
    import json
    import six
    import os
    import sys

    if not PY2:
        try:
            from unittest.mock import patch, MagicMock
        except ImportError:
            from mock import patch, MagicMock
    else:
        from mock import patch, MagicMock

    from ansible.module_utils.facts.network.base import NetworkFactBase
    from ansible.plugins.action import ActionModule
    from ansible.plugins.action.setup import ActionModule as ActionModuleSetup
    from ansible.module_utils.parsing.convert_bool import boolean


# Generated at 2022-06-13 09:58:34.252216
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Tests with wrong parameters or well formed parameters
    o = ActionModule(None, {'test': 'arg'})
    o = ActionModule(None, {})
    o = ActionModule(None, {'ansible_facts_parallel': 'True'})
    o = ActionModule(None, {'ansible_facts_parallel': 'False'})
    o = ActionModule(None, {'ansible_facts_parallel': True})
    o = ActionModule(None, {'ansible_facts_parallel': False})
    o = ActionModule(None, {'ansible_facts_parallel': None})

# Generated at 2022-06-13 09:59:19.635791
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    tmp = None
    task_vars = {'ansible_facts_parallel': False}
    setup = ActionModule(tmp, task_vars)
    setup.run(tmp, task_vars)

# Generated at 2022-06-13 09:59:31.528938
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.facts.network.base import FactsBase

# Generated at 2022-06-13 09:59:33.500545
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(loader=None, connection=None, play_context=None,
                        loader_obj=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 09:59:35.270866
# Unit test for constructor of class ActionModule
def test_ActionModule():

    my_action_module = ActionModule()
    assert True


# Generated at 2022-06-13 09:59:37.254747
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = {}
    tmp = None

    # Create an instance of the ActionModule class.
    action_module = ActionModule(tmp, task_vars)

# Generated at 2022-06-13 09:59:52.329748
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.module_common import ModuleBase

    class MockModuleBase(ModuleBase):
        def __init__(self, *args, **kwargs):
            super(MockModuleBase, self).__init__(*args, **kwargs)

        def run(self, tmp=None, task_vars=None):
            res = TaskResult(host=self._task._host)
            res.action = 'setup'

            res.ansible_facts = {'top_level_fact': 'top_level_value'}
            res.ansible_facts['nested'] = {'nested_key': 'nested_value'}
            res.ansible_facts['list'] = ['list_value_1', 'list_value_2']

            return

# Generated at 2022-06-13 09:59:53.527711
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(isinstance(ActionModule(None, None, None, None, None, None), ActionModule))

# Generated at 2022-06-13 09:59:54.968613
# Unit test for constructor of class ActionModule
def test_ActionModule():
    #This test requires a patched config file and connection plugin file
    actionModule = ActionModule() # A dummy object
    assert hasattr(actionModule, 'run')

# Generated at 2022-06-13 10:00:01.525447
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    class FakeLoader():
        def find_plugin_with_context(self, module_name, collection_list):
            class FakePlugin():
                def __init__(self):
                    self.resolved_fqcn = 'ansible.legacy.setup'
            return FakePlugin()

    class FakeTask():
        def __init__(self):
            self.args = {}
            self.module_defaults = {}
            self._parent = FakePlay()
            self.collections = []

    class FakePlay():
        def __init__(self):
            self._action_groups = []

    class FakeConnection():
        def __init__(self):
            self._load_name = 'local'
            self._shell = FakeShell()


# Generated at 2022-06-13 10:00:03.605926
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:01:47.979242
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule()

# Generated at 2022-06-13 10:01:48.545191
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()

# Generated at 2022-06-13 10:01:55.784578
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # NOTE: These tests are very preliminary and only test the code before the _execute_module call.
    #       These tests need to be further improved to at least test the full method which can be done by mocking
    #       `_execute_module`.
    from ansible.executor.task_queue_manager import TaskQueueManager
    connection = MagicMock()
    connection._load_name = 'network_cli'
    connection._shell.tmpdir = '/tmp/dir'
    task = MagicMock()
    task.tags = []

    # test no setup modules and no parallel
    task.args = {}
    result_1 = ActionModule(task, connection, MagicMock(), MagicMock()).run(MagicMock(), {})

# Generated at 2022-06-13 10:02:09.054565
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = AnsibleModule(
        argument_spec = dict(
            ansible_facts_parallel = dict(type='bool', default=None),
            parallel = dict(type='bool', default=None),
        ),
        supports_check_mode = True,
    )

    # construct the object and assign to module.params
    module.params = dict(
        ansible_facts_parallel = module.params.ansible_facts_parallel,
        parallel = module.params.parallel,
    )

    action_module = ActionModule(module, module.params, "setup_facts")

    result = action_module.run(task_vars=None)

    assert result["ansible_facts"]["_ansible_facts_gathered"] == True

# Generated at 2022-06-13 10:02:15.525538
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    actionmodule = ActionModule()

    fp = open("./test_data/test_module.yml")
    actionmodule._task = yaml.load(fp.read())
    actionmodule._task.args = dict()

    try:
        result = actionmodule.run(tmp=None, task_vars=dict())
    except Exception as e:
        print(e)
        assert False

    assert result['ansible_facts'] == {}
    assert result['warnings'] == []
    assert result['deprecations'] == []

    fp.close()

# Generated at 2022-06-13 10:02:23.502518
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.facts import FactCache
    from ansible.vars.manager import VariableManager

    action_base = ActionBase()
    user_action_module = ActionModule(action_base)
    user_action_module._supports_check_mode = True
    user_action_module._display = type(C.display)()
    user_action_module._task.action = 'setup'
    user_action_module._task.args = {}
    user_action_module._task.collections = []
    user_action_module._shared_loader_obj = type(C.config.loader)(
        C.config.get_config_value('CONFIG_FILE')
    )
    user_action_module._templar = type(C.config.templar)()
    user_action_module._connection

# Generated at 2022-06-13 10:02:33.383579
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import pytest


# Generated at 2022-06-13 10:02:41.105776
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    tas = {
        'name': 'TestExecutor',
        'hosts': ['host1', 'host2'],
        'vars': {'ansible_connection': 'mocked'},
        'tasks': [{'action': 'setup'}]
    }

    res = {
        'ansible_facts': {},
        'warnings': [],
        'deprecations': []
    }

    p = ActionModule(tas, None)
    test_result = p.run({}, {})
    assert test_result == res, "test_ActionModule_run() failed"


if __name__ == "__main__":
    test_ActionModule_run()

# Generated at 2022-06-13 10:02:49.524339
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.setup import ActionModule
    from ansible.executor.task_queue_manager import TaskQueueManager

    connection = None
    _mock_module_command = "/usr/bin/ansible"

    ansible = AnsibleRunner(
        hosts_file="/usr/local/etc/ansible/nodelist.yml",
        module_file="/usr/local/etc/ansible/modules",
        pattern="*.yml",
        module_path="/usr/local/etc/ansible/modules",
        module_name="action",
        module_args="ansible.legacy.setup",
    )
    ansible.execute()

# Generated at 2022-06-13 10:02:59.627076
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Tests the run() method of the ActionModule class

    # Create a mock task
    task = Task()
    task.args = {
        'ansible_facts_parallel': None,
        'parallel': None
    }


    # Create a mock task
    task_vars = dict()
    task_vars['ansible_facts_parallel'] = "True"

    # Create a mock config
    config = dict()
    config['FACTS_MODULES'] = ["test_facts_module"]

    # Create a mock loader
    loader = MockLoader()

    # Create a mock variable manager
    variable_manager = MockVariableManager()

    # Create a mock display
    display = MockDisplay()

    # Create a mock shell
    shell = MockShell()

    # Create a mock connection
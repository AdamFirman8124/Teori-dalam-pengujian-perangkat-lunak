

# Generated at 2022-06-13 10:06:06.391213
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    _task = mock.Mock()
    _task.args = {'dir': 'vars'}
    # set up test variables
    am = ActionModule()
    am._task = _task
    am._set_dir_defaults()
    am._set_root_dir()
    # walk through the directory and further test the iteration
    for root_dir, basenames in am._traverse_dir_depth():
        for basename in basenames:
            filename = path.join(root_dir, basename)
            am._load_files(filename)
            print(filename)

if __name__ == '__main__':
    mocker = Mock()
    test_ActionModule_run()

# Generated at 2022-06-13 10:06:19.049751
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import pytest
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    play_context = PlayContext()

    # source_dir
    action_args = {
        'dir': '../../test/integration/targets/included_vars_dir',
        'depth': 2,
        'ignore_files': '^.*\ignoreme.*$',
        'extensions': 'yaml'
    }
    action_obj = action_loader.get('include_vars',
                                   variable_manager=variable_manager,
                                   loader=variable_manager._loader,
                                   play_context=play_context)

# Generated at 2022-06-13 10:06:20.377957
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module is not None


# Generated at 2022-06-13 10:06:31.660598
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()

    # Test for invalid arguments
    action._task.args = {'hash_behaviour': 'merge', 'name': 'test', 'dir': 'test', 'depth': 3, 'files_matching': 'test', 'ignore_files': 'test', 'extensions': 'test', 'ignore_unknown_extensions': True, 'file': 'test', '_raw_params': 'test', 'invalid_arg': 'test'}
    status = action.run()
    assert(status['failed'])
    assert(status['message'] == 'invalid_arg is not a valid option in include_vars')

    # Test for hash_behaviour = none, name = None

# Generated at 2022-06-13 10:06:38.909214
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # need to mock up loader and module_utils
    class TestModuleUtils(object):
        def __init__(self, *args, **kwargs):
            pass

    class TestLoader(object):
        def __init__(self, *args, **kwargs):
            pass

        def load(self, *args, **kwargs):
            pass

        def _get_file_contents(self, *args, **kwargs):
            return "", "False"

    test_actionmodule = TestActionModule(
        '', TestTask(), TestModuleUtils(), TestLoader(), {}
    )
    # Test with no args
    test_actionmodule.run()

# Generated at 2022-06-13 10:06:39.592995
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False

# Generated at 2022-06-13 10:06:50.874218
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Test ansible.plugins.action.vars.ActionModule._load_files_in_dir() """
    import shutil
    import tempfile
    from ansible.vars.manager import VariableManager

    test_var = {'key_1': 'value_1', 'key_2': {'key_3': 'value_3'}}
    data = 'key_1: value_1\nkey_2:\n  key_3: value_3'

    root_dir = tempfile.mkdtemp()
    vars_dir = path.join(root_dir, 'vars')
    variables_dir = path.join(vars_dir, 'variables')
    os.mkdir(vars_dir)
    os.mkdir(variables_dir)


# Generated at 2022-06-13 10:06:59.137522
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # initialize ActionModule object
    # initialize ActionModule object
    AM = ActionModule(
        task=dict(
            args=dict(
                file=['/home/ansible/test.yml', '/home/ansible/test2.yml'],
                _raw_params='/home/ansible/test3.yml',
                hash_behaviour='merge',
                name='vars'
            )
        ),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    # create test fixture
    file = {
        'a': {
            'b': 'c'
        }
    }
    # create temp dir and file
    import tempfile
    from tempfile import mkdtemp

# Generated at 2022-06-13 10:07:08.942610
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os

    # Add the test directory to the module_utils path so ansible can find the mock modules
    module_utils_path = {'ANSIBLE_MODULE_UTILS': os.path.join(os.path.dirname(__file__), 'mock_module_utils')}
    os.environ.update(module_utils_path)

    mock_module_args = {'name': 'test_name', 'hash_behaviour': 'merge'}
    mock_module_return = {'ansible_facts': {'test_facts': {'facts': 'facts'}}, 'ansible_included_var_files': ['file'], 'changed': False, '_ansible_no_log': False}
    mock_action_module = MockActionModule(mock_module_args)

    assert mock_action_

# Generated at 2022-06-13 10:07:14.831289
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert isinstance(am, ActionBase)
    assert hasattr(am, 'TRANSFERS_FILES')
    assert hasattr(am, 'VALID_FILE_EXTENSIONS')
    assert hasattr(am, 'VALID_DIR_ARGUMENTS')
    assert hasattr(am, 'VALID_FILE_ARGUMENTS')
    assert hasattr(am, 'VALID_ALL')

# Generated at 2022-06-13 10:07:41.589499
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import doctest
    doctest.testmod(verbose=False)

if __name__ == '__main__':
    print(test_ActionModule_run())

# Generated at 2022-06-13 10:07:51.254775
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from io import StringIO
    from tempfile import TemporaryDirectory

    # example of data

# Generated at 2022-06-13 10:07:52.622732
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert(isinstance(action_module, ActionModule))


# Generated at 2022-06-13 10:08:00.969983
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ test method ActionModule.run """

    # run method with dir argument
    mock_self_task_ds_data_source = "vars/main.yml"
    mock_self_task_ds = Object()
    mock_self_task_ds._data_source = mock_self_task_ds_data_source
    mock_self_task_role = None
    mock_self_task = Object()
    mock_self_task._role = mock_self_task_role
    mock_self_task._ds = mock_self_task_ds
    mock_self_task._ds._data_source = mock_self_task_ds_data_source
    mock_self_task_args = {}
    mock_self_task_args['dir'] = "vars"

# Generated at 2022-06-13 10:08:02.331662
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)


# Generated at 2022-06-13 10:08:03.187191
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: to implement unit tests for class ActionModule
    assert(False)

# Generated at 2022-06-13 10:08:14.324911
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import IncludeRole
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager

    play_context = PlayContext()
    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources=['test/test_inventory.yml'])
    variable_manager = VariableManager(loader=loader, inventory=inv_manager)

# Generated at 2022-06-13 10:08:15.532415
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule, object)

# Generated at 2022-06-13 10:08:21.089558
# Unit test for constructor of class ActionModule
def test_ActionModule():
    with open("/etc/ansible/hosts", "r") as f:
        data = f.read()
    d = ActionModule(None, data, None)
    print("Successfully tested ActionModule constructor")


if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:08:34.206382
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class TestActionBase(ActionBase):
        def run(self, tmp=None, task_vars=None):
            """Runs the Task.
            Args:
                tmp (str): The path to a temporary directory that can be used for storing files.
                task_vars (dict): A dict containing variables mapped to values that can be used in the execution of the Task.
            Returns:
                dict: A dict containing the result of the Task.
            """
            pass

        def _execute_module(self, module_name=None, module_args=None, task_vars=None, tmp=None, persist_files=True, delete_remote_tmp=True, **kwargs):
            pass
    class TestTask(object):
        def __init__(self, **kwargs):
            self._ds = kwargs.get('ds')

# Generated at 2022-06-13 10:09:26.704745
# Unit test for constructor of class ActionModule
def test_ActionModule():
    obj = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert obj

# Generated at 2022-06-13 10:09:39.543269
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test case 1: Unsupported arguments
    try:
        result = ActionModule(
            task=dict(
                args=dict(
                    file='foo',
                    bar='baz'
                )
            )
        )
        assert False, 'Test case #1 passed but should have failed'
    except AnsibleError as e:
        assert str(e) == 'bar is not a valid option in include_vars', 'Test case #1 failed'

    # Test case 2: Invalid type for extensions

# Generated at 2022-06-13 10:09:40.741188
# Unit test for constructor of class ActionModule
def test_ActionModule():
   action_module = ActionModule(dict(), dict(), dict())
   assert(isinstance(action_module, ActionModule))


# Generated at 2022-06-13 10:09:42.146728
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: Add your unit tests here
    test = True
    assert test

# Generated at 2022-06-13 10:09:43.287745
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass



# Generated at 2022-06-13 10:09:51.833172
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Unit test for constructor of class ActionModule"""
    actionmodule = ActionModule()
    assert actionmodule.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']
    assert actionmodule.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    assert actionmodule.VALID_FILE_ARGUMENTS == ['file', '_raw_params']
    assert actionmodule.VALID_ALL == ['name', 'hash_behaviour']


# Generated at 2022-06-13 10:10:01.484579
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile
    root_dir = tempfile.mkdtemp()
    from collections import namedtuple
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader

    _Task = namedtuple('_Task', ['args'])
    _Task._role = namedtuple('_Role', ['_role_path'])
    _Task._ds = namedtuple('_DS', ['_data_source'])
    _Task.async_val = 0

    rval = {
        'changed': False,
        'failed': False,
        'previous_task': None,
        'skip_reason': 'conditional result was False',
        'skipped': True
    }


# Generated at 2022-06-13 10:10:02.611709
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' Create instance of ActionModule class. '''
    ActionModule()

# Generated at 2022-06-13 10:10:10.042733
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule(None, None, None)
    assert actionModule.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']
    assert actionModule.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    assert actionModule.VALID_FILE_ARGUMENTS == ['file', '_raw_params']
    assert actionModule.VALID_ALL == ['name', 'hash_behaviour']



# Generated at 2022-06-13 10:10:17.937982
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

    class Options(object):
        connection = 'local'
        verbosity = 1
        module_path = None
        forks = None
        become = None
        become_method = None
        become_user = None
        check = False
        diff = False

    _loader = DataLoader()
    _inventory = InventoryManager(loader=_loader, sources=None)
    _variable_manager = VariableManager(_loader, _inventory)

# Generated at 2022-06-13 10:12:21.167057
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']
    assert module.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    assert module.VALID_FILE_ARGUMENTS == ['file', '_raw_params']
    assert module.VALID_ALL == ['name', 'hash_behaviour']
    assert module._task == None
    assert module._task.args == None
    assert module._task._role == None
    assert module._task._role._role_path == None
    assert module._task._ds == None
    assert module._task._ds._data_source == None
    assert module.source_dir == None

# Generated at 2022-06-13 10:12:22.095588
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False

# Generated at 2022-06-13 10:12:33.914918
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    print('\n<=== Testing method run with case:  source_dir argument ===>')

# Generated at 2022-06-13 10:12:40.639107
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionmodule = ActionModule('task', 'play', loader=None, templar=None, shared_loader_obj=None)
    actionmodule._task.args = {
        '_raw_params': 'lighthouse',
        'name': 'foo',
        'hash_behaviour': 'replace',
        'files_matching': '*.yml',
        'extensions': ['yml'],
        'ignore_unknown_extensions': False
    }
    result = actionmodule.run(task_vars={})
    print(result)


# Generated at 2022-06-13 10:12:49.762581
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task

    from ansible.plugins.action.include_vars import ActionModule
    curr_dir = os.path.dirname(os.path.abspath(__file__))

    # set up the test task
    task_vars = {}
    task_ds = {}

    play_context = PlayContext()
    pm = MagicMock()
    loader = DataLoader()

    task = Task()
    action = ActionModule(task, play_context, pm, loader)


# Generated at 2022-06-13 10:12:50.996386
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    raise NotImplementedError


# Generated at 2022-06-13 10:12:53.099457
# Unit test for constructor of class ActionModule
def test_ActionModule():

    actionModule = ActionModule()
    assert isinstance(actionModule, ActionModule)



# Generated at 2022-06-13 10:12:53.765518
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()

# Generated at 2022-06-13 10:13:03.896395
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Test1")
    print("Test2")
    print("Test3")
    print("Test4")
    print("Test5")
    print("Test6")
    print("Test7")
    print("Test8")
    print("Test9")
    print("Test10")
    print("Test11")
    print("Test12")
    print("Test13")
    print("Test14")
    print("Test15")
    print("Test16")
    print("Test17")
    print("Test18")
    print("Test19")
    print("Test20")
    print("Test21")
    print("Test22")
    print("Test23")
    print("Test24")
    print("Test25")
    print("Test26")
    print("Test27")
    print("Test28")

# Generated at 2022-06-13 10:13:11.127945
# Unit test for constructor of class ActionModule
def test_ActionModule():
    instance = ActionModule()
    assert instance.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']
    assert instance.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    assert instance.VALID_FILE_ARGUMENTS == ['file', '_raw_params']
    assert instance.VALID_ALL == ['name', 'hash_behaviour']

# Unit tests for set_dir_defaults method
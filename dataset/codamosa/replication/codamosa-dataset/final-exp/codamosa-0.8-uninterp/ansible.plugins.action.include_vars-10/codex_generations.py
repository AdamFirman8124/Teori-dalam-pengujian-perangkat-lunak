

# Generated at 2022-06-13 10:06:06.550280
# Unit test for constructor of class ActionModule
def test_ActionModule():
    source_file = path.join(path.dirname(__name__), '../../../test_data/test.yml')
    action_module = ActionModule(task=object, connection=object, _play_context=object, loader=object,
                                 templar=object, shared_loader_obj=None)
    action_module._set_args()
    assert action_module.source_file, source_file
    assert action_module.valid_extensions, action_module.VALID_FILE_EXTENSIONS

# Generated at 2022-06-13 10:06:07.420751
# Unit test for constructor of class ActionModule
def test_ActionModule():
    return ActionModule()

# Generated at 2022-06-13 10:06:11.061799
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert a.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']


# Generated at 2022-06-13 10:06:21.997906
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext

    from io import StringIO
    tmp = StringIO()
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=None)
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 10:06:36.263839
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile
    import shutil
    import sys
    import yaml

    # setup
    tmpdir = tempfile.mkdtemp(prefix='ansible_test_include_vars')
    old_cwd = os.getcwd()
    os.chdir(tmpdir)

    filename = 'main.yml'
    data = {'foo': 'baz'}

    with open(filename, 'w') as f:
        yaml.dump(data, f)

    test_source_file = filename

    #test
    am = ActionModule(None, None)
    am._set_args()
    am.source_file = test_source_file
    am.module_name = 'include_vars'
    result = am.run(task_vars={})
    print(result)

    # te

# Generated at 2022-06-13 10:06:36.865107
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:06:44.701047
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    source_dir = '/home/asanabria/tests/'
    hash_behaviour = 'replace'
    file_matching = '*'
    depth = 2
    ignore_files = '*.txt'
    extensions = ['yml']
    return_results_as_name = 'host_var'

    class Task:
        def __init__(self):
            self.args = dict()
            self.args['dir'] = source_dir
            self.args['depth'] = depth
            self.args['files_matching'] = file_matching
            self.args['ignore_files'] = ignore_files
            self.args['extensions'] = extensions
            self.args['name'] = return_results_as_name

    task_vars = dict()
    action = ActionModule()
    action._task = Task()

# Generated at 2022-06-13 10:06:45.401822
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:06:54.212303
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create mock
    mock_self = Mock()

    # Mock attributes
    mock_self.VALID_FILE_EXTENSIONS = ['yaml', 'yml', 'json']
    mock_self.VALID_DIR_ARGUMENTS = ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    mock_self.VALID_FILE_ARGUMENTS = ['file', '_raw_params']
    mock_self.VALID_ALL = ['name', 'hash_behaviour']

    # Mock methods
    mock_self.set_dir_defaults = MagicMock()
    mock_self.set_args = MagicMock()
    mock_self.run = MagicMock()

# Generated at 2022-06-13 10:07:07.767569
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Prepare for testing
    import sys
    import os
    import tempfile
    if sys.version_info >= (3, 0):
        import unittest.mock as mock
    else:
        import mock
    # Start testing
    
    # Case 1
    # Prepare for testing
    with tempfile.TemporaryDirectory() as tmpdirname:
        # Prepare test data
        ds = '/var/test_dir/test_role/tasks/main.yml'
        _task = mock.MagicMock()
        _task._role = None
        _task._ds = mock.MagicMock()
        _task._ds._data_source = ds
        _task.args = {}
        # Run test

# Generated at 2022-06-13 10:07:31.397424
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module is not None

# Generated at 2022-06-13 10:07:36.021947
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    action_module._set_dir_defaults()
    assert(action_module.depth == 0)
    assert(action_module.matcher is None)
    assert(action_module.ignore_files == [])


# Generated at 2022-06-13 10:07:44.033076
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']
    assert action_module.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    assert action_module.VALID_FILE_ARGUMENTS == ['file', '_raw_params']
    assert action_module.VALID_ALL == ['name', 'hash_behaviour']



# Generated at 2022-06-13 10:07:53.018861
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None, None)
    action_module.__dict__['_task'] = None

    assert action_module.__class__.__name__ == 'ActionModule'
    assert action_module._task is None
    assert 'VALID_FILE_EXTENSIONS' in action_module.__dict__.keys()
    assert 'VALID_DIR_ARGUMENTS' in action_module.__dict__.keys()
    assert 'VALID_FILE_ARGUMENTS' in action_module.__dict__.keys()
    assert 'VALID_ALL' in action_module.__dict__.keys()
    assert action_module.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']


if __name__ == '__main__':
    test_ActionModule

# Generated at 2022-06-13 10:08:01.343055
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class Task:
        def __init__(self, task_name, task_args):
            self.name = task_name
            self._args = task_args

        def get_args(self):
            return self._args

    class Play:
        def __init__(self, play_ds):
            self._ds = play_ds

    class Role:
        def __init__(self, role_path):
            self._role_path = role_path

    # Define the class we are testing
    class ActionModuleTest(ActionModule):
        def __init__(self, task):
            self._task = task

        # Override parent class functions

# Generated at 2022-06-13 10:08:02.252945
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None)

# Generated at 2022-06-13 10:08:03.108860
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Unit tests for ActionModule class """
    temp = ActionModule


# Generated at 2022-06-13 10:08:04.531126
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None)
    assert action is not None

# Generated at 2022-06-13 10:08:05.521094
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:08:16.165031
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.constants as C
    from ansible.module_utils.six import string_types
    from ansible.module_utils._text import to_text
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.plugins.action import ActionBase
    from ansible.utils.vars import combine_vars
    import json
    import pytest
    from textwrap import dedent

    class TestActionModule(ActionModule):

        TRANSFERS_FILES = False
        VALID_FILE_EXTENSIONS = ['yaml', 'yml', 'json']
        VALID_DIR_ARGUMENTS = ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']

# Generated at 2022-06-13 10:09:07.056130
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # check if the constructor of the class ActionModule is working properly
    # This is a positive test case
    try:
        test_object = ActionModule()
        assert True
    except:
        assert False


# Generated at 2022-06-13 10:09:10.041653
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 'ActionModule' in globals(), "ActionModule not found"
    a = ActionModule()
    assert a, "Object not found"

# Test for _set_args

# Generated at 2022-06-13 10:09:14.618686
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # fixture
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.module_utils.six import PY2
    from ansible.plugins.loader import action_loader

    context = PlayContext()
    context._diff = False
    context._connection = 'local'
    context._play_context = context
    context._set_task_and_variable_override(TaskResult(task=dict()), dict())

    # test
    import_path = 'ansible.plugins.action.include_vars'
    if PY2:
        (_, module, _) = import_path.rpartition('.')
    else:
        (top_module, _, module) = import_path.rpartition('.')
    action = action_

# Generated at 2022-06-13 10:09:22.258048
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:09:36.386162
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import operator
    import pytest

    from ansible.module_utils.six import string_types
    from ansible.errors import AnsibleError
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader

    @pytest.fixture
    def source_dir(tmpdir):
        tmpdir.mkdir('vars').join('main.yml').write('test_var_dir: true')
        tmpdir.mkdir('group_vars').join('all.yml').write('test_var_all: true')
        return tmpdir

    @pytest.fixture
    def source_file(tmpdir):
        tmpdir.mkdir('vars').join('main.yml').write('test_var_file: true')

# Generated at 2022-06-13 10:09:46.700589
# Unit test for constructor of class ActionModule
def test_ActionModule():

    def _set_args(action=None, task=None, connection=None, play_context=None, loader=None, templar=None,
                  shared_loader_obj=None):
        action._task = task
        action._connection = connection
        action._play_context = play_context
        action._loader = loader
        action._templar = templar
        action._shared_loader_obj = shared_loader_obj

    # Test case - A
    # Test case - A.1
    # Test if valid_extensions param is a list
    #       valid_extensions = ['yaml', 'yml', 'json']
    from ansible.plugins.action import ActionModule
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

# Generated at 2022-06-13 10:09:58.165858
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test to test the run method of the ActionModule class.
    """
    import mock
    import os

    # Mock the ActionBase class
    action_base_mock = mock.MagicMock()
    action_base_mock.run = mock.MagicMock()
    action_base_mock.run.return_value = dict()

    # Mock the ActionModule class
    with mock.patch('ansible.plugins.action.vars.ActionModule.run', new=mock.MagicMock()):
        action_module_mock = mock.MagicMock()

        # Create test object for ActionModule
        action_module_obj = ActionModule(action_module_mock)

        os.chdir(os.path.join(os.path.dirname(__file__), '..'))

        # Set the parameters

# Generated at 2022-06-13 10:10:07.271076
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import sys
    import json
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import IncludeRole
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor

    class Options(object):
        verbosity = 0
        inventory = './tests/inventory'
        listhosts = None
        subset = None
        module_paths = None
        extra_vars = []
        forks = 1
        ask_vault

# Generated at 2022-06-13 10:10:16.757681
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins import action_loader

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_loader(loader)
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, host_list='localhost')
    variable_manager.set_inventory(inventory)
    action_plugins = action_loader.all(class_only=True)
    action_plugin = {}
    for plugin in action_plugins:
        action_plugin[plugin.name] = plugin


# Generated at 2022-06-13 10:10:18.504899
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_result import TaskResult

    # TODO: write test
    assert True

# Generated at 2022-06-13 10:12:27.503253
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from io import StringIO
    option_vars = dict(
        hash_behaviour='merge',
        name='test_hash_merge_dict',
        dir='vars_test',
        files_matching='^test.*yml$'
    )
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 10:12:31.966157
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None)
    assert action_module.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']
    assert action_module.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    assert action_module.VALID_FILE_ARGUMENTS == ['file', '_raw_params']
    assert action_module.VALID_ALL == ['name', 'hash_behaviour']


# Generated at 2022-06-13 10:12:40.751780
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_module = ActionModule()

    # run with bad source_dir
    test_module.source_dir = 'invalid/dir'
    result = test_module.run()
    assert result['failed']
    assert 'directory does not exist' in result['message']

    # run with bad source_file
    test_module.source_dir = None
    test_module.source_file = 'invalid/file'
    result = test_module.run()
    assert result['failed']
    assert 'does not exist' in result['message']

    # run with missing dir and file
    test_module.source_file = None
    result = test_module.run()
    assert result['failed']
    assert 'was not found in' in result['message']

# Generated at 2022-06-13 10:12:51.217303
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # initializing variables
    tmp = None
    task_vars = {'hostvars': {'host1': {'hostvars_var1': 'hostvars1 first', 'hostvars_var2': 'hostvars1 second'}}}
    task_args = {'dir': 'test/files',
                 'name': ['dir_var'],
                 'hash_behaviour': 'replace',
                 'files_matching': '.*\.yml$',
                 'ignore_files': ['main.yml', '.*\.yaml$'] }
    am = ActionModule(task=DummyTask(args=task_args), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:13:01.360390
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class ds:
        def __init__(self, path):
            self._path = path
    class task:
        def __init__(self, args, ds):
            self.args = args
            self._ds = ds
            self._role = None
    class role:
        def __init__(self, path):
            self._role_path = path
    class loader:
        def __init__(self):
            pass

        def load(self, data, file_name=None, show_content=False):
            return {}

    # ActionModule has no constructor
    # (one is automatically added by Python)
    # This does not test any functionality yet

    # Check different argument combinations
    am = ActionModule()
    am.run(task_vars={})
    am = ActionModule()

# Generated at 2022-06-13 10:13:06.797547
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = dict()
    task["args"] = dict()
    task["_role"] = list()
    task["_ds"] = list()

    action = ActionModule()
    action.task = task

    bad_args_list = [["file", "dir"], ["file", "extensions"], ["file", "depth"]]
    good_args_list = [["file", "name", "hash_behaviour"], ["file", "name"], ["file"], ["dir"], ["dir", "name"]]

    for args in bad_args_list:
        task["args"] = dict()
        for arg in args:
            task["args"][arg] = arg

# Generated at 2022-06-13 10:13:16.849849
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    fake_task = {'args': {'name': 'dummy_name', 'ignore_files': 'dummy_ignore_files'}}
    fake_task['_role'] = {'_role_path': 'dummy_role_path'}
    fake_task['_ds'] = {'_data_source': 'dummy_data_source'}
    fake_action_module = ActionModule(fake_task, 'dummy_connection', 'dummy_play_context', 'dummy_loader', 'dummy_templar', 'dummy_shared_loader_obj')
    fake_action_module._set_args = MagicMock()
    fake_action_module._set_dir_defaults = MagicMock()

# Generated at 2022-06-13 10:13:17.821406
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:13:26.274552
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ansible_runner = MongoDBActionModuleRunner()
    ansible_runner.parameter = {}
    ansible_runner.parameter['port'] = 27017
    # Test whether the provided port is valid or not
    is_port_valid = ansible_runner._ActionModule__is_port_valid()
    assert is_port_valid == True
    assert is_port_valid == True

# Unit test to verify the mongo db connection

# Generated at 2022-06-13 10:13:34.345520
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Arrange
    patch_builtin_open()
    patch_walk()

    tmp = '/tmp'
    task_vars = None
    # Act
    results = ActionModule(dict(), None).run(tmp, task_vars)
    # Assert
    assert results['ansible_facts'] == {"my var1": "foobar", "my var2": "barfoo"}
    assert results['ansible_included_var_files'] == ['/tmp/file1']

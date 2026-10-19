

# Generated at 2022-06-13 10:06:07.914551
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # mock task_vars
    task_vars = dict()
    task_vars['inventory_dir'] = "/home/ansible/ansible-repos/stratospheric/tests/integration/targets/inventory"

    # mock tmp
    tmp = ""

    # mock source_dir
    source_dir = "../../integration/targets/playbook.vars/testattrs/testattrs"
    source_file = "../../integration/targets/playbook.vars/testattrs/testattrs/test_attr.yml"

    # mock self._task.args

# Generated at 2022-06-13 10:06:20.572332
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.errors import AnsibleError
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.plugins.action import ActionBase
    from ansible.playbook.play_context import PlayContext

    # create dummy class objects
    dataloader = DataLoader()
    variable_manager = VariableManager()

    task_vars = dict()

    # create a variable json object
    variable = dict()
    variable['test_var1'] = 'test_var1'

# Generated at 2022-06-13 10:06:21.576513
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass


# Generated at 2022-06-13 10:06:22.633352
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule_instance = ActionModule()

# Generated at 2022-06-13 10:06:23.306999
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 10:06:34.227088
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import unittest
    # Both the vars and files are allowed to be null
    class Task:
        def __init__(self, args):
            self.args = args
    class Role:
        pass
    class DataSource:
        pass
    class PlayContext:
        def __init__(self):
            self.new_task_var = None
        def set_new_task_var(self, value):
            self.new_task_var = value
    class TaskDs:
        def __init__(self, data_source):
            self._data_source = data_source
    class Task_:
        def __init__(self, ds, role):
            self._ds = ds
            self._role = role

# Generated at 2022-06-13 10:06:40.848208
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule()

    assert not actionModule.TRANSFERS_FILES
    assert actionModule.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']
    assert actionModule.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions',
                                                'ignore_unknown_extensions']
    assert actionModule.VALID_FILE_ARGUMENTS == ['file', '_raw_params']
    assert actionModule.VALID_ALL == ['name', 'hash_behaviour']



# Generated at 2022-06-13 10:06:45.227139
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    for attr in ['VALID_FILE_EXTENSIONS', 'VALID_DIR_ARGUMENTS',
                 'VALID_FILE_ARGUMENTS', 'VALID_ALL']:
        assert hasattr(action_module, attr)

# Generated at 2022-06-13 10:06:54.099300
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    host_vars = {}
    inventory = InventoryManager([], host_vars=host_vars)
    variable_manager = VariableManager(loader=None, inventory=inventory)
    play_context = PlayContext()
    task = Task()
    role = None

    # Test with dir only
    action_module = ActionModule(task, play_context, variable_manager, loader=None, templar=Templar(), shared_loader_obj=None)
    task.args = {'dir': './tests/unit/modules/include_vars/dir'}

# Generated at 2022-06-13 10:06:58.476077
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']
    assert am.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    assert am.VALID_FILE_ARGUMENTS == ['file', '_raw_params']
    assert am.VALID_ALL == ['name', 'hash_behaviour']

# Generated at 2022-06-13 10:07:23.046873
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.__name__ == 'ActionModule'

# Generated at 2022-06-13 10:07:29.822189
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    action.included_files = []
    action._set_args()
    action.source_dir = os.path.dirname(os.path.abspath(__file__))

    results = dict()
    for root_dir, filenames in action._traverse_dir_depth():
        failed, err_msg, updated_results = (action._load_files_in_dir(root_dir, filenames))
        if failed:
            break
        results.update(updated_results)
    print(results)

# Generated at 2022-06-13 10:07:32.537525
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set all required arguments
    mod = ActionModule(dict())
    mod.run(task_vars=dict(), tmp=None)


# Generated at 2022-06-13 10:07:34.928714
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    t = ActionModule()
    t.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:07:45.292020
# Unit test for constructor of class ActionModule
def test_ActionModule():
    #Initialize action arguments
    args = dict()
    args['file'] = "test_file"
    #Create instance of action module
    am = ActionModule(dict(), dict(), False, args, None)
    #Assert instance variables
    assert am.return_results_as_name == None
    assert am.source_dir == None
    assert am.source_file == "test_file"
    assert am.depth == None
    assert am.files_matching == None
    assert am.ignore_unknown_extensions == False
    assert am.ignore_files == None
    assert am.valid_extensions == ['yaml', 'yml', 'json']

    # Reset variables
    args = dict()
    args['dir'] = "test_dir"
    am = ActionModule(dict(), dict(), False, args, None)
   

# Generated at 2022-06-13 10:07:47.423928
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    result = module.run()
    assert result['ansible_facts'] == {'foo': 'bar'}

# Generated at 2022-06-13 10:07:54.547563
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # check, if following parameters are parsed correctly
    valid_args = {
        'file': 'abc.yml',
        'name': 'my_name'
    }
    # check, if argument parsing will raise an exception
    # if both file and dir arguments are present
    invalid_args = {
        'file': 'abc.yml',
        'dir': 'my_dir',
    }
    print(ActionModule(None, valid_args).run())
    # print(ActionModule(None, invalid_args).run())

if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:07:55.147715
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()

# Generated at 2022-06-13 10:08:03.796735
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Declare input values for method run.
    tmp = None
    task_vars = {'ansible_facts': {'include_vars': {'ansible_os_family': 'Debian', 'ansible_ssh_host': '127.0.0.1', 'ansible_ssh_port': 22}}}

    # Declare return values for method run.
    class_retval = {"ansible_facts": {'ansible_os_family': 'Debian'}, "ansible_included_var_files": ["/Users/muhkuh/Source/A2/a2/lib/ansible/modules/utilities/logic/async_wrapper.py"], "_ansible_no_log": True, "failed": False}

    # Create mock object.

# Generated at 2022-06-13 10:08:05.552951
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        actionModule = ActionModule()
    except Exception as e:
        raise e

# Generated at 2022-06-13 10:09:01.443681
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 10:09:02.305048
# Unit test for constructor of class ActionModule
def test_ActionModule():
    return ActionModule(dict(), dict())


# Generated at 2022-06-13 10:09:02.870151
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:09:05.173414
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert type(ActionModule()) is ActionModule


# Generated at 2022-06-13 10:09:13.199838
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Configure the object. Creating a dummy _task, _connection, and _play_context
    task = type('task', (object,), dict(args=dict(name='myOutput')))()
    connection = type('connection', (object,), dict())()
    play_context = type('play_context', (object,), dict())()
    obj = ActionModule(task, connection, play_context, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(obj, ActionModule)


# Generated at 2022-06-13 10:09:24.041349
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create mock arguments for ActionModule constructor
    args = dict(hash_behaviour='merge', name='test',
                file='test/test_main.yml', _raw_params='test/test_main.yml', extensions=['test'])

    # Mock up class ActionModule
    module = ActionModule(task=None, connection=None,
                          _task_fields=['action', 'args'],
                          _task_vars=dict(ansible_version='2.9.9', ansible_python_interpreter='python'),
                          loader=None,
                          templar=None,
                          shared_loader_obj=None)

    # Mocked up task
    task_obj = Mock()

    # Set args as attributes of task_obj
    task_obj.args = args

    # Set task_

# Generated at 2022-06-13 10:09:36.419994
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariablesManager
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils.common.collections import ImmutableDict

    # Create mock play context
    context = PlayContext()
    context._ds = 'whatever'

    # Create mock task instance
    task = 'include_vars'
    args = {'file': 'tests/files/vars_data.yml'}
    task = task_class(task, args)

    # Create mock inventory manager
    im = InventoryManager(loader=None, sources=None)

    # Create mock variable manager
    vm = VariablesManager(loader=None, inventory=im)

    # Create action module
    action_module = ActionModule(context, task, vm)

# Generated at 2022-06-13 10:09:46.701110
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.loader import action_loader
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.cli.arguments import OptionParser
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import combine_vars

    class MockVariableManager:
        def __init__(self):
            self.vars = dict()

        def __setitem__(self, key, value):
            self.vars[key]

# Generated at 2022-06-13 10:09:47.413772
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    assert m.run() == {}

# Generated at 2022-06-13 10:09:58.727252
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.task
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    pb = ansible.playbook.PlayBook(
        playbook="test.yml",
        module_path=None,
        loader=None,
        inventory=None,
        variable_manager=VariableManager(),
        loader_cache=None)

# Generated at 2022-06-13 10:12:02.088454
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    setattr(ActionModule, '_execute_module', lambda self, tmp=None: None)
    setattr(ActionModule, '_low_level_execute_command', lambda self, cmd, tmp=None: None)
    setattr(ActionModule, '_task', lambda self: None)
    setattr(ActionModule._task, 'args', {'name': 'test', 'extensions': ['yml']})
    setattr(ActionModule, '_task', lambda self: None)
    setattr(ActionModule._task, 'run_once', True)
    setattr(ActionModule, '_loader', lambda self: None)
    setattr(ActionModule._loader, '_get_file_contents', lambda self, filename: ('', True))

# Generated at 2022-06-13 10:12:04.491517
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class DummyActionModule(ActionModule):
        VALID_FILE_EXTENSIONS = ['yaml', 'yml', 'json']
    action_module = DummyActionModule()
    action_module.run(task_vars=dict())
    # Not throwing exception is good check for run method

test_ActionModule_run()

# Generated at 2022-06-13 10:12:08.614217
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('Begin method test_ActionModule_run')
    keys = []
    for key in ActionModule.run.__code__.co_varnames:
        keys.append(key)
    print(*keys, sep=', ')



# Generated at 2022-06-13 10:12:17.661028
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = dict(action=dict(module='include_vars', args=dict(name='test')))
    result = dict(ansible_included_var_files=[], ansible_facts=dict(), _ansible_no_log=False)
    action = ActionModule(task, dict())

    # Test for invalid arguments
    task = dict(action=dict(module='include_vars', args=dict(_raw_params='/path/to/file', file='/path/to/file')))
    try:
        action = ActionModule(task, dict())
    except AnsibleError:
        pass
    else:
        assert False

    task = dict(action=dict(module='include_vars', args=dict(dir='/path/to/dir', file='/path/to/file')))

# Generated at 2022-06-13 10:12:29.105669
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile
    from ansible.module_utils.six import StringIO
    from ansible.utils.vars import combine_vars

    # patch loader
    def _get_file_contents(self, path):
        return to_text(path, errors='surrogate_or_strict'), True
    def load(self, data, file_name=None, show_content=True):
        return data
    def create_file(self, path, contents):
        with open(path, 'wb') as f:
            f.write(to_bytes(contents, errors='surrogate_or_strict'))
    FakeLoader = type('FakeLoader', (object,), {'_get_file_contents': _get_file_contents, 'load': load, 'create_file': create_file})

    #

# Generated at 2022-06-13 10:12:31.239627
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(None, None)


if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:12:32.912285
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_var = ActionModule()
    assert test_var is not None



# Generated at 2022-06-13 10:12:35.189105
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert isinstance(am, ActionModule)

#Unit test for run method of class ActionModule

# Generated at 2022-06-13 10:12:43.872777
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for method run of class ActionModule.
    """
    import ast
    import sys

    # setup
    p_module = sys.modules['ansible.plugins.action']
    def mock_from_module(*args, **kwargs):
        return {'ansible_facts': {}}
    p_module.from_module.from_module = mock_from_module

    # Don't fail when reading 'config' or 'ignore_files'
    def mock_get_file_contents(*args, **kwargs):
        return 1234

    p_module._text.assert_type_str = mock_get_file_contents
    p_module._text.to_text = mock_get_file_contents
    p_module.ActionModule._get_file_contents = mock_get_file_contents

    p

# Generated at 2022-06-13 10:12:53.366718
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible
    from ansible.utils.vars import combine_vars
    # -- Initialization --
    # args
    dir = './tests/integration/targets/'
    file = './tests/integration/targets/vars/main.yml'
    # task_vars
    task_vars = {
        'a': 1,
        'b': 2,
    }
    # -- Preparation --
    task_ds = 'tests/integration/targets/vars/main.yml'
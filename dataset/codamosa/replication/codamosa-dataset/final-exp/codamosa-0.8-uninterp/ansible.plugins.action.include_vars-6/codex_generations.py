

# Generated at 2022-06-13 10:06:06.728740
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import unittest
    import mock
    import os
    import tempfile
    import json

    def test_normal_dict():
        test_dict = {}
        test_dict['test_string_key'] = 'test_string_value'
        test_dict['test_int_key'] = 123
        test_dict['test_list_key'] = ['test_list_item', 'test_list_item2']
        test_dict['test_dict_key'] = {'test_dict_key2':'test_dict_value2'}
        with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
            json.dump(test_dict, tmp, ensure_ascii=True)

        # test each of the extensions
        result = {}

# Generated at 2022-06-13 10:06:11.300513
# Unit test for constructor of class ActionModule
def test_ActionModule():
    my_action_module = ActionModule()
    if my_action_module is not None:
        print("Constructor test successfull")
    else:
        print("Constructor test failed")



# Generated at 2022-06-13 10:06:22.149303
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook import include_vars
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role import Role
    import ansible.constants as C
    import os
    caller_dir = os.path.dirname(os.path.dirname(__file__))
    loader_dir = os.path.join(caller_dir, 'test')
    def mock_get_file_contents(filename, task_vars=None):
        return open(filename, 'r').read(), True
    setattr(ActionModule, '_get_file_contents', mock_get_file_contents)

    task = TaskInclude()
    role = Role()
    role._role_path = loader_dir
    task._role = role
    task._ds = None

   

# Generated at 2022-06-13 10:06:33.307287
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # setup
    import os
    import shutil
    from tempfile import mkdtemp
    from ansible.module_utils.six.moves import builtins
    from ansible.playbook.play_context import PlayContext

    # define types for test variables
    class DummyModule():
        class DummyDs():
            data_source = ''

        class DummyTask():
            class DummyDs():
                _data_source = ''

            class DummyRole():
                role_path = ''

            ds = DummyDs()
            role = DummyRole()
            args = {'file': '', '_raw_params': ''}

        # pylint: disable=too-few-public-methods
        class DummyActionBase():
            def __init__(self):
                self.tqm = TqmM

# Generated at 2022-06-13 10:06:33.912658
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:06:34.802708
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert a is not None

# Generated at 2022-06-13 10:06:37.526638
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module=ActionModule()
    assert isinstance(action_module,ActionBase)


# Generated at 2022-06-13 10:06:49.028044
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # set up the task
    task_vars = dict()
    t = {
        "args":{
            "name": "vars_result",
            "file": "../../../../vars/main.yml"
        },
        "task_vars": task_vars
    }

    setattr(t, "_ds", dict())

    am = ActionModule(t, dict())
    am._set_args()

    # call run of the action module
    result = am.run(task_vars=task_vars)

    assert result['ansible_included_var_files'] == [
        u'/tmp/ansible_collections/ansible_collections/agude/openwrt/tests/vars/main.yml']

# Generated at 2022-06-13 10:06:57.742051
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Test constructor
    :return:
    '''
    obj = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert obj.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']
    assert obj.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    assert obj.VALID_FILE_ARGUMENTS == ['file', '_raw_params']
    assert obj.VALID_ALL == ['name', 'hash_behaviour']



# Generated at 2022-06-13 10:07:02.172929
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(action_module, ActionModule)


# Generated at 2022-06-13 10:07:30.846039
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.include_vars import ActionModule

    action_module_instance = ActionModule(
        task=None,
        connection=None,
        _play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert action_module_instance is not None


# Generated at 2022-06-13 10:07:42.557405
# Unit test for constructor of class ActionModule
def test_ActionModule():
    config = dict()
    config['ANSIBLE_MODULE_UTILS'] = './library/'
    config['DEFAULT_MODULE_UTILS'] = './library/'
    config['DEFAULT_MODULE_UTILS_PATH'] = './library/'
    config['DEFAULT_HASH_BEHAVIOUR'] = 'merge'
    config['TRANSPORT'] = 'ssh'
    config['DEFAULT_KEEP_REMOTE_FILES'] = False
    config['DEFAULT_REMOTE_TMP'] = '.ansible/tmp'
    config['DEFAULT_LOCAL_TMP'] = '.ansible/tmp'
    config['DEFAULT_DEBUG'] = False
    config['DEFAULT_USE_SYMLINK'] = False

# Generated at 2022-06-13 10:07:44.656081
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 'ActionModule' in str(ActionModule)



# Generated at 2022-06-13 10:07:53.948020
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:07:57.292623
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule(
        task=dict(args=dict(file="vars/main.yml")),
        connection=None,
        _task_vars=dict(facts=dict()),
        loader=None
    )
    assert not action.run()

# Generated at 2022-06-13 10:07:58.278044
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert (ActionModule is not None)



# Generated at 2022-06-13 10:08:05.538183
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()

    # validate @VALID_ALL
    assert a.VALID_ALL == ['name', 'hash_behaviour']

    # validate @VALID_DIR_ARGUMENTS
    assert a.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']

    # validate @VALID_FILE_ARGUMENTS
    assert a.VALID_FILE_ARGUMENTS == ['file', '_raw_params']

    # validate @VALID_FILE_EXTENSIONS
    assert a.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']


# Generated at 2022-06-13 10:08:13.162804
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import load_extra_vars

    from units.mock.loader import DictDataLoader
    from units.mock.inventory import MockInventory
    from units.mock.vars import MockVars


# Generated at 2022-06-13 10:08:22.902386
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    my_play = Play()
    my_loader = DataLoader()
    my_var_manager = VariableManager()
    my_inven_manager = InventoryManager()
    my_task_queue = TaskQueueManager()
    my_playbook_executor = PlaybookExecutor()
    ActionModule(my_loader, my_play, my_var_manager, my_inven_manager, my_task_queue, my_playbook_executor)

# Generated at 2022-06-13 10:08:23.772622
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:09:15.648947
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    variables = {'var1': 'val1', 'var2': 'val2'}
    task_vars = {'var1': 'val1', 'var2': 'val2'}

    module = ActionModule()

    # validate the arguments
    with pytest.raises(AnsibleError):
        module.run(task_vars=task_vars)

    # ensure that source_dir is properly set
    source_dir = 'test/var_files'
    task_vars['templates'] = '/task/path/templates'
    module._task.args = {'dir': source_dir}
    expected_source_dir = path.join(task_vars['templates'], source_dir)

# Generated at 2022-06-13 10:09:25.791712
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import IncludeRole
    from ansible.playbook.task import Task
    from ansible.template import Templar

    class DataLoaderMock(object):
        def get_basedir(self, *args, **kwargs):
            return 'test/data/test_action_module'

    class TaskMock(object):
        def __init__(self, *args, **kwargs):
            self.args = {
                'name': 'plugin_facts',
                'ignore_unknown_extensions': False,
                'extensions': ['yaml']
            }

    class VarManagerMock(object):
        def __init__(self, *args, **kwargs):
            self

# Generated at 2022-06-13 10:09:28.330376
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module_run = ActionModule.run
    return action_module_run


# Generated at 2022-06-13 10:09:28.824310
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:09:29.968366
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:09:40.176351
# Unit test for constructor of class ActionModule
def test_ActionModule():
    usecase = ['test1.yml','test2.yml','test3.yml','test4.yml','test5.yml','test6.yml','test7.yml','test8.yml','test9.yml','test10.yml']
    #case 1
    action_module = ActionModule('/root/', 'name', 'file')
    assert action_module.return_results_as_name == 'name'
    assert action_module.source_file == '/root/'
    assert action_module.source_dir == None
    assert action_module.depth == None
    assert action_module.files_matching == None
    assert action_module.ignore_unknown_extensions == False
    assert action_module.ignore_files == None

# Generated at 2022-06-13 10:09:40.828902
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:09:49.203033
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor import (
        PlaybookExecutor,
        play_context,
        task_result
    )
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    import ansible.plugins.loader
    import ansible.plugins
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    import ansible.module_utils.network.common.utils
    import os, shutil
    from six import StringIO
    import tempfile
    import json


# Generated at 2022-06-13 10:09:49.960578
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()


# Generated at 2022-06-13 10:10:00.323455
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # For a complete test we would need two mock classes:
    # one for the ActionModule and one for ActionBase.
    # The following is only a small test

    # Test with an empty directory
    task_vars = {
        "vars": {
            "base_dir_content": [],
            "base_dir": ""
        }
    }

    action_module = ActionModule()
    result = action_module.run(None, task_vars)
    assert isinstance(result, dict)
    assert result['ansible_facts'] == {}
    assert result['ansible_included_var_files'] == []
    assert result['_ansible_no_log']
    assert not result['failed']

    # Test with a directory containing one file

# Generated at 2022-06-13 10:12:11.833800
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Unit test for class ActionModule.
    Returns:
        True if successful, False otherwise"""
    test_action = ActionModule(dict(dir='dir'), dict(dir='dir'), 'dir')

    if not isinstance(test_action, ActionModule):
        return False

    if not isinstance(test_action._task, dict):
        return False

    if not isinstance(test_action._connection, dict):
        return False

    if test_action._play_context is not None:
        return False

    if test_action._loader:
        return False

    if test_action._templar:
        return False

    return True



# Generated at 2022-06-13 10:12:19.972617
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    args = dict(dir="dir", depth=2, files_matching="matching",
                ignore_files=["ignore1", "ignore2"], extensions=["yaml", "yml", "json"])

    # Define a fake task
    task = dict(args=args)

    # Define a fake loader
    loader = dict(get_basedir=lambda self, x=None, **kwargs: r"/basedir/",
                  path_dwim=lambda self, x=None, **kwargs: r"/basedir/x/y/file")

    # Define a fake task with role
    role = dict(_role_path=r"/basedir/x/y/")
    task_with_role = dict(args=args, _role=role)

    # Define a fake task with data source
    d

# Generated at 2022-06-13 10:12:20.927712
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule()
    actionModule.run()

# Generated at 2022-06-13 10:12:33.004132
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_result import TaskResult
    from ansible.plugins.action.include_vars import ActionModule

    # Mock task arguments
    # for directory case
    dir_args = {
        'dir': 'test_include',
        '_raw_params': None,
        'ignore_files': list()
    }

    # for file case
    file_args = {
        'file': 'vars/test_include_file.yaml',
        '_raw_params': 'vars/test_include_file.yaml',
        'ignore_files': list()
    }

    # Mock task object
    task_object = open('test_include/tasks/main.yml', 'r').read()

    # Mock task variables

# Generated at 2022-06-13 10:12:41.964004
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Unit tests for ActionModule
    Args:
        None
    Returns:
        List of test results
    """

    am = ActionModule()

    # Validate _set_args()
    am.VALID_DIR_ARGUMENTS = ['dir', 'depth',
                              'files_matching', 'ignore_files',
                              'extensions', 'ignore_unknown_extensions']
    am.VALID_FILE_ARGUMENTS = ['file', '_raw_params']
    am.VALID_ALL = ['name', 'hash_behaviour']

    if am._task.args['dir']:
        assert am.source_dir == 'testdir'
        assert am.depth == 0
        assert am.files_matching == '.*'
        assert am.ignore_files == ['regex_pattern']

# Generated at 2022-06-13 10:12:50.675099
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # data to be used in testing
    filepath1 = '../../lib/ansible/modules/cloud/gce/gce.py'
    filepath2 = '../../lib/ansible/modules/network/nxos/nxos_static_routes.py'
    filepath3 = '../../lib/ansible/modules/network/nxos/nxos_static_routes.cfg'


    # testing the constructor of class ActionModule
    assert ActionModule._is_valid_file_ext(filepath1) == True
    assert ActionModule._is_valid_file_ext(filepath2) == True
    assert ActionModule._is_valid_file_ext(filepath3) == False


# Generated at 2022-06-13 10:12:58.750877
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # _task object
    _task = object()

    # _connection object
    _connection = object()

    # AnsibleTaskFiles object
    AnsibleTaskFiles = lambda x: x

    # AnsibleLoader object
    AnsibleLoader = lambda x: x

    action = ActionModule(_task, _connection, AnsibleTaskFiles, AnsibleLoader)

    assert action._task is _task
    assert action._connection is _connection
    assert action._loader is AnsibleLoader
    assert action._templar is AnsibleTaskFiles
    assert action._shared_loader_obj is AnsibleLoader
    assert action._display is None


# Generated at 2022-06-13 10:13:00.273401
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    print(action.run())

# Generated at 2022-06-13 10:13:14.782869
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.vars import combine_vars

    test_action = ActionModule()
    merge_hashes = True

    old_value = {'a': 1, 'b': {'c': 2}}
    value = {'a': 2, 'b': 3, 'd': 4}

    result = {'a': 2, 'b': {'c': 2}, 'd': 4}

    assert combine_vars(old_value, value, merge=merge_hashes) == result, 'combine_vars() failed to update old_value'
    assert combine_vars(old_value, value, merge=False) == value, 'combine_vars() failed to set old_value with value'

    merge_hashes = False
    result = value


# Generated at 2022-06-13 10:13:23.165076
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    b_data = b'{ "var1": "foo"}'
    task = Task()
    task._role = None

    task.args = {'dir': 'test_dir'}
    task._ds = {'_data_source': 'test_source'}
    task._task_vars = {}
    task_vars = VariableManager()
    templar = Templar(loader=None, variables=task_vars)

    action = ActionModule(task, templar, task_vars)
    action._loader = FakeLoader(b_data)

    action._task.args = {'dir': 'test_dir'}
    action._task._role = None
    action._
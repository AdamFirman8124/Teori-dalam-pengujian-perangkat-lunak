

# Generated at 2022-06-13 10:06:00.081415
# Unit test for constructor of class ActionModule
def test_ActionModule():

    a = ActionModule()
    assert a is not None
    assert isinstance(a, ActionModule)



# Generated at 2022-06-13 10:06:07.864515
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    action_module = ActionModule()

    def __init__(self):
        pass

    def get_vars(self):
        return {}

    def load_file(self, filepath):
        pass

    action_module.setup_loader({})
    action_module.show_content = True
    action_module.included_files = None
    action_module._task = Task()
    action_module._task._role = None
    action_module._task._ds = Play()
    action_module._task._ds._data_source = "/home/user/Desktop/Ansible/ansible-test/test.yml"
    action_module._

# Generated at 2022-06-13 10:06:09.722195
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:06:15.020159
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_parameters = {
        'ansible_included_var_files': [],
        'message': '',
        'ansible_facts': {
            'key_1': 'val_1',
            'key_2': 'val_2',
        },
    }

    return module_parameters

# Generated at 2022-06-13 10:06:24.126234
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test to test method run of class ActionModule
    '''
    import os
    import shutil
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.plugins.strategy.linear import StrategyModule
    from ansible.plugins.callback.default import CallbackModule

    from collections import namedtuple
    from ansible.utils.vars import combine_vars
    from ansible.module_utils.six import string_types

    # Create Files inside the test_variable_dir for the purpose of testing


# Generated at 2022-06-13 10:06:25.239354
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:06:35.742916
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    source_dir = None
    depth = None
    files_matching = None
    ignore_files = None
    ignore_unknown_extensions = None
    source_file = None
    valid_extensions = ["yaml", "yml", "json"]
    return_results_as_name = None
    hash_behaviour = None
    err_msg = ''

# Generated at 2022-06-13 10:06:37.000679
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Testing the ActionModule without any parameters
    pass

# Generated at 2022-06-13 10:06:37.868186
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:06:39.874038
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule('test_ActionModule', 'test_task', dict())
    return actionModule


# Generated at 2022-06-13 10:07:04.673631
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule(None)

# Generated at 2022-06-13 10:07:05.932206
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:07:16.911829
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialize environment variables
    dict_of_vars = {}
    dict_of_vars['a'] = 'b'
    dict_of_vars['b'] = 'c'

    # Initialize ActionModule
    action_module = ActionModule()
    action_module._task.args['file'] = 'yml/test_file.yml'
    action_module._task.args['name'] = 'results'
    action_module._task.args['extensions'] = ['yaml', 'yml']
    action_module._task.args['ignore_unknown_extensions'] = False

    # Initialize _loader
    action_module._loader = DictDataLoader()

    # testing run()
    ansible_dict = action_module.run(task_vars=dict_of_vars)

    # Check whether

# Generated at 2022-06-13 10:07:22.130983
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role

    action = ActionModule("test", "test", dict())
    action._task = Task("test", "test", dict())
    action._task._role = Role("test")

    action.VALID_ALL = ["test"]
    action.VALID_DIR_ARGUMENTS = ["test"]
    action.VALID_FILE_ARGUMENTS = ["test"]
    action.VALID_FILE_EXTENSIONS = ["test"]

    action.run(task_vars=dict())

# Generated at 2022-06-13 10:07:28.187492
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.included_file import IncludedFile
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.executor import playbook_executor

    module_loader = DataLoader()
    results_callback = playbook_executor.RUN_RESULTS(tqm=None, loader=module_loader)
    inventory = InventoryManager(module_loader, sources='')
    variable_manager = VariableManager(loader=module_loader, inventory=inventory)
    play_context = PlayContext()

    test_task = Task()

# Generated at 2022-06-13 10:07:35.942612
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.executor.task_queue_manager
    import ansible.module_utils.basic
    import ansible.parsing.data
    import ansible.plugins.loader
    import ansible.utils.vars
    import os
    import tempfile

    class Fake_Role(object):

        def __init__(self):
            self._role_path = ''

    class Fake_DS(object):

        def __init__(self):
            self._data_source = ''

    class Fake_Task(object):

        def __init__(self):
            self._role = Fake_Role()
            self._ds = Fake_DS()
            self.args = {'dir': False, 'file': False, '_raw_params': False}


# Generated at 2022-06-13 10:07:45.874253
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test_case_01:
    #   file=test_case_01.yml
    #   source_dir=test_case_01.yml
    #   source_file=test_case_01.yml
    #   depth=0
    #   files_matching='test_case_01.*'
    #   ignore_files=(1, 2, 3, )
    #   extensions=(yml, yaml, )
    #   dir=None
    #   _raw_params
    #   result=dict()
    input_data = dict()
    input_data['file'] = 'test_case_01.yml'
    input_data['source_dir'] = 'test_case_01.yml'
    input_data['source_file'] = 'test_case_01.yml'
   

# Generated at 2022-06-13 10:07:47.505156
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(dict(), dict(), 'yml') is not None


# Generated at 2022-06-13 10:07:48.346546
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('test')

# Generated at 2022-06-13 10:07:50.091373
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock_loader = ""
    mock_task = ""
    assert ActionModule(mock_loader, mock_task)

# Generated at 2022-06-13 10:08:40.314115
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create an instance of class ActionModule
    action_module = ActionModule()
    print('instance has been created')

# Extract variables recursively from a directory

# Generated at 2022-06-13 10:08:53.533766
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    obj = ActionModule()
    obj._set_args()

    class ActionModule(object):
        pass

    class _task(object):
        def __init__(self):
            self.args = {'dir': 'test', 'name': 'test'}
    obj._task = _task()
    obj._task.args = {'dir': 'test', 'name': 'test'}

    obj._set_dir_defaults()

    obj._set_root_dir()
    obj._traverse_dir_depth()
    obj._ignore_file('test')
    obj._is_valid_file_ext('test')
    obj._load_files('test')
    obj._load_files_in_dir('test', ['test'])

    obj.run(task_vars={'test': 1})

# Generated at 2022-06-13 10:09:02.491829
# Unit test for constructor of class ActionModule
def test_ActionModule():
    Task = dict()
    Task['args'] = dict()
    Task['_role'] = dict()
    Task['_ds'] = dict()
    Task['_task'] = dict()
    Task['_task']['args'] = dict()
    Task['_task']['_role'] = dict()
    Task['_task']['_ds'] = dict()
    Task['_task']['_role']['_role_path'] = dict()

    # Test 1
    Task['args']['_raw_params'] = 'value'
    task = dict()
    task['args'] = dict()
    task['_role'] = dict()
    task['_ds'] = dict()
    task['_ds']['_data_source'] = '/home/ansible/test_load_yml_files.py'

# Generated at 2022-06-13 10:09:08.368989
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    plugin = ActionModule()
    # Deleted variable "tmp" as keyword argument
    assert plugin.run(task_vars={}) == {'ansible_facts': {'_ansible_no_log': False, 'ansible_included_var_files': []}, '_ansible_no_log': False, 'ansible_included_var_files': []}


# Generated at 2022-06-13 10:09:20.673434
# Unit test for constructor of class ActionModule
def test_ActionModule():
    params = {
        'file':'path/to/file',
        'name':'name',
        'hash_behaviour':'hash_behaviour'
    }
    task_vars = {
        'ds': {
            '_data_source': 'path'
        }
    }
    # Test with dir
    action_module = ActionModule(dict(params, dir='dir'), 'current/path/to/task')
    action_module._task._role = 'role/path'
    action_module.run(task_vars=task_vars)
    action_module = ActionModule(dict(params, dir='vars/dir'), 'current/path/to/task')
    action_module._task._role = 'role/path'
    action_module.run(task_vars=task_vars)

# Generated at 2022-06-13 10:09:23.120160
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a class object and call some methods
    am = ActionModule()
    am._set_dir_defaults()
    am._set_args()
    am.run()
    return True

# Generated at 2022-06-13 10:09:24.517031
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:09:25.555860
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module.run()
    pass


# Generated at 2022-06-13 10:09:28.788342
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action is not None

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:09:38.443761
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.include_vars import ActionModule
    am = ActionModule()
    assert am.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']
    assert am.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    assert am.VALID_FILE_ARGUMENTS == ['file', '_raw_params']
    assert am.VALID_ALL == ['name', 'hash_behaviour']


# Generated at 2022-06-13 10:11:31.551927
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(name='test_ActionModule', task=dict())
    assert am.name == 'test_ActionModule'
    assert isinstance(am._task, dict)
    assert am.RETURN_SUCCESS == 'SUCCESS'
    assert am.RETURN_FAILURE == 'FAILED'


# Generated at 2022-06-13 10:11:38.380157
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test case when source directory is present
    source_dir = "test_var_dir"
    depth = 0
    files_matching = ""
    ignore_files = ""
    extensions = "yml"
    ignore_unknown_extensions = False
    name = "test_name"
    hash_behaviour = "replace"
    source_file = ""
    _raw_params = ""
    td = {"dir": source_dir, "depth": depth, "files_matching": files_matching,
          "ignore_files": ignore_files, "extensions": extensions, "ignore_unknown_extensions": ignore_unknown_extensions,
          "name": name, "hash_behaviour": hash_behaviour, "file": source_file,
          "_raw_params": _raw_params}
    t = MockTask(td)

# Generated at 2022-06-13 10:11:39.622407
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert a is not None
    assert a is not None

# Generated at 2022-06-13 10:11:48.407732
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    params = {
        "dir": "/path_to_dir"
    }
    # Test case 1
    results_1 = run_test_case(params, "", "", {})
    assert type(results_1) is dict
    assert set(results_1.keys()) == set(["failed", "result", "msg"])
    assert type(results_1["failed"]) is bool
    assert results_1["failed"] is False
    assert type(results_1["result"]) is dict
    assert results_1["msg"] == ""
    # Test case 2
    results_2 = run_test_case(params, "/path_to_dir/file", "", {})
    assert type(results_2) is dict
    assert set(results_2.keys()) == set(["failed", "result", "msg"])


# Generated at 2022-06-13 10:11:59.123239
# Unit test for constructor of class ActionModule
def test_ActionModule():
    file = "filename"
    root_dir = "/root"
    var_files = ["var_files"]

    task_vars = dict()
    res = ActionModule(task_vars)
    assert res._task._role is None, " Role should be None"
    assert res.return_results_as_name is None, "Name of variable should be None"
    assert res.source_file is None, "Source file should be None"
    assert res.hash_behaviour is None, "Hash behaviour should be None"
    assert res.source_dir is None, "Source directory should be None"
    assert len(res.valid_extensions) == 3, "Valid extensions size should be 3"

    assert res._set_dir_defaults() == None, "_set_dir_defaults() should return None"

# Generated at 2022-06-13 10:12:11.093551
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for the run method of class ActionModule
    """

    # initialize variables
    action_module = ActionModule(None)
    action_module.depth = 0
    action_module.ignore_files = []

    # define args
    args = ['name', 'ansible', 'hash_behaviour', 'merge', 'dir', './', 'depth', '0']

    # initialize dummy _task
    action_module._task.args = {}
    for i in range(0, len(args), 2):
        action_module._task.args[args[i]] = args[i+1]

    # initialize dummy _loader

# Generated at 2022-06-13 10:12:15.556219
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    assert module.VALID_FILE_ARGUMENTS == ['file', '_raw_params']
    assert module.VALID_ALL == ['name', 'hash_behaviour']

# Generated at 2022-06-13 10:12:16.482722
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(ActionModule())


# Generated at 2022-06-13 10:12:18.286743
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, variable_manager=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:12:24.700999
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_result import TaskResult
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.plugins.loader import module_loader
    import ansible.utils.vars
    from ansible.vars.manager import VariableManager

    playbook = Play().load({
        'hosts': 'localhost',
        'tasks': [
            {
                'action': 'include_vars',
                'args': {
                    'file': 'test_include_vars.yaml'
                },
                'name': 'Include vars'
            }
        ]
    }, variable_manager=None, loader=DataLoader())
    play = playbook.get_plays()[0]

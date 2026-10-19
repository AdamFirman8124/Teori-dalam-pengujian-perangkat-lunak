

# Generated at 2022-06-13 10:06:07.480732
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Change current directory
    import os
    import sys
    old_cwd = os.getcwd()
    os.chdir('..')
    # Assign __file__ to code_dir that is above in directory structure
    code_dir = os.path.dirname(os.path.realpath(__file__))
    print("code dir" + code_dir)
    # Insert code directory to import path
    sys.path.insert(1, code_dir)
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    pc = PlayContext()
    pc._play = dict()
    pc._play['name'] = "test_play"
    pc._play['id'] = "test_play_id"

# Generated at 2022-06-13 10:06:18.788079
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = dict()
    task['args'] = dict()
    task['args']['file'] = 'test.yml'
    task['_role'] = None
    task['_ds'] = None
    task['_ds'] = dict()
    task['_ds']['_data_source'] = ''
    task['name'] = 'test'
    task_vars = dict()
    tmp = ''
    loader = ''
    am = ActionModule(task=task, connection=None, play_context=None, loader=loader, templar=None, shared_loader_obj=None)
    assert am.run(tmp=tmp, task_vars=task_vars)

# Generated at 2022-06-13 10:06:20.147289
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()


# Generated at 2022-06-13 10:06:23.652685
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # ActionModule()
    am = ActionModule()
    print(am)
    print(am.VALID_FILE_EXTENSIONS)
    print(am.VALID_DIR_ARGUMENTS)

# test_ActionModule()


# Generated at 2022-06-13 10:06:27.223406
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.include_vars import ActionModule
    action = ActionModule(dict(foo='bar'), dict(), False, 'path/to/file')
    assert action


# Generated at 2022-06-13 10:06:28.526437
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO
    pass

# Generated at 2022-06-13 10:06:29.240638
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:06:38.635040
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import IncludeRole
    from ansible.executor.task_queue_manager import TaskQueueManager
    def __init__(self):
        pass
    task_queue_manager = TaskQueueManager(None)
    block = Block(play=Play().load(dict(name='testing', hosts=['localhost'], gather_facts='no', tasks=[dict(include_vars=dict(file='./tests/includes_vars_file.yml', name='testing_params'))])), task_include=IncludeRole())
    block.filter_tagged_tasks(tags=['always'])
    block.post_validate()

# Generated at 2022-06-13 10:06:49.925441
# Unit test for method run of class ActionModule
def test_ActionModule_run(): 

    # NOTE: The following code is a copy of the method 'run' of class ActionModule, modified with some adjustments
    #       to be run without requiring further dependencies.

    tmp=None
    task_vars=None

    # Validate arguments
    dirs = 0
    files = 0
    for arg in self._task.args:
        if arg in self.VALID_DIR_ARGUMENTS:
            dirs += 1
        elif arg in self.VALID_FILE_ARGUMENTS:
            files += 1
        elif arg in self.VALID_ALL:
            pass
        else:
            raise AnsibleError('{0} is not a valid option in include_vars'.format(to_native(arg)))


# Generated at 2022-06-13 10:06:51.669825
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule()
    assert True

# Generated at 2022-06-13 10:07:22.814023
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule("test_role", "test_loader", "test_tempcache", "test_shared_loader_obj")
    assert module._task['role'] == "test_role"
    assert module._task._role == "test_role"
    assert module._loader == "test_loader"
    assert module._tempcache == "test_tempcache"
    assert module._shared_loader_obj == "test_shared_loader_obj"

# Unit Test for _traverse_dir_depth function

# Generated at 2022-06-13 10:07:23.808541
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(ActionModule(None, None) != None)


# Generated at 2022-06-13 10:07:25.214920
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: Create unit test for ActionModule.run()
    return None

# Generated at 2022-06-13 10:07:26.177806
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 10:07:27.111379
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:07:38.831772
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    source_dir = "test_dir"
    source_file = "/etc/ansible/test_file"
    var_files = ["test_vars_1", "test_vars_2"]

    class MockTask(object):
        def __init__(self):
            self.args = dict()
            self.args["dir"] = source_dir
            self.args["name"] = "test_name"
            self.args["_raw_params"] = source_file
            self.args["hash_behaviour"] = "test_hash"
            self.args["files_matching"] = "[a-z]*_1"
            self.args["extensions"] = "yaml yml"
            self.args["ignore_unknown_extensions"] = False

# Generated at 2022-06-13 10:07:45.338356
# Unit test for constructor of class ActionModule
def test_ActionModule():
    args = dict()
    args['name'] = 'pam'
    args['dir'] = '/home/user/test'
    args['depth'] = 1
    args['files_matching'] = '.*\.yml'
    args['ignore_files'] = ['main.yml']

    # NOTE: The following line is commented out because ActionBase() is an abstract class
    # am = ActionModule(dict(), args)
    # assert am
    # assert isinstance(am, ActionModule)
    pass

# Generated at 2022-06-13 10:07:46.304668
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, [], None)


# Generated at 2022-06-13 10:07:55.685169
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict()
    result = dict()
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action.loader is not None

    # Test run method
    task_vars = dict()
    results = action.run(tmp=None, task_vars=task_vars)
    assert results is not None
    assert results['ansible_included_var_files'] == []
    assert results['ansible_facts'] == {}
    assert results['_ansible_no_log']
    assert results['failed']
    assert results['message'] == 'Must specify file or dir'

    task_vars = dict()

# Generated at 2022-06-13 10:08:03.388865
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: fix Mock implementation and run unit tests
    from unittest.mock import Mock
    from unittest.mock import patch
    mock_module = Mock()
    mock_module.run.return_value = dict(ansible_facts=dict(test=dict(result=42)))
    with patch.object(ActionModule, 'run', mock_module.run) as mock_run:
        action_module = ActionModule(task=dict(args=dict(dir='tests')))
        result = action_module.run()
        mock_module.run.assert_called_with(tmp=None, task_vars=None)
        assert dict(test=dict(result=42)) == result['ansible_facts']

# Generated at 2022-06-13 10:08:42.180230
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:08:43.010188
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:08:50.712470
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_ds = {}
    task_args = {}
    loader_mock = {}
    templar_mock = {}

    action_base_module = ActionModule(task=task_ds, connection=None, play_context=None, loader=loader_mock, templar=templar_mock, shared_loader_obj=None)

    assert isinstance(action_base_module, ActionBase)



# Generated at 2022-06-13 10:08:58.603923
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.unsafe_proxy import UnsafeProxy
    class Fake_task(Task):
        def __init__(self):
            return

    task = Fake_task()
    task._role = None
    task._ds = Fake_task()
    task._ds._data_source = '/home/test/test'
    class Fake_loader(DataLoader):
        def __init__(self):
            return
    loader = Fake_loader()
    class Fake_variable_manager(VariableManager):
        def __init__(self):
            return
    vars = Fake_variable_manager()

# Generated at 2022-06-13 10:09:07.170217
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ##
    ## mock object, then test results
    ##
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.action import ActionBase
    import json

    class TestBackgroundExecute(ActionBase):
        def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
            super(TestBackgroundExecute, self).__init__(task, connection, play_context, loader, templar, shared_loader_obj)
            self._task_vars = task_vars
            self._loader = loader
            self._templar = templar

        def run(self, tmp=None, task_vars=None):
            if task_vars is None:
                task_v

# Generated at 2022-06-13 10:09:12.923257
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(None, None, None, None, None)
    action_module_dir_args = {'dir': "vars", 'ignore_files': "main.yml", 'files_matching': ".*"}
    action_module_file_args = {'file': "roles/mysql/vars/Debian.yml", 'ignore_files': "main.yml", 'files_matching': ".*"}
    action_module_all_args = {'dir': "vars", 'ignore_files': "main.yml", 'files_matching': ".*", 'name': "results"}
    action_module_error = {'hash_behaviour': "invalid_value"}

    action_module._task.args = action_module_dir_args
    action_module._task.args = action

# Generated at 2022-06-13 10:09:23.886039
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    source_file = "/home/allen/Desktop/tst.yml"
    source_dir = "/home/allen/Desktop/tst"
    name = 'tst'
    task = Task()
    task._role = Role()
    task._role._role_path = "/home/allen/Desktop/roles/tst"
    task._ds = Play()
    task._ds._data_source = "/home/allen/Desktop/playbook.yml"
    task._ds._parent = TaskQueueManager()
    task._role._parent

# Generated at 2022-06-13 10:09:25.101760
# Unit test for constructor of class ActionModule
def test_ActionModule():
    return ActionModule(None, None, None)

# Generated at 2022-06-13 10:09:37.476422
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # mock _set_args
    action_module._set_args = MagicMock(name="_set_args")
    action_module._set_root_dir = MagicMock(name="_set_root_dir")
    action_module._set_dir_defaults = MagicMock(name="_set_dir_defaults")
    action_module._traverse_dir_depth = MagicMock(name="_traverse_dir_depth")
    action_module._is_valid_file_ext = MagicMock(name="_is_valid_file_ext")
    action_module._ignore_file = MagicMock(name="_ignore_file")
    action_module._load_files_in_dir = MagicMock(name="_load_files_in_dir")


    # call method run with arguments: tmp, task

# Generated at 2022-06-13 10:09:38.092009
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()

# Generated at 2022-06-13 10:10:58.902702
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import sys
    sys.path.append('/home/vagrant/workspace/ansible/test/units/module_utils')
    from ansible.module_utils.parsing.convert_bool import boolean

    class Task:
        def __init__(self,args):
            self.args = args

    class Datasource:
        def __init__(self,_data_source):
            self._data_source = _data_source

    class Role:
        def __init__(self,_role_path):
            self._role_path = _role_path

    class TaskDs:
        def __init__(self,_ds):
            self._ds = _ds


# Generated at 2022-06-13 10:11:00.486213
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert isinstance(module, ActionBase)


# Generated at 2022-06-13 10:11:07.354030
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test method run of class ActionModule
    """
    ActionModule_instance = ActionModule()

    # We test method run in case when depth == 0
    ActionModule_instance._task.args = {'var_files': 'file1.yml', 'file1.yml': 'var1=text1\n', 'var2': 'text2'}
    ActionModule_instance._task._role = None
    ActionModule_instance._task._ds = None
    results = ActionModule_instance.run()
    assert results['ansible_included_var_files'] == []
    assert results['ansible_facts'] == {'var1': 'text1', 'var2': 'text2'}

# Generated at 2022-06-13 10:11:08.447580
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print(ActionModule())

# Generated at 2022-06-13 10:11:09.121787
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False

# Generated at 2022-06-13 10:11:16.828075
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_args_dir = dict(dir='test')

    test_args_dir_depth = dict(dir='test', depth=1)

    test_args_dir_depth_recurse = dict(dir='test', depth=0)

    test_args_dir_depth_matching = dict(dir='test', depth=1, files_matching='test.yml')

    test_args_dir_depth_ignore_files = dict(dir='test', depth=1, ignore_files='test.yml')

    test_args_dir_depth_ignore_files_dict = dict(dir='test', depth=1, ignore_files=dict(test=1))

    test_args_dir_depth_ignore_files_list = dict(dir='test', depth=1, ignore_files=['test.yml'])

    test_

# Generated at 2022-06-13 10:11:20.292998
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test for class ActionModule
    module = ActionModule()

    # Test for method run of class ActionModule
    def test_run() -> None:
        pass

    test_run()

# Generated at 2022-06-13 10:11:26.438544
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import io
    import sys
    import unittest
    from os import path
    from tempfile import TemporaryDirectory
    from shutil import copyfile

    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.parsing.convert_bool import boolean

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

   

# Generated at 2022-06-13 10:11:34.648934
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.facts import Facts
    from ansible.playbook import PlayContext
    from ansible.vars import VariableManager
    from ansible.task import Task
    from ansible.plugins.action import ActionBase
    from ansible.parsing.yaml.objects import AnsibleUnicode

    def test_test():
        pass


# Generated at 2022-06-13 10:11:37.006458
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule('test', 'args', 'task', 'loader', 'templar', 'shared_loader_obj')
    assert type(a).__name__ == 'ActionModule'

# Generated at 2022-06-13 10:14:30.421573
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_args = {}
    task_vars = {}
    walk_return_value = [('some_path', [], ['main.yml'])]

    # Test with normal execution
    action = ActionModule(dict(), task_vars=task_vars)
    action._traverse_dir_depth = lambda: walk_return_value
    action._load_files_in_dir = lambda root_dir, var_files: (False, '', var_files)
    action._set_args()
    action._set_root_dir()
    assert action.source_dir == 'some_path'

    # Test with mock execution
    action = ActionModule(dict(), task_vars=task_vars)
    action._traverse_dir_depth = lambda: walk_return_value
    action._load_files_in_dir

# Generated at 2022-06-13 10:14:31.939006
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_am = ActionModule()
    assert test_am.run() == True


# Generated at 2022-06-13 10:14:32.754048
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:14:38.789098
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # source_dir = '~/dev/ansible_playbooks/playbooks/network/nxos/nxos_facts/vars/'
    source_dir = '/Users/sanabriar/dev/ansible_playbooks/playbooks/network/nxos/nxos_facts/vars/'
    args = {'dir': source_dir, 'depth': 0}
    am = ActionModule()
    am.run(task_vars={'ansible_fact_network_os': 'nxos'},
         _task=FakeTask(args=args))


# Generated at 2022-06-13 10:14:46.076400
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None)
    assert isinstance(module, ActionModule)
    assert module.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']
    assert module.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    assert module.VALID_FILE_ARGUMENTS == ['file', '_raw_params']
    assert module.VALID_ALL == ['name', 'hash_behaviour']


# Generated at 2022-06-13 10:14:54.831428
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import os.path
    import unittest
    import __builtin__
    import glob
    import shutil
    import yaml

    class MockModule(object):
        def __init__(self):
            self._role = None
            self._ansible_no_log = False
            self._ansible_verbosity = 0
            self._ansible_debug = False
            self._ansible_diff = False

    class MockRole(object):
        def __init__(self, role_path):
            self._role_path = role_path

    class MockTask(object):
        def __init__(self, role=None):
            self._role = role
            self._ds = None

        def get_ds(self):
            self._ds = '/etc/yml/main.yml'  # noqa
            return

# Generated at 2022-06-13 10:15:03.368820
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_obj = ActionModule()
    test_obj._task = 'test'
    test_obj._task.args = {
    'dir': 'test',
    'hash_behaviour': 'test_hash',
    'name': 'test_name'
    }
    test_obj._task._role = 'test_role'
    test_obj._task._role._role_path = 'test_role.path'
    test_obj._task._ds = 'test_ds'
    test_obj._task._ds._data_source = 'test_source'
    test_obj._loader = 'test_loader'
    test_obj._loader._get_file_contents = lambda x, y: x
    test_obj.show_content = True
    test_obj.included_files = 'test_file'
    test_

# Generated at 2022-06-13 10:15:04.340314
# Unit test for constructor of class ActionModule
def test_ActionModule():
    AM = ActionModule()
    print(AM)

# Generated at 2022-06-13 10:15:05.790867
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Tests to validate the run method of the class ActionModule
    """
    pass



# Generated at 2022-06-13 10:15:13.839833
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setting
    task = {
        'name': 'my_test_task',
        'args': {
            'file': 'my_test_file',
            'name': 'my_test_var_name'
        },
        'directory': 'my_test_directory'
    }
    # my_task = Task.load(task)
    # my_task.args = {'file': 'my_test_file', 'name': 'my_test_name'}
    # my_task.directory = 'my_test_directory'
    # my_vars = {
    #     'my_test_variable': 'my_test_value',
    #     'my_test_variable2': 'my_test_value2'
    # }
    # my_search_path = 'my_test_search_path'
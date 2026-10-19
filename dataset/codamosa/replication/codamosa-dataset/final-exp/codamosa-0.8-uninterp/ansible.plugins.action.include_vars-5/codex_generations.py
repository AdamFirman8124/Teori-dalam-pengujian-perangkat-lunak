

# Generated at 2022-06-13 10:06:07.359578
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tests.utils as utils
    import ansible.executor.task_result as task_result
    import ansible.plugins.loader as plugin_loader
    import ansible.template as template
    import ansible.vars.manager as vars_manager
    import ansible.vars.unsafe_proxy as unsafe_proxy

    t = utils.DummyTask('include_vars', 'play')
    am = ActionModule(t, '/tmp', 'config', 'runner')
    setattr(t, '_role', 'role')
    setattr(t, '_ds', '/var/tmp')

    # first run
    am._set_args()
    am._set_root_dir()
    am.return_results_as_name = 'result_as_name'

# Generated at 2022-06-13 10:06:20.175816
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict()

    source_dir = '/path/to/dir'
    source_file = 'test.yml'
    source_dir_file = source_dir + '/' + source_file
    dir_args = {
        'dir': source_dir,
        'depth': 0,
        'files_matching': None,
        'ignore_files': 'test.yml',
    }
    file_args = {
        'file': source_file,
        '_raw_params': None,
    }

    # Test run with source_dir
    task = MockTask(dir_args)
    action = ActionModule(task, task_vars)
    action._set_args()
    action._is_valid_file_ext = Mock(returns=True)
    action._set_root_dir

# Generated at 2022-06-13 10:06:31.448040
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class Task:
        def __init__(self, role=None, args=dict()):
            self.role = role
            self.args = args

        def _role(self):
            return self.role

    class Role:
        def __init__(self, role_path=str()):
            self.role_path = role_path

        def _role_path(self):
            return self.role_path

    class DataSource:
        def __init__(self, data_source=str()):
            self.data_source = data_source

        def _data_source(self):
            return self.data_source

    class TaskDS:
        def __init__(self, ds=DataSource()):
            self.ds = ds

        def _ds(self):
            return self.ds


# Generated at 2022-06-13 10:06:41.257027
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    # The following code is used to perform setup
    # required to run the unit test.
    code_block = """
    - include_vars:
        file: 'some_file'
        name: 'test_var'
        _raw_params: 'some_file'
    """
    task_vars = dict()
    variable_manager = VariableManager()
    loader = DataLoader()
    host_list = [Inventory(loader=loader).get_host('all')]
    variable_manager.set_inventory(Inventory(host_list=host_list))
    variable_manager.set_vault_secrets('hashivault')

# Generated at 2022-06-13 10:06:48.515498
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Test the constructor of the class ActionModule
    """
    from ansible.plugins.action.include_vars import ActionModule
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert action_module.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']
    assert action_module.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    assert action_module.VALID_FILE_ARGUMENTS == ['file', '_raw_params']
    assert action_module.VALID_ALL == ['name', 'hash_behaviour']


# Generated at 2022-06-13 10:06:58.081859
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Test the output of the run method of the class ActionModule.
    """
    class MockTask(object):
        def __init__(self, a_args, a_ds, a_role):
            self.args = a_args
            self._ds = a_ds
            self._role = a_role


    action_module = ActionModule()
    action_module._task = MockTask({'depth': 5}, 'ansible/roles/role1/tasks/main.yml', 'role1')
    action_module.VALID_FILE_EXTENSIONS = ['yaml', 'yml', 'json']
    action_module.valid_extensions = ['yaml', 'yml', 'json']
    action_module.show_content = True
    action_module.included_files = []


# Generated at 2022-06-13 10:07:00.329423
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: Create tests.
    pass

# Generated at 2022-06-13 10:07:09.261503
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Do not need to test takes_args and takes_params, they are abstract methods
    # and are
    # in the base class
    # mock data
    test_response = {'ansible_facts': {"hello": "world"},
                     'ansible_included_var_files': ['hosts'],
                     '_ansible_no_log': True,
                     'failed': False
    }

    # mock data for args
    test_args_dir_success = {'dir': '.', 'extensions': 'yml'}
    test_args_dir_failure = {'dir': '.', 'extensions': 'yml',
                             'files_matching': '^(?!hello.yml$).*$'}
    test_args_file_success = {'file': 'hello.yml'}


# Generated at 2022-06-13 10:07:19.073564
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    try:
        from unittest.mock import patch
        from io import StringIO
        from ansible.module_utils.six import PY3
    except ImportError:
        from mock import patch
        from StringIO import StringIO
        PY3 = True
    from ansible.errors import AnsibleError
    from ansible.plugins.action.vars import ActionModule
    from ansible.module_utils.six import string_types

    def _get_basic_task(action_base):
        action_base._task.action = 'include_vars'
        action_base._task.args = dict()
        return action_base


# Generated at 2022-06-13 10:07:19.481367
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:07:43.422957
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True == False

# Generated at 2022-06-13 10:07:44.708941
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None


# Generated at 2022-06-13 10:07:52.776083
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # init
    from ansible.plugins.loader import action_loader
    from ansible.playbook.task import Task

    t = Task()
    t.args = {'file': '../tests/resources/vars.yml'}
    action = action_loader.get('include_vars', task=t)

    # call
    result = action.run(task_vars={})

    # assert
    assert result['ansible_facts'] == {
        'var1': 'test1',
        'var2': 'test2',
        'var3': {'var3': 'test3'}
    }
    assert result['ansible_included_var_files'] == ['../tests/resources/vars.yml']


# Generated at 2022-06-13 10:07:53.585295
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO
    pass



# Generated at 2022-06-13 10:08:01.810743
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    from ansible.utils.vars import combine_vars

    data1 = (
        { "a": [1, 2], "b": { "c": 3, "d": 4 } }
        )

    data2 = (
        { "a": [3, 4], "b": { "c": 5, "e": 6 } }
        )

    data3 = (
        { "a": [5, 6], "b": { "f": 7, "e": 8 } }
        )


# Generated at 2022-06-13 10:08:12.811812
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    options = dict()
    variable_manager = VariableManager()
    loader = DataLoader()

# Generated at 2022-06-13 10:08:22.633049
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    task_vars = dict()

    test_args = dict(
        name='test_name',
        dir='test_dir',
        depth=2,
        files_matching='mykey',
        extensions='yaml',
        ignore_unknown_extensions=True,
        ignore_files=['main.yml', 'defaults.yml']
    )

    action = ActionModule(
        {"name": "test name", "task": ""},
        task={"args": test_args},
        connection=None,
        play_context={"basedir": ""},
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    result = action.run(task_vars=task_vars)

    assert result['ansible_facts'] == dict()
    assert result

# Generated at 2022-06-13 10:08:23.496144
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:08:26.454952
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        test_class = ActionModule()
        assert(True)
    except:
        assert(False)


# Generated at 2022-06-13 10:08:27.936371
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule('test')._task.args == 'test'

# Generated at 2022-06-13 10:09:12.990559
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:09:21.101847
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    am.TRANSFERS_FILES = False
    am.VALID_FILE_EXTENSIONS = ['yaml', 'yml', 'json']
    am.VALID_DIR_ARGUMENTS = ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    am.VALID_FILE_ARGUMENTS = ['file', '_raw_params']
    am.VALID_ALL = ['name', 'hash_behaviour']
    #am._set_dir_defaults()
    #am._set_args()
    #assert not am.run()

    #am.source_dir = True

# Generated at 2022-06-13 10:09:22.171427
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 10:09:24.211947
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:09:26.357580
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, 'run')
    assert hasattr(ActionModule, '_load_files')

# Generated at 2022-06-13 10:09:38.468523
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # import ansi.module_utils.ansible_free5gc_module
    # import ansible.modules.converters.network.nso
    import ansible.modules.converters.network.nso as nso

    # new_nso = ansible.module_utils.ansible_free5gc_module.AnsibleModule(argument_spec={}, supports_check_mode=False)
    new_nso = nso.AnsibleModule(argument_spec={}, supports_check_mode=False)
    # print("type: ", type(new_nso))

    arg_name_value = {'name': 'test_name', 'hash_behaviour': 'merge',  'file': 'input.yaml', '_raw_params': 'input.yaml'}

# Generated at 2022-06-13 10:09:40.091128
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass
    # TODO: implement unit test


# Generated at 2022-06-13 10:09:48.364081
# Unit test for constructor of class ActionModule
def test_ActionModule():
    my_module = ActionModule()
    assert my_module.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']
    assert my_module.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    assert my_module.VALID_FILE_ARGUMENTS == ['file', '_raw_params']
    assert my_module.VALID_ALL == ['name', 'hash_behaviour']



# Generated at 2022-06-13 10:09:53.354384
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert getattr(ActionModule, 'run') is not None
    assert getattr(ActionModule, '_set_args') is not None
    assert getattr(ActionModule, '_load_files') is not None
    assert getattr(ActionModule, '_load_files_in_dir') is not None

# Generated at 2022-06-13 10:09:55.703715
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.loader
    test_module = ansible.plugins.loader.get("action", "include_vars")
    assert isinstance(test_module, ActionModule)


test_ActionModule()

# Generated at 2022-06-13 10:11:47.522327
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert len(ActionModule.VALID_FILE_EXTENSIONS) > 0
    assert len(ActionModule.VALID_DIR_ARGUMENTS) > 0
    assert len(ActionModule.VALID_FILE_ARGUMENTS) > 0
    assert len(ActionModule.VALID_ALL) > 0
    assert ActionModule(dict()).run(task_vars=dict()) == dict(ansible_facts=dict())

# Generated at 2022-06-13 10:11:58.147896
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    play_context = PlayContext()
    templar = Templar(play_context=play_context)
    
    task_vars = dict()
    results = dict()

    # Call method run of class ActionModule with source_dir
    task = TaskInclude()
    task._role = None
    task._ds = None
    task.args = dict()
    
    task.args = dict(dir = '../data/var_files')
    task.args = dict(depth = 1)
    task.args = dict(files_matching = '.*')

# Generated at 2022-06-13 10:11:58.827232
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:12:10.502181
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    def get_tmp_path(tmp, *args):
        return path.join(tmp, *args)

    def get_file_content(filename):
        with open(filename) as fh:
            return fh.read()

    def write_file(filename, content):
        with open(filename, 'w') as tmp_file:
            tmp_file.write(content)

    from ansible.module_utils._text import to_bytes

    from ansible.plugins.action import ActionBase
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    import ansible.config
    from ansible.utils.vars import combine_vars


# Generated at 2022-06-13 10:12:19.318354
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.task.include_vars import ActionModule
    import tempfile
    import shutil
    import os
    import sys
    import json

    class MockModule:
        def __init__(self):
            self.task = MockModule()
            self.task.args = dict()
            self.task.args['_raw_params'] = 'foo.json'
            self.task.args['name'] = 'foo'
            self.task.args['hash_behaviour'] = 'merge'
            self.task._role = MockModule()
            self.task._role._role_path = tempfile.mkdtemp()
            self.task._ds = MockModule()

# Generated at 2022-06-13 10:12:31.197192
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # dir
    print(1)
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action_module._set_args()
    print(action_module.source_file)
    assert action_module.source_dir is None
    assert action_module.source_file is None
    assert action_module.depth is None
    assert action_module.files_matching is None
    assert action_module.ignore_unknown_extensions is False
    assert isinstance(action_module.ignore_files, list)
    assert action_module.return_results_as_name is None

    # file
    print(2)

# Generated at 2022-06-13 10:12:32.006058
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:12:33.136114
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """"""
    pass



# Generated at 2022-06-13 10:12:42.061258
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    import sys
    import os

    root_dir = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
    sys.path.append(os.path.join(root_dir, "lib"))

    from ansible.module_utils import basic

    from ansible.plugins.action import ActionBase

    from ansible.parsing import vault
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleMapping, AnsibleSequence

    class TestModule(object):
        def __init__(self, data):
            self.params = data

    class TaskDS(object):
        def __init__(self, data):
            self._data_source = data


# Generated at 2022-06-13 10:12:52.020558
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader

    mock_task = type('Mock', (object,), {
        "_role": None,
        "_ds": None,
        "args": dict()
    })
    mock_task._role = type('MockRole', (object,), {
        "_role_path": "/path/to/roles/myrole",
        "name": "myrole"
    })
    mock_task._ds = type('MockDS', (object,), {
        "_data_source": "/path/to/roles/myrole/tasks/main.yml"
    })

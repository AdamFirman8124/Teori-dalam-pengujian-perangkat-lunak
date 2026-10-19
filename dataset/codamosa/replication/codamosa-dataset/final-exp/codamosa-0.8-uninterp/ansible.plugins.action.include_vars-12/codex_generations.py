

# Generated at 2022-06-13 10:06:01.502814
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create an instance of the class
    action = ActionModule()

# Generated at 2022-06-13 10:06:02.377839
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: Implement unit tests
    return True

# Generated at 2022-06-13 10:06:04.998244
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create a basic action module
    mod = ActionModule()
    # setup a command and run it
    mod.run(task_vars={'foo': 'bar', 'one': 'two'})
    # iterate over the result to get the command
    for result in mod.run_command(['echo', '"hello"'])['rc']:
        print(result)

# Generated at 2022-06-13 10:06:10.735004
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.manager import VariableManager

    class Master:
        def __init__(self):
            self.name = 'Master'
            self.hostvars = {}
            self.inventory = None
            self.vars = {}
            self.get_vars = lambda: self.vars

    class Inventory:
        def __init__(self, hostvars):
            self.hosts = ['localhost']
            self.hosts = {'localhost': {'vars': hostvars}}

    class Role:
        def __init__(self, _role_path):
            self._role_path = _role_path


# Generated at 2022-06-13 10:06:13.812785
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert(isinstance(action, ActionBase))
    assert(action.TRANSFERS_FILES == False)


# Generated at 2022-06-13 10:06:16.004819
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert type(ActionModule("task", "file", "path", "loader"))

# Generated at 2022-06-13 10:06:22.216326
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']
    assert ActionModule.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    assert ActionModule.VALID_FILE_ARGUMENTS == ['file', '_raw_params']
    assert ActionModule.VALID_ALL == ['name', 'hash_behaviour']


# Generated at 2022-06-13 10:06:24.362569
# Unit test for constructor of class ActionModule
def test_ActionModule():
    klass = ActionModule(task=dict())
    assert isinstance(klass, ActionModule)


# Generated at 2022-06-13 10:06:26.842375
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ test setup """
    action_module = ActionModule("localhost", MockTask())
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 10:06:36.966682
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import os
    os.system('mkdir folder')
    os.chdir('folder')
    f = open('test.yml', 'w')
    f.write('---\n- hosts: all\n  vars: {test: success}\n')
    f.close()
    os.chdir('..')

    import sys
    sys.path.append('.')

    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.context import CLIARGS

    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-13 10:07:04.615923
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print('Testing constructor of class ActionModule')
    module = ActionModule()
    print('State of object:', str(module))

    print('Testing destructor of class ActionModule')
    del module

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:07:11.558530
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(task_ds=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    result = module.run(task_vars=dict())

    assert 'failed' in result
    assert result['failed'] is True
    assert 'message' in result
    assert result['message'] == 'Invalid arguments passed to include_vars'



# Generated at 2022-06-13 10:07:17.247706
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('Testing method `run` of class `ActionModule`')

    from ansible.plugins.action.vars import ActionModule  # noqa: F401

    # Test for failure when a required argument is missing
    try:
        am = ActionModule
        am.run(am, {})
    except Exception as e:
        assert e.args[0] == 'Source file or source dir (file, dir) must be specified'



# Generated at 2022-06-13 10:07:23.257455
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import combine_vars
    from ansible.conf import default_loader
    from ansible.plugins.callback import CallbackBase
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    class AnsibleHost:
        def __init__(self, host_name, host_vars):
            self.name = host_name
            self.vars = host_vars


# Generated at 2022-06-13 10:07:27.032694
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module._task is None
    assert action_module._connection is None
    assert action_module._play_context is None
    assert action_module._loader is None
    assert action_module._templar is None
    assert action_module._shared_loader_obj is None

# Generated at 2022-06-13 10:07:35.004678
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    import os
    import tempfile

    cur_dir = os.path.dirname(os.path.realpath(__file__))
    role_dir = os.path.join(cur_dir, '../../../', 'test/integration/targets/test_custom_include_vars_plugin/roles/test_plugin')

    task_include = TaskInclude(block=Block(), task_ds={'role': 'test_plugin'})

    # Create temporary directory and files
    tmp_dir = tempfile.mkdtemp(prefix='ansible_')
    tmp_dir2 = tempfile.mkdtemp(prefix='ansible_')

# Generated at 2022-06-13 10:07:43.008823
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor for ActionModule
    action_module = ActionModule()
    assert action_module.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']
    assert action_module.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    assert action_module.VALID_FILE_ARGUMENTS == ['file', '_raw_params']
    assert action_module.VALID_ALL == ['name', 'hash_behaviour']


# Generated at 2022-06-13 10:07:52.363092
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.plugins.loader import action_loader
    import ansible.plugins.action as action
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    action_loader.add_directory(path.join(path.dirname(action.__file__), '_vars_plugins'))
    mock_loader, inventory, variable_manager = MockLoader(), MockInventory(), MockVariableManager()
    play_context = PlayContext()
    play_context.run_as_root = False
    play_context.remote_user = 'root'
    play_context.connection = 'ssh'   # Need a connection as Variables.

# Generated at 2022-06-13 10:07:53.155142
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # This is a stub
    pass



# Generated at 2022-06-13 10:07:55.135536
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' Method that tests the ActionModule constructor by creating an instance of it
    '''
    assert('run' in dir(ActionModule))


# Generated at 2022-06-13 10:08:54.563619
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # define test variables
    module_return_value = {
        'ansible_included_var_files': [],
        'ansible_facts': {
            'var1': 'val1', 'var2': 'val2', 'var3': 'val3'
        },
        '_ansible_no_log': False,
        'changed': False,
        '_ansible_verbosity': 0
    }

    # define mock objects
    class MockTask:
        def __init__(self):
            self.args = {
                'name': None,
                'file': path.abspath('./test/test_vars/input/test_input1.yml'),
                'hash_behaviour': None
            }

    class MockCallbacks:
        def __init__(self):
            self.verb

# Generated at 2022-06-13 10:08:55.403235
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:08:56.314161
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO
    pass

# Generated at 2022-06-13 10:09:04.441021
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for method run of class ActionModule
    """
    source = 'test_include_vars.yml'
    test_ActionModule = ActionModule()
    test_ActionModule._task = mock_task
    test_ActionModule._task.args = {'_raw_params': './test/' + source}
    test_ActionModule._connection = mock_connection
    result = test_ActionModule.run(None, None)
    assert result
    assert result['_ansible_no_log'] is False
    assert result['ansible_facts']['test_load_vars_file'] == ['Content of ' + source]
    assert result['ansible_facts']['test_load_vars_dir'] == ['Content of subdir/' + source]


# Generated at 2022-06-13 10:09:15.927964
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.role.definition import RoleDefinition
    from StringIO import StringIO

    my_vars = dict(
        ansible_connection='local',
        ansible_ssh_user='user',
        ansible_ssh_pass='pass',
        ansible_port=22
    )
    my_task = Task()
    my_task._role = RoleDefinition()
    my_task.args = dict(
        file='/path/to/file'
    )
    ActionModule(my_task, StringIO()).run(task_vars=my_vars)

    my_task = Task()
    my_task._role = RoleDefinition()
    my_task.args = dict(
        name='passed'
    )

# Generated at 2022-06-13 10:09:26.010983
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import basic
    from ansible.module_utils import six


# Generated at 2022-06-13 10:09:34.303098
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for method run of class ActionModule
    """

    #Create instance of class ActionModule
    assert isinstance(ActionModule, type)
    action_module_instance = ActionModule()

    #Test attribute run
    assert hasattr(action_module_instance, "run")
    assert callable(getattr(action_module_instance, "run"))
    assert isinstance(action_module_instance.run, object)


# Generated at 2022-06-13 10:09:40.120856
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)
    assert ActionModule.TRANSFERS_FILES is False
    assert isinstance(ActionModule.VALID_FILE_EXTENSIONS, list)
    assert isinstance(ActionModule.VALID_DIR_ARGUMENTS, list)
    assert isinstance(ActionModule.VALID_FILE_ARGUMENTS, list)
    assert isinstance(ActionModule.VALID_ALL, list)

# Generated at 2022-06-13 10:09:42.285367
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    l = ActionModule(None, None, None)
    l.run(None, {'test': 'me'})

# Generated at 2022-06-13 10:09:45.141233
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    dir_defaults = module._set_dir_defaults()
    assert dir_defaults is None
    args = module._set_args()
    assert args is None



# Generated at 2022-06-13 10:11:38.075071
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None, None, None)
    assert type(action_module) is ActionModule


# Generated at 2022-06-13 10:11:42.719572
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule(None, None)
    assert isinstance(m, ActionBase)
    assert not hasattr(m, 'show_content')
    assert not hasattr(m, 'included_files')
    assert not hasattr(m, 'source_dir')
    assert not hasattr(m, 'source_file')


# Generated at 2022-06-13 10:11:50.906404
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print('Testing ActionModule')
    action = ActionModule(1, 2, 'some_var')

    assert action.VALID_DIR_ARGUMENTS == ['dir', 'depth',
                                          'files_matching', 'ignore_files',
                                          'extensions', 'ignore_unknown_extensions'],\
        'Failed to initialize VALID_DIR_ARGUMENTS'

    assert action.VALID_FILE_ARGUMENTS == ['file', '_raw_params'],\
        'Failed to initialize VALID_FILE_ARGUMENTS'

    assert sorted(action.VALID_ALL) == sorted(['name', 'hash_behaviour']),\
        'Failed to initialize VALID_ALL'


# Generated at 2022-06-13 10:12:00.508305
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_task = {}
    test_task['name'] = 'AnsibleModule: include_vars'
    test_task['action'] = {}
    test_task['action']['__ansible_argspec'] = {'args': []}
    # test_task['action']['__ansible_argspec']['args'].append(['file', {'removed_in_version': '2.13'}])
    test_task['action']['__ansible_argspec']['args'].append(['dir', {}])
    test_task['action']['__ansible_argspec']['args'].append(['name', {}])

# Generated at 2022-06-13 10:12:04.931220
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        module = ActionModule()
    except Exception as e:
        print("ActionModule constructor test failed.\nError: %s" % e)
        return False

    print("ActionModule constructor test succeeded.")
    return True


# Generated at 2022-06-13 10:12:08.614818
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None)
    assert action_module
    assert str(action_module)
    assert repr(action_module)

# Test for _set_dir_defaults method

# Generated at 2022-06-13 10:12:10.657928
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Check if constructor can be created
    actionModule = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Validate private method of class
    results = actionModule._traverse_dir_depth()
    assert results is not None

# Generated at 2022-06-13 10:12:18.395613
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:12:18.958897
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()

# Generated at 2022-06-13 10:12:30.841195
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: remove this duplicated code
    from ansible.module_utils.six import PY2
    from ansible.plugins import action
    from ansible.utils.vars import combine_vars

    class MockTaskDS:

        def __init__(self):
            self._data_source = None

        def set_data_source(self, data_source):
            self._data_source = data_source


    class MockTask:

        def __init__(self):
            self._role = None
            self._ds = MockTaskDS()
            self._ds.set_data_source('/Users/al/workspace/ansible-playbook/test/units/library/include_vars/yml/1/main.yml')
            self.args = {}

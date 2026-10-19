

# Generated at 2022-06-13 10:06:07.565954
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # __init__
    class Fake_ActionModule_run_Task(object):
        def __init__(self):
            self.args = dict()
            self.args['hash_behaviour'] = 'merge'
            self.args['name'] = 'mock_result'
            self.args['dir'] = 'vars'

    class Fake_ActionModule_run_DS(object):
        def __init__(self):
            self._data_source = '../../../../library/modules/include_vars.py'

    class Fake_ActionModule_run_Role(object):
        def __init__(self, role_path):
            self._role_path = role_path

    class Fake_ActionModule_run_Loader(object):
        def __init__(self):
            self.__inits = dict()


# Generated at 2022-06-13 10:06:20.396504
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("ActionModule_run")

    # Create mocks
    tmp = None
    task_vars = dict()
    display = dict()

    # Create the instance of class ActionModule
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action_module._display = display

    # Test empty args, exception
    try:
        action_module.run(tmp=tmp, task_vars=task_vars)
    except AnsibleError as e:
        expected_e_msg = 'Missing required arguments: dir'
        assert(expected_e_msg == e.args[0])

    # Test with only dir and depth
    task_vars['dir'] = 'dir'
    task_vars['depth']

# Generated at 2022-06-13 10:06:31.660622
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(not ActionModule({'dir': 'dir_test'}).source_dir)
    assert(not ActionModule({'dir': 'dir_test', 'depth': 0, 'ignore_files': 'file_test', 'extensions': 'yaml'}).source_dir)
    assert(ActionModule({'dir': 'dir_test', 'depth': 0, 'ignore_files': 'file_test', 'extensions': 'yaml', 'ignore_unknown_extensions': False}).source_dir == 'dir_test')
    assert(ActionModule({'dir': 'dir_test', 'depth': 0, 'ignore_files': 'file_test', 'extensions': 'yaml', 'ignore_unknown_extensions': False}).depth == 0)

# Generated at 2022-06-13 10:06:38.749146
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    action_module._loader = TestLoader()
    action_module._task = TestTask()
    results = action_module.run(task_vars=dict(test1=1, test2=2))
    assert results == {'ansible_facts': {'testvar': 'testval'},
                       'ansible_included_var_files': ['/path/to/file1', '/path/to/file2'],
                       '_ansible_no_log': True}


# Generated at 2022-06-13 10:06:41.161170
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, {}) is not None
    assert ActionModule(None, {})._task.args == {}


# Generated at 2022-06-13 10:06:51.888760
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    fails = []
    #case 1
    print("case 1 ")
    source_dir = 'test_data'
    depth = 0
    files_matching = '.*'
    ignore_files = ['test.yml']
    extensions = ['yml', 'yaml']
    ignore_unknown_extensions = True
    name = "results"
    hash_behaviour = "merge"

    source_file = None

    x = ActionModule(files_matching=files_matching,
                     extensions=extensions,
                     ignore_unknown_extensions=ignore_unknown_extensions,
                     ignore_files=ignore_files,
                     depth=depth,
                     dir=source_dir,
                     file=source_file,
                     name=name,
                     hash_behaviour=hash_behaviour)
    y = x.run

# Generated at 2022-06-13 10:06:53.975146
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(load_fragment = True)
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 10:06:54.870028
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 'ActionModule' in dir(ActionModule())

# Generated at 2022-06-13 10:07:00.602069
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_action = ActionModule(None, None, None)
    current_dir = '/'.join(__file__.split('/')[:-1])
    assert test_action._find_needle('vars', 'main.yml') == path.join(current_dir, 'vars', 'main.yml')

# Generated at 2022-06-13 10:07:01.913379
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Debatable whether to test run method
    pass

# Generated at 2022-06-13 10:07:33.304613
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Check 'unittest' is supported
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    # Test class
    class ActionModule_test(unittest.TestCase):
        # Setup class
        @classmethod
        def setUpClass(cls):
            # Create an instance of the action plugin class
            cls.action_module = ActionModule()
            cls.action_module.valid_extensions = ActionModule.VALID_FILE_EXTENSIONS
            cls.action_module._task = type('task', (), {})
            cls.action_module._task.args = dict()
            cls.action_module._task._ds = type('datasource', (), {})

# Generated at 2022-06-13 10:07:44.278252
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import fixtures
    import tempfile
    import copy
    import shutil
    import json

    # init ActionModule
    try:
        tmpdir = tempfile.mkdtemp()
        action = ActionModule(task=fixtures.mock_task(), connection=None, play_context=fixtures.mock_play_context(), loader=None, templar=None, shared_loader_obj=None)
    except Exception as exc:
        shutil.rmtree(tmpdir)
        assert False, 'Exception: {0}'.format(exc)

    # test run method

# Generated at 2022-06-13 10:07:47.944718
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(None, None, None, None)
    assert module.run() == {
            '_ansible_no_log': False,
            'ansible_facts': {},
            'ansible_included_var_files': []
        }

# Generated at 2022-06-13 10:07:48.401910
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule().run()

# Generated at 2022-06-13 10:07:57.386628
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from __main__ import ActionModule
    from __main__ import Display
    
    display = Display()
    action_module = ActionModule(display)

    # test instance variables
    assert (action_module.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json'])
    assert (action_module.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions'])
    assert (action_module.VALID_FILE_ARGUMENTS == ['file', '_raw_params'])
    assert (action_module.VALID_ALL == ['name', 'hash_behaviour'])

    # test method _set_dir_defaults
    action_module.depth = 3
    action_module.files_match

# Generated at 2022-06-13 10:07:58.355323
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False, "Test not implemented"

# Generated at 2022-06-13 10:08:06.460671
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_data = {
        'name': 'test_param',
        'hash_behaviour': 'merge',
        'dir': '.',
        'depth': 0,
        'files_matching': None,
        'ignore_files': None,
        'extensions': None,
        'ignore_unknown_extensions': False
    }
    task = {'action': {
        '__ansible_module__': 'include_vars',
        '__ansible_arguments__': test_data
    },
    'args': test_data
    }
    task['vars'] = {}
    module = ActionModule(task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert isinstance(module, ActionModule)

    module.run

# Generated at 2022-06-13 10:08:16.721338
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ ActionModule_run method tests. """
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.utils import context_objects as co
    from ansible.executor.task_queue_manager import TaskQueueManager

    class RunWrapper:
        def __init__(self, source_dir, source_file, extension, depth):
            self.extension = extension
            self.depth = depth
            self.source_dir = source_dir
            self.source_file = source_file


# Generated at 2022-06-13 10:08:25.245975
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.playbook.play_context
    import ansible.playbook.role
    import ansible.playbook.task
    import ansible.utils.vars
    context = ansible.playbook.play_context.PlayContext()
    role = ansible.playbook.role.Role()
    role._role_path = '/tmp/role'
    task = ansible.playbook.task.Task()
    task._role = role
    task_vars = dict()
    tmp = dict()
    module = ActionModule(task, tmp, task_vars)
    module.source_dir = 'vars'
    module._set_root_dir()
    module.depth = 0
    module.ignore_unknown_extensions = True
    module.ignore_files = None

# Generated at 2022-06-13 10:08:26.392181
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action is not None

# Generated at 2022-06-13 10:09:15.664045
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert not action_module.depth
    assert not action_module.ignore_files
    assert not action_module.return_results_as_name
    assert not action_module.source_dir
    assert not action_module.source_file

# Generated at 2022-06-13 10:09:17.256955
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule().run()

# Generated at 2022-06-13 10:09:25.111830
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert action_module
    assert isinstance(action_module, ActionModule)
    assert isinstance(action_module.VALID_FILE_EXTENSIONS, list)
    assert isinstance(action_module.VALID_DIR_ARGUMENTS, list)
    assert isinstance(action_module.VALID_FILE_ARGUMENTS, list)
    assert isinstance(action_module.VALID_ALL, list)

# Generated at 2022-06-13 10:09:35.490378
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    import ansible.config

    class TestActionModule(unittest.TestCase):

        def setUp(self):
            self.maxDiff = None
            self.action = ActionModule()

        def tearDown(self):
            pass

        def test_returns_dict_with_ansible_included_var_files(self):

            self.action.run()

            self.assertIsInstance(self.action.run(), dict)

    unittest.main()

if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:09:45.903441
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.include import RoleInclude
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.strategy import StrategyBase
    from ansible.plugins.callback import CallbackBase
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from io import StringIO

    # Make

# Generated at 2022-06-13 10:09:57.665198
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MockTask():
        def __init__(self, args):
            self.args = args
            self._role = None
            self._ds = None

    class Mock(object):
        """ Mock object for the importer plugin object """
        pass

    class MockLoader():
        """ Mock object for the loader plugin object """
        def __init__(self):
            self.data = ''
            self.file_name = ''
            self.show_content = True

        def load(self):
            if self.file_name in ['bar.yml', 'baz.yml']:
                if self.file_name == 'bar.yml':
                    return dict(foo=dict(baz=True))

# Generated at 2022-06-13 10:09:59.051912
# Unit test for constructor of class ActionModule
def test_ActionModule():
  module = ActionModule()
  assert module != None

# Generated at 2022-06-13 10:10:04.599175
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # test 1: Invalid value for depth

    task = dict(
        action=dict(
            dir='vars',
        ),
        args=dict(
            dir='vars',
            depth='invalid'
        ),
        role=dict(
            role_name='dummy_role',
            role_path='/path/to/roles/dummy_role/vars/main.yml'
        ),
        _ds=dict(
            _data_source='/path/to/roles/dummy_role/vars/main.yml'
        )
    )

    with pytest.raises(AnsibleError) as excinfo:
        action = ActionModule(task, connection=None, play_context=None, loader=None, templar=None)

# Generated at 2022-06-13 10:10:05.718309
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:10:06.340042
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 10:12:05.717027
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins import action
    action_module = action.ActionModule(None, None, None)
    assert isinstance(action_module, action.ActionModule)

# Generated at 2022-06-13 10:12:13.244312
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.loader import action_loader
    action = action_loader.get('include_vars', class_only=True)
    action. RUN_OKAY = False
    action._set_args()
    print(action.source_dir)
    print(action.source_file)
    print(action.depth)
    print(action.files_matching)
    print(action.ignore_unknown_extensions)
    print(action.ignore_files)
    print(action.valid_extensions)


# Generated at 2022-06-13 10:12:14.174743
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()

# Generated at 2022-06-13 10:12:15.098911
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, dict())

# Generated at 2022-06-13 10:12:17.248710
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)


# Generated at 2022-06-13 10:12:28.641140
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  """
  Setting up Ansible module to test
  """
  from ansible.module_utils.facts import ansible_module
  from ansible.module_utils.facts import ansible_all_facts
  from ansible.module_utils.facts import Facts

  module_args = dict(
    hash_behaviour = 'merge',
    name = 'my_var',
    depth = 0,
    file = 'my_directory/my_file'
  )

  def _get_file_contents(self, file_name):
    try:
      with open(file_name, 'rb') as results:
        return results.read().decode('utf-8')
    except Exception as e:
      pass


# Generated at 2022-06-13 10:12:30.117946
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module is not None

# Generated at 2022-06-13 10:12:33.587327
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict()
    source_dir = "vars/main.yml"
    _task = dict()
    assert ActionModule(_task, task_vars).source_dir == source_dir


# Generated at 2022-06-13 10:12:42.364876
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # 1. Create a mock class for ansible.module_utils.parsing.dataroot.AnsibleDataroot
    ANSIBLE_MODULE_UTILS_PARSING_DATAROOT_ANSIBLE_DATAROOT = TYPE_CHECKING and \
                            Mock(name='AnsibleDataroot', spec=AnsibleDataroot)
    ANSIBLE_MODULE_UTILS_PARSING_DATAROOT_ANSIBLE_DATAROOT.ansible_vars_dirs = ['/test']

    # 2. Create a stub class for ansible.parsing.dataloader.DataLoader

# Generated at 2022-06-13 10:12:52.311933
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    a = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    a.TRANSFERS_FILES = False

    # Test case 1
    a.show_content = True
    a.included_files = []
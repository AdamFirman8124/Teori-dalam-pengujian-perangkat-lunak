

# Generated at 2022-06-13 10:06:01.057873
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:06:06.251518
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:06:10.686971
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    file_action = ActionModule()
    file_action._task = {}
    file_action._task['args'] = {'dir': 'tests/unit/fixtures/vars_dir'}
    file_action.run(None, None)

# Generated at 2022-06-13 10:06:11.968007
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, None, None)

# Generated at 2022-06-13 10:06:14.354936
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(dict(), dict(), False, './test')
    assert action_module


# Generated at 2022-06-13 10:06:17.044811
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test if initialisation of ActionModule is done correctly
    import ansible.executor.task_queue_manager

    # create instance of ActionBase
    from ansible.plugins.action.load_vars import ActionModule as action_module

    tqm = ansible.executor.task_queue_manager.TaskQueueManager(None, None, None, None, None, None, None)
    task = ansible.playbook.task.Task()
    action_module('TestAction', task, tqm)
    assert True

# Generated at 2022-06-13 10:06:25.706655
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import unittest
    import mock
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    # Set up ActionModule from Module shared fixture
    # The fixture is set up to run tests for module 'include_vars'
    action = ActionModule(Task({}))
    action.setup_loader()

    class MyTest(unittest.TestCase):
        tests_result = []
        tests_args_set = []
        tests_args_set_dir_defaults = []
        tests_args_set_file_defaults = []
        tests_args_set_all_defaults = []
        tests_result_load_file = []
        tests_result_load_file_in_dir = []

        def setUp(self):
            self.tests_

# Generated at 2022-06-13 10:06:36.083764
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    source_path = path.join(os.getcwd(), "action_plugins")
    action_path = path.join(source_path, "include_vars")
    sys.path.insert(0, action_path)
    from include_vars import ActionModule

    obj_task = namedtuple("TASK", "args")
    obj_task._role = None
    obj_task._ds = None
    obj_task.args = {'dir': '/etc/ansible/modules/utilities/include_vars/vars',
                     'depth': None, 'files_matching': None, 'ignore_files': None, 'extensions': None,
                     'ignore_unknown_extensions': False, 'name': None, 'hash_behaviour': None}
    obj_tmpl_data = {"foo": "bar"}


# Generated at 2022-06-13 10:06:47.872259
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test for empty set
    set_task_vars = set()
    # Test for an empty string
    set_task_tmp = ""
    # Test for an empty list
    set_task_args = list()
    # Test for empty dictionary
    set_loader_basedir = dict()
    # Test for uninitialized variable
    set_loader_basedir1 = None
    # Test for valid set of arguments
    set_valid_file_extensions = ["yaml", "yml", "json"]
    set_valid_dir_arguments = ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    set_valid_file_arguments = ['file', '_raw_params']
    set_valid_all = ['name', 'hash_behaviour']
   

# Generated at 2022-06-13 10:06:49.823024
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(ActionModule("_task","_connection", "_play_context", "_loader","_templar").__class__.__name__ == "ActionModule")


# Generated at 2022-06-13 10:07:13.289079
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:07:22.584524
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    contains_results = False
    contains_failed = False
    contains_message = False

    test_module = ActionModule()
    result = test_module.run()

    if 'ansible_facts' in result:
        contains_results = True
    if 'failed' in result:
        contains_failed = True
    if 'message' in result:
        contains_message = True

    return contains_results and contains_failed and contains_message



# Generated at 2022-06-13 10:07:24.784902
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule(None, None)
    assert actionmodule is not None

# Generated at 2022-06-13 10:07:25.738558
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule((), {})

# Generated at 2022-06-13 10:07:26.678714
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:07:28.994320
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        assert True
        print("test_ActionModule: PASS")
    except AssertionError:
        print("test_ActionModule: FAIL")


# Generated at 2022-06-13 10:07:34.084765
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule(None, None)
    assert actionModule.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']
    assert actionModule.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    assert actionModule.VALID_FILE_ARGUMENTS == ['file', '_raw_params']
    assert actionModule.VALID_ALL == ['name', 'hash_behaviour']


# Generated at 2022-06-13 10:07:44.879920
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test for if dirs and files exist
    ActionModule._set_args = lambda self: None
    assert ActionModule.run.__doc__ == ' Load yml files recursively from a directory.\n'

    # test for if dirs is 0 and files is 1
    assert ActionModule._set_args.__doc__ == ' Set instance variables based on the arguments that were passed '

    # test for if dirs is 1 and files is 0
    assert ActionModule._set_dir_defaults.__doc__ == None

    # test for if dirs and files are 0
    ActionModule._set_dir_defaults = lambda self: None
    assert ActionModule._set_dir_defaults.__doc__ == None

    # test for if dirs and files are 1
    ActionModule._traverse_dir_depth = lambda self: None

# Generated at 2022-06-13 10:07:46.345128
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Calling test_ActionModule")
    assert ActionModule("action") is not None

# Generated at 2022-06-13 10:07:50.005869
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule(task='', connection='', play_context='', loader='', templar='', shared_loader_obj='')
    assert actionModule != None
    assert isinstance(actionModule, ActionModule)


# Generated at 2022-06-13 10:08:37.039395
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Unit tests for class ActionModule
    """
    # TODO: Write tests

# Generated at 2022-06-13 10:08:41.371526
# Unit test for constructor of class ActionModule
def test_ActionModule():
    obj = ActionModule(None, None, None)
    obj._task = None
    obj._set_dir_defaults()
    obj._set_args()
    obj.run(None, None)

# Generated at 2022-06-13 10:08:54.738493
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    context = dict()
    context['task'] = dict()
    context['task']['args'] = dict()
    context['task']['args']['dir'] = '/home/user/.ansible/roles/role_to_run/vars'
    context['task']['_ds'] = dict()
    context['task']['_ds']['_data_source'] = './tests/unit/mock_runner/include_vars/mock_tasks.yml'

    context['_task'] = dict()
    context['_task']['args'] = dict()
    context['_task']['args']['dir'] = '/home/user/.ansible/roles/role_to_run/vars'
    context['_task']['_ds'] = dict()

# Generated at 2022-06-13 10:08:55.534920
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:08:56.120556
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:09:00.269500
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Unit test of class ActionModule
    """
    import ansible.constants as C
    # test constructor of class ActionModule
    _task = ansible.playbook.task.Task()
    _loader = ansible.parsing.dataloader.DataLoader()
    _variable_manager = ansible.vars.manager.VariableManager()
    test_obj = ansible.plugins.action.ActionModule(_task, _loader, _variable_manager)
    assert test_obj is not None

# Generated at 2022-06-13 10:09:01.266021
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()


# Generated at 2022-06-13 10:09:12.981068
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    task = Task()
    task.action = 'include_vars'

    def _load_name(self, attr):
        return 'some_name'
    setattr(task, '_load_name', _load_name)
    task.args = {'dir': '/test/dir', 'depth': 0, 'name': 'some_name'}
    task._role = RoleInclude()
    task._role._role_path = '/dummy_role_path'


# Generated at 2022-06-13 10:09:14.577406
# Unit test for constructor of class ActionModule
def test_ActionModule():
    theActionModule = ActionModule()
    assert theActionModule is not None


# Generated at 2022-06-13 10:09:19.201534
# Unit test for constructor of class ActionModule
def test_ActionModule():
    path = '~/ansible/ansible/plugins/action/'
    action_module = ActionModule(play_context=2, task=1, connection=2,
                                 loader=2, templar=2, shared_loader_obj=2)
    assert action_module != None
    assert action_module.run(tmp='tmp', task_vars='taskvars') != None


# Generated at 2022-06-13 10:10:58.880665
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.strategy import ActionModule
    #import ansible.playbook.play_context
    #import ansible.executor.task_result


# Generated at 2022-06-13 10:11:07.390777
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # init ActionModule class
    action_module = ActionModule()
    # init task dict
    task_dict = {
        'args': {},
        '_role': None,
        '_ds': None,
        'action': 'test_module',
        'delegate_to': 'localhost',
        '_low_level_subelement_access': True,
        '_uses_shell': False,
        '_raw_params': '',
        '_tmpdir': '/tmp'
    }
    # init ActionBase class
    super_action_base = ActionBase()
    # init super class of ActionBase
    super_action_base._play_context = {
        'become': False,
        'become_method': 'sudo',
        'become_user': 'root'
    }
    action_module

# Generated at 2022-06-13 10:11:10.442212
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(ActionModule._set_dir_defaults())
    assert(ActionModule._set_args())
    assert(ActionModule._set_root_dir())
    assert(ActionModule._traverse_dir_depth())
    assert(ActionModule._ignore_file('filename'))
    assert(ActionModule._is_valid_file_ext('filename'))
    assert(ActionModule._load_files('filename'))
    assert(ActionModule._load_files_in_dir('root_dir','var_files'))

# Generated at 2022-06-13 10:11:16.841271
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict()
    source_dir = '/home/vagrant/roles/foo/vars/'
    source_file = 'bar.yml'
    depth = 1
    valid_extensions = ['yaml', 'yml']
    ignore_unknown_extensions = True

    test_action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    test_action_module._set_args()
    test_action_module._set_dir_defaults()
    test_action_module._set_root_dir()
    test_action_module.source_dir = source_dir
    test_action_module.source_file = source_file
    test_action_module.depth = depth
    test

# Generated at 2022-06-13 10:11:18.894221
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: Test the run method of class ActionModule
    pass

# Generated at 2022-06-13 10:11:19.548336
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 10:11:23.178177
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    run_all = ActionModule(dict(), dict())
    assert run_all.run()['failed'] == True
    assert run_all.run()['message'] == 'You are mixing file only and dir only arguments, these are incompatible'
    assert run_all.run(task_vars=dict(dir='this should fail'))['ansible_facts'] == {}

# Generated at 2022-06-13 10:11:24.376514
# Unit test for constructor of class ActionModule
def test_ActionModule():
    b = ActionModule()
    assert b is not None


# Generated at 2022-06-13 10:11:31.452664
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Testing class ActionModule, method run")
    import ansible.playbook.play_context as PC
    import ansible.playbook.task_include as TI
    import ansible.utils.template as T
    import ansible.vars.hostvars as HV
    import ansible.vars.unsafe_proxy as UP
    from ansible.utils.color import stringc
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import action_loader

    class Base(object):

        pass
    setattr(Base, '_play_context', PC.PlayContext())

# Generated at 2022-06-13 10:11:38.280888
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task

    assert issubclass(ActionModule, ansible.plugins.action.ActionModule)

    # Test for constructor
    assert isinstance(ActionModule, object)

    # Test for TRANFER_FILES type
    assert ActionModule.TRANSFERS_FILES == False

    # Test for VALID_FILE_EXTENSIONS type
    assert isinstance(ActionModule.VALID_FILE_EXTENSIONS, list)

    # Test for VALID_DIR_ARGUMENTS type
    assert isinstance(ActionModule.VALID_DIR_ARGUMENTS, list)

    # Test for VALID_FILE_ARGUMENTS type
    assert isinstance(ActionModule.VALID_FILE_ARGUMENTS, list)

    # Test for VALID_ALL type
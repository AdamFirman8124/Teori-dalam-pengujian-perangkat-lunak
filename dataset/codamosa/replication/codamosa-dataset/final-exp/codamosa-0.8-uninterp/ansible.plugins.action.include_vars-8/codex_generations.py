

# Generated at 2022-06-13 10:06:07.138704
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.vars import combine_vars, combine_vars_overwrite
    action = ActionModule()
    #Unit test 1:
    # test source_dir = ''
    task_vars = dict()
    task_vars['source_dir'] = ''
    results = action.run(tmp=None, task_vars=task_vars)
    assert results['ansible_facts'] == dict()
    #Unit test 2:
    # test source_file = None
    task_vars = dict()
    task_vars['source_file'] = None
    results = action.run(tmp=None, task_vars=task_vars)
    assert results['ansible_facts'] == dict()
    #Unit test 3:
    # test source_dir = 'data'
    task_vars

# Generated at 2022-06-13 10:06:19.993646
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_source_dir = '/tmp'
    test_depth = 0
    test_files_matching = ''
    test_ignore_files = '_test_ignore.yaml'
    test_ignore_unknown_extensions = True
    test_valid_extensions = ['yaml', 'yml', 'json']
    test_hash_behaviour = None
    test_return_results_as_name = 'test_name'

    # create _task object
    test_run_module = ActionModule()
    test_run_module._task = Mock()

# Generated at 2022-06-13 10:06:31.147194
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a fake task
    task = FakeTask()
    task.args = {'dir': '/tmp/', 'depth': 1}

    # Create a fake module action
    action = ActionModule(task, dict(), dict())

    # Unit test for method _set_dir_defaults()
    action._set_dir_defaults()
    assert action.depth == 1
    assert action.matcher == None
    assert action.ignore_files == list()

    # Unit test for method _set_root_dir()
    action._set_root_dir()
    assert action.source_dir == '/tmp/'

    # Unit test for method _traverse_dir_depth()
    action.depth = 0
    action.source_dir = 'test/test_action_module'
    sorted_walk = list(walk(action.source_dir))

# Generated at 2022-06-13 10:06:39.357341
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class FakeTask():
        class FakeDS():
            pass
        _ds = FakeDS()
    task = FakeTask()
    task._ds._data_source = 'https://github.com/ansible/ansible-modules-core/blob/devel/system/ping.py'

    task._ds._data_source = 'https://github.com/ansible/ansible-modules-core/blob/devel/system/ping.py'
    task_vars = dict()
    a = ActionModule()
    a._task = task
    a._tqm = None
    a.run(task_vars=task_vars)

# Generated at 2022-06-13 10:06:50.673880
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task

    def create_playbook():
        pb = Playbook()
        p = Play.load({}, pb, DataLoader())
        pb._entries.append(p)
        r = Role()
        r._role_name = "test"
        r._role_path = "/some/path"
        p._entries.append(r)
        t = Task()
        t._uuid = "testuuid"
        t._role = r
        r._entries.append(t)
        b = Block()
        b._parent = t
        t._entries.append

# Generated at 2022-06-13 10:06:59.088554
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    host = "127.0.0.1"
    args = {'hosts':host, 'user':'test', 'password':'test'}
    log_path="./ansible_test.log"
    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)
    results_callback = ResultCallback()
    tqm = TaskQueueManager(
        inventory=InventoryManager(loader=loader, sources=['127.0.0.1']),
        variable_manager=variable_manager,
        loader=loader,
        stdout_callback=results_callback,
        passwords=dict(vault_pass='secret'),
    )
    playbook_path = './test_ansible/test_playbook.yml'

# Generated at 2022-06-13 10:07:03.989579
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()
    assert ActionModule().VALID_DIR_ARGUMENTS
    assert ActionModule().VALID_FILE_ARGUMENTS
    assert ActionModule().VALID_ALL
    assert ActionModule.TRANSFERS_FILES == False


# Generated at 2022-06-13 10:07:11.603662
# Unit test for constructor of class ActionModule
def test_ActionModule():
    Task = namedtuple('Task', ['args'])
    task = Task(args={'file': 'roles/provision/vars/main.yml'})
    action_module = ActionModule(task, dict(vars=dict(key1='value1', key2='value2')))
    assert action_module.source_file == 'roles/provision/vars/main.yml'


if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:07:13.838450
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print('ActionModule is a class for constructing the Action Module')

# Generated at 2022-06-13 10:07:15.996205
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule().run(tmp='', task_vars='')

# Generated at 2022-06-13 10:07:51.197554
# Unit test for constructor of class ActionModule
def test_ActionModule():
    act = ActionModule(None)
    assert act.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']
    assert act.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    assert act.VALID_FILE_ARGUMENTS == ['file', '_raw_params']
    assert act.VALID_ALL == ['name', 'hash_behaviour']

# Generated at 2022-06-13 10:07:51.814221
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:08:00.293436
# Unit test for constructor of class ActionModule
def test_ActionModule():
    testActionModule = new.instance(ActionModule)
    if testActionModule.TRANSFERS_FILES == False:
        assert True
    else:
        assert False
    if testActionModule.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']:
        assert True
    else:
        assert False
    if testActionModule.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']:
        assert True
    else:
        assert False
    if testActionModule.VALID_FILE_ARGUMENTS == ['file', '_raw_params']:
        assert True
    else:
        assert False

# Generated at 2022-06-13 10:08:01.304529
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:08:09.408557
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    (tmp, action_module) = prepare_module_for_test()

    results = action_module.run(tmp=tmp, task_vars={})
    assert results['ansible_included_var_files'] == ['/tmp/vars/main.yml'], 'Included var file list is wrong'
    assert results['ansible_facts']['var1'] == 'ansible', 'Included var value is wrong'
    assert results['_ansible_no_log'] is True, '_ansible_no_log is wrong'



# Generated at 2022-06-13 10:08:18.678169
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # setup
    import imp
    fake_action_module = imp.load_source('fake_action_module', 'action_plugins/fake_action_module.py')
    a = ActionModule()
    a.VALID_DIR_ARGUMENTS = fake_action_module.ActionModule.VALID_DIR_ARGUMENTS
    a.VALID_FILE_ARGUMENTS = fake_action_module.ActionModule.VALID_FILE_ARGUMENTS
    a.VALID_ALL = fake_action_module.ActionModule.VALID_ALL
    import ansible.executor.task_result as result

# Generated at 2022-06-13 10:08:27.100727
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for method run of class ActionModule.
    """
    # _set_dir_defaults
    assert ActionModule()._set_dir_defaults() is None
    # _set_args
    assert ActionModule()._set_args() is None
    # run
    assert ActionModule().run() == {'ansible_facts': {}, '_ansible_no_log': True, 'ansible_included_var_files': [], 'changed': False}

# Generated at 2022-06-13 10:08:27.722142
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 10:08:28.314929
# Unit test for constructor of class ActionModule
def test_ActionModule():
    x = ActionModule()

# Generated at 2022-06-13 10:08:37.700016
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Assumptions: the include_vars module is imported, and the class ActionModule is instantiated.
    # The method run is called with the following parameters
    tmp = None
    task_vars = {'dir': 'dir'}
    # The method _set_dir_defaults is called within run with no parameters
    # The method _set_args is called within run with no parameters
    # The method run is called with the following parameters
    tmp = None
    task_vars = {'dir': 'dir'}
    # The method _set_dir_defaults is called within run with no parameters
    # The method _set_args is called within run with no parameters
    # The class ActionModule is instantiated.
    # The method _set_dir_defaults is called with no parameters
    # The method _set_args is called with no

# Generated at 2022-06-13 10:09:47.540594
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class TestActionModule(object):
        def __init__(self, args):
            self.args = args
    class TestTask(object):
        def __init__(self, args):
            self.args = args
    class TestRole(object):
        def __init__(self, path):
            self._role_path = path
    class TestDataSource(object):
        def __init__(self, data_source):
            self._data_source = data_source
    class TestLoader(object):
        def _get_file_contents(self, path):
            if path == 'valid_path_1':
                return 'contents', False
            elif path == 'valid_path_2':
                return 'contents', False
            else:
                return '', False

# Generated at 2022-06-13 10:09:48.180938
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:09:59.316602
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext

    context = PlayContext()
    context.CLIARGS = {}
    context.CLIARGS['syntax'] = False
    context.CLIARGS['module_path'] = ''
    context.CLIARGS['forks'] = 5

    test_am = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=context,
        loader=None,
        templar=None,
        shared_loader_obj=None)

    assert isinstance(test_am, ActionModule)
    # this is kind of silly but we need to set this up to make sure we don't
    # hit the code paths in the module which would cause the unit test to
    # fail due to the try..except.

# Generated at 2022-06-13 10:10:01.268651
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test whether the class ActionModule is defined
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module


# Generated at 2022-06-13 10:10:01.961696
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO implement test
    pass

# Generated at 2022-06-13 10:10:07.102260
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.parsing import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # PlayContext, Constructor of PlayContext initializes with play, Options and connection,
    # we have to provide these arguments
    # connection is initialized with PlayContext, it is initialized with play_context,
    # and other arguments

    # Constructor of DataLoader requires path option which we have to provide
    loader = DataLoader()
    # Constructor of VariableManager requires play_context argument
    # Task also requires play_context argument

    t = Task()
    play_context = PlayContext(loader=loader)
    template = Templar(loader, play_context)
    variable_manager = VariableManager()

# Generated at 2022-06-13 10:10:16.652606
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from .mock import MagicMock
    from .mock import patch

    # setup
    m_module = MagicMock()

    m_module.params = {
        'file': 'main.yml',
        '_raw_params': 'main.yml',
        'name': 'f',
        'hash_behaviour': 'replace',
    }
    m_module.run.return_value = {
        'failed': False,
        'message': '',
        'ansible_facts': {
            'a': 1,
        },
    }

    # unit under test
    m_action_module = ActionModule(m_module)

    # mock
    m_find_needle = patch.object(m_action_module, '_find_needle', return_value='main.yml')
    m

# Generated at 2022-06-13 10:10:21.404765
# Unit test for constructor of class ActionModule
def test_ActionModule():
    obj = ActionModule()
    try:
        b = obj.run({}, {})
        assert (b.get('failed') is True)
    except AssertionError as e:
        print("{}Expected failed but it didn't get failed".format(e))
        raise
    except Exception as e:
        print("{}Unexpected error".format(e))
        raise


# Generated at 2022-06-13 10:10:31.502864
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:10:32.112711
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:13:16.762709
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create mock objects for ActionModule class
    # create mock objects for ActionBase class
    ActionBase._execute_module = lambda x, y, z, w: (True, {}, {})
    ActionBase._add_hook_validate_file = lambda x, y: None
    ActionBase._add_hook_cleanup_file = lambda x, y: None
    ActionBase._flush_lookup_plugins = lambda : None

    # create mock objects for Task class

# Generated at 2022-06-13 10:13:28.372798
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    path_current_file = path.realpath(__file__)
    path_current_dir = path.dirname(path_current_file)
    path_playbook = path.join(path_current_dir, '../../../../')
    path_role = path.join(path_current_dir, '../../../../lib/ansible/modules/utilities/logic/yaml/vars/')

    # Init
    var_loader = MockVarLoader()
    role = MockTestRole()
    role.set_role_path(path_role)

    action_module = ActionModule(task=MockTestTask(role=role), connection=MockTestConnection(), play_context=MockTestPlayContext(), loader=var_loader, templar=var_loader, shared_loader_obj=None)
    action_module

# Generated at 2022-06-13 10:13:34.046452
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action.VALID_FILE_EXTENSIONS == ['yaml', 'yml', 'json']
    assert action.VALID_DIR_ARGUMENTS == ['dir', 'depth', 'files_matching', 'ignore_files', 'extensions', 'ignore_unknown_extensions']
    assert action.VALID_FILE_ARGUMENTS == ['file', '_raw_params']
    assert action.VALID_ALL == ['name', 'hash_behaviour']


# Generated at 2022-06-13 10:13:40.882088
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup test setup
    set_module_args({
        'dir': '/tmp/test/data',
        'include': '*.yml',
        'ignore_files': '*.old',
        'depth': 3,
        'name': 'test'
    })
    action = ActionModule()
    action._set_args()
    action._set_dir_defaults()

    # Setup test results

# Generated at 2022-06-13 10:13:54.707411
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile
    import shutil
    import json
    import os

    validate_expected_results = {
        'ansible_included_var_files': [],
        'ansible_facts': {
            'test': {
                'test2': {
                    'test3': 'test4'
                }
            }
        },
        'failed': True,
        'msg': 'test/test.json must be stored as a dictionary/hash'
    }

    # --------------------------------------------------------------------------------------------------
    # Test multiple files with a root directory
    # --------------------------------------------------------------------------------------------------
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_sub_dir = tempfile.mkdtemp(prefix=temp_dir)
        temp_file = tempfile.mkstemp(suffix="_test.json", dir=temp_sub_dir)

# Generated at 2022-06-13 10:14:04.635217
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import mock

    fake_filename = 'fake'
    fake_contents = 'fake_contents'
    fake_sub_role = mock.Mock()
    fake_sub_role._role_path = 'fake/fake'

    fake_ds = mock.Mock()
    fake_ds._data_source = 'fake/source/fake.yml'

    fake_task = mock.Mock()
    fake_task._role = fake_sub_role
    fake_task._ds = fake_ds
    fake_task.args = dict(source_file=fake_filename)
    fake_task.args['_raw_params'] = fake_filename

    fake_file_loader = mock.Mock()

    fake_module = mock.Mock()
    fake_module._loader = fake_file_loader
    fake_module._

# Generated at 2022-06-13 10:14:14.108090
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    import ansible.constants as C
    import ansible.plugins.loader as loader
    import ansible.plugins.action.include_vars as include_vars_action
    import sys
    import os

    class Options(object):
        _connection = None
        _shell = None
        become = False
        become_method = None
        become_user = None
        become_ask_pass = False
        check = False
        diff = False
        extra_vars = list()
        flush_cache = None
        force_handlers = False
        forks = None
        inventory = None
        listhosts = None
        module_

# Generated at 2022-06-13 10:14:14.854197
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass  # TODO

# Generated at 2022-06-13 10:14:16.034893
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    return action_module

# Generated at 2022-06-13 10:14:27.817067
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils import varMatches

    # Make sure that in the case where there are no files the result is the empty dict
    module = ActionModule()
    result = module.run(task_vars={'role_path': '/path/to/role'})
    assert result['ansible_facts'] == dict()
    assert not result.get('failed', False)

    # Make sure that in the case where there are no files the result is the empty dict
    module = ActionModule()
    module._task = {'args': {'dir': 'test/test_data/test_include_vars_dir'}}
    result = module.run(task_vars={'role_path': '/path/to/role'})
    assert result.get('ansible_facts', dict()).get('a') == 3
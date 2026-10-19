

# Generated at 2022-06-13 11:19:00.645117
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    task = dict(args=dict(use='auto', state='installed'))
    task_vars = dict(ansible_facts=dict(pkg_mgr='yum', redhat_yum=True), ansible_pkg_mgr='yum')
    result = module.run(None, task_vars)
    assert not result['failed']
    assert result['ansible_facts']['pkg_mgr'] == 'yum'
    assert result['task']['args']['pkg'] == 'auto'
    assert result['task']['args']['state'] == 'installed'

# Generated at 2022-06-13 11:19:11.502407
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 11:19:22.045915
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import pytest

    TEST_VARS = {
        'ansible_pkg_mgr': 'yum',
        'hostvars': {'host1': {'ansible_facts': {'pkg_mgr': 'dnf'}}},
        'ansible_facts': {'pkg_mgr': 'yum3'},
    }

    def _get_action_module_mock_object(module_name, action_plugin_name, task_vars=TEST_VARS):
        import ansible
        from ansible.playbook.task import Task

        action_plugin_args = dict(
            _uses_shell=False,
            _raw_params="",
            _task_vars=task_vars,
            _templar=None,
        )

        action_plugin_path

# Generated at 2022-06-13 11:19:31.810607
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup dependencies
    module = 'ansible.legacy.yum'
    loader, path, entities = loader_factory.gen_modules_from_class(module, ActionModule)
    sys.modules[module] = loader.load_module(module)

    tmp = None
    task_vars = dict(
        ansible_facts=dict(
            pkg_mgr='auto'
        )
    )
    my_action = ActionModule(
        task=dict(
            args=dict(
                use='auto'
            )
        )
    )
    result = my_action.run(tmp, task_vars)

    assert result.get('failed') == True

# Generated at 2022-06-13 11:19:36.274955
# Unit test for constructor of class ActionModule
def test_ActionModule():
    result = {}
    args = dict(yum='yum', yum_version=1)
    result.update(args)
    module_args = dict(yum='yum', yum_version=1)
    result.update(module_args)
    task_vars = dict(yum='yum', yum_version=1)
    result.update(task_vars)
    ActionModule(args, module_args, task_vars)

# Generated at 2022-06-13 11:19:37.520463
# Unit test for constructor of class ActionModule
def test_ActionModule():

    am = ActionModule(None, {}, {})
    assert am.TRANSFERS_FILES is False

# Generated at 2022-06-13 11:19:38.685153
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert VALID_BACKENDS == frozenset(('yum', 'yum4', 'dnf'))

# Generated at 2022-06-13 11:19:42.004313
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action

    # Create yum action plugin object
    obj = ansible.plugins.action.ActionModule(cls=dict(), task=dict(), connection=dict(), play_context=dict(),
                                              loader=dict(), templar=dict(), shared_loader_obj=dict())

    assert isinstance(obj, ActionModule)

# Generated at 2022-06-13 11:19:44.190240
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module

# Generated at 2022-06-13 11:19:47.990991
# Unit test for constructor of class ActionModule
def test_ActionModule():
    p = ActionModule(task={"args": {"name": "httpd"}}, connection=None, play_context=None, loader=None, templar=None,
                     shared_loader_obj=None)
    assert True


# Generated at 2022-06-13 11:19:58.233591
# Unit test for constructor of class ActionModule
def test_ActionModule():  # pylint: disable=redefined-outer-name
    module = ActionModule(dict(), dict())
    assert module._supports_check_mode
    assert module._supports_async



# Generated at 2022-06-13 11:20:09.432887
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_result import TaskResult
    from ansible.executor.process.result import ResultProcess
    from ansible.plugins.action.yum import ActionModule
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.constants import DEF_REMOTE_TMP

    class FakeDisplay:
        class FakeColor:
            def __getattr__(self, name):
                pass

        class FakeDeprecation:
            def deprecated(self, key, version, alt=None):
                pass

            def removed(self, key, version, removal_version):
                pass

            def generic(self, msg, version, removable_version=None, error=False, id=None):
                pass


# Generated at 2022-06-13 11:20:12.978005
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule(task=dict(action=dict(module_name='yum'), args=dict(use_backend='yum4')))
    assert mod.run() == {'ansible_facts': {'pkg_mgr': 'yum4'}, 'changed': False}

# Generated at 2022-06-13 11:20:13.514875
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 11:20:14.469699
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)

# Generated at 2022-06-13 11:20:24.310002
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common._collections_compat import Mock
    from ansible.plugins.loader import action_loader

    task_vars = dict(ansible_facts=dict(pkg_mgr='yum'))

    mock_task = Mock()
    mock_task._ds = dict(vars=task_vars)
    mock_task.args = dict(use='yum')
    mock_task.async_val = 10
    mock_task.delegate_to = None
    mock_task.delegate_facts = True

    mock_connection = Mock()
    mock_connection._shell = Mock()
    mock_connection._shell.tmpdir = 'test'

    mock_loader = Mock()
    mock_loader.module_loader = Mock()

# Generated at 2022-06-13 11:20:34.070930
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 11:20:42.429911
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import os
    import tempfile
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch

    temp_file = tempfile.mkstemp()
    temp_dir = tempfile.mkdtemp()

    with patch.object(ActionBase, '_execute_module') as mock_execute_module, \
         patch.object(ActionBase, '_execute_module_with_delay'), \
         patch.object(ActionBase, '_execute_module_raise_on_path_not_found'), \
         patch.object(ActionBase, '_execute_module_with_modlib'), \
         patch.object(ActionBase, '_load_params'):
        mock_execute_module.return_value = {'ansible_facts': {'pkg_mgr': 'yum'}}
       

# Generated at 2022-06-13 11:20:53.299720
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import sys

    if sys.version_info.major < 3:
        raise Exception("Must run unit tests using python3")

    # Setup mock inputs
    tmp = None
    from ansible.plugins.loader import add_all_plugin_dirs
    # add plugins/action directory to module_loader path
    add_all_plugin_dirs([os.path.dirname(os.path.abspath(__file__))])

    test_hostvars = {
        "localhost": {
            "ansible_facts": {
                "pkg_mgr": "dnf"
            }
        }
    }
    test_task_vars = {
        "hostvars": test_hostvars
    }
    test_args = {
        "use_backend": "yum",
    }



# Generated at 2022-06-13 11:20:56.308367
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Constructor for ActionModule class
    '''
    action_mod = ActionModule()
    assert isinstance(action_mod, ActionModule)

# Generated at 2022-06-13 11:21:06.649005
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action is not None
    assert action._supports_check_mode is True
    assert action._supports_async is True

# Generated at 2022-06-13 11:21:15.326676
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test for method run of class ActionModule'''

    # Generate a mock task object and a mock shared loader object
    _task = MockTask()
    _shared_loader_obj = MockSharedLoaderObj()

    # Generate a mock connection object
    _connection = MockConnection()

    # Create a new ActionModule instance to test
    _action = ActionModule(_task=_task, connection=_connection, _loader=_shared_loader_obj._loader,
        _templar=_shared_loader_obj._templar, _shared_loader_obj=_shared_loader_obj)

    # Test the run method
    _action.run()
    assert _action._task.args['use_backend'] == "yum"
    _action._task.args['use_backend'] = 'dnf'
    _action

# Generated at 2022-06-13 11:21:16.193855
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # module = mymodule.MyClass()
    pass

# Generated at 2022-06-13 11:21:23.194829
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.compat.tests.mock import patch, Mock
    from ansible.compat.tests.mock import MagicMock

    templar = MagicMock()
    ansible_facts = {'pkg_mgr': 'yum'}
    facts = {'ansible_facts': ansible_facts}
    task_vars = dict()
    task_vars['hostvars'] = {'localhost': {'ansible_facts': ansible_facts}}
    task_vars['ansible_facts'] = ansible_facts

    templar.template = Mock(return_value = 'yum')
    mock_shared_loader_obj = MagicMock()
    mock_shared_loader_obj.module_loader.has_plugin = MagicMock(return_value = True)


# Generated at 2022-06-13 11:21:28.055811
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.errors import AnsibleParserError
    from ansible.parsing.dataloader import DataLoader

    class FakeTask(object):
        def __init__(self, args=None, delegate_to=None, delegate_facts=None, async_val=None):
            self.args = args or {}
            self.delegate_to = delegate_to
            self.delegate_facts = delegate_facts
            self.async_val = async_val

    class FakeTemplar(object):
        def __init__(self):
            self.filters = {}

        def add_plugin_filter(self, filter_name, filter_func):
            self.filters[filter_name] = filter_func

        def template(self, string):
            return self.filters['to_json'](string)

   

# Generated at 2022-06-13 11:21:33.132881
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule()
    
    assert mod is not None
    assert mod.__dict__.get('_supports_check_mode', None) == True
    assert mod.__dict__.get('_supports_async', None) == True
    

# Generated at 2022-06-13 11:21:33.908086
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  pass

# Generated at 2022-06-13 11:21:37.438838
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module._task.args.get('use', module._task.args.get('use_backend', 'auto')) == 'auto'

# Generated at 2022-06-13 11:21:46.020831
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    display = Display()
    display.verbosity = 4
    use_backend = 'auto'
    module = 'auto'
    test_ansible_facts = {'pkg_mgr': 'yum'}
    module_name = 'ansible_yum_module'

    task_args = {'use_backend': use_backend}
    task_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    task_vars = {'ansible_facts': test_ansible_facts}

    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action.use_cache = False
    action.connection = None
    action.display = display

# Generated at 2022-06-13 11:21:53.763125
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  # Testing with a simple task and args
  class display_mock:
    def __init__(self, display_mock):
      display_mock.vvvv = lambda x: {'failed': False, 'msg': "ansible.legacy.auto"}
  
  class _task_mock:
    def __init__(self, _task_mock):
      _task_mock.args = {'use_backend': 'auto'}
      _task_mock.delegate_to = None
      _task_mock.delegate_facts = None
      _task_mock.async_val = False
  
  def _remove_tmp_path_mock(self, _connection_mock):
    pass

# Testing with an installed package

# Generated at 2022-06-13 11:22:08.217299
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    assert True

# Generated at 2022-06-13 11:22:09.595215
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(ActionModule(None, {}, None, None)._task.action == 'yum')


# Generated at 2022-06-13 11:22:18.839940
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    ActionModule unit test
    '''
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.action import ActionBase
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.utils.display import Display

# Generated at 2022-06-13 11:22:27.317871
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import pytest

    from ansible.module_utils.six.moves import StringIO

    def test_ActionModule_run_method(self, module, function, args, msg):
        # Capture the sys.stdout
        system_stdout = sys.stdout
        sys.stdout = StringIO()

        try:
            # Attempt to execute tasks and expect results
            self._task.args = {'use': module, 'function': function, 'args': args, 'msg': msg}
            result = self.run(tmp=None, task_vars=None)
            self.assertTrue(result['failed'])
            self.assertEqual(result['msg'], msg)
        finally:
            # Restore sys.stdout
            sys.stdout = system_stdout

    # create an instance of the Ansible

# Generated at 2022-06-13 11:22:28.674447
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module_object = ActionModule()
    assert action_module_object

# Generated at 2022-06-13 11:22:30.174021
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Pass, but only because this method has not been implemented yet."""
    pass

# Generated at 2022-06-13 11:22:36.846739
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Test case: yum modules without yum_repositories, yum_vars, or "name" key
    '''
    module_args = dict(
        state="present",
        name="python-devel",
    )

    module = 'ansible.legacy.yum'

    task = 'TASK [test-yum : debug] *************************************************'
    display = 'TASK [test-yum : debug] *************************************************\n'
    action = ActionModule(task, module_args, display=display)

    # addition of key "msg" indicates a failure
    assert "msg" not in action.run()



# Generated at 2022-06-13 11:22:39.211399
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module is not None
    assert module._supports_check_mode is True
    assert module._supports_async is True

# Generated at 2022-06-13 11:22:49.635904
# Unit test for constructor of class ActionModule
def test_ActionModule():

    from ansible.context import CLIContext

    # Constructor Test
    obj = ActionModule(task=None, connection=None, play_context=CLIContext(), loader=None, templar=None,
                       shared_loader_obj=None)

    obj._templar = "templar"
    obj._shared_loader_obj = "loader"
    obj._supports_check_mode = True
    obj._supports_async = True
    assert obj._connection is None
    assert obj.Templar == "templar"
    assert obj.loader == "loader"
    assert obj.supports_check_mode is True
    assert obj.supports_async is True

# Generated at 2022-06-13 11:22:50.399970
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 11:23:24.631222
# Unit test for constructor of class ActionModule
def test_ActionModule():
    x = ActionModule(
        task={'args': {'use': 'yum4', 'name': 'my_package'}},
        connection={'_shell': {'tmpdir': '/tmp/path'}},
        play_context={'check_mode': True, 'should_continue': True},
        loader=None,
        templar=None,
        shared_loader_obj=None)

    assert x.TRANSFERS_FILES is False
    assert x._supports_check_mode is True
    assert x._supports_async is True
    assert x._task.args['use'] == 'yum4'
    assert x._connection._shell.tmpdir == '/tmp/path'
    assert x._play_context.__dict__ == {'check_mode': True, 'should_continue': True}




# Generated at 2022-06-13 11:23:38.106915
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os
    import contextlib
    import tempfile
    from ansible.module_utils.six import PY2
    from ansible.module_utils.six.moves import StringIO

    # Method run can be tested via the following steps.
    # 1. Save the current stdout and stderr.
    # 2. Temporarily redirect stdout and stderr.
    # 3. Prepare arguments for run method.
    # 4. Call run method with the prepared arguments.
    # 5. Get the results from the stdout and stderr.
    # 6. Restore the stdout and stderr.

    # prepare arguments
    class C(object):
        pass
    class A(object):
        pass
    class B(object):
        pass

# Generated at 2022-06-13 11:23:42.498193
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Constructor for class ActionModule
    '''
    module = ActionModule(
        task=dict(action=dict(module_name='yum', module_args=dict(name='httpd'))),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None)

    assert module is not None

# Generated at 2022-06-13 11:23:43.291572
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 11:23:44.050639
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()
    assert a

# Generated at 2022-06-13 11:23:44.965348
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule({}, {}, {}, {})
    assert action_module

# Generated at 2022-06-13 11:23:48.708075
# Unit test for constructor of class ActionModule
def test_ActionModule():
    with pytest.raises(AnsibleActionFail):
        action_module = ActionModule(load_plugins=False)
        action_module._task.args = dict(use='yum',use_backend='yum4')
        result = action_module.run(tmp=None, task_vars=None)
        assert result.get('failed')

# Generated at 2022-06-13 11:23:59.368984
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import combine_vars

    from ansible.utils.display import Display
    from ansible.plugins.strategy import StrategyBase

    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources=['localhost,'])

    host = Host('localhost')

# Generated at 2022-06-13 11:24:05.963835
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    display.debug("***** Test case: Test ActionModule.run() method *****")

    # Test case #1:
    # Test calling the action module correctly, when use is specified.
    # The expected result is:
    # the method returns result for dnf backend module
    display.display("Test case #1")
    action_module = ActionModule()
    action_module._connection = None
    action_module._task = None
    action_module._loader = None
    action_module._templar = None
    action_module._shared_loader_obj = None
    result = action_module.run(None, {}, {'use': 'dnf'})
    assert(result['failed'] == False)


# Generated at 2022-06-13 11:24:08.222084
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''

    assert isinstance(ActionModule(), ActionBase)

# Generated at 2022-06-13 11:25:17.096522
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.facts.system.pkg_mgr import get_distribution

    def mock_execute_module(module_name=None, module_args=None, task_vars=None, wrap_async=None):
        assert module_name == 'ansible.legacy.dnf'
        assert module_args == {'name': 'some_package', 'use': 'some'}
        assert task_vars == "some_vars"
        assert wrap_async == "some_async_val"
        return {'failed': False, 'rc': 0, 'changed': False, 'invocation': {'module_args': module_args}, 'module_name': module_name}

    class TestActionModule(ActionModule):
        _templar = None
        _connection = None
        _shell = None

# Generated at 2022-06-13 11:25:19.962808
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 11:25:23.835802
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None,
                                 templar=None, shared_loader_obj=None)
    assert action_module._supports_check_mode is True
    assert action_module._supports_async is True



# Generated at 2022-06-13 11:25:30.771829
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    action_module = ActionModule()

    args = {}
    task_vars = {}
    facts_result = {}
    facts_result['ansible_facts'] = {'pkg_mgr': 'yum'}
    # test for normal run
    ansible_module_run = AnsibleModule()
    ansible_module_run.run_command = MagicMock(return_value= (0, "", ""))
    ansible_module_run.get_bin_path = MagicMock(return_value="/usr/bin/dnf")
    # Format the result of the action_module as the result of
    # the mocked ansible module.
    result = ansible_module_run.exit_json(**action_module.run(args, task_vars))

# Generated at 2022-06-13 11:25:40.862441
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest

    connection = {'name': 'test_connection'}
    _shared_loader_obj = {'name': 'test_loader'}

    action_base = ActionBase()

    class Task:
        def __init__(self):
            self.name = 'test_task'
            self.action = 'yum'
            self.async_val = None
            self.delegate_to = None
            self.delegate_facts = None

    class PlayContext:
        def __init__(self):
            self.connection = 'test_connection'
            self.check_mode = False
            self.become = False
            self.diff = False

    mock_task = Task()

    mock_task.args = dict(use = 'yum')

# Generated at 2022-06-13 11:25:48.797060
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock_display = Display()
    mock_task = {"args": {"use_backend": "fake_backend"}}
    mock_tmp = None
    mock_task_vars = None

    action_module = ActionModule(task=mock_task, connection=None, play_context=None, loader=None, templar=None,
                                 shared_loader_obj=None)
    action_module._supports_check_mode = True
    action_module._supports_async = True
    action_module._display = mock_display
    action_module._task = mock_task


# Generated at 2022-06-13 11:25:53.888926
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(
        task=dict(args=dict()),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert action is not None

# Generated at 2022-06-13 11:25:58.206246
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a new ActionModule object
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert am is not None



# Generated at 2022-06-13 11:26:07.979736
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()

    #1 Fail case
    result = module.run({}, {})

    #2 Fail case
    result = module.run({}, { 'ansible_facts': { 'pkg_mgr': 'auto' } })

    #3 Fail case
    result = module.run({}, { 'ansible_facts': { 'pkg_mgr': 'auto' }, 'use_backend': 'yum4' })

    #4 Pass case
    result = module.run({}, { 'ansible_facts': { 'pkg_mgr': 'auto' }, 'use': 'yum' })

    #5 Pass case
    result = module.run({}, { 'ansible_facts': { 'pkg_mgr': 'auto' }, 'use_backend': 'yum' })

    #6 Pass case

# Generated at 2022-06-13 11:26:14.877285
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class MockActionPlugin():
        """Mock class for the ActionModule class"""
        def __init__(self):
            self._task = MockTask()
            self._task.args = { 'use': 'auto' }
            self._connection = MockConnection()
            self._shared_loader_obj = MockLoader()
            self._templar = MockTemplar()
            self._execute_module = MockExecuteModule()

    class MockTask():
        """Mock class for the ActionModule class"""
        def __init__(self):
            self.delegate_to = False
            self.delegate_facts = False
            self.async_val = False

    class MockConnection():
        """Mock class for the ActionModule class"""
        def __init__(self):
            self._shell = MockShell()


# Generated at 2022-06-13 11:28:04.526765
# Unit test for constructor of class ActionModule
def test_ActionModule():
    return ActionModule(module_name='yum', task_vars={})



# Generated at 2022-06-13 11:28:06.824286
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task=dict(action=dict(module_name="yum", module_args="module args")),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    action_module.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 11:28:15.086159
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor of class ActionModule
    module = ActionModule(
        task=dict(args=dict()),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )

    # test instance of class
    assert isinstance(module, ActionModule)

    # test attributes of class
    assert module.TRANSFERS_FILES == False
    assert module._supports_check_mode == True
    assert module._supports_async == True


# Generated at 2022-06-13 11:28:17.577586
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionModule
    mod = ActionModule()
    assert mod is not None
    assert mod.TRANSFERS_FILES is False

# Generated at 2022-06-13 11:28:20.842042
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.yum import ActionModule

    obj = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert obj

# Generated at 2022-06-13 11:28:22.821984
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None, None)
    assert action_module is not None

# Generated at 2022-06-13 11:28:24.591044
# Unit test for constructor of class ActionModule
def test_ActionModule():
    args = dict(use='auto')
    am = ActionModule(None, args, None)


# Generated at 2022-06-13 11:28:25.629971
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    :return:
    '''
    pass



# Generated at 2022-06-13 11:28:26.640680
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.common.removed import removed

    assert removed is not None

# Generated at 2022-06-13 11:28:31.908456
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    def execute_module(module_name, module_args, task_vars):
        return action_module.run(module_name, module_args, task_vars)

    from ansible.module_utils.six import StringIO
    from ansible.plugins.loader import action_loader
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.display import Display
    from ansible.utils.plugins import PluginLoader

    class MockDisplay(Display):
        def __init__(self):
          pass

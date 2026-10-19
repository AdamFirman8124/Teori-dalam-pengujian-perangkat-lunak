

# Generated at 2022-06-13 11:19:01.246865
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module._task = Task()
    module._task.delegate_to = "localhost"
    module._task.delegate_facts = True
    module._task.async_val = None
    module._templar = Templar(loader=DictDataLoader())
    module._templar._available_variables = {'hostvars': {'localhost': {'ansible_facts': {'pkg_mgr': "dnf"}}}}
    result = module.run(None, None)
    assert result['failed'] is False and result['msg'] == "", "run() returned unexpected results"
    assert "ansible_facts" in result and result["ansible_facts"] == {'pkg_mgr': 'dnf'}, "run() returned unexpected results"



# Generated at 2022-06-13 11:19:03.978540
# Unit test for constructor of class ActionModule
def test_ActionModule():
    connection = None
    module_loader = None
    class_action_module = ActionModule(connection, module_loader)
    assert class_action_module is not None

# Generated at 2022-06-13 11:19:14.181930
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.utils.context_objects as context_objects
    import ansible.plugins.loader as loader
    import ansible.plugins.action as action
    import ansible.utils.vars as vars
    import ansible.utils.template as template
    import ansible.utils.display as display

    # Load plugins
    action._load_action_plugins()
    loader.load_plugins()

    # Create a context
    context = context_objects.DynamicGlobal()

    # Create a task
    task = {
        'action': {
            '__ansible_module__': 'yum',
            '__ansible_arguments__': {'use': 'auto', 'name': 'foo'}
        },
        'async_val': False
    }

    # Create a display
    display_obj = display.Display()



# Generated at 2022-06-13 11:19:22.594452
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFacts

    mock_task = Mock()
    mock_task.args = dict(use='auto', install=True, name='python')
    mock_task.delegate_to = None
    mock_task.delegate_facts = False
    mock_task.async_val = False

    am = ActionModule(mock_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # test yum because we know it will be installed on most machines
    pkg_mgr_facts = PkgMgrFacts()
    pkg_mgr_facts.get_platform_facts()
    pkg_mgr_facts.get_pkg_mgr_facts()


# Generated at 2022-06-13 11:19:23.687765
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert a.TRANSFERS_FILES is False

# Generated at 2022-06-13 11:19:29.219708
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Example setup
    tree = {
        'module': 'yum',
        'action': 'foo',
        'args': {
            'use': 'auto',
            'other': 'arg'
        }
    }
    try:
        m = ActionModule(tree, MagicMock(), MagicMock(), MagicMock())
    except Exception:
        pass
    m.run(MagicMock(), MagicMock())

# Generated at 2022-06-13 11:19:29.793261
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:19:31.093155
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(None, None, {})
    assert mod

# Generated at 2022-06-13 11:19:31.634930
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 11:19:42.029075
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import sys

    if sys.version_info[0] > 2:
        mod = __import__('ansible.compat.tests.mock', fromlist='ansible.compat.tests.mock')
    else:
        import imp
        mod = imp.load_source('ansible.compat.tests.mock', 'lib/ansible/compat/tests/mock.py')

    class MockDisplay(object):
        def __init__(self):
            pass

        def debug(self, msg):
            print("display_debug: %s" % msg)

        def vvvv(self, msg):
            print("display_vvvv: %s" % msg)

    class MockShell(object):
        def __init__(self):
            pass

        def tmpdir(self):
            return "/tmp/"



# Generated at 2022-06-13 11:19:59.569304
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule.

    Tests if the correct modules are chosen for the yum and dnf cases.
    '''

    test_vars = {'ansible_facts': {'pkg_mgr': 'yum'}}

    task = MagicMock()
    task.args = {'name': 'git'}

    # Test with yum (yum3)
    task.delegate_facts = False
    task.delegate_to = None
    task.async_val = None

    m_module_loader = MagicMock()
    m_module_loader.has_plugin.side_effect = lambda x: x.startswith('ansible.legacy.yum')

    m_shared_loader_obj = MagicMock()
    m_shared_loader_obj.module

# Generated at 2022-06-13 11:20:02.382938
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Dummy test to exercise AnsibleAction.run method
    action = ActionModule(None, None)
    action.run(None, None)



# Generated at 2022-06-13 11:20:04.219340
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, 'run')

# Generated at 2022-06-13 11:20:07.445168
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.yum import ActionModule
    a = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert a.run(None, None), "Result of run method should be a dict"

# Generated at 2022-06-13 11:20:16.758559
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 11:20:17.354058
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:20:17.982035
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule != None

# Generated at 2022-06-13 11:20:29.046492
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create mock objects for test
    class MockTask:
        def __init__(self):
            self.async_val = 'test'
            self.args = {}
            self.delegate_to = None
            self.delegate_facts = None
    class MockTaskVars:
        pass
    class MockTemplar:
        pass
    class MockConnection:
        def __init__(self):
            self._shell = MockShell()
        class MockLoader:
            class MockModuleLoader:
                def has_plugin(self, mod):
                    return True
        class MockSharedLoaderObj:
            def __init__(self):
                self.module_loader = self.MockLoader.MockModuleLoader()
        shared_loader_obj = MockSharedLoaderObj()

# Generated at 2022-06-13 11:20:37.275600
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up the parameters required by class AnsibleModule
    args = {'use': 'auto', 'state': 'latest'}
    module = 'ansible.legacy.yum'
    # Set up the parameters required by class ActionModule
    tmp = '/tmp/ansible-tmp-1542475948.71-40284848255719/'
    task_vars = dict(ansible_facts=dict(pkg_mgr='dnf'))

    # Create an instance of class ActionModule
    action_module_obj = ActionModule()
    action_module_obj._connection = MagicMock()
    action_module_obj._templar = MagicMock()
    action_module_obj._shared_loader_obj = MagicMock()
    action_module_obj._task = MagicMock()
    action_module_obj

# Generated at 2022-06-13 11:20:44.878372
# Unit test for constructor of class ActionModule
def test_ActionModule():
    for action in [
        'yum',
        'dnf'
    ]:
        class Connection:
            def __init__(self):
                self.defs = dict()

            def get_option(self, opt):
                return self.defs[opt]

            def set_option(self, opt, val):
                self.defs[opt] = val

            def has_pipelining(self):
                return True

        class Task:
            def __init__(self):
                self.args = dict()
                self.async_val = False

        class ModuleLoader:
            def __init__(self):
                self.defs = dict()

            def has_plugin(self, mod):
                return mod in self.defs

            def add_directory(self, key, val):
                self.defs

# Generated at 2022-06-13 11:21:06.249824
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 11:21:13.260653
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule('setup', 'yum', ActionBase._shared_loader_obj, 'tasks/yum.yml', 2, {})
    assert module.p, 'No p'
    assert module.v, 'No v'
    assert module._templar, 'No _templar'
    assert module._shared_loader_obj, 'No _shared_loader_obj'
    assert module._connection, 'No _connection'
    assert module._play_context, 'No _play_context'
    assert module._task, 'No _task'
    assert module._loader, 'No _loader'
    assert module._task_vars, 'No _task_vars'
    assert module._iterator, 'No _iterator'
    assert module._play_context, 'No _play_context'
    assert module.set_options

# Generated at 2022-06-13 11:21:23.142709
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os
    import pytest

    """Unit test for ActionModule run"""

    if not pytest.config.pluginmanager.hasplugin("yaml"):
        pytest.skip("This test requires the YAML plugin to run.")

    import yaml

    # pylint: disable=protected-access
    #file_name = os.path.join(os.path.dirname(__file__), "..", "..", "..", "testcases", "testdata", "test_playbooks", "test_run_action_module.yml")
    file_name = os.path.join(os.path.dirname(__file__), "..", "..", "..", "testcases", "testdata", "test_run_action_module.yml")

    # Read file_name as YAML


# Generated at 2022-06-13 11:21:27.693443
# Unit test for constructor of class ActionModule
def test_ActionModule():
    foo = ActionModule()
    assert foo._shared_loader_obj is not None
    assert foo._loader is not None
    assert foo._templar is not None
    assert foo._connection is not None
    assert foo._play_context is not None
    assert foo._task.async_val is False
    assert foo._supports_async is True
    assert foo._supports_check_mode is True

# Generated at 2022-06-13 11:21:30.100308
# Unit test for constructor of class ActionModule
def test_ActionModule():

    action_module = ActionModule(None, None, None, None)
    print(action_module)


# Generated at 2022-06-13 11:21:31.507882
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 11:21:33.788601
# Unit test for constructor of class ActionModule
def test_ActionModule():
    myobj = ActionModule()
# Check the action plugin version

# Generated at 2022-06-13 11:21:44.313981
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    params = dict(
        state='installed',
        name='gcc',
        force="yes",
        allow_downgrade="yes",
        use='yum'
    )

    module_mock = ActionModule(task=dict(args=params), connection=MockConnection())

    result = module_mock.run(tmp=None, task_vars=None)
    assert result['failed'] == False

    assert result['changed'] == True

    module_mock.run(tmp=None, task_vars={'ansible_pkg_mgr': "dnf"})
    module_mock.run(tmp=None, task_vars={'ansible_pkg_mgr': "dnf"})

# Generated at 2022-06-13 11:21:49.199073
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action as action_base
    import ansible.plugins.action.yum as action_yum

    global VALID_BACKENDS

    # Test the constructor
    yum_action_module = action_yum.ActionModule(action_base.DummyConnection(), 'test')

    assert yum_action_module.VALID_BACKENDS == VALID_BACKENDS


# Generated at 2022-06-13 11:21:51.535007
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule

    :return:
    """
    module = ActionModule()
    module.run(tmp=None, task_vars={})

# Generated at 2022-06-13 11:22:21.013656
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None)
    module = action_module._task.args.get('use', action_module._task.args.get('use_backend', 'auto'))
    assert module == 'auto'

    action_module = ActionModule(None, {}, None)
    module = action_module._task.args.get('use', action_module._task.args.get('use_backend', 'auto'))
    assert module == 'auto'

# Generated at 2022-06-13 11:22:28.521616
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.loader
    import ansible.plugins.action
    import os
    import yaml
    from ansible.module_utils._text import to_bytes

    global_vars = dict(imaginary_variable='imaginary_value')
    context_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    paths = dict(action=os.path.join(context_path, 'action_plugins'))
    loader = ansible.plugins.loader.ActionModuleLoader(paths, '', global_vars)
    action_module = ansible.plugins.action.ActionModule(loader, None, '', '', '', None, None, global_vars)
    tmp = None
    task_vars = dict(ansible_pkg_mgr='auto')

# Generated at 2022-06-13 11:22:29.282840
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:22:31.930578
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    main_module_class = ActionModule()
    main_module_class.run()


if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 11:22:32.732206
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:22:35.588391
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Creating an object of class ActionModule
    act_obj = ActionModule()

    # Calling method run of class ActionModule
    act_obj.run()

# Generated at 2022-06-13 11:22:42.502012
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Set up action module
    module_args = {
        "use_backend": "yum",
        "use": "yum4"
    }
    action_mod = ActionModule(None, module_args, None)

    # Constructor
    task_vars = {

    }
    action_mod.run(None, task_vars)

# Generated at 2022-06-13 11:22:43.616144
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None, None, None, None)
    assert module

# Generated at 2022-06-13 11:22:45.780519
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionm = ActionModule(None, None)
    assert actionm.VALID_BACKENDS == frozenset(('yum', 'yum4', 'dnf'))

# Generated at 2022-06-13 11:22:46.681526
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:23:43.589164
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import unittest
    import ansible.plugins.action.yum as yum
    import ansible.module_utils.facts as facts

    class Mock_ActionBase(yum.ActionModule):
        def __init__(self, *args, **kwargs):
            self._task = Mock_Task()
            self._templar = Mock_Templar()
            self._shared_loader_obj = Mock_SharedLoaderObj()
            self._connection = Mock_Conn()

        def _execute_module(self, *args, **kwargs):
            pass

    class Mock_Task:
        def __init__(self):
            self.async_val = None
            self.args = {}
            self.delegate_facts = None
            self.delegate_to = None


# Generated at 2022-06-13 11:23:44.916629
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action as action
    global action
    assert isinstance(action, module)


# Generated at 2022-06-13 11:23:54.563538
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    action_module = ActionModule()

    test_args = dict()
    test_args['name'] = 'httpd'
    test_args['state'] = 'installed'

    # All packages are installed, no changes
    test_result = action_module.run(task_vars=dict(ansible_facts=dict(pkg_mgr='dnf')))
    assert test_result['failed'] is False
    assert test_result['module_name'] == 'ansible.legacy.dnf'

    # Yum is not installed and package is not installed, has changed
    test_args['state'] = 'absent'
    test_args['name'] = 'httpd'
    test_result = action_module.run(task_vars=dict(ansible_facts=dict(pkg_mgr='auto')))
    assert test

# Generated at 2022-06-13 11:24:01.079472
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert action_module.run() == {
        'failed': True,
        'msg': ("Could not detect which major revision of yum is in use, which is required to determine module backend.",
                "You should manually specify use_backend to tell the module whether to use the yum (yum3) or dnf (yum4) backend})"),
    }

# Generated at 2022-06-13 11:24:02.933055
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.errors
    am = ActionModule(None, None, None, None, None, None)
    assert(am)

# Generated at 2022-06-13 11:24:14.118584
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test method for run method of class ActionModule
    '''
    from ansible.module_utils.basic import AnsibleModule
    from ansible.plugins.loader import action_loader

    mod = AnsibleModule(
        argument_spec=dict(
            use=dict(),
            use_backend=dict()
        ),
        supports_check_mode=False,
        bypass_checks=False,
    )

    print("testing run method for ActionModule")
    task = mod.params
    # TODO: This could be handled in a helper module
    task_vars = dict()
    task_vars['ansible_facts'] = dict()
    task_vars['ansible_facts']['pkg_mgr'] = 'yum'
    display = Display()

# Generated at 2022-06-13 11:24:19.000744
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule(None, {'name': 'test', 'argument_spec': {}})
    assert not m._shared_loader_obj.module_loader.has_plugin('ansible.legacy.foo')
    assert m._shared_loader_obj.module_loader.has_plugin('ansible.legacy.yum')

# Generated at 2022-06-13 11:24:28.347094
# Unit test for constructor of class ActionModule
def test_ActionModule():

    connection = object()
    data = object()
    templar = object()
    shared_loader_obj = object()
    # Constructor test:
    action = ActionModule(connection=connection,
                          task_vars=data,
                          tmp=data,
                          templar=templar,
                          module_compression=data,
                          module_name="something",
                          module_args={},
                          task_uuid=data,
                          _task=data,
                          _ansible_version=data,
                          load_path=data,
                          shared_loader_obj=shared_loader_obj)

    assert action._task == data
    assert action._task_vars == data
    assert action._templar == templar
    assert action._connection == connection
    assert action._

# Generated at 2022-06-13 11:24:30.851340
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Test the constructor and represents an example of unit test."""

    am = ActionModule(None, {}, {})
    assert isinstance(am, ActionModule)
    assert isinstance(am.action_loader, ActionBase)
    assert am.action_loader != am

# Generated at 2022-06-13 11:24:41.388815
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class FakeModule:
        def __init__(self):
            self._supports_check_mode = True
            self._supports_async = True
            pass

    # create a fake action module
    am = ActionModule()
    am.action_loader = FakeModule()
    am.task_vars = dict()
    am._shared_loader_obj = FakeModule()
    am._task = FakeModule()
    am.task_vars = dict()
    am._connection = FakeModule()
    am._templar = FakeModule()
    am._connection._shell = FakeModule()
    am._connection._shell.tmpdir = "test_tmpdir"
    am._remove_tmp_path = FakeModule()

    # test the case that task.use_backend and task.use are both specified
    # in the task
   

# Generated at 2022-06-13 11:26:24.980790
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()

# Generated at 2022-06-13 11:26:32.647681
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.block
    import ansible.playbook.role
    test_play = ansible.playbook.play.Play()
    test_block = ansible.playbook.block.Block()
    test_block._parent = test_play
    test_role = ansible.playbook.role.Role()
    test_play.set_variable_manager(ansible.vars.manager.VariableManager())
    test_task = ansible.playbook.task.Task()
    test_task._role = test_role
    test_task._block = test_block
    test_task.args = {"use_backend":"yum4"}
    test_task.action = 'yum'
    test_task.async_val

# Generated at 2022-06-13 11:26:41.344518
# Unit test for constructor of class ActionModule
def test_ActionModule():
    hostvars = dict()
    hostvars['test_host'] = dict()
    hostvars['test_host']['ansible_facts'] = dict()
    hostvars['test_host']['ansible_facts']['pkg_mgr'] = 'yum'
    task_vars = dict()
    task_vars['ansible_connection'] = 'test_connection'
    task_vars['ansible_inventory_sources'] = ['[']
    task_vars['hostvars'] = hostvars
    obj = ActionModule()
    obj._task.args = dict()
    obj._task.args['use_backend'] = 'auto'
    obj._task.delegate_to = 'test_host'
    obj._task.async_val = False
    obj._task.de

# Generated at 2022-06-13 11:26:52.440535
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    class FakeModuleAction(ActionBase):
        def run(self, *args, **kwargs):
            return {"failed": False, "ansible_facts": {"pkg_mgr": "yum"}}

    class FakeTask(object):
        def __init__(self, args=None, delegate_to=None, delegate_facts=None, async_val=False):
            self.args = args
            self.delegate_to = delegate_to
            self.delegate_facts = delegate_facts
            self.async_val = async_val

    class FakeLoader(object):
        def __init__(self):
            self.module_loader = FakeModuleLoader()


# Generated at 2022-06-13 11:26:54.274582
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    display = Display()
    # display.debug('Task should have failed with msg "%s", but it did not.' % expected_err)

# Generated at 2022-06-13 11:27:08.014138
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    class Task(object):
        args = dict()
        async_val = None
    class Connection(object):
        class _shell(object):
            tmpdir = '/tmp'
    task = Task()
    connection = Connection()
    m._task = task
    m._connection = connection
    m._shared_loader_obj = object()
    m._templar = object()
    m._execute_module = object()
    m._remove_tmp_path = object()
    task.args = dict()
    m.run()
    # delete tmpdir of connection
    m._remove_tmp_path.assert_called_with(m._connection._shell.tmpdir)
    # no msg in result
    assert not 'msg' in m.run().keys()


# Generated at 2022-06-13 11:27:13.218990
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(
        task=dict(args=dict(arg1="value1",arg2="value2")),
        connection=dict(
            _shell=dict(
                tmpdir="tmpdir_value"
            )
        ),
        play_context=dict(
            check_mode=True
        ),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )

# Generated at 2022-06-13 11:27:23.891524
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Case#1: Should fail when use_backend and use are passed as arguments
    test_task = dict(name="yum", args=dict(use="yum", use_backend="yum"))
    test_task_vars = {}
    test_action = ActionModule()
    test_action._task = test_task
    display = Display()
    display.verbosity = 3
    try:
        test_action.run(None, test_task_vars)
    except AnsibleActionFail as e:
        assert str(e) == "parameters are mutually exclusive: ('use', 'use_backend')"

    # Case#2: Should successfully detect the version of package manager to use
    from ansible.compat.tests import unittest
    test_case = unittest.TestCase('__init__')
   

# Generated at 2022-06-13 11:27:35.110625
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(load_plugins=False)

    # simulate the run action from ansible.plugins.action.ActionBase
    action_module._supports_check_mode = True
    action_module._supports_async = True

    # simulate the legacy method
    action_module._remove_tmp_path = lambda _: None

    # simulate the _execute_module() method
    mock_execute_module = lambda *_, **__: {'ansible_facts': {'pkg_mgr': 'yum3'}}
    action_module._execute_module = mock_execute_module

    # simulate the task, which is an instance of ansible.playbook.task.Task

# Generated at 2022-06-13 11:27:45.330449
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # You can test against valid dictionary of params
    test_dict = {'use_backend': 'auto', 'use': 'yum'}
    # You must initiate class object with a valid dictionary of action parameters
    obj = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # You can also initiate class object with None to test against all possible params
    obj = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # You can test against valid dictionary of params
    test_dict = {'use_backend': 'auto', 'use': 'yum'}
    # You must initiate class object with a valid dictionary of action parameters
    obj = Action
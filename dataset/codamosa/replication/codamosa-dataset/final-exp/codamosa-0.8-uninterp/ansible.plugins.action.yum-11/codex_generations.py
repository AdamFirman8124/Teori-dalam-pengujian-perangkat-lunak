

# Generated at 2022-06-13 11:19:01.990889
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    display = Display()
    display.verbosity = 4

    my_action = ActionModule(task=dict(action=dict(module_name='yum', module_args=dict(name=['httpd'], state='present'))))

    my_action._task.vars = dict(ansible_pkg_mgr='dnf', ansible_facts=dict(ansible_pkg_mgr='auto'))
    my_action._templar = my_action.loader.template

    results = my_action.run(task_vars=my_action._task.vars)
    assert results.get('failed') == True

# Generated at 2022-06-13 11:19:03.524705
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am.TRANSFERS_FILES == False

# Generated at 2022-06-13 11:19:07.753550
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''
    action_module = ActionModule()
    assert action_module._supports_check_mode
    assert action_module._supports_async
    assert action_module.TRANSFERS_FILES == False

# Generated at 2022-06-13 11:19:17.353649
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import action_loader, module_loader
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    import ansible.constants as C

    def create_host(host):
        host = Host(name=host)
        return host

    def create_play(play_hosts):
        play_source = dict(
            name="Ansible Play",
            hosts=play_hosts,
            gather_facts='no',
            tasks=[dict(
                action=dict(
                    module='setup'
                )
            )]
        )


# Generated at 2022-06-13 11:19:25.141549
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # FIXME: all tests are failing, need to fix
    return
    # test case 1: run with parameters use_backend, and use_backend contains
    # a valid value, dnf, this is a positive test case
    task = Mock()
    task.delegate_to = ''
    task.args = dict(use_backend='dnf')
    task.async_val = False
    task.delegate_facts = False
    action = ActionModule(task, {})
    action.run()

    # test case 2: run with parameters use_backend and use.
    # this is a negative test case
    task = Mock()
    task.delegate_to = ''
    task.args = dict(use_backend='dnf', use='yum')
    task.async_val = False
    task

# Generated at 2022-06-13 11:19:25.796786
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert 3 == 3

# Generated at 2022-06-13 11:19:26.421715
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:19:29.596974
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None,
                          templar=None, shared_loader_obj=None)
    assert module is not None
    assert module._shared_loader_obj is not None

# Generated at 2022-06-13 11:19:40.168947
# Unit test for constructor of class ActionModule
def test_ActionModule():
    yum3_action = ActionModule(
        task=dict(args={'use': 'yum'}),
        connection=None,
        play_context=dict(check_mode=True, prompt=None),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert yum3_action
    assert yum3_action._supports_check_mode is True
    assert yum3_action._supports_async is True

    yum3_action = ActionModule(
        task=dict(args={'use_backend': 'yum'}),
        connection=None,
        play_context=dict(check_mode=True, prompt=None),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

# Generated at 2022-06-13 11:19:47.921875
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.path import makedirs_safe
    from ansible.module_utils.facts import get_facts
    from ansible.module_utils._text import to_bytes
    from ansible.utils.display import Display
    import os
    import stat
    import shutil
    import tempfile
    import json
    import platform

    dummy_sys = platform.system()
    dummy_machine = platform.machine()
    dummy_version = platform.python_version()
    tmpdir_path = tempfile.gettempdir()
    os.environ['PATH'] = os.pathsep.join([tmpdir_path, os.environ['PATH']])

# Generated at 2022-06-13 11:19:56.079670
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    # ensure the constructor has set the _supports_check_mode attribute
    am.main()

# Generated at 2022-06-13 11:19:56.543925
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:20:08.511391
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.yum_select
    import json
    import sys
    import os
    import tempfile
    from ansible.module_utils.common.collections import is_iterable

    # Initialize a class instance
    am = ansible.plugins.action.yum_select.ActionModule(
        task=dict(async_val=None, async_seconds=None, _ansible_no_log=False,
                  delegate_to='127.0.0.1', _ansible_verbosity=0, _ansible_version=1.99,
                  delegate_facts=False))

    # Run test
    tmp = tempfile.TemporaryDirectory()
    task_vars = dict(ansible_facts=dict(pkg_mgr='yum'))

# Generated at 2022-06-13 11:20:09.821438
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test constructor of class ActionModule
    module = ActionModule()
    assert module

# Generated at 2022-06-13 11:20:13.586037
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module_run_test = ActionModule(DummyTask())
    module = action_module_run_test.run(None, None)
    assert module['failed']
    assert module['msg'][0].startswith("parameters are mutually exclusive")

    action_module_run_test = ActionModule(DummyTask())
    action_module_run_test._task.args = {'use':'auto'}
    try:
        action_module_run_test.run(None, None)
    except AnsibleActionFail:
        assert False


# Generated at 2022-06-13 11:20:15.168423
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module is not None


# Generated at 2022-06-13 11:20:20.619405
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule(action='yum', action_plugin='yum', name='yum')
    assert m.action == 'yum'
    assert m.action_plugin == 'yum'
    assert m.name == 'yum'
    assert m._supports_check_mode == True
    assert m._supports_async == True

# Test run() method of class ActionModule

# Generated at 2022-06-13 11:20:21.993438
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), object)

# Generated at 2022-06-13 11:20:31.919887
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_module_file = "ansible_collections/ansible/builtin/plugins/action/plugins/modules/yum.py"
    module_args = dict(
        name='httpd',
        state='present',
    )

    test_module = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    result = test_module._execute_module(module_name=test_module_file, module_args=module_args, task_vars={})

    assert result['name'] == 'httpd'
    assert result['state'] == 'present'
    assert result['changed'] == False
    assert result['module_stderr'] == ''

# Generated at 2022-06-13 11:20:40.430748
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.handler import Handler
    from ansible.playbook.handlerlist import HandlerList
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar

    class RunnerMock:
        def __init__(self, loader):
            self._loader = loader
            self._shell = None
            self._final_q = None
            self._connection = None

        @property
        def loader(self):
            return self._loader


# Generated at 2022-06-13 11:21:02.298644
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFacts

    module = ActionModule(None, None, None)

    # test auto-detection, error handling, and single run of all 3 backends
    # note: only way to mock a delegate is to construct the whole Task object here
    fake_task = type('fake_task', (object,), {'async_val': False, 'delegate_to': False, 'delegate_facts': True})()
    for val in ['auto', 'yum', 'yum4', 'dnf']:
        fake_task.args = {'use_backend': val}
        outcome = module.run(None, task_vars={'ansible_facts': dict(PkgMgrFacts.defaultdict)})
        assert outcome == module.run

# Generated at 2022-06-13 11:21:06.395175
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a mock instance of class ActionModule
    m_ActionModule = ActionModule()
    try:
        # Call the run method of class ActionModule
        m_ActionModule.run()
    except Exception as e:
        assert(False), "An error occurred in ActionModule.run(): %s" % e

# Generated at 2022-06-13 11:21:13.384228
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.path import unfrackpath
    from ansible.plugins.loader import action_loader

    mock_task = type('MockTask', (object, ), {})
    mock_task.args = {}
    mock_task.delegate_to = None
    mock_task.delegate_facts = True
    mock_task.async_val = None
    mock_task.action = 'yum'

    mock_connection = type('MockConnection', (object,), {})
    mock_connection._shell = type('_MockShell', (object, ), {})
    mock_connection._shell.tmpdir = '/tmp'

    mock_loader = type('MockLoader', (object, ), {})
    mock_loader.module_loader = type('_MockModuleLoader', (object, ), {})
    mock_

# Generated at 2022-06-13 11:21:14.603000
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, None, None, None, None) is not None

# Generated at 2022-06-13 11:21:15.305863
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    raise NotImplementedError


# Generated at 2022-06-13 11:21:19.046984
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # pylint: disable=unused-argument
    '''Unit test for the run method of class ActionModule'''
    # create an instance of class ActionModule to call action plugin run() method
    mod = ActionModule(None, None, None, None, None, None, None, None)
    # call method run() of class ActionModule
    mod.run()



# Generated at 2022-06-13 11:21:28.251562
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 11:21:41.228210
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MockTask:
        def __init__(self, async_val, arguments=None):
            self.async_val = async_val
            if arguments is not None:
                self.args = arguments
            else:
                self.args = {}
        def __str__(self):
            return "<MockTask>"

    class MockTemplar:
        def __init__(self, pkg_mgr):
            self.template_string = "{{ansible_facts.pkg_mgr}}"
            self.pkg_mgr = pkg_mgr
        def template(self, string):
            return self.pkg_mgr

    class MockConnection:
        def __init__(self, tmpdir):
            self._shell = MockShell(tmpdir)
        def __enter__(self):
            return self

# Generated at 2022-06-13 11:21:50.414967
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module.VERBOSITY = 0
    module.display = Display()
    module._shared_loader_obj = object()
    module._shared_loader_obj.module_loader = object()
    module._shared_loader_obj.module_loader.has_plugin = lambda arg: arg == 'ansible.legacy.yum'
    module._task.args = {'name': 'foo', 'use_backend': 'yum4'}
    module._templar = object()
    module._templar.template = lambda arg: 'yum4' if arg == "{{ansible_facts.pkg_mgr}}" else 'foo'
    module._execute_module = lambda arg, module_args, task_vars, wrap_async: {'failed': False, 'msg': 'foo'}


# Generated at 2022-06-13 11:21:52.577679
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()
    # TODO: build testcase


# Generated at 2022-06-13 11:22:20.030416
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule()
    assert isinstance(m, ActionModule)

# Generated at 2022-06-13 11:22:24.992634
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' action_plugins/yum.ActionModule() returns ActionModule '''

    module = ActionModule(
        task=dict(action=dict(module='yum', args=dict(force=True, name='zsh'))),
        connection=dict(),
        play_context=dict(check_mode=True),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict())
    assert module

# Generated at 2022-06-13 11:22:34.653203
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    mocked_module_name = 'ansible.legacy.yum'

    def mock_get_plugin(module_name):
        return mocked_module_name

    def mock_module_loader(module_name):
        return mocked_module_name

    def mocked_execute_module(module_name, module_args, task_vars, wrap_async):
        return {'failed': False}

    original_get_plugin = ActionBase._get_action_plugin
    original_module_loader = ActionBase._get_action_plugin
    original_execute_module = ActionBase._execute_module

    ActionBase._get_action_plugin = mock_get_plugin
    ActionBase._module_loader = mock_module_loader
    ActionBase._execute_module = mocked_execute_module

    module = ActionModule()


# Generated at 2022-06-13 11:22:47.573450
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ This is a constructor test for the class ActionModule """
    actionBaseObj = ActionBase()
    actionObj = ActionModule(actionBaseObj._task, actionBaseObj._connection, actionBaseObj._play_context,
                             actionBaseObj._loader, actionBaseObj._templar, actionBaseObj._shared_loader_obj)
    assert actionBaseObj._task == actionObj._task
    assert actionBaseObj._connection == actionObj._connection
    assert actionBaseObj._play_context == actionObj._play_context
    assert actionBaseObj._loader == actionObj._loader
    assert actionBaseObj._templar == actionObj._templar
    assert actionBaseObj._shared_loader_obj == actionObj._shared_loader_obj


# Generated at 2022-06-13 11:22:56.495061
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # constructor variables
    _task = {
        'name': 'testTask',
        'async': 33,
        'async_val': 'asyncValue',
        'environment': {},
        'args': {
            'key': 'value',
            'key2': 'value2'
        },
        'delegate_to': 'delegateTo',
        'delegate_facts': True,
    }


# Generated at 2022-06-13 11:22:57.296292
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    raise NotImplementedError()

# Generated at 2022-06-13 11:23:01.214262
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    test_action_module_run = test_action_module.run(tmp=None, task_vars=None)
    assert "failed" in test_action_module_run


# Generated at 2022-06-13 11:23:04.056020
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(
        connection=None,
        task_vars=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert mod

# Generated at 2022-06-13 11:23:06.845306
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module is not None

# Generated at 2022-06-13 11:23:17.065224
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    import ansible.constants as C


# Generated at 2022-06-13 11:24:16.719468
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import os
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import action_loader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.callback import CallbackBase
    import ansible.constants as C
    from ansible.playbook.play import Play
    from ansible.template import Templar

    class CallbackModule(CallbackBase):
        """
        A sample callback plugin used for testing
        """
        CALLBACK_VERSION = 2.0

# Generated at 2022-06-13 11:24:20.536269
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    arg = '''{"use": "yum"}'''
    task_vars = {}
    result = {}
    my_obj = ActionModule(None, task_vars, arg)
    my_obj.run()

# Generated at 2022-06-13 11:24:21.207067
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:24:21.811094
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 11:24:23.554248
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Unit test for class ActionModule """

    assert(True)

# Generated at 2022-06-13 11:24:28.989548
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module.validate_backend('dnf') == True
    assert module.validate_backend('yum') == True
    assert module.validate_backend('yum4') == True
    assert module.validate_backend('auto') == False
    assert module.validate_backend('yum3') == False
    assert module.validate_backend('rpm') == False
    assert module.validate_backend('rhel') == False
    assert module.validate_backend('centos') == False

# Generated at 2022-06-13 11:24:34.187290
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from units.mock.loader import DictDataLoader


# Generated at 2022-06-13 11:24:44.000434
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager

    task = Task()
    action_plugin = ActionModule(task, {})

    # Test valid backends
    assert action_plugin.VALID_BACKENDS == frozenset(('yum', 'yum4', 'dnf'))

    # Test correct backend detection
    task.args = {'use_backend': 'yum'}

# Generated at 2022-06-13 11:24:47.167151
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create instance of class ActionModule for testing
    action_module_instance = ActionModule()
    # setup the required parameters for testing and return
    return action_module_instance.run()

if __name__ == '__main__':
    # Unit test the module
    print(test_ActionModule_run())

# Generated at 2022-06-13 11:24:54.105670
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_args = dict()
    module_args['use_backend'] = 'yum'
    module_args['name'] = 'httpd'
    module_args['state'] = 'present'
    ansible_facts = dict()
    ansible_facts['pkg_mgr'] = 'yum'
    connection_info = dict()
    task_vars = dict()
    task = dict()
    task['args'] = module_args
    task_vars['ansible_facts'] = ansible_facts
    task_vars['ansible_connection'] = connection_info
    action_module_obj = ActionModule(task, task_vars)

# Generated at 2022-06-13 11:26:49.863187
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Test without all arguments
    am = ActionModule()

    assert am.TRANSFERS_FILES == False
    assert am._supports_check_mode == True
    assert am._supports_async == True

    # Test with arguments
    am = ActionModule(ansible_connection="ssh")

    assert am.TRANSFERS_FILES == False
    assert am._supports_check_mode == True
    assert am._supports_async == True
    assert am._ansible_connection == "ssh"

# Generated at 2022-06-13 11:26:50.679357
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 11:26:56.533137
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule.ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    result = action_module.run()
    assert result == {
            'failed': True,
            'msg': "Could not detect which major revision of yum is in use, which is required to determine module backend.",
            'msg': "You should manually specify use_backend to tell the module whether to use the yum (yum3) or dnf (yum4) backend}"
        }

# Generated at 2022-06-13 11:27:03.155056
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' Unit test for constructor of class ActionModule. '''

    target = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert target.runner_supports_async == True
    assert target.runner_supports_check_mode == True
    assert target.tratransfers_files == False

# Generated at 2022-06-13 11:27:13.667530
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create mock
    mock_loader = unittest.mock.Mock()
    mock_loader.configure_mock(**{'has_plugin.return_value': True})
    mock_task_args = unittest.mock.Mock()
    mock_task_args.configure_mock(**{'get.return_value': 'yum3',
                                     'pop.return_value': 'yum3',
                                     'copy.return_value': {'use': 'yum3'}})

    # Create mocks for module return
    mock_result = unittest.mock.Mock()
    mock_result.configure_mock(**{'update.return_value': 'yum3'})

    # Create mock for task

# Generated at 2022-06-13 11:27:20.596182
# Unit test for constructor of class ActionModule
def test_ActionModule():
    cls = ActionModule
    action_plugin = cls(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # attributes of class ActionModule
    attr = 'TRANSFERS_FILES'
    assert action_plugin.TRANSFERS_FILES == False

    # methods of class ActionModule
    func = 'run'
    assert callable(getattr(action_plugin, func, None))

# Generated at 2022-06-13 11:27:31.664258
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.yum import ActionModule
    from ansible.plugins.action.dnf import ActionModule as DnfActionModule
    from ansible.plugins.action.yum import ActionModule as YumActionModule

    class FakeModule:
        def __init__(self, task_args, module_args, task_vars):
            self._task = FakeTask()
            self._task.args = task_args
            self._module = module_args['use']
            self._module_args = module_args.copy()
            self._task_vars = task_vars

        def run(self, tmp, task_vars):
            return FakeBackendModule.run(self, tmp, task_vars)


# Generated at 2022-06-13 11:27:33.329701
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule('minimal_arguments')
    assert action

# Generated at 2022-06-13 11:27:36.642632
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Given
    module = ActionModule()
    module.result = dict()
    module.result['ansible_facts'] = dict()

    # When
    module.run()

    # Then
    assert(module.result['ansible_facts'] == {})

# Generated at 2022-06-13 11:27:44.122162
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector
    from ansible.plugins.loader import module_loader
    from ansible.template import Templar

    am = ActionModule()

    # Create the "old style" task for backwards compatibility
    am._task.static_args = dict(foo='bar')

    # If delegate_to is present, use_backend must be too, otherwise we can't know
    # which backend to use, since we don't know which system to get facts from.
    am._task.args = dict(use='auto')
    am._task.delegate_to = dict()


# Generated at 2022-06-13 11:18:52.597360
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:18:53.104468
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert a is not None

# Generated at 2022-06-13 11:18:59.530442
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MockConnection(object):
        _shell = None

        def __init__(self):
            self._shell = MockShell()

    class MockShell(object):
        tmpdir = None

        def __init__(self):
            self.tmpdir = '/path/to/tempdir'

    class MockModuleLoader(object):
        has_plugin = None

        def __init__(self):
            self.has_plugin = MockModuleLoader_has_plugin()

    class MockModuleLoader_has_plugin(object):
        def __init__(self):
            pass

        def __call__(self, plugin):
            if plugin == 'ansible.legacy.yum':
                return True
            else:
                return False

    class MockString(object):
        def __init__(self):
            self._string = 'auto'

# Generated at 2022-06-13 11:19:00.233393
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, 'run')

# Generated at 2022-06-13 11:19:06.140647
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create a Module Runner object
    runner = ActionModule()
    # set _loader_obj variable in runner with a mock
    runner._loader_obj = mock.Mock()
    # set _shared_loader_obj variable in runner with a mock
    runner._shared_loader_obj = mock.Mock()
    # set variables in runner
    runner._task = mock.Mock()
    runner._task.async_val = True
    runner._task.args = None
    runner._task.delegate_to = None
    runner._task.delegate_facts = None
    # set _execute_module variable in runner with a mock
    runner._execute_module = mock.Mock()
    # create a mock for class AnsibleActionFail
    mock_AnsibleActionFail = mock.Mock()
    # set _templar variable in

# Generated at 2022-06-13 11:19:07.367786
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert ActionModule.run()

# Generated at 2022-06-13 11:19:13.073122
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module._task = dict()
    module._task['args'] = {'use': 'auto'}
    module._task['action'] = 'yum'
    module._task['async'] = 0
    module._task['async_val'] = 0
    module._templar = dict()
    module._templar.template = lambda x: "auto"
    module.run(None, None)

# Generated at 2022-06-13 11:19:17.269371
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(load_name="", action_name="", task_name="")
    action = module.run()
    assert "msg" in action
    assert action["msg"] == "No defaults/main.yml file was found for yum"
    assert "failed" in action
    assert action["failed"] is True

# Generated at 2022-06-13 11:19:18.484116
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.TRANSFERS_FILES == False


# Generated at 2022-06-13 11:19:29.719241
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test backend auto-detection
    # Build a task so we can call run()
    from ansible.playbook import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    test_task = Task()
    test_task.action = 'yum'
    test_task._role = None
    test_task._block = Block()
    test_task._role = None
    test_task._parent = Play()
    test_task.vars = {}
    test_task.args = {}
    test_task.set_loader(None)

    # Build a connection so we can call run()
    from ansible.inventory.host import Host

# Generated at 2022-06-13 11:19:36.585877
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert (ActionModule())

# Generated at 2022-06-13 11:19:45.622132
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars import VariableManager

    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    import ansible.constants as C

    # initial variables
    play_source = dict(
        name = "YUM",
        hosts = 'localhost',
        gather_facts = 'no',
        tasks = [dict(action=dict(module='yum', args=dict(name=['foo', 'bar'], state='present')))]
    )


# Generated at 2022-06-13 11:19:52.440543
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 11:19:53.662426
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)

# Generated at 2022-06-13 11:20:00.518046
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Test case-1:
    task_obj = dict(
        action=dict(use_backend='auto'),
        args={'name': 'vim', 'state': 'present'},
        async_val=100
    )
    task_vars = dict(ansible_pkg_mgr='yum')
    module_obj = ActionModule(task_obj, connection=dict(), ansible_version=2.7, play_context={}, loader=dict(), templar=dict(), shared_loader_obj=dict())
    result = module_obj.run(task_vars=task_vars)
    assert result['changed'] == True
    assert module_obj._task.args == {'name': 'vim', 'state': 'present'}
    assert module_obj._task.async_val == 100
    assert module_obj

# Generated at 2022-06-13 11:20:02.082310
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None, {})
    return action_module

# Generated at 2022-06-13 11:20:04.777752
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None, None, None, None)
    action = module.run(None, None)
    assert isinstance(action, dict)

# Generated at 2022-06-13 11:20:13.185144
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Action plugin handler for yum3 vs yum4(dnf) operations.

    Enables the yum module to use yum3 and/or yum4. Yum4 is a yum
    command-line compatibility layer on top of dnf. Since the Ansible
    modules for yum(aka yum3) and dnf(aka yum4) call each of yum3 and yum4's
    python APIs natively on the backend, we need to handle this here and
    pass off to the correct Ansible module to execute on the remote system.
    '''

    # create instance of class ActionModule
    action_plugin_instance = ActionModule()

    # execute run method of ActionModule

# Generated at 2022-06-13 11:20:23.344569
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # result should be successful (successful task execution)
    # when the use_backend parameter is yum4
    module_args = dict(name=['httpd'], use_backend='yum4')
    result = ActionModule(dict(module_args=module_args)).run()
    assert result['failed'] is False

    # result should be successful (successful task execution)
    # when the use_backend parameter is yum
    module_args = dict(name=['httpd'], use_backend='yum')
    result = ActionModule(dict(module_args=module_args)).run()
    assert result['failed'] is False

    # result should be successful (successful task execution)
    # when the use_backend parameter is yum4

# Generated at 2022-06-13 11:20:33.160148
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # mock objects
    tmp = None
    task_vars = {
        'ansible_pkg_mgr': 'yum' # setting ansible_pkg_mgr in task_vars to test auto logic without collecting facts
    }
    result = super(ActionModule, ActionModule).run(None, task_vars)
    del tmp # tmp no longer has any effect

    # Executing run method
    result = super(ActionModule, ActionModule).run(tmp, task_vars)
    del tmp  # tmp no longer has any effect

    # Test path if 'use' and 'use_backend' are present in self._task.args

# Generated at 2022-06-13 11:20:46.511057
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass


# Generated at 2022-06-13 11:20:52.880172
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest
    from ansible.module_utils.common.collections import ImmutableDict
    # Catch warnings from dnf, then restore to previous state
    from ansible.utils.warnings import warn_deprecations
    from dnf.yum import cli
    warn_deprecations()
    cli.logger.setLevel(cli.logging.INFO)

    # Create a fake action_base instance
    tmp = None
    task_vars = ImmutableDict()
    action_base = ActionBase(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Create a fake action_module instance

# Generated at 2022-06-13 11:21:02.052772
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a mocks around task and connection
    _task = Mock()
    _connection = Mock()
    _connection._shell = Mock()
    _connection._shell.tmpdir = '/tmp'
    _task.async_val = False
    _task._connection = _connection

    # Create a mock for display
    _display = Mock(spec=Display)

    # Create a mock for templar
    _templar = Mock()
    _templar.template.return_value = 'yum3'

    # Create a mock for AnsibleLoader
    _ansible_loader = Mock()
    _ansible_loader.module_loader.has_plugin.return_value = True

    # Create a mock for the AnsibleActionFail
    _ansible_action_fail = Mock(spec=AnsibleActionFail)

    # Instant

# Generated at 2022-06-13 11:21:02.617116
# Unit test for method run of class ActionModule
def test_ActionModule_run(): 
    pass

# Generated at 2022-06-13 11:21:07.706046
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    from ansible.module_utils._text import to_text

    # Test for case when there is no arg to compare with
    context = dict(task=dict(args=None), templar=dict())
    p = ActionModule(context=context)
    result = p.run()
    assert result['failed'] == True

# Generated at 2022-06-13 11:21:11.194548
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    unit test of AnsibleActionFail exception
    """
    action_module = ActionModule()
    try:
        action_module.run()
        raise AssertionError('Expected exception')
    except Exception as e:
        assert isinstance(e, AnsibleActionFail)
        assert str(e) == "parameters are mutually exclusive: ('use', 'use_backend')"

# Generated at 2022-06-13 11:21:15.231296
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action.VALID_BACKENDS == ('yum', 'yum4', 'dnf'), 'VALID_BACKENDS failed.'


# Generated at 2022-06-13 11:21:16.948407
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert VALID_BACKENDS == frozenset(('yum', 'yum4', 'dnf'))


# Generated at 2022-06-13 11:21:23.679560
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Import required python modules
    import ansible.plugins.action.yum as yum
    import os
    import sys
    import unittest

    # Set module and class variables
    module_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'hacking', 'test_module_compat.py')
    src_module_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'lib', 'ansible', 'modules', 'system', 'yum.py')

    if not os.path.exists(module_path):
        # if the file does not exist, create it
        fd = open(module_path, 'w')

# Generated at 2022-06-13 11:21:24.248316
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:21:50.130236
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_module = ActionModule('yum', {'use':'yum4'})
    result = test_module.run()
    assert result['failed'] == True

# Generated at 2022-06-13 11:21:51.285082
# Unit test for constructor of class ActionModule
def test_ActionModule():

    action = ActionModule()

    assert action.TRANSFERS_FILES == False

# Generated at 2022-06-13 11:21:53.690075
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(module, ActionModule)


# Generated at 2022-06-13 11:21:54.474103
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 11:21:57.204889
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # prepare test data
    data = prepare_data()
    # prepare expected result
    expected_result = expected_result_data()

    # start test
    module = ActionModule()

    result = module.run(data['tmp'], data['task_vars'])

    assert result == expected_result



# Generated at 2022-06-13 11:21:59.659926
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # FIXME:  I can't find a good way to test this, as it's dependent on multipart tasks
    # (describe how ansible task handles that)
    pass

# Generated at 2022-06-13 11:22:08.126750
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Arrange
    task_vars = dict(ansible_facts=dict(pkg_mgr='yum'))
    am = ActionModule(task=dict(args=dict(use_backend='dummy')),
                      connection=None,
                      play_context=None,
                      loader=None,
                      templar=None,
                      shared_loader_obj=None)
    am._execute_module = lambda module_name, module_args, task_vars, wrap_async : dict(failed=False, changed=True)

    # Act
    result = am.run(task_vars=task_vars)

    # Assert
    assert result == dict(failed=False, changed=True)

# Generated at 2022-06-13 11:22:14.232182
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Arrange
    tmp = None
    task_vars = {'ansible_pkg_mgr': 'yum'}
    class ActionModuleTest(ActionModule):
        def run(self, tmp=None, task_vars=None):
            return tmp, task_vars
    class AnsibleModule:
        class ArgumentSpec:
            pass
    action_module_test = ActionModuleTest(AnsibleModule(), '/tmp')

    # Act
    result = action_module_test.run(tmp, task_vars)

    # Assert
    assert result == (tmp, task_vars)

# Generated at 2022-06-13 11:22:22.499943
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import action_loader
    from ansible.playbook.task import Task
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.context_objects import Context
    from ansible.plugins.callback import CallbackBase
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group


# Generated at 2022-06-13 11:22:23.852330
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO: Find a way to unit-test this in Python 3
    pass

# Generated at 2022-06-13 11:23:21.160133
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task=dict(
            args={
                'use_backend': 'yum'
            },
            async_val=False,
            delegate_to='localhost',
            delegate_facts=True
        ),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    assert action_module.run(tmp=None, task_vars=None) == {
        'failed': True,
        'msg': "Could not detect which major revision of yum is in use, which is required to determine module backend.",
        'msg': "You should manually specify use_backend to tell the module whether to use the yum (yum3) or dnf (yum4) backend})"
    }

# Generated at 2022-06-13 11:23:24.648718
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=dict(), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 11:23:33.917466
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Constructor for class ActionModule
    '''
    act_obj = ActionModule(
        task=dict(), connection='connection', templar='templar', shared_loader_obj='shared_loader_obj')
    assert act_obj.task == dict()
    assert act_obj.connection == 'connection'
    assert act_obj.templar == 'templar'
    assert act_obj.shared_loader_obj == 'shared_loader_obj'

# Generated at 2022-06-13 11:23:43.069152
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule('mock', 'mock')

    action_module._task.delegate_to = None
    action_module._task.delegate_facts = False
    action_module._task.delegate_to = False
    action_module._task.async_val = 1
    action_module._task.args = {'name': 'test', 'enabled': 1, 'use': 'yum'}

    action_module._shared_loader_obj._plugin_classes['ansible.legacy.yum'] = 'ansible.legacy.yum'
    action_module._shared_loader_obj._plugin_classes['ansible.legacy.dnf'] = 'ansible.legacy.dnf'

    result = action_module.run("tmp", "task_vars")

# Generated at 2022-06-13 11:23:50.833673
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task

    class MockVarsModule(object):
        def __init__(self):
            pass

        def vars_from_file(self, filename):
            return {}

        def template(self, data):
            return data

    class MockTask(object):
        def __init__(self):
            self.args = None
            self.async_val = None
            self.delegate_to = None
            self.delegate_facts = None

    class MockPluginLoader(object):
        def __init__(self, plugins=None):
            self.plugins = {'yum': "foo"} if plugins is None else plugins

        def has_plugin(self, plugin):
            return self.plugins.get(plugin, False)


# Generated at 2022-06-13 11:23:54.306311
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionplugin = ActionModule(
        task=dict(), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None
    )
    assert actionplugin is not None

# Generated at 2022-06-13 11:23:54.912250
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass  # TODO

# Generated at 2022-06-13 11:24:00.691749
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    facts = am._execute_module(module_name="ansible.legacy.setup", module_args=dict(filter="ansible_pkg_mgr", gather_subset="!all"))
    display.debug("Facts %s" % facts)
    assert facts.get("ansible_facts", {}).get("ansible_pkg_mgr") == "auto"
    assert 'ansible_facts' in facts

# Generated at 2022-06-13 11:24:11.854661
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a mock class object so that it can be treated as an instance of class ActionModule
    mock_class_object = ActionModule(10, 20, 'module_name', 'module_args', 'task_vars', 'tmp', 'delegate_to', 'delegate_facts', 'timeout', 'async_val', 'poll', 'container', 'ansible_play_hosts', 'play_context', 'loader', 'shared_loader_obj', 'templar', 'connection', '_play_context', '_task', '_loader', '_connection', '_task_vars', '_templar', '_tmp')

    # Create a mock class object so that it can be treated as an instance of class Display
    mock_display_object = Display()
    mock_display_object.display = Mock(return_value=None)

    #

# Generated at 2022-06-13 11:24:14.429556
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class MockTask():
        def __init__(self):
            self.args = {}

    task = MockTask()
    action_plugin = ActionModule(task, None)


# Generated at 2022-06-13 11:25:58.834301
# Unit test for constructor of class ActionModule
def test_ActionModule():
    obj = ActionModule()
    assert isinstance(obj, ActionModule)
    assert obj._supports_check_mode == True
    assert obj._supports_async == True

# Generated at 2022-06-13 11:26:04.446626
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    var_manager = MockVariableManager()
    loader = MockDataLoader()
    display_mock = MockDisplay()
    tpm_mock = MockTaskPreparerModule()
    action_module = ActionModule(var_manager, loader, tpm_mock, display_mock)
    action_module.set_task(MockTask())

    assert action_module.run() == {}



# Generated at 2022-06-13 11:26:05.569709
# Unit test for method run of class ActionModule
def test_ActionModule_run():

  module = ActionModule()
  assert module.run() == {}

# Generated at 2022-06-13 11:26:11.716498
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Arrange
    task = dict(name='test action module')
    task['args'] = {
        'use': 'auto',
        'name': 'patch',
        'state': 'absent'
    }

    templar = dict()
    templar['template'] = dict()
    templar['template'].side_effect = ValueError('cannot determine pkg_mgr')

    # Act
    action_module = ActionModule(task, templar)

    # Assert
    assert action_module
    action_module._templar.template.assert_called_once_with('{{ansible_facts.pkg_mgr}}')

# Generated at 2022-06-13 11:26:13.014492
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, dict(), None, None, None) is not None

# Generated at 2022-06-13 11:26:14.012699
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert callable(ActionModule)



# Generated at 2022-06-13 11:26:19.125528
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action
    assert issubclass(ansible.plugins.action.ActionModule, ansible.plugins.action.ActionBase)
    assert ActionModule == ansible.plugins.action.ActionModule
    action_module = ActionModule(task=dict(action=dict(module_name='yum', module_args={})), connection='connection', play_context='play context', loader='loader', templar='templar', shared_loader_obj='shared_loader_obj')
    assert action_module

# Generated at 2022-06-13 11:26:23.426024
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Unit test for constructor of class ActionModule"""

    action_module = ActionModule(task=dict(args=dict(use_backend='')), connection=None, play_context=None, loader=None,
                                 templar=None, shared_loader_obj=None)
    assert action_module._task.args == dict()

# Generated at 2022-06-13 11:26:29.074785
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ ActionModule.run() - simple test to confirm that run() returns some result
    """

    # Test setup
    tmp = '''{
            "ansible_pkg_mgr": "yum"
        }
        '''

    task = dict(
        task = dict(args = dict(use = 'auto')),
        delegate_to = '',
        delegate_facts = ''
    )

    # Exercise the module code
    result = ActionModule.run(tmp, task)

    # Test assertions
    assert result is not None
    assert result['failed'] == False

# Generated at 2022-06-13 11:26:30.831943
# Unit test for constructor of class ActionModule
def test_ActionModule():
    dest = "test"
    action_module = ActionModule(dest, "task", {}, {}, {}, {})
    assert isinstance(action_module, ActionModule)
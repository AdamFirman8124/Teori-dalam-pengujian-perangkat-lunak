

# Generated at 2022-06-13 10:26:47.422228
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Given
    action = ActionModule()
    # When
    result = action.run()
    # Then
    assert result == {
        '_ansible_verbose_always': False,
        '_ansible_no_log': False,
        '_ansible_verbose_override': False,
        'exception': 'ansible.errors.AnsibleError'
    }

# Generated at 2022-06-13 10:26:50.806044
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test constructor of class ActionModule with arguments
    result = ActionModule(
        task=dict(args=dict(use='auto')))
    assert result is not None

# Generated at 2022-06-13 10:27:00.635242
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create connection object
    mock_connection = MockConnection()

    test_module = 'ansible.legacy.service'

    # Test Case 1: service module without async
    mock_task = MockTask()
    mock_task.async_val = 0
    mock_task.args = dict(use=test_module)

    # Test Case 1: service module with async
    mock_task = MockTask()
    mock_task.async_val = 1
    mock_task.args = dict(use=test_module)

    # Test Case 3: 'auto' module without async
    mock_task = MockTask()
    mock_task.async_val = 0
    mock_task.args = dict(use='auto')

    # Test Case 4: 'auto' module with async
    mock_task = MockTask()
    mock_

# Generated at 2022-06-13 10:27:09.583480
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test the method run of class ActionModule which is to be used to gather facts
    """
    # Tests
    # Verify the operation if different types of facts are gathered

    # fact_types = ['hardware', 'network', 'virtual', 'fips', 'identity', 'all']
    # for fact_type in fact_types:
    #     action = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())
    #     action._execute_module = MagicMock(name='_execute_module')
    #     action._execute_module.return_value = 1
    #     with pytest.raises(AnsibleActionFail) as exec_info:
    #         action.run(module_name='setup', module_args=dict(

# Generated at 2022-06-13 10:27:20.571624
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule '''
    # Creating object of class ActionModule
    action_module = ActionModule()
    # Creating object of class ActionBase
    action_base = ActionBase()
    # Creating object of class AnsibleMock
    action_base.ansible_mock = AnsibleMock()
    # Creating object of class ConnectionBase
    connection_base = ConnectionBase()
    # Creating object of class PlayContext
    play_context = PlayContext()
    # Creating object of class AnsibleOptions and setting required values

# Generated at 2022-06-13 10:27:23.413316
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    tmp=None
    task_vars=None
    a = ActionModule(tmp, task_vars)
    a.run()

# Generated at 2022-06-13 10:27:33.997577
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ test_ActionModule_run() basic testing of ActionModule.run """
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    import ansible.constants as C
    from ansible.executor.process.worker import WorkerProcess

    class MockSource(object):
        pass

    class MockOptions(object):
        connection = 'local'
        module_path = ''
        forks = 10
        become = False
        become_method = 'sudo'
        become_user = 'root'
        check = False
        diff = False
        private_key_file = None
        verbosity = 0
        module_path = None
        become_ask_pass = True

# Generated at 2022-06-13 10:27:37.629165
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert repr(ActionModule)
    assert callable(ActionModule)

# End of test_ActionModule


# Generated at 2022-06-13 10:27:38.288033
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:27:48.690861
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    play_context = {}
    play_context['remote_user'] = 'ansible'
    play_context['connection'] = 'local'
    play_context['port'] = '3390'
    play_context['remote_addr'] = None
    play_context['password'] = None
    play_context['private_key_file'] = None
    play_context['timeout'] = 10
    play_context['shell'] = None
    play_context['executable'] = None
    play_context['become_method'] = 'sudo'
    play_context['become_user'] = 'root'
    play_context['become'] = True
    play_context['become_password'] = None
    play_context['become_exe'] = None
    play_context['become_flags'] = '-H'
    play

# Generated at 2022-06-13 10:28:04.408043
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mock_task_vars = {'ansible_facts': {'service_mgr': 'systemd'}}
    mock_task_args = {'name': 'cron', 'state': 'started', 'use': 'auto'}
    am = ActionModule(None, mock_task_vars)
    am.task_vars = mock_task_vars
    am._task.args = mock_task_args
    result = am.run()

if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:28:15.801669
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import mock
    import json

    test_obj = ActionModule(
        task=mock.MagicMock(), connection=mock.MagicMock(),
        play_context=mock.MagicMock(), loader=mock.MagicMock(),
        templar=mock.MagicMock(), shared_loader_obj=mock.MagicMock())
    test_obj._supports_check_mode = False
    test_obj._supports_async = False
    test_obj._task.args = {
        'name': "test",
        'state': "test",
        'pattern': "test",
        'runlevel': "test",
        'sleep': "test",
        'arguments': "test",
        'args': "test"
    }


# Generated at 2022-06-13 10:28:24.247583
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import sys
    import collections

    task_vars = dict(
        ansible_ssh_user='user',
        ansible_ssh_pass='pass',
        ansible_ssh_port=22,
        ansible_sudo_pass='sudo_pass',
    )
    task_vars.update(
        collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(dict))))


# Generated at 2022-06-13 10:28:34.320784
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = __import__('ansible.plugins.action.service').get_action_class('service')
    action_module = action_module()
    action_module.test_module = True
    action_module.set_runner(object())
    action_module.set_loader(object())
    action_module.set_options(object())
    action_module._task = object()
    action_module._task.args = {'name': 'sshd'}

    result = action_module.run()
    return result

# Generated at 2022-06-13 10:28:37.637986
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class MyActionModule(ActionModule):
        pass
    module = MyActionModule(connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module is not None

# Generated at 2022-06-13 10:28:45.644998
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import pytest
    from ansible.playbook.task import Task

    # instantiate a fake Task object with fake Task.args asked by the ActionModule
    task_args = {
        'name': 'fake name',
        'state': 'fake state',
        'use': 'fake use',
    }
    task = Task()
    task.args = task_args

    # temporary disable the test of actual loader
    # this test should be re-enabled once we have a mocked loader
    # (And AnsibleModule.load_resources should be mocked in the test)
    #
    # Here use a fake loader to test ActionModule.run()
    #
    with pytest.raises(ImportError):
        from ansible_collections.ansible.community.plugins.loader import action_loader

# Generated at 2022-06-13 10:28:54.875416
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit tests for the method `module.ActionModule.run`
    """

    # dummy task object to test
    class Task:
        """ Dummy task object to test the module.ActionModule.run method
        """

        def __init__(self):
            self.args = {
                'use': 'auto', 'name': 'sample-service', 'state': 'stopped'
            }
            self.module_defaults = {
                'systemd': {'pattern': 'sample-service', 'runlevel': 'default'}
            }
            self.module_name = 'sample-module-name'
            self.executor_config = {}

        def _get_action(self):
            """ Returns name of task action
            """
            return 'test_' + self.module_name


# Generated at 2022-06-13 10:29:02.760116
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    original_data = dict(
        _task=dict(
            args=dict(
                use='auto',
            )
        ),
    )
    original_data['_task'].update(**original_data)
    instance = ActionModule(original_data['_task'], dict(connection='local'))
    fake_functions = dict(
        _execute_module=lambda *args, **kwargs: dict(ansible_facts=dict(ansible_service_mgr='auto')),
        _remove_tmp_path=lambda *args, **kwargs: None,
    )
    instance.__dict__.update(**fake_functions)
    result = instance.run(tmp=None, task_vars=dict())

# Generated at 2022-06-13 10:29:03.860189
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO
    pass

# Generated at 2022-06-13 10:29:12.701890
# Unit test for constructor of class ActionModule
def test_ActionModule():
  '''
  Unit test for constructor of class ActionModule
  '''
  module = ActionModule(None, None)
  assert module.TRANSFERS_FILES is False
  assert module.UNUSED_PARAMS == {
        'systemd': ['pattern', 'runlevel', 'sleep', 'arguments', 'args'],
    }
  assert module.BUILTIN_SVC_MGR_MODULES == set(['openwrt_init', 'service', 'systemd', 'sysvinit'])

# Generated at 2022-06-13 10:29:31.793151
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    This function is used to test method run of class ActionModule.
    """
    # Define test data
    task_vars = {}
    tmp = None
    module = "systemd"
    new_module_args = { 'name': "test", 'state': "started", "enabled": "yes" }
    module_name = "ansible.legacy.%s" % module
    module_obj = "ansible.legacy.%s" % module

    # Create test object
    action_module_obj = ActionModule()

    # Run test method
    action_module_obj.run(tmp, task_vars)

# Generated at 2022-06-13 10:29:44.767096
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(
            async_val=0,
            args={},
            async_jid=None,
            becomes=False,
            delegates=None,
            delegate_facts=None,
            delegate_to=None,
            environment=None,
            no_log=False,
            poll=None,
            run_once=False,
            tags=[],
            verbosity=0
        ),
        connection=dict(),
        play_context=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=dict(),
        final_dump=dict(),
        _dependency_calculator=None,
        add_cleanup_task=None
    )

    assert module.TRANSFERS_FILES is False


# Generated at 2022-06-13 10:29:45.411215
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:29:46.255448
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    print(module)

# Generated at 2022-06-13 10:29:54.115581
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    service = ActionModule()
    assert not service._shared_loader_obj.module_loader.has_plugin('openwrt_init')
    service._shared_loader_obj.module_loader.find_plugin('openwrt_init')
    assert service._shared_loader_obj.module_loader.has_plugin('ansible.legacy.openwrt_init')
    assert not service._shared_loader_obj.module_loader.has_plugin('ops')
    service._shared_loader_obj.module_loader.find_plugin('ops')
    assert service._shared_loader_obj.module_loader.has_plugin('ansible.legacy.ops')

# Generated at 2022-06-13 10:30:06.359400
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager

    context = PlayContext()
    result = TaskResult(host=None, task=None, return_data=None)
    manager = TaskQueueManager(None, None, None, None, context, None, None)
    manager._shell = None
    manager._play_context = context

    action = ActionModule(task=None, connection=manager, play_context=context, loader=None, templar=None, shared_loader_obj=None)

    new_connection = action.connection
    assert new_connection._shell is None
    assert new_connection._play_context == context
    assert new_connection._new_stdin is None

# Generated at 2022-06-13 10:30:15.030448
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule('ansible.legacy.service', dict(name='name', args='args'), 'play', 'play_ds', 'task', 'task_ds')
    assert(action.name == 'name')
    assert(action.args == 'args')
    assert(action.play == 'play')
    assert(action.play_ds == 'play_ds')
    assert(action.task == 'task')
    assert(action.task_ds == 'task_ds')
    return

# Generated at 2022-06-13 10:30:25.595472
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mock_manager, mock_loader, mock_display, patch_action_base, patch_display = ActionBase._patch_action_base()

    # Create instance of action module
    action_plugin = ActionModule(
        task=dict(args=dict(use='openwrt_init', name='foo', state='started')),
        connection=None,
        play_context=dict(),
        loader=mock_loader,
        templar=None,
        shared_loader_obj=None
    )

    # Run method under test
    result = action_plugin.run(tmp=None, task_vars=None)

    # Assert we got expected result
    assert result == dict(
        _ansible_no_log=False,
        ansible_facts=dict(),
        ansible_modules=dict()
    )

    #

# Generated at 2022-06-13 10:30:35.096787
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Setup test input
    ##################
    task_args = {
        'name': 'test',
        'state': 'started',
        'daemon_reload': True
    }
    module_args = {
        'use': 'auto',
        'name': 'test',
        'state': 'started',
        'daemon_reload': True
    }

    # create object instance
    ########################
    action_module = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    # call run() - this should always return a dictionary with the keys "failed" and "changed"
    ############################################################################################

# Generated at 2022-06-13 10:30:36.285640
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for method ActionModule.run"""
    module = ActionModule()

# Generated at 2022-06-13 10:31:12.029269
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import imp
    import os
    import sys
    import unittest

    # save the initial cwd
    saved_path = os.getcwd()

    sys.path.insert(0, os.path.abspath('lib'))

    class TestActionModuleAddition(unittest.TestCase):

        def setUp(self):
            self.action = imp.load_source('library.service', 'lib/ansible/modules/legacy/system/service.py').ActionModule()

        def tearDown(self):
            self.action = None

        # test method for constructor of class ActionModule
        def test_constructor(self):
            self.assertIsNotNone(self.action)

    def cleanup():
        # change the path back to the original
        os.chdir(saved_path)

# Generated at 2022-06-13 10:31:19.894426
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock_task = {
        'args': {
            'use': 'auto',
        }
    }

    action_module = ActionModule(mock_task, {'tmp': '/tmp', 'task_vars': {}}, mock_task.get('args'))
    assert action_module.run() == {
        'changed': False,
        'failed': True,
        'module_stderr': 'Exception from Service Module\n',
        'module_stdout': '',
        'msg': 'Could not detect which service manager to use. Try gathering facts or setting the "use" option.'
    }

# Generated at 2022-06-13 10:31:28.823589
# Unit test for constructor of class ActionModule
def test_ActionModule():
    sample_task = {
        "args": {
            "use": "auto",
            "name": "foo"
        }
    }
    sample_task.update({"delegate_to": "test"})
    sample_load = {
        "transfers": "smart",
        "vault_id": "default@prompt"
    }

# Generated at 2022-06-13 10:31:39.519246
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import platform
    from ansible.utils.context_objects import AnsibleContext
    from ansible.module_utils.six.moves import StringIO
    from ansible.errors import AnsibleError
    from ansible.module_utils.common.json import json
    from ansible.module_utils.common.text.strings import xml_to_dict
    from ansible.module_utils.network.ios.ios import load_config
    from ansible.module_utils.network.ios.ios import ios_argument_spec
    from ansible.module_utils.network.ios.ios import get_config
    from ansible.module_utils.network.ios.ios import get_defaults_flag
    from ansible.module_utils.network.ios.ios import get_connection

# Generated at 2022-06-13 10:31:47.089352
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    action_module._task.args = {'use': 'auto'}
    tmp = '/Users/test/test_dir'
    task_vars = {
        'ansible_facts': {'service_mgr': 'auto'}
    }

    action_module._shared_loader_obj = 'loader_obj'
    action_module._shared_loader_obj.module_loader = 'module_loader'
    action_module._shared_loader_obj.module_loader.has_plugin = MagicMock(return_value='module')
    action_module._execute_module = MagicMock(return_value='module_return_value')
    action_module._shared_loader_obj.module_loader.find_plugin_with_context = MagicMock(return_value='context')
    action_

# Generated at 2022-06-13 10:31:48.089109
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None)

# Generated at 2022-06-13 10:31:51.537422
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert test_module._supports_async is True
    assert test_module._supports_check_mode is True
    assert test_module._supports_async is True
    assert test_module._shared_loader_obj is shared_loader_obj

# Generated at 2022-06-13 10:31:52.341854
# Unit test for constructor of class ActionModule
def test_ActionModule():
	pass

# Generated at 2022-06-13 10:31:55.191595
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert((type(m) is ActionModule))

# Generated at 2022-06-13 10:32:10.016732
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = {"action": {"__ansible_module__": "service"},
            "async": 15,
            "async_val": "no",
            "delegate_to": "127.0.0.0",
            "register": "test_module",
            "retries": 5,
            "until": "test_until",
            "delay": "test_delay",
            "first_available_file": ["test_file1", "test_file2"],
            "loop_control": "test_control",
            "loop": "test_loop",
            "tags": ["test_tag"]}

# Generated at 2022-06-13 10:33:10.293626
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module_object = ActionModule(None, None, None, None, None, None)
    assert isinstance(action_module_object, ActionModule)

# Generated at 2022-06-13 10:33:13.110294
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # try:
    assert True
    # except Exception:
    #     print('Test failed')
    # else:
    #     print('Test succeeded')

# Test call of run
test_ActionModule_run()

# Generated at 2022-06-13 10:33:23.118378
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )
    # Verify instance
    assert isinstance(module, ActionModule)

    # Check members
    assert hasattr(module, "_connection")
    assert hasattr(module, "_task")
    assert hasattr(module, "_play_context")
    assert hasattr(module, "_loader")
    assert hasattr(module, "_templar")
    assert hasattr(module, "_shared_loader_obj")
    assert hasattr(module, "_display")
    assert hasattr(module, "_supports_async")
    assert hasattr(module, "_supports_check_mode")

# Generated at 2022-06-13 10:33:30.081744
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test for constructor
    am = ActionModule(loader=None, action=None, task=None, connection=None, play_context=None, loader_cache=None, shared_loader_obj=None, final_q=None)
    assert am._connection is None
    assert am._loader is None
    assert am._loader_cache is None
    assert am._task is None
    assert am._play_context is None
    assert am._shared_loader_obj is None
    assert am.noop_values is None
    assert am.noop_on_check(tmp=None, task_vars=None)
    assert am.ACTION_WARNINGS == {}
    assert am.ACTION_COMMAND_WARNINGS == {}
    assert am.ACTION_MSGS == {}


# Generated at 2022-06-13 10:33:40.193355
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os
    import shutil

    sys.path.insert(0, os.path.abspath(os.path.realpath(os.path.dirname(__file__))))

    from ansible.module_utils.six import StringIO
    from ansible.module_utils.network.common.utils import prepare_config
    from ansible.module_utils.connection import Connection
    from ansible.plugins.action.service import ActionModule
    from ansible.plugins.loader import shared_loader_obj

    fake_loader = shared_loader_obj.plugin_loader

    fake_loader.add_directory(os.path.abspath(os.path.realpath(os.path.dirname(__file__))))
    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-13 10:33:46.705121
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # We must construct a task for the unit test framework to execute
    from ansible.playbook.task import Task
    t = Task()
    t.args = {'use': 'auto', 'name': 'test'}
    m = ActionModule(t, fake_shell=None)
    assert isinstance(m, ActionModule)

# Generated at 2022-06-13 10:33:57.862423
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    my_action_module = ActionModule()
    my_action_module.__dict__['_shared_loader_obj'] =  {}
    my_action_module.__dict__['_task'] = {}
    my_action_module.__dict__['_task'].__dict__['args'] = {
        "name": "foo",
        "state": "present"
    }
    my_action_module.__dict__['_task'].__dict__['async_val'] = None
    my_action_module.__dict__['_task'].__dict__['collections'] = None
    my_action_module.__dict__['_task'].__dict__['module_defaults'] = {}
    my_action_module.__dict__['_task'].__dict__['delegate_to'] = None


# Generated at 2022-06-13 10:34:09.478946
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Check with no arguments
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module._task is None
    assert action_module._connection is None
    assert action_module._play_context is None
    assert action_module._loader is None
    assert action_module._templar is None
    assert action_module._shared_loader_obj is None
    assert action_module._supports_check_mode is True
    assert action_module._supports_async is True

# Generated at 2022-06-13 10:34:20.007569
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Adding tests for run method of class ActionModule
    #
    # test with
    # service type is auto
    module_args = {
        'name': 'sshd',
        'state': 'started',
        'enabled': True,
        'use': 'auto'
    }
    set_module_args(module_args)
    facts = dict(ansible_service_mgr='systemd')
    my_action = ActionModule(task_vars=dict(ansible_facts=facts))
    my_action.run()
    assert my_action.action_result.get('module_name') == 'ansible.legacy.service'

    module_args = {
        'name': 'sshd',
        'state': 'started',
        'enabled': True,
        'use': 'auto'
    }
   

# Generated at 2022-06-13 10:34:29.952580
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    global sys
    basetestcase.shutil=shutil
    basetestcase.datetime=datetime
    sys = Mock()
    sys.stdin = Mock()
    sys.stdout = Mock()
    sys.exit = Mock()
    _task_vars = dict()
    _result = dict()
    _tmp = dict()


    _action = ActionModule('/root/action_plugins/test_action.py', load_args_from_file=False)
    _action._supports_check_mode = True
    _action._supports_async = True

    _action._shared_loader_obj.module_loader.has_plugin = Mock(return_value=True)
    _action._execute_module = Mock(return_value=dict())

    _action.run(_tmp, _task_vars)

# Generated at 2022-06-13 10:36:30.714714
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    
    tmp = '/Users/rashad/Downloads/ansible-playbook/test/test'
    module = 'ansible.legacy.service'
    ansible_facts = {}

    svc = ActionModule(loader=None, task=None, connection=None)
    
    
    result = svc.run()
    print(result)

if __name__ == "__main__":
    test_ActionModule_run()

# Generated at 2022-06-13 10:36:31.600229
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule()
    assert (m)

# Generated at 2022-06-13 10:36:32.443770
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:36:36.168175
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert am.__class__.__name__ == 'ActionModule'
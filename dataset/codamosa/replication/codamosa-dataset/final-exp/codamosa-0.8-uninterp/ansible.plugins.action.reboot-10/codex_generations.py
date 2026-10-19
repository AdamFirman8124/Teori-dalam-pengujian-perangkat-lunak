

# Generated at 2022-06-13 10:27:14.022547
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    my_ActionModule = ActionModule()
    assert my_ActionModule.run() == 0

# Generated at 2022-06-13 10:27:17.903844
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
  initial_boot_time = "2010-07-02T04:50:08"
  ActionModule_obj = ActionModule(dict(connection='connection'), dict(name='name'), 'task', 'play_context', loader=None, templar=None, shared_loader_obj=None)
  ActionModule_obj.check_boot_time('test', initial_boot_time)


# Generated at 2022-06-13 10:27:28.212598
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    # test case:
    #   output:
    #       - description: 'something'
    #       - returned: failure
    #       - value: 'something'
    #   os_family:
    #       - description: 'something'
    #       - returned: success
    #       - value: 'something'
    #   rc:
    #       - description: 'something'
    #       - returned: success
    #       - value: 0
    #   stdout:
    #       - description: 'something'
    #       - returned: success
    #       - value: 'something'
    #   changed:
    #       - description: 'something'
    #       - returned: success
    #       - value: True

    # Build mock variables
    task = MagicMock()
    connection = MagicMock()
    task

# Generated at 2022-06-13 10:27:29.808406
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    # ActionModule has no dummy
    assert False


# Generated at 2022-06-13 10:27:36.249338
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    ad = ActionModule({}, {'action': 'reboot'})
    ad.DEPRECATED_ARGS = {}
    ad._task = {'args': {
        'connect_timeout': 10,
    }}

    class FakeTimedOutException(Exception):
        pass

    def fake_action(**kwargs):
        raise FakeTimedOutException()

    ad.do_until_success_or_timeout(fake_action, action_desc='test action desc', reboot_timeout=10, distribution='test_distribution')



# Generated at 2022-06-13 10:27:38.990836
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    module = AnsibleActionModule()
    module.get_system_boot_time('ubuntu')


# Generated at 2022-06-13 10:27:49.314119
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ar1 = ActionModule(load_strategy="network_only")
    ad = {}
    task_vars = {}
    result = ar1.run(tmp=None, task_vars=task_vars)
    assert result == {'changed': False, 'elapsed': 0, 'rebooted': False, 'failed': True, 'msg': 'Running ' + ar1._task.action + ' with local connection would reboot the control node.'}

    ar2 = ActionModule(load_strategy="delegated")
    result = ar2.run(tmp=None, task_vars=task_vars)
    assert result == {'rebooted': True, 'changed': True, 'elapsed': 0}

    ar3 = ActionModule(load_strategy="yes")

# Generated at 2022-06-13 10:27:51.634348
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    module = ActionModule(None, None, None)
    try:
        module.get_system_boot_time(None)
    except Exception as e:
        assert isinstance(e, NotImplementedError)


# Generated at 2022-06-13 10:27:52.420007
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    assert 1==1

# Generated at 2022-06-13 10:27:54.728039
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    print(action_module.deprecated_args())



# Generated at 2022-06-13 10:28:52.695097
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup
    action_module = ActionModule('notify', dict(task_vars={'this_is_a': 'variables'}, connection='local', play_context=dict(check_mode=False)), lambda: dict(diff=dict()))
    action_module._connection.transport = 'local'
    action_module._task.action = 'reboot'
    action_module.post_reboot_delay = 2
    expected_result = dict(changed=True, elapsed=0, rebooted=True)

    # Test
    action_module.run(tmp='', task_vars={})

    # Assert
    assert expected_result == action_module._result


# Generated at 2022-06-13 10:29:03.270708
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    from ansible.errors import AnsibleError
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY3
    from units.mock.procenv import swap_stdin_and_arguments, patch_getoutput
    from units.modules.utils import set_module_args, AnsibleExitJson, AnsibleFailJson
    from system_timer import SystemTimer
    import shlex
    import os
    import tempfile
    import pytest

    FAKE_DISTRIBUTION = 'DEBIAN'


# Generated at 2022-06-13 10:29:07.010163
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    module = ActionModule(task=MagicMock(), connection=MagicMock(), play_context=MagicMock())
    result = module.validate_reboot(
        distribution=None,
        original_connection_timeout=None,
        action_kwargs=None
    )
    assert result.keys() == {
       'rebooted',
       'changed'
    }



# Generated at 2022-06-13 10:29:12.208891
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    action_module = ActionModule.ActionModule(play_context=play_context, new_stdin=None)
    # Test if the method raises a TimedOutException when the action times out
    with pytest.raises(TimedOutException) as excinfo:
        action_module.do_until_success_or_timeout(action=action_module.check_boot_time,
                                                  action_desc="last boot time check",
                                                  reboot_timeout=1, distribution="", action_kwargs={}
                                                 )
    assert 'Timed out' in str(excinfo.value)

# Generated at 2022-06-13 10:29:20.933077
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    # Create an instance of class ActionModule with default parameter values
    action_module = ActionModule()

    # Create an instance of class StubConnectionForActionModule
    stub_connection = StubConnectionForActionModule()

    # Assign the stub connection to the connection property of class ActionModule
    action_module.connection = stub_connection

    # Create an instance of class StubPlayContextForActionModule
    stub_play_context = StubPlayContextForActionModule()

    # Assign the stub play context to the play_context property of class ActionModule
    action_module.play_context = stub_play_context

    # Create an instance of class StubTaskForActionModule
    stub_task = StubTaskForActionModule()

    # Assign the stub task to the task property of class ActionModule
    action_module.task = stub_task

    # Return the stub task when TaskLoader

# Generated at 2022-06-13 10:29:29.435568
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    module_name = 'reboot'
    action_name = 'test_action'
    defaults = {}
    connection_info = {}
    module_kwargs = {}
    task = Task(action=action_name, module=module_name, defaults=defaults, connection_info=connection_info, module_kwargs=module_kwargs)
    task.args = {}
    action_obj = ActionModule(task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    distribution = 'ubuntu'
    action_kwargs = {'previous_boot_time': '1'}

# Generated at 2022-06-13 10:29:36.258377
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    module = AnsibleModule(
        argument_spec=dict()
    )
    set_module_args(dict(
        action='reboot',
        _ansible_check_mode=True,
        _ansible_debug=True
    ))

    am = ActionModule(module=module, task_vars=dict())
    am.check_boot_time(distribution='foo')


# Generated at 2022-06-13 10:29:45.280365
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    mock_self = Mock()
    mock_self.DEFAULT_SUDOABLE = True
    mock_self._task = Mock()
    
    mock_distribution = Mock()
    mock_distribution.value = "test_distribution"

    mock_self.run_test_command(mock_distribution)

    mock_self._low_level_execute_command.assert_called_with("test_command", mock_self.DEFAULT_SUDOABLE)


# Generated at 2022-06-13 10:29:53.905167
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    # Arrange
    action_module = ActionModule()
    task = Mock()
    task.action = "mock"
    action_module._task = task
    action_module.DEFAULT_SUDOABLE = True
    command_result = {
        "rc": 0,
        "stdout": "Tue 2019-09-10 20:25:09 UTC",
        "stderr": ""
    }
    boot_time_command = "/usr/bin/who -b"
    action_module._low_level_execute_command = Mock()
    action_module._low_level_execute_command.return_value = command_result
    action_module.DEFAULT_BOOT_TIME_COMMAND = boot_time_command
    distribution = "Mock"
    # Act
    result = action_module.get_system_

# Generated at 2022-06-13 10:29:56.892252
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    action_module = ActionModule()
    # Validating a single reboot
    distribution = 'DEBIAN'
    original_connection_timeout = None
    action_kwargs={'previous_boot_time': 'test_previous_boot_time'}
    assert action_module.validate_reboot(distribution, original_connection_timeout, action_kwargs) == {}



# Generated at 2022-06-13 10:31:33.799961
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    pass

# Generated at 2022-06-13 10:31:43.435111
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    display = Display()
    def mocked_get_distribution(task_vars):
        return 'redhat'

    module = ActionModule(
        task=Mock(),
        connection=Mock(),
        play_context=Mock(),
        loader=Mock(),
        templar=Mock(),
        shared_loader_obj=Mock()
    )
    module._low_level_execute_command = Mock(return_value=dict(rc=0, stdout="boot time"))
    module.get_distribution = mocked_get_distribution
    display.warning = Mock()

    args = {'reboot_timeout_sec': 3, 'timestamp': "secret", 'connect_timeout': 20}
    module._task.args = args
    module.deprecated_args()
    assert display.warning.call_count == 2

# Generated at 2022-06-13 10:31:53.867782
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    # Create a mock task to provide an _task to the action plugin
    mock_task = mock.MagicMock()
    mock_task.action = "mock_action"

    # Create an instance of the action plugin
    action_instance = ActionModule(mock_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Create a mock distribution to provide context to the get_shutdown_command_args function
    mock_distribution = "mock_distribution"

    # Call get_shutdown_command_args to test it
    shutdown_command_args = action_instance.get_shutdown_command_args(mock_distribution)

    # Test that the shutdown command args are actually the default args
    assert shutdown_command_args == action_instance.DEFAULT

# Generated at 2022-06-13 10:31:55.466250
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    action_module = ActionModule()
    assert action_module != None


# Generated at 2022-06-13 10:32:05.053660
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    import time

    class MockDistribution():
        BOOT_TIME_COMMANDS = {}

    class MockActionModule():
        post_reboot_delay = 0

    class MockTask():
        args = {}

    class Mocklow_level_execute_command():
        def __init__(self):
            self.stdout = 'boot time'

    class MockConnection():
        def __init__(self):
            self.transport = 'SSH'

        def get_option(self):
            return 1000

        def set_option(self):
            pass

        def reset(self):
            pass

    class MockTime():
        def __init__(self):
            self.max_end_time = 0

        def sleep(self, sleep_time):
            time.sleep(sleep_time)


# Generated at 2022-06-13 10:32:08.288162
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    # setup
    task_vars = Dict()
    action_module = ActionModuleMock()
    distribution = "unknown"
    # execution
    with pytest.raises(AnsibleError):
        action_module.get_shutdown_command(task_vars, distribution)



# Generated at 2022-06-13 10:32:12.707662
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	# Setup
	os.environ['ANSIBLE_LIBRARY'] = '../../../../lib/ansible/modules/system/'
	action_module = ActionModule('reboot')
	action_module.setup()

	# Test
	return_value = action_module.run()
	print(return_value)

	# Tear down
	action_module.teardown()
	del os.environ['ANSIBLE_LIBRARY']

# Generated at 2022-06-13 10:32:20.658034
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    """
    test_get_distribution() - test the get_distribution method of class ActionModule
    """
    import os

    from ansible.module_utils.network.common.utils import to_list

    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, MagicMock

    # create an instance of the Options class and execute the
    # set_action() method so that it creates the self.action
    # data structure for the 'reboot' action
    options = Options()
    options.action = {}
    options.action['reboot'] = dict()

    # create an instance of the AnsibleModule to load the reboot
    # module into the test

# Generated at 2022-06-13 10:32:21.814276
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    action = ActionModule()
    # Do nothing as it's used directly by the action module

# Generated at 2022-06-13 10:32:29.027142
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    # Create Mock object to test method perform_reboot of class ActionModule
    mock_ActionModule_obj = Mock()

    # Create mock object for task_vars
    mock_task_vars = {}

    # Create mock object for distribution
    mock_distribution = 'Red Hat Enterprise Linux Server release 7.0 (Maipo)'

    # Setup mock return value for method get_shutdown_command()
    mock_ActionModule_obj.get_shutdown_command.return_value = '/sbin/shutdown'

    # Setup mock return value for method get_shutdown_command_args()
    mock_ActionModule_obj.get_shutdown_command_args.return_value = '-r +1 "Ansible reboot initiated"'

    # Run method perform_reboot of class ActionModule and make assertions
    # Setup mock return value for method _

# Generated at 2022-06-13 10:33:41.624042
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    result = None
    result = check_deprecated_args(ActionModule())
    assert result is None


# Generated at 2022-06-13 10:33:49.746214
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    """
    Check the method run_test_command of class ActionModule.

    """
    # environment
    distribution = "linux"
    action_kwargs = {}

    # test
    module = AnsibleModule(**{})
    am = ActionModule(module, "/path/to/action", "/tmp/ansible")
    am.run_test_command(distribution, **action_kwargs)


# Generated at 2022-06-13 10:33:58.347963
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    # Mock the distribution
    distributions = (
        'unknown',
        'centos',
        'debian',
        'freebsd',
        'openbsd',
        'redhat',
        'scientific',
        'sles',
        'solaris',
        'ubuntu',
    )


# Generated at 2022-06-13 10:33:59.819290
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    pass


# Generated at 2022-06-13 10:34:13.245586
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    #
    # [iinno-rhel-01 ~]$ uname -a
    # Linux iinno-rhel-01 3.10.0-693.el7.x86_64 #1 SMP Wed Jul 26 19:06:34 EDT 2017 x86_64 x86_64 x86_64 GNU/Linux
    #
    print("")
    print("test_ActionModule_get_shutdown_command")
    test_task_vars = dict(
        ansible_distribution='Red Hat Enterprise Linux',
        ansible_distribution_major_version='7',
        ansible_distribution_version='7.4'
    )
    test_module = ActionModule(dict(
        pattern='shutdown',
        paths=['/sbin'],
        file_type='any'
    ))
    test_

# Generated at 2022-06-13 10:34:14.476701
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    pass


# Generated at 2022-06-13 10:34:20.959577
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
	# arrange
	argument = {}
	am = ActionModule(argument, None)
	distribution = 'distribution'
	# arrange
	am._get_value_from_facts = MagicMock(return_value='whee')
	am._low_level_execute_command = MagicMock(return_value='sometimes')
	am.get_system_boot_time = MagicMock(return_value='whee')
	am.get_system_boot_time.assert_called_once_with(distribution)


# Generated at 2022-06-13 10:34:28.873068
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create instance
    module = AnsibleModule('reboot')
    action = ActionModule()
    action.set_task(module)

    # Run method
    result = action.run(None, None)

    # Verify results
    assert isinstance(result, dict)
    assert 'changed' in result and isinstance(result['changed'], bool)
    assert 'elapsed' in result and isinstance(result['elapsed'], int)
    assert 'rebooted' in result and isinstance(result['rebooted'], bool)
    assert 'failed' in result and isinstance(result['failed'], bool) or 'msg' in result and isinstance(result['msg'], str)



# Generated at 2022-06-13 10:34:35.631793
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest
    import tempfile

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, Mock, MagicMock
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.action import ActionBase
    from ansible.utils.hashing import checksum
    from ansible.module_utils.six import StringIO
    from ansible.vars.hostvars import HostVars

    # for test_action_task_vars_missing
    mock_tqm = None
    mock_loader

# Generated at 2022-06-13 10:34:36.679240
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    """Test deprecated_args method"""
    pass

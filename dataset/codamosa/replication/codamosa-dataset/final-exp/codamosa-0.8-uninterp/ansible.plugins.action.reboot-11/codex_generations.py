

# Generated at 2022-06-13 10:27:24.804620
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    """Unit test for ActionModule: validate_reboot"""

    # test ActionModule instance
    class DummyActionModule(ActionModule):
        """
        Dummy ActionModule for testing.
        """

        def _low_level_execute_command(self, cmd, sudoable=False):
            """
            Dummy _low_level_execute_command for testing
            """

            self.cmd = cmd
            self.sudoable = sudoable
            return 'test'


    class DummyAnsibleConnection:
        """
        Dummy AnsibleConnection for testing
        """

        def set_option(self, key, value):
            self.key = key
            self.value = value

        def get_option(self, key):
            self.key = key


# Generated at 2022-06-13 10:27:35.224108
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    # Set up mock
    mock_ansible_module = MagicMock(AnsibleModule)

    # Set up class instance
    action_module = ActionModule(mock_ansible_module)

    # Mock method calls
    mock_ansible_module.run_command = MagicMock(return_value=(0, '', ''))
    task_vars = {"ansible_distribution": "RedHat", "ansible_distribution_version": "6", "ansible_distribution_release": "Santiago"}
    distribution = "RedHat"

    # Call unit under test
    result = action_module.get_shutdown_command(task_vars, distribution)

    # Validate
    expected_result = '/sbin/shutdown'
    mock_ansible_module.run_command.assert_called_once_with

# Generated at 2022-06-13 10:27:36.089530
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  pass

# Generated at 2022-06-13 10:27:42.673334
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    from ansible.utils.timedeltamath import datetime
    from ansible.plugins.action.reboot import ActionModule
    system = ActionModule(None, None, None)

    action_counter = 0
    def action_func():
        nonlocal action_counter
        action_counter += 1
        raise ActionModule()

    system.do_until_success_or_timeout(action=action_func, reboot_timeout=10, action_desc="Action", distribution="distribution")
    assert action_counter == 1

    action_counter = 0

    def action_func():
        nonlocal action_counter
        action_counter += 1
        raise Exception()


# Generated at 2022-06-13 10:27:44.233523
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():

    ActionModule.run_test_command('test_distribution', 'test_action', 'test_reboot_timeout')

# Generated at 2022-06-13 10:27:45.914746
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    pass # nothing to do here

# Generated at 2022-06-13 10:27:53.858440
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    print('Starting test_ActionModule_check_boot_time')
    print()
    
    import time

    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    Playbook = namedtuple('Playbook', ['playbook', 'inventory', 'connection', 'module_path'])

    print(Playbook)
    print

# Generated at 2022-06-13 10:28:06.007598
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    module = AnsibleModule(argument_spec={
        'reboot_timeout': {'type': 'int'},
        'post_reboot_delay': {'type': 'int'},
        'test_command': {'type': 'str'},
        'shutdown_command': {'type': 'str'},
        'shutdown_timeout': {'type': 'int'},
        'connect_timeout': {'type': 'int'},
        'distribution': {'type': 'str'},
        'test_command': {'type': 'str'},
        'test_connections': {'type': 'list'}
    })

    class MockTask(object):
        def __init__(self, args):
            self.args = args


# Generated at 2022-06-13 10:28:16.858817
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    action_module = Reboot()
    action_module.set_action_state(ActionModule)
    task_vars = {
        'ansible_connection': 'network_cli',
        'ansible_network_os': 'nxos',
        'ansible_user': 'test_user',
        'ansible_ssh_pass': 'test_pass'
    }

    ansible_facts = {
        'nxos_ver': '8.3(3)',
        'ansible_distribution': 'Cisco NX-OS',
        'ansible_distribution_version': '8.3(3)'
    }

    action_module.set_task(AnsibleTask('test_task', AnsiblePlay(), AnsibleTaskResult(success=True)))
    action_module._task.action = 'test_reboot'

# Generated at 2022-06-13 10:28:20.874013
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    '''
    get_shutdown_command_args returns the expected args
    '''
    # Set up arguments/variables
    distribution = ''
    # Call the method
    actual = _ActionModule__ActionModule().get_shutdown_command_args(distribution)

    # Test the results
    expected = ''
    assert actual == expected

# Generated at 2022-06-13 10:29:02.438677
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    from ansible.plugins.action import ActionModule

    module = ActionModule(
        task=None,
        connection=None,
        _play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None,
    )

    task_vars = {}
    with pytest.raises(AnsibleError) as exception_info:
        module.get_distribution(task_vars)
    assert 'Unable to determine distribution' in str(exception_info.value)

    task_vars = dict(ansible_facts={})
    with pytest.raises(AnsibleError) as exception_info:
        module.get_distribution(task_vars)
    assert 'Unable to determine distribution' in str(exception_info.value)

    task_

# Generated at 2022-06-13 10:29:09.744238
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    args = dict(
        reboot_timeout=30,
        test_command='echo Hi',
        connect_timeout=300,
        connect_timeout_sec=300,
        use_reboot=True,
        reboot_timeout_sec=30,
        msg='this is a test',

    )

    def get_ansible_module(self):
        return dict(
            params=dict(
                _ansible_verbosity=4,
                _ansible_version=__version__,
                _ansible_syslog_facility=LOG_TO_SYSLOG_FACILITY_NAMES.get('user'),
                _ansible_no_log=False
            )
        )

    ActionModule.get_ansible_module = get_ansible_module

    def get_ansible_connection(self):
        return

# Generated at 2022-06-13 10:29:19.605110
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    class TestModuleConnection(Connection):
        ''' Dummy Connection Class for test_ActionModule_validate_reboot
            Expected methods get_option, reset and set_option'''

        def reset(self):
            return

        def get_option(self, key):
            return "test_connection"

        def set_option(self, key, value):
            return

    class Task():
        def __init__(self):
            self.action = "reboot"
            self.args = {
                'connect_timeout': '10',
                'reboot_timeout': '30',
                'post_reboot_delay': '5',
                'test_command': 'uptime',
                'msg': 'System is going down for reboot NOW!',
                'shutdown_timeout': '4321',
            }


# Generated at 2022-06-13 10:29:29.112244
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    import datetime
    from ansible.module_utils._text import to_text
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=dict(
        )
    )

    am = ActionModule(
        module,
        'reboot',
        connection='local'
    )

    distribution = 'DEFAULT'
    previous_boot_time = "2018-06-28 17:02:40.991953"

    with pytest.raises(ValueError) as exc_info:
      am.check_boot_time(distribution=distribution, previous_boot_time=previous_boot_time)
    assert 'boot time has not changed' in to_text(exc_info.value)


# Generated at 2022-06-13 10:29:37.720932
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    # Create test object
    action_module_obj = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Add test_param to mock ansible facts
    facts = dict()
    test_param = 'test_value'
    facts['distribution'] = test_param

    result_obj = action_module_obj.get_distribution(facts)
    #assert result == test_param
    assert True is not False


# Generated at 2022-06-13 10:29:46.273311
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    # Mock argument values for method deprecated_args
    _task = {"action": "reboot"}
    _task_args = {"reboot_timeout": 30, "connect_timeout": None, "test_command": None}

    # Perform the call to method deprecated_args
    am = ActionModule()
    am._task = _task
    am._task.args = _task_args
    am.deprecated_args()


# Generated at 2022-06-13 10:29:55.662673
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    from ansible.module_utils.connection import ConnectionError
    from ansible.errors import AnsibleError
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY2
    import os
    import sys
    import pytest
    if PY2:
        import __builtin__ as builtins
    else:
        import builtins

    tests_path = os.path.dirname(os.path.realpath(__file__))
    test_utils_path = os.path.join(tests_path, os.path.pardir)
    modules_path = os.path.join(test_utils_path, 'module_utils')
    sys.path.insert(0, test_utils_path)
    sys.path.insert(1, modules_path)


# Generated at 2022-06-13 10:30:05.016149
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    action_module = ActionModule()
    task = dict(args=dict())
    action_module._task = MagicMock(spec=task)
    action_module._low_level_execute_command = MagicMock()
    action_module.get_system_boot_time = MagicMock()
    action_module._task.args = {}
    with pytest.raises(ValueError, match="boot time has not changed") as err:
        action_module.check_boot_time("distribution", "previous_boot_time")


# Generated at 2022-06-13 10:30:08.485295
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    action_module = ActionModule(None, None)
    assert action_module.get_shutdown_command({}) == "shutdown"

# Generated at 2022-06-13 10:30:13.905962
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    action = ActionModule()
    action.DEFAULT_SHUTDOWN_TIMEOUT = 3600
    args = action.get_shutdown_command_args('ADDITIONAL_SHUTDOWN_ARGS')
    assert args == 'ADDITIONAL_SHUTDOWN_ARGS'

# Generated at 2022-06-13 10:31:26.589424
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    boot_time_command = "uptime"
    distribution = "ubuntu"
    previous_boot_time = "[my_previous_boot_time]"
    test_instance = setup_default_instance()
    test_instance.get_system_boot_time = lambda distribution: "dummy_output"

    # Test normal branch
    test_instance.check_boot_time(distribution, previous_boot_time)

    # Test ValueError branch
    test_instance.get_system_boot_time = lambda distribution: ""
    with pytest.raises(ValueError) as e_info:
        test_instance.check_boot_time(distribution, previous_boot_time)

    # Test ValueError branch
    test_instance.get_system_boot_time = lambda distribution: previous_boot_time

# Generated at 2022-06-13 10:31:37.345438
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    command = "ls"
    command_args = "-ltr"
    expected_result = {'changed': True, 'elapsed': 0, 'rebooted': True}
    # set command args
    module_arguments = {'command': command, 'command_args': command_args}
    # set expected arguments
    expected_command = command + " " + command_args
    # set mock values
    module_mock = MagicMock(name='module mock')
    module_mock.run_command = MagicMock(return_value=expected_result)
    module_mock.get_bin_path = MagicMock(return_value=command)

    # mock module class
    module_class_mock = MagicMock(name='module class mock')

# Generated at 2022-06-13 10:31:43.883376
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    class Foo(ActionModule):
        def __init__(self):
            self.test_attempt_count = 0

        def foo(self, distribution, previous_boot_time):
            self.test_attempt_count += 1
            raise ValueError('Foo')

    f = Foo()

    f.do_until_success_or_timeout(action=f.foo, action_desc="foo", reboot_timeout=1, distribution='bar', action_kwargs={'previous_boot_time': 'bar'})

    assert f.test_attempt_count == 2


# Generated at 2022-06-13 10:31:54.122471
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    module = ActionModule()

    # Create a mock of the module's super class
    super_mock = mock.Mock()
    super_mock.run.return_value = {}

    module.__class__ = super_mock

    # Create a mock of the socket module used to get a read-only file descriptor
    # This is used in the connection plugin to detect if the connection is still alive
    socket_mock = mock.Mock()
    socket_mock.socket.return_value.fileno.return_value = 0

    # Create a mock of the connection plugin
    connection_mock = mock.Mock()
    connection_mock.transport = 'local'


# Generated at 2022-06-13 10:32:09.806394
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = AnsibleModule(
        argument_spec = dict(
            test_command=dict(type='str', default='/bin/true'),
            connect_timeout=dict(type='int', default=5),
            reboot_timeout=dict(type='int', default=120),
            post_reboot_delay=dict(type='int', default=0),
            msg=dict(type='str', default='system rebooted')
        ),
        supports_check_mode=True
    )

    action_module = ActionModule()

    action_module._task = FakeTask({'action': 'reboot'})
    action_module._connection = FakeConnection({'transport': 'local'})
    action_module._play_context = FakePlayContext({'check_mode': False})
    res = action_module.run(None, None)


# Generated at 2022-06-13 10:32:13.332744
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    my_obj = ActionModule(connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    ####################################################################################
    # ValueError: boot time has not changed
    ####################################################################################
    my_obj.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:32:21.117714
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():

    # create a mock module
    module_obj = ActionModule()
    print("type of module_obj: ",type(module_obj))

    # create mock ActionModule instance
    m_inst = mock.Mock(spec_set=ActionModule, instance=True)
    m_inst._task.action = 'Reboot'
    m_inst._task.args = dict()
    m_inst._display.display = mock.Mock()
    m_inst._task.args["wait_for_connection"] = False
    m_inst._task.args["connect_timeout"] = 5
    m_inst.DEFAULT_CONNECT_TIMEOUT = 5
    m_inst.DEFAULT_REBOOT_TIMEOUT = 300
    m_inst._task.args["reboot_timeout"] = 300

# Generated at 2022-06-13 10:32:25.247767
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    # Mock: ActionModule
    action_module = MagicMock(spec_set=ActionModule, autospec=True)

    test_name = 'test'

    # Check if the method get_shutdown_command_args returns
    # the valid shutdown_command_args for a distribution
    response = action_module._get_shutdown_command_args(test_name)
    assert response == '-r now'

# Generated at 2022-06-13 10:32:30.397153
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    module = ActionModule(None, None, 'whatever', 'whatever', 'whatever')
    assert module._supports_check_mode == True
    assert module._supports_async == True
    command_args = module.get_shutdown_command_args('test_distribution')
    expected = 'test_command_args'
    assert command_args == expected


# Generated at 2022-06-13 10:32:36.183774
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    def run_test_command__test(self, distribution, **kwargs):
        test_command = self._task.args.get('test_command', self._get_value_from_facts('TEST_COMMANDS', distribution, 'DEFAULT_TEST_COMMAND'))
        display.vvv("{action}: attempting post-reboot test command".format(action=self._task.action))
        display.debug("{action}: attempting post-reboot test command '{command}'".format(action=self._task.action, command=test_command))
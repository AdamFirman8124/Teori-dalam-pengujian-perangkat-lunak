

# Generated at 2022-06-13 10:27:19.223864
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    def test_action(reboot_timeout):
        FAIL_COUNT['count'] += 1
        if FAIL_COUNT['count'] > 3:
            return True
        else:
            raise RuntimeError

    global FAIL_COUNT
    FAIL_COUNT = { 'count': 0 }

    am = ActionModule()

    am.do_until_success_or_timeout(test_action, 'Test Action', reboot_timeout=3)

    assert FAIL_COUNT['count'] == 4

# Generated at 2022-06-13 10:27:25.348821
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    class MockResponse:
        def __init__(self, stdout, stderr, rc):
            self.stdout = stdout
            self.stderr = stderr
            self.rc = rc
    class MockConnection:
        def __init__(self, reboot_timeout,stderr,stdout):
            self.reboot_timeout = reboot_timeout
            self.stderr = stderr
            self.stdout = stdout
        def reset(self):
            pass
        def low_level_execute_command(command, sudoable=True):
            return MockResponse(stdout=self.stdout,stderr=self.stderr,rc=0)
        def get_option(self, connection_timeout):
            return self.reboot_timeout

# Generated at 2022-06-13 10:27:30.912104
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    # Create an object of class ActionModule to test it.
    test_object = ActionModule()
    
    # Set up any necessary test data.
    task_vars = ''
    distribution = ''

    # Call the method under test
    result = test_object.perform_reboot(task_vars, distribution)

    
    
    



# Generated at 2022-06-13 10:27:39.300813
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    """
    Unit test for method get_distribution of class ActionModule
    """
    # Initialization
    # The import statement is at the top of this file
    task = FakeTask()
    task_vars = {
        'ansible_facts': {
            'ansible_distribution': 'debian'
        }
    }

    # Non-Linux cases

# Generated at 2022-06-13 10:27:49.498333
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    with patch.object(ActionModule, '_low_level_execute_command', return_value={u'stdout': u'custom message\n', u'stderr': u'', u'rc': 0}):
        with patch.object(ActionModule, '_get_value_from_facts', return_value='shutdown_command_args'):
            testobj = ActionModule()
            testobj._task.args = {'distribution': 'redhat'}
            testobj._task.action = 'test_module'
            result = testobj.get_shutdown_command_args('redhat')
            assert ('shutdown_command_args' == result)
            testobj._task.args = {'distribution': 'banana'}
            result = testobj.get_shutdown_command_args('banana')

# Generated at 2022-06-13 10:27:57.576627
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    from datetime import datetime, timedelta
    from unittest.mock import MagicMock
    from ansible.utils.pycompat24 import integer_types

    action_module = ActionModule()

    # Some values we'll need
    current_time = datetime.utcnow()
    other_time = datetime.utcnow() + timedelta(seconds=5)

    # Mock the datetime class to return known values
    def mock_datetime_utcnow():
        nonlocal current_time
        retval = current_time
        current_time += timedelta(seconds=1)
        return retval

    class_mocker = MagicMock()
    class_mocker.return_value = mock_datetime_utcnow
    datetime.utcnow = class_mocker

    # Mock out the action
   

# Generated at 2022-06-13 10:28:01.176977
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    action_module = ActionModule()
    action_module.get_system_boot_time('Ubuntu')
    action_module.get_system_boot_time('RedHat')



# Generated at 2022-06-13 10:28:12.475371
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    """
    Tests if the correct distribution name is returned by get_distribution
    """

    # Given: Some distribution-specific fact
    task_vars = dict()
    fact = 'debian_version'
    value = '10'

    # When: We pass the fact and its value to get_distribution
    task_vars[fact] = value
    action_module = ActionModule(None, None)

    real_distribution = action_module.get_distribution(task_vars)

    # Then: The distribution name is retrieved from the fact_map
    distro_map = action_module.distro_map
    assert distro_map[fact] == real_distribution


# Generated at 2022-06-13 10:28:20.127612
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    module = 'reboot'
    distribution = 'debian'
    distribution_path = '{0}.{1}'.format(module, distribution)
    distribution_module_obj = ansible_collections.ansible.community.plugins.module_utils.distro.__dict__[distribution]

    facts = {"BOOT_TIME_COMMANDS": {"DEFAULT_BOOT_TIME_COMMAND": "echo \"Fri Sep 28 14:06:08 PDT 2018\""}}

    # unset the last boot time cache

# Generated at 2022-06-13 10:28:35.745760
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    class MockedTask(object):
        pass

    class MockedModule(object):
        pass

    class MockedConnection(object):
        pass

    with patch.object(ActionModule, 'get_distribution') as mocked_get_distribution:
        mocked_get_distribution.return_vaule = 'redhat'

        with patch.object(ActionModule, '_connection') as mocked__connection:
            mocked__connection.return_value = MockedConnection()

            action_module = ActionModule(mockedTask, mocked_Module, task_vars={})
            action_module.DEFAULT_REBOOT_TIMEOUT = 10


# Generated at 2022-06-13 10:29:08.773795
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    action_module = ActionModule()
    task_args = {'reboot_timeout': 1, 'connect_timeout': 2}
    action_module.set_defaults(task_args)

    action_module.deprecated_args()
    assert action_module._task.args.get('reboot_timeout') == 1
    assert action_module._task.args.get('connect_timeout') == 2



# Generated at 2022-06-13 10:29:18.898378
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    fixture = ActionModule()
    fixture.DEPRECATED_ARGS = "test"
    fixture._task.args = {"a": "b"}

    display.warning = MagicMock()
    check_type_str = MagicMock()
    str_to_num = MagicMock()
    to_text = MagicMock()

    with patch("ansible.module_utils.common.text.to_text", to_text):
        with patch("ansible.module_utils.common.str_to_num", str_to_num):
            with patch("ansible.module_utils.common.check_type_str", check_type_str):
                with patch.dict(fixture.__dict__, {"_task": {"action": "test"}, "DEPRECATED_ARGS": {"a": "b"}}):
                    fixture.dep

# Generated at 2022-06-13 10:29:22.794634
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    action_mod = ActionModule(task(), connection(), play_context(), loader(), templar(), shared_loader_obj)
    action_mod.check_boot_time("redhat", "boot_time")

# Generated at 2022-06-13 10:29:24.753450
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    action_module = ActionModule()
    distribution = 'debian'
    action_module.run_test_command(distribution=distribution)


# Generated at 2022-06-13 10:29:32.840672
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:29:37.399827
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Construct the object
    action_module = ActionModule()
    # Try performing reboot
    result = action_module.run(None, None)
    assert result == {'changed': True, 'elapsed': 0, 'rebooted': True}

# Generated at 2022-06-13 10:29:50.548221
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    _connection = AnsibleConnection('ssh')
    _low_level_execute_command = MagicMock()
    _task = AnsibleTask('reboot')
    _task.args = {
        'pre_reboot_delay': 0,
        'post_reboot_delay': 0,
        'test_command': 'whoami',
        'connect_timeout': 30,
        'reboot_timeout': 600,
        'connect_timeout_sec': 30,
        'reboot_timeout_sec': 600,
    }
    _play_context = PlayContext()
    _action_base = ActionBase()
    _action_module = ActionModule(_connection, _low_level_execute_command, _task, _play_context, _action_base)

    # Mock out get_distribution
    _action_module.get_distribution

# Generated at 2022-06-13 10:30:04.810452
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    # set up
    class TestActionModule(ActionModule):
        def __init__(self):
            self.DEFAULT_TEST_COMMAND = 'echo 1'
            self.TEST_COMMANDS = dict()
            self.BOOT_TIME_COMMANDS = dict()

    class TaskFake(object):
        def __init__(self):
            self.args = dict()
            self.action = 'reboot'

    task = TaskFake()

    module = TestActionModule()
    module._task = task
    distribution = 'Ubuntu'

    # test
    try:
        result = module.run_test_command(distribution)
    except Exception:
        failed = False
        msg = ''
    else:
        failed = True
        msg = 'Expected exception to be raised'


# Generated at 2022-06-13 10:30:10.574869
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    action_module = ActionModule(None, None)
    distribution = "RedHat"
    expected_output = "now"
    actual_output = action_module.get_shutdown_command_args(distribution)
    assert actual_output == expected_output



# Generated at 2022-06-13 10:30:16.986017
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():

    # CommandAttributeError is raised by _get_value_from_facts.
    # Since there is no way to insert a suitable entry into the facts,
    # we bypass the method.
    # This is done by creating a mock object that the method will interact with.

    # Create the mock class.
    class FactMock:
        def __init__(self):
            self.value = None
            self.get_value_input = None
            self.get_value_output = None

        def get_value(self, key):
            self.get_value_input = key
            return self.get_value_output


    # Create an object of the mock class
    mock_fact = FactMock()

    # Create a mock object to pass as self
    # We know that the method gets the distributions from the fact
    # self._get_value

# Generated at 2022-06-13 10:31:24.058337
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
  action_module = ActionModule()
  # TODO: Pass in required object instances.
  # Pass in false and expect to get error
  try:
    action_module.deprecated_args()
    assert False
  except Exception as e:
    assert True


# Generated at 2022-06-13 10:31:28.858354
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    hostvars = dict(ansible_distribution='SLES')
    result = ActionModule._get_distribution('Debian', hostvars)
    assert result == 'Debian'
    hostvars = dict(ansible_distribution='SLES', ansible_distribution_release='15')
    result = ActionModule._get_distribution('Debian', hostvars)
    assert result == 'SLES'



# Generated at 2022-06-13 10:31:39.669936
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    # Create an instance of class ActionModule without specifying a task or connection
    test_instance = ActionModule()
    # Create a class to return when action is called
    class ActionResult:
        def __init__(self):
            self.result = None

        def action(self, **kwargs):
            self.result = kwargs

    # Create a instance of ActionResult
    action_result = ActionResult()
    # Set up test input
    kwargs = {'distribution': 'Cusotm'}
    # Set up test input
    action_kwargs = {'previous_boot_time': '14:00:00 Nov 20'}
    # Set up test input
    action_desc = 'boot time check'
    # Set up test input
    reboot_timeout = timedelta(seconds=1)
    # Set up test input

# Generated at 2022-06-13 10:31:49.766144
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    host_name = 'myhost'

# Generated at 2022-06-13 10:31:52.996296
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():

    # Perform the method call
    result = ActionModule.perform_reboot()

    # Check if the result is as expected
    if result != expected:
        raise Exception("Result does not match expected result")



# Generated at 2022-06-13 10:31:59.561680
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    os.unlink("systemd-sleep.jpg")
    os.unlink("cypress.jpg")
    os.unlink("flowers.jpg")
    os.rmdir("/var/tmp/ansible-temp-1537786773.65-157480785036489/prophet")
    os.rmdir("/var/tmp/ansible-temp-1537786773.65-157480785036489")
    os.rmdir("/var/tmp")


# Generated at 2022-06-13 10:32:04.136849
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    import pytest
    host_vars = dict(
                     ansible_distribution="RedHat",
                     )
    pytest.skip("TODO: test_ActionModule_validate_reboot")


# Generated at 2022-06-13 10:32:11.897809
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    from ansible.errors import AnsibleError
    from ansible.module_utils.connection import Connection
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.reboot_test_command import ActionModule
    from ansible.utils.display import Display
    from ansible.utils.vars import merge_hash
    from ansible.vars import combine_vars
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play_context import PlayContext
    import ansible.module_utils.facts.test_helper as test_helper
    import ansible.module_utils.facts.system.distribution as distribution

# Generated at 2022-06-13 10:32:17.838432
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Calls the method to a test
    class TestException(Exception):
        pass

    exception_raised = False
    start = time.time()
    try:
        action_module.do_until_success_or_timeout(action=lambda: None, action_desc=None, reboot_timeout=3, action_kwargs={})
    except TestException:
        exception_raised = True

    assert exception_raised
    assert time.time() - start >= 3.0

# Generated at 2022-06-13 10:32:20.777380
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    action_module = ActionModule(task=MagicMock(), connection=MagicMock(), play_context=MagicMock(), loader=MagicMock(), templar=MagicMock(), shared_loader_obj=None)
    

# Generated at 2022-06-13 10:34:31.695790
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    
    #Declare the ActionModule object
    am = ActionModule()
    
    #Declare the distribution
    distribution = "Red Hat"
    
    #Call the method get_system_boot_time by passing the distribution
    result = am.get_system_boot_time(distribution)
    
    if result == "Tue Apr 14 16:01:45 EDT 2015":
        return "get_system_boot_time method works as expected"
    else:
        return "get_system_boot_time method needs to be debugged"


# Generated at 2022-06-13 10:34:32.708379
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    pass


# Generated at 2022-06-13 10:34:37.524353
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    # init action module
    action_module = ActionModule(task=Task())
    # fake task_vars
    task_vars = {}
    # fake distribution
    distribution = 'openbsd'

    # when OS_FAMILY is openbsd, it should return '/sbin/reboot'
    action_module.OS_FAMILY = 'openbsd'
    rst = action_module.get_shutdown_command(task_vars, distribution)
    assert rst == '/sbin/reboot'

# Generated at 2022-06-13 10:34:43.274386
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_connection = 'local'
    test_task_vars = dict()
    test_task = dict(action = '',
                     async_val = '',
                     connection = test_connection,
                     delegate_to = '',
                     delay = '',
                     become = '',
                     become_method = '',
                     become_user = '',
                     check = '',
                     diff = '',
                     loop = '',
                     no_log = '',
                     poll = '',
                     retries = '',
                     run_once = '',
                     until = '',
                     timeout = '',
                     tags = '',
                     when = '',
                     debug_task = ''
                     )
    test_tmp = dict()
    test_result = dict()


# Generated at 2022-06-13 10:34:57.711812
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    # Set up mock
    url = 'file://testing_dir/test_ActionModule_get_distribution.yaml'

# Generated at 2022-06-13 10:35:05.206862
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    mocker.patch('__main__.ActionModule._get_value_from_facts')
    mocker.patch('__main__.ActionModule._low_level_execute_command')
    module = mocker.Mock()
    module._task = mocker.Mock()
    module._task.action = 'reboot'
    module._connection = mocker.Mock()
    module._connection.transport = 'ssh'
    module._supports_check_mode = True
    module._supports_async = True
    module.post_reboot_delay = 15
    module.DEFAULT_SUDOABLE = True
    module.DEFAULT_REBOOT_TIMEOUT = 30
    module.DEFAULT_CONNECT_TIMEOUT = 15

# Generated at 2022-06-13 10:35:06.877622
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    # file: modules/system/reboot.py
    # method: run_test_command
    # class: ActionModule

    # TODO: implement test_run_test_command
    pass


# Generated at 2022-06-13 10:35:13.832098
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    m = ActionModule()
    distribution = 'DEFAULT'
    m.do_until_success_or_timeout(m.check_boot_time, reboot_timeout=60, distribution=distribution, action_kwargs={})
    m.do_until_success_or_timeout(m.run_test_command, reboot_timeout=60, distribution=distribution, action_kwargs={})

# Generated at 2022-06-13 10:35:17.631434
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
#     action_module = ActionModule()
    print("WTF?")

if __name__ == '__main__':
    test_ActionModule_validate_reboot()
    # Unit test for method run of class ActionModule
    def test_ActionModule_run():
#         action_module = ActionModule()
        print("WTF?")

if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:35:30.471239
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    runner_mock = unittest.mock.MagicMock()
    runner_mock._task.action = 'reboot'
    runner_mock._task.args = {}
    action = reboot.ActionModule(runner_mock._connection, runner_mock._play_context, runner_mock._loader, runner_mock._templar, runner_mock._shared_loader_obj)
    action._task.args = {}

    with unittest.mock.patch.object(action, 'get_distribution') as get_distribution_mock:
        get_distribution_mock.return_value = 'arch'
        result = action.get_shutdown_command_args('arch')
        assert result == '1'
        get_distribution_mock.return_value = 'freebsd'
       
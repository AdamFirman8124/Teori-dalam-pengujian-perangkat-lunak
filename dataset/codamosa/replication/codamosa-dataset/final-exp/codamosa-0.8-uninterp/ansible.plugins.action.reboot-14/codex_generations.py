

# Generated at 2022-06-13 10:27:19.100140
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    with patch.object(runner, '_make_tmp_path') as make_tmp_path, \
            patch.object(ActionModule, 'do_until_success_or_timeout') as do_until_success_or_timeout, \
            patch.object(ActionModule, 'get_distribution') as get_distribution, \
            patch.object(ActionModule, 'run') as run, \
            patch.object(ActionModule, '_low_level_execute_command') as _low_level_execute_command:
        tmp = '/tmp/ansible'
        make_tmp_path.return_value = tmp
        task_vars = {'distribution': 'DEFAULT_BOOT_TIME_COMMAND'}

# Generated at 2022-06-13 10:27:25.255516
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
  # input parameters
  task_vars = 'task_vars'

  # context for invoke call
  context = {}

  # mocks for the action plugin
  ansible_facts = dict(
    distribution='distribution',
    ansible_distribution='ansible_distribution',
    ansible_distribution_version='ansible_distribution_version',
    ansible_distribution_release='ansible_distribution_release',
    ansible_os_family='ansible_os_family'
  )
  m_get_value_from_facts = 'get_value_from_facts'
  m_get_value_from_group_vars = 'get_value_from_group_vars'
  m_get_value_from_host_vars = 'get_value_from_host_vars'



# Generated at 2022-06-13 10:27:35.544145
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test when reboot command fails and returns non zero rc
    action_module = ActionModule()

    task_vars = {}

    # expected result after performing reboot
    expected_reboot_result = {"failed": True, "rebooted": False, "start": datetime.utcnow()}
  
    # mock connection to perform reboot
    action_module._connection = MockConnection(reboot_command_result={
        "rc": 1,
        "stdout": "Failed to reboot successfully",
        "stderr": "Error rebooting"
    })
    # perform reboot
    reboot_result = action_module.perform_reboot(task_vars, "Ubuntu")
    # assert returned result
    assert reboot_result == expected_reboot_result
    # test when validation of reboot fails and throws exception

# Generated at 2022-06-13 10:27:43.447963
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    # uncomment and update test case if necessary
    # action_module = ActionModule(connection=None, module_name='', module_args=dict(), task_vars=dict(), tmp=None)
    action_module = ActionModule(connection=conn, module_name='', module_args=dict(), task_vars=dict(), tmp=None)
    distribution = "foobar"
    previous_boot_time = "foobar"
    action_module.check_boot_time(distribution, previous_boot_time)


# Generated at 2022-06-13 10:27:52.221903
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    # Unit test variables
    result = False
    # mock_ansible_module_complete_args:
    test_args = {}
    # mock_ansible_module_get_bin_path:
    test_get_bin_path_map = {}
    # mock_ansible_module_run_command:
    test_command = None
    test_run_command_rc = 0
    test_run_command_return_code = 0
    test_run_command_stdout = b''
    test_run_command_stderr = b''
    test_run_command_results = {}
    # mock_ansible_module_get_distribution:
    test_get_distribution_result = 'redhat'
    # mock_ansible_module_get_all_facts:
    test_returned_facts = {}

# Generated at 2022-06-13 10:28:02.752486
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    # we have to set connection to None to get it to work with the code
    # we have in the default constructor
    module = ActionModule(connection=None)
    # Set default sleep
    global test_timer
    test_timer = 0.01

    # Set up action
    def action_success(reboot_timeout, distribution, action_kwargs):
        raise Exception('test action should not be executed outside of do_until_success_or_timeout')

    module.do_until_success_or_timeout(action=action_success, action_desc=None, reboot_timeout=1, distribution=None, action_kwargs=None)

    # Test action failure
    def action_failure(reboot_timeout, distribution, action_kwargs):
        raise TimedOutException('test action')


# Generated at 2022-06-13 10:28:14.785493
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    def function_to_execute(distribution, *args, **kwargs):
        for arg, arg_value in kwargs.items():
            if arg == 'fail_count' and arg_value > 3:
                raise RuntimeError('success')

        raise Exception('failed')

    def function_to_execute2(distribution, *args, **kwargs):
        for arg, arg_value in kwargs.items():
            if arg == 'fail_count' and arg_value > 3:
                raise RuntimeError('success')

        raise Exception('failed')

    # create a fake task so we can execute do_until_success_or_timeout
    task_vars = {}
    class FakeActionModule():
        def __init__(self):
            self.task = FakeTask()


# Generated at 2022-06-13 10:28:16.437981
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    mod = bashd.ActionModule()

    # test callable without arguments
    result = mod.get_shutdown_command()

    assert result is not None


# Generated at 2022-06-13 10:28:17.006489
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    pass

# Generated at 2022-06-13 10:28:21.017192
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    # Set up parameters for call to method perform_reboot
    task_vars = {}
    distribution = None

    # Create instance of class ActionModule
    action_reboot_obj = ActionModule()

    # Call method perform_reboot
    result = action_reboot_obj.perform_reboot(task_vars, distribution)

# Generated at 2022-06-13 10:28:50.345316
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    pass #we do not test class methods

# Generated at 2022-06-13 10:29:00.016856
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    # Unit test for method check_boot_time of class ActionModule
    # Given a set of `errors` set to what the return should be, a set
    # of `inputs` set to the values the function will be called with, make sure
    # the function returns the correct value as described in `errors`.

    # Note: this test case is simply a placeholder for future unit test cases.

    expected = 'Error: You must implement your own unit test for this function!'

    module = ActionModule()

    result = module.check_boot_time([])

    assert result == expected


# Generated at 2022-06-13 10:29:00.993427
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    pass



# Generated at 2022-06-13 10:29:02.077104
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    pass


# Generated at 2022-06-13 10:29:05.365980
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    # This test validates the correct error gets raised if a system has no
    # boot time command defined
    action_module = ActionModule()

    with pytest.raises(AnsibleError):
        action_module.get_system_boot_time('nodistro')

# Generated at 2022-06-13 10:29:10.669149
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    act = ActionModule()
    act.DEFAULT_REBOOT_TIMEOUT = 60

    class SomeException(Exception):
        pass

    class SomeOtherException(Exception):
        pass

    def fake_check_boot_time(distribution, previous_boot_time):
        raise SomeOtherException()

    def fake_run_test_command(distribution):
        raise SomeException()

    def fake_check_boot_time_successful(distribution, previous_boot_time):
        return True

    def fake_run_test_command_successful(distribution):
        return True


# Generated at 2022-06-13 10:29:11.973331
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    action_module = ActionModule()

# Generated at 2022-06-13 10:29:20.791699
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():

    # UnitTest: test get_shutdown_command_args for DEBIAN or UBUNTU
    with patch.object(ActionModule, 'get_distribution') as mock_method:
        mock_method.return_value = 'DEBIAN'
        a = ActionModule(dict(ANSIBLE_MODULE_ARGS={}), dict())
        assert a.get_shutdown_command_args('DEBIAN') == '-r now'

    # UnitTest: test get_shutdown_command_args for FEDORA, CENTOS, or REDHAT
    with patch.object(ActionModule, 'get_distribution') as mock_method:
        mock_method.return_value = 'CENTOS'
        a = ActionModule(dict(ANSIBLE_MODULE_ARGS={}), dict())
        assert a.get_shut

# Generated at 2022-06-13 10:29:21.723361
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    pass # TODO: Implementation


# Generated at 2022-06-13 10:29:30.120613
# Unit test for method get_shutdown_command_args of class ActionModule

# Generated at 2022-06-13 10:30:26.670553
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    action_module = ActionModule()
    assert True


# Generated at 2022-06-13 10:30:36.044144
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    # Create a mock connection plugin to be set on the module object
    mock_connection_plugin = ConnectionMock()

    # Create a mock ActionModule object.  It should be noted that these
    # are not valid unit tests since the action module objects are not
    # stand-alone.  These are simply duplicating the methods in the
    # action module so it is easier to test the logic.
    action_module = ActionModule()
    action_module._connection = mock_connection_plugin
    action_module._task = TaskMock()
    action_module._task.action = 'reboot'

    # Set defaults in the action module
    action_module.DEFAULT_TEST_COMMAND = '/bin/true'
    action_module.DEFAULT_BOOT_TIME_COMMAND = 'uptime'
    action_module.BOOT_TIME

# Generated at 2022-06-13 10:30:42.198542
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    # Create a mock for class ActionModule
    action_module = mock.Mock(spec=ActionModule)
    # Define test input argument values for ActionModule.run_test_command
    distribution = 'SLACKWARE'
    # Execute method ActionModule.run_test_command with the above defined input argument values
    action_module.run_test_command(distribution)
    # Verify if method ActionModule.run_test_command was called as expected
    action_module.run_test_command.assert_called_once_with(distribution)

# Generated at 2022-06-13 10:30:49.110365
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    action_module = ActionModule('/home/project/ansible/ansible/lib/ansible/plugins/action/reboot.py', 'module', '', '/home/project/ansible/ansible/lib/ansible/plugins/action/reboot.py')
    task_vars = {}
    assert_equals(action_module.get_distribution(task_vars), 'DEFAULT_DISTRIBUTION')

# Generated at 2022-06-13 10:30:50.842599
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    action_module = ActionModule()
    assert action_module.deprecated_args() == None



# Generated at 2022-06-13 10:30:57.880700
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    # Declare the class we are testing
    test_class = ActionModule
    # Create an instance of that class
    test_instance = test_class()
    
    # Specify constants to be used in this test
    shutdown_bin_path = 'test'
    task_vars = {}
    distribution = 'test'
    # Execute the method we are testing
    method_result = test_instance.get_shutdown_command(shutdown_bin_path, task_vars, distribution)
    # Test for expected result
    assert method_result == shutdown_bin_path

# Generated at 2022-06-13 10:31:01.548072
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    action_module = ActionModule()
    result = action_module.run_test_command("test")
    assert result == None, "Expected: None, Actual: {0}".format(result)


# Generated at 2022-06-13 10:31:13.521784
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    action_module = ActionModule()

    action_module.__dict__['_files_to_copy'] = []
    action_module.__dict__['_connection'] = Connection()
    action_module.__dict__['_play_context'] = PlayContext()
    action_module.__dict__['_task'] = Task()


# Generated at 2022-06-13 10:31:16.021404
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    module = AnsibleModule(argument_spec=dict())
    fixture = Fixture02()
    fixture.run_test_command(distribution=None)


# Generated at 2022-06-13 10:31:21.853039
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    # Input parameters
    distribution = 'DEFAULT_DISTRIBUTION'
    previous_boot_time = 'DEFAULT_PREVIOUS_BOOT_TIME'

    # Output parameters
    expected_result = 'DEFAULT_EXPECTED_RESULT'

    # Module to test
    am = ActionModule()

    # When
    result = am.check_boot_time(distribution, previous_boot_time)

    # Then
    assert result == expected_result
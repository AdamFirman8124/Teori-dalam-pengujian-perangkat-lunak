

# Generated at 2022-06-13 10:27:17.547079
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    # Create a dummy module to supply to ActionModule
    class DummyModule:
        def get_bin_path(self, arg, required=False, opt_dirs=None):
            return '/bin/date'

    dm = DummyModule()
    am = ActionModule(dm)

    # Create a dummy ansible task to supply to ActionModule
    class DummyAnsibleTask(object):
        def __init__(self):
            self.args = {
                'test_command': 'date',
            }
    at = DummyAnsibleTask()

    # Create a dummy ansible connection to supply to ActionModule
    class DummyAnsibleConnection(object):
        def reset(self):
            pass

    ac = DummyAnsibleConnection()

    # Create a dummy result dict

# Generated at 2022-06-13 10:27:18.211142
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    pass

# Generated at 2022-06-13 10:27:24.574194
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    # For testing to work we need to have a valid connection
    module_utils.connection.Connection.CONNECTION = Connection(connection_info={'host': '127.0.0.1'})
    result = {}
    result['failed'] = False
    result['rebooted'] = False
    action_kwargs = {'previous_boot_time': 'test_ActionModule_do_until_success_or_timeout'}
    reboot_timeout = 1
    distribution = 'test'
    test_action = ActionModule()

    # case when action is not valid

# Generated at 2022-06-13 10:27:31.383823
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    # Set up mock
    task_vars = {}
    shutdown_bin = ''

    module = ActionModule()

    # Generate tests
    distribution = ''
    search_paths = ''
    expected_result = ''
    # Execute the task
    results = module.get_shutdown_command(shutdown_bin, distribution, search_paths)
    # Test for no exceptions
    # Test for expected result
    assert results == expected_result


# Generated at 2022-06-13 10:27:35.301474
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    a = ActionModule(None, None)
    a.get_system_boot_time(None)

# Generated at 2022-06-13 10:27:43.651177
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    task_vars = {'ansible_distribution': 'RedHat', 'ansible_distribution_release': '7', 'ansible_distribution_version': '7'}
    am = ActionModule(self._task, self._connection, task_vars, templar=self._loader)
    self.assertEquals(am.get_shutdown_command(task_vars, 'DEFAULT'), 'shutdown')
    self.assertEquals(am.get_shutdown_command(task_vars, 'RedHat'), 'shutdown')
    

# Generated at 2022-06-13 10:27:47.069822
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    a = ActionModule()
    module_args = {}
    a._task.args = module_args

    # call the method
    result = a.get_shutdown_command_args(distribution='redhat')
    assert result == '-r now'

# Generated at 2022-06-13 10:27:54.135347
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    class TestActionModule(ActionModule):
        def get_distribution(self):
            return Distribution
        def get_shutdown_command(self):
            return 'command'
        def get_shutdown_command_args(self):
            return 'args'
        def get_system_boot_time(self):
            return '123456'
        class TestDistribution:
            pass
        class TestConnection:
            def get_option(**kwargs):
                return 10
            def set_option(**kwargs):
                return None
            def reset(**kwargs):
                return None

    assert test_module.validate_reboot(module, TestDistribution, TestConnection) == {'changed': True, 'elapsed': 0, 'failed': False, 'rebooted': True}

# Generated at 2022-06-13 10:27:54.942833
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    pass # nothing to test



# Generated at 2022-06-13 10:28:08.320167
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    # test when action succeeds with no retries
    result = {'start': datetime.utcnow()}
    distribution = "Debian"
    mock_reboot_validation = Mock()
    mock_reboot_validation.side_effect = [Exception(), Exception(), Exception(), Exception()]
    a = ActionModule()

    reboot_timeout = 1
    try:
        a.do_until_success_or_timeout(action=mock_reboot_validation,
                                      action_desc="last boot time check",
                                      reboot_timeout=reboot_timeout,
                                      distribution=distribution)
    except Exception as e:
        assert False

    # test when action succeeds with retries
    mock_reboot_validation.side_effect = [Exception(), Exception(), Exception(), ValueError()]

# Generated at 2022-06-13 10:28:44.697734
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    action_module = ActionModule(
        connection=None,
        task_vars={
            'ansible_distribution': 'SUSE Linux Enterprise Server',
            'ansible_distribution_file_parsed': True,
            'ansible_distribution_file_path': '/etc/SuSE-release',
            'ansible_distribution_file_variety': 'SUSE'
        },
        loader=None,
        play_context=None,
        shared_loader_obj=None,
        tmp=None,
        add_final_message=False,
        ansible_version=None
    )

    # Method get_distribution of class ActionModule returns really nothing
    result = action_module.get_distribution()

    assert result is None

# Generated at 2022-06-13 10:28:55.797859
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    with patch.object(display.Display, 'warning', return_value=None):
        with patch.object(display.Display, 'debug', return_value=None):
            action_module = ActionModule(task={"args": {"test": "test"}}, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
            action_module.deprecated_args()

            action_module = ActionModule(task={"args": {}}, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
            action_module.deprecated_args()



# Generated at 2022-06-13 10:29:05.033428
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    # Patch AnsibleModule to avoid the AnsibleModule boilerplate
    mock_AnsibleModule = MagicMock()

    # Patch AnsibleModule.fail_json
    mock_fail_json = MagicMock()
    mock_AnsibleModule.fail_json = mock_fail_json

    # Patch AnsibleModule.exit_json
    mock_exit_json = MagicMock()
    mock_AnsibleModule.exit_json = mock_exit_json

    # Create the class under test
    am = ActionModule(mock_AnsibleModule)

    # Example return from ansible_facts

# Generated at 2022-06-13 10:29:06.898316
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	assert True == False



# Generated at 2022-06-13 10:29:08.867584
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    pass

# Unit tests for method check_boot_time of class ActionModule

# Generated at 2022-06-13 10:29:14.152714
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    # Build mock objects to pass to the module
    original_connection_timeout = None
    action_kwargs = None

    # Call method
    r = ActionModule.validate_reboot(self, distribution=distribution, original_connection_timeout=original_connection_timeout, action_kwargs=action_kwargs)
    assert r == None


# Generated at 2022-06-13 10:29:22.299566
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    # Runs test case against method deprecated_args of class ActionModule
    action = ActionModule('reboot', {}, False)
    task = AnsibleTask()
    new_instance = action.__class__('reboot', {}, False)

    new_instance.DEPRECATED_ARGS = {}
    action.DEPRECATED_ARGS = {'test_command': '2.9'}
    new_instance._task = task
    action._task = task

    action.deprecated_args()



# Generated at 2022-06-13 10:29:27.000512
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    test_args = dict(
        test_command = dict(
            test_name = dict(
                test_args = dict(),
                expected_output = dict()
            )
        )
    )
    test_reboot_result = ActionModule.get_shutdown_command_args(**test_args)
    assert test_reboot_result is None


# Generated at 2022-06-13 10:29:33.888603
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    # prepare the test
    mock_task = Mock()
    mock_task.action = 'reboot'
    mock_task.args = {}
    mock_task.args['reboot_timeout'] = 5
    mock_task.async_val = 1
    mock_task.notify = ['foo']
    mock_task.run_once = False

    mock_play_context = Mock()
    mock_play_context.check_mode = False

    mock_connection = Mock()
    mock_connection.transport = 'smart'
    mock_connection.reset.return_value = None

    mock_set_module_args = Mock()

    # instantiate the class to be tested

# Generated at 2022-06-13 10:29:38.649649
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    # Pass
    test_action_module = ActionModule()
    test_distribution = 'Ubuntu'
    return_value = test_action_module.run_test_command(test_distribution)
    assert return_value is None
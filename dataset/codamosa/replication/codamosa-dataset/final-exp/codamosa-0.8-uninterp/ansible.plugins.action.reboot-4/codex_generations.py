

# Generated at 2022-06-13 10:27:22.122568
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    # Setup test values
    distribution = 'distribution'
    self = ActionModule()
    ansible_distribution = 'ansible_distribution'
    ansible_distribution_version = 'ansible_distribution_version'
    ansible_distribution_major_version = 'ansible_distribution_major_version'
    ansible_os_family = 'ansible_os_family'
    ansible_distribution_release = 'ansible_distribution_release'
    ansible_distribution_version_full = 'ansible_distribution_version_full'
    action_module_shutdown_command_args_facts = dict()
    action_module_shutdown_command_args_facts['ansible_distribution'] = ansible_distribution

# Generated at 2022-06-13 10:27:30.519453
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    action = reboot.ActionModule(dict(name='test_ActionModule_do_until_success_or_timeout', async_val=10, poll=0))
    distribution = {'DEFAULT_TEST_COMMAND': 'uptime'}
    original_connection_timeout = None
    action_kwargs = {}
    try:
        action.do_until_success_or_timeout(action=action.run_test_command,
                                           action_desc="post-reboot test command",
                                           reboot_timeout=20,
                                           distribution=distribution,
                                           action_kwargs=action_kwargs)
    except Exception as e:
        raise Exception("test_ActionModule_do_until_success_or_timeout failed: {}".format(e))

# Generated at 2022-06-13 10:27:43.095061
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    # Test that it returns an appropriate response when run_test_command is called and the user has not defined a test command.
    #   1. Setting up the variables required for testing this unit test
    class Task:
        def __init__(self):
            self.args = {}

    class ModuleDeprecationWarning:
        def __init__(self, msg):
            self.msg = msg

    action_module = ActionModule()
    action_module._task = Task()

    # 2. Setting up the mocks needed for this function
    action_module._low_level_execute_command = Mock()

    # 3. Calling the unit test
    action_module.run_test_command("distribution")

    # 4. Asserting the expected results

# Generated at 2022-06-13 10:27:46.445179
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module.get_shutdown_command_args("a") == "a"


# Generated at 2022-06-13 10:27:54.688593
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    # Setup
    data = {}
    data['DEFAULT_BOOT_TIME_COMMAND'] = 'test_DEFAULT_BOOT_TIME_COMMAND'
    data['DEFAULT_BOOT_TIME_COMMANDS'] = {'Ubuntu': 'test_DEFAULT_BOOT_TIME_COMMANDS_Ubuntu'}
    data['DEFAULT_FILE_SEARCH_PATH'] = 'test_DEFAULT_FILE_SEARCH_PATH'
    data['DEFAULT_SUDOABLE'] = False
    data['DEFAULT_TEST_COMMAND'] = 'test_DEFAULT_TEST_COMMAND'
    data['DEFAULT_TEST_COMMANDS'] = {' Ubuntu': 'test_DEFAULT_TEST_COMMANDS_Ubuntu'}

    action_module = ActionModule()
    #

# Generated at 2022-06-13 10:28:01.184528
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # get the module
    reboot_module = sys.modules['lib.actions.reboot']

    # create an instance of the module
    module = reboot_module.ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    def mocked_run(self, tmp=None, task_vars=None):
        return super(reboot_module.ActionModule, self).run(tmp, task_vars)

    def mocked_get_distribution(self, task_vars):
        return self._get_value_from_facts('DISTRIBUTION', 'redhat', 'DEFAULT_DISTRIBUTION')

    def mocked_is_connection_to_localhost(self):
        return False


# Generated at 2022-06-13 10:28:13.711070
# Unit test for method get_shutdown_command of class ActionModule

# Generated at 2022-06-13 10:28:20.875043
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    # ARRANGE
    # set up a test action module
    am = ActionModule(None, None, None)

    class MockTask(object):
        def __init__(self):
            self.action = 'test_action'
            self.args = {'test_arg': 'test_value'}

    class MockConnection(object):
        def __init__(self):
            self.transport = 'ssh'

    class MockTaskVars(object):
        def __init__(self):
            self.test_facts = {'test_fact': 'test_value'}

    am._task = MockTask()
    am._connection = MockConnection()
    am.DEFAULT_SUDOABLE = True

# Generated at 2022-06-13 10:28:31.395463
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    m = ActionModule(task=MagicMock(), connection=MagicMock(), play_context=MagicMock())
    m.action = "reboot"

    m.DEPRECATED_ARGS = {
        "reboot_timeout": 2.3,
        "reboot_timeout_sec": 2.3,
        "connect_timeout": 2.3,
        "connect_timeout_sec": 2.3,
        "test_command": 2.3
    }

    m._task.args = {
        "reboot_timeout": 1,
        "reboot_timeout_sec": 1,
        "connect_timeout": 1,
        "connect_timeout_sec": 1,
        "test_command": 1
    }

    m.deprecated_args()

# Generated at 2022-06-13 10:28:42.621906
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    fake_self = create_autospec(ActionModule)

    setattr(fake_self, '_task', {'action': 'reboot'})
    setattr(fake_self, '_connection', create_autospec(Connection, spec_set=True))
    fake_self._task.update(dict(
        args=dict(
            distribution=None
        ),
        _raw_params='',
    ))

    # Use a mock to return a specific distribution to test code path
    fake_self._get_value_from_facts = Mock()
    fake_self._get_value_from_facts.return_value = 'redhat7'

    distribution = fake_self.get_distribution({})
    assert 'redhat7' == distribution


# Generated at 2022-06-13 10:29:18.822893
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    task_vars = dict()
    am = ActionModule(
        task=dict(action=dict(reboot=dict())),
        connection=dict(transport='mock'),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )
    display = Display()
    distribution = dict(distribution='test distribution')

    # Set up and check results
    am.get_system_boot_time(distribution)
    assert False, "Should not reach here"



# Generated at 2022-06-13 10:29:28.601579
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    inventory = Inventory(loader=None, variable_manager=None, host_list=None)
    variable_manager = VariableManager(loader=None, inventory=inventory)
    loader = DataLoader()
    module = AnsibleModule(argument_spec=dict())
    module.params = {}

    am = ActionModule(module=module, task=None, connection=None, play_context=None, loader=loader, templar=None, shared_loader_obj=None)
    facts = copy.deepcopy(FACTS_DISTRIBUTION_REDHAT)
    assert am.get_distribution(facts) == 'RedHat'

    facts = copy.deepcopy(FACTS_DISTRIBUTION_DEBIAN)
    assert am.get_distribution(facts) == 'Debian'


# Generated at 2022-06-13 10:29:33.521725
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    action_module = ActionModule()
    reboot_result = action_module.perform_reboot(1, 2)
    assert(reboot_result['failed'] == False)
    
# # Unit test for method check_boot_time of class ActionModule

# Generated at 2022-06-13 10:29:35.263571
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():

    # TODO
    assert False



# Generated at 2022-06-13 10:29:46.164335
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    os.system("rm -f -r ./test/temp/*")
    os.system("mkdir ./test/temp/")

# Generated at 2022-06-13 10:29:54.625449
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
	# Create a test object of class ActionModule, with a mock connection
	connection_obj = connection.Connection(MagicMock())
	action_module = ActionModule(connection_obj, MagicMock())
	
	mocked_task = MagicMock()
	mocked_task.args = {}
	
	# Create test data for task vars

# Generated at 2022-06-13 10:30:06.583420
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    # Try to initialize class ActionModule
    test_obj = ActionModule(task='task', connection='connection', play_context='play_context', loader='loader', templar='templar', shared_loader_obj='shared_loader_obj')

    # Try to execute method validate_reboot('Ubuntu', 'original_connection_timeout', 'action_kwargs') of class ActionModule
    test_args = [{'distribution': 'Ubuntu', 'original_connection_timeout': 'original_connection_timeout', 'action_kwargs': 'action_kwargs'}]

    # Test execute method validate_reboot() of class ActionModule
    test_obj.validate_reboot(distribution, original_connection_timeout, action_kwargs={'previous_boot_time': previous_boot_time})

# Generated at 2022-06-13 10:30:21.046566
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    #Arrange
    loader = DictDataLoader({"vars": {"server.ansible_host": "1.2.3.4", "server.ansible_python_interpreter": "/usr/bin/python3"}})

# Generated at 2022-06-13 10:30:24.929687
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_action_module = ActionModule()
    result = test_action_module.run()
    assert(result['msg'] == 'Running reboot with local connection would reboot the control node.')
    print("Test run() of class ActionModule.");

# Generated at 2022-06-13 10:30:31.159098
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    results = dict(
        changed=False,
        msg=''
    )
    ansible_module = DummyActionModule()
    action = MagicMock()
    reboot_timeout = IntegerType().validate(2)
    distribution = StringType().validate("CentOS")
    action_desc = StringType().validate("last boot time check")
    try:
        ansible_module.do_until_success_or_timeout(action, reboot_timeout, action_desc, distribution)
    except:
        results['failed'] = True
        results['msg'] = "do_until_success_or_timeout did not do its job."
        pass
    assert not results['failed']
    return results



# Generated at 2022-06-13 10:31:16.937970
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    # state = None
    # action = None
    task_vars = None
    # distribution = None
    # tmp = None
    am = ActionModule(state=None, action=None, task_vars=task_vars, distribution=None, tmp=None)

    distribution = "DEBIAN"
    assert not am.get_system_boot_time(distribution) is None
    assert not am.get_system_boot_time(distribution) == ""

    distribution = "CENTOS"
    assert not am.get_system_boot_time(distribution) is None
    assert not am.get_system_boot_time(distribution) == ""

    distribution = "RANDOM"
    assert not am.get_system_boot_time(distribution) is None

# Generated at 2022-06-13 10:31:26.345075
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    # Setup test parameters
    action_module = get_action_module('reboot')

    # Setup test facts
    task_vars = dict()
    task_vars['ansible_facts'] = dict()

    # Test with no facts present
    task_vars['ansible_facts']['distribution'] = None
    task_vars['ansible_facts']['distribution_release'] = None
    task_vars['ansible_facts']['distribution_version'] = None
    task_vars['ansible_facts']['os_family'] = None

    result = action_module.get_distribution(task_vars)
    assert result == 'Generic'

    # Test with os_family present
    task_vars['ansible_facts']['distribution'] = None
    task_vars

# Generated at 2022-06-13 10:31:37.024257
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
  class AnsibleModuleMock:
    def __init__(self):
      self.params = {}
      
    class _task:
      def __init__(self):
        self.args = {}
      
  target = ActionModule(None, None)
  target._task = AnsibleModuleMock()._task()
  target._task.args = {'pre_reboot_delay': 0, 'connect_timeout_sec': 10, 'post_reboot_delay': 0, 'test_command': ''}
  target._supports_check_mode = True
  import os
  os.environ['SSH_CLIENT'] = '192.168.168.168 50475 22'
  task_vars = {}
  expected = 'default'
  actual = target.get_distribution(task_vars)

# Generated at 2022-06-13 10:31:42.691046
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    # Test that a call with a system that returns now as the boot time fails.
    action = ActionModule()
    action._low_level_execute_command = Mock(return_value={'rc': 0, 'stdout': 'now\n'})
    with pytest.raises(ValueError) as excinfo:
        action.get_system_boot_time('linux')
    assert "boot time has not changed" in str(excinfo.value)


# Generated at 2022-06-13 10:31:53.518479
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    module_config = dict(
        test_task_vars=dict(
            ansible_distribution='Debian',
            ansible_distribution_version='8'
        )
    )
    module = ActionModule(None, None, None, None)
    with mock.patch.multiple('ActionModule',
                             get_shutdown_bin=lambda self, task_vars: 'shutdown',
                             _task=mock.PropertyMock(return_value=mock.MagicMock(action='reboot',
                                                                                    args=module_config)),
                             _low_level_execute_command=lambda self, command, sudoable: dict(rc=0, stdout='shutdown')
                             ):
        result = module.get_shutdown_command(module_config['test_task_vars'])


# Generated at 2022-06-13 10:32:03.468490
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    plugin = ActionModule(
            {'action': 'reboot'},
            task=Task(
                action='reboot',
                args={'shutdown_command': None},
                module_defaults={'name': 'reboot'},
                task_vars=dict(),
                loader=None,
                templar=None,
                shared_loader_obj=None
            ),
            connection=None,
            _play_context=PlayContext()
        )

    # test platform

# Generated at 2022-06-13 10:32:09.753532
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    # Setup
    module = AnsibleModule()
    module.DEFAULT_SUDOABLE = False
    action_module = ActionModule(module, task, connection, play_context, loader, templar, shared_loader_obj)
    action_module._low_level_execute_command = MagicMock()
    distribution = 'centos'
    test_command = 'test_command'
    # Exercise
    action_module.run_test_command(distribution)
    # Verify
    action_module._low_level_execute_command.assert_called_once_with(test_command, sudoable=False)


# Generated at 2022-06-13 10:32:13.503603
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    action = ActionModule(specs={'action': 'reboot'})
    distribution = 'Ubuntu'
    action.get_shutdown_command_args(distribution)

# Generated at 2022-06-13 10:32:15.534358
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    try:
        raise RuntimeError("Unit test not implemented")
    except Exception as e:
        print("Unit test failed: " + str(e))
        raise

# Generated at 2022-06-13 10:32:18.688743
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    module = ActionModule(Connection(_load_name_conf_file=False), Playbook(), None)
    task_vars = dict(
    )
    distribution = dict(
    )
    assert module.get_shutdown_command_args(distribution=distribution) is None

# Generated at 2022-06-13 10:33:20.722395
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    pass



# Generated at 2022-06-13 10:33:26.717827
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    action_module = ActionModule()
    
    # given
    task_vars = dict(
        ansible_distribution='Debian',
        ansible_distribution_release='stretch',
        ansible_distribution_version='9.4',
        ansible_os_family='Debian',
    )
    
    # when
    distribution = action_module.get_distribution(task_vars)

    # then
    assert('Debian' == distribution)


# Generated at 2022-06-13 10:33:37.148115
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    action_module = reload(sys.modules['lib.ansible.plugins.action.reboot'])
    action_module.ActionModule.REBOOT_TIMEOUT = 2

    test_distribution = 'test'
    test_boot_time = 'Fri 20 Jan 2017 14:35:14 UTC'
    test_boot_time_command = 'echo '+test_boot_time

    connection_mock = MagicMock()

    def mock_execute_command(*args, **kwargs):
        return dict(rc=0, stdout=b'', stderr=b'', stdin=None)

    connection_mock.execute = mock_execute_command

    display_mock = MagicMock()

    action_module.ActionModule._low_level_execute_command = mock_execute_command
    action_module.ActionModule._

# Generated at 2022-06-13 10:33:50.854485
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    # Given
    action_module = ActionModule(task=Task(), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action_module._task.action = 'reboot'
    action_module._task.args = {'wait_for_reboot': 5, 'other_arg': 'value'}
    action_module.DEPRECATED_ARGS = {'wait_for_reboot': '2.4.0', 'wait_for_connection': '4.8.0'}

    # When
    try:
        action_module.deprecated_args()
        assert True
    except:
        assert False


# Generated at 2022-06-13 10:33:54.771414
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    module = ActionModule(None, None)
    arg = random.choice(['-k', '-h', '-r'])
    module._task.args = {'shutdown_timeout': arg}
    assert module.get_shutdown_command_args('redhat') == arg



# Generated at 2022-06-13 10:34:09.481365
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    # Construct an instance of the ActionModule class with a mock task and connection plugin
    task = mock.Mock()
    task.action = 'reboot'
    connection = 'local'
    action_module = ActionModule(task, connection)
    action_module._task.args = {'pre_reboot_delay': 5,
                                'post_reboot_delay': 5,
                                'connect_timeout': 5,
                                'reboot_timeout': 300,
                                'test_command': 'uptime'
                                }

    with mock.patch.object(display, 'warning') as mock_warning:
        action_module.deprecated_args()

    # Check that the warning was called four times
    assert mock_warning.call_count == 6



# Generated at 2022-06-13 10:34:20.075327
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    import sys
    import copy
    import unittest
    from unittest.mock import patch, MagicMock
    from ansible.module_utils.basic import AnsibleModule

    def get_action_mock():
        # Get an ActionModule object for testing
        class MockActionModule(ActionModule):
            def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
                super(MockActionModule, self).__init__(task, connection, play_context, loader, templar, shared_loader_obj)
                self.check_boot_time_error = None

            def check_boot_time(self, distribution, previous_boot_time):
                if self.check_boot_time_error:
                    raise self.check_boot_time_error

        return MockAction

# Generated at 2022-06-13 10:34:22.946173
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    action_module=ActionModule()
    action_module.test_gf_shell("asdf")

# Generated at 2022-06-13 10:34:31.126557
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    action_module = ActionModule(connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Let's create a imaginary distribution
    class Distribution:
        pass

    distribution = Distribution()
    distribution.os_family = 'RedHat'

    # The boot time of the distribution is not properly defined, so it returns a default boot time
    assert action_module.get_system_boot_time(distribution) == action_module.DEFAULT_BOOT_TIME_COMMAND

    # The boot time of the distribution is properly defined, so it returns the command to get it
    distribution.os_family = 'Solaris'

# Generated at 2022-06-13 10:34:38.810679
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    # Create an instance of ActionModule()
    action_module = ActionModule()
    # TODO: create mock task_vars, with return value 'system_distribution'
    # TODO: create mock system_distribution, with return value 'debian'
    
    # Test get_distribution with valid parameters
    assert action_module.get_distribution(task_vars=task_vars) == 'debian'
    
    # Test get_distribution with invalid parameters
    try:
        action_module.get_distribution(task_vars=None)
    except Exception as e:
        assert isinstance(e, AttributeError)



# Generated at 2022-06-13 10:36:50.716323
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    """Unit test for method get_shutdown_command_args of class ActionModule"""
    
    # function test_ActionModule_get_shutdown_command_args
    def test(dist, result_expected):
        """
        Parameters
        ----------
            dist: str
                Linux distribution
            result_expected: str
                Expected result
        """
        
        result = None
        try:
            result = ActionModule.get_shutdown_command_args(dist)
        except Exception as e:
            print("Exception thrown in ActionModule.get_shutdown_command_args:")
            raise e
        if result != result_expected:
            raise Exception("result != result_expected where result = {0} and result_expected = {1}".format(result, result_expected))
    
    # test case
    dist = {}
   
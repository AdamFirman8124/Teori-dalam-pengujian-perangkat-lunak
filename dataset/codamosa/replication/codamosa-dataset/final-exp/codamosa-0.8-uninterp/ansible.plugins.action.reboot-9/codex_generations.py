

# Generated at 2022-06-13 10:27:20.883788
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    # Boot time test command failure
    boot_time_command = 'exit 1'
    module = ActionModule()
    distribution = 'redhat'
    try:
        module.run_test_command(distribution)
        raise AssertionError('Test command succeeded when it should have failed.')
    except RuntimeError:
        pass

    # No test command provided
    boot_time_command = ''
    module = ActionModule()
    distribution = 'redhat'
    module.run_test_command(distribution)

    # Test command success
    boot_time_command = 'exit 0'
    module = ActionModule()
    distribution = 'redhat'
    module.run_test_command(distribution)

# Generated at 2022-06-13 10:27:32.455740
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    collection_list = ('reboot',)
    task = AnsibleTask(collection_list, 'reboot', 'localhost', 'test_host')
    am = ActionModule(task, 'library', 'reboot', connection='smart', port=22, _play_context=play_context, loader=None, templar=None, shared_loader_obj=None, **kwargs)
    task_vars = {'ansible_facts': {}}
    assert am.get_distribution(task_vars) == 'default'

    task_vars = {'ansible_facts': {'distribution': 'MAJOR'}}
    assert am.get_distribution(task_vars) == 'major'

    task_vars = {'ansible_facts': {'distribution': 'MAJOR'}}
    assert am.get

# Generated at 2022-06-13 10:27:40.505470
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    net_os = {
        'distribution': 'Debian',
        'distribution_version': '7'
    }
    self = ActionModule()
    self.DEFAULT_SHUTDOWN_BIN = 'shutdown'
    self.DEFAULT_SUDOABLE = True
    result = self.get_shutdown_command(net_os)
    assert result == 'sudo shutdown'



# Generated at 2022-06-13 10:27:43.038142
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    pass

# Generated at 2022-06-13 10:27:45.701208
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    d = {}
    testobj = ActionModule(d, d)
    testobj.do_until_success_or_timeout()
    assert False  # TODO: implement your test here



# Generated at 2022-06-13 10:27:48.365280
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    action_module = ActionModule()
    distribution = 'debian'
    action_module.run_test_command(distribution=distribution)

# Generated at 2022-06-13 10:27:56.251042
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    fake_module = None
    action_module = ActionModule(self=fake_module, task=fake_task, connection=fake_connection, play_context=fake_play_context)
    distribution = 'a_distribution'

    # Test when BOOT_TIME_COMMAND is not None
    boot_time_command = 'boot_time_command'
    action_module._task.args['boot_time_command'] = boot_time_command
    action_module.get_system_boot_time(distribution)
    assert action_module.get_system_boot_time.call_count == 1
    assert action_module.get_system_boot_time.call_args == call(distribution)

    # Test when BOOT_TIME_COMMAND is None

# Generated at 2022-06-13 10:28:04.407340
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    results = {}
    results['failed'] = True
    results['changed'] = True
    results['msg'] = 'unable to retrieve system boot time'
    # Stub out method run_test_command to fail
    with pytest.raises(Exception) as e:
        ActionModule.run_test_command(ActionModule(task=None, connection=None, play_context=None), 'rhel', **results)
    assert to_native(e.value) == 'unable to retrieve system boot time'

# Generated at 2022-06-13 10:28:15.844269
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    import time
    import collections

    _task_vars = {'test_distribution': 'test'}
    def raise_test_exception():
        raise TestException

    def raise_test_timeout_exception():
        raise RuntimeError()

    def raise_ansible_connection_failure():
        raise AnsibleConnectionFailure

    def get_system_boot_time(_distribution):
        raise TestException

    def check_boot_time(_distribution, previous_boot_time):
        ''' this is a successful check_boot_time '''
        # FreeBSD returns an empty string immediately before reboot so adding a length
        # check to prevent prematurely assuming system has rebooted
        if len(previous_boot_time) == 0:
            raise TestException
        else:
            return


# Generated at 2022-06-13 10:28:23.660313
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    def get_task():
        return MockTask()
    def get_connection(self):
        return MockConnection(self)
    def get_variable(self, variable):
        return MockFact(variable)
    # 
    # set up test case
    # 
    class TestActionModule(ActionModule):
        _supports_check_mode = True
        _supports_async = True
        DEFAULT_SUDOABLE = True
        DEFAULT_CONNECT_TIMEOUT = 60
        DEFAULT_REBOOT_TIMEOUT = 300

# Generated at 2022-06-13 10:28:56.418854
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    from ansible.modules.system import reboot as reboot_module

    # GIVEN
    module = reboot_module.ActionModule()
    module.run_test_command("testing")

# Generated at 2022-06-13 10:29:05.338686
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    
    ansible_module = AnsibleModule(
        argument_spec = dict(
            reboot_timeout = dict(default=600, type='int', aliases=['reboot_timeout_sec'])
        )
    )
    module = a_module.ActionModule(
       connection = ansible_module.connection,
       _connection_info = ansible_module.connection_info,
       _task_vars = dict(),
       _task = dict(action='reboot', args=dict())
    )
    
    fact_cache = dict()
    fact_cache['distribution'] = None

    task_vars = dict()
    task_vars['ansible_facts'] = dict()
    task_vars['ansible_facts']['ansible_distribution'] = 'Debian'

# Generated at 2022-06-13 10:29:12.210351
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    hostvars = dict()
    module_defaults = dict()
    set_module_defaults(module_defaults)
    # Class instantiation of the module
    module = ActionModule(
        connection=None,
        _new_stdin=None,
        _task_vars=hostvars,
        _task_args=dict(
            connect_timeout='300',
            msg='system going down for maintenance NOW'),
        _ansible_debug=True,
        _play_context=None,
        loader=None,
        _shared_loader_obj=None,
        templar=None,
        # args=dict(),
    )

    assert isinstance(module, ActionModule)
    module.deprecated_args()

###############################################################################
# Unit tests for class ActionModule
###############################################################################



# Generated at 2022-06-13 10:29:19.845940
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():

    args = { 'connect_timeout' : 'connect_timeout_sec' }

    # attempt to load deprecated_args function
    module = load_module_util('/Users/sadafriaz/ansible-reboot', 'reboot')
    module.ActionModule._deprecated_args = args

    # attempt to load instance of class with deprecated_args function
    instance = module.ActionModule({})
    assert hasattr(instance, '_deprecated_args')
    assert instance._deprecated_args == args


# Generated at 2022-06-13 10:29:21.938040
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    # action_module.ActionModule.perform_reboot(task_vars, distribution)
    #
    # TODO: implement here
    return None

# Generated at 2022-06-13 10:29:23.666989
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    action_module = ActionModule()
    # TODO: Write unit test
    assert False == True


# Generated at 2022-06-13 10:29:31.560183
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
        host = MagicMock()
        task = MagicMock()
        connection = Connection(host=host, task=task, play_context=MagicMock())
        connection._shell = Shell()

        task.action = 'reboot'
        task.args = {}

        am = ActionModule(task, connection, play_context=MagicMock(), loader=MagicMock(), templar=MagicMock(), shared_loader_obj=None)
        am._low_level_execute_command = MagicMock()
        am.get_system_boot_time = MagicMock()

        # Case 1: am.get_system_boot_time returns a value
        am.get_system_boot_time.return_value = 'foo'
        am.check_boot_time('distribution', 'foo')
        assert am._low_level_execute_

# Generated at 2022-06-13 10:29:44.650422
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    fixture_path = os.path.join(fixtures_path, 'ActionModule_do_until_success_or_timeout')
    module_utils = os.path.join(fixture_path, 'module_utils.py')
    m = imp.load_source('module_utils', module_utils)
    action = ActionModule()
    distribution_dict = {'os_name': 'OS', 'os_family': 'OSFAMILY'}
    class_inst = m.FakeActionModule()
    count = 0
    while count < 8:
        count += 1
        class_inst.count = count
        action.do_until_success_or_timeout(class_inst.raise_func, action_desc='test', reboot_timeout=10, distribution=distribution_dict, action_kwargs={})


# Generated at 2022-06-13 10:29:45.724372
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    pass



# Generated at 2022-06-13 10:29:50.505193
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    # create an instance of class ActionModule
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # create an instance of class Task to pass on as an argument
    task = Task()

    # create an instance of class TaskExecutionContext to pass on as an argument
    class TaskExecutionContext:
        def __init__(self, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None):
            self.task = task
            self.connection = connection
            self.play_context = play_context
            self.loader = loader
            self.templar = templar
            self.shared_loader_obj = shared_loader_obj

    task

# Generated at 2022-06-13 10:30:53.394473
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    action_module = ActionModule()
    result = action_module.run_test_command(['cat', '/etc/redhat-release'])
    assert result['rc'] == 0, "Test command failed"


# Generated at 2022-06-13 10:30:59.081734
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    # Test a simple case
    task = AnsibleTask()
    action_module = ActionModule(task=task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    task_vars = {}
    distribution = ""
    # Test if the method correctly returns a result with all fields
    assert action_module.perform_reboot(task_vars, distribution) == {"start": datetime.utcnow(), "failed": True, "rebooted": False, "msg": "Reboot command failed. Error was: 'None, None'"}


# Generated at 2022-06-13 10:31:07.030847
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    import unittest

    class ActionModuleTestCase(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            cls._connection = MockConnection()
            cls._task = MockTask()

            cls._action_module = ActionModule(
                cls._connection,
                cls._task,
                connection_loader=None,
                play_context=None,
                loader=None,
                templar=None,
                shared_loader_obj=None)

        @classmethod
        def tearDownClass(cls):
            del cls._action_module

        def setUp(self):
            mock_ansible_connection(self._connection)

        def tearDown(self):
            pass


# Generated at 2022-06-13 10:31:18.246308
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    action_module = ActionModule(execute_module=None, async_val=None,
                                 no_log_val=None, task_vars_val=None,
                                 wrap_async_val=None, wrap_name_val=None,
                                 task_name_val=None, job_id_val=None,
                                 seq_val=None, play_context_val=None,
                                 loader_val=None, connection_info_val=None,
                                 module_path_val=None, task_uuid_val=None,
                                 environment_val=None, connection_name_val=None)

    # test when distribution is not specified
    result = action_module.get_shutdown_command_args(distribution=None)
    assert result == "-r now"

    # test with distribution which is other

# Generated at 2022-06-13 10:31:23.283819
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    Task = collections.namedtuple('Task', ['action'])
    action_module_instance = ActionModule()
    action_module_instance._task = Task(action="reboot")
    assert action_module_instance._get_value_from_facts('BOOT_TIME_COMMANDS', 'Debian', 'DEFAULT_BOOT_TIME_COMMAND') == 'uptime -s'


# Generated at 2022-06-13 10:31:28.060734
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    test_obj = create_test_obj(ActionModule)
    test_data = get_test_data(['centos6', 'centos7', 'debian', 'freebsd', 'opensuse'])
    for distribution, facts in test_data.items():
        test_obj._handle_exception = MagicMock()
        test_obj.get_distribution(facts)
        test_obj._handle_exception.assert_not_called()
    # Test not found
    test_obj._handle_exception = MagicMock()
    test_obj.get_distribution({})
    test_obj._handle_exception.assert_called_once_with(
        "Failed to determine OS type while gathering distribution information")


# Generated at 2022-06-13 10:31:38.856659
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    # Initialize fixture
    mock_distribution = 'mock_distribution'
    mock_previous_boot_time = 'mock_previous_boot_time'
    mock_check_boot_time_func = 'mock_check_boot_time_func'
    mock_ConnectionError = 'mock_ConnectionError'
    mock_ValueError = 'mock_ValueError'
    mock_Exception = 'mock_Exception'
    mock_RuntimeError = 'mock_RuntimeError'
    mock_AnsibleError = 'mock_AnsibleError'
    mock_AnsibleError_set_option = 'mock_AnsibleError_set_option'
    mock_AnsibleError_reset = 'mock_AnsibleError_reset'

    # Initialize test class
    mock_ansible_

# Generated at 2022-06-13 10:31:45.944345
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    fact_cache = dict()
    fact_cache['distribution'] = 'CentOS'
    action_module_obj = ActionModule(play_context=dict(), connection=dict(), loader=None, templar=None, shared_loader_obj=None)
    action_module_obj._task.args = dict()
    result = action_module_obj._get_shutdown_command_args(fact_cache['distribution'])
    assert result == '-r now'
    fact_cache['distribution'] = 'MacOS'
    result = action_module_obj._get_shutdown_command_args(fact_cache['distribution'])
    assert result == '-r now'


# Generated at 2022-06-13 10:31:55.525526
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    logfile = 'ansible-test.log'
    with codecs.open(logfile, 'a', encoding='utf-8') as f:
        f.write('\n=== test_ActionModule_validate_reboot ===\n')

    class MockTaskAction(object):
        def __init__(self, action):
            self.action = action

        def __str__(self):
            return self.action

    class MockTaskArgs(object):
        def __init__(self, **kwargs):
            self.update(kwargs)

        def update(self, kwargs):
            self.__dict__.update(kwargs)

    class MockTask(object):
        def __init__(self, action, args=None):
            self.action = action
            self.args = args


# Generated at 2022-06-13 10:31:58.554511
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    task_vars = {}
    self = ActionModule(self, task_vars)
    task_vars = {}
    distribution = {}

    self.get_shutdown_command(task_vars, distribution)

# Generated at 2022-06-13 10:33:53.917076
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    action_module = ActionModule()
    dist = 'foo'
    action_module._task.args = {'test_command': '/bin/echo 1'}
    action_module.run_test_command(dist)


# Generated at 2022-06-13 10:33:57.464288
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    action_module = ActionModule()
    assert action_module.get_shutdown_command_args() == ' -r now'


# Generated at 2022-06-13 10:34:12.395842
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    """Test method deprecated_args of class ActionModule.
    """
    from ansible.utils.plugin_docs import gen_docstring
    docstring = gen_docstring(ActionModule, for_doc=True)
    assert 'deprecated_args' in docstring
    assert 'DEPRECATED_ARGS' in docstring
    # ActionModule.DEPRECATED_ARGS = dict(reboot_timeout=2.5, reboot_timeout_sec=2.5,
    #                                     connect_timeout=2.5, connect_timeout_sec=2.5)
    dep_args = dict(reboot_timeout=2.5, reboot_timeout_sec=2.5, connect_timeout=2.5, connect_timeout_sec=2.5)
    task = dict(action=dict(reboot_timeout=1))
    # action

# Generated at 2022-06-13 10:34:21.796057
# Unit test for method deprecated_args of class ActionModule

# Generated at 2022-06-13 10:34:28.528104
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
	''' Test perform_reboot of class ActionModule'''
	print('Test ActionModule.perform_reboot')
	task_vars = {}
	distribution = 'test'
	test_obj = ActionModule(self=None, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
	return_value = test_obj.perform_reboot(task_vars, distribution)
	print('End ActionModule.perform_reboot')
	return return_value

# Generated at 2022-06-13 10:34:30.243088
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    class ActionModule:
        class Run(ActionModule):
            Run.run(ActionModule,tmp,task_vars)
    assert True

# Generated at 2022-06-13 10:34:31.338305
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    pass



# Generated at 2022-06-13 10:34:40.491985
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    # Test 1
    module = ActionModule()
    action_vars = {'ansible_distribution': 'Debian'}
    expected_result = 'Debian'
    result = module.get_distribution(action_vars)
    assert result == expected_result

    # Test 2
    module = ActionModule()
    action_vars = {'ansible_distribution_major_version': '8'}
    expected_result = 'Debian'
    result = module.get_distribution(action_vars)
    assert result == expected_result

    # Test 3
    module = ActionModule()
    action_vars = {'ansible_distribution': 'Debian', 'ansible_distribution_major_version': '8'}
    expected_result = 'Debian'
    result = module.get_dist

# Generated at 2022-06-13 10:34:45.230425
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    Task_module = ActionModule()
    ditribute = "Ubuntu"
    result = Task_module.get_system_boot_time(ditribute)
    assert result == "echo `date -d \"$(uname -s -r)\" \"+%Y-%m-%d %H:%M:%S\"`"
    #assert string_splitter("'hello world'", "'") == ['hello world']

Task_module = ActionModule()
#task_vars = dict()
task_vars = {"ansible_distribution": "Ubuntu"}
a = Task_module.get_distribution(task_vars)

# Generated at 2022-06-13 10:34:54.517173
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    hostvars = {}
    task_vars = {'hostvars': hostvars}
    args = {}
    module = ActionModule(None, task_vars=task_vars, args=args)
    assert datetime.strptime(module.get_system_boot_time('Fedora'), '%Y-%m-%d %H:%M:%S') > datetime.utcnow() - timedelta(days=2)

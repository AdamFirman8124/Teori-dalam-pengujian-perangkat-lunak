

# Generated at 2022-06-13 10:27:17.586729
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult

    class RunnerMock(object):
        def __init__(self):
            self._shared_loader_obj = None
            self._loader = None
            self._templar = None
            self._connection = None
            self._low_level_execute_command = None
            self.tmpdir = None

    class ConnectionMock(object):
        def __init__(self, transport, got_password=False, remote_user=None, sudo_pass=None, connection_timeout=None, network_os=None):
            self.transport = transport
            self.got_password = got_password
            self.remote_user = remote_user
            self.sudo_pass = sudo_pass
            self.connection_

# Generated at 2022-06-13 10:27:19.949241
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    device_instance = ActionModule()
    result = device_instance.validate_reboot(distribution, original_connection_timeout, action_kwargs)
    assert(result == "")

# Generated at 2022-06-13 10:27:31.175482
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    connection = Connection()
    tmp = None

# Generated at 2022-06-13 10:27:44.252035
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    # Only run this test if the plugin is in fact an instance of ActionModule
    from ansible import module_utils
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.action.reboot import ActionModule as _ActionModule
    if ActionModule != _ActionModule:
        # This is a way to make this unit test not run on the instance of ActionModule
        # on the ansible/modules pythonpath - even if it passes the check above.
        from importlib import import_module
        a_module_utils = import_module('ansible.plugins.action.reboot')
        a_ActionModule = a_module_utils.ActionModule

# Generated at 2022-06-13 10:27:45.617377
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    evaluate_result('reboot', 'perform_reboot', 'reboot', ActionModule)

# Generated at 2022-06-13 10:27:54.013230
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    from ansible.modules.system.reboot import DEFAULT_FORCE_OPTIONS
    from ansible.modules.system.reboot import DEFAULT_DELAY_OPTION

    search_paths = ['/bin', '/sbin', '/usr/bin', '/usr/sbin']
    for default_path in search_paths:
        for force_option, delay_option in zip(DEFAULT_FORCE_OPTIONS, DEFAULT_DELAY_OPTION):
            am = ActionModule({
                'path': ''
            })

            # test that returned result is the expected
            result = am.get_shutdown_command_args(distribution='redhat', force_option=force_option, delay_option=delay_option)
            assert result == ''


# Generated at 2022-06-13 10:28:06.294374
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    # mock self._get_value_from_facts
    def _get_value_from_facts(e1, e2, e3):
        return None
    # mock self._task
    _task = Mock()
    _task.action = 'test_get_system_boot_time'

    # mock self._low_level_execute_command
    def _low_level_execute_command(e1, e2):
        return {'rc': 0, 'stdout': '2015-07-18 14:35:09 -0700'}

    # get the object
    am = ActionModule()
    am._get_value_from_facts = _get_value_from_facts
    am._task = _task
    # mock protected member _low_level_execute_command
    am._low_level_execute_command = _low_

# Generated at 2022-06-13 10:28:12.150999
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
  class MockConnection:
    class transport:
      class value:
        name = "name"

    class become_method:
      value = "value"

    def __init__(self):
      self.transport = self.transport()
      self.become_method = self.become_method()

  class MockPlayContext:
    def __init__(self):
      self.become = "become"
      self.become_user = "become_user"

  class MockTaskExecutionContext:
    def __init__(self):
      self.connection = "connection"
      self.playbook_name = "playbook_name"
      self.task_name = "task_name"

  class MockTask:
    def __init__(self):
      self.execution = self.execution()

   

# Generated at 2022-06-13 10:28:16.165705
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    # command = get_shutdown_command(task_vars, distribution)
    raise NotImplementedError


# Generated at 2022-06-13 10:28:19.452597
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	host = Host('ssh://localhost')
	host.set_variable('ansible_user', '')

	action = ActionModule(task=Task(), connection=Connection(host))
	result = action.run(tmp='', task_vars={})
	assert result['failed']

# Generated at 2022-06-13 10:28:59.073079
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts.system.distribution import Distribution

    am = ActionModule('test')

    # test for default case, ansible_facts should have ansible_distribution set
    facts = Facts()
    dist = Distribution()
    defaults = [
        'ansible_facts',
        'distribution'
    ]
    dist.populate(defaults)

    facts.populate(dist=dist)
    results = am.get_distribution({'ansible_facts': facts.serialize()})
    assert results == dist.name

    # test that if ansible_distribution is set, ansible_facts is not used
    facts = Facts()
    dist = Distribution()
    defaults = [
        'distribution'
    ]

# Generated at 2022-06-13 10:29:06.963204
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():

    # Initialize task vars
    task_vars = {}

    # Initialize distribution
    distribution = None

    # Initialize instance of ActionModule
    module = ActionModule()

    # Run perform_reboot method of class ActionModule and store result
    result = module.perform_reboot(task_vars, distribution)

    # Assert
    # Test if result is not a dictionary
    if not isinstance(result, dict):
        raise AssertionError('result is not a dictionary')

    # Test if rebooted key of result is not a boolean
    if not isinstance(result['rebooted'], bool):
        raise AssertionError('rebooted key of result is not a boolean')

    # Test if changed key of result is not a boolean
    if not isinstance(result['changed'], bool):
        raise Assertion

# Generated at 2022-06-13 10:29:12.395456
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    # Tests on ActionModule._get_value_from_facts, _get_distribution, _get_shutdown_command_args and _get_shutdown_command methods
    # are performed in other unit tests without hacking the instance variable
    try:
        module.deprecated_args()
    except Exception as e:
        assert False, "ActionModule.deprecated_args() raised an unexpected exception: {}".format(e)
# Tests on ActionModule._get_value_from_facts, _get_distribution, _get_shutdown_command_args and _get_shutdown_command methods
# are performed in other unit tests without hacking the instance variable

# Generated at 2022-06-13 10:29:21.073398
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
  action_module = ActionModule({},{},{},{},{},{})

  # Obtain an instance of the class this class wraps
  runner_action_base = action_module.runner_action_base
  class_name = runner_action_base.__class__.__name__

  # Unit test setup
  try:
    # Perform test
    action_module.deprecated_args()
  except:
    # Cleans up after the test
    runner_action_base.__dict__ = runner_action_base._saved_action_base_attributes
    delattr(action_module, 'runner_action_base')
    delattr(action_module, '_saved_runner_action_base_attributes')
    # Checks if test successful

# Generated at 2022-06-13 10:29:29.495628
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    print('ActionModule.get_shutdown_command_args')

    distribution = 'RedHat'

# Generated at 2022-06-13 10:29:37.769958
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    # Instantiate mock action module
    action_module = ActionModule()
    action_module._task.args = {}
    action_module._task.args['reboot_timeout'] = 300
    action_module._task.args['connect_timeout'] = 60

    # A mock distribution
    distribution = 'Mock_Dist'

    # Call ActionModule.get_shutdown_command_args
    res = action_module.get_shutdown_command_args(distribution)
    assert res == '-r now'

# Generated at 2022-06-13 10:29:48.024864
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    # Setup and initialize the class
    test_action_module = ActionModule(task=dict(), connection=None, play_context=dict(), loader=None, templar=None, shared_loader_obj=None)
    test_task_vars = dict()
    test_distribution = 'Linux'
    expected_result = '/sbin/shutdown'

    # Run the method
    result = test_action_module.get_shutdown_command(test_task_vars, test_distribution)

    # Assertion
    assert result == expected_result


# Generated at 2022-06-13 10:30:01.053671
# Unit test for method get_shutdown_command_args of class ActionModule

# Generated at 2022-06-13 10:30:02.829836
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    action_module = ActionModule()
    # result = action_module.get_shutdown_command_args(
    #     distribution,
    #     task_vars
    # )
    assert False

# Generated at 2022-06-13 10:30:07.431190
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    def test_action_module_check_boot_time(mocker):
        test_action_module = ActionModule()

        check_boot_time_mock = mocker.patch.object(ActionModule, 'check_boot_time')

        test_action_module.check_boot_time()
        check_boot_time_mock.assert_called_once()

    test_action_module_check_boot_time(mocker)


# Generated at 2022-06-13 10:31:20.834939
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    from ansible.inventory.host import Host
    from ansible.executor.task_result import TaskResult
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.plugins.loader import get_plugin_loader

    loader = get_plugin_loader(get_all_plugin_loaders(), 'TestActionModule')

    # Used for testing
    class TaskExecutor(object):
        def __init__(self, connection):
            self.connection = connection

        def execute(self, task, tmp=None, task_vars=None, **kwargs):
            return self.connection.execute(task, tmp, task_vars)

    class Task(object):
        def __init__(self, action):
            self.action = action
            self.args = kwargs


# Generated at 2022-06-13 10:31:29.470724
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():

    from ansible.module_utils._text import to_bytes, to_native
    from ansible.module_utils.common.collections import ImmutableDict
    import ansible.module_utils.connection as connection

    module_name = 'reboot'
    module_args = {
        'connect_timeout': 10,
        'reboot_timeout': 10,
        'test_command': 'uname -a'
    }

    class Connection(object):

        def __init__(self):
            self.module_name = module_name
            self.module_args = module_args
            self.socket_path = None

        def get_option(self, key):
            self.module_args[key]

        def set_option(self, key, value):
            self.module_args[key] = value


# Generated at 2022-06-13 10:31:32.508962
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    module = AnsibleModule()
    action_module = ActionModule(module)
    action_module.check_boot_time("dummy")
    assert 1 == 1


# Generated at 2022-06-13 10:31:36.313044
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    action_module = get_module_obj()

    action_module._task.args = {'connect_timeout': 1, 'msg': 'System is going down for reboot NOW!', 'delay': 1}
    action_module._connection.transport = 'ssh'
    action_module.post_reboot_delay = 0

    task_vars = {'ansible_facts': {'distribution': 'CentOS', 'distribution_major_version': '7'}}

    assert action_module.perform_reboot(task_vars, 'CentOS')['failed'] is False



# Generated at 2022-06-13 10:31:45.007188
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    from ansible.module_utils.basic import AnsibleModule
    from shutil import rmtree

    def setup_mock_ansible_module(tmp_path):
        module_args = dict(
            test_command='/bin/true',
            reboot_timeout=0
        )
        module_args.update(DEFAULT_ARG_SPEC)

        am = AnsibleModule(
            argument_spec=module_args
        )


# Generated at 2022-06-13 10:31:52.986254
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    my_ActionModule = get_test_ActionModule()
    setattr(my_ActionModule, '_low_level_execute_command', fake_low_level_execute_command)
    result = my_ActionModule.run_test_command(
        distribution=my_distribution,
        action_desc=my_action_desc,
        reboot_timeout=my_reboot_timeout,
        **{'previous_boot_time': my_previous_boot_time}
    )
    assert result is None


# Generated at 2022-06-13 10:32:03.048393
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.inventory.host import Host
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    action_module = ActionModule(
        Task(),
        VariableManager(),
        'fake_host',
        'fake_connection',
    )
    action_module._play_context.check_mode = False
    action_module.get_distribution = Mock(return_value='fake_distro')
    action_module.get_shutdown_command = Mock(return_value='shutdown')
    action_module.get_shutdown_command_args = Mock(return_value='-r now')
    action_module.get_system_boot_time = Mock(return_value='fake_boot_time')

# Generated at 2022-06-13 10:32:14.954995
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    # Create a dummy class
    class DummyClass(ActionModule):
        def _load_params(self):
            self.msg = 'Test'
            self.play_context = None
            self.playbook = None
            self.DEFAULT_SUDOABLE = True
            self.DEFAULT_CONNECT_TIMEOUT = 10
            self.DEFAULT_REBOOT_TIMEOUT = 600
            self.FACTS_TO_DISTRIBUTION = dict()
            self.distribution = 'AmigaOS'
            self.KERNEL_REBOOT_RETURN_CODES = []
            self.TEST_COMMANDS = dict()
            self.BOOT_TIME_COMMANDS = dict()
            self.init_command = 'blah'

    dummy_obj = DummyClass()
    dummy_obj._

# Generated at 2022-06-13 10:32:15.653378
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    pass

# Generated at 2022-06-13 10:32:22.193053
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    actionmodule = ActionModule()
    # Test with good input
    test_task_vars = {'ansible_distribution': 'test_distribution'}
    result = actionmodule.get_distribution(test_task_vars)
    assert result == 'test_distribution'

    # Test with bad input
    test_task_vars = {'ansible_distribution': None}
    result = actionmodule.get_distribution(test_task_vars)
    assert result is None
    test_task_vars = None
    result = actionmodule.get_distribution(test_task_vars)
    assert result is None


# Generated at 2022-06-13 10:34:33.459494
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():

    # Initialize a test task object
    task = mock.Mock()
    # Define task action for rest of code
    task.action = 'reboot'
    task.args = {}

    # Build the ActionModule object
    ActionModule_obj = ActionModule(task, mock.Mock())

    # Set up test parameters
    action = ActionModule_obj.check_boot_time
    action_desc = 'test action'
    reboot_timeout = 13
    distribution = None
    action_kwargs = {}

    # Call method

# Generated at 2022-06-13 10:34:39.983123
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    # pylint: disable=too-many-statements
    action_module = ActionModule()
    action_module._task = Task()
    action_module._task.action = 'reboot'
    action_module._task.args = {'reboot_timeout': 10}
    action_module._connection = Connection()
    action_module._connection.transport = 'ssh'
    # 'reboot' command does not exist
    setattr(action_module._low_level_execute_command, 'return_value', {'rc': 2, 'stdout': '', 'stderr': 'reboot: Need to be root\n'})
    def get_value_from_facts(key, distro, default_value):
        return 'reboot'

# Generated at 2022-06-13 10:34:45.902149
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    def shutdown_command(self, task_vars, distribution):
        if self._task.args.get('shutdown_command'):
            shutdown_command = self._task.args.get('shutdown_command')
            return shutdown_command

        try:
            return task_vars['shutdown_command']
        except KeyError:
            pass


# Generated at 2022-06-13 10:35:00.579742
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    for distribution, patterns in {'centos': ['CentOS', 'Red Hat'], 'ubuntu': ['Ubuntu']}.items():
        data = {'TEST_COMMANDS': {distribution: 'echo "OK"'},
                'BOOT_TIME_COMMANDS': {distribution: 'echo "1970-01-01 00:00:00 UTC"'}}
        facts = dict()
        facts['distribution'] = 'centos'
        facts['lsbmajdistrelease'] = '7'
        facts['lsbminordistrelease'] = '3'
        facts['kernel_name'] = 'Linux'
        facts['processor'] = 'Intel(R) Xeon(R) CPU E5-2660 0 @ 2.20GHz'
        facts['product_name'] = 'KVM'

# Generated at 2022-06-13 10:35:01.103446
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:35:02.488363
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    pass

# Generated at 2022-06-13 10:35:06.433471
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    action_module = ActionModule()
    action_module._task = Mock()
    action_module._task.action = "test_action"
    action_module._task.args = {
        "shutdown_timeout": 10,
        "post_reboot_delay": 20,
        "wait_for_reboot": 30,
        "reboot_timeout": 40
    }
    action_module.DEPRECATED_ARGS= {
        "shutdown_timeout": "2.5",
        "post_reboot_delay": "2.5",
        "wait_for_reboot": "2.5",
        "reboot_timeout": "2.5"
    }
    action_module.deprecated_args()


# Generated at 2022-06-13 10:35:16.696451
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    distro = Distribution(distro='test_distro', major_version='major', minor_version='minor')
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    module._low_level_execute_command = Mock()
    module._low_level_execute_command.return_value = {'rc':0}
    module.run_test_command(distribution=distro)
    assert module._low_level_execute_command.call_count == 1

# Generated at 2022-06-13 10:35:18.431903
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    action_module = ActionModule()
    action_module.get_distribution({})

# Generated at 2022-06-13 10:35:25.215126
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import Mock, call, patch

    platform_patcher = patch('platform.dist')
    lsb_release_patcher = patch('ansible_collections.notstdlib.moveitallout.plugins.modules.system.reboot.reboot._lsb_release')
    lsb_release_patcher.start()

    platform = Mock()
    platform_patcher.start()

    am = ActionModule(Mock(), Mock())
    am.DEFAULT_DISTRIBUTION = 'default_distribution'

    platform.return_value = ('debian', '8', 'jessie')
    assert am.get_distribution({}) == 'debian'

    platform.return_value = ('redhat', '7', '0')

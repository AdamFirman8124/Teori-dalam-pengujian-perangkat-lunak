

# Generated at 2022-06-13 10:27:15.400191
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    action = ActionModule()

# Generated at 2022-06-13 10:27:21.571082
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    host = Mock()
    host.system_info = {'distribution': 'test-dist'}

    action_module = ActionModule(task=Mock(), connection=Mock(), play_context=Mock())
    action_module._low_level_execute_command = Mock(return_value={'rc': 0})

    action_module.check_boot_time = Mock()
    action_module.run_test_command = Mock()
    action_module.validate_reboot(distribution=host.system_info['distribution'])

    action_module.check_boot_time.assert_called_once()
    action_module.run_test_command.assert_called_once()

# Generated at 2022-06-13 10:27:22.827586
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    pass

# Generated at 2022-06-13 10:27:27.933338
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    am = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None,
    )
    distribution = 'DISTRIBUTION'
    expected_command = 'expected_command'

    my_boolean = True
    my_int = 1
    my_list = ["item0", "item1"]
    my_dict = {
        "key0": "value0",
        "key1": "value1",
    }

    # check if get_system_boot_time can handle ValueError

# Generated at 2022-06-13 10:27:36.786197
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    # declare return variables
    results = {}
    ansible_module_get_system_boot_time = {}
    # initialize return variables
    results["actual"] = {}
    results["expected"] = {}
    # Instantiate the class
    obj = ActionModule()
    # call get_system_boot_time method and store the result in ansible_module_get_system_boot_time
    result = obj.get_system_boot_time(distribution=None)
    ansible_module_get_system_boot_time = result
    # compare the results
    results["actual"]["ansible_module_get_system_boot_time"] = ansible_module_get_system_boot_time
    print(results)


# Generated at 2022-06-13 10:27:47.842770
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    class Obj:
        def __init__(self, x):
            self.x = x


# Generated at 2022-06-13 10:27:54.729589
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    # test_ActionModule_check_boot_time() : Test whether ActionModule class method check_boot_time() works as expected. Return True if it does else return False.
    display.vvv("test_ActionModule_check_boot_time()")
    task_vars = dict()
    self_ = ActionModule(self, task_vars)
    # Test if the method check_boot_time() raises a TimedOutException.

# Generated at 2022-06-13 10:28:07.869804
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    ad_hoc_module = {
        'argument_spec': {
            'reboot_timeout': {'default': 10},
            'connect_timeout': {'default': 2},
        },
        '_name': 'reboot',
        'action': 'reboot',
    }

    class ActionModule(object):
        class Connection(object):
            def __init__(self, connection_timeout, transport):
                self.connection_timeout = connection_timeout
                self.transport = transport

            def get_option(self, key):
                if key == 'connection_timeout':
                    return self.connection_timeout
                return None

            def set_option(self, key, value):
                if key == 'connection_timeout':
                    self.connection_timeout = value

            def reset(self):
                pass


# Generated at 2022-06-13 10:28:16.928522
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():

    # Check that when function returns the function should stop
    def check_boot_time():
        raise RuntimeError

    # Check that when method returns the function should stop
    def perform_reboot():
        raise RuntimeError

    # Check that when method returns the function should stop
    def run_test_command():
        raise RuntimeError

    # Check that do_until_success_or_timeout raises a TimedOutException.
    # Method check_boot_time should never return

    # Check that do_until_success_or_timeout raises a TimedOutException.
    # Method perform_reboot should never return

    # Check that do_until_success_or_timeout raises a TimedOutException.
    # Method run_test_command should never return

# Generated at 2022-06-13 10:28:17.936128
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:28:53.246325
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    action_module = ActionModule()
    # Determine the shutdown command to execute
    # test is_shutdown_command_set_in_action_args
    # dummy test
    assert True



# Generated at 2022-06-13 10:28:54.867417
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    pass


# Generated at 2022-06-13 10:28:57.365159
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    a = AnsibleAction()
    test_return_value = a.get_distribution("test")
    return test_return_value


# Generated at 2022-06-13 10:29:05.849143
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    from ansible.module_utils.basic import AnsibleModule
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.common.text.converters import to_text

    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
        mutually_exclusive=[],
        required_together=[]
    )

    mod = ActionModule(
        module=module,
        task_vars={'ansible_facts': {}}
    )

    # check_boot_time is private, so we must manually test it.
    with pytest.raises(ValueError):
        mod._check_boot_time('test')

    time.sleep(1)
    with pytest.raises(ValueError):
        mod._check_boot_time('test')

    time

# Generated at 2022-06-13 10:29:17.152242
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    class TestException(Exception):
        pass

    class TestActionModule(ActionModule):
        def __init__(self, *args, **kwargs):
            self.test_action = None

        def make_action_fail(self, *args, **kwargs):
            raise TestException()

        def make_action_succeed(self, *args, **kwargs):
            pass

    action_module = TestActionModule()

    def make_action_fail(self, *args, **kwargs):
        action_module.test_action = action_module.make_action_fail

    def make_action_succeed(self, *args, **kwargs):
        action_module.test_action = action_module.make_action_succeed

    # Test: Action with failure then success
    make_action_fail()


# Generated at 2022-06-13 10:29:22.086838
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    # Arrange
    distribution = mock.MagicMock()
    previous_boot_time = mock.MagicMock()
    action_module = ActionModule()

    # Act
    action_module.check_boot_time(distribution, previous_boot_time)

    # Assert
    assert True

# Generated at 2022-06-13 10:29:30.443536
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    # test_ActionModule_get_system_boot_time tests that the get_system_boot_time method of the class
    # ActionModule returns the correct formatted output for a system boot time.

    # Arrange
    from ansible.compat.tests import unittest
    from ansible.module_utils.action._reboot import ActionModule

    data = json.loads('''
        {
            "ansible_facts": {
                "ansible_distribution": "RedHat"
            }
        }
    ''')

    # Act
    actionModule = ActionModule(None, data, None, None)
    boot_time_output = actionModule.get_system_boot_time(data['ansible_facts']['ansible_distribution'])

    # Assert

# Generated at 2022-06-13 10:29:44.355952
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
  # Initialize data used in test
  module_name = 'reboot'
  class_name = 'ActionModule'
  method_name = 'get_distribution'
  module = AnsibleModule(argument_spec=dict())
  distribution = 'CentOS'
  task_vars = {"ansible_facts": {
    "distribution": distribution
  }}


  ###
  # Run unit test
  ###

  # This instantiation is required to initialize the class obj instance properly
  class_obj = ActionModule(module_name, module, task_vars=task_vars)

  # Get the method from the class we want to test
  method = getattr(class_obj, method_name)

  # Perform the test
  result = method()
  assert result == distribution

# Generated at 2022-06-13 10:29:53.279419
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test runs here
    from ansible_collections.notmintest.not_a_real_collection.tests.unit.compat import unittest
    from ansible_collections.notmintest.not_a_real_collection.tests.unit.compat.mock import MagicMock, patch
    from ansible.utils.path import unfrackpath

    try:
        from resource import RLIMIT_NOFILE
    except ImportError:
        RLIMIT_NOFILE = None

    from ansible_collections.notmintest.not_a_real_collection.plugins.modules import reboot

    class TestActionModule(unittest.TestCase):
        def setUp(self):
            self.tmpdir = tempfile.mkdtemp()
            self.addCleanup(shutil.rmtree, self.tmpdir)



# Generated at 2022-06-13 10:30:06.090536
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    m = ModuleTestFramework("test_ActionModule_deprecated_args")

    m.add_argument("--connect_timeout_sec", dest="connect_timeout_sec", required=False, type=int)
    m.add_argument("--to", dest="to", required=False)
    m.add_argument("--reboot_timeout_sec", dest="reboot_timeout_sec", required=False, type=int)
    m.add_argument("--test_command", dest="test_command", required=False)
    m.add_argument("--shutdown_timeout_sec", dest="shutdown_timeout_sec", required=False, type=int)
    m.add_argument("--post_reboot_delay", dest="post_reboot_delay", required=False, type=int)

    args = m.parse_args

# Generated at 2022-06-13 10:31:23.539076
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    '''
    Unit test for method ActionModule.perform_reboot of class ActionModule
    '''
    print("\n## Getting class ActionModule")
    my_class = get_class("ActionModule")
    print("\n## Instantiate a new object of the class ActionModule")
    my_instance = my_class()
    print("\n## Make a copy of the attribute: task_vars")
    task_vars = copy.deepcopy(my_instance.task_vars)
    print("\n## Get a copy of the variable distribution in the task_vars variable")
    distribution = my_class.get_distribution(task_vars)

    print("\n## Get object result after performing the method perform_reboot of the class ActionModule with parameters: task_vars and distribution")

# Generated at 2022-06-13 10:31:29.834328
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    # Copy-pasted from the real method and slightly modified to run this test
    # (extracts the needed function from the code of method `run` above)
    # Do NOT remove this comment, this is important for our code-analysis tool:
    horton.patch()

    # Get parameters from test-file (_input.yml)
    action=AnsibleActionModule()
    action.check_boot_time(horton.Dict({'ANSIBLE_DISTRIBUTION': 'CentOS', 'ANSIBLE_DISTRIBUTION_RELEASE': '10'}), 'Mon, 27 Jul 2020 02:13:03 +0000')

# Generated at 2022-06-13 10:31:40.701538
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    import time
    import paramiko
    from ansible.plugins.connection.ssh import Connection as Connection_ssh

    class ActionModule(Reboot): # subclass of Reboot
        DEFAULT_REBOOT_TIMEOUT = 10

    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None) # object of class Reboot

    class MockConnection(Connection_ssh):
        def __init__(self, data):
            super(MockConnection, self).__init__(None, 'ssh', None)
            self._play_context = data

        def exec_command(self, cmd, tmp_path, sudoable=True):
            if cmd.startswith('/sbin/shutdown'):
                time.sleep(2)  # simulate reboot
               

# Generated at 2022-06-13 10:31:43.518892
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    action_module = ActionModule()
    result = action_module.get_shutdown_command_args('centos')
    assert result == '-r now'

# Generated at 2022-06-13 10:31:45.944436
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    module = ActionModule(None)
    assert module.validate_reboot(None, None) is not None

# Generated at 2022-06-13 10:31:55.526027
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    res = {}
    task_vars = {}
    module = ActionModule(mock.Mock(), task_vars=task_vars)

    test_distribution = 'DEFAULT'
    test_test_command = 'echo "foo"'

    with mock.patch.object(ActionModule, '_low_level_execute_command', return_value={'stdout': 'foo', 'stderr': '', 'rc': 0}):
        module.run_test_command(test_distribution)

    with mock.patch.object(ActionModule, '_low_level_execute_command', return_value={'stdout': 'foo', 'stderr': 'bar', 'rc': 1}):
        test_result = module.run_test_command(test_distribution)

        assert test_result['failed'] == True
       

# Generated at 2022-06-13 10:31:57.979151
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    aa = ActionModule()
    a_str = "a_str"
    assert aa.get_system_boot_time(a_str) == None


# Generated at 2022-06-13 10:32:12.877126
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    action = ActionModule()
    # test method create_reboot_command of class ActionModule
    # creates the reboot command
    distribution = "DEBIAN"
    action.DEFAULT_TEST_COMMAND = 'whoami'
    command_str = action.run_test_command(distribution)
    assert command_str == None
    # test method get_distribution of class ActionModule
    # returns the correct distribution
    distribution = "DEBIAN"
    distribution_result = action.get_distribution(distribution)
    assert distribution_result == "DEBIAN"
    # test method get_boot_time_command of class ActionModule
    # returns the command to get boot time information
    distribution = "DEBIAN"
    command_result = action.get_boot_time_command(distribution)

# Generated at 2022-06-13 10:32:20.774412
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    # init the class
    am = ActionModule()

    # set up the return code
    reboot_rc = 0

    # set up the stub methods
    def test_get_shutdown_command():
        return 'echo'

    def test_get_shutdown_command_args():
        return '-n'

    def test_low_level_execute_command(*args, **kwargs):
        reboot_result = {'rc': reboot_rc, 'stderr': 'test_stderr', 'stdout': 'test_stdout'}
        return reboot_result

    am.get_shutdown_command = test_get_shutdown_command
    am.get_shutdown_command_args = test_get_shutdown_command_args
    am._low_level_execute_command = test_low_level_execute_command

# Generated at 2022-06-13 10:32:25.715049
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    # global var
    global_var = {}

    # initialize input arguments
    args = {}

    # initialize builtin module
    import ansible.module_utils.basic
    import ansible.module_utils.facts
    import ansible.module_utils.pycompat24

    # initialize module class

# Generated at 2022-06-13 10:35:00.678374
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import sys
    import shutil
    import tempfile
    import re

    def _get_result(result):
        '''Return a dictionary containing only the keys:
        'failed', 'msg', 'rebooted' and 'changed'.
        '''
        return {k: result[k] for k in ('failed', 'msg', 'rebooted', 'changed') if k in result}

    def _get_argspec(obj):
        '''Returns the arguments a function accepts.
        '''
        if hasattr(obj, '__func__'):
            obj = obj.__func__
        if hasattr(obj, '__code__'):
            obj = obj.__code__

# Generated at 2022-06-13 10:35:08.450766
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    action = ActionModule(dict(ANSIBLE_MODULE_ARGS=dict()), make_connection())
    boot_time = action.get_system_boot_time("")
    try:
        action.check_boot_time("", boot_time)
        error = False
    except ValueError:
        error = True
    assert error is False


# Generated at 2022-06-13 10:35:16.027154
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    action_obj = ActionModule()

    task_vars = {
        'ansible_distribution': 'RedHat',
        'ansible_distribution_version': '6.8',
        'ansible_distribution_release': 'Santiago',
        'ansible_distribution_file_parsed': True
    }

    def get_shutdown_command(task_vars, distribution):
        return '/bin/test_shutdown_bin'

    action_obj.get_shutdown_command = get_shutdown_command

    def _low_level_execute_command(cmd, sudoable=True):
        return ({'rc': 0}, b'', b'test_shutdown_stderr')

    action_obj._low_level_execute_command = _low_level_execute_command
    action_obj._

# Generated at 2022-06-13 10:35:28.630195
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    mytask = call_task()
    shutmod = ActionModule(mytask, mytask.connection)

    assert shutmod.get_system_boot_time('redhat') == 'date -d "$(awk -F. \'{print $1}\' /proc/uptime) second ago" +"%Y-%m-%d %H:%M:%S"'
    assert shutmod.get_system_boot_time('centos') == 'date -d "$(awk -F. \'{print $1}\' /proc/uptime) second ago" +"%Y-%m-%d %H:%M:%S"'

# Generated at 2022-06-13 10:35:40.050911
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    action_module = ActionModule({})
    max_end_time = datetime.utcnow() + timedelta(seconds=10000)
    distribution = 'test_distribution'
    previous_boot_time = "test_boot_time"

    def test_action(distribution, **kwargs):
        pass

    def test_check_boot_time(distribution, **kwargs):
        pass

    # There is no need to execute this test in the normal way, because it is already tested in validate_reboot()
    #action_module.do_until_success_or_timeout(action=test_action, action_desc="test_action", reboot_timeout=1000, distribution=distribution, action_kwargs={'previous_boot_time':previous_boot_time})



# Generated at 2022-06-13 10:35:46.408815
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():

    module = ActionModule()

    task_vars = {}

    distribution = "centos"

    # test with valid data
    expect = module.DEFAULT_SHUTDOWN_COMMAND_ARGS
    actual = module.get_shutdown_command_args(distribution)
    assert(actual == expect)

    # test a different linux distribution
    task_vars["ansible_facts"] = {
        "distribution": "ubuntu",
        "distribution_release": "18.04",
        "distribution_version": "18.04"
    }
    distribution = "ubuntu"
    expect = module.DEFAULT_SHUTDOWN_COMMAND_ARGS
    actual = module.get_shutdown_command_args(distribution)
    assert(actual == expect)

    # test windows

# Generated at 2022-06-13 10:35:52.821979
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars

    inventory = InventoryManager(loader=DataLoader(), sources='')
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

# Generated at 2022-06-13 10:36:00.821939
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():

    # Creating test object
    test_obj = ActionModule(
        connection=Mock(),
        _make_tmp_path=Mock(
            return_value=Mock()
        ),
        loader=Mock(),
        _connection_info=Mock(
            return_value=dict()
        ),
        _task_fields=dict(action='test_action'),
        shared_loader_obj=Mock(),
        _task=Mock(),
        _play_context=Mock(
            check_mode=False
        ),
        _loader=Mock(),
        _templar=Mock(),
        _shared_loader_obj=Mock()
    )

    test_distribution = ''

    # Testing method
    with pytest.raises(AnsibleError) as err:
        test_obj.get_dist

# Generated at 2022-06-13 10:36:04.224891
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    tobject = ActionModule()
    task_vars = {}
    expected_result = 'DEFAULT'
    result = tobject.get_distribution(task_vars)
    assert(result == expected_result)


# Generated at 2022-06-13 10:36:06.577916
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # ansible/lib/ansible/plugins/action/reboot.py
    # FIXME: Test not fully implemented, check why not
    pass


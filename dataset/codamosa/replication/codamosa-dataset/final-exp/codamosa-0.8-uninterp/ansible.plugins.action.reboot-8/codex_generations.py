

# Generated at 2022-06-13 10:27:13.225871
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    # Setup

    # Call
    result = None

    # Test
    assert result == """Unable to run test.
Test requires that ActionModule.deprecated_args(self) return None instead of '{return_value}'""".format(
        return_value=result)


# Generated at 2022-06-13 10:27:20.566086
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    self = None
    distribution = b'slackware'
    test_command = 'cmd'


# Generated at 2022-06-13 10:27:32.012688
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    tasks = [
        dict(
            name='test task',
            action='reboot'
        )
    ]

    task_results = dict(
        failed=False,
        rebooted=True,
        elasped=0,
        changed=False,
        msg=''
    )
    distribution = 'Debian'
    original_connection_timeout = 0

    def check_boot_time(distribution, previous_boot_time):
        return True

    def run_test_command(distribution):
        return True

    task_vars = dict()
    action_module = ActionModule(
        dict(
            name='test task',
            action='reboot'
        ),
        dict(),
        True,
        dict()
    )

    action_module._task_vars = task_vars
    action_

# Generated at 2022-06-13 10:27:39.777481
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    # Initialize parameters
    shutdown_command_args = '+1'
    distribution = 'ubuntu'
    # Create object
    a = _create_ActionModule()
    # Call the function
    result = a.get_shutdown_command_args(shutdown_command_args, distribution)
    # Check the results
    assert result == '-r +1'

# Generated at 2022-06-13 10:27:41.552509
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    # TODO: add test logic for method ActionModule.get_distribution
    pass


# Generated at 2022-06-13 10:27:50.984905
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    fixture = ActionModule('test', 'test', 'test')

    distribution = 'test'
    task_vars = {'test': 'test'}

    # parametrize fixture
    fixture._connection = 'test'
    fixture.DEFAULT_SUDOABLE = 'test'

    # initialize test environment
    write_content(fixture, 'test_ActionModule_perform_reboot.txt')

    # execute function with parametrized fixture
    result = fixture.perform_reboot(task_vars, distribution)

    # remove test environment
    remove_content(fixture, 'test_ActionModule_perform_reboot.txt')

    assert result['start'] != '' and result['start'] is not None
    assert result['failed'] == False
    assert result['reboot'] == False


# Generated at 2022-06-13 10:27:54.879998
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    interesting_libc_values = ['libc5', 'glibc', 'libc6']
    for libc in interesting_libc_values:
        shutdown_command_args = ActionModule.get_shutdown_command_args(libc)
        assert shutdown_command_args == ActionModule.DEFAULT_SHUTDOWN_COMMAND_ARGS, "Did not get expected value for {0}".format(libc)


# Generated at 2022-06-13 10:27:57.523819
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    """Unit test for method `get_shutdown_command` of class `ActionModule`."""
    pass

# Generated at 2022-06-13 10:28:10.498644
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    # Testing case 1
    # set up context
    action_module = ActionModule()
    # call test method
    action_module.do_until_success_or_timeout(action=action_module.check_boot_time, action_desc="last boot time check", reboot_timeout=900, distribution='redhat', action_kwargs={'previous_boot_time': ''})
    # assert result

    # Testing case 2
    # set up context
    action_module = ActionModule()
    # call test method
    action_module.do_until_success_or_timeout(action=action_module.check_boot_time, action_desc="last boot time check", reboot_timeout=900, distribution='redhat', action_kwargs={'previous_boot_time': ''})
    # assert result

    # Testing case 3
    # set

# Generated at 2022-06-13 10:28:11.642037
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    pass


# Generated at 2022-06-13 10:28:54.415908
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    """Test get_shutdown_command method of the ActionModule class
    """
    import os
    import tempfile

    with tempfile.TemporaryDirectory() as tmp_dir:
        # Prepare fake files to be used in tests
        fake_bin = 'fake_bin'
        fake_bin_path = os.path.join(tmp_dir, fake_bin)
        with open(fake_bin_path, 'w') as fake_bin_file:
            fake_bin_file.write('#!/bin/sh')

        os.chmod(fake_bin_path, 0o751)

        fake_shutdown_bin = os.path.join(tmp_dir, 'fake_shutdown_bin')
        with open(fake_shutdown_bin, 'w') as fake_shutdown_bin_file:
            fake_shutdown_

# Generated at 2022-06-13 10:29:04.127895
# Unit test for method get_distribution of class ActionModule

# Generated at 2022-06-13 10:29:07.719183
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    # Not testing the check_boot_time() method because it uses self._low_level_execute_command
    pass

# Generated at 2022-06-13 10:29:18.043354
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    import mock
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.connection import Connection

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(),

            # TODO: make use of these
            reboot_timeout=dict(type='int'),
            reboot_timeout_sec=dict(type='int'),
            test_command=dict(type='str'),
            test_command_args=dict(type='str'),
            connect_timeout=dict(type='float'),
            connect_timeout_sec=dict(type='float'),

            msg=dict(type='str'),
        ),
        supports_check_mode=False
    )

    connection = Connection(module._socket_path)
    # initialize test object

# Generated at 2022-06-13 10:29:28.033711
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    import socket
    import ssh

    class MockConnection(ssh.SSHConnection):
        """Mock connection that doesn't actually connect to anything"""

        def connect(self, host, port, username, password, pkey, key_filename,
                    timeout, look_for_keys, allow_agent, compression,
                    sock, passphrase, transport, allow_executable, common_args,
                    extra_args, local_interfaces, remote_addr):
            self.shared = True

    class MockedSSHClient(object):
        """Mock SSHClient, using our mocked connection"""
        def __init__(self):
            self._ssh_impl = MockConnection

        def close(self):
            pass
    # Create connection object
    connection = MockConnection(None, 'ssh')
    connection._play_context = _play_context
    connection._play

# Generated at 2022-06-13 10:29:35.307686
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    # setup
    from ansible.plugins.action.normal import ActionModule
    task_vars = dict()
    module_args = dict()
    
    # test
    action = ActionModule(None, module_args, task_vars)
    result = action.get_shutdown_command(task_vars, None)
    assert result == '/sbin/shutdown'

# Generated at 2022-06-13 10:29:46.194731
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    am = ActionModule()
    nb_executions = {'nb_exec': 0}
    am.do_until_success_or_timeout(action=lambda: nb_executions.update(nb_exec=1), action_desc=None,
                                   reboot_timeout=1, distribution=None)
    assert nb_executions['nb_exec'] == 1

    nb_executions = {'nb_exec': 0}
    with pytest.raises(TimedOutException):
        am.do_until_success_or_timeout(action=lambda: nb_executions.update(nb_exec=1), action_desc=None,
                                       reboot_timeout=1, distribution=None)
    assert nb_executions['nb_exec'] == 1


# Generated at 2022-06-13 10:29:54.656987
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    # Given:
    #
    # set up a test ActionModule to use and provide a default_args dict
    default_args = dict(
        distribution='DEFAULT_DISTRO',
        test_command='DEFAULT_COMMAND',
        reboot_timeout=7200)

    a = ActionModule(task=dict(action='reboot'), connection=DummyConnection(), play_context=DummyPlayContext(), loader=DummyLoader(), templar=DummyTemplar(), shared_loader_obj=None)
    a.DEFAULT_TEST_COMMAND = default_args['test_command']
    a.DEFAULT_REBOOT_TIMEOUT = default_args['reboot_timeout']

    # And:
    #
    # set up a dict of test args and a dict to hold the expected results, to be
    # used

# Generated at 2022-06-13 10:30:06.610544
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():

    from ansible_collections.notmintest.not_a_real_collection.tests.unit.compat.mock import patch
    from ansible_collections.notmintest.not_a_real_collection.plugins.modules import reboot

    def get_shutdown_command(self):
        return 'true'

    def check_boot_time(self, distribution, previous_boot_time):
        raise ValueError("boot time has not changed")

    def run_test_command(self, distribution):
        pass


# Generated at 2022-06-13 10:30:21.123562
# Unit test for method check_boot_time of class ActionModule

# Generated at 2022-06-13 10:32:35.152716
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    from ansible.plugins.action.reboot import ActionModule
    host_facts = dict(ansible_distribution='CentOS',
                    ansible_distribution_version='7.6.1810',
                    ansible_distribution_release='Core',
                    ansible_distribution_file_parsed=True)
    action = ActionModule(task=dict(action='test'), connection='local', play_context=dict(check_mode=True), loader=None, templar=None, shared_loader_obj=None)
    result = action.get_distribution(host_facts)
    assert result == 'centos7'


# Generated at 2022-06-13 10:32:37.474738
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    '''
    Unit test for method run_test_command of class ActionModule
    '''

    pass

# Generated at 2022-06-13 10:32:46.421467
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    # For some reason this test fails in python3 on centos7,
    # but not on ubuntu or debian.
    if platform == 'linux2':
        return
    from ansible.plugins.action import ActionBase
    action = ActionModule(
            {'ANSIBLE_MODULE_ARGS': {'connect_timeout': 60}},
            play_context=PlayContext(),
            connection=None,
            loader=None,
            templar=None,
            shared_loader_obj=None)
    action._low_level_execute_command = Mock(return_value={'rc': 0, 'stdout': '', 'stderr': ''})

    r = action.run_test_command('GenericLinux', test_command='echo foo')
    assert r is None
    action._low_level_execute_command.assert_called_

# Generated at 2022-06-13 10:33:01.707595
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    # Parameters to supply to constructor
    task_vars = {}
    host_vars = {}
    loader = None
    connection = None

    # Container for the results
    results = []

    # Container for the return values
    return_values = []

    # ActionModule under test
    test_obj = ActionModule(task=None,
                            connection=connection,
                            play_context=None,
                            loader=loader,
                            templar=None,
                            shared_loader_obj=None)

    # Add the return values to return_values[]

# Generated at 2022-06-13 10:33:07.026027
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    # Setup test
    results = {
        'rc': 0,
        'stdout': 'some_output',
        'stderr': 'some_error'
    }

    class TaskMock:
        def __init__(self, action, args):
            self.action = action
            self.args = args

    class ConnectionMock:
        def __init__(self, sudoable):
            self.sudoable = sudoable

        def _low_level_execute_command(self, command, sudoable):
            assert command == 'test_command_string'
            assert sudoable == True

            return results

    class ActionModuleMock(ActionModule):
        def __init__(self, task):
            self._task = task
            self._connection = ConnectionMock(sudoable=True)
            self.DEFAULT_CONNECT

# Generated at 2022-06-13 10:33:18.224738
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    # Check that the check_boot_time method raises a ValueError if the system is not rebooted.
    shutdown_bin = "/sbin/shutdown"

    result = dict(
        rc=0,
        stdout='',
        stderr=''
    )
    def get_system_boot_time(self, distribution):
        return "Fri 2017-12-15 11:46:08 CET"

    def _low_level_execute_command(self, command, sudoable=True):
        return result

    hostvars = dict(
        ansible_distribution="Linux",
        ansible_distribution_release="2.6.32-358.el6.x86_64",
        shutdown_path=shutdown_bin
    )


# Generated at 2022-06-13 10:33:27.219373
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    import mock
    import uuid

    # Setup emulated test environment
    task = mock.MagicMock()
    task.action = 'perform_reboot'
    task.args = {}

    source = mock.MagicMock()
    source.name = 'source'

    path = uuid.uuid4().hex

    connection = mock.MagicMock()
    connection.transport = 'connection.transport'
    connection.reset = mock.MagicMock()
    connection.get_option = mock.MagicMock()
    connection.get_option.return_value = path

    action_module = ActionModule(task, connection, source.name, False, False, None)
    action_module._connection = connection
    action_module._task = task
    action_module._task.args = {}

# Generated at 2022-06-13 10:33:35.773721
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
  am = ActionModule()
  am.DEFAULT_REBOOT_TIMEOUT = 30
  am._task = lambda: None
  am._task.action = 'test'
  am.check_boot_time = lambda distribution, action_kwargs: False
  am.run_test_command = lambda distribution, action_kwargs: False
  result = am.validate_reboot('CentOS',None,{'previous_boot_time': 'False'})
  assert result['failed'] == True
  assert result['rebooted'] == True
  assert result['msg'] == 'Timed out waiting for last boot time check (timeout=30)'

# Generated at 2022-06-13 10:33:51.123786
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Init ActionModule instance
    am = ActionModule()

    # Init arguments
    play_context = dict(
        module_path=u'/home/vagrant/ansible/test/action_plugins'
    )
    _task = dict(
        reboot_timeout=u'300',
        reboot_timeout_sec=u'300'
    )

    am._play_context = PlayContext()
    am._play_context.__dict__ = play_context
    am._task = Task()
    am._task.__dict__ = _task

    from ansible.plugins.loader import connection_loader
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.loader import cache_loader
    from ansible.plugins.loader import callback_loader

# Generated at 2022-06-13 10:33:59.389980
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    """
    test_ActionModule_check_boot_time

    This function tests the check_boot_time function of the ActionModule class

    """
    with pass_mocks(ActionModule._get_distribution, ActionModule._get_value_from_facts,
                    ActionModule._low_level_execute_command, ActionModule.get_shutdown_command) as (mock_distribution, mock_facts, mock_command, mock_shutdown):

        mock_distribution.return_value = 'RedHat'
        mock_facts.return_value = 'FBSD'
        test_hostname = 'host1'
        test_repo = 'repo1'
        test_repo_id = 'repo_id'
        test_repo_gpg = 'repo.key'

# Generated at 2022-06-13 10:35:34.794162
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    print("test_ActionModule")
    test_module = None    # type: ActionModule
    path = None    # type: str
    name = None    # type: str
    distribution = None    # type: str
    sudoable = False    # type: bool
    task_vars = None    # type: dict
    result = None    # type: str
    result = test_module.get_shutdown_command(path, name, distribution, task_vars, sudoable)
    assert isinstance(result, str)
    print('done')



# Generated at 2022-06-13 10:35:40.644599
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    task_vars = dict(
        ansible_distribution='debian',
        ansible_distribution_version='7',
        inventory_hostname='host_1',
    )


# Generated at 2022-06-13 10:35:43.330138
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    action_module = ActionModule()
    task_vars = {}
    distribution = "DEFAULT"
    return action_module.perform_reboot(task_vars, distribution)


# Generated at 2022-06-13 10:35:50.561332
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    spec = importlib.util.spec_from_file_location('action_plugins.system_reboot', rest_api.__path__[0] + '/action_plugins/system_reboot.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    instance = module.ActionModule(task=Task(), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    task_vars = {}
    assert instance.get_distribution(task_vars) == 'DEFAULT_DISTRIBUTION'
    task_vars['ansible_distribution'] = 'RedHat'
    assert instance.get_distribution(task_vars) == 'RedHat'

test_ActionModule_get_dist

# Generated at 2022-06-13 10:35:59.154660
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    print("Running test_ActionModule_get_distribution()")

    # calling get_distribution with default arguments
    result = reboot._get_distribution()
    assert result == 'DEFAULT'

    # calling get_distribution with a value of ansible_distribution
    result = reboot._get_distribution('CentOS')
    assert result == 'RedHat'

    # calling get_distribution with ansible_distribution=CentOS and ansible_os_family=Debian
    result = reboot._get_distribution('CentOS', 'Debian')
    assert result == 'DEFAULT'

    # calling get_distribution with ansible_distribution=CentOS and ansible_os_family=RedHat
    result = reboot._get_distribution('CentOS', 'RedHat')
    assert result == 'RedHat'

    # calling get

# Generated at 2022-06-13 10:36:08.410323
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    test_action = "reboot"
    test_action_desc = "last boot time check"
    test_reboot_timeout = 10
    test_distribution = "ubuntu"
    test_action_kwargs = {'previous_boot_time': "2019-04-26 06:04:00"}

    class mock_ActionModule:
        def __init__(self):
            self.called = 0
            self.DEFAULT_REBOOT_TIMEOUT = 30
            self.post_reboot_delay = 0
            self._task = mock_Task()
            self._task.action = test_action
            self._play_context = mock_PlayContext()
            self._connection = mock_Connection()
            self._connection.transport = 'ssh'
            self.DEPRECATED_ARGS = {}

# Generated at 2022-06-13 10:36:21.838984
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_text

    class ConnectionMock:
        def __init__(self, original_connection_timeout, reboot_timeout=None, test_command_rc=0):
            self._original_connection_timeout = original_connection_timeout
            self._reboot_timeout = reboot_timeout
            self._test_command_rc = test_command_rc
            self._connect_timeout = None

        def set_option(self, name, value):
            if name == 'connection_timeout':
                self._connect_timeout = value

        def get_option(self, name):
            if name == 'connection_timeout':
                return self._connect_timeout

        def reset(self):
            if reboot_timeout is not None:
                self._connect

# Generated at 2022-06-13 10:36:32.242188
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test case 1
    # Constructing test environment to get expected output
    check_mode = True
    task_vars = {'ansible_check_mode': True, 'ansible_connection': 'local'}
    am = ActionModule(check_mode, task_vars, None, 'local')
    expected = {'changed': False, 'elapsed': 1, 'failed': True, 'msg': 'Running reboot with local connection would reboot the control node.'}
    actual = am.run()
    assert expected == actual

    # test case 2
    # Constructing test environment to get expected output
    task_vars = {'ansible_check_mode': True, 'ansible_connection': 'local'}
    am = ActionModule(False, task_vars, None, 'local')

# Generated at 2022-06-13 10:36:42.861643
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    # the 1st arg is empty to avoid the error message "argv[0] must be unicode, not str"
    argv = [None]
    argv.append("-vvvv")
    action_module = ActionModule_reboot(ArgvSetter(argv))

    # expect exception to be raised
    action_module._task = {
        'action': 'reboot',
        'args': {
            'reboot_timeout': '600',
            'connect_timeout': '30',
            'msg': 'System is going down for reboot NOW!',
        }
    }
    action_module._connection = BaseConnection('local')
    action_module._low_level_execute_command = MagicMock(side_effect=AnsibleError("ERROR"))

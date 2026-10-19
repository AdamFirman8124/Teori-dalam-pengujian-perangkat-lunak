

# Generated at 2022-06-13 10:27:11.688146
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    pass


# Generated at 2022-06-13 10:27:19.781595
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    success = None


# Generated at 2022-06-13 10:27:20.368268
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:27:25.678345
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():

    # TODO: Remove this once we can use a @patch decorator
    # @Patch(ActionModule)
    def test_success():
        pass

    from ansible.plugins.action.reboot import ActionModule
    action_module = ActionModule()
    action_module.do_until_success_or_timeout(test_success, "test", 1)

# Generated at 2022-06-13 10:27:30.197934
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    # Arrange
    action_module = ActionModule(None)
    task_vars = {}
    distribution = None

    # Act
    result = action_module.get_shutdown_command(task_vars, distribution)

    # Assert
    assert result == '/sbin/shutdown'


# Generated at 2022-06-13 10:27:30.923427
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    pass

# Generated at 2022-06-13 10:27:35.091924
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    test_actions = ActionModule()
    assert test_actions.get_system_boot_time("Redhat") is not None


# Generated at 2022-06-13 10:27:43.810036
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    dist = 'Debian'
    try:
        # get last boot time from system
        current_bt = am.get_system_boot_time(dist)
        try:
            # run check_boot_time with same boot time to ensure function times out
            am.check_boot_time(dist, current_bt)
            raise AssertionError('boot time check passed without reboot')
        except Exception as e:
            # as long as it times out we're good
            if isinstance(e, ValueError):
                pass
            else:
                raise e
    except Exception as e:
        raise e



# Generated at 2022-06-13 10:27:49.206319
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    # create test ActionModule object
    am = ActionModule(action=None, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # set task.args in object
    am._task.args['connect_timeout'] = 10

    # call deprecated_args
    am.deprecated_args()

    # assert message displayed
    assert display.display_string.startswith('DEPRECATION WARNING')


# Generated at 2022-06-13 10:27:56.962490
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    print("start ActionModule_get_shutdown_command")
    # mock task
    # mock task
    mock_task = Mock()
    mock_task.action = "reboot"
    mock_task.async_val = 42
    mock_task.args = {
        'use_reboot':False,
        'reboot_timeout':60,
        'connect_timeout':10,
        'msg':"Reboot initiated by Ansible"
    }
    # mock task._task, here task is task_executor
    mock_task._task = Mock()
    mock_task._task.action = "reboot"
    mock_task._task.async_val = 42

# Generated at 2022-06-13 10:28:33.167847
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    ansible_module = AnsibleModule(supports_check_mode=True)
    action_module = ActionModule(ansible_module, "reboot", {}, {}, {})
    action_module._task = MagicMock()
    action_module._task.action = "reboot"
    action_module._task.args = {"shutdown_timeout": 30, "post_reboot_delay": 30, "connect_timeout": 30}
    action_module.deprecated_args()


# Generated at 2022-06-13 10:28:37.004348
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    import requests
    from ansibullbot.wrappers.issuewrapper import IssueWrapper

    print('validate_reboot()')

    assert True == False


# Generated at 2022-06-13 10:28:39.720870
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    action_class = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    result = action_class.check_boot_time("distribution", "previous_boot_time")

# Generated at 2022-06-13 10:28:42.614744
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    # No test yet, since not used by the action plugin
    return

# Generated at 2022-06-13 10:28:50.947952
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils._text import to_bytes

    class TaskMock:
        def __init__(self, args):
            self.args = args

        def __getitem__(self, key):
            return self.args[key]

        def __setitem__(self, key, value):
            self.args[key] = value

        def __delitem__(self, key):
            del self.args[key]

    task_mock = TaskMock({'test_command': '/bin/echo "OK"'})

    class RunnerMock:
        def __init__(self, distribution, connection):
            self.runner = {}
            self.runner['distribution'] = distribution
            self.runner['connection'] = connection
           

# Generated at 2022-06-13 10:29:02.478143
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    '''Test method do_until_success_or_timeout of class ActionModule.'''
    import pytest
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.action import ActionBase
    from ansible.utils.display import Display

    class ActionModule(ActionBase):
        _task = {'action': 'reboot'}

        class Connection:
            ''' Mock connection class. '''
            @staticmethod
            def reset():
                pass

        def get_distribution(self, vars):
            return None

        def get_shutdown_command(self, vars, distribution):
            return '/sbin/shutdown'

        def get_shutdown_command_args(self, distribution):
            return "-r now"


# Generated at 2022-06-13 10:29:06.268191
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
  module = ActionModule()
  task_vars = {
    "ansible_facts": {
      "distribution": {
        "name": "CENTOS",
        "major_version": "7"
      }
    }
  }
  assert(module.get_distribution(task_vars) == "CENTOS7")


# Generated at 2022-06-13 10:29:17.311959
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    fixture = FixtureActionModule()
    fixture.setUp()

    fake_task_vars = {'ansible_distribution': 'Fedora'}
    expect_command = "/sbin/shutdown -r +1"
    expect_result = {'start': datetime.utcnow(), 'rebooted': False, 'failed': False}
    expect_result['start'] = datetime.utcnow()

    fixture._execute_remote_shell_command_mock.return_value = {'rc': 0, 'stdout': 'success'}
    result = fixture.perform_reboot(fake_task_vars, distribution="Fedora")
    assert result == expect_result
    assert fixture._execute_remote_shell_command_mock.call_count == 1
    assert fixture._execute_remote_shell_command_m

# Generated at 2022-06-13 10:29:27.606944
# Unit test for method deprecated_args of class ActionModule

# Generated at 2022-06-13 10:29:34.216249
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    """
        :return:
    """
    # Generate Stub for ActionModule
    actionmodule = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Set attributes
    actionmodule.DEFAULT_CONNECT_TIMEOUT = 12
    actionmodule.DEFAULT_REBOOT_TIMEOUT = 24
    actionmodule.POST_REBOOT_DELAY = 4
    actionmodule.DEFAULT_SUDOABLE = True
    actionmodule._display = display
    actionmodule.get_distribution = MagicMock(return_value='RedHat')
    actionmodule.get_shutdown_command = MagicMock(return_value='shutdown')

# Generated at 2022-06-13 10:30:42.234455
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    action_shutdown = ActionModule('shutdown', {}, create_ansible_task(TASK_VARS_LINUX))

    # Test sysvinit shutdown
    result = action_shutdown.get_shutdown_command_args('Linux')
    assert result == '-r +1'

    # Test systemd shutdown
    result = action_shutdown.get_shutdown_command_args('Systemd')
    assert result == '-r +1 "Test Reboot" "Autoreboot test"'

    # Test freebsd shutdown
    result = action_shutdown.get_shutdown_command_args('FreeBSD')
    assert result == '-r +1'


# Generated at 2022-06-13 10:30:43.851051
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    pass



# Generated at 2022-06-13 10:30:55.278843
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = {
        'ansible_system_capabilities': ['network_server', 'cap_net_raw'],
        'ansible_distribution': 'RedHat',
        'ansible_facts': {
            'ansible_system': 'Linux',
            'ansible_distribution': 'RedHat',
            'ansible_distribution_major_version': '6'
        },
        'ansible_pkg_mgr': 'yum'
    }

    tmp = '/path/to/tmp'
    self = ActionModule()
    self._connection = None
    self._supports_check_mode = None
    self._supports_async = None
    self._task = None
    self.reboot_timeout = None
    self.post_reboot_delay = 0

# Generated at 2022-06-13 10:30:56.190970
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    assert False, "Test not implemented"

# Generated at 2022-06-13 10:31:00.220876
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    my_actionmodule = ActionModule('dummy_connection')
    print(my_actionmodule.validate_reboot())


# Generated at 2022-06-13 10:31:07.477401
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Mock all the test params
    mock_ActionModule = ActionModule(
        task=dict(
            args=dict(
                use_reboot='no'
            )
        ),
        connection=dict(
            transport='local'
        ),
        play_context=dict(
            check_mode=True
        ),
        DEPRECATED_ARGS=dict(
            use_reboot='2.2',
        ),
        _task=dict(
            action='reboot',
        )
    )
    mock_task_vars = dict()

    # Call the method under test and assert results
    mock_ActionModule._supports_check_mode = True

    # Call the method under test

# Generated at 2022-06-13 10:31:10.254214
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    module = AnsibleModule()
    am = ActionModule(module, module._connection, '/path/to/foo', task_vars={})
    distribution = 'Ubuntu'
    assert am.get_shutdown_command_args(distribution) == 'now'

# Generated at 2022-06-13 10:31:11.424878
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 10:31:12.201200
# Unit test for method run of class ActionModule
def test_ActionModule_run(): pass

# Generated at 2022-06-13 10:31:22.684166
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():

    # Initialization
    repo = git.Repo(search_parent_directories=True)
    repo_dir = repo.working_dir

    my_module_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(my_module_dir, "../"))

    from module_utils.basic import AnsibleModule

    class MyTask(object):
        def __init__(self):
            self.action = "reboot"
            self.args = dict()

    class MyPlayContext(object):
        def __init__(self):
            self.check_mode = False
            self.remote_addr = "192.168.0.1"


# Generated at 2022-06-13 10:33:18.064515
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    module_args = dict(
        connect_timeout=10,
        reboot_timeout=10,
        test_command='/bin/ls',
        post_reboot_delay=0
    )
    am = ActionModule(None, module_args)
    distribution = dict(
        id='Ubuntu',
        release='14.04'
    )
    result = am.validate_reboot(distribution, None)
    assert 'failed' not in result
    assert result['rebooted'] == True
    assert result['changed'] == True


# Generated at 2022-06-13 10:33:27.116894
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    import os
    import sys
    import imp
    import pytest
    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import PY2
    from ansible.utils.unicode import to_unicode
    from ansible.compat.tests.mock import patch, MagicMock, Mock

    # Make sure we have a sane python version
    assert sys.version_info >= (2, 7)

    # Set some paths and import
    test_data_foldername = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'data', 'module_utils', 'test_reboot')

# Generated at 2022-06-13 10:33:29.031253
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    obj = ActionModule(dict(), dict())
    distribution = "Linux"
    obj.get_system_boot_time(distribution)

# Generated at 2022-06-13 10:33:39.579436
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    # Prepare the test environment and test arguments
    ActionModule.DEFAULT_TEST_COMMAND = 'test_command'
    ActionModule.DEFAULT_REBOOT_TIMEOUT = 5
    ActionModule.DEFAULT_CONNECT_TIMEOUT = None

    task = AnsibleTask()
    shutdown_module = ActionModule(task, connection=None)

    # Prepare mocks
    distribution = 'Fedora'
    test_command = 'test_command'
    test_command_result = {'rc': 0, 'stderr': 12, 'stdout': 6}

    commands = [
        'shutdown -h now',
        'systemctl poweroff',
        'reboot',
        'systemctl reboot',
        'shutdown -r now',
        'halt -p',
        'init 6'
    ]


# Generated at 2022-06-13 10:33:49.604762
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    """Test validate_reboot()"""
    action = ActionModule()
    action.check_boot_time = Mock(side_effect=ValueError)
    result = action.validate_reboot('distribution', original_connection_timeout=0, action_kwargs={'previous_boot_time': 'previous_boot_time'})
    assert result == {'failed': True, 'rebooted': True, 'msg': 'Timed out waiting for last boot time check (timeout=0)'}


# Generated at 2022-06-13 10:33:58.346915
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    from ansible.plugins.loader import module_loader
    from ansible.module_utils.facts import _get_file_contents, _get_distribution

    def freeze_debian():
        return {
            "ansible_distribution": "Ubuntu",
            "ansible_distribution_file_parsed": True,
            "ansible_distribution_file_path": "/etc/issue",
            "ansible_distribution_file_variety": "Debian",
            "ansible_distribution_major_version": "12.04",
            "ansible_distribution_release": "precise",
            "ansible_distribution_version": "12.04",
        }


# Generated at 2022-06-13 10:34:03.821171
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    # test_get_distribution_default_distribution
    module = ActionModule()
    module._task = AnsibleTask()
    module._task.args = {'distribution': None}
    module._get_value_from_facts_mock = MagicMock(return_value='DEFAULT_DISTRIBUTION')
    module._connection = AnsibleConnection()
    module._connection._shell = AnsibleShell()
    module._connection._shell.get_distro_facts = MagicMock(return_value={'ansible_facts': {'distribution': 'CentOS'}})
    assert module.get_distribution(task_vars = None) == 'CentOS'


# Generated at 2022-06-13 10:34:13.101723
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    my_action = ActionModule()
    task_vars = {
        'ansible_facts': {
            'distribution': 'Ubuntu',
            'distribution_release': '18.04',
            'distribution_version': '18.04',
            'system': 'Linux'
        },
        'ansible_connection': 'ssh'
    }

    actual_result = my_action.perform_reboot(task_vars, 'Ubuntu')

    assert actual_result['failed'] == False
    assert actual_result['changed'] == True


# Generated at 2022-06-13 10:34:15.066945
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    # function to test check_boot_time of class ActionModule
    test_obj = ActionModule()



# Generated at 2022-06-13 10:34:17.832564
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    with pytest.raises(AnsibleError):
        a = ActionModule()
        a.get_shutdown_command({}, 'rhel')


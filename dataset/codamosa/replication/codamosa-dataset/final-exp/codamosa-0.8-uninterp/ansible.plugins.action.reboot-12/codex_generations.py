

# Generated at 2022-06-13 10:27:21.447059
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    # initialize necessary resources
    action_module = ActionModule()
    distribution = {'name': 'Centos', 'version': '7'}
    action_module._task = dict()
    action_module._task['args'] = dict()
    action_module._task['args']['shutdown_command_args'] = '-h'
    # expected values
    expected_shutdown_command_args = '-h'
    # invoke the method to be tested
    shutdown_command_args = action_module.get_shutdown_command_args(distribution)
    # verify the results
    assert shutdown_command_args == expected_shutdown_command_args

# Generated at 2022-06-13 10:27:32.920545
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    task_vars = {}
    distribution = 'debian'
    action_module = ActionModule(task=Mock(), connection=Mock(), play_context=Mock(), loader=Mock(), templar=Mock(), shared_loader_obj=None)
    task_vars['ansible_service_mgr'] = 'systemd'
    action_module.get_shutdown_command(task_vars, distribution)
    task_vars['ansible_service_mgr'] = 'upstart'
    action_module.get_shutdown_command(task_vars, distribution)
    task_vars['ansible_service_mgr'] = 'sysvinit'
    action_module.get_shutdown_command(task_vars, distribution)
    task_vars['ansible_service_mgr'] = None


# Generated at 2022-06-13 10:27:34.737386
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    pass

# Generated at 2022-06-13 10:27:41.371452
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('Test run')
    task = Task(action='reboot', module_name='reboot')
    action_module = ActionModule(task, connection=None, play_context=PlayContext(), loader=None, templar=None, shared_loader_obj=None)
    task_vars = {}
    result = action_module.run(tmp=None, task_vars=task_vars)

# Generated at 2022-06-13 10:27:50.938055
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    m = ActionModule()
    m._task = MagicMock()

    m._task.action = 'reboot'
    m._task.args = dict(connect_timeout='1', connect_timeout_sec='2')
    m.deprecated_args()

    m._task.args = dict(check_interval='1', check_interval_sec='2')
    m.deprecated_args()

    m._task.args = dict(reboot_timeout='1', reboot_timeout_sec='2')
    m.deprecated_args()

    m._task.args = dict(pre_reboot_delay='1', pre_reboot_delay_sec='2')
    m.deprecated_args()

    m._task.args = dict(post_reboot_delay='1', post_reboot_delay_sec='2')

# Generated at 2022-06-13 10:27:54.536874
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    task_vars = {}
    module_returned_args = {}
    action_instance = ActionModule(task=DummyTask, connection=DummyConnection, play_context=DummyPlayContext(), loader=DummyLoader())
    expected = '/sbin/shutdown'
    actual = action_instance.get_shutdown_command(task_vars, 'REDHAT')
    assert actual == expected


# Generated at 2022-06-13 10:28:00.129154
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    distribution = 'debian'
    task_vars = {'ansible_os_family': 'Debian',
                 'ansible_distribution': 'Debian',
                 'ansible_distribution_version': '9.6'}

    # Create an ActionModule object
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Invoke test function
    actual_result = am.get_shutdown_command(task_vars, distribution)

    assert type(actual_result) == str
    assert actual_result == '/sbin/shutdown'


# Generated at 2022-06-13 10:28:12.665719
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    for fact_os_family, expected_distribution in [
            ('RedHat', 'RedHat'),
            ('Debian', 'Debian'),
            ('Solaris', 'Solaris'),
            ('Darwin', 'Darwin'),
            ('Unexpected', 'DEFAULT_DISTRIBUTION')
    ]:
        with mock.patch.object(ActionModule, '_get_value_from_facts') as mock_get_value_from_facts:
            mock_get_value_from_facts.return_value = fact_os_family
            distribution = action_module.get_distribution({})
            assert distribution == expected_distribution

# Generated at 2022-06-13 10:28:17.727346
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    module = AnsibleModule()
    action = ActionModule(module)
    action.do_until_success_or_timeout(wait_time_func, reboot_timeout=10, wait_time_desc='last boot time check', distribution='ubuntu')


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    #test_ActionModule_do_until_success_or_timeout()

# Generated at 2022-06-13 10:28:25.128317
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    #  pylint: disable=unused-argument
    def mock_check_for_controlpersist(sudoable, *args):
        return False
    def mock_get_controlpersist_dir_cmd(sudoable):
        return ''

    # Prepare for test
    low_level_execute_command = ActionModule.__dict__['_low_level_execute_command']
    setattr(ActionModule, '_low_level_execute_command', lambda *args, **kwargs: {'rc': 0, 'stderr': '', 'stdout': '2018-01-18 09:00:00'})

    display_vvv = ActionModule.__dict__['display_vvv']
    setattr(ActionModule, 'display_vvv', lambda *args, **kwargs: None)

    display_debug = ActionModule.__

# Generated at 2022-06-13 10:29:04.465994
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    am = ActionModule(dict(action='fake', connection='smart', distribution=None))
    
    class Wrapper:
        def __init__(self):
            self.args = {}
            self.args['reboot_timeout'] = 10
            self.args['reboot_timeout_sec'] = 10
            self.task_vars = {}
            self.deprecated = {}
            self.deprecated['username'] = None
            self.deprecated['password'] = None
            self.deprecated['sudo_user'] = None
            self.deprecated['sudo_pass'] = None
            self.deprecated['sudo'] = None
            self.deprecated['sudo_exe'] = None
            self.deprecated['sudo_flags'] = None
            self.deprecated['transport'] = None
            self.deprecated['path'] = None


# Generated at 2022-06-13 10:29:16.580436
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    task_vars = dict()
    module = ActionModule(task=MagicMock(), connection=MagicMock(), play_context=MagicMock())

    # test no sudo
    test_shutdown_bin = 'my-shutdown-bin'
    task_vars['ansible_sudo_exe'] = None
    task_vars['ansible_shutdown_command'] = test_shutdown_bin

    shutdown_command = module.get_shutdown_command(task_vars, 'DEFAULT')
    assert shutdown_command == test_shutdown_bin

    # test with sudo
    test_shutdown_bin = 'my-shutdown-bin'
    test_sudo_exe = '/path/to/sudo'
    task_vars['ansible_sudo_exe'] = test_sudo_exe

# Generated at 2022-06-13 10:29:27.144516
# Unit test for method get_shutdown_command of class ActionModule

# Generated at 2022-06-13 10:29:30.982802
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    task_vars = {'ansible_connection': 'local'}
    distribution = 'Linux'
    previous_boot_time = 'Fri 2018-05-18 15:18:26 UTC'

    try:
        ActionModule.check_boot_time(distribution, previous_boot_time)
        assert True
    except Exception:
        assert False


# Generated at 2022-06-13 10:29:40.234060
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
  task = Task('/')
  action = ActionModule(task, 'name')
  action.DEFAULT_SHUTDOWN_COMMAND = 'DEFAULT_SHUTDOWN_COMMAND'
  action.DEFAULT_SUDOABLE = True
  task_vars = {}
  distribution = 'distribution'
  action._task.action = 'action'

  # Call tested method
  result = action.get_shutdown_command(task_vars, distribution)

  # TODO: validate result


# Generated at 2022-06-13 10:29:52.510487
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    """Unit test for method run_test_command of class ActionModule"""
    runner = custom_runner.CustomRunner(ActionModule)
    #---------------
    # Initialize tests
    #---------------
    # test_ActionModule_run_test_command - test_case #1
    class test_ActionModule_run_test_command(unittest.TestCase):
        def test_run_test_command(self):
            #---------------
            # Initialize tests
            #---------------
            expected_result = {}
            expected_result['failed'] = False
            expected_result['changed'] = False
            #---------------
            # Execute tests
            #---------------

# Generated at 2022-06-13 10:30:05.675677
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    # Create an instance of ActionModule
    action_module = ActionModule()

    # Create an instance of AnsibleModule
    ansible_module = FakeAnsibleModule()

    # Set the action of the module
    action_module._task.action = 'reboot'

    # Create a connection plugin object
    class ConnectionPlugin(ConnectionBase):
        transport = 'network_cli'
        def __init__(self, task, connection, play_context, new_stdin, *args, **kwargs):
            super(ConnectionPlugin, self).__init__(task, connection, play_context, new_stdin, *args, **kwargs)
        def _low_level_execute_command(self, cmd, sudoable=False):
            display.vvv(u"Executing: {}".format(cmd))

# Generated at 2022-06-13 10:30:18.637627
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():

    # create an instance of the AnsibleModule mock
    am = AnsibleModuleMock()

    # create an instance of our class
    amodule = ActionModule(am)

    # the values returned when calling ansible.module_utils.basic.AnsibleModule.exit_json
    am.exit_json.side_effect = [
        {'foo': 'bar'}
    ]

    # the values that AnsibleModule.run_command will return
    # rc values are not used
    am.run_command.side_effect = [
        ('', '', 0),
    ]

    # our target method
    amodule.run_test_command(distribution='CentOS')


# Generated at 2022-06-13 10:30:28.641632
# Unit test for method get_distribution of class ActionModule

# Generated at 2022-06-13 10:30:37.986007
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    # Fixture: test object
    ActionModule_obj = ActionModule(task=Mock(), connection=Mock(), play_context=Mock(), loader=None, templar=None, shared_loader_obj=None)

    # set up attribute '_task'
    ActionModule_obj._task = Mock()

    # set up attribute '_task.action'
    ActionModule_obj._task.action = "reboot"

    # set up attribute '_task.args'
    ActionModule_obj._task.args = {
    }

    # set up attribute '_task.async_val'
    ActionModule_obj._task.async_val = 0

    # set up attribute '_task.cleanup'
    ActionModule_obj._task.cleanup = ""

    # set up attribute '_task.delegate_to'


# Generated at 2022-06-13 10:31:46.332618
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    from ansible.plugins.action import ActionBase
    import ansible.errors as ae
    import ansible.utils.display as aud
    aud.VERBOSITY = 4

# Generated at 2022-06-13 10:31:53.206373
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    # fake data for the argument_spec

# Generated at 2022-06-13 10:32:03.228268
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    from ansible.module_utils.facts.system.distribution import Distribution

    # Create an instance of class ActionModule with parameters
    # input and set the values of module
    arg_spec = dict()
    arg_spec.update(DEFAULT_ARGS)
    task_action = ActionModule(dict(name='action_module', args=dict(action='reboot', reboot_timeout_sec=30, connect_timeout_sec=30)), DEFAULT_ARGS, arg_spec)
    task_action._task.args.update(DEFAULT_ARGS)
    task_action.DEFAULT_REBOOT_TIMEOUT = 30
    task_action.DEFAULT_CONNECT_TIMEOUT = 30
    task_action._task.args.update(dict(reboot_timeout=60, connect_timeout=60))

    # Create an instance of class

# Generated at 2022-06-13 10:32:09.309029
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()

    result = module.run()
    assert result["msg"] == "Running reboot with local connection would reboot the control node."
    assert result["skipped"] == False
    assert result["changed"] == False

if __name__ == "__main__":
    test_ActionModule_run()

# Generated at 2022-06-13 10:32:10.255274
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    # Placeholder for test
    pass


# Generated at 2022-06-13 10:32:17.628208
# Unit test for method get_distribution of class ActionModule
def test_ActionModule_get_distribution():
    run_only = True
    if run_only:
        return False

    am = ActionModule()

    pprint.pprint(am.get_distribution(task_vars={}))
    pprint.pprint(am.get_distribution(task_vars={'ansible_distribution': 'Ubuntu'}))
    pprint.pprint(am.get_distribution(task_vars={'ansible_distribution': 'RHEL'}))
    pprint.pprint(am.get_distribution(task_vars={'ansible_distribution': 'CentOS'}))
    pprint.pprint(am.get_distribution(task_vars={'ansible_distribution': 'Fedora'}))

# Generated at 2022-06-13 10:32:25.530492
# Unit test for method perform_reboot of class ActionModule
def test_ActionModule_perform_reboot():
    def perform_reboot(self, task_vars, distribution):
        pass
    am = ActionModule()
    am._task = ansible.utils.unsafe_proxy.AnsibleUnsafeProxy({'args': {}, 'action': 'reboot'})
    am._low_level_execute_command = perform_reboot
    # Test perform_reboot without ansible_facts
    assert am.perform_reboot(None, None) == {'start': datetime(1970, 1, 1, 0, 0)}
    # Test perform_reboot with ansible_facts
    task_vars = {
        'ansible_facts': {
            'distribution': 'test'
        }
    }

# Generated at 2022-06-13 10:32:34.283937
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    # Create a mock value for module_builtin
    test_ansible_module = lambda *args, **kwargs: 'ansible-module-412'
    with patch('ansible.module_utils.basic.AnsibleModule', test_ansible_module):
        action_module = ActionModule()
        action_module.register_dump_object()


# Generated at 2022-06-13 10:32:44.294357
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    mod = modulemock.ModuleMock(name='ansible.modules.system.reboot',
                                params={'reboot_timeout_sec': 5},
                                checkmode=False)
    act = ActionModule(mod)

    dist = 'Linux'

    # Check boot time checking with timeout = 0 and result = True
    value = {'previous_boot_time': '0'}
    assert act.check_boot_time(distribution=dist, **value) == None

    # Check boot time checking with timeout > 0 and result = True
    value = {'previous_boot_time': '1'}
    assert act.check_boot_time(distribution=dist, **value) == None

    # Check boot time checking with timeout > 0 and result = False

# Generated at 2022-06-13 10:32:59.822710
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    import tempfile
    import shutil

    tempdir = tempfile.mkdtemp()

    # Test when test_command is not provided
    facts = {
        'TEST_COMMANDS': {
            'DISTRO-1': 'TEST-CMD-1',
            'DISTRO-2': 'TEST-CMD-2'
        },
        'DEFAULT_TEST_COMMAND': 'DEFAULT-TEST-CMD'
    }
    distribution = 'DISTRO-3'
    action_module = _create_instance_of_ActionModule(tempdir, facts)

    action_module.run_test_command(distribution)

    # Test when test_command is provided
    test_command = 'TEST-CMD'
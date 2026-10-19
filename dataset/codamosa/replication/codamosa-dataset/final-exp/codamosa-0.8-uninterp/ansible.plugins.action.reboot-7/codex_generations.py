

# Generated at 2022-06-13 10:27:18.688081
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    from ansible import context
    from ansible.utils.path import unfrackpath
    
    c = context.CLIARGS
    c['module_path'] = unfrackpath('/a/data/base/devel/ansible/lib/ansible/modules/system')
    
    
    
    c = context.CLIARGS
    c['module_path'] = unfrackpath('/a/data/base/devel/ansible/lib/ansible/modules/system')
    
    o = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    # no arguments, return value is not checked
    o.check_boot_time('Ubuntu')

# Generated at 2022-06-13 10:27:19.235333
# Unit test for method check_boot_time of class ActionModule
def test_ActionModule_check_boot_time():
    pass

# Generated at 2022-06-13 10:27:30.204753
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    hostvars = dict()
    hostvars['ansible_os_family'] = 'RedHat'
    hostvars['ansible_distribution'] = 'CentOS'
    hostvars['ansible_distribution_version'] = '7'
    hostvars['ansible_distribution_major_version'] = '7'
    task_vars = dict()
    task_vars['hostvars'] = hostvars
    action_module = ActionModule(task=dict(),
                                 connection=dict(),
                                 play_context=dict(),
                                 loader=dict(),
                                 templar=dict(),
                                 shared_loader_obj=dict())

    hostvars['ansible_os_family'] = 'RedHat'

# Generated at 2022-06-13 10:27:42.609452
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    # test_task_vars = dict(
    #     ansible_facts=dict(
    #         DISTRIBUTION_FAMILY='Debian',
    #         DISTRIBUTION_RELEASE='16.04LTS',
    #         DISTRIBUTION_VERSION='16.04',
    #         DISTRIBUTION_CODENAME='xenial',
    #         DISTRIBUTION_NAME='Ubuntu',
    #     )
    # )
    test_distribution = 'Ubuntu'

# Generated at 2022-06-13 10:27:43.205549
# Unit test for method run_test_command of class ActionModule
def test_ActionModule_run_test_command():
    pass

# Generated at 2022-06-13 10:27:51.891965
# Unit test for method get_shutdown_command_args of class ActionModule
def test_ActionModule_get_shutdown_command_args():
    class module_mock(object):
        # required for accessing base class methods
        class BaseAction(ActionBase):
            def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
                super(module_mock.BaseAction, self).__init__(task, connection, play_context, loader, templar, shared_loader_obj)
                # Some methods are called from the base class and may require these attributes
                self._loader = None
                self._templar = None
                self._task_vars = None
                self._shared_loader_obj = None

# Generated at 2022-06-13 10:27:53.982792
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
  # create an instance of ActionModule
  action_module = ActionModule()
  # call method get_system_boot_time
  action_module.get_system_boot_time('')

# Generated at 2022-06-13 10:27:56.701777
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    # Test 1:
    # Test method's name
    assert test_module.ActionModule.validate_reboot.__name__ == 'validate_reboot', "Unit Test 1 Failed: ActionModule.validate_reboot does not have the correct name"



# Generated at 2022-06-13 10:28:05.340867
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    module = ActionModule()
    module._task = MagicMock()
    module._task.args = {'action': 'reboot'}
    module._task.action = 'reboot'
    module.DEPRECATED_ARGS = {'keyname': '2.12'}
    with patch.object(builtins, 'display') as mock_display:
        module.deprecated_args()
        mock_display.warning.assert_called_once_with('Since Ansible 2.12, keyname is no longer a valid option for reboot')

# Generated at 2022-06-13 10:28:12.572309
# Unit test for method do_until_success_or_timeout of class ActionModule
def test_ActionModule_do_until_success_or_timeout():
    class MockTask(object):
        def __init__(self):
            self.action = 'test'
            self.args = {}

    action_module = ActionModule(MockTask(), '/dev/null')
    distribution = 'test_os'

    action_module.do_until_success_or_timeout(action_module.get_system_boot_time, action_desc=None, reboot_timeout=3, distribution=distribution)
    assert True

# Generated at 2022-06-13 10:28:47.261752
# Unit test for method get_system_boot_time of class ActionModule
def test_ActionModule_get_system_boot_time():
    shutdown_module = ActionModule()
    res = shutdown_module.get_system_boot_time('deb')
    assert res is not None, 'Unable to get system boot time'


# Generated at 2022-06-13 10:28:50.190776
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    t = ActionModule()
    ex = Exception()
    assert t.validate_reboot(ex) == "Exception"


# Generated at 2022-06-13 10:28:58.670328
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    module = AnsibleModule(
        argument_spec=dict()
    )

    action_mod = ActionModule(module._task, module._connection, module._play_context, module._loader, module._templar, module._shared_loader_obj)
    action_mod._task = dict()
    action_mod._task['args'] = dict()

    args = dict()
    for arg in action_mod.DEPRECATED_ARGS.keys():
        args[arg] = 'some_value'
        action_mod._task['args'].update(args)
        action_mod.deprecated_args()



# Generated at 2022-06-13 10:29:03.738413
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a mock config with sample values
    config = create_autospec(ConfigParser)
    config.getint.side_effect = lambda section, key: {
        'display': {
            'timeout': 1200,
            'verbosity': 4
        }
    }.get(section, {}).get(key, 0)

# Generated at 2022-06-13 10:29:06.787314
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    # Test type of string
    assert isinstance(validate_reboot(ActionModule, 'debian'), dict)


# Generated at 2022-06-13 10:29:11.767615
# Unit test for method validate_reboot of class ActionModule
def test_ActionModule_validate_reboot():
    my_obj = ActionModule()
    with pytest.raises(Exception) as err:
        my_obj.validate_reboot()
    assert err.value.args[0] == "'ActionModule' object has no attribute 'validate_reboot'"


# Generated at 2022-06-13 10:29:15.911939
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    # test with no arguments
    expected_result = {}
    actual_result = module.run()
    assert actual_result['failed'] == expected_result['failed']
    assert actual_result['rebooted'] == expected_result['rebooted']


# Generated at 2022-06-13 10:29:17.050661
# Unit test for method deprecated_args of class ActionModule
def test_ActionModule_deprecated_args():
    pass


# Generated at 2022-06-13 10:29:22.946767
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    tmp = None
    task_vars = None
    am = ActionModule(connection="connection",
                      play_context=play_context(),
                      loader="loader",
                      templar="templar",
                      shared_loader_obj=None)
    result = am.run(tmp, task_vars)
    assert isinstance(result, dict)


# Generated at 2022-06-13 10:29:29.984806
# Unit test for method get_shutdown_command of class ActionModule
def test_ActionModule_get_shutdown_command():
    expected = ['shutdown', '-r', 'now', '&&', 'echo', '"Rebooting due to Ansible"']
    test_task = dict(task=dict(args=dict(shutdown_timeout='now',
                                         reboot=True,
                                         reboot_timeout_sec=300,
                                         connect_timeout_sec=30,
                                         pre_reboot_delay=10,
                                         post_reboot_delay=10)),
                     task_vars=dict())
    am = ActionModule(None, test_task, None)
    result = am.get_shutdown_command(test_task['task_vars'])
    assert result == expected



# Generated at 2022-06-13 11:18:52.149184
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 11:18:53.139485
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    am.run()

# Generated at 2022-06-13 11:18:53.793582
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 11:19:00.381792
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # given
    fake_self = FakeActionModule()
    fake_self._task.args = {}
    fake_self._task.async_val = False
    fake_self._connection._shell.tmpdir = "abcd"
    fake_self._task.delegate_facts = True
    fake_self._task.delegate_to = None
    fake_self._templar.template = MagicMock(return_value="auto")
    fake_self._shared_loader_obj.module_loader.has_plugin = MagicMock(return_value=True)
    fake_self._execute_module = MagicMock()

    # when
    actual_result = ActionModule.run(fake_self, None, None)

    # then

# Generated at 2022-06-13 11:19:11.265826
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # make a fake display object
    display_obj = Display()
    display.deprecated("action_plugins.yum")
    action_base_obj = ActionBase(None, display=display_obj)
    action_plugin_obj = ActionModule(None, action_base_obj, display=display_obj)
    # set valid values for task, task_vars
    task_obj = {}
    task_vars = {}
    # test run method
    assert action_plugin_obj.run(task_obj, task_vars) != {}
    # set tmp to True
    assert action_plugin_obj.run(tmp=True, task_vars=task_vars) != {}
    # set valid value for use
    task_obj.update({"args":{"use": "auto"}})
    # test run method
    assert action

# Generated at 2022-06-13 11:19:16.926069
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None, None, None)
    # Testing _supports_check_mode
    assert module._supports_check_mode == True
    # Testing _supports_async
    assert module._supports_async == True
    # Testing TRANSFERS_FILES
    assert module.TRANSFERS_FILES == False
    # Testing _display
    assert module._display == Display()

# Generated at 2022-06-13 11:19:28.163890
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.parsing.dataloader import DataLoader

    module = AnsibleModule(argument_spec={})
    loader = DataLoader()
    context = dict()

    # test with empty arguments
    am = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=loader, templar=None, shared_loader_obj=None)
    result = am.run(task_vars=None)
    assert result.get('failed') == True

# Generated at 2022-06-13 11:19:29.445599
# Unit test for constructor of class ActionModule
def test_ActionModule():

    assert ActionModule()

# Generated at 2022-06-13 11:19:35.401004
# Unit test for constructor of class ActionModule
def test_ActionModule():
    inp = dict(
        _ansible_no_log=True,
        use_backend='yum',
    )

    yum_backend_checker = ActionModule(dict(
        _task=dict(
            args=inp,
        ),
    ))

    assert yum_backend_checker.run() == {'failed': True, 'msg': "parameters are mutually exclusive: ('use', 'use_backend')"}

# Generated at 2022-06-13 11:19:37.389697
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None, None)
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 11:19:50.661173
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_args = dict(
        name="package",
        state="present",
        use="yum",
        conf_file="/etc/yum.conf",
        enablerepo="epel, satellite*",
        disable_gpg_check="yes",
        install_repoquery="yes",
        exclude="kernel,*-firmware,python*-pip,python*-setuptools,python*-wheel",
    )

    variable_manager = []
    loader = []
    display = Display()
    variable_manager = VariableManager()
    loader = DataLoader()


# Generated at 2022-06-13 11:19:56.842659
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Unit test for the constructor of the class.
    """
    from ansible.playbook.task import Task
    from ansible.playbook.role.include import Include

    y = ActionModule(include=Include(), task=Task(), connection='local', play_context=dict(), loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(y, ActionModule)
    assert y.TRANSFERS_FILES is False



# Generated at 2022-06-13 11:19:58.567267
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module

# Generated at 2022-06-13 11:19:59.230570
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:20:10.200489
# Unit test for constructor of class ActionModule
def test_ActionModule():

    import os
    import json
    import ansible.config.manager
    from collections import Mapping

    # load the action plugin
    yum_action_plugin = ActionModule(task=dict(
        args=dict(name='vim gcc'),
        async_val=0,
        async_jid='931f9d2b-8e8a-4bac-a799-393b7cfc5e5e',
        action='yum',
        delegate_to='localhost',
        delegate_facts=True,
        register='some_result',
        versioned=False
    ), connection=dict(), play_context=dict(become=True, become_user='foo'), loader=dict(), templar=dict(), shared_loader_obj=None)

    # get ansible config
    ansible_config = ansible.config

# Generated at 2022-06-13 11:20:14.164945
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for main method of class ActionModule
    '''
    import ansible.plugins.action.yum as yum
    action_module = yum.ActionModule(name="test", task=dict())

    results = action_module.run(tmp=None, task_vars=None)
    assert results['failed'] is True
    assert results['msg'] == "Could not detect which major revision of yum is in use, which is required to determine module backend. You should manually specify use_backend to tell the module whether to use the yum (yum3) or dnf (yum4) backend}"

# Generated at 2022-06-13 11:20:24.141780
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    result = dict(
        changed=False,
        rc=0,
        module_stderr="",
        module_stdout="",
    )

    # Name of the task being executed
    task_name = 'yum'

    # If name parameter is passed as argument, then it is passed as _name in task
    task_name = 'yum'

    # Retrieve yum arguments
    task_args = dict(name="vim-enhanced")

    # task_vars is a dictionary which has attributes like ansible_facts and ansible_all_ipv4_addresses
    task_vars = dict()

    # If this value is set in task, then the task is executed asynchronously
    async_val = False

    # Ansible module object
    base_ansible_module = ActionBase()

    # Ansible action

# Generated at 2022-06-13 11:20:33.881306
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    class FakeModule:
        def __init__(self, args=None):
            self.params = args

    class FakeTask:
        def __init__(self, args=None, async_val=False):
            self.args = args
            self.async_val = async_val
            self.tmpdir = ''

    class FakeTaskVars:
        def __init__(self, delegate_to=None, delegate_facts=None):
            self.delegate_to = delegate_to
            self.delegate_facts = delegate_facts

    class FakeFacts:
        def __init__(self, ansible_facts_pkg_mgr=None):
            self.ansible_facts_pkg_mgr = ansible_facts_pkg_mgr
            self.failed = False


# Generated at 2022-06-13 11:20:42.273798
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.facts.system import default_fact_collection
    import ansible.plugins
    assert 'yum' in ansible.plugins.action.ActionModule._plugins

    #yum3 is default
    #facts = default_fact_collection()
    #display.debug("YUM AUTO Facts %s" % facts)
    #assert 'yum' in ansible.plugins.action.ActionModule._plugins
    #module = ansible.plugins.action.ActionModule._plugins['yum'].run(dict(), facts)
    #assert module['changed'] is True
    #assert 'ansible_facts' in module
    #assert 'pkg_mgr' in module['ansible_facts']
    #assert module['ansible_facts']['pkg_mgr'] == 'yum'

    #yum4
   

# Generated at 2022-06-13 11:20:42.917575
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 11:21:00.463682
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule '''
    def test_inner(mocker, tmp_path_factory):
        ''' Inner function for testing ActionModule.run method '''
        mocker.patch.dict('ansible.plugins.action.yum.VALID_BACKENDS',
                          {'yum', 'yum4'})
        mocker.patch('ansible.plugins.loader.ActionModule._execute_module', return_value={'failed': True})
        mocker.patch('ansible.plugins.action.yum.ActionModule._remove_tmp_path')
        mocker.patch('ansible.plugins.action.yum.ActionModule.run')
        args = {}
        module = 'ansible.legacy.yum'

# Generated at 2022-06-13 11:21:01.030185
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:21:05.052196
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Create an instance for the testing of the class constructor
    action = ActionModule("Test", "Test", "Test", "Test")

    # Check the name of the action plugin
    assert action._plugin_name == 'yum', "Instance of the action plugin is not created"

# Generated at 2022-06-13 11:21:06.559890
# Unit test for constructor of class ActionModule
def test_ActionModule(): # noqa
    assert ActionModule is not None

# Generated at 2022-06-13 11:21:07.412864
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 11:21:09.531862
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, {}).__class__.__name__ == 'ActionModule'

# Generated at 2022-06-13 11:21:18.808053
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    # Test good use_backend
    module._task.args['use_backend'] = 'yum'
    module._task.args['name'] = 'test_pkg'
    module._task.args['state'] = 'present'
    module._task.delegate_to = 'localhost'
    module._task.delegate_facts = True
    module._shared_loader_obj.module_loader.has_plugin.return_value = True
    assert module.run() == {'msg': "All items completed", 'results': [], 'changed': False}
    module._task.args['use_backend'] = 'dnf'
    assert module.run() == {'msg': "All items completed", 'results': [], 'changed': False}

# Generated at 2022-06-13 11:21:20.298304
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, None)
    assert am

# Generated at 2022-06-13 11:21:21.359046
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass



# Generated at 2022-06-13 11:21:22.746081
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None)
    assert not action.transfers_files()

# Generated at 2022-06-13 11:21:48.359992
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()



# Generated at 2022-06-13 11:21:49.846102
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, 'run')

# Generated at 2022-06-13 11:21:55.005028
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict(
        ansible_facts=dict(pkg_mgr='yum4')
    )
    _task = dict(
        args=dict()
    )
    _play_context = dict()
    action = ActionModule(_task, _play_context)
    result = action.run(task_vars=task_vars)
    assert "ansible_facts" in result
    assert result["ansible_facts"]["pkg_mgr"] == "dnf"

# Generated at 2022-06-13 11:21:59.675120
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """valuation of yum3 vs. yum4 module run method"""

    # set up input parameters
    mock_module_args = {
        'use': 'yum',
        'name': 'vim'
    }

    # set up mock objects
    mock_task = MagicMock()
    mock_task.args = mock_module_args
    mock_task.module_name = 'yum'
    mock_task.async_val = 21
    mock_task.delegate_to = False
    mock_task.delegate_facts = True

    mock_shared_loader_obj = MagicMock()
    mock_shared_loader_obj.module_loader.has_plugin.return_value = True

    # set up mock ansible.module_utils.basic.AnsibleModule
    mock_ansible_module = Magic

# Generated at 2022-06-13 11:22:00.945215
# Unit test for constructor of class ActionModule
def test_ActionModule():

    ActionModule('yum')

# Generated at 2022-06-13 11:22:09.960442
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 11:22:19.164189
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Set up a required task_vars
    task_vars = dict(
        ansible_pkg_mgr="dnf",
    )

    # Set up a required tmp
    tmp = dict(
        path="/home/username",
    )

    # Set up a required wrap_async
    wrap_async = True

    # Set up a required templar
    templar = Display()

    # Set up a required display
    display = Display()

    # Set up a required loader object
    loader = dict(
        has_plugin = lambda x: True,
    )

    # Set up a required connection object
    connection = dict(
        _shell = dict(
            tmpdir = "/tmp/temp-space",
        )
    )

    # Set up the args for the plugin

# Generated at 2022-06-13 11:22:23.674738
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_plugin = ActionModule(
        task=dict(action=dict(type="yum", args=dict(name=["vim"]))),
        connection=None,
        play_context=dict(check_mode=True, diff=False),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    # pylint: disable=protected-access
    print(action_plugin._task.action)

# Generated at 2022-06-13 11:22:33.385102
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 11:22:34.809504
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.__name__ == 'ActionModule'

# Generated at 2022-06-13 11:23:25.529089
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None, None)
    assert action.VALID_BACKENDS == VALID_BACKENDS

# Generated at 2022-06-13 11:23:38.453091
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import tempfile
    tempdir = tempfile.mkdtemp()
    topdir = tempdir + "/topdir"
    chdir = tempdir + "/chdir"
    os.makedirs(topdir)
    os.makedirs(chdir)
    os.chdir(chdir)

    class Options(object):
        verbosity = 0
        forks = 10
        module_path = tempdir
        become = False
        become_method = None
        become_user = None
        check = False
        extra_vars = Bunch()
        diff = False
        listhosts = None
        listtasks = None
        listtags = None
        syntax = None

    class Tqm(object):
        def __init__(self):
            self.hostvars = dict()

# Generated at 2022-06-13 11:23:44.227738
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test handler ActionModule run
    # Test no errors occur

    # Inject mocks
    import ansible.module_utils.basic
    import ansible.module_utils.facts.system
    import ansible.module_utils.facts.network

    # Setup test ActionModule object
    # Setup test obj for init_data_dispatch_save
    # Setup test obj for find_needle
    # Setup test obj for parse_kv
    # Setup test obj for get_platform
    # Setup test obj for get_distribution
    # Setup test obj for get_file_content
    # Setup test obj for get_distribution_version
    # Setup test obj for strptr
    # Setup test obj for get_all_subclasses
    # Setup test obj for system_distribution
    # Setup test obj for _get_file_content
    # Setup

# Generated at 2022-06-13 11:23:45.475842
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    This is a dummy unit test to be replaced by real tests when implemented.
    """
    assert True

# Generated at 2022-06-13 11:23:46.005475
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:23:46.890690
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None)

# Generated at 2022-06-13 11:23:57.365472
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import mock

    # Setup mock values
    mock_self = mock.Mock()
    mock_self._task = mock.Mock()
    mock_self._task.args = {}
    mock_self._task.delegate_to = 'test_hostname'
    mock_self._task.delegate_facts = True
    mock_self._task.async_val = None
    mock_self._connection = mock.Mock()
    mock_self._connection._shell = mock.Mock()
    mock_self._connection._shell.tmpdir = 'test_tmpdir'
    mock_self._shared_loader_obj = mock.Mock()
    mock_self._shared_loader_obj.module_loader = mock.Mock()
    mock_self._shared_loader_obj.module_loader.has_plugin.return_value

# Generated at 2022-06-13 11:24:01.728443
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    mock_data = {
        "ansible_facts": {
            "pkg_mgr": "dnf"
        },
        "changed": False,
        "msg": "All items completed"
    }

    mock_task = {
        "action": {
            "__ansible_module__": "yum",
            "__ansible_arguments__": {
                "use_backend": "auto"
            }
        },
        "args": {
            "use": "auto"
        },
        "async_val": None,
        "delegate_facts": True,
        "delegate_to": None
    }

    ModuleMock = Mock()
    ActionBaseMock = Mock()
    DisplayMock = Mock()
    DisplayMock.debug = Mock(return_value=mock_task)

# Generated at 2022-06-13 11:24:05.683672
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module.ActionModule(
        task=dict(action=dict(name='yum')),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

# Generated at 2022-06-13 11:24:06.732541
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert 1 == 1

# Generated at 2022-06-13 11:26:00.794119
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = {}
    magic_variable_precedence = ''
    tmp = ''
    action = ''

    module = ActionModule(task_vars, magic_variable_precedence, action, tmp)

    target_module = 'yum'
    module_args = {}
    task_vars = {}
    wrap_async = False

    # _execute_module returns a dictionary.
    # test case when the module is not a backend we recognize
    module_args['use'] = 'invalid'
    result = module._execute_module(module_name=target_module,
                                    module_args=module_args,
                                    task_vars=task_vars,
                                    wrap_async=wrap_async)
    assert result['failed'] == True

# Generated at 2022-06-13 11:26:01.527721
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:26:09.173228
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # mock data
    execution_path = "/path/to/executable"
    connection_info = {}
    connection_info['persistent_connection'] = None
    connection_info['network_os'] = 'any_os'
    connection_info['remote_addr'] = '127.0.0.1'
    connection_info['remote_user'] = 'root'
    connection_info['port'] = 22
    connection_info['become_method'] = 'sudo'
    connection_info['become_user'] = 'root'
    connection_info['become_pass'] = 'rootpass'
    connection_info['module_lang'] = 'python'
    connection_info['module_set_locale'] = False
    connection_info['module_name'] = "setup"
    connection_info['module_args'] = ""

# Generated at 2022-06-13 11:26:12.638416
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test for method run of class ActionModule

    :precondition: Ansible testing framework installed

    :step:
        1. Create a ActionModule object

    :expectedresults:
        1. ActionModule object should be created
    """
    module = ActionModule()

# Generated at 2022-06-13 11:26:20.608421
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Make sure we are not running on ansible < 2.8
    assert(ActionModule.run != ActionBase.run)

    # test case 1: normal case - module auto
    # just call init function and make sure it runs
    action_module_obj = ActionModule(
        task={"args": {"test": "test", "use": "auto"}},
        connection={},
        play_context={},
        loader={},
        templar={},
        shared_loader_obj={})
    action_module_obj.run()

    # test case 2: module specified
    # just call init function and make sure it runs

# Generated at 2022-06-13 11:26:22.371914
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Test complete")

if __name__ == "__main__":
    test_ActionModule()

# Generated at 2022-06-13 11:26:23.271186
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 11:26:25.094197
# Unit test for constructor of class ActionModule
def test_ActionModule():
    p = ActionModule()
    assert(p.VALID_BACKENDS == frozenset(('yum', 'yum4', 'dnf')))

# Generated at 2022-06-13 11:26:26.191636
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test with no argument
    temp_action_module = ActionModule()

# Generated at 2022-06-13 11:26:33.676399
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for the ActionModule class
    '''
    # Set up class
    args = {'use': 'auto'}
    task = type('', (object,), {'args': args, 'async_val': True})

    # Set up mocks
    task_vars = type('', (object,), {'task_vars': {'ansible_facts': {'pkg_mgr': 'auto'}}})
    templar = type('', (object,), {'template': lambda self, template: template})
    module_loader = type('', (object,), {'has_plugin': lambda self, module: True})
    shared_loader_obj = type('', (object,), {'module_loader': module_loader})
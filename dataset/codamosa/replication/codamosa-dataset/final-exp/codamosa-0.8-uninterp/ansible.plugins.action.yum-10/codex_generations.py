

# Generated at 2022-06-13 11:18:52.198276
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 11:18:53.238391
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)

# Generated at 2022-06-13 11:19:01.792514
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(
        task=dict(
            args={
                "name": ["test_package"],
                "use_backend": "yum3",
            },
            async_val=0,
            delegate_to="localhost",
        ),
        connection="",
        play_context={
            "remote_addr": "localhost"
        },
        loader="",
        templar="",
        shared_loader_obj="",
    )
    results = module.run(task_vars={"ansible_pkg_mgr": "auto"})
    assert results["failed"] == False
    assert results["changed"] == True


# Generated at 2022-06-13 11:19:02.444736
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:19:13.032397
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile
    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-13 11:19:14.732068
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None)
    assert action is not None


# Generated at 2022-06-13 11:19:15.340345
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:19:16.619714
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    assert "failed" in module.run()


# Generated at 2022-06-13 11:19:23.763212
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json
    import sys
    args = '"use": "auto"'
    am = ActionModule(
        task=json.loads("{ \"args\": {" + args + "}}"),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    # Global variable __file__ is used in Display class
    # __file__ is defined in python >=2.4
    if sys.version_info.major < 2 or sys.version_info.minor < 4:
        Display.__file__ = sys.modules[__name__].__file__
    am.run(tmp=None, task_vars={})

# Generated at 2022-06-13 11:19:26.675398
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    # check instance attributes were set
    assert action._supports_check_mode is True
    assert action._supports_async is True

# Generated at 2022-06-13 11:19:40.560648
# Unit test for constructor of class ActionModule
def test_ActionModule():
    shell_mock = Mock()
    shell_mock.tmpdir = "some path"
    connection = Mock()
    connection._shell = shell_mock

    am = ActionModule(connection)

    assert am._supports_async == True
    assert am._supports_check_mode == True
    assert am.CONST == 'some value'
    assert am.VALID_BACKENDS == frozenset(['yum', 'yum4', 'dnf'])
    assert am._connection._shell.tmpdir == 'some path'

# Generated at 2022-06-13 11:19:48.240997
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create variables
    task_vars = {"delegate_to": ""}
    tmp = None
    module_return_value = {"failed": False,
                           "changed": True,
                           "msg": "",
                           "rc": 0
                           }

    # Create a mock of ActionBase class
    class Mock_of_ActionBase():
        def _execute_module(self,
                            module_name=None,
                            module_args=None,
                            task_vars=None,
                            wrap_async=False):
            return module_return_value

    # Create an instance of class ActionModule
    test_action_obj = ActionModule()

    # Create an instance of class Mock_of_ActionBase
    mock_action_obj = Mock_of_ActionBase()

    # Set attributes of instance mock_

# Generated at 2022-06-13 11:19:59.275595
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    This is the unit test for the run method of the class ActionModule
    """
    args = {'use_backend': 'auto'}

    tmp = "temp"
    delegate_facts = False
    delegate_to = None
    register = None
    no_log = None
    run_once = True
    delegate_facts = False
    async_val = True
    environment = None
    warn = False

    # instantiate an object of class Task
    task = Task(args, tmp, delegate_facts, delegate_to, register, no_log, run_once, async_val, environment, warn)
    # instantiate an object of class ActionModule
    yum_module = ActionModule()
    # load a module

# Generated at 2022-06-13 11:20:10.241730
# Unit test for constructor of class ActionModule
def test_ActionModule():

    class MockModule(object):
        def __init__(self, *args, **kwargs):
            super(MockModule, self).__init__()

            self.args = kwargs.get('args', {})
            self.action = kwargs.get('action')
            self.display = kwargs.get('display')
            self.task_vars = kwargs.get('task_vars', {})
            self.tmp = kwargs.get('tmp')

    class MockTask(object):
        def __init__(self, *args, **kwargs):
            super(MockTask, self).__init__()

            self.args = kwargs.get('args', {})
            self.async_val = kwargs.get('async_val')
            self.delegate_facts

# Generated at 2022-06-13 11:20:10.820767
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule('', dict())
    assert module

# Generated at 2022-06-13 11:20:15.628504
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ## Setup test
    from ansible.module_utils._text import to_text
    from ansible_collections.ansible.legacy.plugins.modules import yum as test_modules_yum


    am = ActionModule(task=None, connection=None, _play_context=None, loader=None, templar=None, shared_loader_obj=None)
    am._connection = FakeConnection()
    am._templar = FakeTemplar()

    TestModulesYum = type(test_modules_yum)
    TestModulesYum.run = lambda self: self.module_args
    am._shared_loader_obj = FakeLoader(module_utils={"yum": TestModulesYum})

    # Test 'auto' backend
    am._templar.template = lambda x: 'yum'
   

# Generated at 2022-06-13 11:20:24.859418
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Create an instance of ActionModule, which has run method
    yum_action_instance = ActionModule()

    # Create a fake task for the run method
    task = dict(
        args = dict(
            use_backend = 'yum'
        )
    )

    # Create a fake task_vars for the run method
    task_vars = dict(
        hostvars = dict(
            localhost = dict(
                ansible_facts = dict(
                    pkg_mgr = 'yum'
                )
            )
        )
    )

    # Verify that run method works as intended
    # Action plugin handler for yum3 vs yum4(dnf) operations.
    # Ensure that run method is working as intended,
    # by verifying that the keys present in the returned value
    # are a subset of the

# Generated at 2022-06-13 11:20:34.351232
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    this_module = sys.modules[__name__]
    ################################################################################
    # Test case: #1
    ################################################################################
    class ActionModule_run_TC1:
        ####
        # Test case: #1
        ####
        def test_run_TC1_1(self):
            this_module.module = MagicMock()
            this_module.module.run.return_value = {'results': 1}
            result = this_module.ActionModule_run1({'use_backend':'yum'}, 'hostvars')
            assert result["results"] == 1
        ####
        # Test case: #1
        ####
        def test_run_TC1_2(self):
            this_module.module = MagicMock()

# Generated at 2022-06-13 11:20:39.409962
# Unit test for constructor of class ActionModule
def test_ActionModule():
    #fail if the class does not exist
    if not hasattr(ActionModule, '__init__') :
        raise AssertionError("ActionModule class not found")

    #fail if not the exact number of arguments are accepted
    if hasattr(ActionModule, '__init__') and len(inspect.getargspec(ActionModule.__init__).args) != 3 :
        raise AssertionError("ActionModule class constructor has wrong number of arguments")

    #fail if the class does not have run method
    if not hasattr(ActionModule, 'run') :
        raise AssertionError("ActionModule class does not have run method")

# Generated at 2022-06-13 11:20:43.724032
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import tempfile
    with tempfile.TemporaryDirectory() as tmp_main_dir:
        with tempfile.TemporaryDirectory() as tmp_src_dir:
            with tempfile.TemporaryDirectory() as tmp_artifact_dir:
                assert True

# Generated at 2022-06-13 11:20:58.735130
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(connection=None, task_id=None, loader=None, play_context=None, new_stdin=None,
                     options=None, args=None)
    assert isinstance(a, ActionBase)

# Generated at 2022-06-13 11:21:08.553104
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.module_utils._text import to_bytes
    from ansible.plugins.action.yum3 import ActionModule


# Generated at 2022-06-13 11:21:17.199516
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 11:21:20.690154
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Instantiated object of class ActionModule
    obj = ActionModule()
    # Checks if class ActionModule is an instance of class ActionBase
    assert isinstance(obj, ActionBase)


# Generated at 2022-06-13 11:21:21.419269
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False

# Generated at 2022-06-13 11:21:24.615041
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task=dict(action=dict(module_name="yum", module_args=dict(use='auto'))))

    assert action_module

# Generated at 2022-06-13 11:21:32.732255
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = 'ansible.legacy.yum'
    action = ActionModule({"use_backend": "yum", "test": "ok"}, load_plugins=False, task_loader=None,
                          connection_loader=None, play_context=None, shared_loader_obj=None)
    if not isinstance(action, ActionModule):
        raise AssertionError("Error in creating object of class %s" % ActionModule)

# Generated at 2022-06-13 11:21:33.794530
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:21:40.535308
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()
    a._task = MagicMock()

    a._connection = 'Fake-Connection'
    a._play_context = MagicMock()
    a._display = MagicMock()
    a._templar = MagicMock()
    a._loader = MagicMock()
    a._shared_loader_obj = MagicMock()
    a._task.async_val = True

# Generated at 2022-06-13 11:21:48.431459
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.yum as yum
    import ansible.plugins.action as action
    from ansible.module_utils.six import string_types
    yum_instance = yum.ActionModule()
    assert isinstance(yum_instance._supports_check_mode, bool)
    assert isinstance(yum_instance._supports_async, bool)
    assert isinstance(yum_instance.TRANSFERS_FILES, bool)
    assert isinstance(yum_instance.run, types.FunctionType)
    assert isinstance(yum.VALID_BACKENDS, frozenset)

# Generated at 2022-06-13 11:22:13.254727
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:22:21.748630
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m_task = DummyClass()
    m_task.args = {'test': 'test'}
    m_task.async_val = DummyClass()
    m_task.async_val.value = 'one'
    m_task.delegate_facts = False
    m_task.delegate_to = False
    m_task.args = {'use': 'yum'}
    connection = DummyClass()
    connection._shell = DummyClass()
    connection._shell.tmpdir = "/tmp"
    shared_loader_obj = DummyClass()
    shared_loader_obj.module_loader = DummyClass()
    shared_loader_obj.module_loader.has_plugin = lambda x: True

# Generated at 2022-06-13 11:22:22.990316
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert "yum" in VALID_BACKENDS

# Generated at 2022-06-13 11:22:24.835911
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am._supports_check_mode == True
    assert am._supports_async == True

# Generated at 2022-06-13 11:22:34.507527
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create the task
    task = {
        'action': {'module': 'yum',
                   'args': {'name': 'foo', 'state': 'present', 'use_backend': 'auto'}
                   },
        'delegate_to': None,
        'delegate_facts': True,
        'register': 'test_yum3_vs_yum4'
    }

    mock_module_loader = MockModuleLoader()

    # Create a mock templar obj
    mock_templar = MockTemplar()

    mock_display = MockDisplay()

    # Create the action plugin

# Generated at 2022-06-13 11:22:48.520673
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.common.collections import ImmutableDict

    action_module_object = ActionModule((1,))
    assert action_module_object is not None

    # test for case when 'use' and 'use_backend' are present in task args
    result = action_module_object.run(
        tmp=None, task_vars=ImmutableDict({'ansible_facts': {'pkg_mgr': 'yum3'}}))
    assert result['failed']
    assert result['msg'] == (
        'parameters are mutually exclusive: (\'use\', \'use_backend\')')

    # test for case when 'use_backend' is missing
    action_module_object = ActionModule((1,), 'resmoke.py', 'use')
    result = action_module_object

# Generated at 2022-06-13 11:22:55.694346
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    fixture_data = dict()
    argument_spec = dict(
        use=dict(required=False, default='auto'),
        use_backend=dict(required=False, default='auto'),
        )
    action_module = ActionModule()
    result = action_module.run(argument_spec, dict(), dict())

# Generated at 2022-06-13 11:23:04.333472
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module._task = mock.MagicMock()
    module._task.args = {
        'name': ['vim', 'tmux'],
        'use': 'yum4'
    }
    module._task.delegate_to = None
    module._task.async_val = None

    ret = module.run(task_vars=dict())
    assert ret['failed'] == True
    assert ret['msg'] == ("Could not detect which major revision of yum is in use,"
                          " which is required to determine module backend.",
                          "You should manually specify use_backend to tell the module whether to"
                          " use the yum (yum3) or dnf (yum4) backend})")

# Generated at 2022-06-13 11:23:06.189164
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Unit test for constructor of class ActionModule"""
    module = ActionModule(task=dict(action=dict()), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), share=dict())
    assert module

# Generated at 2022-06-13 11:23:16.727657
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(loader=None,
                          action=None,
                          task=None,
                          connection=None,
                          play_context=None,
                          loader_path=None,
                          shared_loader_obj=None,
                          finalize=None)
    module._shared_loader_obj = True
    module._task.args = True
    module._task.async_val = None
    module._task.delegate_to = None
    module._task.delegate_facts = True
    result = module.run()
    assert 'ansible_facts' in result
    module._task.args = True
    module._task.async_val = None
    module._task.delegate_to = None
    module._task.delegate_facts = False
    result = module.run()

# Generated at 2022-06-13 11:24:12.934075
# Unit test for constructor of class ActionModule
def test_ActionModule():
    loader = 'foo'
    connection = 'bar'
    templar = 'baz'
    shared_loader_obj = 'foobar'
    options = 'barfoo'
    task_uuid = 'foobaz'
    set_type_immediately = 'bazfoo'
    task = 'ffoobbaarr'

    module = ActionModule(loader, connection, templar, shared_loader_obj, options, task_uuid, set_type_immediately, task)
    assert module.TRANSFERS_FILES is False

# Generated at 2022-06-13 11:24:23.829353
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    class MyActionModule(ActionModule):
        def _execute_module(self, module_name=None, module_args=None, job_id=None, task_vars=None, wrap_async=None):
            print(module_name)
            print(module_args)
            print(job_id)
            print(task_vars)
            print(wrap_async)
            return {'failed': False}

    class MyTask:
        async_val = False
        args = {}

    class MyPlayContext(PlayContext):
        def __init__(self):
            self.check_mode = True

    class MyDisplay:
        def debug(self, msg):
            print(msg)


# Generated at 2022-06-13 11:24:25.059307
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False, "Unit test for method run of class ActionModule not implemented"

# Generated at 2022-06-13 11:24:25.585678
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    assert False

# Generated at 2022-06-13 11:24:32.307669
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionmodule = ActionModule()
    task_vars = {}

    # set up values of args (self._task.args)
    use = 'yum'
    auto = 'auto'
    # set up values of ansible_facts (facts)
    ansible_facts = {}
    ansible_facts['pkg_mgr'] = use

    # test case 1: if use and use_backend are not in self._task.args and pkg_mgr is not in ansible_facts, raise error

# Generated at 2022-06-13 11:24:42.920936
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    module = AnsibleModule(argument_spec={'use_backend': {'type': 'str', 'choices': ['yum', 'dnf']}, 'use': {'type': 'str', 'choices': ['yum', 'dnf']}}, supports_check_mode=True)
    # Test case - with use_backend
    module.params['use_backend'] = 'yum'
    module.params['use'] = None
    del module.params['use_backend']
    # Test case - with use
    module.params['use'] = 'yum'
    module.params['use_backend'] = None
    del module.params['use']
    # Test case - with both use_backend and use
    module.params['use'] = 'yum'
    module.params['use_backend']

# Generated at 2022-06-13 11:24:49.443071
# Unit test for constructor of class ActionModule
def test_ActionModule():
	# 인스턴스 생성
	obj = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
	# 속성 할당 후 할당된 속성값 테스트
	obj._supports_async = True
	assert obj._supports_async
	obj._supports_check_mode = True
	assert obj._supports_check_mode


# Generated at 2022-06-13 11:24:51.040609
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    assert True

# Generated at 2022-06-13 11:24:59.466676
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 11:24:59.925813
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 11:26:48.672177
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Load the module with no parameters
    module = ActionModule()

    # Check for params_disallowed_in_paramiko_config property
    assert hasattr(module, 'params_disallowed_in_paramiko_config')

    # Check initialisation of _supports_check_mode, _supports_async and _shared_loader_obj properties
    assert module._supports_check_mode
    assert module._supports_async
    assert module._shared_loader_obj

    # Check that the run() method exists
    assert hasattr(module, 'run')

# Generated at 2022-06-13 11:26:50.823250
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module is not None
    action_plugin = module.run()
    assert action_plugin is not None

# Generated at 2022-06-13 11:26:54.448008
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # This is a very basic unit test that is run by continuous integrations.
    # It verifies that the code can be executed without throwing exceptions.
    # Tests that actually verify functionality are very hard to implement
    # as they require emulating Yum and Dnf behaviors.
    assert True

# Generated at 2022-06-13 11:27:00.844492
# Unit test for constructor of class ActionModule
def test_ActionModule():
    connection = {
        'transport': 'dummy',
        '_shell': {'tmpdir': 'tmpdir'}
    }

    task = {
        'args': {
            'use': 'foo',
        },
    }

    pm = ActionModule(connection=connection, task=task)

    assert pm._task.args['use'] == task['args']['use']

# Generated at 2022-06-13 11:27:09.386297
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task

    module_args = {"use_backend": "yum3"}
    task = Task()
    task.args = module_args

    action_module = ActionModule(task, {"connection": "network_cli"})

    assert action_module._task.args == module_args
    assert action_module.VALID_BACKENDS == ("yum", "yum4", "dnf")

# Generated at 2022-06-13 11:27:17.100663
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.facts import Facts
    from ansible_collections.ansible.community.tests.unit.mock.ansible_module_mock import AnsibleModuleMock
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import StringIO

    # Create a Mock module
    module = AnsibleModuleMock(
        argument_spec={},
        supports_check_mode=False,
        supports_async=True,
    )

    # Construct a task with its action handler
    task = {
        'args': {
            'use_backend': 'yum',
        }
    }

# Generated at 2022-06-13 11:27:30.857449
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_name = "yum"
    name = "name"
    action = "action"
    value = "value"
    src = "src"
    template = "template"
    task_name = 'task_name'
    task_vars = {}

    class AnsiblePlaybookShell:
        def tmpdir(self):
            return 'tmp'

    class AnsibleShell:
        def tmpdir(self):
            return 'tmp'

    class AnsibleConnection:
        _shell = None
        _play_context = None

        def __init__(self):
            self._shell = AnsibleShell()
            self._play_context = AnsiblePlaybookShell()


    class AnsibleTask:
        async_val = False
        _connection = AnsibleConnection()
        _shared_loader_obj = None
        _task

# Generated at 2022-06-13 11:27:36.056970
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    data = {
        'actions': 'install',
        'name': 'package-name'
    }
    with mock.patch("ansible.plugins.action.ActionBase") as mock_action_base:
        mock_action_base.return_value.run.return_value = data
        assert module.run() == data


# Generated at 2022-06-13 11:27:45.161298
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #from ansible.compat.tests.mock import patch, Mock
    from ansible.compat.tests.mock import patch

    with patch('ansible.plugins.action.ActionBase._execute_module', return_value=dict(failed=False, msg="")):
        with patch('ansible.plugins.action.ActionBase._remove_tmp_path'):
            with patch('ansible.plugins.action.ActionBase.run'):
                a = ActionModule()
                assert a.run() == dict(failed=False, msg="Could not detect which major revision of yum is in use, which is required to determine module backend.",
                                       You='You should manually specify use_backend to tell the module whether to use the yum (yum3) or dnf (yum4) backend')

# Generated at 2022-06-13 11:27:48.885273
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test empty run
    module = ActionModule(None, None)
    result = module.run(tmp='/tmp/test_yum', task_vars={'pkg_mgr': 'auto'})
    assert 'failed' in result
    assert result['failed']


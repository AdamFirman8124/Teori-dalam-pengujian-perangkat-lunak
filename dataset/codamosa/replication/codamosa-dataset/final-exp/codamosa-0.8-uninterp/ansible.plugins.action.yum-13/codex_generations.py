

# Generated at 2022-06-13 11:18:59.647112
# Unit test for constructor of class ActionModule
def test_ActionModule():

    test_dict = {
        "myvar": "myval",
        "othervar": "otherval",
        "password": "secretpassword"
    }

    test_task = {
        "action": {
            "__ansible_module__": "yum",
            "__ansible_arguments__": "",
            "__ansible_verbosity__": 4
        },
        "args": test_dict
    }

    test_task_vars = {
        "inventory_hostname": "localhost",
        "group_names": [
            "ungrouped"
        ],
        "groups": {
            "ungrouped": []
        }
    }

    test_tmp = "/tmp/ansible-tmp-1538583623.92-99355356011290"


# Generated at 2022-06-13 11:19:05.675191
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(loader=None, connection=None, play_context=None,
                          new_stdin=None, shell=None, module_compression=None,
                          as_root=None, privileged=None,
                          persist_files=False,
                          _old_async_val=None, _task_vars=None, _task_type=None,
                          _task_path=None, _task_lang=None, _task_action=None,
                          _task_args=None, _shared_loader_obj=None,
                          _role=None, _loader_cache=None, _display=None,
                          _tmp_path=None, _task=None, _play_context=None)
    assert action is not None
    assert isinstance(action, ActionModule)

# Generated at 2022-06-13 11:19:15.548380
# Unit test for constructor of class ActionModule
def test_ActionModule():

    action_module = ActionModule()

    assert hasattr(action_module, '_supports_check_mode'), "ActionModule must have attribute '_supports_check_mode'"
    assert hasattr(action_module, '_supports_async'), "ActionModule must have attribute '_supports_async'"
    assert hasattr(action_module, '_loose_version'), "ActionModule must have attribute '_loose_version'"
    assert hasattr(action_module, '_conn'), "ActionModule must have attribute '_conn'"
    assert hasattr(action_module, '_templar'), "ActionModule must have attribute '_templar'"
    assert hasattr(action_module, '_loader'), "ActionModule must have attribute '_loader'"

# Generated at 2022-06-13 11:19:18.532273
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        {'use': 'yum'},
        {},
        {},
        {}
    )
    module._shared_loader_obj.module_loader.has_plugin('doesnt_exist')
    module.run()

# Generated at 2022-06-13 11:19:29.720171
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create our object
    class Task(object):
        def __init__(self):
            self.args = {}
    class Connection(object):
        def __init__(self):
            self._shell = object
    class Shell(object):
        def __init__(self):
            self.tmpdir = ''
    class PlayContext(object):
        def __init__(self):
            self.check_mode = True
            self.connection = None
    class Runner(object):
        def __init__(self):
            self._shared_loader_obj = None
            self._loader = None
            self._templar = None
            self.options = None
            self.variable_manager = None
            self.plugins = None
    class Playbook(object):
        def __init__(self):
            self.basedir = ''

# Generated at 2022-06-13 11:19:31.709448
# Unit test for constructor of class ActionModule
def test_ActionModule():

    t = ActionModule('name', 'task_details')

    assert t.name == 'name'
    assert t._task == 'task_details'

# Generated at 2022-06-13 11:19:32.711083
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    m.run()

# Generated at 2022-06-13 11:19:33.552510
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:19:37.226724
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_plugin = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_plugin.__class__.__name__ == 'ActionModule'

# Generated at 2022-06-13 11:19:44.197816
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("----test_ActionModule----")
    # An ansible_module_runner.Runner object
    runner = object()
    # An ansible.inventory.hosts.Host object
    host = object()
    # An ansible.playbook.play.Play object
    play = object()
    # The list of tasks that are executed on this host
    task = object()
    # An ansible.vars.manager.VariableManager object
    variable_manager = object()
    # A dictionary that contains system/OS information
    loader = object()
    # An ansible.parsing.dataloader.DataLoader object
    templar = object()
    shared_loader_obj = object()
    # The persistent connection is the connection used by the PlayContext
    # object and may be used by other classes as well
    connection = object()


# Generated at 2022-06-13 11:19:52.830625
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=dict(), connection=dict(), play_context=dict())


# Generated at 2022-06-13 11:19:56.239382
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Create an instance and call run"""
    module = ActionModule(
        task=dict(args=dict(name='ansible')),
        connection=dict(play_context=dict(check_mode=True)),
        templar=dict(),
        shared_loader_obj=dict()
    )
    module.run()

# Generated at 2022-06-13 11:20:00.307976
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Arrange - mocks
    class MockedActionModule(ActionModule):
        def _execute_module(self, *args, **kwargs):
            return dict(delegate_to="unit.host.com")

        def _templar(self, tmpl):
            return "yum3"

    instance = MockedActionModule()
    instance.run(task_vars=None)

    # Assert - mocks
    assert(instance)
    assert(instance._execute_module)

# Generated at 2022-06-13 11:20:08.022027
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = AnsibleModule(argument_spec={
        'use': {'required': False, 'default': 'auto'},
        'use_backend': {'required': False, 'default': 'auto'}
    })
    a = ActionModule(m)
    # check values of instance variable
    assert a._supports_check_mode is True
    assert a._supports_async is True
    assert a._task.args['use'] == 'auto'
    assert a._task.args['use_backend'] == 'auto'

# Generated at 2022-06-13 11:20:13.001034
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create temporary directory for unit testing
    import tempfile
    tmpdir = tempfile.mkdtemp()

    # Create a mock connection for the ActionModule class
    from ansible.plugins.connection.local import Connection
    conn = Connection(tmpdir)

    # Create a mock loader for the ActionModule class
    from ansible.plugins.loader import PluginLoader
    loader = PluginLoader(
        'ansible.plugins.action',
        'ActionModuleTest',
        C.DEFAULT_INVENTORY_PLUGIN_PATH,
        'action')
    action_plugin = ActionModule(conn, 'async', loader=loader)

    # Create mock task for the ActionModule class
    from ansible.task import Task
    task = Task()
    task.async_val = 100

# Generated at 2022-06-13 11:20:18.792299
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    async_val = False
    wrap_async = False
    display = Display()
    cls = ActionModule(async_val=async_val)
    cls._task.async_val = async_val
    cls._task.delegate_facts = False
    cls._task.delegate_to = None
    cls._task.args = {'use': 'auto'}
    backend = 'yum'
    facts = {'ansible_facts': {'pkg_mgr': backend}}
    tmp = None
    task_vars = {'ansible_check_mode': False, 'ansible_verbose_override': False}

# Generated at 2022-06-13 11:20:29.947839
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Define Test ActionModule class for unit test
    class TestActionModule(ActionModule):
        def __init__(self, *args, **kwargs):
            self._task = None
            self._connection = None
            self._play_context = None
            self._loader = None
            self._templar = None
            self._shared_loader_obj = None
            super(TestActionModule, self).__init__(*args, **kwargs)


# Generated at 2022-06-13 11:20:31.835411
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(dict(), dict(), "/path/to/ansible/lib").__class__.__name__ == 'ActionModule'

# Generated at 2022-06-13 11:20:32.485237
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 11:20:32.984053
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 11:20:57.523183
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action
    reload(ansible.plugins.action)  # in case nitty was previously imported
    import ansible.plugins.action.yum as yum
    reload(yum)  # in case nitty was previously imported
    import ansible.plugins.action.yum as nitty
    reload(nitty)  # in case nitty was previously imported
    import ansible.plugins.action.yum as yum4
    reload(yum4)  # in case nitty was previously imported
    import dnf
    import yum
    module = ActionModule()
    assert isinstance(module, ActionBase)
    assert isinstance(module, ActionModule)
    assert not isinstance(yum, ActionBase)
    assert not isinstance(yum4, ActionBase)

# Generated at 2022-06-13 11:21:06.483139
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''
    action_module = ActionModule()

# Generated at 2022-06-13 11:21:13.475928
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import unittest

    class FakeActionBase(ActionBase):

        def __init__(self):
            pass

        def _execute_module(self, **params):
            return {'result': 'fake_execute_module_method ' + json.dumps(params)}

    class FakeTemplar(object):

        def template(self, template_string):
            return 'fake_template_method ' + template_string

    # Test case 1: module == auto

    # pkg_mgr == yum
    task_vars = {'ansible_pkg_mgr': 'yum'}

# Generated at 2022-06-13 11:21:23.363243
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(task={'args': {}})

    assert module._execute_module(module_name='ansible.legacy.setup',
                                  module_args={'filter': 'ansible_pkg_mgr', 'gather_subset': '!all'},
                                  task_vars={'ansible_facts': {'pkg_mgr': 'yum'}}) == \
           {'failed': False, 'invocation': {'module_args': {'filter': 'ansible_pkg_mgr', 'gather_subset': '!all'}},
            'ansible_facts': {'ansible_pkg_mgr': 'yum'}, 'changed': False}


# Generated at 2022-06-13 11:21:32.731895
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(None, None)

    # Test module when there is no exception
    result = module.run(tmp=None,task_vars=None)
    assert result['failed'] == False

    # Test module when there is an exception
    result['failed'] = False
    module._task.args = {'use': 'auto', 'use_backend':'yum'}
    module._templar = None
    result.update(module.run(tmp=None,task_vars=None))
    assert result['failed'] == True

# Generated at 2022-06-13 11:21:33.522781
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:21:44.253844
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class FakeTask:
        def __init__(self, args, delegate_to, delegate_facts, async_val):
            self.args = args
            self.delegate_to = delegate_to
            self.delegate_facts = delegate_facts
            self.async_val = async_val

    fake_module = ActionModule(
        FakeTask(
            args={
                'use_backend': 'yum4',
            },
            delegate_to='foo',
            delegate_facts=True,
            async_val=True,
        ),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None,
    )

# Generated at 2022-06-13 11:21:50.405860
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    This test covers additional functionality that isn't already
    covered in tests for modules/package/yum.

    Testing for the functionality of the backend module functionality
    is covered in tests for modules/package/yum3/main.py and
    modules/package/dnf/main.py.
    '''

    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.yum import ActionModule

    from units.compat.mock import patch
    import json

    mock_task = MagicMock()
    mock_connection = MagicMock()

    mock_action_base = ActionBase(mock_task, mock_connection)


# Generated at 2022-06-13 11:21:59.053299
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = dict(use='auto')
    task_vars = dict()
    tmp = tempfile.mkdtemp()
    mock_shared_loader_obj = mock.Mock()
    mock_shared_loader_obj.module_loader = mock.Mock()
    mock_shared_loader_obj.module_loader.has_plugin.return_value = True
    mock_connection = mock.Mock()
    mock_connection._shell.tmpdir = tmp
    mock_task = mock.Mock()
    mock_task.args = task
    mock_task.async_val = 'test'
    mock_task.delegate_to = 'localhost'
    mock_task.delegate_facts = True

# Generated at 2022-06-13 11:21:59.713743
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:22:34.397952
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 11:22:39.194655
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert isinstance(module, ActionModule)
    assert module._supports_async == True
    assert module._supports_check_mode == True
    assert module.TRANSFERS_FILES == False


# Generated at 2022-06-13 11:22:50.378178
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    with pytest.raises(AnsibleActionFail) as excinfo:
        am = ActionModule(None, {})
        am._task.args = {'use': 'yum', 'use_backend': 'yum'}
        am.run(None, None)
    assert "parameters are mutually exclusive: ('use', 'use_backend')" in str(excinfo.value)

    am = ActionModule(None, {})
    am._task.args = {'use_backend': 'auto'}
    am._task.delegate_to = 'localhost'
    am._templar.template = lambda x: 'auto'
    assert am.run(None, None) == {'changed': False, 'msg': "yum3 is already the latest version", 'rc': 0, 'results': []}


# Generated at 2022-06-13 11:22:59.608672
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ast

    task_args = {'_raw_params': 'install httpd-1.0',
                 '_uses_shell': False,
                 '_ansible_selinux_special_fs': ['fuse', 'nfs', 'vboxsf', 'ramfs', '9p'],
                 '_ansible_no_log': False,
                 '_ansible_check_mode': False,
                 'use': 'auto',
                 'name': ['httpd']}

    task_vars = {}
    tmp = "/tmp/xyz"
    fake_display = object()
    fake_loader_obj = object()
    fake_tmp_path = object()


# Generated at 2022-06-13 11:23:06.404005
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import unittest
    import sys

    if sys.version_info[0] == 3 and sys.version_info[1] >= 4:
        from unittest.mock import patch
    else:
        from mock import patch

    class TestActionModule(unittest.TestCase):

        def setUp(self):
            # Without these lines the test will not work in the circle CI.
            # For some reason, the dnf module is not found when this test is
            # run in the CircleCI environment.  It works locally.
            import ansible.plugins.action.yum
            import ansible.modules.system.yum as dnf
            ansible.plugins.action.yum.dnf = dnf

            self.test_data = {}
            self.test_data['tmp'] = "tmp"
            self

# Generated at 2022-06-13 11:23:14.587549
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = {'argument_spec': dict(
        command=dict(type='str', aliases=['name']),
    ), 'required_one_of': [
        ['command', 'x']
    ]}

    task = {'args': {'command': 'd', 'path': 'p', 'root': 'r'}}
    am = ActionModule(task, module, {})
    assert am._task.args['command'] == 'd'
    assert am._task.args['root'] == 'r'
    assert am._task.args['path'] == 'p'

# Generated at 2022-06-13 11:23:15.985977
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, '__init__')

# Generated at 2022-06-13 11:23:19.215322
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule({})
    assert(action_module._supports_check_mode == True)
    assert(action_module._supports_async == True)
    assert(action_module.TRANSFERS_FILES == False)

# Generated at 2022-06-13 11:23:22.080045
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.loader import ActionModuleLoader

    assert 'yum' in ActionModuleLoader().all

# Generated at 2022-06-13 11:23:25.293844
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_plugin_ActionModule_instance = ActionModule()

    tmp = None
    task_vars = None

    action_plugin_ActionModule_instance.run(tmp, task_vars)

# Generated at 2022-06-13 11:24:26.165499
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(module_arg_spec=dict(), module_name='module-name')

    module._supports_check_mode = True
    module._supports_async = True

    # test with 'use_backend' in the argument list
    module._task.args = dict(use_backend='auto')
    result = module.run(tmp=None, task_vars=dict())
    assert 'failed' in result
    assert 'msg' in result

    # test with 'use' in the argument list
    module._task.args = dict(use='auto')
    result = module.run(tmp=None, task_vars=dict())
    assert 'failed' in result
    assert 'msg' in result

    # test with 'use' & 'use_backend' in the argument list
    module._task.args

# Generated at 2022-06-13 11:24:31.827136
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Unit test for constructor of class ActionModule"""

# Generated at 2022-06-13 11:24:42.534116
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    action_module._display = display
    action_module.templar = action_module._shared_loader_obj.templar
    action_module._templar = action_module._shared_loader_obj.templar
    action_module._task = action_module._shared_loader_obj.templar
    action_module._connection = action_module._shared_loader_obj.templar
    action_module._shell = action_module._shared_loader_obj.templar
    action_module._execute_module = action_module._shared_loader_obj.templar
    action_module._remove_tmp_path = action_module._shared_loader_obj.templar
    action_module._supports_check_mode = True
    action_module._supports_async

# Generated at 2022-06-13 11:24:57.000392
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("####################################################")
    print("# Constructor")
    print("####################################################")
    am = ActionModule('name', 'module_utils')
    print("####################################################")
    print("# Task")
    print("####################################################")
    task_args = {'use': 'auto', 'state': 'installed'}
    am.set_task_args(task_args)
    print("####################################################")
    print("# run()")
    print("####################################################")
    task_vars = {'ansible_pkg_mgr': 'yum'}
    am.run(task_vars)
    print("####################################################")
    print("# run() with no tmp set")
    print("####################################################")
    am.run()
    print("####################################################")


# Generated at 2022-06-13 11:25:13.154279
# Unit test for constructor of class ActionModule
def test_ActionModule():
    def set_module_args(args):
        args = json.dumps({'ANSIBLE_MODULE_ARGS': args})
        basic._ANSIBLE_ARGS = to_text(args)

    def execute_module(module_name='', module_args=None, tmp=None, task_vars=None):
        args = module_args or {}
        set_module_args(args)
        task_args = json.load(basic._ANSIBLE_ARGS)
        del task_args['ANSIBLE_MODULE_ARGS']
        task_vars = task_vars or {}

        # generate a temporary path on the remote node
        tmp = utils.tmp_path()

# Generated at 2022-06-13 11:25:15.324698
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(dict(action="setup"))
    assert action

# Unit test imports

# Generated at 2022-06-13 11:25:16.828771
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.yum as yum

    yum.ActionModule()

# Generated at 2022-06-13 11:25:26.543279
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # set up a mock task and connection
    mock_task = Mock()
    mock_task.args = {}
    mock_connection = Mock()
    mock_connection._shell = Mock()
    mock_connection._shell.tmpdir = "/tmp/"

    # set up a mock of a loaded module plugin
    class mock_module_loader:
        def has_plugin(self, name):
            if name == "ansible.legacy.yum":
                return True
            else:
                return False

    # set up a mock templar
    # use a subclass of the AnsibleTemplar class to be able to mock the template() method
    # https://docs.python.org/2/library/test.html#test-testsupport

# Generated at 2022-06-13 11:25:37.540444
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.plugins.action.yum import ActionModule
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import StringIO
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    # Create AnsibleContext objects
    loader = DataLoader()
    variable_manager = VariableManager()

    action_module = ActionModule(loader=loader, templar=None, shared_loader_obj=None)
    action_module._shared_loader_obj = loader



# Generated at 2022-06-13 11:25:38.547240
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, None)

# Generated at 2022-06-13 11:27:36.996319
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.loader import action_loader

    class ActionModule(ActionModule):

        def _execute_module(self, module_name, module_args=None, task_vars=None, wrap_async=False):
            pass

    class Task:
        def __init__(self, args):
            self.args = args

    class PlayContext:
        def __init__(self, use_backend):
            self.check_mode = False
            self.become = True
            self.become_user = True
            self.become_method = 'sudo'
            self.become_flags = "-H"
            self.verbosity = False
            self.use_backend = use_backend
            self.remote_addr

# Generated at 2022-06-13 11:27:39.248520
# Unit test for constructor of class ActionModule
def test_ActionModule():
    temp = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert temp is not None

# Generated at 2022-06-13 11:27:39.908579
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionmodule = ActionModule()

# Generated at 2022-06-13 11:27:43.476445
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test of method run of class ActionModule
    """
    import ansible.plugins.action.yum as yum

    action_module = yum.ActionModule()

    assert action_module.run() == {}



# Generated at 2022-06-13 11:27:44.449281
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule('test', '', {})

# Generated at 2022-06-13 11:27:46.799978
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=dict(), connection=None, play_context=None, loader=None,
                                 templar=None, shared_loader_obj=None)
    assert action_module._task is not None

# Generated at 2022-06-13 11:27:50.112614
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module.run(None, None) is not None
    module = ActionModule()
    assert module.VALID_BACKENDS == frozenset(['yum', 'yum4', 'dnf'])

# Generated at 2022-06-13 11:27:55.298811
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Initializing class obj with empty args and empty task_vars
    test_obj = ActionModule(dict(), dict())
    # The _task class variable is None by default.
    assert test_obj._task is None
    # The _supports_check_mode class variable is True by default.
    assert test_obj._supports_check_mode is True
    # The _supports_async class variable is True by default.
    assert test_obj._supports_async is True

# Generated at 2022-06-13 11:28:00.615241
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(async_val=False, args=dict(use='auto')),  # Setting use = 'auto' indicates to select backend automatically
        connection=dict(conn_keys=[], play_context=dict()),
        play_context=dict(),
        loader=dict(),
        templar=dict()
    )
    
    type(module) == ActionModule


# Generated at 2022-06-13 11:28:04.764731
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils._text import to_text
    from ansible.vars.unsafe_proxy import UnsafeProxy

    action = ActionModule({}, {})

    assert isinstance(action, ActionBase)
    assert action._supports_check_mode == True
    assert action._supports_async == True

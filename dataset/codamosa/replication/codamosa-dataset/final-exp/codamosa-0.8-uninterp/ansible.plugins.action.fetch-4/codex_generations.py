

# Generated at 2022-06-13 09:55:37.107902
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(action, ActionBase)

    action = ActionModule(dict(), task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(action, ActionBase)


# Generated at 2022-06-13 09:55:45.870787
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os

    import pytest

    from ansible.errors import AnsibleError, AnsibleActionFail, AnsibleActionSkip

    # Unit test to verify object creation of class ActionModule
    def test_ActionModule_obj(mocker):
        action_mod = ActionModule(mocker.MagicMock(), mocker.MagicMock(), '/tmp/ansible_fetch_payload', False)
        assert type(action_mod) == ActionModule

    # Unit test to verify run method from class ActionModule
    def test_ActionModule_run(mocker, monkeypatch):
        # Mock the return values for the test
        resp = mocker.MagicMock(spec=dict)
        resp.return_value = {"failed": True, "msg": "source is a directory, fetch cannot work on directories"}

# Generated at 2022-06-13 09:55:56.842638
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for method run."""
    # 1. ActionModule instance
    # Since run() is the last action method of the ActionBase class,
    # the only way in which all method of ActionBase, which is the
    # parent class of ActionModule, are called is in the constructor.
    # So, we don't need to write a test for run() method.
    # Only what we need to test here are some attributes, which are
    # taken from their parents.
    yaml = """
    - hosts: all
      tasks:
        - name: test
          fetch:
            src: /tmp/foo.txt
            dest: /tmp/
    """
    results = list(Play().load(yaml, variable_manager=VariableManager(), loader=DataLoader()).run())
    assert results[0]._task.action == 'fetch'

# Generated at 2022-06-13 09:56:08.211070
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.fetch import ActionModule
    from ansible.plugins.connection.local import Connection
    from ansible.inventory import Inventory
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    inventory = Inventory(loader=None, variable_manager=None, host_list=[])
    variable_manager = None
    loader = None

    context = PlayContext(remote_addr='127.0.0.1', port=22)

# Generated at 2022-06-13 09:56:20.527986
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import mock
    # Mocking the _create_remote_tmp_dir method to avoid creating the tmp dir
    with mock.patch("ansible.plugins.action.fetch.ActionModule._create_remote_tmp_dir", return_value="tmp"):
        action_module = ActionModule(mock.MagicMock(), mock.MagicMock())
        source = "fake_source_path"
        dest = "fake_dest_path"
        task_vars = dict()

        # Ensuring that when the remote file doesn't exist, remote_checksum becomes "1" and
        # an error is raised

# Generated at 2022-06-13 09:56:29.335485
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_action_module = ActionModule(load_config_file=False)

    # Test validates src and dest are strings
    args_dict = dict(src=123, dest='/tmp/dest')
    result = test_action_module.run(tmp=None, task_vars=None, **args_dict)
    assert(result['failed'] == 1)
    assert(result['msg'] == 'Invalid type supplied for source option, it must be a string')

    args_dict = dict(src='/tmp/src', dest=123)
    result = test_action_module.run(tmp=None, task_vars=None, **args_dict)
    assert(result['failed'] == 1)
    assert(result['msg'] == 'Invalid type supplied for dest option, it must be a string')

    # Test validate src and dest

# Generated at 2022-06-13 09:56:32.759196
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    test_ActionModule - unit test for constructor of class ActionModule
    '''
    action_module = ActionModule()

    assert action_module
    assert isinstance(action_module, ActionBase)

# Generated at 2022-06-13 09:56:43.615600
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class FakedArgv:
        def __init__(self, args):
            self.args = args
        def __getitem__(self, i):
            return self.args[i]
        def __len__(self):
            return len(self.args)

    class FakedVarsManager:
        def __init__(self, vars):
            self.vars = vars
        def get_vars(self, loader=None, play=None, task=None, include_hostvars=True):
            return self.vars

    import sys
    from ansible.executor.task_result import TaskResult
    from ansible.executor.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

# Generated at 2022-06-13 09:56:46.520957
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(
        task=dict(args=dict(src='/tmp/test.txt', dest='/tmp/test_dest.txt')),
        connection=dict())

# Generated at 2022-06-13 09:56:56.252060
# Unit test for constructor of class ActionModule
def test_ActionModule():
  args = dict(
    _ansible_connection='connection',
    _ansible_module_name='module_name',
    _ansible_no_log=True,
    _ansible_keep_remote_files=True,
    _ansible_verbosity=5,
    _ansible_version='version',
    _ansible_debug=True,
    _ansible_diff=False,
    _ansible_check_mode=True,
    _ansible_remote_tmp='remote_tmp',
    _ansible_tmp='tmp',
    _ansible_socket_path='socket_path',
    _ansible_selinux_special_fs=['selinux_special_fs'],
    _ansible_shell_executable='shell_executable')

# Generated at 2022-06-13 09:57:15.424419
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None)
    assert am is not None

# Generated at 2022-06-13 09:57:25.598059
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os

    ##############################################################################################################
    # ActionModule.run() Failures - test all ways to fail in the path through run()
    ##############################################################################################################
    # Cause an exception to be raised when action plugin is invoked with an invalid option
    try:
        tmp = dict()
        task_vars = dict()
        my_action = ActionModule()
        result = my_action.run(tmp, task_vars)
    except AnsibleActionFail as e:
        if e.exception.args[0] != "src and dest are required":
            raise

    # Cause an exception to be raised when action plugin is invoked with an invalid option

# Generated at 2022-06-13 09:57:35.735061
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test method ActionModule.run
    """

    # -------------------------------------------------------------------------
    # TestCase setup
    # -------------------------------------------------------------------------
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 09:57:44.926727
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Connection manager
    connection_manager = ConnectionManager(loader=None, connections=None, passwords=dict())

    # HostManager
    host_manager = HostManager()

    # InventoryManager, VariableManager, DataLoader
    inventory_manager = InventoryManager(loader=None, sources=[])
    variable_manager = VariableManager(loader=None, inventory=inventory_manager)
    loader = DataLoader()
    variable_manager.set_vault_secrets

# Generated at 2022-06-13 09:57:46.601266
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # No args
    assert(Ternary(ActionModule().run()) == Ternary(1))


# Generated at 2022-06-13 09:57:47.516303
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)

# Generated at 2022-06-13 09:57:50.691428
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Test that constructor fails if no connection is provided
    """
    try:
        ActionModule()
        assert False, "ActionModule constructor should fail if no connection is provided"
    except:
        pass

# Generated at 2022-06-13 09:57:51.879186
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module.run()

# Generated at 2022-06-13 09:57:52.430792
# Unit test for constructor of class ActionModule
def test_ActionModule():
    d = {}
    ActionModule(d)

# Generated at 2022-06-13 09:57:53.996377
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # try creating an instance of ActionModule
    assert ActionModule(task=Task())



# Generated at 2022-06-13 09:58:36.165920
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import os.path
    import ansible.errors
    import ansible.module_utils.common.text.converters
    import ansible.module_utils.parsing.convert_bool
    import ansible.plugins.action
    import ansible.utils.display
    import ansible.utils.hashing
    import ansible.utils.path
    import tempfile
    import yaml

    # Setup
    tempdir = tempfile.mkdtemp()
    test_file = os.path.join(tempdir, 'test_file')
    with open(test_file, 'w') as f:
        f.write('test_file')
    m = 'ansible.plugins.action.ActionModule'
    f = 'run'
    m_args = dict()
    m_args['tmp'] = None

# Generated at 2022-06-13 09:58:44.996963
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(action=None, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(action, ActionModule)
    assert isinstance(getattr(action, '_task', None), dict)
    assert isinstance(getattr(action, '_connection', None), dict)
    assert isinstance(getattr(action, '_play_context', None), dict)
    assert isinstance(getattr(action, '_loader', None), dict)
    assert isinstance(getattr(action, '_templar', None), dict)
    assert isinstance(getattr(action, '_shared_loader_obj', None), dict)

# Generated at 2022-06-13 09:58:55.681134
# Unit test for constructor of class ActionModule
def test_ActionModule():
    yaml = YAML(typ='safe')
    yaml.default_flow_style = False
    yaml.width = 2**31
    hostvars = ModuleHelper.load_fixture('test_action_fetch/hostvars')
    host = ModuleHelper.load_fixture('test_action_fetch/host')
    hostvars = yaml.load(hostvars)
    host = yaml.load(host)
    module_utils = AnsibleModuleUtils()
    module_utils.basic._ANSIBLE_ARGS = ''
    tmpdir = tempfile.mkdtemp()
    module_utils.basic._ANSIBLE_INVENTORY = module_utils.inventory.Inventory(host_list=host).get_host_list()
    module_utils.basic._ANSIBLE_INVENTORY.host

# Generated at 2022-06-13 09:59:02.765426
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile
    try:
        os.mkdir("/tmp/test_ActionModule")
    except OSError:
        pass
    try:
        os.mkdir("/tmp/test_ActionModule/dest")
    except OSError:
        pass
    try:
        os.mkdir("/tmp/test_ActionModule/dest/1")
    except OSError:
        pass


# Generated at 2022-06-13 09:59:11.027497
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.utils.vars import load_extra_vars, load_options_vars
    from ansible.utils.display import Display
    from ansible.utils.path import path_dwim
    from ansible import context

# Generated at 2022-06-13 09:59:12.784032
# Unit test for constructor of class ActionModule
def test_ActionModule():
    args = dict()
    args['src'] = 'foo'

    f = ActionModule(args=args, action_plugins=None)
    assert f.module_args == ['src=foo']

# Generated at 2022-06-13 09:59:18.964672
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    unit test for method run of class ActionModule
    '''
    # set up parameters for unit test
    # define class for unit test
    class ConnectionMock():
        def __init__(self, become=False, check_mode=False):
            self._shell = ShellMock()
            self.become = become
            self.check_mode = check_mode

        def fetch_file(self, src, dest):
            fetch_file_list.append(dest)

    class ShellMock():
        def __init__(self):
            self.join_path = os.path.join
            self.tmpdir = '/tmp'

    class PlayContextMock():
        def __init__(self, become=False, check_mode=False):
            self.become = become
            self.check_mode = check_

# Generated at 2022-06-13 09:59:20.690929
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None, None, None)

    assert module

# Generated at 2022-06-13 09:59:34.465133
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.fetch import ActionModule
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play

    # Test code of class ActionModule
    # Test code of class ActionModule
    # Test code of class ActionModule
    # Test code of class ActionModule
    # Test code of class ActionModule
    # Test code of class ActionModule
    # Test code of class ActionModule
    # Test code of class ActionModule
    # Test code of class ActionModule
    # Test code of class ActionModule
    # Test code of class ActionModule
    # Test code of class ActionModule
    # Test code of class ActionModule
    class test_ShellModule(ActionModule):
        pass

    tm = test

# Generated at 2022-06-13 09:59:42.274855
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # setup
    import os
    import tempfile
    from ansible.module_utils.parsing.convert_bool import boolean
    tmp = tempfile.mkdtemp()
    path = os.path.join(tmp, "ansible_transfer_file_test")
    os.makedirs(path)
    real_path = os.path.join(path, "foo.txt")
    f = open(real_path, "w")
    f.write("bla")
    f.close()
    fake_connection = FakeConnection(tmp=tmp)
    fake_loader = FakeLoader()
    fake_display = FakeDisplay()
    fake_display.verbosity = 4

# Generated at 2022-06-13 10:01:11.058161
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # To ensure backward compatibility, ActionModule constructor should accept
    # a name parameter, it can be accept to be None.
    ActionModule(None, None)

    # To ensure backward compatibility, ActionModule constructor should accept
    # a task parameter, it can be accept to be None.
    ActionModule(None, None, None)

    # To ensure backward compatibility, ActionModule constructor should accept
    # a connection parameter, it can be accept to be None.
    ActionModule(None, None, None, None)

    # To ensure backward compatibility, ActionModule constructor should accept
    # a play_context parameter, it can be accept to be None.
    ActionModule(None, None, None, None, None)

    # To ensure backward compatibility, ActionModule constructor should accept
    # a loader parameter, it can be accept to be None.

# Generated at 2022-06-13 10:01:12.506935
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=dict())



# Generated at 2022-06-13 10:01:14.275965
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' Unit test for constructor of class ActionModule '''
    assert ActionModule


# Generated at 2022-06-13 10:01:22.225961
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import unittest

    try:
        from unittest import mock
    except ImportError:
        import mock
    import ansible.plugins.action.fetch as fetch

    real_utcnow = fetch.datetime.datetime.utcnow
    real_path_dwim = fetch.os.path.normpath
    real_open = fetch.builtins.open
    real_md5 = fetch.hashlib.md5
    real_cwd = os.getcwd

    mock_task = mock.MagicMock()
    mock_task._ds = dict()
    mock_task._ds.get = dict.get
    mock_task._ds.get.return_value = None
    mock_task.args = dict()
    mock_task.args.get = dict.get

# Generated at 2022-06-13 10:01:29.255919
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from msvcrt import get_osfhandle
    class Object(object):
        pass
    class Shell(object):
        called = False
        tmpdir = r'C:\Temp\ansible-tmp'
        def join_path(self, *args):
            return r'\\?\C:\Temp\ansible-tmp\file'
        def _unquote(self, src):
            return src
    class PlayContext:
        def __init__(self):
            self.remote_addr = '10.10.10.10'
            self.remote_user = 'root'

# Generated at 2022-06-13 10:01:40.651380
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.fetch import ActionModule
    from ansible.plugins.connection.local import Connection
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    connection = Connection(None)
    play_context = PlayContext(None, None)
    tqm = TaskQueueManager(inventory=InventoryManager(), variable_manager=VariableManager(), loader=None)

# Generated at 2022-06-13 10:01:41.845318
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None)
    assert isinstance(am, ActionModule)



# Generated at 2022-06-13 10:01:52.262386
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule()
    action.display = {
        'verbosity': 2,
        'verbose': True
    }
    action._task = {
        'args': {
            'src': '/etc/passwd',
            'dest': '/tmp/pwd'
        }
    }
    action._play_context = {
        'remote_addr': 'localhost'
    }
    action._connection = {
        '_shell': {
            'tmpdir': '/tmp',
            'join_path': lambda src: src
        },
        '_shell._unquote': lambda src: src,
        'fetch_file': lambda src, dest: True
    }
    action._loader = {
        'path_dwim': lambda dest: dest
    }

# Generated at 2022-06-13 10:01:53.910123
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), object)

# Generated at 2022-06-13 10:02:03.674596
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.text.converters import to_native as um
    from ansible.plugins.action.fetch import ActionModule

    fake_connection_class_instance = FakeConnection()
    fake_loader_class_instance = FakeLoader()
    fake_task_class_instance = FakeTask()
    fake_play_context_class_instance = FakePlayContext()

    test_action = ActionModule(fake_connection_class_instance, fake_loader_class_instance, fake_task_class_instance, fake_play_context_class_instance)

    test_action._remove_tmp_path = lambda x=None: 'remove_tmp_path_found_and_removed'

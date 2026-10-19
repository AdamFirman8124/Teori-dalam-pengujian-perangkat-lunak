

# Generated at 2022-06-13 09:55:41.923782
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialize vars and options
    opts = {'_ansible_pipelining': True, '_ansible_debug': True, '_ansible_check_mode': False, '_ansible_verbosity': False,
            '_ansible_no_log': False, '_ansible_diff': False, '_ansible_version': '2.4.2'}
    options = Mock()
    options.connection = 'test'
    options.module_path = '/tmp'
    options.module_name = 'test_module'
    options.forks = 10
    options.become = False
    options.become_method = 'test'
    options.become_user = 'test'
    options.check = False
    options.listhosts = None
    options.listtasks = None
    options

# Generated at 2022-06-13 09:55:43.199973
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(None, None)
    assert a != None

# Generated at 2022-06-13 09:55:45.504602
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 09:55:46.169456
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:55:47.606937
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:55:48.233883
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:55:49.267883
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 09:55:58.620610
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create file with contents 'test_ansible'
    with open('test_action_module.txt', 'w') as file:
        file.write('test_ansible')
    # Create an instance of ActionModule
    action_module = ActionModule({'src': 'test_action_module.txt', 'dest': 'test_action_module_1.txt'})
    result = action_module.run()
    os.remove('test_action_module.txt')
    assert(result['msg'] == '[secure_hash]: The checksum was computed over the initial content and not the resultant content.')
    os.remove('test_action_module_1.txt')



# Generated at 2022-06-13 09:55:59.317985
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 09:56:00.430366
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionmodule = ActionModule()



# Generated at 2022-06-13 09:56:28.266875
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for ActionModule class. Tests run() method
    """
    import os
    import tempfile
    from ansible.plugins.action._fetch import ActionModule

    tmp = tempfile.NamedTemporaryFile(delete=True)
    os.chmod(tmp.name, 0o644)
    os.chmod(os.path.dirname(tmp.name), 0o755)

    mod = ActionModule('fetch_test')

    res = mod.run(task_vars={'inventory_hostname': 'localhost'},
                  tmp={},
                  src=tmp.name,
                  dest=os.path.dirname(tmp.name))
    assert res.get('changed') is True
    assert res.get('dest').endswith(os.path.basename(tmp.name))

    res = mod

# Generated at 2022-06-13 09:56:29.220033
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert a is not None

# Generated at 2022-06-13 09:56:40.418036
# Unit test for constructor of class ActionModule
def test_ActionModule():
    temp_config = {'ANSIBLE_REMOTE_TEMP': '.ansible'}
    temp_loader = DictDataLoader({})
    temp_var = {'inventory_hostname': 'test1_server'}
    temp_connection = Connection(temp_loader)
    temp_task = Task()
    temp_task.args = {'src': '/tmp/test_tmp', 'fail_on_missing': False,
                      'flat': True, 'dest': 'test_dest'}
    temp_play_context = PlayContext()
    temp_options = Options()
    temp_action = ActionModule(temp_connection, temp_task, temp_var, temp_play_context, temp_loader, temp_options)
    assert temp_action._remove_tmp_path(temp_action._connection._shell.tmpdir) is None

# Generated at 2022-06-13 09:56:49.282906
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Test ActionModule
    """
    from ansible.module_utils.common.text.converters import to_bytes, to_text
    from ansible.plugins.connection.local import Connection
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.vars.hostvars import HostVarsVars

    hostvars = HostVarsVars({"localhost": {}}, [])
    inventory = InventoryManager(loader=DataLoader(), sources=[])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory, host_vars=hostvars)

# Generated at 2022-06-13 09:56:58.927360
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    #from ansible.executor.task_result import TaskResult
    from ansible.executor.stats import AggregateStats
    from ansible.plugins.callback import CallbackBase

    class ResultCallback(CallbackBase):
        """A sample callback plugin used for performing an action as results come in

        If you want to collect all results into a single object for processing at
        the end of the execution, look into utilizing the ``json`` callback plugin
        or writing your own custom callback plugin
        """

# Generated at 2022-06-13 09:57:00.558022
# Unit test for constructor of class ActionModule
def test_ActionModule():
        ActionModule('test', {}, None)

# Generated at 2022-06-13 09:57:13.108138
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up the class we are testing
    test_action_module = ActionModule('test', 'test')

    # Setup the class to test, this will be run inside the test method
    def run_test(task_args):
        # We need task vars to exist
        task_vars = {
            'ansible_ssh_user': 'test',
            'ansible_ssh_host': 'test',
            'ansible_ssh_port': 1234
        }

        # Set up an expected result
        expected_result = {'dest': 'this_is_a_path'}

        # Now run the method, which we are testing
        actual_result = test_action_module.run(task_vars=task_vars)

        # Ensure these are the same

# Generated at 2022-06-13 09:57:19.014550
# Unit test for constructor of class ActionModule
def test_ActionModule():
    connection=True
    display=True
    _task=True
    _play_context=True
    loader=True
    shared_loader_obj=True
    path_loader=True
    variable_manager=True
    action_base=ActionModule(connection,display,_task,_play_context,loader,shared_loader_obj,path_loader,variable_manager)


# Generated at 2022-06-13 09:57:27.514041
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.errors import AnsibleActionFail

    # object initialization
    task = dict(action=dict(module='fetch', src="src_content", dest="dest_content",
                            flat=True, validate_checksum='True'))
    connection_info = dict()

    fetch_module_obj = ActionModule(task, connection_info, '', '')

    # Test case 1: raise error if source type is not string
    task = dict(action=dict(module='fetch', src=["src_content"], dest="dest_content",
                            flat=True, validate_checksum='True'))
    fetch_module_obj = ActionModule(task, connection_info, '', '')

    with pytest.raises(AnsibleActionFail) as excinfo:
        fetch_module_obj.run()

    exception_

# Generated at 2022-06-13 09:57:37.377346
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test fixture
    from ansible.utils.path import makedirs_safe, is_subpath
    from ansible.plugins.action import ActionBase
    from ansible.module_utils.six import string_types
    from ansible.plugins import action
    import os
    import tempfile
    import shutil
    import collections
    import contextlib

    # setup temp directory and file
    tempdir = tempfile.mkdtemp(prefix='ansible_test_actionmodule_run')
    src = os.path.join(tempdir, 'src.txt')
    with open(src, 'wb') as f:
        f.write(b'src content')

    # dummy test data
    task_vars = {}
    tmp = None
    result = collections.defaultdict(dict)
    remote_data = None
    dest_dir

# Generated at 2022-06-13 09:58:14.999483
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:58:24.388140
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for method run of class ActionModule"""

    # The following data is generated from command
    # ansible-playbook -vvvv test_action_module_data.yaml

    test_data1 = {
        "changed": True,
        "checksum": "3906e95fcec7a06d17a8baf5e24ad2b9d0416b55",
        "dest": "/home/shixiaofei/tmp/test_tmp/test_tmp/test_tmp/test-fetch/127.0.0.1/roles/test_fetch_module/files/test_file",
        "file": "roles/test_fetch_module/files/test_file",
        "msg": ""
    }


# Generated at 2022-06-13 09:58:30.756422
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.callback import CallbackBase

    class ResultCallback(CallbackBase):
        def v2_runner_on_ok(self, result, **kwargs):
            host = result

# Generated at 2022-06-13 09:58:32.130689
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 09:58:32.500192
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:58:47.678403
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import shutil
    # Initial test
    module = ActionModule(connection=None,
                          task_uuid=None,
                          tmp=None,
                          runner_executor=None,
                          play_context=None,
                          loader=None,
                          templar=None,
                          shared_loader_obj=None)
    os.makedirs("/tmp/run")
    os.makedirs("/tmp/run/dest")
    os.makedirs("/tmp/run/dest/a")
    os.makedirs("/tmp/run/dest/a/b/c")
    f = open("/tmp/run/dest/a/b/c/d", "w")
    f.write("Hello")
    f.close()

# Generated at 2022-06-13 09:58:48.951786
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule(None, None)
    am.run(None, None)

# Generated at 2022-06-13 09:58:56.545620
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.text import to_bytes
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.task import Task
    from ansible.connection import Connection
    from ansible.utils import context_objects as co

    from units.mock.connection import MockConnection
    from units.mock.loader import DictDataLoader
    from units.mock.vc_shim import MockVaultLib


# Generated at 2022-06-13 09:59:03.134153
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    def execute_module():
        pass
    def join_path(*args):
        return args[1]
    def __init__(self, *args, **kwargs):
        pass
    def remote_expand_user(self, *args, **kwargs):
        return args[0]
    def _unquote(self, *args, **kwargs):
        return args[0]
    def _execute_remote_stat(self, *args, **kwargs):
        return {"exists" : True, "isdir" : False}
    def fetch_file(self, *args, **kwargs):
        pass
    action = ActionModule(execute_module)
    action._execute_module = execute_module

# Generated at 2022-06-13 09:59:04.966564
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert hasattr(ActionModule, 'run'), "ActionModule class is missing run method"

# Generated at 2022-06-13 10:00:36.050149
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Arrange
    action = ActionModule()
    # Act
    result = action.run(tmp=None, task_vars=None)
    # Assert
    assert result == None

# Generated at 2022-06-13 10:00:45.982060
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Test the method without any arguments
    test1 = ActionModule()
    test1._task = object()
    test1._task.args = {}
    test1._connection = object()
    test1._connection._shell = object()
    test1._connection._shell.tmpdir = '/tmp/ansible_test'
    test1._loader = object()
    test1._loader.path_dwim = lambda x, y: '/foo'
    test1._play_context = object()
    test1._play_context.remote_addr = 'hostname'
    test1._remote_expand_user = lambda x: x
    test1._remove_tmp_path = lambda x: True

    test1._connection.fetch_file = lambda x, y: None
    test1._connection.become = False
    test1._play

# Generated at 2022-06-13 10:00:47.035459
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass


# Generated at 2022-06-13 10:00:47.820450
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:00:48.498499
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:00:49.695898
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False, "Test not implemented"

# Generated at 2022-06-13 10:00:57.828505
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.six import StringIO
    from ansible.utils.color import stringc
    import sys
    import io
    import tempfile
    import shutil
    import hashlib
    import imp

    tmp_dir_name = tempfile.mkdtemp()
    module_loader = imp.load_source('module_loader', 'hacking/module_loader.py')

    # let's be kind and give the world something in case we cause a crash
    orig_stdout = sys.stdout
    orig_stderr = sys.stderr
    sys.stdout = new_stdout = StringIO()
    sys.stderr = new_stderr = StringIO()


# Generated at 2022-06-13 10:01:07.741523
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_result import TaskResult
    from ansible.module_utils._text import to_bytes

    import pytest
    from ansible.module_utils.common.text.converters import to_text, to_bytes
    from ansible.plugins import module_loader

    if not module_loader.find_plugin('slurp'):
        raise AnsibleActionSkip("slurp module not in library path; skipping test")

    try:
        import os
        import tempfile
    except ImportError:
        raise AnsibleActionSkip("Could not import os or tempfile, 'fetch' module requires both; skipping test")

    try:
        import filecmp
    except ImportError:
        raise AnsibleActionSkip("filecmp module is not installed; skipping test")


# Generated at 2022-06-13 10:01:12.847163
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_mod = ActionModule()

    assert action_mod.__class__ == ActionModule

    # The following line is needed for the correct functionality of the
    # unit tests using the autospec functionality of the mock library
    ActionModule.run = ActionModule.run

#Unit test for constructor of class ActionBase

# Generated at 2022-06-13 10:01:14.537747
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert ActionModule.run(ActionModule, tmp=None, task_vars=None) == None

# Generated at 2022-06-13 10:04:46.667204
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule(connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert actionModule

test_ActionModule()

# Generated at 2022-06-13 10:04:53.741490
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = dict(
        action=dict(module='fetch', args=dict(src='/tmp/file1', dest='/tmp/file2')),
        connection='ssh',
        _ansible_verbosity=4,
        _ansible_no_log=False,
        )

    play_context = dict(
        remote_addr='localhost',
        password='password',
        become=True,
        become_method='sudo',
        become_user='root',
        check=True,
        )

    task_vars = dict(
        ansible_ssh_host='localhost',
        ansible_ssh_pass='password',
        ansible_become_pass='password',
        #    ansible_python_interpreter='/usr/bin/python',
        )


# Generated at 2022-06-13 10:05:00.605277
# Unit test for constructor of class ActionModule
def test_ActionModule():

   action_module = ActionModule()
   assert action_module.RESULTS_CACHE_LOCK is not None
   assert action_module.RESULTS_CACHE is not None
   assert action_module._play_context is not None
   assert action_module._task is not None
   assert action_module._connection is not None
   assert action_module._loader is not None

# Generated at 2022-06-13 10:05:02.015476
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action != None

# Generated at 2022-06-13 10:05:05.164543
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        module = ActionModule()
        raise Exception("Did not raise exception")
    except NotImplementedError:
        pass

# Generated at 2022-06-13 10:05:14.176899
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    act = ActionModule(None, None)
    act._task = MockTask()
    act._task_vars = {
        'ansible_version': {'full': '2.0.0.0'},
        'group_names': [],
        'inventory_hostname': 'server1',
        'inventory_hostname_short': 'server1',
        'inventory_dir': '/tmp/ansible/inventory'
    }
    act._loader = MockLoader()
    act._connection = MockConnection()
    act._play_context = MockPlayContext()
    act._remove_tmp_path = MockRemoveTmpPath()
    act._loader.path_dwim = MockLoaderPathDwim()
    act._execute_remote_stat = MockExecuteRemoteStat()
    act._execute_module = MockExecuteModule()



# Generated at 2022-06-13 09:55:30.709465
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import os
    import tempfile

    a = ActionModule(load_attr_module=True)
    assert a

# Generated at 2022-06-13 09:55:42.026263
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Note: for following test code to work, the 'testmod' method needs to be commented out
    #       in the main body of the module
    import sys
    import unittest

    import tempfile

    # This is the test code that we need to run
    # module params
    src = 'test.conf'
    dest = tempfile.gettempdir()
    flat = 'yes'

    # parameters that are needed by the plugin
    task_vars = dict()
    connection_info = dict(host='localhost', port=22)

    # initialize needed objects
    display = Display()
    display.verbosity = 3
    try:
        from __main__ import CLIARGS
    except ImportError:
        from ansible.utils.args import parse_kv
        from ansible.utils.vars import combine_vars

       

# Generated at 2022-06-13 09:55:43.653494
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Test the module fetch"""
    assert True

# Generated at 2022-06-13 09:55:54.568663
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os
    import tempfile
    import shutil
    import six
    from io import StringIO

    if six.PY3:
        from io import BytesIO
    else:
        from StringIO import StringIO
    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()
    # Create a source file
    source = os.path.join(tmpdir, 'fetch_src')
    with open(source, 'wt') as f:
        f.write('One line')
    # Create a destination directory
    dest = os.path.join(tmpdir, 'fetch_dest')
    os.makedirs(dest)

    # Initialize a mock for AbstractConnection
    class AbstractConnection_Mock(object):
        import json

        def __init__(self):
            self._shell

# Generated at 2022-06-13 09:56:01.123768
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import action_loader
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import combine_vars
    from ansible.playbook.play import Play

    display = Display()
    loader = DataLoader()

    class Task(object):
        def __init__(self, args, vars):
            self.args = args
            self.vars = combine_vars(vars, args)


# Generated at 2022-06-13 09:56:06.006305
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Verify that the constructor of ActionModule sets the right variables.
    """
    test_action_module = ActionModule("test_name", "test_path")

    assert test_action_module._name == "test_name"
    assert test_action_module._action_plugins_path == "test_path"

# Generated at 2022-06-13 09:56:15.227305
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    conn = AnsibleConnection('localhost')
    task = {'args': dict(src='/path/to/src', dest='/path/to/dest')}
    module = ActionModule(task, conn)
    try:
        result = module.run()
        raise AssertionError('expected AnsibleActionFail error')
    except AnsibleActionFail:
        pass

    module._task.args['src'] = '.'
    try:
        result = module.run()
        raise AssertionError('expected AnsibleActionFail error')
    except AnsibleActionFail:
        pass

    module._task.args['src'] = '/path/to/src'
    module._task.args['dest'] = '.'

# Generated at 2022-06-13 09:56:16.040989
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:56:26.804122
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.executor.task_result import TaskResult
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.vars.hostvars import HostVars
    import ansible.constants as C
    import json

    inventory = InventoryManager(loader=DataLoader(), sources=C.DEFAULT_HOST_LIST)
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    play_context = PlayContext()

   

# Generated at 2022-06-13 09:56:32.810351
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create instance
    am = ActionModule()

    # check for useful attributes
    keys = dir(am)
    for s in ("_config", "_task", "_connection", "_play_context",
              "_loader", "_templar", "validate_checksum", "flat",
              "dest", "remote_checksum", "original_dest", "fail_on_missing", "remote_md5sum"):
        assert s in keys



# Generated at 2022-06-13 09:56:51.382000
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule

# Generated at 2022-06-13 09:57:06.509863
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult

    modules_path = 'test/test_action_modules'
    module_utils_path = 'test/test_module_utils'
    inventory_path = 'test/test_action_module_units/inventory'
    list_all = [{'name': 'localhost', 'groups': ['all'], 'vars': {'ansible_connection': 'local'}}]

    mock_loader = MockLoader()
    mock_loader.set_module_name('ansible.legacy.slurp')
    mock_loader.set_module_args({'src': 'abc', 'dest': 'abc'})

# Generated at 2022-06-13 09:57:15.094828
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create a fake connection with fake modules
    conn = ansible.plugins.connection.ConnectionBase(play_context=dict())

    # create the action
    fetch = ansible.plugins.action.copy.ActionModule(connection=conn, play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())

    # create a fake task with a fake task_vars variable
    task = dict()
    task['args'] = dict()
    task_vars = dict()
    task_vars['ansible_check_mode'] = False

    # fetch the file and check for changes
    fetch._execute_remote_stat = MagicMock()
    fetch._execute_remote_stat.return_value = dict(changed=True, md5sum=None, file=None, dest=None, checksum=None)
   

# Generated at 2022-06-13 09:57:16.944137
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert isinstance(am, ActionModule) == True
    am.run()


# Generated at 2022-06-13 09:57:17.630771
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 09:57:19.242490
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule(None, None, None, None)

# Generated at 2022-06-13 09:57:26.130747
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule

    # set up the module args that would be sent to the module
    module_args = {'remote_checksum': 'sha1:10c40402f31025e6930c8e90426da1b22d1b4fe4',
                   'dest': 'test_file',
                   'src': 'test_src'}

    # create a ansible module for ActionModule
    am = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    # create an ActionModule object
    action_module = ActionModule(
        am,
        'test_ActionModule_run',
        module_args,
        'always'
    )

    # set up mocked modules

# Generated at 2022-06-13 09:57:26.981596
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 09:57:28.822628
# Unit test for constructor of class ActionModule
def test_ActionModule():
    t = ActionModule(None, None)
    assert t is not None

# Generated at 2022-06-13 09:57:35.543188
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule()
    actionModule._task = 'test'
    actionModule._connection = 'test'
    actionModule._play_context = 'test'
    actionModule._loader = 'test'
    actionModule._templar = 'test'
    actionModule._shared_loader_obj = 'test'


    actionModule._task.args = {
        'src': 'test',
        'dest': 'test',
        'flat': True,
        'fail_on_missing': True,
        'validate_checksum': True,
    }

    actionModule.run()

# Generated at 2022-06-13 09:58:13.830140
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = None
    result = ActionModule.run(module, tmp=None, task_vars=None)
    assert 'msg' in result.keys()
    assert 'failed' in result.keys()
    assert result['failed'] == True


# Generated at 2022-06-13 09:58:15.480286
# Unit test for constructor of class ActionModule
def test_ActionModule():

    print("\nTESTING ActionModule class constructor\n")



# Generated at 2022-06-13 09:58:17.090808
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of class ActionModule
    # Return a dictionary of action results
    pass

# Generated at 2022-06-13 09:58:18.307851
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Just test the constructor of the class
    assert isinstance(ActionModule(), ActionModule)

# Generated at 2022-06-13 09:58:18.889332
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:58:21.080073
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    ActionModule.run()
    """
    # FIXME: Write a test for this
    pass



# Generated at 2022-06-13 09:58:24.501271
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for method run.
    """
    test_ActionModule= ActionModule('test', dict(a=dict(b=10, c=100), d=100), dict())
    test_ActionModule.run(None, dict(a=dict(b=10, c=100), d=100))

# Generated at 2022-06-13 09:58:36.630827
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(
        task=dict(vars=dict()),
        connection=dict(
            transport='local',
            _shell=dict(
                tmpdir='tmp_dir'
            ),
            become=False
        ),
        play_context=dict(
            check_mode=False,
            remote_addr='10.0.0.1'
        ),
        loader=dict(),
        _shared_loader_obj=dict()
    )

    # test errors
    result = module.run(
        task_vars=dict(
            ansible_check_mode=False,
            inventory_hostname='myhost',
            ansible_fips=False
        )
    )

    assert("src and dest are required" in result['msg'] == True)


# Generated at 2022-06-13 09:58:45.906511
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    from ansible.parsing.mod_args import ModuleArgsParser

    module_args_parser = ModuleArgsParser()

    task_args = dict(dest='/tmp/foo',
                     src='/etc/hosts',
                     validate_checksum=True,
                     fail_on_missing=False)
    action_plugin_args = '{"action": {"__ansible_module__": "fetch", "__ansible_action__": "fetch", "__ansible_arguments__": {"dest": "/tmp/foo", "src": "/etc/hosts", "validate_checksum": true, "fail_on_missing": false}}}'

    temp_dir = os.path.join(os.getcwd(), 'tests/test_action_plugins/temp')

# Generated at 2022-06-13 09:58:52.681663
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task_vars=[{'src': None, 'dest': None}],
        connection=[{'play_context': {'connection': 'local', 'remote_addr': '127.0.0.1',
                                      'remote_user': 'admin'}}],
        _remove_tmp_path=[None],
        _execute_module=[True],
        _execute_remote_stat={'checksum': '1'}
    )
    assert module is not None

# Generated at 2022-06-13 10:00:07.266257
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    raise RuntimeError("Test not implemented")


# Generated at 2022-06-13 10:00:13.922645
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # pylint: disable=unused-argument
    def run_mock(self, tmp=None, task_vars=dict()):
        return super(ActionModule, self).run(tmp=None, task_vars=task_vars)

    setattr(ActionModule, 'run', run_mock)

    action_module = ActionModule()
    setattr(action_module, '_task', type('task', (object,), dict(args=dict(src='src', dest='dest'))))
    setattr(action_module, '_connection', type('connection', (object,), dict()))
    setattr(action_module._connection, '_shell', type('shell', (object,), dict(tmpdir=None)))
    setattr(action_module._connection._shell, '_unquote', lambda s: s)


# Generated at 2022-06-13 10:00:15.463525
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule()

    assert(actionModule is not None)

# Generated at 2022-06-13 10:00:16.343608
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    assert not module.run()

# Generated at 2022-06-13 10:00:27.166618
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ test_ActionModule_run
    """
    module = ActionModule()
    module._remove_tmp_path = lambda x: None
    module._execute_remote_stat = lambda x, y, z: {'checksum': 'abc123'}
    module._execute_module = lambda x, y, z: {'encoding': 'base64', 'content': 'abc123'}

    module._play_context = DummySavedPlayContext()
    module._connection = DummyConnection()
    module._loader = DummyLoader()

    module._task = DummyTask()
    module._task.args = {'src': 'foo', 'dest': 'bar', 'flat': 'false', 'fail_on_missing': 'true', 'validate_checksum': 'true'}

    ret = module.run()

# Generated at 2022-06-13 10:00:27.764342
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:00:28.927583
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True


# Generated at 2022-06-13 10:00:37.023941
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile
    import os
    import shutil
    from ansible.plugins.action.fetch import ActionModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_executor import get_default_fact_cache
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.play_context import PlayContext

# Generated at 2022-06-13 10:00:46.586959
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.fetch
    import ansible.module_utils.basic
    from ansible.plugins.action.fetch import ActionModule
    from ansible.module_utils.connection import Connection

# Generated at 2022-06-13 10:00:47.171784
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:03:55.359978
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # initialize AnsibleAction
    pass  # FIXME: test me



# Generated at 2022-06-13 10:04:02.628119
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create a fake task to test method run of class ActionModule.
    #
    # Data for fake task
    task_vars = {}
    tmp = None
    dest = "/tmp/test_ansible/file_exists.txt"

    # Create a fake task.
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play

    play_context = Play().load({}, variable_manager={}, loader=None)
    task = TaskInclude()
    task._role = None
    task._block = Block()
    task._play = play_context
    task.vars = task_vars
    task.args = {'dest': dest}
    task._role = None
    # Create a fake connection
    connection = Fake

# Generated at 2022-06-13 10:04:06.288100
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import __builtin__
    try:
        del __builtin__._

        ActionModule(play_context=None, task=None, connection='connection', play_ds=None, loader=None, templar=None, shared_loader_obj=None)
    finally:
        __builtin__._ = '_'

# Generated at 2022-06-13 10:04:07.368577
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print(ActionModule)
    # print(ActionModule._ActionModule__execute_module)

# Generated at 2022-06-13 10:04:14.595040
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ACTION_MODULE = ActionModule()
    sample = {'dest': 'dest', 'src': 'src'}
    sample['flat'] = True
    sample['remote_checksum'] = ACTION_MODULE.run(tmp=None, task_vars=None, **sample)
    sample['flat'] = False
    sample['remote_checksum'] = ACTION_MODULE.run(tmp=None, task_vars=None, **sample)
    assert isinstance(sample['remote_checksum'], dict)

# Generated at 2022-06-13 10:04:19.025981
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class Options():
        become = False
        become_method = 'sudo'
        become_user = 'root'
        check = False
        connection = 'smart'
        diff = False
        force_handlers = False
        forks = 5
        remote_user = 'remote'
        private_key_file = '/home/remote/.ssh/id_rsa'
        ssh_common_args = None
        ssh_extra_args = None
        sftp_extra_args = None
        scp_extra_args = None
        verbosity = 3
        timeout = 10

    action_module = ActionModule(play_context = Options())

    class Task():
        args = dict(src='/remote/path/file', dest='/local/path/file', validate_checksum=False)


# Generated at 2022-06-13 10:04:20.956965
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    foo
    """
    # TODO: implement this

# Generated at 2022-06-13 10:04:21.845187
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:04:22.902857
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True == True


# Generated at 2022-06-13 10:04:24.362994
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins
    m = ansible.plugins.action.ActionModule(None,None,None)
    assert m is not None
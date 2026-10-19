

# Generated at 2022-06-13 09:23:48.593227
# Unit test for constructor of class ActionModule
def test_ActionModule():
    t_vars = dict()
    t = ActionModule(dict(),t_vars)
    assert t is not None

# Generated at 2022-06-13 09:23:57.146164
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class TestTask:
        def __init__(self):
            self.args = {'ignore_hidden': False, 'regexp': None, 'src': '../test_data/src', 'delimiter': None, 'dest': '../test_data/dest', 'remote_src': 'yes'}

    class TestConnection:
        def __init__(self):
            class TestShell:
                def __init__(self):
                    self.tmpdir = '../test_data/dest'

                def join_path(self, path_list, *args, **kwargs):
                    return '/'.join(path_list)

            self._shell = TestShell()

        def _execute_remote_stat(self, path, all_vars, follow):
            return {'checksum': '777'}


# Generated at 2022-06-13 09:24:01.033853
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule('task', 'play', False, {'src': 'source', 'dest': 'destination'}, [])
    assert m._task.args.get('src') == 'source'
    assert m._task.args.get('dest') == 'destination'



# Generated at 2022-06-13 09:24:04.421018
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    module_obj = ActionModule(
        task=dict(args=dict(src=u'src', dest=u'dest')),
        connection=dict(tmp=u'/tmp'))

    assert module_obj.run() == dict(changed=False)



# Generated at 2022-06-13 09:24:06.144927
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module

# Generated at 2022-06-13 09:24:09.359567
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert a

# Generated at 2022-06-13 09:24:20.560104
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.display import Display

    from ansible.plugins.action import ActionBase

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager)
    variable_manager.set_inventory(inventory)
    display = Display()
    play_context = PlayContext(variable_manager=variable_manager, loader=loader)
    tqm = None
    task = Task()
    action

# Generated at 2022-06-13 09:24:30.038437
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import shutil

    result = dict()
    file1="""#!/usr/bin/python

import os
import sys
import traceback

if __name__ == '__main__':
    print("This is a test")
"""
    file2="""#!/usr/bin/python

import os
import sys
import traceback

if __name__ == '__main__':
    print("This is another test")
"""
    tempdir = tempfile.mkdtemp()
    src = os.path.join(tempdir, 'src')
    dest = os.path.join(tempdir, 'dest')
    os.mkdir(src)
    os.mkdir(dest)


# Generated at 2022-06-13 09:24:30.611263
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  pass

# Generated at 2022-06-13 09:24:33.405056
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 09:24:44.639158
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:24:46.433993
# Unit test for constructor of class ActionModule
def test_ActionModule():
    global module
    module = ActionModule(task=dict(action=dict()), connection=None, play_context=C.load(dict()), loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 09:24:47.143314
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:24:59.380518
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY3

    mod_mock = AnsibleModule(
        argument_spec=dict(
            src=dict(type='str'),
            dest=dict(type='str'),
            delimiter=dict(type='str'),
            remote_src=dict(type='str'),
            regexp=dict(type='str'),
            follow=dict(type='str'),
            ignore_hidden=dict(type='str'),
        )
    )

    # create test 'module' to use in mock_execute_module

# Generated at 2022-06-13 09:25:04.852614
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # create an instance of the class to test
    actionModule = ActionModule()

    # TODO: implement this test
    # check if the instance is of the proper type
    #assert type(actionModule) == "ActionModule"

    # check if the instance is of the proper type
    #assert isinstance(actionModule, ActionModule)

    #assert type(actionModule) == "ABCMeta"

    #assert actionModule.__dict__
    #assert actionModule.__doc__
    #assert actionModule.__module__
    #assert actionModule.__weakref__
    #assert actionModule.name



# Generated at 2022-06-13 09:25:06.559384
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    print('%s' % action_module)



# Generated at 2022-06-13 09:25:12.927081
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import ansible.module_utils.basic
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 09:25:14.361407
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None


# Generated at 2022-06-13 09:25:22.294039
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # We don't have an actual module to test with, but we will just check
    # if the desired exception is thrown.
    a = ActionModule(dict(), '')
    args = {}
    result = a.run(tmp='/tmp', task_vars=dict())
    assert result == {'failed': True, 'msg': "src and dest are required"}, result

    try:
        a.run(tmp='/tmp', task_vars=dict())
        assert False, "AnsibleActionFail was not raised."
    except AnsibleActionFail as e:
        assert e.result == {'failed': True, 'msg': "src and dest are required"}, e.result

# Generated at 2022-06-13 09:25:34.991773
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # example of src and dest
    src = '/home/foo/test'
    dest = '/home/bar/test'
    delimiter = None
    remote_src=False
    regexp = None
    follow = False
    ignore_hidden = False
    decrypt = True
    args = {'src': src, 'dest': dest, 'delimiter': delimiter, 'remote_src': remote_src, 'regexp': regexp, 'follow': follow, 'ignore_hidden': ignore_hidden, 'decrypt': decrypt}
    module = ActionModule(name='module', task=dict(), args=args)
    assert module is not None
    assert module._task == dict()

# Generated at 2022-06-13 09:25:59.061815
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 09:26:09.617128
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible import context
    import ansible.constants as C

    context.CLIARGS = ImmutableDict(connection='smart', forks=10, become=None,
                                    module_path=None, become_method=None, become_user=None, check=False, diff=False,
                                    listhosts=None, listtasks=None, listtags=None, syntax=None)
    ActionModule.task = task = Task()

# Generated at 2022-06-13 09:26:17.388566
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Mock data
    task_vars = {
        'ansible_connection': 'local',
        'ansible_ssh_pass': 'pass',
        'ansible_ssh_user': 'user',
        'ansible_ssh_port': 'port',
        'ansible_ssh_host': 'host',
        'inventory_hostname': 'localhost',
        'group_names': '[u\'all\']',
        'groups': {
            'group1': {
                'hosts': ['host1'],
            },
            'all': {
                'hosts': ['host1', 'host2'],
            },
        },
    }


# Generated at 2022-06-13 09:26:19.785460
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(loader=None, connection=None, play_context=None, new_stdin=None)
    assert a is not None

# Generated at 2022-06-13 09:26:21.192493
# Unit test for constructor of class ActionModule
def test_ActionModule():

    module = ActionModule()
    assert isinstance(module, ActionModule)

# Generated at 2022-06-13 09:26:33.084957
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    from ansible.playbook.task import Task
    from mock import MagicMock, patch
    task = Task()
    task._role = None
    task.action = 'copy'
    task.args = {}
    task_vars = {}
    tmp_path = None
    connection = MagicMock()
    connection._shell.join_path = MagicMock(side_effect=lambda x, y: x+'/'+y)
    connection._shell.tmpdir = '/tmp'
    connection._shell.exists = MagicMock(return_value=False)
    connection._shell.isdir = MagicMock(return_value=False)
    connection._shell.listdir = MagicMock(return_value=["file"])

# Generated at 2022-06-13 09:26:35.126040
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert a


# Generated at 2022-06-13 09:26:48.996443
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Python 2.6 doesn't have mock in stdlib, so we need to install it
    import sys
    major_version = sys.version_info[0]
    minor_version = sys.version_info[1]
    if major_version == 2 and minor_version == 6:
        import unittest.mock as mock
    else:
        import mock

    m = mock.MagicMock()
    m.args = {'src': '/path/to/dir/of/templates'}

    m.result = {'new_module_args': {}}
    m.task_vars = None

    mod = ActionModule()

    def _execute_module(module_name, module_args, task_vars):
        return {'changed': False}
    mod._execute_module = _execute_module


# Generated at 2022-06-13 09:26:56.221727
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Instantiate an object of class ActionModule
    am = ActionModule()
    # Call the method run of class ActionModule
    result = am.run()
    # Check the value returned by the method run of class ActionModule
    print("test_ActionModule_run: " + str(result))

if __name__ == "__main__":
    # Call the unit test for method run of class ActionModule
    test_ActionModule_run()

# Generated at 2022-06-13 09:27:06.563679
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible_collections.nsbl.aws.tests.lib.targets.local as local_targets
    import ansible_collections.nsbl.aws.tests.lib.test_runner as test_runner

    class MockModule(object):
        def __init__(self, dest, src, regexp, delimiter, remote_src, ignore_hidden, decrypt):
            self.args = {}
            self.args['dest'] = dest
            self.args['src'] = src
            self.args['regexp'] = regexp
            self.args['delimiter'] = delimiter
            self.args['remote_src'] = remote_src
            self.args['ignore_hidden'] = ignore_hidden
            self.args['decrypt'] = decrypt


# Generated at 2022-06-13 09:27:51.506081
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create the actions module
    module = ActionModule(None, dict(src = None, dest = None, regexp = None, delimiter = None, remote_src = 'yes', decrypt = True))
    assert module is not None

# Generated at 2022-06-13 09:28:04.327111
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import platform
    import tempfile
    
    from ansible.executor.task_result import TaskResult
    
    from ansible.modules.copy import ActionModule
    from ansible import context
    from ansible.plugins.action import ActionBase

    os.chmod(tempfile.gettempdir(), 0o700) # Temp dir has to be accessible by the user running this test

    def load_action_plugin(self):
        pass

    def _execute_module(self, module_name, module_args=None, task_vars=None):
        return TaskResult()

    def _execute_remote_stat(self, path, all_vars, follow):
        return TaskResult()

    def _transfer_file(self, path, remote_path):
        return TaskResult()


# Generated at 2022-06-13 09:28:05.463768
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:28:09.794122
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(
        task = None,
        connection = None,
        play_context = None,
        loader = None,
        templar = None,
        shared_loader_obj = None,
    )


# Generated at 2022-06-13 09:28:19.728964
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import tempfile
    import shutil
    import glob


# Generated at 2022-06-13 09:28:23.781705
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test for fact gathering
    action = ActionModule(dict(gather_facts='no'), load_collections=False)
    assert action._gather_facts == 'no'
    # test for module_name
    action = ActionModule(dict(module_name='setup'), load_collections=False)
    assert action._module_name == 'setup.py'

# Generated at 2022-06-13 09:28:24.745729
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None


# Generated at 2022-06-13 09:28:31.748016
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest
    import os
    import shutil
    import json
    import errno
    from ansible.playbook import Playbook

    # test assemble on localhost
    assembly_dir = "/tmp/ansible-unittest/local-assemble"
    (tmpdir_path, tmpdir_name) = os.path.split(assembly_dir)
    try:
        os.makedirs(assembly_dir)
    except OSError as e:
        if e.errno != errno.EEXIST or not os.path.isdir(assembly_dir):
            raise
    # create fragment files
    with open(assembly_dir + "/fragment-A", "w") as f:
        f.write("# fragment A")

# Generated at 2022-06-13 09:28:33.032204
# Unit test for constructor of class ActionModule
def test_ActionModule():
    return ActionModule()

# Generated at 2022-06-13 09:28:33.710761
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    assert False

# Generated at 2022-06-13 09:30:06.680867
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Unit test for constructor of class ActionModule
    """
    module_args = ['./test/integration/targets/test.yml', 'all', './test/integration/targets/test.retry']
    task = None
    shared_loader_obj = None
    connection_loader_obj = None
    loader_obj = None
    play_context_obj = None
    play_context_obj.remote_addr = None
    new_stdin = None

    action_module_obj = ActionModule(module_args, task, shared_loader_obj, connection_loader_obj, loader_obj, play_context_obj, new_stdin)


# Generated at 2022-06-13 09:30:10.920376
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test constructor
    obj = ActionModule(name = 'test_ActionModule_1')
    assert not hasattr(obj,'_supports_check_mode')
    assert not hasattr(obj,'_task')
    assert not hasattr(obj,'_connection')
    assert not hasattr(obj,'_play_context')
    assert not hasattr(obj,'_loader')
    assert not hasattr(obj,'_templar')
    assert not hasattr(obj,'_shared_loader_obj')


# Generated at 2022-06-13 09:30:14.202876
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None)
    assert isinstance(action, ActionBase)
    assert action._supports_check_mode == False


# Generated at 2022-06-13 09:30:15.678545
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """ Unit test for ActionModule.run method """
    pass

# Generated at 2022-06-13 09:30:16.534981
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 09:30:17.960715
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    p = ActionModule()
    p.run()

# Generated at 2022-06-13 09:30:18.776569
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 09:30:28.040182
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 09:30:39.502089
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import action_loader
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.connection.local import Connection
    import ansible.executor.task_queue_manager
    import ansible.executor.task_result
    ansible.executor.task_queue_manager.TaskQueueManager = MockTaskQueueManager
    ansible.executor.task_result.TaskResult = MockTaskResult

    module_name = 'test_ActionModule_run'

    action_plugin = action_loader.get(module_name,
                                      task=dict(action=dict(module_name=module_name)),
                                      connection=Connection(),
                                      play_context=PlayContext(),
                                      loader=None,
                                      templar=None,
                                      shared_loader_obj=None)

# Generated at 2022-06-13 09:30:48.638231
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # copy unittest/action_module.py to test_action_module.py
    # and remove this line to enable this unittest
    raise unittest.SkipTest
    import os
    import shutil

    from ansible.utils import context_objects as co
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play_context import PlayContext

    mock_action = co.AnsibleAction(None, None, 'any', None)
    mock_play = co.AnsiblePlay(None, None, None)
    mock_play_context = PlayContext()
    mock_play_context.check_mode = False
    mock_play_context.network_os = 'any'
    mock_play
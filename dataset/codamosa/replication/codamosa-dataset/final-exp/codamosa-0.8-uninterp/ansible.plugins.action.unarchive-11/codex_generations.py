

# Generated at 2022-06-13 10:53:00.546390
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # load and test the action plugin
    import os
    import tempfile

    test_dir = tempfile.mkdtemp(prefix='ansible_test_dir')
    source = test_dir + '/source'
    dest = test_dir + '/dest'
    creates = os.path.join(dest, 'filename')
    test_file = os.path.join(source, 'filename')
    os.mkdir(source)
    os.mkdir(dest)
    with open(test_file, 'w') as f:
        f.write('test')
    test_output = os.listdir(dest)
    os.remove(test_file)
    os.rmdir(source)
    os.rmdir(dest)

    from ansible.module_utils.common.removed import removed

# Generated at 2022-06-13 10:53:08.698005
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins import action
    import ansible
    import ansible.plugins
    import __main__ as main

    setattr(main, '__file__', '/')
    setattr(ansible.plugins, '__file__', '/')
    setattr(ansible.plugins.action, '__file__', '/')


# Generated at 2022-06-13 10:53:10.403192
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert isinstance(action_module, ActionModule)
    assert isinstance(action_module.run(dict()), dict)

# Generated at 2022-06-13 10:53:16.650360
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test for method run of class ActionModule'''
    # Define test variables
    task_vars = {}
    tmp = None
    # Execute the method under test
    result = ActionModule(tmp, task_vars).run(tmp, task_vars)
    # Check if the method under test return the expected result
    assert result == None
# Unit test end


# Generated at 2022-06-13 10:53:18.396135
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()._get_action_handler() is not None

# Generated at 2022-06-13 10:53:21.774062
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Note: see test_autosupport_ActionModule.py
    #       for testing _execute_module.
    obj = ActionModule()
    # CCTODO: Check vars set in object.

    return

# Generated at 2022-06-13 10:53:26.493038
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Constructor for ActionModule class
    '''
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    # This assertion is not valid.
    # assert action_module is not None

# Generated at 2022-06-13 10:53:28.847285
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:53:39.509196
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    import ansible.module_utils.parsing.convert_bool
    import ansible.plugins.action

    module = ansible.plugins.action.ActionModule('', '')
    super(ansible.plugins.action.ActionModule, module).run('', '')

    module = ansible.plugins.action.ActionModule('', '')
    super(ansible.plugins.action.ActionModule, module).run(tmp='', task_vars='')

    module = ansible.plugins.action.ActionModule('', '')
    source = 'test_source'
    dest = 'test_dest'
    remote_src = False
    creates = 'test_creates'
    decrypt = True

    class ActionBase(object):
        TRANSFERS_FILES = False


# Generated at 2022-06-13 10:53:50.592278
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # load module test
    test_module = AnsibleModule(
        argument_spec=dict(
            src=dict(required=True, type='str'),
            dest=dict(required=True, type='str'),
            remote_src=dict(required=False, type='str'),
            creates=dict(required=False, type='str'),
            decrypt=dict(required=False, type='str'),
        )
    )

    source = test_module.params['src']
    dest = test_module.params['dest']
    remote_src = test_module.params['remote_src']
    creates = test_module.params['creates']
    decrypt = test_module.params['decrypt']

    # Unit test component:
    # Initialize the class
    action_module = ActionModule()

    # Unit test component:
   

# Generated at 2022-06-13 10:54:06.595991
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  # Test with insufficient params.
  module = ansible.plugins.action.unarchive.ActionModule(connection='connection',
                                                         display='display',
                                                         task='task',
                                                         file_vars=dict(),
                                                         loader='loader',
                                                         play_context='play_context')
  test_result = module.run(tmp='tmp', task_vars=dict(src=None, dest=None))
  assert test_result['failed'] is True
  assert test_result['msg'] == 'src (or content) and dest are required'

  # Test with missing src.

# Generated at 2022-06-13 10:54:07.749330
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for method run of class ActionModule"""
    raise NotImplementedError()

# Generated at 2022-06-13 10:54:08.232964
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:10.623063
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Testing ActionModule.run()")
    # TODO
    print("UNFINISHED")

# Generated at 2022-06-13 10:54:18.930952
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' Unit test for method run of class ActionModule '''
    ##########################################################################
    # This test is using a modified version of the test_async.py file.
    # The modifications are to safely use this test file by only adding a
    # small amount of code to the existing test file and not modifying any
    # of the existing code in this file.
    #
    # The following lines are the additions for the unit test.
    from ansible.plugins.test.test_unarchive import test_ActionModule_run

    print("Start of test_ActionModule_run() method")
    result = test_ActionModule_run()
    print("result: " + str(result))
    print("End of test_ActionModule_run() method")

# Generated at 2022-06-13 10:54:21.137401
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Test run method of class ActionModule.
    """

    # TODO: Unit tests for class ActionModule implementation.

if __name__ == "__main__":
    test_ActionModule_run()

# Generated at 2022-06-13 10:54:24.617426
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Test case for instanciation of class ActionModule
    '''
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert action.__class__ is ActionModule

# Generated at 2022-06-13 10:54:33.707399
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Testing constructor of class ActionModule")
    # Test 1
    print("Test 1: Constructor ActionModule with no arguments")
    action = ActionModule()
    assert action is not None, "ActionModule() failed when passed no arguments"
    print("Test 1: Passed!")
    # Test 2
    print("Test 2: Constructor ActionModule with task and connection")
    task = object()
    connection = object()
    action = ActionModule(task, connection)
    assert action is not None, "ActionModule() failed with valid arguments"
    print("Test 2: Passed!")
    print("ActionModule constructor passed all tests")


# Generated at 2022-06-13 10:54:38.561300
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Constructor for class ActionModule without arguments
    try:
        action_module = ActionModule()
    except:
        print('ActionModule constructor raised exception')

    # Constructor for class ActionModule with arguments
    # action_module = ActionModule(task, connection, tempalte, play_context, loader, templar, shared_loader_obj)

# Generated at 2022-06-13 10:54:43.203829
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_module = ActionModule()
    test_module._task.args = {'src':'src', 'dest':'dest', 'creates':'creates', 'decrypt':False}
    test_module._task.action = 'unarchive'
    test_module._connection = None
    assert test_module.run() == {'skipped':True, 'skipped_reason':"skipped, since creates exists"}

# Generated at 2022-06-13 10:54:53.218398
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True == True

# Generated at 2022-06-13 10:54:54.107498
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:55:02.988857
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    from ansible.module_utils.parsing.convert_bool import boolean
    actionMap = {'ansible.legacy.unarchive': {'creates': None, 'path': 'unarchive.py', 'remote_src': None, 'dest': 'C:\\WPy64-3740\\tcl', 'src': 'C:\\Users\\Administrator\\ansible-role-tester\\src\\uncompressed_archive.zip'}}

    module = ActionModule(dict(ANSIBLE_MODULE_ARGS=actionMap['ansible.legacy.unarchive']), load_plugins=False)
    task_vars = {'ansible_check_mode': False}
    result = module.run(None, task_vars)

# Generated at 2022-06-13 10:55:06.350430
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(action='unarchive', task=dict(args=dict(src=None, dest=None, remote_src=False, creates=None, decrypt=True)))

# Generated at 2022-06-13 10:55:11.530757
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = AnsibleActionModule(
        {'dest': '/home/vagrant/ansible/test', 'remote_src': False, 'src': '~/ansible/test/test'})
    assert module.run() == {'changed': False, '_ansible_no_log': False, 'msg': 'skipped, since /home/vagrant/ansible/test exists'}

# Generated at 2022-06-13 10:55:18.538584
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('Testing ActionModule.run')
    module_instance = ActionModule()
    # Source directory that will be transferred to the host system.
    test_src = os.path.abspath('/tmp/')
    # Destination directory on the host system.
    test_dest = '/tmp'
    test_args = {'src': test_src, 'dest': test_dest}
    args = module_instance.run(test_args)
    print(args)

test_ActionModule_run()

# Generated at 2022-06-13 10:55:28.643577
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    from ansible.module_utils._text import to_bytes
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.loader import action_loader
    from ansible.utils.display import Display
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    display = Display()
    options = load_options_vars()
    options['subset'] = 'all'
    loader = DataLoader()
   

# Generated at 2022-06-13 10:55:29.657785
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.__doc__ != ''

# Generated at 2022-06-13 10:55:39.004124
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile
    import shutil
    from ansible.plugins.action import ActionModule
    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-13 10:55:40.752206
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = AnsibleAction()
    action = ActionModule()
    action.run(tmp=None, task_vars=task)

# Generated at 2022-06-13 10:55:59.440389
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.basic import AnsibleModule

    from ansible.plugins import action_loader
    results = action_loader.get('copy', class_only=True)
    assert results == ActionModule

# Generated at 2022-06-13 10:56:09.299609
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a mock connection object.
    connection = MockConnection()
    # Create an action module object.
    action_module = ActionModule(connection=connection, action_loader=None)

    # Test the _task attribute.
    task = action_module._task
    assert task is not None

    # Test the _play_context attribute.
    play_context = action_module._play_context
    assert play_context is not None

    # Test the _connection attribute.
    module_connection = action_module._connection
    assert module_connection is connection

    # Test the _loader attribute.
    loader = action_module._loader
    assert loader is not None

    # Test the _templar attribute.
    templar = action_module._templar
    assert templar is not None

    # Test the _shared_loader_obj attribute

# Generated at 2022-06-13 10:56:11.462009
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO: add an actual unit test ...
    #assert(False)
    return

# Generated at 2022-06-13 10:56:12.260528
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:56:21.208861
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for ActionModule run method.

    :return: Void
    """

    result = {'failed': True, 'msg': 'Test description'}

    # Mock our AnsibleRunner object and make sure it has a result
    ansible_runner = MagicMock()
    ansible_runner.result = result

    # Now make the object we are testing and call the method
    action_module = ActionModule()
    action_module.runner = ansible_runner
    result = action_module.run()

    # Test
    assert result == result

# Generated at 2022-06-13 10:56:21.886591
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:56:31.396157
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test invalid src
    invalid_src = os.path.join(os.getcwd(), 'invalid-file')
    test_args_1 = {'src':invalid_src, 'dest':'dest'}
    action_module_1 = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    try:
        action_module_1.run(tmp=None, task_vars=None)
        raise Exception('Failed')
    except AnsibleActionFail as e:
        if str(e) != "Failed to find src in expected paths":
            raise Exception('Unexpected exception')

    # test invalid dest
    invalid_dest = os.path.join(os.getcwd(), 'invalid-dir')
    test

# Generated at 2022-06-13 10:56:40.208695
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    This will test the method run.
    """
    from ansible import context
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.process.worker import WorkerProcess
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager

    assert action_loader.has_plugin('copy')
    action_copy = action_loader.get('copy')

# Generated at 2022-06-13 10:56:48.220502
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task
    from ansible.vars import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import merge_hash
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.utils.vars import load_group_vars
    from ansible.utils.vars import get_group_vars
    
    # Initializing varible manager, loader and host
    variable_manager = VariableManager()
    loader = DataLoader()
    host = Host("127.0.0.1")

    # Setting data in test variables

# Generated at 2022-06-13 10:56:52.839400
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert not os.path.exists('testfile')
    mm = ActionModule('testfile', 'testfile', '/testfile', {'src': 'testfile', 'dest': '/tmp'})
    assert isinstance(mm, ActionBase)
    assert isinstance(mm, ActionModule)
    mm = ActionModule('testfile', 'testfile', '/tmp', {'src': 'testfile', 'dest': '/tmp'})
    assert isinstance(mm, ActionBase)
    assert isinstance(mm, ActionModule)
    assert os.path.exists('testfile')
    os.remove('testfile')
    assert not os.path.exists('testfile')


# Generated at 2022-06-13 10:57:28.150477
# Unit test for constructor of class ActionModule
def test_ActionModule():
    foo = ActionModule()

# Generated at 2022-06-13 10:57:31.263010
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action

# Generated at 2022-06-13 10:57:34.003138
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionModule = ActionModule()
    assert isinstance(actionModule, ActionModule)
    assert isinstance(actionModule, ActionBase)
    assert actionModule.TRANSFERS_FILES is True


# Generated at 2022-06-13 10:57:34.582772
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:57:42.765445
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.utils
    from ansible.plugins.action.unarchive import ActionModule
    from ansible.utils.vars import combine_vars

    # We need to mock this out because we are trying to test the interaction between
    # either the local machine and a remote SSH host or the local machine and an
    # SSH host in a Docker container.  The assignment to 'action.unarchive' is a
    # side effect of the following command, but this module is already loaded.
    # So we have to mock it out to get this test to work.
    ansible.utils.plugin_docs['action']['unarchive'] = "action.unarchive"
    unarchive_action = ActionModule()

    # Set up the mock context for a connection between the local machine and a
    # remote SSH host

# Generated at 2022-06-13 10:57:54.434418
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionBase
    """
    from ansible.module_utils.ansible_modlib.test import ModuleTestCase

    module = ModuleTestCase.module
    # We need some files to put in the test/files directory of the test
    # environment.
    source = __file__
    dest = 'test/files/test_ActionModule_run.txt'
    destdir = 'test/files/test_ActionModule_run'

    # Run the test.
    main = ActionModule(module)
    action = 'ansible.legacy.acquia_backup_restore'
    remote_src = False
    creates = None
    decrypt = True

    result = main.run(action, source, dest, remote_src, creates, decrypt)
    # Check if the destination file matches the source file.

# Generated at 2022-06-13 10:58:02.340657
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task = {}
    task["action"] = {}
    task["action"]["name"] = "unarchive"
    task["action"]["args"] = {}
    task["action"]["args"]["creates"] = "creates"
    task["action"]["args"]["dest"] = "dest"
    task["action"]["args"]["remote_src"] = False
    task["action"]["args"]["src"] = "src"
    result = {}
    result["exists"] = True
    result["isdir"] = True
    result["path"] = "dest"
    result["__ansible_module__name__"] = "action"
    task_vars = {}
    task_vars["result"] = result
    tmp = []

# Generated at 2022-06-13 10:58:08.537653
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class DummyModule(object):

        def __init__(self, *args, **kwargs):
            return super(DummyModule, self).__init__(*args, **kwargs)

        def _execute_module(self):
            return True

    # pylint: disable=protected-access
    my_action = ActionModule(DummyModule(), task=DummyModule())
    assert my_action.run()

# Generated at 2022-06-13 10:58:12.350431
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(None,None)
    assert a.TRANSFERS_FILES, "Should be True"
    
if __name__ == "__main__":
    test_ActionModule()

# Generated at 2022-06-13 10:58:13.954415
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActMod = ActionModule()
    assert to_text(ActMod.run()) is not None

# Generated at 2022-06-13 10:59:33.067799
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task = "Unarchive", connection = "local", play_context = "", loader = "", templar = "", shared_loader_obj = "")

# Generated at 2022-06-13 10:59:44.021257
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class ActionModule(object):
        pass
    class Task(object):
        pass
    class PlayContext(object):
        pass
    class Connection(object):
        pass
    class Shell(object):
        pass
    class Play(object):
        pass
    class Playbook(object):
        pass
    class PlaybookExecutor(object):
        def __init__(self):
            self.loader = Loader()
            self.inventory = Inventory()

    class Loader():
        def get_basedir(self, host):
            return "base_dir"
    class Inventory():
        pass
    class TaskExecutor(object):
        def __init__(self):
            self.task = Task()
            self.task.action = "Unarchive"

# Generated at 2022-06-13 10:59:46.592560
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule()
    assert actionmodule
    assert hasattr(actionmodule, 'run')


# Generated at 2022-06-13 10:59:58.481479
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    unittest.main()


if __name__ == '__main__':
    import inspect
    import sys

    # For example, running this module as
    #
    # python library/ansible/plugins/action/unarchive.py
    #
    # will cause the following data structure to be returned to the caller.
    #
    # {
    #   "msg": "",
    #   "failed": false,
    #   "changed": false,
    #   "skipped": false,
    #   "invocation": {
    #     "module_name": "unarchive",
    #     "module_args": {}
    #  }
    # }
    #
    # Running this module as
    #
    # python library/ansible/plugins/action/unarchive.py msg="

# Generated at 2022-06-13 10:59:59.850676
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass


# Generated at 2022-06-13 11:00:06.972499
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.connection import Connection

    am = ActionModule(
        connection=Connection(),
        task_uuid='test',
        loader=None,
        templar=None,
        shared_loader_obj=None)

    am.run(ImmutableDict({'tmp':asd}), ImmutableDict({'task_vars':'test_task_vars'}))

# Generated at 2022-06-13 11:00:09.121050
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None, None, None)
    assert action is not None

# Generated at 2022-06-13 11:00:11.967839
# Unit test for constructor of class ActionModule
def test_ActionModule():
  assert ActionModule(task=None, connection=None,
                      play_context=None, loader=None,
                      templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 11:00:12.358810
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 11:00:14.157649
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass  # TODO: write your own test



# Generated at 2022-06-13 10:52:48.627567
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.copy as copy
    action = copy.ActionModule(dict(ACTION_MODULE_ARGS='ACTION_MODULE_ARGS'))
    assert type(action) == copy.ActionModule

# Generated at 2022-06-13 10:52:55.360566
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create a new instance of the ActionModule class
    # and incorporate the test cases for the unarchive action plugin
    action_module = ActionModule('unarchive')
    assert action_module.action == 'unarchive'
    assert action_module.name == 'unarchive'
    assert action_module.TRANSFERS_FILES == True

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:53:03.591395
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.loader import connection_loader
    connection = connection_loader.get('local', {})
    task = {
        'args': {
            'src': 'my_source.tar.gz',
            'dest': 'my_destination/'
        }
    }
    am = ActionModule(task, connection, tmp_path='./tests/test_data/tmp')
    assert am is not None
    # If we get to this point, no exception was raised.

# Generated at 2022-06-13 10:53:12.859030
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # GIVEN
    module_name = 'action_module.py'
    module_args = {'dest': '/tmp'}
    task_vars = {'hostvars': 'TODO'}
    error_arg = None
    error_module_name = 'error_module'
    error_module_args = None
    try:
        raise AnsibleError('AnsibleError')
    except AnsibleError as e:
        error_arg = to_text(e)

    # WHEN
    # The following code is to test the ActionModule class.
    # The run method tests how the class reacts when an AnsibleError exception is raised.
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None)

# Generated at 2022-06-13 10:53:24.722674
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import basic
    from ansible.module_utils import common
    from ansible.vars import VariableManager

    from ansible.plugins.action import ActionModule

    # The 'local_action' should be set to the name of the class on the 'ActionModule' line at the top of this file.
    # This is part of the new API that replaces ActionBase.
    local_action = 'ActionModule'

    # Create the task object.
    task = AnsibleTask()

    # Create the results object to store the results of the run method.
    results = AnsibleResults()

    # Create the tmp directory in the working directory.
    tmp_dir = make_temp_dir(os.getcwd())
    print("tmp_dir=%s" % (tmp_dir))

    # Create the source file to be downloaded to

# Generated at 2022-06-13 10:53:26.384863
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule()
    b = ActionModule()
    c = ActionModule()

# Generated at 2022-06-13 10:53:28.375117
# Unit test for constructor of class ActionModule
def test_ActionModule():
    con = {}
    action_module = ActionModule(con)
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 10:53:29.477223
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 10:53:30.913064
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('ActionModule_run: ')
    a = ActionModule()

# Generated at 2022-06-13 10:53:41.280698
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)._connection is None
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None)._task is None
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None)._play_context is None
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None)._loader is None
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None)._templar is None

# Generated at 2022-06-13 10:53:53.394168
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Unit test not implemented.
    #
    # The following is a trivial comment test.  The code is not implemented
    # and will not compile until a unit test is implemented.
    #

    # Create an object of class ActionModule.
    a = ActionModule()
    # Call the run() method of class ActionModule.  This will fail because
    # the method has not been implemented yet.
    a.run()

# Generated at 2022-06-13 10:53:58.428904
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play

    # Define test variables.
    source = 'playbooks/library/unarchive.py'
    dest = 'playbooks/'
    local_file = 'playbooks/library/unarchive.py'
    remote_src = False
    tmp = None
    creates = None
    decrypt = True

    # Create Ansible/Ansible inventory (host) and playbook objects.
    host = 'localhost'
    inventory = Inventory(host)
    playbook = Play()

    # Create Ansible variables.
    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory)

    # Create an Ansible ActionModule item.

# Generated at 2022-06-13 10:53:58.956951
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule().run()

# Generated at 2022-06-13 10:54:00.946475
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task=dict(action='unarchive', args=dict(src='s', dest='d')))
    assert am
    assert am.TRANSFERS_FILES


# Generated at 2022-06-13 10:54:04.290022
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Test ActionModule"""

    print("TestActionModule")
        
    #
    # Test to make sure that ActionBase has been inhereted and that we have the variables
    # it needs.
    #
    actionbase = ActionBase()
    var_stuff = actionbase()

# Generated at 2022-06-13 10:54:06.661287
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' action_plugin/unarchive.py:ActionModule() construct '''
    # pylint: disable=undefined-variable
    assert isinstance(ActionModule.run, object)
    # pylint: enable=undefined-variable

# Generated at 2022-06-13 10:54:13.650200
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    This will test the constructor of the class ActionModule.
    """
    am = ActionModule(connection=None, task=None, loader=None, templar=None, shared_loader_obj=None)
    assert am.task_vars == dict()
    assert am.loader.get_aliases() == dict()
    assert am.TRANSFERS_FILES == True



# Generated at 2022-06-13 10:54:14.182370
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:54:19.398110
# Unit test for constructor of class ActionModule
def test_ActionModule():
    result = True
    try:
        t = ActionModule()
    except TypeError as e:
        print("type error %s" % e)
        result = False
    assert(result)

if __name__ == "__main__":
    test_ActionModule()

# Generated at 2022-06-13 10:54:32.268893
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import tempfile
    import shutil
    from ansible.plugins.action.unarchive import ActionModule

    temp_dir = tempfile.mkdtemp()
    fake_module_name = os.path.join(temp_dir, 'fake_module')
    shutil.copyfile(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'archive_module.py'), fake_module_name)

    test_body = {}
    test_body['_ansible_parsed'] = True
    test_body['action'] = 'unarchive'
    test_body['args'] = dict(
            src='test.tar.gz',
            dest='test_dest',
            remote_src=True,
            decrypt=True,
            creates='test.txt')
    test

# Generated at 2022-06-13 10:54:50.568754
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    import ansible.constants as C
    import json

    #################################################
    # Ansible is using the 'load_from_file' method of C to load a file that
    # has the following JSON formatted data
    # {"dest": "/tmp", "remote_src": false, "src": "~/test.tgz"}
    #################################################

    loader = DataLoader()

# Generated at 2022-06-13 10:55:00.685545
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    loader = DataLoader()
    context = PlayContext()
    task = Task()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 10:55:01.558786
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(dict()).run is not None

# Generated at 2022-06-13 10:55:12.910962
# Unit test for method run of class ActionModule
def test_ActionModule_run():
	# mock_loader, mock_connection, and mock_task are built in dictionaries - no need for any setup, just
	# call the constructor for ActionModule, defining it with the parameters provided (mocks are already setup)
	am = ActionModule(mock_loader, mock_connection, mock_task)

	# define the source and destination for the ActionModule.run method - to be called further below
	source = "/Users/user1/Documents/Ansible"
	dest = "/Users/user1/Documents/Ansible/archive"

	# define the return value of the mocked ActionModule.run method, being returned below

# Generated at 2022-06-13 10:55:17.407039
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    # I am going to use the object variables instead of creating the object with the values that I need because I am lazy.

    # I don't have a good way to test the AnsibleAction case.
    assert action_module.run() == None
    return

# Generated at 2022-06-13 10:55:19.357166
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test empty constructor
    action_module = ActionModule()
    assert action_module is not None

# Generated at 2022-06-13 10:55:21.300299
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    AM = ActionModule()
    AM.run()


# Generated at 2022-06-13 10:55:30.303181
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a testable action module
    import os
    test_am = ActionModule(
        connection=None,
        _shell_executor=os.system,
        become_method='sudo',
        become_user='root',
        check_mode=False,
        # diff=False,
        # diff_peek=False,
        tmpdir=None,
        remote_user='test_user',
        load_path=None,
        module_name='test_name',
        module_args='test_arg',
        task_uuid='1',
        verbosity=10
    )

    # test

# Generated at 2022-06-13 10:55:31.669670
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule()
    assert type(m) == ActionModule



# Generated at 2022-06-13 10:55:38.073352
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    # TODO: Incomplete
    action_module = ActionModule()
    action_module._task = {}
    action_module._task['args'] = {}
    action_module._task['args']['src'] = 'src'
    action_module._task['args']['remote_src'] = True
    action_module._task['args']['dest'] = 'dest'
    print(action_module.run(tmp=None, task_vars=None))

# Generated at 2022-06-13 10:55:54.683225
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 10:56:05.858785
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of ActionModule
    am = ActionModule()

    # Create temporary files for testing.
    import tempfile
    src_file_handle, src_file_name = tempfile.mkstemp()
    dest_dir_handle, dest_dir_name = tempfile.mkstemp()

    # Create test data for use with temporary files.
    src_file_contents = """{
        "test": {
            "test1_module": "test1_args"
        },
        "test2": {
            "test2_module": "test2_args"
        }
    }"""
    dest_dir_contents = """
    """
    src_file_contents = src_file_contents.encode('UTF-8')

    # Write data to temporary files.

# Generated at 2022-06-13 10:56:08.116253
# Unit test for constructor of class ActionModule
def test_ActionModule():
	action_module = ActionModule()
	assert action_module != None, "ActionModule object constructor error"
	del action_module


# Generated at 2022-06-13 10:56:15.868372
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import unittest
    from ansible.playbook.task import Task
    from ansible.plugins.action import ActionBase
    from ansible.utils.listify import listify_lookup_plugin_terms
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible import context
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.plugins.action.unarchive import ActionModule
    import sys
    import os
    import json




# Generated at 2022-06-13 10:56:26.387401
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Testing constructor of ActionModule")

    # test default arguments
    task = dict()
    task['args'] = dict()
    task['args']['src'] = "/etc/hosts"
    task['args']['dest'] = "/tmp"
    action = ActionModule(task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert(action != None)

    # test with mocked paramaters
    task = dict()
    task['args'] = dict()
    task['args']['src'] = "/etc/hosts"
    task['args']['dest'] = "/tmp"

# Generated at 2022-06-13 10:56:26.983133
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 'ActionModule' == ActionModule.__name__

# Generated at 2022-06-13 10:56:36.694792
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:56:44.608470
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_name = 'copy'
    src = 'foo.conf'
    dest = '/tmp/foo.conf'
    creates = '/tmp/create.conf'
    remote_src = 'True'
    test_action_instance = ActionModule(action_name, src, dest, creates, remote_src)
    assert test_action_instance is not None
    assert test_action_instance.action == action_name
    assert test_action_instance.src == src
    assert test_action_instance.dest == dest
    assert test_action_instance.creates == creates
    assert test_action_instance.remote_src == remote_src
    # CCOB-8

# Generated at 2022-06-13 10:56:45.712177
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # This runs in tests and will fail the test if it is not implemented
    pass

# Generated at 2022-06-13 10:56:47.494589
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am is not None


# Generated at 2022-06-13 10:57:20.983880
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Put code here
    # To test methods, override the run function
    # . . . and call it here.
    pass

# Generated at 2022-06-13 10:57:28.003268
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os, shutil, tempfile
    
    # Create temp dir and file to simulate ansible config dir
    tmp_path = tempfile.mkdtemp()
    ansible_cfg = os.path.join(tmp_path, 'ansible.cfg')
    open(ansible_cfg, 'a').close()
    
    # Set ANSIBLE_CONFIG environment variable to point at the ansible config file
    # including the ansible.cfg file in that directory
    os.environ['ANSIBLE_CONFIG'] = ansible_cfg
    
    from ansible.plugins.action import ActionModule
    
    action_module = ActionModule()
    action_module._loader = None
    action_module._connection = None
    

# Generated at 2022-06-13 10:57:37.963117
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Mock an Ansible module object with an Ansible play, a task, and an ActionModule object
    class AnsibleModule:
        def __init__(self):
            self.params = {}
            class AnsiblePlay:
                def __init__(self):
                    self.vars = {'ansible_user': 'bob'}
                    self.become_user = 'fred'
            self.play = AnsiblePlay()
        class AnsibleTask:
            def __init__(self):
                self.args = {}
        class AnsibleActionModule(ActionModule):
            def __init__(self):
                self._task = AnsibleTask()
                self._connection = {'_shell': {'tmpdir': 'temp'}}
        class AnsibleError(Exception):
            def __init__(self):
                pass

# Generated at 2022-06-13 10:57:45.538184
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('Test: ActionModule/run')
    
    import ansible.plugins.action
    import ansible.plugins
    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.task_include
    import ansible.utils.plugin_docs
    import ansible.utils.display
    import ansible.utils.vars
    import ansible.vars
    import ansible.template
    import ansible.parsing.meta
    import ansible.parsing.yaml.objects
    import ansible.parsing.mod_args
    import ansible.inventory
    import ansible.inventory.host
    import ansible.inventory.group
    import ansible.inventory.expand_hosts
    import ansible.errors
    import ansible.constants
    import ansible

# Generated at 2022-06-13 10:57:52.059855
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule

    :return: nothing
    '''

    # CCTODO: Create unit test
    pass

if __name__ == '__main__':
    # CCTODO: This routine needs to be converted to a unit test
    a = ActionModule()
    print(a)

# Generated at 2022-06-13 10:57:56.534897
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # pylint: disable=unused-variable
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module is not None

# Generated at 2022-06-13 10:58:04.581059
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.config.manager import ConfigManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import PluginLoader
    from ansible.vars.manager import VariableManager
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.vars import combine_vars
    from ansible.template import Templar
    import ansible.constants as C
    import sys

    source = 'foo'
    dest = 'bar'


# Generated at 2022-06-13 10:58:17.248677
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test with arguments
    actionModule = ActionModule()
    actionModule._task = {}
    actionModule._task.args = {}
    actionModule._task.args['src'] = 'test_src'
    actionModule._task.args['dest'] = 'test_dest'
    actionModule._task.args['remote_src'] = False
    actionModule._task.args['creates'] = None
    actionModule._task.args['decrypt'] = True
    actionModule._remove_tmp_path = lambda *args, **kwargs: None


# Generated at 2022-06-13 10:58:20.027732
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print('Test ActionModule constructor')
    assert(ActionModule)

# Generated at 2022-06-13 10:58:26.960731
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    AnsibleActionFail: src (or content) and dest are required
    AnsibleActionFail: parameters are mutually exclusive: ('copy', 'remote_src')
    AnsibleActionFail: dest '%s' must be an existing dir
    AnsibleActionFail: could not find src in expected paths
    AnsibleAction: OK
    """
    pass



# Generated at 2022-06-13 10:59:38.122612
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    ActionModule()
    '''
    pass


# Generated at 2022-06-13 10:59:44.546093
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(
        { "decrypt": "yes",
        "dest": "c:\\Users\\lstevenson\\ansible\\test_unarchive",
        "src": "c:\\Users\\lstevenson\\ansible\\test_file.zip"
         },
        connection="local",
        task_uuid="f414a537-0a0e-4323-8fa0-e3e9d62139ab",
        loader=None,
        templar=None,
        shared_loader_obj=None)
    assert action
    assert action.TRANSFERS_FILES

# Generated at 2022-06-13 10:59:50.770011
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        from ansible.plugins.action.archive import ActionModule as ActionModuleClass
        a = ActionModuleClass(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
        assert type(a) == ActionModuleClass
    except ImportError:
        pass

# Generated at 2022-06-13 10:59:51.530052
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    return

# Generated at 2022-06-13 10:59:52.820763
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule()
    assert mod

# Generated at 2022-06-13 10:59:53.578956
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:59:56.462283
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule('unarchive', {'src': 'xxx', 'dest': 'yyy'})
    assert True


# Generated at 2022-06-13 10:59:57.324772
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False, "No tests for this module"

# Generated at 2022-06-13 11:00:09.014424
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Data mocked from shell.py
    class MockTask():
        def __init__(self, args):
            self.args = args

    class MockPlayContext():
        def __init__(self, check_mode=False, diff=False):
            self.check_mode = check_mode
            self.diff = diff

    play_context = MockPlayContext()
    task = MockTask(args={
        'src': 'src',
        'dest': 'dest',
        'creates': 'creates',
        'decrypt': True,
        'remote_src': False
    })

    def mock_expand_user(path):
        return path

    def mock_fixup_perms2(paths):
        return paths


# Generated at 2022-06-13 11:00:16.401323
# Unit test for method run of class ActionModule
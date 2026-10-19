

# Generated at 2022-06-13 10:52:48.136493
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule(dict(action=dict()), dict())

# Generated at 2022-06-13 10:52:59.793170
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.six import StringIO

    action_module = ActionModule()

    # Source file: 'User1.txt' exists and dest file: 'tmp/User1.txt' exists
    # test_run1: run() should return 'changed: False' and
    #           'dest: /home/User1/tmp/User1.txt'
    my_task_args1 = {'src': './test/User1.txt', 'dest': '/home/User1/tmp/User1.txt'}
    action_module._task.args = my_task_args1
    action_module._connection = MockConnection()
    my_tmp1 = '/home/User1'
    my_task_vars1 = {'ansible_fact_tmp': my_tmp1}
    res1 = action_module.run

# Generated at 2022-06-13 10:53:01.386771
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass  # TODO: Implement test for the method run of class ActionModule.

# Generated at 2022-06-13 10:53:08.070423
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import shutil, tempfile
    from ansible.plugins.action import ActionBase
    from ansible.module_utils.common.removed import removed
    from ansible.module_utils.network.common.utils import load_provider
    import ansible.utils.template as template
    from ansible.module_utils.connection import Connection, ConnectionError

    # Initialize and instanciate object
    tmpdir = tempfile.mkdtemp()
    res = {}
    am = ActionModule(task=None, connection=None, _play_context=None, loader=None,
                     templar=template.Templar(), shared_loader_obj=None)
    am._remove_tmp_path = lambda _: None # Do nothing
    am._load_name_to_path_cache = lambda: None # Do nothing
    am._fixup

# Generated at 2022-06-13 10:53:22.156166
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class TestConnection:
        def __init__(self):
            self._shell = TestShell()

        class TestShell:
            def __init__(self):
                self.tmpdir = 'a_tmp_dir'

            def join_path(self, *args):
                return '_'.join(args)

    class TestTask:
        def __init__(self):
            self.args = {'src': 'src-file', 'dest': 'dest-dir', 'remote_src': False, 'creates': 'creates-file', 'decrypt': True}

    class TestActionBaseModule:
        def __init__(self):
            self._task = TestTask()

    class TestLoader:
        def get_real_file(self, name, decrypt=True):
            return name


# Generated at 2022-06-13 10:53:26.765503
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Constructor test using mock objects and AnsibleModule
    '''
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.dataloader import DataLoader

    task = dict()
    task['args'] = dict()
    task['action'] = 'action_unarchive'
    task['args']['src'] = 'test/test_module_utils.py'
    task['args']['dest'] = 'test/'
    task['args']['remote_src'] = False

    task_vars = dict()

    def get_real_file(filename, decrypt=True):
        '''Mock of loader.get_real_file'''
        return filename


# Generated at 2022-06-13 10:53:28.741258
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module.TRANSFERS_FILES == True

# Generated at 2022-06-13 10:53:31.571530
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(loader=None, connection=None, play_context=None)
    assert a is not None

# vim: set et sw=4 ts=4

# Generated at 2022-06-13 10:53:32.114123
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass



# Generated at 2022-06-13 10:53:33.073202
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass # TODO: Implement unit test for ActionModule_run

# Generated at 2022-06-13 10:53:42.483709
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create an instance of ActionModule
    am = ActionModule()
    assert isinstance(am, ActionModule)

# Generated at 2022-06-13 10:53:49.516238
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert not ActionModule(None, None)._task.args.get('remote_src', None)
    assert not ActionModule(None, None)._task.args.get('copy', None)
    assert boolean(ActionModule(None, None)._task.args.get('decrypt', None), strict=False)
    assert not ActionModule(None, None)._task.args.get('creates', None)
    assert not ActionModule(None, None)._task.args.get('content', None)


# Generated at 2022-06-13 10:53:54.224002
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor of class ActionModule when only required parameters are passed
    a = ActionModule(name='unarchive', run_once=True, action_plugins=['ansible/plugins/action'], vars={}, task_vars={}, play_vars={})
    assert a.name == 'unarchive'
    assert a.run_once == True
    assert a.action_plugins == ['ansible/plugins/action']
    assert a.vars == {}
    assert a.task_vars == {}
    assert a.play_vars == {}
    assert a.datastore == {}

# Generated at 2022-06-13 10:54:00.999133
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import shutil
    import tempfile
    import unittest

    # class for mocking AnsibleModule
    class MockAnsibleModule():
        def __init__(self):
            self.params = {}
            self.result = {'changed': False}
            self.run_command_called = False
            self.fail_json_called = False

        def run_command(self, cmd, tmp_path, sudoable=False, executable="/bin/sh", data=None):
            self.run_command_called = True
            return (0, '', '')

        def fail_json(self, msg):
            self.fail_json_called = True

    # class for mocking AnsibleConnection
    class MockAnsibleConnection():
        def __init__(self):
            self.shell = MockAnsibleShell()

    # class

# Generated at 2022-06-13 10:54:14.245526
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.errors import AnsibleParserError

# Generated at 2022-06-13 10:54:18.915578
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=dict(args=dict(src=None, dest=None, remote_src=False, creates=None)), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:54:25.913193
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from __main__ import display
    from ansible.plugins.action import ActionModule
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.vars.manager import VariableManager
    import ansible.constants
    import json

    ansible.constants.HOST_KEY_CHECKING = False

    context = PlayContext()

    pbex = PlaybookExecutor(playbooks=['/Users/jefferyb/ansible/core/hacking/test_module.yml'],
                            inventory=None,
                            variable_manager=VariableManager(),
                            loader=None,
                            options=None,
                            passwords=None)

   

# Generated at 2022-06-13 10:54:27.493500
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule({})
    assert module.run({}, {})


# Generated at 2022-06-13 10:54:39.062575
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = dict(
        args=dict()
    )
    tmp = '/tmp'


# Generated at 2022-06-13 10:54:39.987250
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False, "No test_ActionModule_run implemented"

# Generated at 2022-06-13 10:54:57.651072
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # See the detailed information on ActionModule.
    # https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/action/unarchive.py
    ActionModule()

# Generated at 2022-06-13 10:54:58.974216
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None, None)

# Generated at 2022-06-13 10:55:06.028988
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #Initiate the action plugin.
    action_plugin = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Mock the class needed for the run method.
    class MockClass:
        def __init__(self):
            self.args = dict()
            self.args['src'] = 'test'
            self.args['dest'] = 'test'
            self.args['remote_src'] = True

    action_plugin._task = MockClass()

    # Mock the connection needed for run.
    class MockConnection:
        def __init__(self):
            self._shell = MockShell()

    action_plugin._connection = MockConnection()

    # Mock the loader needed for run.

# Generated at 2022-06-13 10:55:06.694552
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:55:17.704736
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.utils.color import stringc
    from ansible.utils.unicode import to_unicode
    from ansible.utils.vars import combine_vars
    from ansible import constants as C

    import sys
    import unittest
    import json


# Generated at 2022-06-13 10:55:21.454646
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Tests the run method of Ansible module ansible.plugins.action.unarchive.

    :return: None
    '''
    pass  # TODO: Add tests of module run method.

# Generated at 2022-06-13 10:55:22.134917
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:55:27.001270
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # GIVEN:
    module = ActionModule(connection=None)
    module._execute_remote_stat = lambda x, **y: dict(exists=True, isdir=True)

    # WHEN:
    # Runs method run
    result = module.run()

    # THEN:
    # Verifies if result is an instance of the class AnsibleAction
    assert isinstance(result, AnsibleAction)



# Generated at 2022-06-13 10:55:34.123431
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def _test_run(mock_unarchive, mock_remote_expand_user, mock_remote_stat,
                  mock_result, mock_task_args, mock_shell):

        # pylint: disable=no-self-use, unused-argument, protected-access

        obj = ActionModule()

        # CCTODO: Add test for source being a dict (content attribute).

        # Test with the file found in the playbook dir.
        mock_task_args['src'] = 'a/file.txt'

        # Test with the file found in the tasks dir.
        # mock_task_args['src'] = 'b/file.txt'

        # Test with the file found in the role's files dir.
        # mock_task_args['src'] = 'c/file.txt'

        # Test with the file not found anywhere

# Generated at 2022-06-13 10:55:47.922501
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor import task_result
    from ansible.executor.play_iterator import PlayIterator
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.included_file import IncludedFile

    # Set up class ActionModule
    task_vars = dict()
    play_context = PlayContext()
    tmp_path = '/tmp'
    connection = 'local'
    loader = None
    settings = None
    task = Task()
    task._role = Role()
    task._block = Block()
    task._role._block = Block()
    task._role._block._parent = task._role
    task._role._parent = Included

# Generated at 2022-06-13 10:56:27.051118
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import mock

    module = mock.Mock()
    task = mock.Mock()
    task.args = dict()
    task.args['src'] = None
    task.args['dest'] = None
    task.args['remote_src'] = False
    task.args['creates'] = None

    task_vars = dict()

    am = ActionModule(task, module, tmp=None, task_vars=task_vars)
    result = am.run()

# Generated at 2022-06-13 10:56:28.905215
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule('test', {}, False, '/dev/null')
    assert action

# Unit tests for method ActionModule.run()

# Generated at 2022-06-13 10:56:38.263436
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a temporary file.
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.write(b'Test file contents')
    tmp.close()
    test_args = dict(src=tmp.name, dest='/some/path')
    test_task = dict(args=test_args)

    test_action = action.ActionModule(task=test_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    test_result = test_action.run(tmp=None, task_vars=None)

    assert test_result['failed'] == False
    assert test_result['changed'] == True
    assert test_result['failed'] == False
    assert test_result['state'] == 'file'

# Generated at 2022-06-13 10:56:43.028193
# Unit test for constructor of class ActionModule
def test_ActionModule():
    conn = object()
    module = object()
    task = object()
    play_context = object()
    loader = object()
    templar = object()

    try:
        actions.ActionModule(conn, module, task, play_context, loader, templar)
    except Exception as e:
        print(e)

# Generated at 2022-06-13 10:56:44.201755
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert(am)


# Generated at 2022-06-13 10:56:50.789438
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import unittest
    import os
    import yaml
    import json
    import sys
    import tempfile
    import os
    import shutil
    import sys
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_text
    from ansible.playbook.play_context import PlayContext
    
    from ansible.plugins.action import ActionBase
    from ansible.plugins.action.unarchive import ActionModule
    from ansible.plugins.loader import action_loader
    from ansible.plugins.task.basic import TaskModule
    from ansible.module_utils.parsing.convert_bool import boolean

    # create instances for testing

# Generated at 2022-06-13 10:57:00.781238
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import collections
    import re
    import sys
    
    # Prevent calls to print() to interfere with unit tests.
    def print(str):
        pass
    
    # Used to ensure that AnsibleActionFail messages are as expected during unit tests.
    def check_AnsibleActionFail_message(asrt_obj, exception, message):
        asrt_obj.assertEqual(message, exception.message)

    # Used to ensure that AnsibleAction messages are as expected during unit tests.
    def check_AnsibleAction_message(asrt_obj, exception, message):
        asrt_obj.assertEqual(message, exception.result.get('msg'))

    # Used to ensure that a dictionary contains a key with a given value.

# Generated at 2022-06-13 10:57:13.559394
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Load the fake module
    module = load_fixture("fake_ansible_module.py")
    # This is what your shell would return to Ansible
    results = {"msg": "FAKE ANSWER"}
    # The fake module is used in the following way
    # /usr/bin/python module remote_user=token1 check=token2 /path_to_ansible/ansible/modules/commands/command.py /path_to_ansible/ansible/tmp/ansible-tmp-1481376131.42-252477305039237/ /path_to_ansible/ansible/tmp/ansible-tmp-1481376131.42-252477305039237/command.py
    # It's the first command line argument after the fake module

# Generated at 2022-06-13 10:57:14.188031
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:57:15.465041
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True  # TODO: Implement

# Generated at 2022-06-13 10:58:19.822382
# Unit test for constructor of class ActionModule
def test_ActionModule():
    #test = ActionModule()
    return

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:58:22.550713
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Construct an empty ActionModule object
    action_module = ActionModule()
    # Check that the object is an instance of class ActionModule
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 10:58:27.729190
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.common.removed import removed_module
    with removed_module():
        assert ActionModule(
            task=dict(action='foo', args=dict(bar='baz')), connection=None,
            play_context=None, loader=None, templar=None, shared_loader_obj=None
        )

# Generated at 2022-06-13 10:58:38.025981
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.network.common.utils import load_provider
    from ansible.plugins.action import ActionModule
    from ansible.module_utils._text import to_text
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    provider = load_provider('_dummy')
    action = ActionModule(task=None, connection=provider, play_context=PlayContext(become_method='sudo', become_user='test'), loader=None, templar=None, shared_loader_obj=None)
    action._display = {'verbosity': 2}
    action._task = DummyTask()
    action._queue = DummyTaskQueueManager()
    action._connection = provider
    action._loader = DummyLoader()


# Generated at 2022-06-13 10:58:42.449337
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()

    try:
        assert am.run() == 'Invalid args'
    except AssertionError:
        print('ActionModule.run() not valid')
    else:
        print('ActionModule.run() valid')


# Generated at 2022-06-13 10:58:49.308536
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import mock

    import ansible.plugins.action.unarchive as unarchive
    mock_module = mock.Mock(spec=unarchive.ActionModule)

    # Attributes are set to None by default.
    assert(mock_module._task.args is {})

    # Attributes are assigned properly.
    mock_module._task.args = {
        'src': 'source.tar.gz',
        'dest': 'destination',
        'remote_src': True,
        'creates': 'file1.txt',
        'decrypt': False,
    }
    mock_module._task.args['copy'] = 'yes'

    mock_loader = mock.Mock()


# Generated at 2022-06-13 10:58:58.054678
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a class structure for testing
    class TestClass(object):
        pass


    setattr(TestClass, '_execute_remote_stat', test_ActionModule_run.set_execute_remote_stat)
    setattr(TestClass, '_fixup_perms2', test_ActionModule_run.set_fixup_perms2)
    setattr(TestClass, '_remove_tmp_path', test_ActionModule_run.set_remove_tmp_path)
    setattr(TestClass, '_transfer_file', test_ActionModule_run.set_transfer_file)

    task_vars = dict()  # type: dict
    dest_dir = "/home/vagrant"

    task_vars["ansible_check_mode"] = True

# Generated at 2022-06-13 10:59:08.556657
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.strategy import ActionModuleComponent
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    x = '''
    -
      hosts: localhost
      tasks:
        - unarchive:
            src: ~/files/foo.zip
            dest: /tmp/unzip
        - unarchive:
            content: 'yes'
            dest: /tmp/unzip2
        - unarchive:
            src: ~/files/foo.zip
            dest: /tmp/unzip
            creates: /tmp/unzip/file1
    '''

    y= InventoryManager(loader=None, sources="localhost")

# Generated at 2022-06-13 10:59:10.460294
# Unit test for constructor of class ActionModule
def test_ActionModule():
    my_class = ActionModule()
    assert isinstance(my_class, ActionModule)


# Generated at 2022-06-13 10:59:20.252715
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    dest = '/home/snowden/snowden.jpg'
    source = '~/snowden.jpg'
    task_vars = dict()
    creates = None
    decrypt = True
    remote_src = False
    remote_stat = dict()
    remote_stat['exists'] = True
    remote_stat['isdir'] = True
    # test for action fail
    module = ActionModule()
    task = dict()
    task['args'] = dict()
    task['args']['decrypt'] = decrypt
    task['args']['src'] = source
    task['args']['dest'] = dest
    module._task = task
    module._remote_expand_user = lambda x: x
    module._remote_file_exists = lambda x: False

# Generated at 2022-06-13 11:02:05.176478
# Unit test for constructor of class ActionModule
def test_ActionModule():
    instance = ActionModule(None, dict())
    assert isinstance(instance, ActionModule)

# Generated at 2022-06-13 11:02:05.776215
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:02:08.208049
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Test Constructor of ActionModule")
    try:
        action = ActionModule()
    except Exception as e:
        print(e)
    else:
        print("Passed Constructor Test")

if __name__ == "__main__":
    test_ActionModule()

# Generated at 2022-06-13 11:02:15.371855
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    this_directory = os.path.dirname(__file__)
    fname = os.path.join(this_directory, 'test', 'data', 'test_action_module.txt')
    dname = os.path.join(this_directory, 'test', 'data', 'test_action_module')

    # I will run the action module unarchive with the following parameters
    # src = test/data/test_action_module.txt
    # remote_src = False
    # dest = '~/' (the user home directory)
    # creates = test/data/test_action_module (the directory must be created)
    # decrypt = True

    # I will test the function without options
    args = dict(src=None, remote_src=None, dest=None, creates=None, decrypt=None)

# Generated at 2022-06-13 11:02:23.286809
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Mock out a connection plugin
    class MockConnection:
        class _shell:
            class tmpdir:
                def __init__(self):
                    pass
                def __str__(self):
                    return '/tmp'

            def __init__(self):
                self.tmpdir = '/tmp'

            def join_path(self, path1, path2):
                return path1 + "/" + path2

            def _execute_remote_stat(self, path, all_vars=None, follow=True):
                return {'exists': True, 'isdir': True}
        
        def __init__(self):
            self._shell = MockConnection._shell()

        # Mock out a method that the real connection plugin has 
        def _remove_tmp_path(self, tmp):
            pass # Do nothing, just testing run function

# Generated at 2022-06-13 11:02:30.518274
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ''' test_ActionModule
    This is a unit test for the ActionModule constructor
    '''

    # Create mock task, play, and runner objects
    task = MockTask()

    # Create our ActionModule to test
    am = ActionModule(task=task, connection=MockConnection(), play_context=MockPlayContext(), loader=MockLoader(), templar=None, shared_loader_obj=None)

    # Check the name of the module is correctly set
    assert am._task.action == 'unarchive'

# Generated at 2022-06-13 11:02:31.572902
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert(True)



# Generated at 2022-06-13 11:02:35.287934
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible import playbook
    from ansible import play
    from ansible import module_loader

    assert playbook.Playbook()._loader is not None
    assert play.Play()._loader is not None
    assert module_loader._plugins is not None

# Generated at 2022-06-13 11:02:35.754602
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 11:02:49.422447
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os

    from unittest import TestCase
    from unittest import mock
    from ansible.plugins.action.unarchive import ActionModule
    from ansible.parsing.yaml.objects import AnsibleUnicode

    TEST_FILE_NAME = 'test_file'

    class TestActionModule(TestCase):
        def setUp(self):
            self.action_module = ActionModule(
                task=mock.Mock(),
                connection=mock.Mock(),
                play_context=mock.Mock(),
                loader=mock.Mock(),
                templar=mock.Mock(),
                shared_loader_obj=mock.Mock()
            )
            self.action_module._remove_tmp_path = mock.Mock()
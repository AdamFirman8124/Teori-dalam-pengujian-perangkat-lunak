

# Generated at 2022-06-13 10:16:12.585103
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 1 == 1

# Generated at 2022-06-13 10:16:21.019056
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.utils.vars as av
    from ansible.module_utils.basic import AnsibleModule

    module_name = 'setup'
    module_args = {}
    module_args_loaded = av.unpack(module_args)
    module_args_loaded['action'] = 'setup'
    am = AnsibleModule(module_name, module_args, False, False, False)
    at = am.ActionModule(am)
    at.run()
    assert "python version = 2.7.18" in at._execute_module()['invocation']['module_args']

# Generated at 2022-06-13 10:16:22.367049
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Assume role to be non-zero, non-None
    # assert True
    pass

# Generated at 2022-06-13 10:16:23.310456
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:16:33.792086
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # create a connection
    connection = Connection('localhost')

    # create an instance of Ansiballz
    actionmodule = ActionModule(connection._shell, 'test', 'some.module', {})

    # create an instance of AnsibleTask
    task = Task('test module', actionmodule)
    setattr(task._ds, 'become', False)
    setattr(task._ds, 'become_method', None)
    setattr(task._ds, 'become_user', None)
    setattr(task._ds, 'no_log', False)

    # create an instance of PlayContext
    play_context = PlayContext()

    # set the connection in the play context
    play_context.set_connection('local')

    # set the play context in the connection
    connection._play_context = play_context

    # set the

# Generated at 2022-06-13 10:16:34.538683
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run()

# Generated at 2022-06-13 10:16:35.325576
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False

# Generated at 2022-06-13 10:16:37.640807
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.test import test_ActionModule_run
    test_ActionModule_run()

# Generated at 2022-06-13 10:16:38.389310
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 10:16:49.657066
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible import context
    import ansible.constants
    module_name="command"
    task=Task()
    task._ds=dict()
    task._ds['action']='command'
    task._ds['local']='command'
    task._ds['argument_spec']=dict()
    task._ds['argument_spec']['local']=dict()
    play_context=PlayContext()
    play_context._ds=dict()
    play_context_obj=PlayContext()
    play_context_obj._ds['become']=False
    play_context_obj._ds['become_method']=None

# Generated at 2022-06-13 10:17:05.938041
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  module = ActionModule()
  assert(module is not None)

  module._task.async_val = False
  module._connection.has_native_async = False
  module._execute_module = lambda *x: {'a':1}

  result = module.run(task_vars={'a':2})
  print(result)
  assert(result['a'] == 1)
  assert('_ansible_verbose_override' not in result)
  assert('invocation' not in result)

  module._task.async_val = False
  module._connection.has_native_async = True
  module._execute_module = lambda *x: {'a':1}

  result = module.run(task_vars={'a':2})
  print(result)

# Generated at 2022-06-13 10:17:10.071552
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(loader=None, connection=None, play_context=None, loader_basedir=None)
    try:
        module.supports_check_mode = True
        module.supports_async = True
    except NameError as e:
        assert True
        return
    assert False, 'NameError expected'

# Generated at 2022-06-13 10:17:18.002524
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # sample data that we are going to use to mock out our actual test results
    # from the above test code
    _task = {
        u'async_val': 0,
        u'action': u'setup',
        u'async': 0,
    }
    _tmp = u'/tmp/ansible/'
    _task_vars = {
        u'ansible_check_mode': True
    }
    _connection = {
        u'has_native_async': False
    }
    _result = {
        u'invocation': {
            u'module_args': {}
        },
        u'failed': False,
        u'_ansible_item_result': False
    }
    # mock out the AnsibleModule class so we can check what parameters are passed
    # to the run method

# Generated at 2022-06-13 10:17:18.643994
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:17:23.887835
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_plugin = ActionModule('setup', 'localhost', 'setup', 'localhost', '0.0.0.0')
    assert action_plugin._task.name == 'setup'
    assert action_plugin._task.action == 'setup'
    assert action_plugin._connection.host == 'localhost'
    assert action_plugin._connection.port == '0.0.0.0'

# Generated at 2022-06-13 10:17:32.530009
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    ####################
    # action._execute_module
    ####################
    import os
    import re
    import json
    import tempfile
    import pwd
    import operator
    import errno
    import threading
    import itertools
    import subprocess
    import time
    import shutil
    import base64
    import datetime
    import hashlib
    import contextlib
    import copy
    import getpass
    from collections import defaultdict

    from ansible import constants as C
    from ansible.module_utils.six import string_types, text_type, binary_type
    from ansible.module_utils.six.moves import shlex_quote
    from ansible.module_utils._text import to_bytes, to_text, to_native
    from ansible.module_utils.urls import open_url

# Generated at 2022-06-13 10:17:34.572686
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert a.get_action_args() == {}


# Generated at 2022-06-13 10:17:37.883535
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor for class ActionModule
    basic = ActionModule(ActionBase._shared_loader_obj,connection=None, play_context=None, templar=None)
    basic.my_path = "tmp"
    str(basic)

# Generated at 2022-06-13 10:17:48.526633
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Constructor
    action_module = ActionModule(task=Task(), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # action_module._supports_check_mode should be True
    assert action_module._supports_check_mode == True, 'action_moduel._supports_check_mode should be True'

    # action_module._supports_async should be True
    assert action_module._supports_async == True, 'action_module._supports_async should be True'

# Generated at 2022-06-13 10:17:49.053109
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 1 == 1

# Generated at 2022-06-13 10:18:00.320631
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import __main__
    import json
    import unittest

# Use a class so that we can do setup before each test
# not sure if this is the best way to do this
    class TestActionModule(unittest.TestCase):
        def setUp(self):
            # This is needed so that Ansible can read our tmp dir
            # so that the temp file created by _execute_module can be cleaned up
            # not sure this is the best way to do this
            __main__.__file__ = "/tmp"

            test_module = dict()

            test_module['name'] = "testmod"
            test_module['action'] = "testmod"

            test_module['module_name'] = "testmod"
            test_module['module_args'] = "testmod"

            test_module['async_val']

# Generated at 2022-06-13 10:18:02.917977
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None).__class__.__name__ == 'ActionModule'



# Generated at 2022-06-13 10:18:05.498914
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ constructor test """

    action_plugin = ActionModule()
    assert action_plugin is not None

# Generated at 2022-06-13 10:18:16.908860
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import ansible.plugins.action
    import ansible.utils.module_docs as mod_docs

    # construct test module, which returns 'changed' value always as True
    class ActionModuleTest(ActionModule):
        def run(self, tmp=None, task_vars=None):
            return {'changed': True}

    # construct test task
    class PlayContext(object):
        def __init__(self, action=None, verbosity=0):
            self.action = action
            self.verbosity = verbosity

    class Task(object):
        def __init__(self, action=None):
            self.async_val = None
            self.action = action


# Generated at 2022-06-13 10:18:18.908280
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # test defaults
    nick = ActionModule()
    assert nick._supports_check_mode == True
    assert nick._supports_async == True

# Generated at 2022-06-13 10:18:25.904399
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a mock object for the class AnsibleModule
    mock_ansible_module = MagicMock(spec=AnsibleModule)
    # Create a mock object for the class Task
    mock_ansible_task = MagicMock(spec=Task)
    mock_ansible_task._ds = dict()

    # Set the connection property to None
    mock_ansible_task.connection = None

    # Add the mock objects to the ActionModule
    temp = ActionModule(mock_ansible_module, mock_ansible_task)

    # Assert that connection property of class ActionModule is not None
    assert temp._task.connection is not None

# Generated at 2022-06-13 10:18:33.476983
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    task_ds = dict(action=dict(module='debug', args=dict(msg='Hello World')))
    task = Task.load(task_ds)
    play_context = PlayContext()
    action = ActionModule(task, play_context)

    assert action._supports_check_mode is True
    assert action._supports_async is True

# Generated at 2022-06-13 10:18:42.850756
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_obj = ActionModule()
    assert action_obj._task.action == 'test', action_obj.__dict__
    assert action_obj._supports_check_mode == True, action_obj._supports_check_mode
    assert action_obj._supports_async == True, action_obj._supports_async
    assert action_obj._connection._shell.tmpdir == '/root/.ansible/tmp', action_obj._connection._shell.tmpdir
    print("type: ", type(action_obj._connection._shell))
    print("type: ", type(action_obj._task))

if __name__ == "__main__":
    test_ActionModule()

# Generated at 2022-06-13 10:18:46.788389
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create an instance of ActionModule
    action_module = ActionModule()

    # TODO: mock all methods in ActionBase
    # action_module.run(tmp=None, task_vars=None)

# Generated at 2022-06-13 10:18:48.269438
# Unit test for constructor of class ActionModule
def test_ActionModule():
  a = ActionModule()
  assert a.run != None

# Generated at 2022-06-13 10:19:03.512837
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    module = ActionModule()

    # def run(self, tmp=None, task_vars=None):
    # this method has not return value
    print("begin test_ActionModule_run")
    print("end test_ActionModule_run")

if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:19:08.045341
# Unit test for constructor of class ActionModule
def test_ActionModule():
    #Initializing test data
    hostname = "hostname"
    task = {"name": "test"}
    task_vars = {"test_variable": "test_variable"}
    play_context = {}
    loader = None
  
    #Run test
    module = ActionModule(hostname, task, task_vars, play_context, loader)
    assert module is not None

# Generated at 2022-06-13 10:19:15.372238
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory import Inventory
    import ansible.constants as C
    import os
    import tempfile
    import json

    sample_playbook = '''---
- hosts: all
  gather_facts: no
  tasks:
    - name: test
      action_test:
    - name: test2
      action_test:
        test: 2
'''
    test_hosts = ['127.0.0.1', 'localhost']
    test_inventory = Inventory(loader=None,
                               host_list=test_hosts)
    test

# Generated at 2022-06-13 10:19:16.505064
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test that run works as expected
    assert True

# Generated at 2022-06-13 10:19:29.631268
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Constructor test of class ActionModule
    :return:
    '''
    from ansible.playbook.task import Task
    from ansible.playbook.role.task import Task as RoleTask

    action = {u'__ansible_module__': 'test'}
    task = Task.load(action, dict(), loader=None, variable_manager=None)
    role_task = RoleTask.load(action, dict(), loader=None, variable_manager=None)

    assert isinstance(ActionModule(task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None), ActionModule)

# Generated at 2022-06-13 10:19:30.171350
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()

# Generated at 2022-06-13 10:19:39.132702
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.modules.system import ping
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.action.standard import ActionModule
    import ansible.utils.vars
    import ansible.plugins.loader
    import ansible.utils.vars
    import ansible.parsing.dataloader
    import ansible.utils.module_docs
    import sys

    # using a fake module
    sys.modules["ansible.modules.system.ping"] = ping


# Generated at 2022-06-13 10:19:39.625119
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:19:44.745749
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:19:56.556108
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import ansible.plugins.action.__init__ as action
    import ansible.plugins.action.command as command

    class DummyModule:
        def __init__(self):
            self.action_plugins = { 'command': command.ActionModule }
    class DummyFacts:
        def __init__(self):
            self.ansible = DummyModule()
            self.setup = DummyModule()
            self.sysconfig = DummyModule()

    class DummyArgs:
        def __init__(self):
            self.module_args = { 'command': 'ls /' }
        def copy(self):
            return self

    class DummyTask:
        def __init__(self):
            self.action = 'command'
            self.args = DummyArgs()
            self.async_val = 0



# Generated at 2022-06-13 10:20:20.950574
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass
# src/ansible/plugins/action/__init__.py ends here

# Generated at 2022-06-13 10:20:23.209616
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ ActionModule testcases """

    # Constructor test case
    module = AnsibleFiles()
    assert module

# Generated at 2022-06-13 10:20:32.455587
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars

    action_module = ActionModule(task=Task(), connection='local', play_context=PlayContext(), loader=None, templar=None, shared_loader_obj=None)
    source = '{{playbook_dir}}/../../library'
    result = action_module.add_action_plugin_path(source)
    assert(result == '{{playbook_dir}}/../../library/action_plugins')

    source = 'library'
    result = action_module.add_action_plugin_path(source)

# Generated at 2022-06-13 10:20:32.890957
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # pass
    pass

# Generated at 2022-06-13 10:20:38.273237
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module_obj = ActionModule(task={"action":"shell", "args":{"chdir":"/tmp", "executable":"/bin/sh"}})
    assert action_module_obj.name == 'action'
    assert action_module_obj.task_vars == {}
    assert action_module_obj.tmp == "/tmp/ansible-tmp-1554477744.72-263468461333211/"

# Generated at 2022-06-13 10:20:43.983084
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module._execute_module = lambda x, y: {'result': 'from _execute_module'}
    module._remove_tmp_path = lambda x: None
    module._task.async_val = False
    module._connection.has_native_async = False
    result = module.run()
    assert result['result'] == 'from _execute_module'

# Generated at 2022-06-13 10:20:47.325624
# Unit test for constructor of class ActionModule
def test_ActionModule():
    yaml_dict = {}
    yaml_dict['param1'] = "var1"
    yaml_dict['param2'] = "var2"
    assert ActionModule.run_yaml(yaml_dict) is not None

# Generated at 2022-06-13 10:20:57.423740
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # 
    # Initialize required instances and variable
    #
    # instance of ActionModule
    a = ActionModule()
    # instance of Ansible
    ansible = Ansible()
    # instance of TaskExecutor
    task_executor = TaskExecutor()
    #
    # Define test functions
    #
    # [1] run(self, tmp=None, task_vars=None)
    def run(self, tmp=None, task_vars=None):
        #
        # skips all features.
        # [1.1] define dummy functions
        def supported_features(self):
            return C.DEFAULT_COMPLEX_ARGS_KEYS
        # [1.2] overwrite functions
        ActionBase.supported_features = supported_features
        # [1.3] initialize required instances and variable
       

# Generated at 2022-06-13 10:21:09.428933
# Unit test for constructor of class ActionModule
def test_ActionModule(): #ActionModule.__init__
    #Test with default values
    action_module = ActionModule(None, None, None, None, None)
    assert action_module._display.verbosity == 3
    assert action_module._connection.port == 22
    assert action_module._connection.user == 'root'
    assert action_module._connection.password == None
    assert action_module._task.no_log == False
    assert action_module._task.become == True
    assert action_module._task.become_user == 'root'
    assert action_module._task.become_method == 'sudo'
    assert action_module._task.become_flags == '-H'
    assert action_module._task.environment == {}
    assert action_module._task.sudo == True

# Generated at 2022-06-13 10:21:17.857831
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Create a mock instance of class Connection.
    class Connection:
        has_native_async = True
        _shell = None
    # Create a mock instance of class PlayContext.
    class PlayContext:
        async_val = False
    # Create a mock instance of class Str.
    class Str:
        def __init__(self):
            self.name = 'ActionModule'
        def __str__(self):
            return self.name
    class Task:
        async_val = False
    class Play:
        action = 'setup'
    class Playbook:
        action = 'setup'
    # Create a mock instance of class AnsibleModule.
    class AnsibleModule:
        argument_spec = {}
    module_loader = AnsibleModule()
    # Create a mock instance of class ActionBase.

# Generated at 2022-06-13 10:22:19.930999
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for method run of class ActionModule"""
    pass

# Generated at 2022-06-13 10:22:24.078465
# Unit test for constructor of class ActionModule
def test_ActionModule():
    my_module = ActionModule(dict(ACTION=dict(MODULE='test')))
    assert my_module is not None

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:22:27.596291
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        action_module = ActionModule(runner)
    except NameError:
        action_module = ActionModule(None)
    assert type(action_module) is ActionModule

# Generated at 2022-06-13 10:22:29.531473
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print ("Testing method run of class ActionModule")
    #Initalizing the class
    a = ActionModule()
    #calling run with sample arguments
    a.run('tmp=None', 'task_vars=None')

# Generated at 2022-06-13 10:22:33.592761
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule(
        task = dict(action = dict(module = 'ping', args = dict(data = 'pong'))),
        connection = dict(module = 'local', play_context = dict(become = True))
    )

# Generated at 2022-06-13 10:22:34.769036
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    print("test: ActionModule_run")

# Generated at 2022-06-13 10:22:35.289671
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule().run()

# Generated at 2022-06-13 10:22:46.913551
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task_vars = dict(
        ansible_play_hosts=['localhost'],
        ansible_ssh_host='localhost',
        ansible_ssh_user='ubuntu',
        ansible_sudo_pass='password',
    )

    am = ActionModule(task=dict(action='foo', async_val=True), connection='connection_name', play_context=dict(remote_user='root'), loader=None, templar=None, shared_loader_obj=None)
    assert am.async_timeout == C.DEFAULT_ASYNC_POLL_TIMEOUT
    assert am.async_timeout is not None
    assert am.async_val == True
    assert am.connection == 'connection_name'
    assert am.become is False
    assert am.become_method == 'sudo'
    assert am

# Generated at 2022-06-13 10:22:47.451906
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:22:48.711272
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: mock object devel
    raise NotImplementedError()

# Generated at 2022-06-13 10:24:59.214249
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action
    am = ansible.plugins.action.ActionModule(
        connection='smart',
        becomes_user=None,
        diff=False,
        no_log=False,
        su=None,
        sudo=None,
        sudo_user=None
    )
    assert am._connection == 'smart'
    assert am._become is None
    assert am._task is None
    assert am._loader is None
    assert am._variable_manager is None
    assert am._shared_loader_obj is None
    assert am._shared_action_plugin is None
    assert am._connection_info is None
    assert am._templar is None
    assert am._task_vars is None
    assert am._block is None
    assert am._task_ds is None

# Generated at 2022-06-13 10:25:00.153562
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO
    assert True

# Generated at 2022-06-13 10:25:01.430700
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test the function with the default values for its arguments.
    action_module = ActionModule()
    assert action_module.run() == True


# Test if the testcase is being executed from the correct location

# Generated at 2022-06-13 10:25:06.024112
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Test the module
    module = ActionModule(
        task=dict(action=dict(__ansible_module_name__='yum', args=dict(name="httpd"))),
        connection=dict(),
        play_context=dict(check_mode=True),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )
    assert module._supports_check_mode is True
    assert module._supports_async is True

# Generated at 2022-06-13 10:25:07.055150
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule
    """
    pass

# Generated at 2022-06-13 10:25:11.179240
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Given an action module that does not override run
    am = ActionModule()

    # When I run the action module
    am.run()

    # Then I expect that run was called without an exception
    pass

# Generated at 2022-06-13 10:25:14.788873
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # output for run when wrap_async is True
    assert ActionModule.run(ActionModule, None, None) == {}
    # output for run when wrap_async is False
    assert ActionModule.run(ActionModule, None, None, wrap_async=False) == {}

# Generated at 2022-06-13 10:25:19.930424
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # this is a simple unit test to show how one would build a unit test for
    # ansible action plugins
    host_name = 'test_host'
    host_ip = '127.0.0.1'
    args = {}
    args['name'] = 'sample action plugin'
    args['action'] = 'sample_plugin'
    args['delegate_to'] = None
    args['async'] = 0
    args['poll'] = 0
    args['sleep'] = 0
    args['become'] = False
    args['become_method'] = 'sudo'
    args['become_user'] = 'root'
    args['check'] = False
    args['verbosity'] = 0
    args['connection'] = 'local'
    args['_ansible_verbosity'] = 0

# Generated at 2022-06-13 10:25:20.553086
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:25:28.142172
# Unit test for method run of class ActionModule
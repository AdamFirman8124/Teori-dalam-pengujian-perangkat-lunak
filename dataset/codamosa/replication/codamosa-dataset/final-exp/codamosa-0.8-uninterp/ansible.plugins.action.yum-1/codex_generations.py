

# Generated at 2022-06-13 11:18:56.020993
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert 'auto' == am.run(tmp='/tmp', task_vars={'ansible_facts': {'pkg_mgr': 'auto'}})['ansible_facts']['pkg_mgr']

# Generated at 2022-06-13 11:19:01.281004
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(args={'use_backend': 'yum3'}),
        connection=dict(),
        play_context=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )

    assert module._task.args['use_backend'] == "yum3"



# Generated at 2022-06-13 11:19:12.103480
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock_conn = MockConnection()
    mock_conn._shell = Mock()
    mock_connection = Mock()
    mock_connection.get_connection = Mock(return_value=mock_conn)
    mock_module = Mock(connection=mock_connection)

# Generated at 2022-06-13 11:19:22.560256
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    yum_module = ActionModule()

    fake_task = DummyTask()
    fake_play_context = DummyPlayContext()
    fake_shared_loader = DummySharedLoader()
    fake_task_vars = 'faked_task_vars'
    fake_module_args = 'faked_module_args'
    fake_module_name = 'faked_module_name'

    # Case the module_name is supported
    assert yum_module._execute_module(module_name=fake_module_name,
                                      module_args=fake_module_args,
                                      task_vars=fake_task_vars) == {'result': 1}

    # Case the module_name is not supported

# Generated at 2022-06-13 11:19:25.206609
# Unit test for constructor of class ActionModule
def test_ActionModule():

    import ansible.plugins.action.yum as yum
    action_module = yum.ActionModule()
    assert action_module != None

# Generated at 2022-06-13 11:19:33.231491
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_args_dict = { "use": "yum4", }
    module_args_dict["i"] = "yes"
    module_args_dict["g"] = "yes"
    module_args_dict["y"] = "yes"
    module_args_dict["args"] = "install"
    module_args_dict["name"] = "git"
    tmp = None

# Generated at 2022-06-13 11:19:34.266626
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert am

# Generated at 2022-06-13 11:19:42.953856
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule(loader=None, connection=None, play_context=None, loader_obj=None, add_parsed_args=False, templar=None, shared_loader_obj=None, task_vars=None, args=None,
                                internal_poll_interval=None)

    assert actionmodule._supports_check_mode
    assert actionmodule._supports_async
    assert isinstance(actionmodule.VALID_BACKENDS, frozenset)
    assert 'yum' in actionmodule.VALID_BACKENDS
    assert 'yum4' in actionmodule.VALID_BACKENDS
    assert 'dnf' in actionmodule.VALID_BACKENDS

# Generated at 2022-06-13 11:19:50.090030
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import os
    import tempfile

    if sys.version_info[0] < 3:
        import __builtin__ as builtins  # Python 2.x
    else:
        import builtins  # Python 3.x

    import ansible.plugins.action.yum as yum_plugin

    class DummyConnection(object):
        def __init__(self):
            self._shell = DummyShell()

    class DummyShell(object):
        def __init__(self):
            self.tmpdir = tempfile.mkdtemp()

    class DummyTask(object):
        def __init__(self, args):
            self.args = args
            self.async_val = None

    tmp = tempfile.mkdtemp()

    c = DummyConnection()

# Generated at 2022-06-13 11:19:55.509856
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule(load_fixture("fake_task.json"),
                          connection=None,
                         
                          play_context=None,
                          loader=None,
                          templar=None,
                          shared_loader_obj=None)
    result = action.run(tmp=None, task_vars=None)
    assert result['failed'] == True

# Generated at 2022-06-13 11:20:10.935919
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Sample data to be used in tests

    # Sample data to be used in tests
    task_vars = {}
    result = {}
    result['ansible_facts'] = {'pkg_mgr': 'yum'}
    # Expected result of the testcase execution
    expected_result = {
        'failed': True, 'msg': ("Could not detect which major revision of yum is in use, which is required to determine module backend.",
                       "You should manually specify use_backend to tell the module whether to use the yum (yum3) or dnf (yum4) backend})")}

    # Execute the run method to test
    # This creates an object of class ActionModule

# Generated at 2022-06-13 11:20:12.053017
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None)
    assert not action_module is None

# Generated at 2022-06-13 11:20:21.340145
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialize some test data
    tmp = '/tmp/tmp'
    task_vars = ['task_vars']
    module = 'auto'

    # Create a new ActionModule object
    action_module = ActionModule()
    action_module._task.args = {'use': module}

    # Run the code to test
    result = action_module.run(tmp, task_vars)

    # Check assertion
    assert result == {'failed': True, 'msg': ("Could not detect which major revision of yum is in use, which is required to determine module backend.",
                                              "You should manually specify use_backend to tell the module whether to use the yum (yum3) or dnf (yum4) backend})")}

# Generated at 2022-06-13 11:20:31.421297
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.plugins.action.yum import ActionModule as yum_module
    from ansible.playbook.task import Task
    from ansible.utils.vars import combine_vars
    import ansible.plugins.loader as plugins
    import ansible.module_utils.basic as module_utils

    display = Display()

    test_task = Task()
    test_task.args = {
        'name': 'test-module',
        'state': 'present',
        'use_backend': 'yum3',
        'verbose': True
    }
    test_task.delegate_facts = False
    test_task.async_val = 40
    test_task._role = None
    test_task.notify = []
    test_task.tags = []
    test_task._diff = False

   

# Generated at 2022-06-13 11:20:37.292159
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_name = 'yum3'
    module_args = dict(key='value')
    tmp = '/nothing'
    task_vars = dict(key='value')

    am = ActionModule(module_name, module_args, tmp, task_vars)
    assert am.module_name == 'yum3'
    assert am.module_args == dict(key='value')
    assert am.tmp == '/nothing'
    assert am.task_vars == dict(key='value')

# Generated at 2022-06-13 11:20:44.879137
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule.
    '''

    import sys

    import ansible.modules.packaging.legacy.yum
    # import ansible.modules.packaging.yum
    sys.modules['ansible.modules.packaging.legacy.yum'] = ansible.modules.packaging.legacy.yum

    import ansible.modules.packaging.legacy.dnf
    # import ansible.modules.packaging.dnf
    sys.modules['ansible.modules.packaging.legacy.dnf'] = ansible.modules.packaging.legacy.dnf

    class AnsibleModuleFake:
        '''
        Fake class for AnsibleModule.
        '''

# Generated at 2022-06-13 11:20:56.441495
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action
    import ansible.utils.display

    class MockTask:
        def __init__(self):
            self.args = {}
            self.delegate_to = None
            self.delegate_facts = None
            self.async_val = None


    class MockTemplar:
        def __init__(self):
            pass

        def template(self, data):
            return 'yum'

    class MockModuleLoader:
        def __init__(self):
            self.has_plugin_return = True

        def has_plugin(self, module):
            return self.has_plugin_return

    class MockShellConnection:
        def __init__(self):
            self.tmpdir = "/tmp/test/123"


# Generated at 2022-06-13 11:21:03.493692
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mock_action = ActionModule(dict(action='yum'))

    class MockModule:
        def __init__(self, module_name=None, module_args=None, task_vars=None, wrap_async=None):
            self.module_name = module_name
            self.module_args = module_args
            self.task_vars = task_vars
            self.wrap_async = wrap_async

    class MockLoader:
        def has_plugin(self, module_name=None):
            return module_name == 'ansible.legacy.yum'

    mock_action._execute_module = MockModule
    mock_action._templar = MockModule
    mock_action._shared_loader_obj = MockLoader()
    mock_action._task = MockModule()
    mock_action._

# Generated at 2022-06-13 11:21:12.677214
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.TRANSFERS_FILES = False
    action = ActionModule()
    task = {
      'args': {
        'module': 'auto',
        'module_args': {}
      }
    }

# Generated at 2022-06-13 11:21:14.265925
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Inside test_ActionModule")
    my_obj = ActionModule()


# Generated at 2022-06-13 11:21:29.442240
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import json
    import textwrap
    import os
    import pprint
    from io import StringIO
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.vault import VaultLib

# Generated at 2022-06-13 11:21:42.606451
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Class instantiation
    module = ActionModule()
    # Method run
    module.run(tmp=None, task_vars=None)

    # Module import
    from ansible.plugins.action.yum import ActionModule
    # Instanciation
    inst = ActionModule()
    # Class attributes
    # Inherited from ActionBase.ActionBase
    # _shared_loader_obj
    result = inst._shared_loader_obj
    # _display
    result = inst._display
    # _templar
    result = inst._templar
    # _config
    result = inst._config
    # _task
    result = inst._task
    # _loader
    result = inst._loader
    # _connection
    result = inst._connection
    # _play_context
    result = inst._play_context
    # _

# Generated at 2022-06-13 11:21:43.510948
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 11:21:44.951593
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    connection = None
    assert False

# Generated at 2022-06-13 11:21:47.170889
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None,
                        loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 11:21:52.243821
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for the run() method of ActionModule class
    '''

    module = ActionModule(ActionModule._play_context, ActionModule._shared_loader_obj, ActionModule._task,
                          ActionModule._connection, ActionModule._play_context.variable_manager,
                          ActionModule._loader)

    results = module.run()
    assert module is not None
    assert results['failed'] is True
    assert results['msg'] == "parameters are mutually exclusive: ('use', 'use_backend')"

# Generated at 2022-06-13 11:21:52.793327
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 11:21:56.080255
# Unit test for constructor of class ActionModule
def test_ActionModule():
    my_test_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert my_test_module is not None
    assert my_test_module.VALID_BACKENDS == frozenset(('yum', 'yum4', 'dnf'))

# Generated at 2022-06-13 11:21:56.650563
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 11:22:02.859376
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.common.process import get_bin_path
    import os
    import tempfile
    import shutil
    import sys

    # create a temp dir and source and destination files
    tmpdir = tempfile.mkdtemp()
    yum = os.path.join(tmpdir, "yum")
    dnf = os.path.join(tmpdir, "dnf")
    os.environ['PATH'] = "%s:%s" % (tmpdir, os.environ['PATH'])

    # create a fake yum3 and yum4 executables
    with open(yum, 'w') as fh:
        fh.write("#!/bin/sh\n")
        fh.write("echo yum\n")

# Generated at 2022-06-13 11:22:24.994410
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m_task = {
        'args': dict(param1='value1', param2='value2'),
        'delegate_to': None,
        'delegate_facts': True,
    }
    m_module = 'yum'
    m_task_vars = {'ansible_facts': dict(pkg_mgr='auto')}
    m_tmp = 'test'
    m_display = Display()

    action_module = ActionModule(m_task, m_connection, m_play_context, m_loader, m_templar, m_shared_loader_obj)
    result = action_module.run(m_tmp, m_task_vars)


# Generated at 2022-06-13 11:22:34.653077
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule
    """
    fake_task_vars = {}

    # noinspection PyTypeChecker
    test_instance = ActionModule(loader=None,
                                 task=None,
                                 connection=None,
                                 play_context=None,
                                 loader_cache=None,
                                 shared_loader_obj=None,
                                 templar=None,
                                 shared_loader_cache=None)

    # valid argument and no delegate
    test_instance._task.args = {'use': 'auto'}
    test_instance._task.delegate_to = ''
    test_instance._task.async_val = False
    test_instance._task.async_seconds = ''
    test_instance._task.timeout = 0
    # noinspection PyUn

# Generated at 2022-06-13 11:22:48.628207
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #mock connection
    connection = Connection()

    #mock the class inside the action plugin
    class Yum:
        def __init__(self,action,task_vars):
            self.action = action
            self.task_vars = task_vars

        def run(tmp,task_vars):
            return {'ansible_facts': {'pkg_mgr': 'dnf'}}

    #mock the connection object
    #patch the get_option method of the connection
    #mock the get_option method to return a value
    with patch.object(ActionModule,'_execute_module') as _execute_module:
        _execute_module.return_value = {'ansible_facts': {'pkg_mgr': 'dnf'}}
        #patch the connection object

# Generated at 2022-06-13 11:22:51.357568
# Unit test for constructor of class ActionModule
def test_ActionModule():
    expected = {
        'supports_check_mode': True,
        'supports_async': True,
    }
    actual = ActionModule()
    assert actual.__dict__ == expected

# Generated at 2022-06-13 11:22:57.786959
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()

    try:
        action_module._shared_loader_obj = None
        action_module.run()
        assert False
    except AnsibleActionFail:
        assert True

    try:
        action_module._shared_loader_obj = None
        action_module.run(None)
        assert False
    except AnsibleActionFail:
        assert True

    try:
        action_module._shared_loader_obj = None
        action_module.run(None, None)
        assert False
    except Exception:
        assert True

# Generated at 2022-06-13 11:23:06.145221
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils._text import to_bytes
    from ansible.utils.display import Display
    from ansible.plugins.action import ActionBase
    from ansible.playbook.play_context import PlayContext

    display = Display()
    context = PlayContext()

# Generated at 2022-06-13 11:23:10.242145
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Unit test for constructor of class ActionModule
    :return: None
    """
    action_module = ActionModule(None, None)
    del(action_module)

# Generated at 2022-06-13 11:23:15.672111
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    
    #mock_results = {}

    #mock_result = {}
    #mock_result['msg'] = "Could not detect which major revision of yum is in use, which is required to determine module backend."
    #mock_result['failed'] = True
    #mock_results['auto'] = mock_result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pass

# Generated at 2022-06-13 11:23:23.855251
# Unit test for constructor of class ActionModule
def test_ActionModule():

    def test_valid_inputs(input_str, output_str):

        # Create an instance of ActionModule
        action_obj = ActionModule()

        # Make the protected member accessible
        action_obj._task.args = input_str
        action_obj._shared_loader_obj.module_loader.has_plugin = lambda x: True

        # Invoke the run() function and check the output
        assert action_obj.run() == output_str

    # Invoke the test_valid_inputs() with valid inputs

# Generated at 2022-06-13 11:23:26.289947
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None, None)

# Generated at 2022-06-13 11:23:54.152451
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)

# Generated at 2022-06-13 11:23:54.761657
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule()

# Generated at 2022-06-13 11:24:03.884285
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager

    play_context = PlayContext()

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'use': 'auto'}

    task_queue_manager = TaskQueueManager(
        inventory=None,
        variable_manager=variable_manager,
        loader=None,
        options=None,
        passwords=None,
        stdout_callback=None,
    )

    action_module = ActionModule(
        task=None,
        connection=None,
        play_context=play_context,
        loader=None,
        templar=None,
        shared_loader_obj=None,
    )



# Generated at 2022-06-13 11:24:04.556370
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:24:14.414075
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module._task = mock.MagicMock()
    module._task.args = {'pkg': 'cowsay'}
    module._templar = mock.MagicMock()
    module._templar.template.side_effect = ["dnf", "yum", "auto"]

    # normal flow
    module._task.args = {'use': 'auto', 'state': 'present'}
    module._execute_module = mock.MagicMock(return_value={'ansible_facts': {'pkg_mgr': 'dnf'}})
    result = module.run()
    assert 'ansible_facts' in result
    assert result['ansible_facts']['pkg_mgr'] == 'dnf'

# Generated at 2022-06-13 11:24:16.631310
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule().run()['msg'] == "Could not detect which major revision of yum is in use, which is required to determine module backend."

# Generated at 2022-06-13 11:24:20.437388
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test correct execution of run method
    # This method is called as a part of a task execution
    # and we need to mock task, loader and templar objects and
    # get the action plugin object based on them.
    pass # TODO

# Generated at 2022-06-13 11:24:29.262035
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.facts.system.pkg_mgr import get_pkg_mgr_facts

    # Test 1: test when module is auto and ansible_pkg_mgr is yum
    module_return_values = dict()
    module_return_values['ansible.legacy.setup'] = dict(
        ansible_facts=dict(
            ansible_pkg_mgr='yum'
        )
    )
    module_return_values['ansible.legacy.yum'] = dict(
        state='SUCCEEDED'
    )
    mocked_module_runner = MockedModuleRunner(module_return_values)


# Generated at 2022-06-13 11:24:31.987932
# Unit test for constructor of class ActionModule
def test_ActionModule():

    import ansible.plugins.action

    t = ansible.plugins.action.load_action_plugin("yum", action_base=ActionModule)
    a = t()
    assert not a.tranfers_files

# Generated at 2022-06-13 11:24:34.772318
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None)
    assert am is not None
    assert am._supports_async is True
    assert am._supports_check_mode is True

# Generated at 2022-06-13 11:25:37.753258
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = DummyModule(argument_spec=dict())
    action_plugin = ActionModule(module, 'TESTTMP',
                                 '/home/biplab/git/ansible/hacking/test_action_module/testexecdir')
    assert action_plugin.run() == dict(failed=True, msg="Could not detect which major revision of yum is in use, which is required to determine module backend.",
                                       changed=False, skipped=False)

# Generated at 2022-06-13 11:25:40.951141
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a class and check if it is an instance of the parent class.
    action_module = ActionModule({}, {}, [], True, [])
    assert isinstance(action_module, ActionBase)

# Generated at 2022-06-13 11:25:42.553337
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = module_loader.find_plugin('action')
    assert isinstance(m, object)

# Generated at 2022-06-13 11:25:51.274302
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for yum method run
    '''

    # creating instance of class ActionModule
    action_module_instance = ActionModule()

    # getting dictionary of ansible_facts
    ansible_facts_dictionary = dict(ansible_pkg_mgr="yum")

    # getting dictionary of task_vars
    task_vars_dictionary = dict(ansible_facts=ansible_facts_dictionary)

    # creating dictionary of module_args
    module_args_dictionary = dict(use="auto")

    # calling method run with parameters tmp, task_vars and play_context
    # returned value from method run
    result = action_module_instance.run(tmp="", task_vars="", task_vars=task_vars_dictionary, action_args=module_args_dictionary)

# Generated at 2022-06-13 11:26:04.445796
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFacts
    from ansible.module_utils.facts.system.pkg_mgr.yum import PkgMgrFactsYum
    from ansible.module_utils.facts.system.pkg_mgr.dnf import PkgMgrFactsDnf
    from ansible.module_utils.facts.system.pkg_mgr.package import PkgMgrFactsPackageYum
    from ansible.module_utils.facts.system.pkg_mgr.package import PkgMgrFactsPackageDnf
    from ansible.module_utils.facts.system.pkg_mgr.package_manager import PkgMgrFactsPackageManagerYum

# Generated at 2022-06-13 11:26:07.326158
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''
    action_module = ActionModule('task', 'connection', 'play_context', 'loader', 'templar', 'shared_loader_obj')
    assert action_module



# Generated at 2022-06-13 11:26:16.445746
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Unit test for constructor of class ActionModule"""

    # Constructing object

# Generated at 2022-06-13 11:26:24.891264
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    display = Display()
    display.verbosity = 4
    module_backend_plugins = [
        'setup',
        'file',
        'yum',
        'dnf',
        'yum3'
    ]
    # The tests need to run in order, so they're numbered 1 to X
    # Test 1
    # AnsibleTaskVars has ansible_pkg_mgr = 'yum'
    # Task args = auto
    # Returns 'yum'
    task_vars = {
        'ansible_facts': {
            'pkg_mgr': 'yum',
            'ansible_pkg_mgr': 'yum',
            'variables': {}
        },
    }
    args = {
        'use': 'auto',
    }
    action = ActionModule()
    action._task

# Generated at 2022-06-13 11:26:32.579444
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for the ansible.plugins.action.yum module
    '''

    task_vars = dict(ansible_facts=dict(pkg_mgr='yum'))
    tmp = '/tmp'
    task_vars = {}
    action_module = ActionModule(
        {'use': 'auto'}, tmp, task_vars, loader=None,
        templar=None, shared_loader_obj=None)

    display.debug("Trying with yum as ansible_facts.pkg_mgr")
    result = action_module.run(task_vars=task_vars)
    assert result.get("failed") is False

    display.debug("Trying with dnf(yum4) as ansible_facts.pkg_mgr")

# Generated at 2022-06-13 11:26:33.725016
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 'ActionModule' == ActionModule.__name__
    assert 'Module' in ActionModule.__doc__

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 11:28:29.776160
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    pass

# Generated at 2022-06-13 11:28:35.628555
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Create a ActionModule object
    test_object = ActionModule()

    result = test_object.run(
        tmp=None,
        task_vars={
            'ansible_pkg_mgr': 'yum'
        }
    )

    # Tests the result
    assert result['module_name'] == 'ansible.legacy.yum'
    assert 'ansible_facts' in result



# Generated at 2022-06-13 11:28:37.608380
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible import context

# Generated at 2022-06-13 11:28:43.735130
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.loader import action_loader
    task_vars = dict(
        ANSIBLE_MODULE_ARGS=dict(name="test", state="installed"),
        ansible_facts=dict(pkg_mgr="dnf")
    )
    action = action_loader.get('yum',
                               task=dict(action=dict(module='yum', args=dict(name="test", state="installed"))),
                               connection=dict(module='local', play_context=dict()),
                               shared_loader_obj=dict(module_loader=dict()),
                               variables=task_vars)
    action.validate_parameters()

# Generated at 2022-06-13 11:28:47.961896
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for the constructor of class ActionModule
    '''

    mock_templar = {'template': 'yum'}
    mock_task = {'args': {'use': 'yum'}}
    mock_basemodule = {'_execute_module': 'yum'}
    mock_shared_loader_obj = {'module_loader': {'has_plugin': 'yum'}}
    ActionModule(mock_templar, mock_task, mock_basemodule,
                 mock_shared_loader_obj)

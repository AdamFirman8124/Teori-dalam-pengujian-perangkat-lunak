

# Generated at 2022-06-13 11:18:53.703984
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, dict())

# Generated at 2022-06-13 11:19:04.385805
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    display.WARNINGS = True
    display.ERRORS = True
    display.DEBUGS = True
    display.DEPRECATIONS = True
    display.VERBOSITY = 5

    # task vars necessary to carry out test
    task_vars = {
        "ansible_pkg_mgr": "yum4",
        "ansible_facts": {"pkg_mgr": "dnf"}
    }

    # instance of the action module we are testing
    action_mod = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # test valid args for use_backend
    for argument in ["yum", "yum4", "dnf"]:
        args_dict = {
            "use_backend": argument
        }

# Generated at 2022-06-13 11:19:09.110325
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert a._supports_async
    assert a._supports_check_mode
    assert a.TRANSFERS_FILES



# Generated at 2022-06-13 11:19:15.077054
# Unit test for constructor of class ActionModule
def test_ActionModule():
    t = {
        'action': {
            'use': 'yum',
            'stamp': '/tmp/yum_stamp',
        },
        'ansible_job_id': '1',
        'ansible_facts': {'pkg_mgr': 'yum'},
    }

    actionmodule = ActionModule(None, t, None, None)
    result = actionmodule.run(None, None)
    assert result['msg'] == 'TASK FAILURE: module not implemented yet'

# Generated at 2022-06-13 11:19:23.350496
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import unittest

    reload(sys)
    sys.setdefaultencoding('utf8')

    print("Test processing class ActionModule method run")

    # set up test environment
    module = 'ansible.legacy.yum'
    sys.modules[module] = mock.Mock()
    sys.modules[module].ActionModule = ActionModule

    class MyTestCase(unittest.TestCase):
        '''Test class for ansible.plugins.action.yum'''

        def setUp(self):

            self.backends = {}
            for name in VALID_BACKENDS:
                backends[name] = mock.Mock()
                sys.modules[name] = backends[name]

        def tearDown(self):
            pass


# Generated at 2022-06-13 11:19:24.004841
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()

# Generated at 2022-06-13 11:19:32.737918
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import os
    import tempfile

    class MockTask:
        def __init__(self, args, async_val):
            self.args = args
            self.async_val = async_val

    class MockConnection:
        def __init__(self, shell_val):
            self._shell = shell_val

    class MockShell:
        def __init__(self):
            self.tmpdir = tempfile.mkdtemp()

    shell = MockShell()
    # create a file in our temporary path
    with open(os.path.join(shell.tmpdir, 'test_file'), 'w') as temp_file:
        temp_file.write('Test file\n')
    connection = MockConnection(shell)

# Generated at 2022-06-13 11:19:34.516975
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    :return:
    '''
    action_module = ActionModule()
    action_module.run()
    return

# Generated at 2022-06-13 11:19:37.303007
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert(ActionModule.__name__ == 'ActionModule')
    assert(ActionModule.__doc__ == 'Gathers package info from the local machine')
    assert(ActionModule.VALID_BACKENDS == frozenset(('yum', 'yum4', 'dnf')))



# Generated at 2022-06-13 11:19:46.213055
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Test ActionModule.run()"""
    from ansible.compat.tests.mock import patch
    from ansible.compat.tests.mock import MagicMock

    mock_tmplar = MagicMock()

    # Scenario 1 - 'use' is set to something valid.
    mock_task1 = MagicMock()
    mock_task1.args = {'use': 'yum', 'other': 'value'}
    mock_module_loader1 = MagicMock()
    mock_module_loader1.has_plugin.return_value = True
    mock_connection1 = MagicMock()
    mock_task_vars1 = {'ansible_pkg_mgr': 'yum'}
    test_module1 = ActionModule(mock_connection1)
    test_module1._task = mock_task

# Generated at 2022-06-13 11:19:55.447633
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_args = {}
    set_module_args(module_args)
    my_obj = ActionModule()
    rc = my_obj.run()
    print("rc:" + str(rc))



# Generated at 2022-06-13 11:19:59.638328
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.facts.system.pkg_mgr import PackageManager
    from ansible.plugins.action.yum import ActionModule

    tmp = None
    task_vars = {'ansible_facts': {'pkg_mgr': PackageManager()}}
    module = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=dict())

    assert module.run(tmp, task_vars)



# Generated at 2022-06-13 11:20:02.500975
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule()
    mod.run()

if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 11:20:11.173619
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    display = Display()


# Generated at 2022-06-13 11:20:12.455233
# Unit test for constructor of class ActionModule
def test_ActionModule():
  ret = ActionModule()
  assert ret is not None

# Generated at 2022-06-13 11:20:22.110740
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Arrange
    tmp = None
    task_vars = {'ansible_facts': {'pkg_mgr': 'auto', 'ansible_pkg_mgr': 'auto'}}
    task_args = {'use_backend': 'auto'}
    connection = None
    action = ActionModule(task=None, connection=connection, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Act
    with patch.object(ActionBase, 'run', return_value={'failed': False, 'ansible_facts': {'pkg_mgr': 'yum'}}):
        result = action.run(tmp=tmp, task_vars=task_vars)

    # Assert
    assert result['failed'] == False

# Generated at 2022-06-13 11:20:32.000152
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Test run"""
    m = ActionModule(None, None)

    for task in [dict(args=dict(use='yum')), dict(args=dict(use='dnf')), dict(args=dict(use='auto')), dict(args=dict(use='foo'))]:
        result, noop_result, delegate_to, delegate_facts = m._execute_module(None, task, dict(ansible_facts=dict(pkg_mgr='yum'))), dict(), 'server-1', True

# Generated at 2022-06-13 11:20:40.469189
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Creating mock variables for unit test
    mock_tmp = None
    mock_delegate_to = [{'ansible_lsb': {'distcodename': 'xenial', 'distid': 'Ubuntu', 'distrelease': '16.04',
                                                 'distshortcut': 'xenial',
                                                 'majdistrelease': '16.04', 'release': '16.04'}}]
    mock_task_vars = dict(ansible_pkg_mgr='auto', hostvars=mock_delegate_to)
    mock_module = 'auto'
    mock_facts = dict(ansible_facts=dict(ansible_pkg_mgr=mock_module))
    mock_file_local_path = '/tmp/foo'

# Generated at 2022-06-13 11:20:51.158827
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Setup a fake module config
    module_config = {
        'yum': ActionModule,
        'dnf': ActionModule,
        'auto': 'yum4'
    }

    # Setup a fake task
    task = {"args": {"use": "yum4"}, "delegate_to": "fakehost", "delegate_facts": False}

    # Setup a fake templar
    templar = FakeTemplar()

    # Setup a fake task
    connection = FakeConnection()

    # Create an instance of class ActionModule and run the method run.
    action_module = ActionModule()
    result = action_module.run(task_vars={"ansible_pkg_mgr": "auto"}, module_config=module_config, templar=templar, task=task, connection=connection)

    # Ass

# Generated at 2022-06-13 11:20:53.298956
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        ActionModule()
    except Exception:
        assert False, 'Unable to instantiate ActionModule'

# Generated at 2022-06-13 11:21:13.998453
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Fixture is a test object to parametrize. Because we need to test the
    # the `run` method of the class which accept two params which are not
    # really needed because they are Mock objects and we want to use
    # the values that are in the test_cases defined.
    fixture = ActionModule()
    data = [
            ('yum', {}, {'use': 'auto'}, 'yum'),
            ('yum', {'ansible_facts': {'pkg_mgr': 'yum'}}, {'use': 'auto'}, 'yum'),
            ('dnf', {'ansible_facts': {'pkg_mgr': 'dnf'}}, {'use': 'auto'}, 'dnf'),
            ]

# Generated at 2022-06-13 11:21:17.211140
# Unit test for constructor of class ActionModule
def test_ActionModule():
    current = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    assert VALID_BACKENDS == frozenset(('yum', 'yum4', 'dnf'))

# Generated at 2022-06-13 11:21:19.696565
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=dict(),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )

    assert module is not None

# Generated at 2022-06-13 11:21:28.717011
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = object.__new__(ActionModule)
    assert action._shared_loader_obj is None, "shared_loader_obj should be None"
    assert action._task is None, "task should be None"
    assert action._connection is None, "connection should be None"
    assert action._play_context is None, "play_context should be None"
    assert action._loader is None, "loader should be None"
    assert action._templar is None, "templar should be None"
    assert action._shared_loader_obj is None, "shared_loader_obj should be None"
    assert action._supports_check_mode is None, "supports_check_mode should be None"
    assert action._supports_async is None, "supports_async should be None"

# Generated at 2022-06-13 11:21:30.033110
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    raise NotImplementedError

# Generated at 2022-06-13 11:21:33.900048
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    action_module = ActionModule()
    assert isinstance(action_module, ActionModule)

# Generated at 2022-06-13 11:21:35.700072
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''Returns a new ActionModule object'''
    return ActionModule()

# Generated at 2022-06-13 11:21:38.509228
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a new ActionModule without arguments
    action_module = ActionModule()
    assert isinstance(action_module, ActionModule)



# Generated at 2022-06-13 11:21:47.914111
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import json
    import sys
    import tempfile
    import unittest

    class TestActionModule(ActionModule):

        def __init__(self):
            self._task = MockTask()
            self._connection = MockConnection()
            self._play_context = MockPlayContext()
            self._loader = MockLoader()
            self._shared_loader_obj = MockLoader(module_utils=[], paths=['/'])
            self._templar = MockTemplar()


# Generated at 2022-06-13 11:21:52.362155
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Initialize variables for unit test
    md = dict(foo='bar')
    ta = dict(foo='bar')
    tm = None
    td = None
    tt = None
    tk = None

    test = ActionModule(md, ta, tm, td, tt, tk)

    assert test._templar is not None
    assert test._shared_loader_obj is not None
    assert test._task_vars is None


# Generated at 2022-06-13 11:22:15.143845
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.executor import task_result
    from ansible.executor import task_result
    from ansible.playbook.task import Task
    from ansible.playbook.block import BroadcastBlock, HandlerBlock
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    class FakeOptions(object):
        def __init__(self, verbosity):
            self.connection = 'local'
            self.module_path = ''
            self.forks = 5
            self.become = False
            self.become_method = 'sudo'
            self.become

# Generated at 2022-06-13 11:22:24.195831
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.errors import AnsibleActionFail
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager

    action = action_loader.get('yum', class_only=True)

    action_plugin_instance = action()
    variable_manager = VariableManager()
    variable_manager.options._jid = 'aaa'

    class MockTask():
        async_val = False
        async_seconds = None
        async_poll_interval = 10
        async_notify = None
        args = {}
        delegate_to = None
        delegate_facts = False

    action_plugin_instance._task = MockTask()

    module = 'ansible.modules.packaging.os.yum'

# Generated at 2022-06-13 11:22:33.940330
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # pylint: disable=protected-access

    # test when module is auto
    am = ActionModule()

    am._task.args = dict(name="ansible-lint")
    am._templar = {"template": lambda x: "yum"}
    assert am.run(task_vars={})["ansible_facts"]["pkg_mgr"] == "yum"

    am._task.args = dict(name="ansible-lint")
    am._templar = {"template": lambda x: "yum"}
    am._task.delegate_to = "localhost"

# Generated at 2022-06-13 11:22:48.171412
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import tempfile
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import configparser

    config_data = StringIO()

    # Create a temporary configuration file with an empty defaults section.
    # The parser will throw a 'no section' error if the file has no [main]
    # section.
    config_data.write("\n[main]\n")
    config = configparser.RawConfigParser()
    config.readfp(config_data)
    config_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    config.write(config_file)
    config_file.close()

    # Invoke constructor using valid and invalid arguments

# Generated at 2022-06-13 11:22:50.921122
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO: For now, we're testing that the class' constructor can be called.
    # In the future, we should have more in-depth tests.
    myclass = ActionModule('test', 'test', 'test', 'test')
    assert myclass

# Generated at 2022-06-13 11:22:53.418206
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  """
  This method tests the run method of the ActionModule class
  """
  AnsibleModule = ActionModule()
  #assertion test
  assert AnsibleModule.run() == None

# Generated at 2022-06-13 11:23:02.288325
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('test run')
    import json
    testargs = {'use_backend': 'auto'}
    testansible_facts = {'pkg_mgr': 'yum'}
    result = {'ansible_facts': testansible_facts}
    testactionmodule = ActionModule({'loader': None, 'templar': None, 'connection': None, 'dc': None, 'task': None, 'task_vars': None, 'play_context': None, 'shared_loader_obj': None})
    testactionmodule._task.args = testargs
    testactionmodule._task.async_val = None
    testactionmodule._templar.template = lambda x: testansible_facts['pkg_mgr']
    testactionmodule._execute_module = lambda x, y, z: result
    assert json.d

# Generated at 2022-06-13 11:23:08.008505
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    results = ActionModule.run(
        ActionModule(),
        tmp='/var/tmp',
        task_vars={'ansible_pkg_mgr': 'yum'},
        delegate_to='localhost'
    )
    assert results['uses_delegate'] == True
    assert results['changed'] == False

# Generated at 2022-06-13 11:23:12.953288
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Unit test for constructor of class ActionModule"""

    action_module = ActionModule()
    assert isinstance(action_module, ActionModule)
    assert action_module.TRANSFERS_FILES is False
    assert action_module._supports_check_mode is True
    assert action_module._supports_async is True


# Generated at 2022-06-13 11:23:22.257977
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.six import PY2, PY3
    from ansible_collections.ansible.legacy.plugins.action.yum import ActionModule
    from ansible.module_utils.yum import Yum4
    from ansible.module_utils.yum import Yum
    from ansible.errors import AnsibleActionFail
    import os
    import sys
    import operator
    import collections
    import subprocess
    import ansible_module_yum

    if PY2:
        from StringIO import StringIO
    else:
        from io import StringIO

    # Override AnsibleActionFail with StringIO to catch error message if any
    old_stdout = sys.stdout
    sys.stdout = StringIO()

# Generated at 2022-06-13 11:23:50.662662
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:24:01.161844
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import sys
    import json
    import pytest
    import tempfile
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import StringIO

    from ansible.module_utils.six.moves import builtins
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import iteritems
    import ansible.module_utils.six.moves.configparser
    from ansible.module_utils.six.moves import input
    import ansible.module_utils.urls
    from ansible.module_utils._collections_compat import MutableMapping

# Generated at 2022-06-13 11:24:02.689789
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setup
    ACTION_MODULE = ActionModule()

    assert ACTION_MODULE.run()


# Generated at 2022-06-13 11:24:13.940337
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    from ansible.module_utils.basic import AnsibleFallbackNotFound
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.action import ActionBase
    import ansible.plugins.action.yum
    import ansible.plugins.action.dnf
    import ansible.plugins.action.apt
    import ansible.plugins.action.pacman
    import ansible.plugins.action.zypper
    import ansible.module_utils.facts.collector

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()


# Generated at 2022-06-13 11:24:15.285976
# Unit test for constructor of class ActionModule
def test_ActionModule():
    p = ActionModule()
    assert isinstance(p, ActionModule)

# Generated at 2022-06-13 11:24:25.862415
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = __import__('ansible.plugins.action.yum').plugins.action.yum.ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action_module._task = __import__('ansible.playbook.task').playbook.task.Task()
    action_module._task.async_val = False
    action_module._task.action = 'yum'
    action_module._task.args = {'use': 'auto'}
    action_module._task.delegate_to = None
    action_module._task.delegate_facts = True

# Generated at 2022-06-13 11:24:32.476468
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import os
    from ansible.module_utils._text import to_bytes

    class MockModule(object):
        def __init__(self, *args, **kwargs):
            self.args = args

    # Create a mock module

# Generated at 2022-06-13 11:24:37.416433
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(),
                        shared_loader_obj=dict())
    assert test.TRANSFERS_FILES == False
    assert test._supports_check_mode == True
    assert test._supports_async == True


# Generated at 2022-06-13 11:24:38.029524
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 11:24:52.490647
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_action_module = ActionModule(None, None, None, None, None, None)
    assert test_action_module.run() == {'failed': True, 'msg': 'Action plugin for yum3 vs yum4(dnf) operations. Enables the yum module to use yum3 and/or yum4. Yum4 is a yum\ncommand-line compatibility layer on top of dnf. Since the Ansible\nmodules for yum(aka yum3) and dnf(aka yum4) call each of yum3 and yum4\'s\npython APIs natively on the backend, we need to handle this here and\npass off to the correct Ansible module to execute on the remote system.'}

# Generated at 2022-06-13 11:25:54.142629
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

## Unit test case for clear_cache
test_cases = [

]


# Generated at 2022-06-13 11:26:05.808611
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Returns a dynamic test method with appropriate arguments
    # to be used as a test case where:
    # expected_result: dictionary with expected results to validate
    # module_args: dictionary with arguments to be passed to ansible module
    # mock_inject: list of mock objects to be injected (could be None)
    def dynamic_test_method(expected_result, module_args, mock_inject):
        action_module = ActionModule()
        action_module._shared_loader_obj = DummySharedLoaderObj()
        action_module._templar = DummyTemplarObj()
        action_module._task = DummyTaskObj()
        action_module._connection = DummyConnectionObj()
        action_module._task.async_val = None


# Generated at 2022-06-13 11:26:09.345535
# Unit test for constructor of class ActionModule
def test_ActionModule():
    act_mod = ActionModule()

    # test for valid instance
    assert isinstance(act_mod, ActionModule)

    # test for valid attributes
    assert hasattr(act_mod, 'run')

    # test for valid methods
    assert hasattr(act_mod.run, '__call__')


# test for invalid attributes

# Generated at 2022-06-13 11:26:18.215774
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ Unit test for constructor of class ActionModule """

    # Replace the built-in open
    if six.PY3:
        builtin_open = 'builtins.open'
    else:
        builtin_open = '__builtin__.open'
    mock_open = mock.mock_open()

# Generated at 2022-06-13 11:26:20.129183
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible_collections.ansible.legacy.plugins.action import yum
    action_module = yum.ActionModule()
    assert type(action_module) == ActionModule

# Generated at 2022-06-13 11:26:25.924456
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # setup pkg backend
    task = dict(name="/tmp/ansible_yum_payload_5XCe5M/yum", action=dict(module="yum", args=dict(disablerepo=None, enablerepo=None, exclude=None, install_repoquery=False, list=None, name=None, state="present", update_cache=False)))
    shared_loader_obj = None
    play_context = None
    connection = None
    temp_basedir = None
    task_vars = dict(ansible_pkg_mgr="dnf")
    result = dict(changed=False, failed=False, msg="")

    # test with module=auto
    module = "auto"
    action = ActionModule(task, shared_loader_obj, play_context, connection, temp_basedir)
   

# Generated at 2022-06-13 11:26:29.358774
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print('Testing ActionModule constructor')
    ActionModule(task = {'async_val': None, 'args': {'use': 'dnf'}, 'name': 'Install a package', 'action': 'dnf'}, connection = '', play_context = '', loader = '', templar = '', shared_loader_obj = '')

# Generated at 2022-06-13 11:26:37.650204
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create mocks of Task and PlayContext
    task = Task()
    playctx = PlayContext()
    fact_templar = FactTemplar()
    action_module = ActionModule(task, playctx, fact_templar)

    # Create mocks of facts returned by the setup module for specific linux distros
    fedora_fact = {u'ansible_facts': {u'pkg_mgr': u'YUM'}}
    centos_fact = {u'ansible_facts': {u'pkg_mgr': u'YUM'}}
    debian_fact = {u'ansible_facts': {u'pkg_mgr': u'apt'}}
    ubuntu_fact = {u'ansible_facts': {u'pkg_mgr': u'apt'}}

# Generated at 2022-06-13 11:26:44.415231
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    '''
    Unit tests for class ActionModule method run.

    NOTE: Unit tests are in alphabetical order by method name
    '''

    # Setup the class to unit test
    module = ActionModule()

    # Setup test case 1 for method run

    test_case_1_msg = 'Could not detect which major revision of yum is in use, which is required to determine module backend.'
    test_case_1_msg += ' You should manually specify use_backend to tell the module whether to use the yum (yum3) or dnf (yum4) backend})'

    test_case_1_expected_result = {'failed': True, 'msg': test_case_1_msg}

    test_case_1_tmp = None
    test_case_1_task_vars = None

    test_case_1_args

# Generated at 2022-06-13 11:26:46.523724
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(None, None, None)
    module.run(None, None)
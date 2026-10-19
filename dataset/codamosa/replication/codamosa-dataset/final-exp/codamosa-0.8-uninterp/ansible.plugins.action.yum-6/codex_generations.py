

# Generated at 2022-06-13 11:18:53.322902
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

if __name__ == "__main__":
    test_ActionModule_run()

# Generated at 2022-06-13 11:18:54.393529
# Unit test for constructor of class ActionModule
def test_ActionModule():
    x = ActionModule()
    assert isinstance(x, object)

# Generated at 2022-06-13 11:19:00.487131
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class MockTask:
        def __init__(self):
            self.args = {}
            self.async_val = "test"
            return

    class MockLoader:
        def __init__(self):
            self.all_vars = {}
            self.module_loader = None
            return

        def load_from_file(self, module_name):
            if module_name == 'ansible.legacy.dnf':
                return 1
            else:
                return None

    mock_loader = MockLoader()
    mock_task = MockTask()
    action_module = ActionModule(task=mock_task, connection=None, play_context=None, loader=mock_loader, templar=None, shared_loader_obj=None)
    action_module.run()

# Generated at 2022-06-13 11:19:03.146439
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule('setup', dict(filter='ansible_pkg_mgr', gather_subset='!all'), False, None)
    assert action is not None

# Generated at 2022-06-13 11:19:11.548069
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ##################################
    # make an instance of ActionModule
    ##################################
    am = ActionModule()
    # make a mock task with use_backend set to "yum" 
    args = {'use_backend': 'yum'}
    am._task = type('', (), {'args': args})()
    # make a mock self._execute_module
    am._execute_module = type('', (), {'module_name': 'ansible.modules.package_manager.yum', 'module_args': args})()
    # call run
    result = am.run()
    print(result)

# Generated at 2022-06-13 11:19:20.772482
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Use a ActionModule object to test the constructor of class ActionModule
    action_module = ActionModule(
        task=dict(name="test_ActionModule", args=dict(name='acs_agent')),
        connection=None,
        play_context=dict(check_mode=True),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert action_module._task.args['name'] == 'acs_agent'
    assert action_module._play_context.check_mode
    assert isinstance(action_module._loader, type(None))
    assert isinstance(action_module._templar, type(None))
    assert isinstance(action_module._shared_loader_obj, type(None))

# Generated at 2022-06-13 11:19:26.987065
# Unit test for constructor of class ActionModule
def test_ActionModule():
    yum_module = ActionModule()
    test_task = dict(
        action=dict(module_name="yum", args=dict(use_backend="yum4")))
    test_task_vars = dict(ansible_pkg_mgr="yum4")
    yum_module.run(task_vars=test_task_vars)

# Generated at 2022-06-13 11:19:32.894670
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(args={'name': 'emacs'}),
        connection=dict(transport='local'),
        play_context=dict(check_mode=True),
        loader=dict(mocked=True),
        shared_loader_obj=dict(mocked=True),
        templar=dict(mocked=True)
    )

    assert module._supports_check_mode is True
    assert module._supports_async is True
    assert module.VALID_BACKENDS == frozenset(['yum', 'yum4', 'dnf'])

# Generated at 2022-06-13 11:19:42.953674
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = dict(failed = True, msg = "this is the default")
    module = "yum4"
    ansible_facts = dict(pkg_mgr = module)
    module_return = dict(ansible_facts = ansible_facts, failed = False)
    class FakeTemplar:
        def template(self, name):
            return ansible_facts['pkg_mgr']

    class FakeActionBase:
        _task = None
        _templar = FakeTemplar()
        def __init__(self):
            self.results = result
            self.module_return = module_return

        def _execute_module(self, module_name, module_args, task_vars, wrap_async):
            return self.module_return


# Generated at 2022-06-13 11:19:50.499834
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import tempfile
    from ansible.plugins.action import ActionBase
    from ansible.utils.display import Display
    from ansible.module_utils._text import to_bytes

    # Create a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Create a temporary environment variable
    tmp_var_name = 'ANSIBLE_TRANSPORT'
    tmp_var_value = 'paramiko'
    os.environ[tmp_var_name] = tmp_var_value

    # Create a temporary file
    tmp_path_name = os.path.join(tmpdir, 'test')

# Generated at 2022-06-13 11:20:00.221218
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_obj = ActionModule(
        task=dict(action=dict(module_name="yum", module_args=dict(name="foo", state="present"))),
        connection="local",
        play_context=dict(check_mode=False),
        loader=None,
        templar=None,
        shared_loader_obj=None)

    assert action_obj._supports_check_mode == True
    assert action_obj._supports_async == True

# Generated at 2022-06-13 11:20:00.817363
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    assert action != None

# Generated at 2022-06-13 11:20:11.163049
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # test_case 1: module being called is not in VALID_BACKENDS
    test_case = 1
    module = "dnf"
    if module not in VALID_BACKENDS:
        print("Executing test_case: " + str(test_case))
        ansible_module = AnsibleActionModule()
        result = ansible_module.run()
        display.debug("Facts %s" % result)
        #assert result['msg'] == "Could not detect which major revision of yum is in use, which is required to determine module backend.", "Invalid result for test_case: " + str(test_case)
        #assert result['failed'] == True, "Invalid result for test_case: " + str(test_case)
        test_case += 1

# Generated at 2022-06-13 11:20:21.577729
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    task = dict(
        version=2,
        action=dict(
            module='yum',
            args=dict(),
            module_complex_args=dict()
        )
    )


# Generated at 2022-06-13 11:20:31.588146
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.action.yum import ActionModule
    from ansible.plugins.action.package_manager import ActionModule as package_manager
    import os

    my_task_args = {'use':'auto'}
    my_task_action = "yum"
    my_task_async = 20
    my_task_async_val = True
    my_task_delegate_to = "localhost"
    my_task_delegate_facts = True

    my_action_module_obj = ActionModule(
        task=None, connection=None, play_context=PlayContext(), loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 11:20:38.921647
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_text
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import action_loader

    config = dict(
        forks=10,
        become=None,
        become_method=None,
        become_user=None,
        check=False,
        diff=False,
        listhosts=None,
        listtasks=None,
        listtags=None,
        syntax=None,
        start_at_task=None,
    )

    context = PlayContext()
    context._protocol = 'ssh'

    # dummy values used for assertions below
    yum_backend_plugin_name = 'ansible.legacy.yum'
    dnf_backend_plugin_name = 'ansible.legacy.dnf'

# Generated at 2022-06-13 11:20:50.587898
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import tempfile
    from ansible.module_utils.six.moves import shlex_quote
    from ansible.module_utils._text import to_bytes

    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, MagicMock, mock_open, call

    from ansible.plugins.action import ActionBase

    from ansible.executor.play_iterator import PlayIterator
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins import module_loader

    class ActionModule(ActionBase):

        TRANSFERS_FILES = False

        def run(self, tmp=None, task_vars=None):
            return super(ActionModule, self).run(tmp, task_vars)


# Generated at 2022-06-13 11:20:54.638697
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Returns an instance of class ActionModule"""
    return ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 11:20:58.971981
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Test ActionModule class constructor

    Test that an ActionModule object is constructed properly.

    """
    tmp = None
    task_vars = {}
    action_module = ActionModule(tmp, task_vars)
    assert isinstance(action_module, ActionModule)
    assert action_module.TRANSFERS_FILES == False


# Generated at 2022-06-13 11:21:02.657618
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None)
    assert module is not None

# Generated at 2022-06-13 11:21:15.728196
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Access args passed in through the constructor or use default values
    assert ActionModule()._shared_loader_obj is not None



# Generated at 2022-06-13 11:21:22.853784
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.six import text_type
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.playbook.play import Play

    from ansible_collections.community.general.tests.units.compat.mock import patch
    from ansible_collections.community.general.plugins.modules.yum import ActionModule


# Generated at 2022-06-13 11:21:27.130418
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Run without fail
    module = ActionModule(dict(name="testname", args={}),
                          connection_info=dict(platform="testplatform"),
                          loader={"_shell": {"tmpdir": "tmpdirname"}})
    assert module._display.verbosity == 3
    assert module._supports_check_mode is True
    assert module._supports_async is True

# Generated at 2022-06-13 11:21:30.032626
# Unit test for constructor of class ActionModule
def test_ActionModule():

    module = ActionModule()

    assert module._supports_check_mode == True
    assert module._supports_async == True

# Generated at 2022-06-13 11:21:41.964756
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import pytest
    from ansible.plugins.action.yum import ActionModule
    from ansible_collections.ansible.legacy.plugins.module_utils._text import to_bytes
    from ansible.module_utils._text import to_text
    from ansible.plugins.loader import find_plugin
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.utils.vars import combine_vars

    # Args
    task_vars = dict()

    tmp = '/tmp'
    task_vars = VariableManager()
    task_vars.extra_vars = dict()
    loader = DataLoader()
    display = Display()

    # Test

# Generated at 2022-06-13 11:21:57.515700
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible
    from ansible.plugins.action import ActionBase
    from ansible.utils.loader import load_action_plugins

    class Fake_loader:

        def has_plugin(self, name):
            return True

    fake_loader = Fake_loader()
    action_paths = []


# Generated at 2022-06-13 11:22:07.272924
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()

    # Setup a fake class for task_vars and connection
    class FakeTaskVars:
        task_vars = {}
    class FakeConnection:
        _shell = FakeTaskVars()

    # Unit test for method run of class ActionModule
    # This test runs a yum module with yum3 as backend
    task_vars = FakeTaskVars()
    connection = FakeConnection()
    result = am._execute_module(module_name="ansible.legacy.yum", module_args=dict(name="fake_package", state="present"),
                                task_vars=task_vars, connection=connection)
    assert 'failed' in result
    assert not result['failed']

    # Unit test for method run of class ActionModule
    # This test runs a yum module with dnf as backend

# Generated at 2022-06-13 11:22:15.362063
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 11:22:24.438079
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # setup test variables
    action_plugin_object = ActionModule()

    # BEGIN unit test case 1:
    # test case 1: test run method with use_backend and use in args.
    # The run method should raise an exception because use_backend and use are mutually exclusive arguments

# Generated at 2022-06-13 11:22:25.279385
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()

# Generated at 2022-06-13 11:22:53.463876
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule('test', dict(test=True), False, '/tmp/ansible_action_plugin', False, False)
    assert isinstance(action_module, ActionModule)
    assert action_module._supports_check_mode == True
    assert action_module._supports_async == True
    assert action_module.TRANSFERS_FILES == False

# Generated at 2022-06-13 11:22:56.334764
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule(task=lambda: 0, connection=lambda: 0, play_context=lambda: 0, loader=lambda: 0, templar=lambda: 0)
    assert am.run(task_vars=[])

# Generated at 2022-06-13 11:22:59.439973
# Unit test for constructor of class ActionModule
def test_ActionModule():
    fake_task = {
        "args": {
            "name": "tree",
            "extra_packages": "tree"
        }
    }
    package_object = ActionModule()
    assert (isinstance(package_object, ActionModule))
    package_object._task = fake_task

# Generated at 2022-06-13 11:23:06.360386
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import os

    from ansible.plugins.action import ActionBase
    from ansible.utils.display import Display
    from ansible.vars import VariableManager
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector

    # Json contains a sample of input variables.
    # This sample is roughly similar to the real output of facts gathering.
    with open(os.path.join(os.path.dirname(__file__), 'yum_facts.json')) as f:
        facts = json.load(f)
    variables = VariableManager()
    variables.extra_vars = {'ansible_facts': {'ansible_check_mode': False}, 'ansible_pkg_mgr': 'auto'}
    display = Display()

# Generated at 2022-06-13 11:23:07.101774
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:23:12.432238
# Unit test for constructor of class ActionModule
def test_ActionModule():
    obj = ActionModule()
    assert isinstance(obj, ActionModule)
    assert not hasattr(obj, '_supports_check_mode')
    assert not hasattr(obj, '_supports_async')
    assert not isinstance(obj, ActionBase)
    assert obj.run() == {'failed': True}

# Generated at 2022-06-13 11:23:21.791517
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def get_args(params):
        args = {}
        for param in params:
            args[param['key']] = param['value']
        return args

    args = get_args([{'key': 'use_backend', 'value': 'yum'},
                     {'key': 'use', 'value': 'dnf'},
                     {'key': 'name', 'value': 'httpd'}])

    action = yum.ActionModule(task=dict(args=args), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # test fail

# Generated at 2022-06-13 11:23:22.605140
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 11:23:34.777820
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFacts
    from ansible.utils.context_objects import wrap_context

    class DummyVarsModule(object):
        def __init__(self):
            self.ansible_facts = {}

    class DummyTaskModule(object):
        def __init__(self):
            self.args = {}

    with wrap_context(DummyVarsModule()) as ctx2:
        with wrap_context(DummyTaskModule()) as ctx3:
            pmf = PkgMgrFacts()
            pmf.collect(None, None)

# Generated at 2022-06-13 11:23:43.552365
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 11:24:31.744375
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 11:24:32.323396
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()

# Generated at 2022-06-13 11:24:42.911446
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    localhost = dict(ansible_connection='local')
    somehost = dict(ansible_connection='somehost')

    # set up mock objects
    tmp_path = "/tmp/tests/tmp.file"


# Generated at 2022-06-13 11:24:45.009246
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule('action_plugins/yum.py', 'fake/path', {}, False, '/dev/null', 1, True)
    assert action_module

# Generated at 2022-06-13 11:24:53.401886
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json
    import tempfile
    import shutil
    import sys

    from ansible.plugins.action import ActionBase

    # Constructor test
    action_plugin = ActionModule('setup', '', 10, {}, False, None, '/dev/null', None, tempfile.mkdtemp())

    assert action_plugin is not None

    # Unit test for run

# Generated at 2022-06-13 11:24:59.199825
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(action=dict(module_name=dict(use='yum'), module_args=dict(use_backend='yum3'))),
        connection=dict(host=dict(name='test'), shared_loader_obj='test_loader'))
    assert module.VALID_BACKENDS == frozenset(('yum', 'yum4', 'dnf'))
    assert module.TRANSFERS_FILES is False
    assert module.display is not None
    assert module.run() is not None

# Generated at 2022-06-13 11:25:05.288579
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    '''
    Unit test for method run of class ActionModule.
    '''

    # We need to know this information in order to check that we will
    # find a YUM module backend.
    ansible_path = os.environ.get("ANSIBLE_LIBRARY")
    if not ansible_path:
        # Default for the installed system
        ansible_path = "/usr/share/ansible"

    # Create a test ActionModule class
    class TestActionModuleClass(ActionModule):
        def __init__(self, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None):
            # Prevent a dependency on the "action" module
            self._supports_async = False
            self._task = task
            self._connection = connection
            self

# Generated at 2022-06-13 11:25:11.124392
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    This tests the logic of the run method within the
    ansible.plugins.action.yum_select plugin.

    In this test we need to:
     - Test that use is mutually exclusive with use_backend
     - Test that the action fails when ansible_pkg_mgr is not in the facts
    """
    # Test 1
    # Test that use is mutually exclusive with use_backend

# Generated at 2022-06-13 11:25:22.454648
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.utils.template
    from ansible.utils.display import Display
    from ansible.plugins.action.yum import ActionModule
    from ansible.module_utils.six import PY3
    from ansible.utils.path import unfrackpath

    def _mark_no_log_values(self, result):
        return result

    display = Display()
    display.mark_no_log_values = _mark_no_log_values


# Generated at 2022-06-13 11:25:29.762787
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # fake_task_vars is common among all the tests of this module
    fake_task_vars = {'ansible_pkg_mgr': 'yum'}

    # Test 1
    test_inst = ActionModule(dict(), dict())
    test_inst.runner = dict()
    test_inst.runner._shared_loader_obj = dict()
    test_inst.runner._shared_loader_obj.module_loader = dict()
    test_inst.runner._shared_loader_obj.module_loader.has_plugin = lambda x:True
    test_inst._execute_module = lambda x, y, z, w: dict()
    test_inst._task = dict()
    test_inst._task.args = {'use': 'auto'}

# Generated at 2022-06-13 11:27:18.691777
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(1, 1)
    assert module._supports_check_mode
    assert module._supports_async
    assert getattr(module, '_ActionBase__task') == 1
    assert getattr(module, '_shared_loader_obj') == 1
    assert getattr(module, '_remove_tmp_path')



# Generated at 2022-06-13 11:27:31.245786
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict()
    tmp = None

    # Case 1: yum3 is installed on system
    mock_task = Mock()
    mock_task.args = dict(use_backend='auto')
    mock_task.delegate_to = ''
    mock_task.delegate_facts = True
    mock_task.async_val = 0
    mock_task_vars = dict()
    mock_task_vars['ansible_facts'] = dict()
    mock_task_vars['ansible_facts']['pkg_mgr'] = "yum"
    mock_task_vars['ansible_facts']['yum_distribution_major_version'] = "8"

    action_module = ActionModule(None, mock_task, tmp, mock_task_vars)

# Generated at 2022-06-13 11:27:37.821723
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create an instance of class ActionModule
    action = ActionModule()

    # test invaid values in the argument module
    result = action.run(tmp='tmp', task_vars='task_vars')
    assert (result['failed'] == True)

    result = action.run(tmp='tmp', task_vars='task_vars')
    assert (result['failed'] == True)

    result = action.run(tmp='tmp', task_vars='task_vars')
    assert (result['failed'] == True)

# Generated at 2022-06-13 11:27:43.425988
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('test_ActionModule_run')
    import ansible.plugins.action.yum as yum
    test = yum.ActionModule()
    module = 'dnf'
    # new_module_args={'name': 'kernel', 'state': 'latest'}
    new_module_args = {'name': 'kernel'}
    result = test.run(module, new_module_args)
    print(result)

# Generated at 2022-06-13 11:27:51.528580
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()

    # Test with 'use' attribute in args
    test_args = {'use': 'yum',
                 'name': 'example_pkg'
                }

    # Make test_vars None
    test_vars = None

    assert action_module.run(None, test_vars) != None

    # Test with 'use' attribute in args
    test_args = {'use': 'yum',
                 'name': 'example_pkg'
                }

    # Make test_vars not None
    test_vars = {'ansible_facts': {'pkg_mgr': 'yum'}}

    assert action_module.run(None, test_vars) != None

    # Test with 'use_backend' attribute in args

# Generated at 2022-06-13 11:27:53.779258
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create an instance of the class ActionModule
    unit = ActionModule()
    # Check if the instance has the name ActionModule
    assert unit.__class__.__name__ == 'ActionModule'

# Generated at 2022-06-13 11:27:56.978731
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    assert action_module.CONNECTION_PLUGIN_FOR_BECOME == "runas"
    assert action_module.SUPPORTED_HOOK_TYPES == frozenset(("async", "connection"))
    assert action_module.TRANSFERS_FILES == False

# Generated at 2022-06-13 11:27:57.716359
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True



# Generated at 2022-06-13 11:27:58.929148
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    print(action)

# Generated at 2022-06-13 11:28:07.310356
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test for method run of class ActionModule'''
    import unittest
    import tempfile
    import shutil
    import os
    import sys
    import importlib
    import json

    class TestActionModule(unittest.TestCase):
        '''Unit test for class ActionModule'''
        def setUp(self):
            self.test_dir = tempfile.mkdtemp()
            self.maxDiff = None
            self._load_module_util()

        def tearDown(self):
            shutil.rmtree(self.test_dir)

        def _load_module_util(self):
            test_dir = os.path.dirname(__file__)
            sys.path.insert(0, test_dir)
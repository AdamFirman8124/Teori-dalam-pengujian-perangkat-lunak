

# Generated at 2022-06-13 11:18:57.157824
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #  Test for the run method of ActionModule class

    import os

    # This is the current Ansible directory.
    ansible_dir = os.path.dirname(os.path.realpath(__file__))

    # Add the Ansible directory to module path.
    module_utils_path = os.path.join(ansible_dir, 'module_utils')
    sys.path.append(module_utils_path)

    # Create an instance of the class ActionModule
    action_module = ActionModule()

    # Create a temporary Ansible facts directory.
    ansible_facts_dir = tempfile.mkdtemp()
    print("ansible_facts_dir : %s" % ansible_facts_dir)

    # Set an Ansible facts path.
    os.environ['ANSIBLE_LOCAL_TMP'] = ans

# Generated at 2022-06-13 11:18:59.633740
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Constructor of class ActionModule without parameters
    tmp_action_module = ActionModule()
    assert tmp_action_module is not None

# Generated at 2022-06-13 11:19:00.644657
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()
    assert a is not None

# Generated at 2022-06-13 11:19:05.122235
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult

    task_result = TaskResult(host=None, task=Task(), return_data=dict(failed=False))
    am = ActionModule(task=task_result, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    am.run(tmp=None, task_vars=dict(ansible_facts=dict(pkg_mgr="yum")))
    # am.run()
    pass

# Generated at 2022-06-13 11:19:15.167842
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Setting up test
    module = ActionModule(load_collect_fixture('yum_repo_info'))
    module._task.args = {'a': 'b'}
    module._task.delegate_to = 'localhost'
    module._task.delegate_facts = True

    # Test cases
    # Case 1: module = auto; ansible_facts.pkg_mgr = 'yum'
    mock_facts = load_collect_fixture('setup_module_return_facts')
    mock_facts['ansible_facts']['pkg_mgr'] = 'yum'
    module._templar.template = MagicMock(return_value='auto')
    module._execute_module = MagicMock(return_value=mock_facts)
    result = module.run()

# Generated at 2022-06-13 11:19:23.425518
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test ActionModule with use_backend parameter set to 'yum' or 'dnf' or 'auto'
    def mock_actionbase_run(self, tmp=None, task_vars=None):
        return {'ansible_facts': {'pkg_mgr': 'auto'}}
    ActionBase.run = mock_actionbase_run
    module = "ansible.legacy.yum"
    new_module_args = {
        'use': 'yum'
    }
    result = ActionModule().run(tmp=None, task_vars=None)
    del ActionBase.run
    assert module == result['ansible_facts']['pkg_mgr']
    result = ActionModule().run(tmp=None, task_vars=None)

# Generated at 2022-06-13 11:19:32.414280
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.display import Display
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    import ansible.constants as C
    import json
    import sys

    class Task(object):
        def __init__(self, args):
            self.args = args

    class Playbook(object):
        def __init__(self, tasks):
            self.tasks = tasks


# Generated at 2022-06-13 11:19:41.409451
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.loader as plugins
    action = plugins.action_loader.get('yum', class_only=True)
    action_module = plugins.action_loader.get('yum', class_only=False)

    assert not action.run('auto', task_vars=None)
    assert not action.run('manual', task_vars=None)
    assert not action.run('yum', task_vars=None)
    assert not action.run('yum4', task_vars=None)
    assert not action.run('dnf', task_vars=None)
    assert not action.run('yum5', task_vars=None)

# Generated at 2022-06-13 11:19:47.340964
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''
    # Provision of mock object
    mock_connection = {}
    mock_task = {}
    mock_task.__dict__ = {'args': {}}

    # Construction of object
    test_obj = ActionModule(mock_connection, mock_task)

    # Assertion of object attributes
    assert test_obj._supports_check_mode is True
    assert test_obj._supports_async is True
    assert test_obj._task.__dict__ == {'args': {}}


# Generated at 2022-06-13 11:19:58.511060
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class Options:
        def __init__(self):
            self.connection = 'smart'
            self.accelerate = False
            self.async_val = False
            self.no_log = False

    class Task:
        def __init__(self):
            self.args = {'use': 'yum4'}

    class Play:
        pass

    class PlayContext:
        def __init__(self):
            self.become = False
            self.become_method = 'sudo'
            self.become_user = 'root'

    class Connection:
        class _shell:
            tmpdir = 'test'

    module = ActionModule(connection=Connection(), play=Play(), play_context=PlayContext(), task=Task(), loader=Options(), templar=Options())

    # Validate results

# Generated at 2022-06-13 11:20:08.557859
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule.
    '''
    # Create an instance of class ActionModule.
    action_module_instance = ActionModule()
    # Test method run.
    action_module_instance.run()

# Generated at 2022-06-13 11:20:09.025659
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:20:15.908681
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module_instance = ActionModule()

    tasks = dict(
        action=dict(
            args=dict(
                use='yum'
            )
        )
    )

    task_vars = dict()

    action_module_instance._load_task_vars(task_vars)
    action_module_instance._task = tasks
    action_module_instance._supports_check_mode = True
    action_module_instance._supports_async = True
    action_module_instance._execute_module = lambda x, y, z: dict(msg='success')
    action_module_instance._remove_tmp_path = lambda x: None
    action_module_instance._connection = False

    result = action_module_instance.run()

# Generated at 2022-06-13 11:20:25.030141
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a class object of ActionModule
    action_module = ActionModule(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(),
                                 shared_loader_obj=dict())

    # Create a class object of Display()
    display = Display()
    display.verbosity = 4

    # Create an object of AnsibleActionFail
    ansible_action_fail = AnsibleActionFail('test ansible action fail')

    # Create a class object of ActionBase
    action_base = ActionBase(task=dict(), connection=dict(), play_context=dict(), loader=dict(), templar=dict(),
                             shared_loader_obj=dict())

    # Create a class object of ActionBase for _execute_module

# Generated at 2022-06-13 11:20:31.505514
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m_shared_loader_obj = None
    m_connection = None
    m_task_vars = {}
    action_mod = ActionModule(m_shared_loader_obj, m_connection, m_task_vars)

    for name in VALID_BACKENDS:
        action_mod._task.args = dict(use_backend=name)
        action_mod.run(None, None)

    action_mod._task.args = dict(use=name)
    action_mod.run(None, None)

# Generated at 2022-06-13 11:20:32.865562
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(None, None)
    module.run()

# Generated at 2022-06-13 11:20:33.448926
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 11:20:34.375906
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.__name__ == 'ActionModule'

# Generated at 2022-06-13 11:20:35.437286
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 11:20:40.910509
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 11:20:55.110568
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ActionModule.run("tmp", "task_vars")

# Generated at 2022-06-13 11:20:58.735930
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = dict(name='action_plugin_test', action=dict(module='yum', args='foo=1', use='yum3'))
    result = ActionModule(task, dict()).run(None, dict())
    assert not result.get('failed')
    assert result['action_plugin_backend_module'] == 'yum3'

# Generated at 2022-06-13 11:21:08.555514
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.module_utils.six import PY2, PY3

    import os
    import sys
    import types

    if PY2:
        test_dir = os.path.dirname(os.path.abspath(__file__))
        module_utils_path = os.path.join(test_dir, '../../lib/ansible/module_utils')
        sys.path.insert(0, module_utils_path)
    else:
        module_utils_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Generated at 2022-06-13 11:21:17.199337
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible_collections.community.general.tests.unit.compat.mock import (
        patch,
        MagicMock,
    )
    from ansible_collections.community.general.plugins.modules.package_manager import yum as yum3

    # simple test mocking the anssible module execution
    def mock_module_execution(*args, **kwargs):
        return ({
            "msg": "Executed the mock_module",
            "failed": False
        }, None)


# Generated at 2022-06-13 11:21:23.849813
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Check if ActionModule.run method returns the right values"""

    import uuid

    test_str = str(uuid.uuid1())
    display.verbosity = 4

    module_mocker = Mocker()
    module_class_mocker = Mocker()
    module_mock = module_class_mocker.mock()
    module_mock.run(ANY)
    module_mocker.result({"stdout": test_str})
    module_mocker.count(0, None)
    module_class_mocker.replay()

    display_mocker = Mocker()
    display_mock = display_mocker.mock()
    display_mock.display(ANY)
    display_mocker.result(None)
    display_mocker.count(0, None)
    display_m

# Generated at 2022-06-13 11:21:35.265569
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    results = m.run(task_vars={'ansible_pkg_mgr': 'yum'})
    assert results['msg'] == 'Could not find a yum module backend for yum.'

    results = m.run(task_vars={'ansible_pkg_mgr': 'yum4'})
    assert results['msg'] == 'Could not find a yum module backend for dnf.'

    results = m.run(task_vars={'ansible_pkg_mgr': 'yum3'})
    assert results['msg'] != 'Could not find a yum module backend for dnf.'

# Generated at 2022-06-13 11:21:36.500502
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None, 'ActionModule is None'

# Generated at 2022-06-13 11:21:37.381065
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.TRANSFERS_FILES == False


# Generated at 2022-06-13 11:21:42.342933
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Get test class fixture
    ActionModule_class_instance = ActionModule(ActionBase())
    ActionModule_class_instance._task = None

    # Test if instance is of type ActionModule
    assert isinstance(ActionModule_class_instance, ActionModule)

    # Test known return value
    assert ActionModule_class_instance.run() == True


# Generated at 2022-06-13 11:21:46.881291
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert actionmodule.TRANSFERS_FILES == False

# Generated at 2022-06-13 11:22:12.765954
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 11:22:16.836881
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module._supports_check_mode == True
    assert action_module._supports_async == True
    assert action_module.TRANSFERS_FILES == False

# Generated at 2022-06-13 11:22:24.756742
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    result = {
        'ansible_facts': {
            'pkg_mgr': 'yum'
        }
    }
    get_ansible_facts_typed_to_dict_result = {
        'ansible_facts': {
            'pkg_mgr': 'yum'
        }
    }
    task_vars = {
        'ansible_facts': {
            'pkg_mgr': 'yum'
        }
    }
    action_module = ActionModule()
    # Test if is an instance of class ActionModule
    assert isinstance(action_module, ActionModule)
    # Test if method run return what is expected
    assert action_module.run(task_vars=task_vars) == result

# Generated at 2022-06-13 11:22:31.640548
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    ''' This test is to test the functionality of
        method `run` of class `ActionModule`
    '''
    import sys
    if sys.version_info.major < 3:
        import __builtin__ as builtins
    else:
        import builtins

    if 'ansible_facts' in builtins.__dict__:
        builtins.__dict__['ansible_facts'] = {}
    result = {
        '_ansible_verbose_always': None,
        '_ansible_no_log': None,
        'ansible_facts': {'pkg_mgr': 'dnf'},
        'ansible_facts': {'pkg_mgr': 'yum'},
        '_ansible_no_log': None
    }

    if sys.version_info.major < 3:
        mock

# Generated at 2022-06-13 11:22:44.167631
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # a dictionary of input arguments for testing
    setup_args = {
        'use_backend': 'auto',
        'use': 'auto',
        'state': 'present',
        'name': ['kernel', 'vim', 'curl'],
        'disable_gpg_check': True,
        'install_repoquery': True,
        'update_cache': True,
        'clean_requirements_on_remove': False,
        'validate_certs': True,
    }

    # instantiate a mock for the module class
    action_module_mock = ActionModule()
    # instantiate a mock for the display class
    display_mock = Display()

    # create a mock for the templar class
    templar_mock = MagicMock()
    action_module_mock._templar

# Generated at 2022-06-13 11:22:51.370079
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mock_task = type('MockTask', (object,), {
        'args': {'use_backend': 'yum4'},
        'async_val': False,
        'delegate_facts': True,
        'delegate_to': None,
    })
    action = ActionModule(mock_task, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert(action._task.async_val == False)
    assert(action._task.delegate_facts == True)
    assert(action._task.delegate_to == None)
    assert(action._task.args['use_backend'] == 'yum4')
    return True


# Generated at 2022-06-13 11:22:52.737432
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''
    pass

# Generated at 2022-06-13 11:22:54.548537
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None, None)
    assert isinstance(action, ActionBase)

# Generated at 2022-06-13 11:22:58.183003
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    t = Task()
    v = VariableManager()

    am = ActionModule(t, v)

    assert am._supports_async is True
    assert am._supports_check_mode is True

# Generated at 2022-06-13 11:22:59.023438
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # implement unit test here
    pass

# Generated at 2022-06-13 11:24:00.827183
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible import context
    from ansible.utils.vars import merge_hash
    from ansible.module_utils._text import to_text

    import ansible.plugins.action.yum


    ACTION_PLUGIN_PARAMS = {'dest': '/tmp/test'}
    class TestActionModule(ansible.plugins.action.yum.ActionModule):
        """
        This action plugin class provides a test function, which is
        supposed to return the value of its argument as a string
        """
        def test(self, arg):
            return to_text("{0}".format(arg), errors='surrogate_or_strict')

    _task = ansible.playbook.task.Task()
    _task.args = ACTION_PLUGIN_PARAMS

# Generated at 2022-06-13 11:24:02.647498
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, MockTask(), MockLoader(), MockConnection())
    assert type(action) == ActionModule


# Generated at 2022-06-13 11:24:03.577983
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False

# Generated at 2022-06-13 11:24:04.252095
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert 1

# Generated at 2022-06-13 11:24:07.366067
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 11:24:16.286251
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 11:24:18.420834
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    action_plugins.yum_select unit test stub
    '''
    pass

# Generated at 2022-06-13 11:24:27.928725
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action = ActionModule(None, None, None, None)

    test_cases = dict()

    test_cases['case 1'] = dict()
    test_cases['case 1']['delegate_to'] = None
    test_cases['case 1']['delegate_facts'] = None
    test_cases['case 1']['_task_args'] = None
    test_cases['case 1']['_task_async_val'] = None
    test_cases['case 1']['_task_async_val'] = None
    test_cases['case 1']['_loader_obj'] = None
    test_cases['case 1']['_templar_obj'] = None
    test_cases['case 1']['_display_obj'] = None

# Generated at 2022-06-13 11:24:31.958359
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Unit test for constructor of class ActionModule
    assert ActionModule.__name__ == 'ActionModule'

    # Unit test the result of run to check 'failed' and 'msg' in the result
    am = ActionModule()
    assert am.run(None, None) == {'failed': True, 'msg': "Could not detect which major revision of yum is in use, which is required to determine module backend.", 'msg': "You should manually specify use_backend to tell the module whether to use the yum (yum3) or dnf (yum4) backend"}

# Generated at 2022-06-13 11:24:39.503077
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    display = Display()
    display.verbosity = 4
    display.debug("Running unit test for yum3 vs yum4(dnf) operations.")
    display.debug("ActionModule._supports_check_mode = True")
    display.debug("ActionModule._supports_async = True")
    task_vars = {'ansible_facts': {'ansible_pkg_mgr': 'yum'}}
    tmp = 'temp_output'
    display.debug("ActionModule.run(tmp, task_vars)")

# Generated at 2022-06-13 11:26:27.398053
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()
    task_vars = {'ansible_pkg_mgr': 'yum'}
    assert action_module._execute_module(module_name="yum", module_args=dict(name='httpd'), task_vars=task_vars)

# Generated at 2022-06-13 11:26:32.585848
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.common.text.converters import to_native
    from ansible.plugins.action.yum import ActionModule

    import sys
    import os

    fake_os = ImmutableDict({'PATH': '/usr/bin'})

    class FakeModule_load_plugin():
        def has_plugin(self, name):
            if name == 'ansible.legacy.yum':
                return True
            return False

    fake_ansible_facts = ImmutableDict({'pkg_mgr': 'yum'})

    class FakeModule_execute_module():
        @staticmethod
        def run_command(cmd, check_rc=True):
            mock_command = " ".join(cmd)
            assert mock_command

# Generated at 2022-06-13 11:26:36.335973
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.modules.package_manager.yum
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    task = Task()
    task.args = dict()

    play_context = PlayContext()
    play_context.check_mode = True
    task._play_context = play_context
    module_obj = ansible.modules.package_manager.yum.ActionModule(task, {}, {})


# Generated at 2022-06-13 11:26:39.984631
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

# Generated at 2022-06-13 11:26:45.920935
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_args = {}
    am = ActionModule(None, module_args, None)
    assert am._supports_check_mode is True
    assert am._supports_async is True


if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 11:26:47.739932
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actmod = ActionModule(None, None)
    assert VALID_BACKENDS == actmod.VALID_BACKENDS

# Generated at 2022-06-13 11:26:57.051965
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''

    # initialization of class ActionModule with its constructor
    action_module = ActionModule()

    # testing its return value - default should be 'auto'
    assert action_module._task.args.get('use', action_module._task.args.get('use_backend', 'auto')) == 'auto'

    # testing its return value
    assert action_module.VALID_BACKENDS == frozenset(('yum', 'yum4', 'dnf'))



# Generated at 2022-06-13 11:27:10.669136
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.facts.system.pkg_mgr import PkgMgrFactCollector
    from ansible.module_utils.facts.system.pkg_mgr.yum.yum_backend_test_fixtures import YumBackendSetupTestFixture

    # make sure we have no unexpected facts
    test_fixture = YumBackendSetupTestFixture()
    test_fixture.setUp()

    # test yum3 backend
    test_facts = PkgMgrFactCollector.collect(module=MockModule(), collector=PkgMgrFactCollector.name)

    assert "ansible_pkg_mgr" in test_facts, "test_facts: %s" % test_facts

# Generated at 2022-06-13 11:27:11.455436
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 11:27:27.082903
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # yum3, yum4, dnf
    assert ActionModule.run(dict(use='yum4')) == "dnf"
    assert ActionModule.run(dict(use_backend='yum4')) == "dnf"

    # default value auto
    assert ActionModule.run(dict()) == "auto"
    assert ActionModule.run(dict(use='auto')) == "auto"
    assert ActionModule.run(dict(use_backend='auto')) == "auto"

    # We don't have facts from facts module in this unit test
    # Need to extract facts from facts module !
    # assert ActionModule.run(dict(use='auto')) == "yum"
    # assert ActionModule.run(dict(use_backend='auto')) == "yum"
    # assert ActionModule.
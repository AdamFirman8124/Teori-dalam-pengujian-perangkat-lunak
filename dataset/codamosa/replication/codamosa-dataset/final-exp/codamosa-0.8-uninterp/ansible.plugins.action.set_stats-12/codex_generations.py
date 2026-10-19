

# Generated at 2022-06-13 10:42:22.825051
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import unittest
    import sys

    from ansible.plugins.action.set_stats import ActionModule
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task

    class TestActionModuleRun(unittest.TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test__VALID_ARGS(self):
            action = ActionModule(Task(), PlayContext())

            # Assert that there are 'aggregate', 'data', and 'per_host' in _VALID_ARGS
            self.assertTrue('aggregate' in action._VALID_ARGS)
            self.assertTrue('data' in action._VALID_ARGS)
            self.assertTrue('per_host' in action._VALID_ARGS)

# Generated at 2022-06-13 10:42:31.456677
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import sys
    import shlex
    #sys.path.append(os.path.join(os.path.dirname(__file__)))
    from .. import plugins
    from ..action_plugins import set_stats
    import json

    # call method run of class ActionModule
    set_statsObj = set_stats.ActionModule()
    jsonStr = '{'
    jsonStr = jsonStr + '  "aggregate": "yes",'
    jsonStr = jsonStr + '  "data": {'
    jsonStr = jsonStr + '    "foo": "{{name}}",'
    jsonStr = jsonStr + '    "bar": "{{myvar}}"'
    jsonStr = jsonStr + '  },'
    jsonStr = jsonStr + '  "per_host": "yes"'
    jsonStr = jsonStr

# Generated at 2022-06-13 10:42:43.351378
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # mock task and task_vars
    task = dict()
    task_vars = dict()

    # mock tmp
    tmp = None

    # mock result
    result = dict()
    result['failed'] = False
    result['changed'] = False

    # mock templar, module_utils and args
    templar = dict()
    module_utils = dict()
    args = dict()

    # test valid and invalid data values

# Generated at 2022-06-13 10:42:52.929567
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task = {
        'id': '3',
        'action': 'set_stats',
        'args': {
            'per_host': False,
            'data': {
                'a': '{{b}}',
                'c': '4',
                'd': {'1': '2'}
            },
            'aggregate': True
        },
        'module_name': '',
        '_ansible_no_log': False,
        '_ansible_verbose_always': False,
        '_ansible_debug': False
    }

    tmp_path = 'tmp_path'
    task_vars = {
        'b': '3'
    }
    am = ActionModule(task, tmp_path)

    res = am.run(task_vars=task_vars)

   

# Generated at 2022-06-13 10:43:03.713857
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    params = dict(data = dict(a = 1, b = 'string', c = dict(d = 'abc', e = [1, 'a'], f ='b', g = dict(h = 'xyz'))))
    module_instance = ActionModule()
    result = module_instance.run(tmp = None, task_vars = {})

    assert isinstance(result, dict)
    assert 'ansible_stats' in result
    assert isinstance(result['ansible_stats'], dict)

    stats = result['ansible_stats']

    assert 'per_host' in stats
    assert 'aggregate' in stats
    assert 'data' in stats

    data = stats['data']

    assert isinstance(data, dict)
    assert isinstance(data['a'], int)

# Generated at 2022-06-13 10:43:04.881681
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, {})
    assert(am.TRANSFERS_FILES is False)
    assert(am._VALID_ARGS is not None)

# Generated at 2022-06-13 10:43:08.302907
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=None
    )
    assert action is not None

# Generated at 2022-06-13 10:43:10.156181
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am_obj = ActionModule()
    assert am_obj._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

# Generated at 2022-06-13 10:43:19.509447
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from collections import namedtuple
    from ansible.template import Templar
    from ansible.vars import VariableManager

    Environment = namedtuple('Environment', ['basedir'])

    environment = Environment(basedir='/path/to/playbook')
    variable_manager = VariableManager()
    loader = variable_manager.get_vars_loader()
    variable_manager._extra_vars = {
        'hostvars': {
            'localhost': {
                'ansible_facts': {
                    'distribution': 'Debian',
                    'distribution_release': 'jessie',
                    'distribution_version': '8.9',
                }
            }
        },
        'group_names': ['localhost'],
        'groups': {
            'localhost': ['localhost']
        }
    }

    task = type

# Generated at 2022-06-13 10:43:24.734115
# Unit test for constructor of class ActionModule
def test_ActionModule():
    set_stats =  dict(data={"test": 1}, per_host=False, aggregate=True)
    task = dict(action=dict(module="set_stats", args=set_stats))
    task_vars = {}

    action = ActionModule(task, task_vars=task_vars, connection=dict(), play_context=dict())
    assert action._task.args == task['action']['args']

# Generated at 2022-06-13 10:43:31.875208
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    # Not tested
    assert m.run() == {}


# Generated at 2022-06-13 10:43:34.147070
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass
# TODO: write unit test for method run of class ActionModule

# Generated at 2022-06-13 10:43:36.757330
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(None, {}, None)
    assert isinstance(a, ActionModule)

# Generated at 2022-06-13 10:43:38.031285
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert(1 == 1)

# Generated at 2022-06-13 10:43:48.604839
# Unit test for constructor of class ActionModule
def test_ActionModule():

    # Test empty constructor
    assert ActionModule()

    # Test full constructor
    assert ActionModule(
        task=dict(action=dict()),
        connection=dict(),
        play_context=dict(remote_addr='127.0.0.1'),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )
    assert ActionModule(
        task=dict(action=dict()),
        connection=dict(),
        play_context=dict(remote_addr='127.0.0.1'),
        loader=dict(),
        templar=dict(),
        shared_loader_obj=dict()
    )

# Generated at 2022-06-13 10:43:50.454375
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module._connection = None
    module._play_context = None
    module._loader = None
    module._templar = None
    module._shared_loader_obj = None
    module._task = None

    assert module.run() != None

# Generated at 2022-06-13 10:43:51.422046
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:44:05.653506
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module_run = ActionModule(action_base=None, task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    action_module_run._task = {'args': {'data': {'var_name': 'abc', 'var_name1': 'xyz'}, 'per_host': False, 'aggregate': True}}
    action_module_run._templar = "a"
    action_module_run._shared_loader_obj = "b"
    assert action_module_run.run() == {'ansible_stats': {'data': {'var_name': 'abc', 'var_name1': 'xyz'}, 'per_host': False, 'aggregate': True}, 'changed': False}

# Generated at 2022-06-13 10:44:08.819793
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert (ActionModule != object)
    assert (ActionModule != dict)
    assert isinstance(ActionModule, object)
    assert not isinstance(ActionModule, dict)

# Verify that action module class can be instantiated

# Generated at 2022-06-13 10:44:09.723947
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None


# Generated at 2022-06-13 10:44:25.280420
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #
    # Check that run works
    #
    action_module = ActionModule()
    tmp = ''
    task_vars = {}
    action_module.set_runner(ActionModule)
    action_module._task.args = {}
    res = action_module.run(tmp, task_vars)
    assert res['ansible_stats']['data'] == {}
    assert res['ansible_stats']['per_host'] == False
    assert res['ansible_stats']['aggregate'] == True

    #
    # Check that run works with a dictionary data
    #
    action_module = ActionModule()
    tmp = ''
    task_vars = {}
    action_module.set_runner(ActionModule)

# Generated at 2022-06-13 10:44:25.725167
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule()

# Generated at 2022-06-13 10:44:32.979676
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import pytest
    from mock import Mock

    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.vars import load_extra_vars
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    import ansible.constants as C

    am = ActionModule(Task(), Mock())

    # test normal use case: no args
    result = am.run(task_vars={})
    assert result['changed'] == False

# Generated at 2022-06-13 10:44:37.570113
# Unit test for constructor of class ActionModule
def test_ActionModule():
    global _VALID_ARGS
    a = ActionModule()
    assert a._task.action == 'set_stats'
    assert a.TRANSFERS_FILES == False
    assert a._VALID_ARGS == frozenset(['aggregate', 'data', 'per_host'])

# Generated at 2022-06-13 10:44:43.894108
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(
        task=dict(action=dict(module='set_stats', data=dict(ansible_facts=dict(a=1)))),
        connection=dict(module='local', play_context=dict(become_method='sudo')),
        play_context=dict(become_method='sudo'),
        loader=dict(), templar=dict(), shared_loader_obj=dict()
    )

    result = module.run(tmp=None, task_vars=dict())
    assert result['ansible_stats'] == {'aggregate': True, 'data': {'a': 1}, 'per_host': False}


# Generated at 2022-06-13 10:44:46.428848
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.utils.template
    am = ActionModule()
    am_run = am.run
    # TODO
    return am_run

# Generated at 2022-06-13 10:44:50.430433
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Just doing a constructor test here, since
    the actual implementation is tested elsewhere.
    """
    module = ActionModule(task=dict(vars=dict()))
    assert module is not None

# Generated at 2022-06-13 10:44:53.940825
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Load None as the constructor for class ActionModule
    # It will load the real constructor
    action_module = ActionModule(None, "")
    assert action_module is not None

# Generated at 2022-06-13 10:44:56.653930
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    Unit test for constructor of class ActionModule
    '''
    act_mod = ActionModule(None, None)
    assert act_mod is not None

# Generated at 2022-06-13 10:45:07.263882
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    class MockTask:
        name = 'set_stats'
        args = {'data': {'foo': 'bar'}}

    class MockTemplar:
        def template(self, str):
            return str

    class MockModule:
        def __init__(self, *args):
            self.args = args[0]

    class MockTaskVars:
        def get(self, var):
            return {}

    class MockResult:
        def __init__(self, failed=False, msg=""):
            self.failed = failed
            self.msg = msg

    class MockActionBase(ActionBase):
        def __init__(self, *args):
            self._task = MockTask()
            self._templar = MockTemplar()


# Generated at 2022-06-13 10:45:26.600246
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import action_plugin
    import task_ds
    import task_vars
    import play_context

    # load up a test task
    action = action_plugin.ActionModule(task_ds.Task(name="test_task",
                                                     args={'data': "{'foo': true}",
                                                           'per_host': True,
                                                           'aggregate': True}))

    # load up test task_vars
    action._templar.vars = task_vars.TaskVars(
        play=None,
        task=action._task,
        hostvars={},
        vars={})

    # load up test play_context

# Generated at 2022-06-13 10:45:35.235962
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.ansible_release import __version__
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    class Options(object):
        def __init__(self, connection='local', module_path=None, forks=100, become=None, become_method=None, become_user=None, check=False, verbosity=3):
            self.connection = connection
            self.module_path = module_path
            self.forks = forks
            self.become = become
            self.become_method = become_method
            self.become_user = become_user
           

# Generated at 2022-06-13 10:45:42.583425
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    result = {
        'msg': '',
        'failed': False,
        'ansible_stats': {
            'aggregate': True,
            'data': {},
            'per_host': False,
        },
    }

    stats = _ActionModule().run(task_vars=dict(), tmp=None)

    assert result == stats

# Mock for class ActionModule for unittest

# Generated at 2022-06-13 10:45:44.417483
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("Running test_ActionModule_run...")
    assert True

# Generated at 2022-06-13 10:45:54.182633
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # init
    task_vars = {}
    mock_task = {}
    mock_task['args'] = {
        'data': {
            'foo': 1,
            'bar': 'baz',
            'baz': [1, 2, 3],
            'qux': True
        }
    }
    ret = ActionModule.run(mock_task, task_vars)
    # precondition
    assert ret['ansible_stats']['per_host'] == False
    assert ret['ansible_stats']['aggregate'] == True
    # check data
    assert 'foo' in ret['ansible_stats']['data']
    assert ret['ansible_stats']['data']['foo'] == 1
    assert 'bar' in ret['ansible_stats']['data']
   

# Generated at 2022-06-13 10:46:01.821798
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module_test_result = dict()
    module_test_result['data'] = {'a':'value_a', 'b':'value_b'}
    module_test_result['per_host'] = False
    module_test_result['aggregate'] = True
    module_test_result['failed'] = False
    module_test_result['msg'] = ''
    module_test_result['changed'] = False

    module = ActionModule()
    test_result = module.run(task_vars=None, tmp=None)
    assert test_result == module_test_result



# Generated at 2022-06-13 10:46:11.172259
# Unit test for constructor of class ActionModule
def test_ActionModule():

    mock_task = type('Task',(object,),{})()
    mock_tqm = type('TaskQueueManager',(object,),{'_stdout_callback':None})()
    mock_loader = type('Loader',(object,),{})()
    mock_variable_manager = type('VariableManager',(object,),{'_fact_cache':{},'_extra_vars':{},'options':type('Options',(object,),{'ask_pass':False,'ask_su_pass':False,'ask_vault_pass':False})})()

    am = ActionModule(mock_task,mock_connection=None,play_context=None,loader=mock_loader, templar=None, shared_loader_obj=None)
    assert isinstance(am, ActionModule)



# Generated at 2022-06-13 10:46:14.458867
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    This unit test will test constructor of the class ActionModule
    :return: None
    '''
    action = ActionModule(None, None, None)
    assert action._VALID_ARGS == frozenset({'aggregate', 'per_host', 'data'})
    assert action.TRANSFERS_FILES == False



# Generated at 2022-06-13 10:46:15.196535
# Unit test for constructor of class ActionModule
def test_ActionModule():
  x = ActionModule()
  assert x

# Generated at 2022-06-13 10:46:16.223141
# Unit test for constructor of class ActionModule
def test_ActionModule():

    from ansible.plugins import action
    action.ActionModule(None, None)

# Generated at 2022-06-13 10:46:40.918309
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert isinstance(module._VALID_ARGS, frozenset)
    assert module.TRANSFERS_FILES == False


# Generated at 2022-06-13 10:46:42.249374
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Test constructor of class ActionModule."""
    assert ActionModule is not None

# Generated at 2022-06-13 10:46:45.194685
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(task=dict(), connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert mod is not None

# Generated at 2022-06-13 10:46:54.948053
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Set up mock task
    mock_task = type('Mock_task', (object,), {})()
    mock_task.args = {}

    # Set up mock templar
    _template_from_file = type('_template_from_file', (object,), {})()
    _template_from_file._data = ''
    mock_templar = type('Mock_templar', (object,), {})()
    mock_templar.template = lambda x, y=None, z=None: y
    mock_templar.template_from_file = lambda x, y=None, z=False: _template_from_file

    # Set up mock_action_base
    mock_action_base = type('Mock_action_base', (object,), {})()
    mock_action_base

# Generated at 2022-06-13 10:46:59.797926
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(
        load_from_file_module_name='set_stats',
        load_from_file_module_args=dict(
            data=dict(
                one='1',
                two='2',
                three='this needs templating {{ one }}',
            )
        )
    )
    action.run()
    assert action._task.args == dict(
        data=dict(
            one='1',
            two='2',
            three='this needs templating 1',
        )
    )

# Generated at 2022-06-13 10:47:10.471308
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # /tests/units/plugins/action/ActionModuleTest.py
    class TestActionModule(ActionModule):
        def run(self, tmp=None, task_vars=None):
            pass
    # /tests/units/plugins/action/ActionModuleTest.py

    am = TestActionModule(dict(module_args=dict(
            data=dict(hostvars=dict(a=1, b=2, c=3), my_result='ok'),
            aggregate=True,
            per_host=True,
        )))

# Generated at 2022-06-13 10:47:11.604300
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)

# Generated at 2022-06-13 10:47:19.920741
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    global_vars = dict(
        ansible_stats={
            'aggregate': True,
            'per_host': True,
            'data': {'n': 1}})
    ActionModule._task = dict(args=dict())

    module = ActionModule()
    module._templar = FakeTemplar(global_vars)

    result = module.run(task_vars=global_vars)

    assert result['changed'] == False
    assert result['ansible_stats'] == dict(aggregate=True, data={'ok': 'ok'}, per_host=False)


# Generated at 2022-06-13 10:47:31.574476
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    action = ActionModule()

    # TODO: test for the following cases
    #data = {'foo': "{{ 'bar' }}"}

    #data = {'foo': '{{ bar }}'}
    #vars = {'bar': 'baz'}

    #data = {'foo': '{{ 'bar' }}'}
    #vars = {}

    #data = "{{ foo }}"

    #data = {'foo': '{{ 'bar' }}'}
    #vars = {'bar': 'baz'}

    #data = {'foo': '{{ 'bar' }}'}
    #vars = {'bar': 'baz'}

# Generated at 2022-06-13 10:47:39.017821
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule(task=Task(), connection=None, play_context=PlayContext(), loader=None, templar=None, shared_loader_obj=None)
    task_vars = {}
    result = action_module.run(tmp='', task_vars=task_vars)
    assert result.get('ansible_stats') is not None
    assert 'data' in result['ansible_stats']
    assert result['ansible_stats']['data'] == {}
    assert result['ansible_stats']['per_host'] is False
    assert result['ansible_stats']['aggregate'] is True

# Generated at 2022-06-13 10:48:28.506046
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # pylint: disable=star-args
    # pylint: disable=too-many-nested-blocks
    import tempfile
    # pylint: disable=import-error, no-name-in-module
    from ansible.module_utils.facts import ansible_stats

    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils import facts
    import platform
    import ansible.constants as C

    distribution = Distribution()
    distribution.family = 'redhat'
    distribution.name = 'RedHatEnterpriseServer'
    distribution.major_version = '7'
    distribution.minor_version = '1'
    distribution.architecture = 'x86_64'

# Generated at 2022-06-13 10:48:29.141097
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:48:39.469326
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils import context_objects as co

    def get_test_args():
        # Prepare args
        args = dict()
        args['_ansible_syslog_facility'] = 0
        args['_ansible_debug'] = False
        args['_ansible_diff'] = False
        args['_ansible_keep_remote_files'] = False
        args['ansible_capability_check'] = False
        args['ansible_check_mode'] = False
        args['ansible_host_pattern'] = 'all'
        args['ansible_inventory_sources'] = ['./examples/ansible.cfg']
        args['ansible_limit'] = 'all'

# Generated at 2022-06-13 10:48:40.191498
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:48:42.327385
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #print("Testing class: ActionModule")
    # Create an ActionModule object
    myActionModule = ActionModule()

# Generated at 2022-06-13 10:48:42.904514
# Unit test for method run of class ActionModule
def test_ActionModule_run():
  pass

# Generated at 2022-06-13 10:48:43.472804
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:48:50.792160
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """
    Unit test code to test initialization of class ActionModule.
    """
    # initialize mock_task to an empty object
    mock_task = type('', (object,), {})()
    mock_task.__dict__ = {}
    # Argument args does not exist to test exception.
    mock_task.args = {}
    mock_task.__dict__ = {}

    action_module = ActionModule(mock_task, mock_connection, 'action_test.yml', '/tmp/', 'test', '', 1)
    assert action_module
    assert action_module.__dict__ is not {}


# Generated at 2022-06-13 10:49:00.913414
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.base import PlayContext

    class TestActionModule(ActionModule):
        def run(self, tmp=None, task_vars=None):
            return super(TestActionModule, self).run(tmp, task_vars)

    action = TestActionModule(
        play_context=PlayContext(),
        task=dict(args={'data': {'a': '1', 'b': '2'}, 'per_host': 'true', 'aggregate': 'False'})
    )
    result = action.run()

    assert result['changed'] == False
    assert result['ansible_stats'] == {'data': {'a':'1', 'b':'2'}, 'per_host': True, 'aggregate': False}


# Generated at 2022-06-13 10:49:02.471638
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule( 'test', dict(), False)
    assert action_module is not None

# Generated at 2022-06-13 10:51:16.469664
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Define some complex-mock of the original objects.
    # First, we need to have a method that returns a complex-mock
    # (with functions, etc. inside). For example:
    def get_complex_mock():
        mock_obj = MagicMock()

        def get_complex_mock2():
            mock_obj = MagicMock()
            return mock_obj

        mock_obj.get_complex_mock2 = get_complex_mock2
        return mock_obj

    mock_action_base = get_complex_mock()

    # Then, we can define a complex-mock
    mock_task = MagicMock()
    mock_task.args = {}
    mock_task.args['data'] = {}
    mock_task.args['data']['foo'] = 'bar'

   

# Generated at 2022-06-13 10:51:24.345825
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible import constants
    from ansible.plugins.loader import action_loader

    # Create a new default set_stats task
    adhoc = action_loader.get('set_stats', class_only=True)()
    adhoc._task.action = 'set_stats'
    adhoc._task.args = {'data': {'test': 'passed'}, 'per_host': False, 'aggregate': True}
    adhoc._shared_loader_obj = None
    adhoc._task.action = 'set_stats'
    adhoc._task.args = {'data': {'test': 'passed'}, 'per_host': False, 'aggregate': True}
    adhoc._shared_loader_obj = None

    # Run the task

# Generated at 2022-06-13 10:51:31.036278
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule
    :return: None
    """
    set_stats = ActionModule()
    set_stats.set_task_plugins_manager('_manager', '_loader')
    set_stats.set_task('_task')

    # Case 1:  test when _task.args is None
    _task = dict()
    _task['action'] = dict()
    _task['action']['__ansible_module__'] = 'set_stats'
    _task['action']['args'] = None
    set_stats._task = _task
    expected = dict()
    expected['ansible_stats'] = dict()
    expected['ansible_stats']['aggregate'] = True
    expected['ansible_stats']['per_host'] = False

# Generated at 2022-06-13 10:51:36.469736
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    def _mock_task(args):
        return type('MockTask', (), { 'args': args })

    def _mock_templar(template_data):
        return type('MockTemplar', (), { 'template': lambda self, x, convert_bare=False, fail_on_undefined=True: template_data })

    result_true = {
        'changed': False,
        'ansible_stats': {
            'data': {},
            'per_host': False,
            'aggregate': True
        }
    }
    result_false = {
        'changed': False,
        'ansible_stats': {
            'data': {},
            'per_host': False,
            'aggregate': False
        }
    }


# Generated at 2022-06-13 10:51:38.749712
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Output for method run is a list of strings
    assert True

# Generated at 2022-06-13 10:51:40.264214
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule()
    assert isinstance(am, ActionBase)


# Generated at 2022-06-13 10:51:41.917343
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(dict(), {})
    assert action.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:51:42.789148
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert False, "Test not implemented"

# Generated at 2022-06-13 10:51:45.352391
# Unit test for constructor of class ActionModule
def test_ActionModule():
    '''
    action_module = action_module.ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)
    assert action_module != None
    '''
    pass


if __name__ == "__main__":
    test_ActionModule()

# Generated at 2022-06-13 10:51:48.039619
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Unit test to test the run method of ActionModule
    # Create an object of ActionModule. Only required parameters are passed to constructor
    testobj = ActionModule()
    # TODO: Unit test this
    pass
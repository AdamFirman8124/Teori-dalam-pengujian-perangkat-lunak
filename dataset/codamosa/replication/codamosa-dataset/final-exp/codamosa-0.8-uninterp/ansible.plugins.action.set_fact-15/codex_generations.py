

# Generated at 2022-06-13 10:42:21.655030
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Create a fake ansible module object
    # that can act as a 'self' object for the
    # constructor
    class FakeModule(object):
        def __init__(self):
            self.args = dict()
            # set some fake defaults for the task object
            self.check_mode = None
            self.no_log = False
            self.verbosity = 3
    module = FakeModule()

    # create a fake ansible task object that can act as a 'self'
    # object for the constructor
    class FakeTask(object):
        def __init__(self):
            self.args = dict()
            self.check_mode = False
            self.no_log = False
    task = FakeTask()
    task.args = dict()

    # Create a fake ActionBase object that can act as the base class
    # for

# Generated at 2022-06-13 10:42:28.630363
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import tempfile
    from ansible.plugins.action.set_fact import ActionModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=['localhost'])
    variable_manager.set_inventory(inventory)
    loader.set_basedir(tempfile.mkdtemp())

# Generated at 2022-06-13 10:42:41.220645
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(load_fixture('test_action_set_fact_run.yml'))
    module.run()
    module._task.args.append('a=b')  # don't let this fail in cleanup
    module.cleanup()

    assert module.task_vars == {}
    assert module._templar.template('this') == 'this'
    assert module.tmp == None

    module.run(task_vars={'mydict': {'abc': 'def'}})
    module._task.args.append('a=b')  # don't let this fail in cleanup
    module.cleanup()

    assert module.task_vars.get('mydict') == {'abc': 'def'}
    assert module._templar.template('this') == 'this'

# Generated at 2022-06-13 10:42:42.242201
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.run(None)

# Generated at 2022-06-13 10:42:48.668393
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.constants as C

    class Module:
        def __init__(self):
            self.params = {}

    class Task:
        def __init__(self):
            self.args = {'testing': 'ansible'}

    class Play:
        def __init__(self):
            self.hosts = ['127.0.0.1']

    class PlayContext:
        pass

    class Runner:
        pass

    am = ActionModule(Task(), Runner(), PlayContext(), Play())
    assert am is not None
    assert isinstance(am, ActionModule)
    assert isinstance(am._play_context, PlayContext)
    assert am._play_context.connection == 'local'
    assert not am.TRANSFERS_FILES
    assert am._play is not None

# Generated at 2022-06-13 10:42:55.433852
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    print('sys.version_info[0] = ', sys.version_info[0])
    assert sys.version_info[0] == 3, "Python 3 required for this test"

    from unittest.mock import Mock, patch
    from ansible.plugins import action

    myaction = action.ActionModule()
    myaction.task_vars = dict()
    myaction.task_vars['ansible_facts'] = dict()

    myaction.run(task_vars=myaction.task_vars)

# Generated at 2022-06-13 10:42:56.809926
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: Impliment unit test
    assert False



# Generated at 2022-06-13 10:42:59.532341
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule(None, dict(), None, None)
    assert actionModule.run(None, dict()) == dict(changed=False)



# Generated at 2022-06-13 10:43:09.915079
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print('Testing action module....')
    # Testing import of the class
    from ansible.plugins.action.set_fact import ActionModule
    # Python dict which will be converted to JSON and passed to the class run method as task_vars
    task_vars = {'hostvars': {'hostname': {'ansible_distribution': 'ubuntu',
                                           'ansible_distribution_version': '14.04'}}}
    # Dict containing the value for the arguments parameter for the class constructor

# Generated at 2022-06-13 10:43:19.207207
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.compat.tests import unittest
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.compat.tests.mock import patch

    mock_task = unittest.mock.Mock()
    mock_task._role = unittest.mock.Mock()
    mock_task._role.get_default_vars = unittest.mock.Mock(return_value={})

    mock_task_vars = dict()

    # Mock _templar of parent class to return the same value
    class MockTemplar:
        def template(self, val):
            return val

    mock_templar = MockTemplar()

    # Test case 1: No task_vars passed as argument
    # If task_vars is None or

# Generated at 2022-06-13 10:43:25.160690
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule({'name': 'test', 'args': {'a': 1}}, 'test')
    assert action

# Generated at 2022-06-13 10:43:32.307418
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Given a task 'set_fact' with kwargs {'var': 'value'}
    task = dict()
    task['action'] = dict()
    task['action']['module'] = 'set_fact'
    task['action']['args'] = dict()
    task['action']['args']['var'] = 'value'
    # And an action module instance
    actionModule = ActionModule(task, '<test>')

    # When I run the task
    result = actionModule.run(None, None)

    # Then the result is correct
    assert dict() == result
    assert dict() == result['ansible_facts']
    assert False == result['_ansible_facts_cacheable']


# Generated at 2022-06-13 10:43:39.741215
# Unit test for constructor of class ActionModule
def test_ActionModule():
    test_vars = dict(
        ansible_connection='local'
    )
    task_vars = dict(
        ansible_facts=dict(firstvar='red', secondvar='blue'),
        ansible_facts_cacheable=False
    )
    task = dict(
        name="test_module_1",
        action={'module': 'set_fact', 'args': {'new_fact': 'test'}}
    )
    action_module = ActionModule(task=task, connection='local', play_context=dict(basedir='/tmp'), loader=None, templar=None, shared_loader_obj=None)
    assert action_module

# Generated at 2022-06-13 10:43:51.646999
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(load_plugins=False)

    module._task.args = {'test': 'true'}
    module._templar = Dictable()
    assert module.run() == {'ansible_facts': {'test': True}, 'changed': False, '_ansible_facts_cacheable': False}
    module._task.args = {'test': 'false'}
    assert module.run() == {'ansible_facts': {'test': False}, 'changed': False, '_ansible_facts_cacheable': False}

    module._task.args = {'test_1': '1'}
    assert module.run() == {'ansible_facts': {'test_1': '1'}, 'changed': False, '_ansible_facts_cacheable': False}

    module._task.args

# Generated at 2022-06-13 10:43:54.007795
# Unit test for constructor of class ActionModule
def test_ActionModule():
    t = ActionModule(load_empty_file_task, task_vars={})
    assert t is not None

# Generated at 2022-06-13 10:43:54.679869
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:43:57.175283
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:44:03.328983
# Unit test for constructor of class ActionModule
def test_ActionModule():
    x = {}

    x['action'] = ['set_fact']
    x['args'] = dict(a=1)
    y = [{'a': 1}]
    z = {'a': 1, '_ansible_facts_cacheable': False, 'changed': False}

    assert ActionModule(x, None) is not None


# Generated at 2022-06-13 10:44:07.289974
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule()
    result = action.run(tmp='/tmp', task_vars=None)
    assert(result['ansible_facts'] == {})
    assert(result['_ansible_facts_cacheable'] == False)

# Generated at 2022-06-13 10:44:15.675771
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    task_vars = dict(facts_dict=dict(foo='foo', bar='bar'))
    import ansible.plugins.action.set_fact as sf
    ma = sf.ActionModule(dict(task=dict(args={'one': 1})), dict())
    assert ma.run(task_vars)['ansible_facts']['one'] == 1

    ma = sf.ActionModule(dict(task=dict(args={'one': '1', 'two': '2'})), dict())
    assert ma.run(task_vars)['ansible_facts']['one'] == '1'
    assert ma.run(task_vars)['ansible_facts']['two'] == '2'


# Generated at 2022-06-13 10:44:25.737685
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule( {}, {}, {}, {} )
    assert isinstance(action, ActionModule)

# Generated at 2022-06-13 10:44:26.248700
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:44:35.530260
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest
    import ansible.parsing.dataloader
    import ansible.vars.manager
    import ansible.inventory.manager
    import ansible.playbook.play
    import ansible.module_utils.facts.system.distribution
    import ansible.module_utils.facts.system.facter
    import ansible.module_utils.facts.system.system
    import ansible.module_utils.facts.system.pkg_mgr
    import ansible.module_utils.facts.system.selinux
    import ansible.module_utils.facts.network.interface
    import ansible.module_utils.facts.network.interfaces
    import ansible.module_utils.facts.network.ipaddresses

# Generated at 2022-06-13 10:44:43.864708
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    try:
        am = ActionModule()
        am.run()
    except AnsibleActionFail as e:
        print(e)
        assert str(e) == 'No key/value pairs provided, at least one is required for this action to succeed', 'Exception message changed'

    try:
        am = ActionModule()
        am.run(task_vars={'fact1': 'val1'})
    except AnsibleActionFail as e:
        print(e)
        assert str(e) == 'No key/value pairs provided, at least one is required for this action to succeed', 'Exception message changed'


# Generated at 2022-06-13 10:44:45.735008
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule({}, {}, {}, {})

# Generated at 2022-06-13 10:44:57.563349
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Arguments to the run function
    tmp, task_vars = None, { 'ansible_distribution': "Ubuntu" }

    # Return value of the run function
    expected_result = dict(changed=False, ansible_facts=dict(ansible_distribution=task_vars['ansible_distribution']))

    # If run is called without arguments, the result should be the same as the one above
    module_name = 'add'
    module_args = dict(ansible_distribution=dict(default='CentOS'))
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
    )
    am = ActionModule(module, module.params)
    res = am.run(tmp, task_vars)

# Generated at 2022-06-13 10:45:00.569663
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import ansible.plugins.action.set_fact
    am = ansible.plugins.action.set_fact.ActionModule(None, {}, {}, '/dev/null')
    assert am is not None

# Generated at 2022-06-13 10:45:04.074500
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=dict(action=dict()), connection=dict(), play_context=dict(), loader=None, templar=None, shared_loader_obj=None).run()



# Generated at 2022-06-13 10:45:06.011044
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, None, None, None, None)
    assert action.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:45:13.503041
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Test of method run of class ActionModule.

    Initialization of the class, test of run method via check of a dict result
    '''
    action_module = imp.load_source('action_module', 'lib/ansible/plugins/action/set_fact.py')
    action_module_instance = action_module.ActionModule(None, None)

    user_vars = dict()

    # Create different test cases to be checked
    test_cases = dict()
    test_cases[True] = dict(
        tmp=None,
        task_vars=user_vars,
        facts=dict(
            test1='ok1',
            test2='ok2',
        ),
        cacheable=False,
        )

# Generated at 2022-06-13 10:45:32.080886
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(task=dict(args=dict(test_param="test value")))
    assert a._templar is not None, "_templar should not be None"



# Generated at 2022-06-13 10:45:36.862197
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule('test', {}, {}, False, None, module_name='test', task_name='test')
    assert am is not None
    assert isinstance(am, ActionModule)
    assert isinstance(am._templar, object)

# Generated at 2022-06-13 10:45:38.860459
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule()
    assert isinstance(m, ActionModule)

# Generated at 2022-06-13 10:45:42.717812
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    
    ActionModule.run(
        dict(
            action=dict(
                module_name=__name__
            )
        ),
        TaskResult(
            host="localhost",
            task=dict(
                module_name=__name__,
                args=dict(
                    debug='true',
                    value_one=1,
                    value_two=2,
                    value_three=3
                )
            )
        ),
        PlayContext(
            connection='local'
        )
    )

# Generated at 2022-06-13 10:45:51.038566
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """Unit test for method run of class ActionModule"""
    module = AnsibleModule(
        argument_spec = dict(
            key=dict(required=True, type='str'),
            value=dict(required=True, type='str'),
            cacheable=dict(required=False, type="bool", default=False),
        ),
    )
    set_module_args(dict(
        key='my_var',
        value='my_value',
        cacheable=True,
    ))
    action = ActionModule(module, module._task)
    try:
        action.run(task_vars=dict())
    except Exception as e:
        assert isinstance(e, AnsibleActionFail)
        assert 'No key' in str(e)

# Generated at 2022-06-13 10:45:51.700537
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Test constructor of ActionModule class."""
    pass

# Generated at 2022-06-13 10:45:55.677894
# Unit test for constructor of class ActionModule
def test_ActionModule():
    print("Testing ActionModule constructor")
    # Note: We cannot use Mock, because we need to test "if C.DEFAULT_JINJA2_NATIVE"
    ansible_ActionModule = ActionModule(None, {}, None, {})
    print("ActionModule() constructor passed!")

if __name__ == "__main__":
    print("Executing tests")
    test_ActionModule()
    print("Executed tests")

# Generated at 2022-06-13 10:46:01.929400
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_name = "foobar"
    module_args = {}
    am = ActionModule(module_name, module_args)

    # Test constructor of class ActionModule
    assert am, "Failed to instantiate ActionModule"
    assert isinstance(am, ActionModule), "Failed to instantiate ActionModule"

    # Test the method run
    result = {}
    result = am.run()
    assert result is not None, "Failed to run"


if __name__ == "__main__":

    # test ActionModule constructor
    test_ActionModule()

# Generated at 2022-06-13 10:46:02.506872
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()

# Generated at 2022-06-13 10:46:04.584079
# Unit test for constructor of class ActionModule
def test_ActionModule():
    name = 'action_module_name'
    action_module = ActionModule(name=name)
    assert(action_module.name == name)

# Generated at 2022-06-13 10:46:38.961777
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(None, None, None, None, None, None)
    assert mod != None

# Generated at 2022-06-13 10:46:50.187611
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import mock
    import unittest

    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.action import ActionBase

    class ActionModule(ActionBase):
        __test__ = True
        TRANSFERS_FILES = False

        def run(self, tmp=None, task_vars=None):
            return super(ActionModule, self).run(tmp, task_vars)

    class TaskVars(dict):
        def __getitem__(self, key):
            return super(TaskVars, self).__getitem__(key)

        def __setitem__(self, key, value):
            return super(TaskVars, self).__setitem__(key, value)


# Generated at 2022-06-13 10:46:58.731229
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create new action module object
    action_module = ActionModule(None, None, None, None, None, {})
    # Create new action result
    result = {}

    # assert_equal fails to test string, hence use assert_true
    assert_true = lambda a, b: a if a == b else False

    try:
        # Execute run method of the action module (tmp, task_vars)
        action_module.run(None, None)
        result = {'failed': True, 'msg': "AnsibleActionFail not thrown"}
    except AnsibleActionFail:
        # AnsibleActionFail thrown as expected, continue execution
        pass
    except Exception as e:
        # Some other exception thrown, it should not happen
        result = {'failed': True, 'msg': repr(e)}

    # Test if the result is

# Generated at 2022-06-13 10:47:01.647416
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """This is a standalone stub for a unit test for the ActionModule class.
    The stub is meant as a guide for developing and testing the ActionModule.
    """

    module_args = dict(
        cacheable=dict(type='bool', default=False),
        foo='bar',
        ansible_facts=dict(type='dict', elements='str', required=True),
    )

    tmp = '/tmp'
    task_vars = dict()

    ansible_facts = dict()

    am = ActionModule(tmp, task_vars, module_args, ansible_facts)

# Generated at 2022-06-13 10:47:02.835604
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule.__name__ == 'ActionModule'

# Generated at 2022-06-13 10:47:12.045920
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # This is to simulate the templating of module arguments
    class MockTemplar:
        def __init__(self):
            self.template_data = {'a': 'args.a', 'b': 'args.b', 'c': 'args.c', 'd': 'args.d', 'e': 'args.e'}
            self.template_result = {'a': 'foo', 'b': 'bar', 'c': True}

        def template(self, value):
            if value in self.template_result:
                return self.template_result[value]
            return value

    # This is to simulate an AnsibleTask object

# Generated at 2022-06-13 10:47:15.536228
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert am.name == 'set_fact'
    assert not am.no_log

# Generated at 2022-06-13 10:47:21.630146
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Note: we are not testing ActionBase and ActionBase._execute_module
    # because these have no code to be tested.
    import ansible.plugins.action
    ae = ansible.plugins.action.ActionModule('fixtures/action_plugins/test_action_module', 'fixtures/action_plugins/test_action_module', 'ansible.cfg')

    assert ae.get_name() == 'test_action_module'

# Generated at 2022-06-13 10:47:26.351847
# Unit test for constructor of class ActionModule
def test_ActionModule():
    actionmodule = ActionModule(
        task=dict(),
        connection=dict(),
        play_context=dict(),
        loader=None,
        templar=None,
        shared_loader_obj=None)

    assert actionmodule

# Generated at 2022-06-13 10:47:30.945047
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play

    t = Task()
    setattr(t, '_role', None)

    p = Play()
    setattr(t, '_play', p)

    x = ActionModule(t)
    assert x.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:48:41.183303
# Unit test for constructor of class ActionModule
def test_ActionModule():
    tm = ActionModule(None, None, None, None, None, None, None)
    assert tm

# Generated at 2022-06-13 10:48:51.021436
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys, os
    sys.path.append("/usr/lib/python2.7/site-packages/ansible")
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.executor import task_queue_manager
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.template import Templar
    from ansible.errors import AnsibleActionFail

# Generated at 2022-06-13 10:49:01.445043
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    import sys
    import yaml
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six.moves import builtins
    from ansible.plugins.action import ActionBase

    class MockModule(object):
        def __init__(self, **kwargs):
            for k,v in iteritems(kwargs):
                setattr(self, k, v)

        def fail_json(self, *args, **kwargs):
            raise Exception('fail_json')

    class MockTask(object):
        def __init__(self, args):
            self.args = args

    class MockTemplar(object):
        def __init__(self, *args, **kwargs):
            return

        def template(self, data):
            return data


# Generated at 2022-06-13 10:49:04.267228
# Unit test for constructor of class ActionModule
def test_ActionModule():
    a = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert a is not None

# Generated at 2022-06-13 10:49:13.271667
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import os

    test_dir = os.path.dirname(os.path.realpath(__file__)) + "/test_files/ansible/"

    with open(test_dir + "playbook-fact-name-validation-argument-invalid.json") as test_data:
        result = json.load(test_data)

# Generated at 2022-06-13 10:49:13.951694
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # TODO: implement this.
    assert True

# Generated at 2022-06-13 10:49:14.563224
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:49:22.815086
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule()
    actionModule._task = {
        'args': {
            'var1': 'value1',
            'var2': 'value2',
        },
    }
    actionModule._tmp = None
    actionModule._templar = None
    result = actionModule.run(tmp=None, task_vars=None)
    assert result == {'ansible_facts': {'var1': 'value1', 'var2': 'value2'}, '_ansible_facts_cacheable': False}


# Generated at 2022-06-13 10:49:25.983980
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, {}, {}, '/path/to/ansible')
    # make sure we have the right action object
    assert isinstance(action, ActionModule)



# Generated at 2022-06-13 10:49:33.075868
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import sys
    import pytest

    from ansible.module_utils.basic import AnsibleModule

    if sys.version_info[:2] == (2, 6):
        pytest.skip("unittests on python2.6 fail this test", allow_module_level=True)

    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.plugins.action.setup import ActionModule as Setup

    mock_task = dict(run_once=True, args=dict())
    mock_tmp = ''
    mock_task_vars = dict()

    action = Setup(mock_task, mock_tmp)

    with pytest.raises(AnsibleActionFail) as e:
        action.run(task_vars=mock_task_vars)

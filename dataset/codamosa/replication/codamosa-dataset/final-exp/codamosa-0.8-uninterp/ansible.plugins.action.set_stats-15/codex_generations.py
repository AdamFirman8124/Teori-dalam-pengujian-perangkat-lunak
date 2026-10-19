

# Generated at 2022-06-13 10:42:28.721215
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # stubbed data
    tmp = None
    task_vars = {"ansible_ssh_host":"10.0.0.1"}
    self = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # stubbed run function
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        stats = {'data': {}, 'per_host': False, 'aggregate': True}

        if self._task.args:
            data = self._task.args.get('data', {})


# Generated at 2022-06-13 10:42:35.765912
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    result = module.run(tmp=None, task_vars=None)
    assert result['ansible_stats'] == {'data': {}, 'per_host': False, 'aggregate': True}
    assert result['changed'] == False

# Generated at 2022-06-13 10:42:42.688919
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a ActionModule object
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    # Test when run is called with an argument of tmp
    def run_mock_temp(tmp):
        tmp = None
        action_module.run(tmp)

    # Test when run is called with an argument of task_vars
    def run_mock_task_vars(task_vars):
        task_vars = None
        action_module.run(task_vars)

    # Test when run is called with an argument of both tmp and task_vars
    def run_mock_temp_task_vars(tmp, task_vars):
        tmp = None
        task_vars = None
       

# Generated at 2022-06-13 10:42:51.755312
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_context import PlayContext
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    import sys

    results = []

    class Play(object):

        def __init__(self):
            self.name = 'test_play'

    class PlayContext(object):
        def __init__(self):
            self.play = Play()

    class TestModule(object):

        def __init__(self, templar):
            self._templar = templar

    class TestHost(object):
        def __init__(self, name):
            self.name = name


# Generated at 2022-06-13 10:42:57.952298
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:42:58.602897
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert True

# Generated at 2022-06-13 10:43:02.362946
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m = ActionModule()
    m._task.args= {'data': {'toto': 'toto'}}
    d = m.run()
    assert d['ansible_stats']['data']['toto'] == 'toto'

# Generated at 2022-06-13 10:43:03.379151
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_plugin = ActionModule(None, None, None, None, None, None)
    assert action_plugin != None



# Generated at 2022-06-13 10:43:05.841480
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert module is not None


# Generated at 2022-06-13 10:43:13.267363
# Unit test for constructor of class ActionModule
def test_ActionModule():
    result = dict(failed=None, msg=None, ansible_stats=None, changed=None)
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    actions_base = ActionBase(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    name = action_module.__class__.__name__
    assert name == "ActionModule"
    assert action_module.__class__.__bases__ == (actions_base,)
    assert action_module.TRANSFERS_FILES == False
    assert action_module._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))
   

# Generated at 2022-06-13 10:43:24.903379
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action import ActionModule
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    # fake input data
    all_host_data = {'hostvars': {'server1': {'var1': 1, 'var2': 2, 'var3': 3}, 'server2': {'var1': 10, 'var2': 20, 'var3': 30}, 'server3': {'var1': 100, 'var2': 200, 'var3': 300}}}
    inventory = InventoryManager(loader=DataLoader(), sources='localhost,')
    inventory.add_host(host='server1')
   

# Generated at 2022-06-13 10:43:27.661426
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None, None)
    assert action_module._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))



# Generated at 2022-06-13 10:43:38.201919
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # create mocks
    _task = {'args': {}}
    _task['args']['data'] = {'name1': 'value1', 'name2': 5}
    _task['args']['per_host'] = False
    _task['args']['aggregate'] = True

    tmp = None
    task_vars = dict()
    templar = dict()

    # call function
    try:
        set_stats = ActionModule(_task, tmp, task_vars, templar)
    except Exception as e:
        print("Error in running the test case for ActionModule method run: {}".format(e))

    print(set_stats.run(tmp, task_vars))

if __name__ == '__main__':
    test_ActionModule_run()

# Generated at 2022-06-13 10:43:40.951435
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    """
    Unit test for method run of class ActionModule
    :param self:
    :return:
    """
    pass

# Generated at 2022-06-13 10:43:51.594077
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Make an instance of ActionModule
    my_action = ActionModule(
        task=dict(action=dict(module_name='set_stats', module_args=dict(data=dict(a=1, b=2), per_host=False, aggregate=True)))
    )
    # Call run function
    ret_val = my_action.run(None, None)
    # Assert that return value is as expected
    expected_dict = dict(
        changed=False,
        ansible_stats=dict(
            data=dict(
                a=1,
                b=2
            ),
            per_host=False,
            aggregate=True
        )
    )
    assert ret_val == expected_dict

# Generated at 2022-06-13 10:43:54.901902
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: mock 'self._task.args' to test options
    # TODO: implement method run of class ActionModule and then remove this
    # function from this file
    pass

# Generated at 2022-06-13 10:43:58.286512
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule()
    action_module.set_loader(None)
    action_module.set_options(None)
    action_module.set_task(None)

# test_ActionModule()

# Generated at 2022-06-13 10:44:08.238322
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.module_utils.parsing.convert_bool import boolean

    arg_spec_mock = {'required': [], 'defaults': {}, 'argument_spec': {}, 'starargs': None, 'kwargs': None}
    task_mock = {'action': 'set_stats', 'args': {'data': {'foo': 'bar'}, 'aggregate': False, 'per_host': True}}

    obj = ActionModule(task_mock, arg_spec_mock, False, False)

    assert obj


# Generated at 2022-06-13 10:44:15.657775
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:44:18.958799
# Unit test for constructor of class ActionModule
def test_ActionModule():
    s = ActionModule('test')
    assert s.TRANSFERS_FILES == False
    assert s.VALID_ARGS == frozenset(['aggregate', 'data', 'per_host'])



# Generated at 2022-06-13 10:44:34.978038
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.parsing.convert_bool import boolean

    class VarManager:
        def __init__(self, val):
            self.val = val

        def template(self, x, **kwargs):
            return self.val


# Generated at 2022-06-13 10:44:43.641220
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialise the module
    am = ActionModule()

    # See if its a task
    assert(am._is_task())

    # See if task args are set
    assert(am._task.args == {})

    class MockTask(object):
        def __init__(self, args):
            self.args = args

    task = MockTask({'per_host': 'yes', 'aggregate': 'yes', 'data': {'foo': '{{ bar }}'}})

    am._task = task

    class MockTemplar(object):
        def template(self, data):
            return data

    #am._templar = MockTemplar()
    am._templar = MockTemplar()

    result = am.run()

    # See if stats are correct

# Generated at 2022-06-13 10:44:49.104634
# Unit test for constructor of class ActionModule
def test_ActionModule():

    _task = None
    _connection = None
    _play_context = None
    _loader = None
    _templar = None

    # TODO: Write a real unit test
    assert isinstance(ActionModule(_task, _connection, _play_context, _loader, _templar), ActionModule)

# Generated at 2022-06-13 10:45:00.620047
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleMapping
    from ansible.vars.manager import VariableManager

    # create the play
    play = Play()
    play.post_validate()

    # create the task
    task = Task()
    task.action = 'set_stats'
    task.args = dict(data=AnsibleMapping(mapping=dict(a=AnsibleUnicode('1'), aa=AnsibleUnicode('2'))))
    task._role = dict()

    # create the tqm

# Generated at 2022-06-13 10:45:03.327345
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule("/this/is/a/fake/path")
    #  TODO: make a mock of the ActionModule and test it
    assert True

# Generated at 2022-06-13 10:45:11.955916
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Initialize mock data
    task_vars = {}
    tmp = "tmp"

    # Instantiate ActionModule class
    action_module = ActionModule(load=None, variable_manager=None, loader=None)

    # Set return value of ActionBase.run()
    action_module.run = Mock(return_value={
        'failed': False,
        'msg': 'msg',
        'changed': False
    })

    # Setup args passed in to ActionModule.run()
    args = {'data': {}, 'per_host': None, 'aggregate': None}

    # Instantiate SingleTask class
    single_task = SingleTask()

    # Set args value of SingleTask
    single_task.args = args

    # Set task value of ActionModule
    action_module._task = single_task

    # Setup templ

# Generated at 2022-06-13 10:45:19.994815
# Unit test for constructor of class ActionModule
def test_ActionModule():

    action = ActionModule()

    # test run function
    tmp = None
    task_vars = {
        "ansible_play_hosts": 'localhost',
        "inventory_hostname": 'localhost',
        "group_names": ['localhost']
    }

    result = action.run(tmp, task_vars)

    assert result['ansible_stats']['per_host'] == False
    assert result['ansible_stats']['aggregate'] == True
    assert result['ansible_stats']['data'] == {}
    assert result['changed'] == False

# Generated at 2022-06-13 10:45:20.984336
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO
    assert True

# Generated at 2022-06-13 10:45:24.639422
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''Unit test for method run of class ActionModule'''
    print(str(__file__))

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar

    # TODO: write unit tests
    return

# Generated at 2022-06-13 10:45:34.286940
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:45:57.201058
# Unit test for constructor of class ActionModule
def test_ActionModule():
    try:
        # Create an object for ActionModule
        objActionModule = ActionModule()

        # Try to create an instance of ActionBase
        objActionBase = ActionBase()
    except Exception as err:
        print('ActionModule: constructor: err: {}'.format(err))


# Generated at 2022-06-13 10:46:05.041974
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Empty arguments
    args = {}
    assert not ActionModule(None, args, None, MockReporter())._task.args

    # No errors
    args = {'data': {'a': 'b'}}
    assert ActionModule(None, args, None, MockReporter())._task.args == args

    # Errors
    args = {'data': '{{a|b}}'}
    assert ActionModule(None, args, None, MockReporter())._task.args == args
    args = {'data': {'a': '{{a|b}}'}}
    assert ActionModule(None, args, None, MockReporter())._task.args == args
    args = {'data': {'{{a|b}}': 'b'}}
    assert ActionModule(None, args, None, MockReporter())._

# Generated at 2022-06-13 10:46:13.586555
# Unit test for constructor of class ActionModule
def test_ActionModule():
    global remote_user
    global remote_pass
    global remote_port
    global remote_ssh_key
    global remote_transport
    remote_user = 'root'
    remote_pass = ''
    remote_port = 22
    remote_ssh_key = ''
    remote_transport = 'ssh'
    global connection
    connection = Connection(remote_user, remote_pass, remote_port, remote_ssh_key, remote_transport)
    global module
    module = AnsibleModule(connection=connection)
    global result
    result = dict()
    result['ansible_module'] = "set_stat"

    global action_module
    action_module = ActionModule(module, task_vars=dict())
    assert isinstance(action_module, ActionModule)

    # Test method run() of class ActionModule

# Generated at 2022-06-13 10:46:15.481539
# Unit test for constructor of class ActionModule
def test_ActionModule():
	m = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

	assert m is not None

# Generated at 2022-06-13 10:46:21.935078
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult
    from ansible.module_utils.basic import AnsibleModule
    from ansible.template import Templar

    p = PlayContext()
    m = AnsibleModule(argument_spec='', supports_check_mode=True)
    t = Templar(loader=None, variables=None)
    t._templar._available_variables = {}
    task_result = TaskResult(host=None, task=None, return_data=TaskResult.clean_results({}, None, t))
    task_result._result['changed'] = False

# Generated at 2022-06-13 10:46:32.066158
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # create object of Aggregate with empty set of options
    my_object = ActionModule(dict())
    # create object of Result
    my_result = dict()
    # set default change value in result object
    my_result['changed'] = False

    # check action with empty options
    result = my_object.run(None, None)

    assert result['ansible_stats']
    assert result['ansible_stats']['aggregate'] == True
    assert result['ansible_stats']['per_host'] == False
    assert result['ansible_stats']['data'] == {}
    assert result['changed'] == False

    # create object of Aggregate with some options
    my_object1 = ActionModule(dict())

# Generated at 2022-06-13 10:46:33.066617
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, None)

# Generated at 2022-06-13 10:46:35.973211
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()
    result = am.run(tmp='/tmp', task_vars={'test_variable': 1})
    assert result.get('ansible_stats', {}).get('data', {}).get('test_variable', None) == 1

# Generated at 2022-06-13 10:46:46.761097
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from collections import namedtuple
    from ansible.module_utils.parsing.convert_bool import boolean

    Options = namedtuple('Options', ['module_name', 'forks', 'become', 'become_method', 'become_user', 'check'])
    fake_loader = None
    fake_variables = dict()
    fake_task = {'args': dict()}
    fake_templar = dict()

    # test case 1: test exception of block

# Generated at 2022-06-13 10:46:56.087474
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import json
    import unittest
    from ansible.compat.tests import mock
    from ansible.compat.tests.mock import patch

    from ansible.plugins.action import ActionBase

    from ansible.modules.system import set_stats

    # version in module_utils/__init__.py
    ANSIBLE_VERSION = '2.6.0'

    # Construct test class object of class ActionModule without calling __init__()
    #   1. Create mock object of class module_utils.basic.AnsibleModule()
    #   2. Assign values to properties of the mock
    #   3. Create mock object of class ansible.plugins.action.ActionBase()
    #   4. Assign mock to member 'self._task' of mock object of class ansible.plugins.action.ActionBase()
    #  

# Generated at 2022-06-13 10:47:48.289935
# Unit test for constructor of class ActionModule
def test_ActionModule():
    task = dict(
        action=dict(
            module='set_stats',
            args=dict(
                data={'key1': '1', 'key2': 2},
                per_host=True
            )
        )
    )
    task_ds = dict(
        action=dict(
            module='set_stats',
            args=dict(
                per_host=False
            )
        )
    )
    task_m = dict(
        action=dict(
            module='set_stats',
            args=dict(
                data=dict(
                    key1='1',
                    key2='2'
                ),
                # per_host=False
            )
        )
    )


# Generated at 2022-06-13 10:48:00.080892
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.errors import AnsibleError
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence

    # AnsibleTemplar.template(template=None, convert_bare=True, fail_on_undefined=False):
    # class AnsibleTemplar
    #  def do_template(self, data, preserve_trailing_newlines=False, escape_backslashes=True, convert_data=True,
    #                  template_ds=None, _env=None,
    #                  fail_on_undefined=False):
    # class AnsiblePluginLoader
    #  def get(self, cls, *

# Generated at 2022-06-13 10:48:07.669695
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.modules.system import set_stats
    from ansible.compat import PY2 
    from ansible.compat.tests.mock import patch
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.basic import AnsibleModule
    from ansible.utils.vars import isidentifier
    from ansible.__dict__ import __getitem__ as ansible_get_item, __setitem__ as ansible_set_item
    from ansible.__dict__ import  get as ansible_get, setdefault as ansible_setdefault
    import json

    def _checked_setdefault(self, key, item):
        if key == 'boolean_raise':
            raise Exception('boolean_raise is not convertible to boolean')

# Generated at 2022-06-13 10:48:16.741153
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        task=dict(action=dict(module='set_stats', args=dict(data=dict(foo='bar'), aggregate=True))),
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None)

    tmp = None
    task_vars = None

    result = module.run(tmp, task_vars)

    assert result['changed'] is False
    assert result['ansible_stats']['data']['foo'] == 'bar'
    assert result['ansible_stats']['aggregate'] is True
    assert result['ansible_stats']['per_host'] is False

# Generated at 2022-06-13 10:48:22.182203
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    # Construct a mock AnsibleModule object
    parameter_dict = dict(
        data=dict(
            foo='bar'
        ),
        per_host=True,
        aggregate=False
    )
    am = AnsibleModule(argument_spec=parameter_dict)
    parameter_dict['module'] = am
    module = ActionModule(**parameter_dict)

    assert module.run() == dict(
        ansible_stats=dict(
            data=dict(
                foo='bar'
            ),
            per_host=True,
            aggregate=False
        ),
        changed=False
    )

# Generated at 2022-06-13 10:48:28.971106
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(None, None, None, {})
    assert module.run(None, {'ansible_python_interpreter': '/usr/bin/python'}) == dict(changed=False, 
        ansible_stats={
            'data': {},
            'per_host': False,
            'aggregate': True})
    task = dict(data={'a': 'abc', 'b': 'bcd'}, per_host=True)
    assert module.run(None, {'ansible_python_interpreter': '/usr/bin/python'}, task) == dict(changed=False, 
        ansible_stats={
            'data': {'a': 'abc', 'b': 'bcd'},
            'per_host': True,
            'aggregate': True})

# Generated at 2022-06-13 10:48:38.067623
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # call the module constructor with a argument set and valid
    # parameters and return the created object
    module = ActionModule(argument_spec={'data': {}, 'per_host': {}, 'aggregate': {}}, checksum_filters=None, no_log=False)

    # check if the object is of class ActionModule
    if not isinstance(module, ActionModule):
        raise AssertionError("Object is not instance of class ActionModule")

    # check if the object has the complete argument_spec set
    if module._task.args.keys() != {'data', 'per_host', 'aggregate'}:
        raise AssertionError("Object has incomplete argument_spec")

# Generated at 2022-06-13 10:48:38.694559
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert issubclass(ActionModule, ActionBase)

# Generated at 2022-06-13 10:48:49.571214
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import mock
    import yaml
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_FALSE, BOOLEANS_TRUE

    pkl_content = b'\x80\x03}q\x00(X\x03\x00\x00\x00fooq\x01X\x05\x00\x00\x00valueq\x02s.'
    assert ActionModule._VALID_ARGS == frozenset(('aggregate', 'data', 'per_host'))

    # Create a temp file

# Generated at 2022-06-13 10:48:50.505710
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    print("")
    print("Hello World")
    print("")
    

# Generated at 2022-06-13 10:50:44.918975
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:50:50.183804
# Unit test for constructor of class ActionModule
def test_ActionModule():

    try:
        action_module = ActionModule(None, None)
        assert (isinstance(action_module, ActionModule))
        assert (action_module.__class__.__name__ == "ActionModule")
    except:
        print("Exception in ActionModule constructor")
        assert (False)

# Generated at 2022-06-13 10:50:58.386085
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_args = {"data": {"key1": "val1",
                            "key2": "val2"},
                   "aggregate": "True"}
    action = ActionModule(None, module_args, None)
    assert action._task.args == module_args
    module_args = {"data": {"key1": "val1",
                            "key2": "val2"},
                   "aggregate": "true"}
    action = ActionModule(None, module_args, None)
    assert action._task.args == module_args
    module_args = {"data": {"key1": "val1",
                            "key2": "val2"},
                   "aggregate": "True",
                   "per_host": "False"}
    action = ActionModule(None, module_args, None)
    assert action._task.args == module

# Generated at 2022-06-13 10:51:01.010418
# Unit test for constructor of class ActionModule
def test_ActionModule():
      # -- Construct an instance using the class
      obj = ActionModule('setup')

      # -- Verify that the instance is a type of ActionModule
      assert isinstance(obj, ActionModule)
      assert obj._task.action == 'setup'

      # -- Executing run() should run the setup module and gather facts
      # Verify that the result of run is a type of dict
      assert isinstance(obj.run(), dict)


# Generated at 2022-06-13 10:51:03.923485
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit testing method run of class ActionModule
    TODO: implement test_ActionModule_run
    '''
    pass

# Generated at 2022-06-13 10:51:09.563548
# Unit test for constructor of class ActionModule
def test_ActionModule():
    
    action = ActionModule()
    assert isinstance(action.TRANSFERS_FILES, bool)
    assert isinstance(action._VALID_ARGS, frozenset)

# Example data for ActionModule.run
example_task_args = {'aggregate': True, 'data': {'name': 'Koushik'}, 'per_host': False}

# Generated at 2022-06-13 10:51:10.267863
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()

# Generated at 2022-06-13 10:51:16.783544
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class TestActionModule(ActionModule):
        def __init__(self, *args, **kwargs):
            ActionModule.__init__(self, *args, **kwargs)
            for m in self._VALID_ARGS:
                setattr(self, m, True)

    d = {'data': {}, 'per_host': False, 'aggregate': True}
    t = TestActionModule(dict())
    t.run(None, None)
    assert t.run(None, None) == d

# Generated at 2022-06-13 10:51:22.349618
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    class Task:
        def __init__(self, args):
            self.args = args

    class Play:
        def __init__(self, name):
            self.name = name

    class PlayContext:
        pass

    class Connection:
        pass

    class ModuleExecutor:
        pass

    class PlayBookResults:
        def __init__(self):
            self.stats = {'hosts': {}}

    class Cli:
        def __init__(self):
            self.options = {'ask_pass': False}

    class Runner:
        def __init__(self):
            self.cli = Cli()
            self.results = PlayBookResults()


# Generated at 2022-06-13 10:51:25.120807
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # testing the constructor of ActionModule class
    module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(module, ActionModule)
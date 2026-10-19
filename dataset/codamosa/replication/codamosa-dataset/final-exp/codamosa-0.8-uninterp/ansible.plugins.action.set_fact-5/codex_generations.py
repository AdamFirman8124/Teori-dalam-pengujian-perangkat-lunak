

# Generated at 2022-06-13 10:42:20.832434
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Passing no argument will raise an error
    try:
        ActionModule()
    except Exception as e:
        assert isinstance(e, AnsibleActionFail)

    # Passing empty args will raise an error
    try:
        ActionModule(task=dict())
    except Exception as e:
        assert isinstance(e, AnsibleActionFail)

    # Passing key/value should not raise an error
    try:
        ActionModule(task=dict(args=dict(test='test')))
    except Exception as e:
        assert False, 'ActionModule should accept a task object with args'

# Generated at 2022-06-13 10:42:30.310076
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.playbook.play_context

    pc = ansible.playbook.play_context.PlayContext()
    pc.remote_addr = "172.16.0.1"

    a = ActionModule(pc, "/some/path")

    a.task_vars = {"foo": "bar"}

    a.task_vars["ansible_facts"] = {"test_fact": "test_value"}

    # Test with no arguments
    result = a.run()
    assert result["failed"] == True

    # Test with bad arguments, but good key names
    a.task_vars["ansible_facts"] = {}
    result = a.run(task_vars={"foo": "bar", "bar": "baz"}, args_path="/some/path")
    assert result.get("failed", False) == False


# Generated at 2022-06-13 10:42:31.751288
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:42:43.575288
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    res1 = dict()
    res1['ansible_facts'] = dict()
    res1['ansible_facts']['var1'] = 'val1'
    res1['_ansible_facts_cacheable'] = False

    res2 = dict()
    res2['ansible_facts'] = dict()
    res2['ansible_facts']['var1'] = 'val1'
    res2['ansible_facts']['var2'] = 'val2'
    res2['_ansible_facts_cacheable'] = True

    task_vars = dict()
    task_vars['ansible_variable_start_marker'] = ''
    task_vars['ansible_variable_end_marker'] = ''
    task_vars['ansible_facts_cacheable'] = True

    args1

# Generated at 2022-06-13 10:42:52.266102
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule(
        task=dict(args=dict(x=1,y=2)),
        connection=dict(module_name='test', module_path='/dev/null', module_args='', task_uuid='a1b2c3', become_method=''),
        play_context=dict(become_user='', become_pass='', remote_addr='', port=22),
        loader=None,
        variable_manager=None,
        shared_loader_obj=None
    )
    assert m.run() == dict(changed=False, ansible_facts={'x': 1, 'y': 2}, _ansible_facts_cacheable=False)


# Generated at 2022-06-13 10:42:58.040655
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule('task', 'play', {'a': 1}, loader=None, templar=None, shared_loader_obj=None)
    assert action_module is not None
    assert hasattr(action_module, '_task')
    assert hasattr(action_module, '_play')
    assert action_module._task is not None
    assert action_module._play is not None

# Generated at 2022-06-13 10:43:07.078414
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # ModuleFinder can't handle runtime module imports, so we have to use
    # the built-in import function instead of importlib.import_module.
    import collections


# Generated at 2022-06-13 10:43:14.152319
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_text
    from ansible.parsing.vault import VaultLib
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar

    class Values(object):
        extra_vars = dict()
        options = dict(vault_password='secret')

    class FakeTask(object):
        def __init__(self, role, args=None):
            self.args = args
            self.role = role
            self.vars = dict()

# Generated at 2022-06-13 10:43:19.373144
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module_args = {
        'ansible_facts': {
            'test1': True,
            'test2': False,
            'test3': 0,
            'test4': 1,
            'test5': 2,
        },
    }

    # Test when cacheable is not included in the arguments
    action = ActionModule(task=dict(action=dict()), connection=dict(), play_context=dict(), loader=dict(), templar=dict(), shared_loader_obj=None)
    assert action._templar == {}

# Generated at 2022-06-13 10:43:28.773535
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.facts import Facts
    from ansible.plugins.action.set_fact import ActionModule as SetFact
    from ansible.plugins.action.set_fact import ActionModule as SetFact

    args_dict1 = {}
    args_dict1['cacheable'] = False
    args_dict1['firstName'] = 'John'
    args_dict1['lastName'] = 'Doe'

    ansible_facts = {}

    args_dict2 = {}
    args_dict2['cacheable'] = False
    args_dict2['name'] = 'John Doe'

    ansible_facts2 = {}

    args_dict3 = {}
    args_dict3['cacheable'] = False
    args_dict3['name'] = 'John'

    ansible_facts3 = {}

    set_fact = Set

# Generated at 2022-06-13 10:43:41.237498
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.utils.vars import combine_vars

    action = ActionModule()
    action._task.args = {}
    action._task.args['key'] = 'value'
    action._task.args['boolean'] = False
    action._task.args['cacheable'] = False
    action._task.action = 'set_fact'
    action._task.name = 'set fact'
    action._task.args['register'] = 'result'

    # ansible.module_utils.basic.AnsibleModule(argument_spec=dict())
    module = type('AnsibleModule', (object,), dict(fail_json=lambda self, **kwargs:None))
    action._shared_loader_obj = {}
    action._templar = action._shared_loader_obj.get('_templar')
    #

# Generated at 2022-06-13 10:43:43.087682
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module=ActionModule(load_config=True)
    assert action_module.run

# Generated at 2022-06-13 10:43:43.785686
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:43:52.411197
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.set_fact as set_fact
    act = set_fact.ActionModule('module', 'args', 'task')
    act.templar = 'templar'
    act.task = 'task'
    assert act.run() == {}
    act.task = 'task'
    act.task.args = {'cacheable': 'str_val'}
    assert act.run() == {}
    act.task.args = {'cacheable': False}
    act.task.args.update({'a': 1, 'b': 2})
    assert act.run() == {}



# Generated at 2022-06-13 10:43:55.396706
# Unit test for constructor of class ActionModule
def test_ActionModule():
    if __name__ != '__main__':  # import test_main if run as a module
        from ansible.utils.test import test_main
        test_main()

# Generated at 2022-06-13 10:44:01.609189
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    actionModule = ActionModule(None, None)
    actionModule._execute_module = lambda *args, **kwargs:dict(ansible_facts=dict(test_fact='xyz'))
    result = actionModule.run(None, dict())
    assert result == dict(ansible_facts=dict(test_fact='xyz'))


# Generated at 2022-06-13 10:44:12.081786
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create a mock task for unit test
    task_ds = dict(
        action=dict(module_name='set_fact', module_args=dict(a=1)),
        name='test_task',
    )
    mock_task = MagicMock(**task_ds)

    # mock the connection to the host
    mock_connection = MagicMock()

    # mock the play context
    mock_play_context = MagicMock()

    # create an instance of class ActionModule
    am = ActionModule(mock_task, mock_connection, mock_play_context, loader=None, templar=None, shared_loader_obj=None)

    # compare properties of ActionModule class
    assert am._task == mock_task
    assert am._play_context == mock_play_context
    #assert am._loader == mock_loader

# Generated at 2022-06-13 10:44:22.724870
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    def check_result_dict(result, facts, cacheable):
        assert result['ansible_facts'] == facts
        assert result['_ansible_facts_cacheable'] == cacheable

    action_module = ActionModule({}, {}, task_vars={})
    # Check normal processing where fact variables are given
    result = action_module.run(None, {}, {'a': 1, 'b': 'Foo'})
    check_result_dict(result, {'a': 1, 'b': 'Foo'}, False)
    # Check normal processing where fact variables are given
    # and cacheable is set to true
    result = action_module.run(None, {}, {'a': 1, 'b': 'Foo', 'cacheable': 'True'})

# Generated at 2022-06-13 10:44:33.157578
# Unit test for method run of class ActionModule

# Generated at 2022-06-13 10:44:36.100671
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule().run(None, None) == {
        'ansible_facts': {},
        '_ansible_facts_cacheable': False
    }

# Generated at 2022-06-13 10:44:57.097755
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.task import Task
    from ansible.playbook.block import TaskBlock
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play

    task = Task()
    task._role = Role()
    task.block = TaskBlock(play=Play().load(dict(name="myplay", hosts='all', gather_facts='no', tasks=[dict(action=dict(module='debug', args=dict(msg='{{testing}}')))])))
    task.args = dict(
        ansible_facts=dict(
            package_mgr='yum',
        ),
        cacheable='yes',
        foo='bar',
    )

# Generated at 2022-06-13 10:44:58.487111
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule({}, {}, {})
    assert isinstance(action, ActionModule)

# Generated at 2022-06-13 10:44:59.154045
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    assert True

# Generated at 2022-06-13 10:45:00.520424
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None, "ActionModule is None. What up?"

# Generated at 2022-06-13 10:45:01.149745
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:45:02.674705
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert isinstance(ActionModule(), ActionModule)

# Generated at 2022-06-13 10:45:11.496729
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule({}, {}, {}, {'connection': 'local'}, 'test.yml', '/tmp')
    assert module.run({}, {'ansible_facts': {'_ansible_facts': True}}) == {'changed': False, 'ansible_facts': {'_ansible_facts': True}}

    module = ActionModule({'cacheable': True}, {}, {}, {'connection': 'local'}, 'test.yml', '/tmp')
    assert module.run({}, {'ansible_facts': {'_ansible_facts': True}}) == {'changed': False, 'ansible_facts': {'_ansible_facts': True}, '_ansible_facts_cacheable': True}


# Generated at 2022-06-13 10:45:12.349307
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:45:20.393154
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Arrange
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    tmp = None
    task_vars = {"snmp_version": "2c"}

    # Act
    result = action_module.run(tmp, task_vars)

    # Assert
    assert result['ansible_facts'] == {'ansible_net_version': '2c'}
    assert result['_ansible_facts_cacheable'] == False


# Generated at 2022-06-13 10:45:21.715983
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am1 = ActionModule()
    assert am1 is not None


# Generated at 2022-06-13 10:45:40.013662
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, dict(), dict(), dict()) is not None


# Generated at 2022-06-13 10:45:41.338834
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, None, None, None)
    assert am.TRANSFERS_FILES == False

# Generated at 2022-06-13 10:45:42.930263
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert not ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:45:43.721442
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:45:49.088944
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    a = ActionModule({}, {}, {'action_plugins': '/path/to/action_plugins'})
    a._task = MockTask()

    a._task.args = {'k': 'v'}
    result = a.run()
    assert result['ansible_facts']['k'] == 'v'


# Generated at 2022-06-13 10:45:50.563296
# Unit test for constructor of class ActionModule
def test_ActionModule():
    t = ActionModule(None, None, None)
    assert t is not None

# Generated at 2022-06-13 10:45:53.490013
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    t = ActionModule()
    t._task = {'args': {'new_var': 'new_value'}}
    result = t.run({}, {})
    assert result['ansible_facts']['new_var'] == 'new_value'

# Generated at 2022-06-13 10:45:54.378790
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule()
    assert module != None

# Generated at 2022-06-13 10:46:03.711240
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Instantiate an instance of the class under test
    action_module = ActionModule('/test/plugin/path', '/test/action_plugin_path', '/test/action_plugin_data_path')

    # Verify action plugin path
    assert action_module._action_plugin_path == '/test/action_plugin_path', 'Unexpected action plugin path'

    # Verify action plugin data path
    assert action_module._shared_loader_obj.action_loader._action_paths == ['/test/action_plugin_path', '/test/action_plugin_data_path'], \
           'Unexpected action plugin data path'

    # Verify module loader path
    assert action_module._shared_loader_obj.module_loader._module_paths == ['/test/plugin/path'], \
           'Unexpected module loader path'

    # Verify no

# Generated at 2022-06-13 10:46:12.637545
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # Construct an instance of the class ActionModule, with a real task argument
    action_module = ActionModule(dict(), dict(
        action=dict(
            _uses_shell=False,
            _raw_params="param1=value",
        ),
        _ansible_verbosity=2,
        version_info=dict(
            ansible=dict(
                version=dict(
                    string='string',
                    full='full',
                    major=1,
                    minor=2,
                ),
                git=dict(
                    commit='commit',
                    branch='branch',
                    short='short',
                    remotes='remotes',
                ),
                python='python',
            ),
        ),
    ))

    # Run the method run() on the instance
    result = action_module.run()

    # Check the results

# Generated at 2022-06-13 10:46:55.561308
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode, AnsibleUnicode
    from ansible.vars import VariableManager
    from ansible.inventory.host import Host
    from ansible.playbook.task import Task

    fact_cache = dict(foo='bar')
    fact_cacheable = dict(bar='foo')
    result = dict(ansible_facts=fact_cache, _ansible_facts_cacheable=fact_cacheable)

    # Check ansible 2.6
    variable_manager = VariableManager()
    host = Host(name='localhost')
    task = Task()
    task._variable_manager = variable_manager

    am = ActionModule(task, dict())

# Generated at 2022-06-13 10:46:57.337658
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # use native jinja if available to be consistent with the python 'in' operator
    # which has different semantics with jinja 2.8+
    a = ActionModule(dict(name='test'), 'test', True)
    assert isinstance(a, ActionModule)

# Generated at 2022-06-13 10:47:08.745893
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.plugins.action.register import ActionModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Play

    # Load the test_reg file 
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager(), host_list='./ansible/test/integration/inventory')
    variable_manager = VariableManager()

    # Create a task which will set a new fact on localhost
    task1 = dict(action=dict(module='set_fact', fact='new_fact', value='new_fact_value'))
    # Create a task which will set a new fact on localhost, with a trailing space in the key

# Generated at 2022-06-13 10:47:11.644994
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action_module = ActionModule(None, None, None, None, None, None)
    assert action_module.ACTION_VERSION == '1.0'
    assert action_module.ACTION_TYPE == 'normal'



# Generated at 2022-06-13 10:47:13.315792
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, '', None, None, None, None) is not None

# Generated at 2022-06-13 10:47:14.659753
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(None, None, None, None, None) is not None

# Generated at 2022-06-13 10:47:24.368203
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils._text import to_bytes

    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.template import Templar

    from units.mock.loader import DictDataLoader
    from units.mock.inventory import MockInventory

    class ActionModuleTest(ActionModule):
        def run(self, tmp=None, task_vars=None):
            return super(ActionModuleTest, self).run(tmp, task_vars)

    block_args = dict(task=dict(), role=dict(), connection='local', option_a='test')
    block = Block(block_args)
    block._load_included_file = lambda path: dict(tasks=[])


# Generated at 2022-06-13 10:47:34.090498
# Unit test for constructor of class ActionModule
def test_ActionModule():
    import tempfile
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils._text import to_text

    fake_loader, tmpdir = tempfile.mkdtemp(), tempfile.mkdtemp()

    # Let's ensure a temporary file for our fake loader
    module_path = tmpdir + "/test.py"
    with open(module_path, 'w') as f:
        f.write("\n")
    display.display(u"Created temporary module %s" % module_path)

    # Let's load the module

# Generated at 2022-06-13 10:47:40.359383
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """ test_ActionModule: tests the constructor of class ActionModule """
    # Successful instantiation
    ActionModule()
    # Successful instantiation with args
    ActionModule(task=10, connection=10, play_context=10, loader=10, templar=10, shared_loader_obj=10)

if __name__ == '__main__':
    test_ActionModule()

# Generated at 2022-06-13 10:47:43.133334
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert type(ActionModule(task={}, connection={}, play_context={}, loader={}, templar={}, shared_loader_obj={})) == ActionModule

# Generated at 2022-06-13 10:48:59.325287
# Unit test for constructor of class ActionModule
def test_ActionModule():
    module = ActionModule(
        play_context={
            "basedir": "project/roles/test-rol",
            "remote_addr": "192.168.1.1"
        },
        new_stdin="test_input"
    )

# Generated at 2022-06-13 10:49:01.327260
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule(task=dict(), connection=None, play_context=dict(), loader=dict(), templar=None, shared_loader_obj=None)

# Generated at 2022-06-13 10:49:11.121180
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import json
    import mock
    import pytest
    from ansible.module_utils.six import iteritems

    # Initialize ActionModule object
    m = mock.Mock()
    m.__dict__ = {'_templar': '_templar', '_task': '_task'}
    a = ActionModule(m)

    # Initialize mock objects
    m_run = mock.Mock()
    m_run.side_effect = [{'ansible_facts': {'testkey': 'testvalue'}},
                         {'ansible_facts': {'testkey2': 'testvalue2'}},
                         {'ansible_facts': {'testkey3': 'testvalue3'}}]
    a.run = m_run
    m1_convert_bool = mock.Mock()
   

# Generated at 2022-06-13 10:49:11.655169
# Unit test for constructor of class ActionModule
def test_ActionModule():
    obj = ActionModule()

# Generated at 2022-06-13 10:49:16.764150
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Parameters:
    test_action       = ActionModule()
    test_task         = 'test_value'
    test_task_vars    = 'test_value'
    test_tmp          = 'test_value'

    # Expected Result:
    expected_result = {
        'ansible_facts': {},
        '_ansible_facts_cacheable': False,
    }

    # Test ActionModule.run()
    action_result = test_action.run(test_task, test_task_vars)

    # Test Results
    assert action_result == expected_result

# Generated at 2022-06-13 10:49:17.455659
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Unit test of ActionModule constructor"""
    assert True

# Generated at 2022-06-13 10:49:18.364434
# Unit test for constructor of class ActionModule
def test_ActionModule():
    am = ActionModule(None, {})
    assert am

# Generated at 2022-06-13 10:49:20.025566
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: implement testing
    raise NotImplementedError()

# Generated at 2022-06-13 10:49:20.634982
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:49:22.889350
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = create_action_class({'a': 1, 'b': 2})
    assert isinstance(action, type)
    assert issubclass(action, ActionModule)

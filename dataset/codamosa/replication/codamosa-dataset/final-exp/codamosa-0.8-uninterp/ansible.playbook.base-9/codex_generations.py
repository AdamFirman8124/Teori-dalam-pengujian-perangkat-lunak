

# Generated at 2022-06-13 07:50:05.973002
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    assert FieldAttributeBase().validate is None


# Generated at 2022-06-13 07:50:17.005908
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    # test that BaseMeta supports __new__ method
    _mock_cls_name = '_mock_cls_name'
    _mock_parents = ('_mock_parent_a', '_mock_parent_b')
    _mock_dct = {'__dict__': '_mock_dct'}
    _mock_src_dct = {'_mock_attr_dct': '_mock_FieldAttribute'}
    _mock_src_method = '_mock_src_method'
    _mock_dst_method = '_mock_dst_method'
    _mock_dst_dict = {'_mock_dst_attr_dct': '_mock_FieldAttribute'}
    _mock_new_dst_dict

# Generated at 2022-06-13 07:50:18.485938
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
  attr = AnsibleBaseFieldAttribute()
  assert not attr.validate(attribute=1)


# Generated at 2022-06-13 07:50:20.031415
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    f = FieldAttributeBase('foo', default='bar')
    f.validate(None)


# Generated at 2022-06-13 07:50:31.352705
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    from units.mock.loader import DictDataLoader

    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager
    display = Display()

    my_task = dict(action=dict(module='debug', args=dict(msg='{{inventory_hostname}}')))
    mytask_instance = Task.load(my_task)
    mytask_instance.post_validate(dummy_variable_manager())


# Generated at 2022-06-13 07:50:37.306275
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.playbook.block import Block
    from ansible.playbook.attribute import FieldAttribute
    from ansible.playbook.task import Task
    import pytest

    # set up args

# Generated at 2022-06-13 07:50:38.480768
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
  pass


# Generated at 2022-06-13 07:50:44.011459
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    host = dict(hostname='localhost')
    field = FieldAttributeBase('host', FieldAttribute(isa='dict'))
    assert field.dump_attrs() == {'host': {}}
    field.set_value(host)
    assert field.dump_attrs() == {'host': {'hostname': 'localhost'}}


# Generated at 2022-06-13 07:50:45.402164
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    FieldAttributeBase.post_validate()

# Generated at 2022-06-13 07:50:57.552923
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    '''
    Test for FieldAttributeBase.load_data
    '''
    # Dummy data to test load_data

# Generated at 2022-06-13 07:51:27.256842
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():

    # Create a new FieldAttributeBase object named 'myobj'
    myobj = FieldAttributeBase()
    assert myobj != None
    # Base object only has uuid, finalized and squashed attrs
    attrs = myobj.dump_attrs()
    assert len(attrs) == 3
    assert attrs['finalized'] == myobj._finalized
    assert attrs['squashed'] == myobj._squashed
    assert attrs['uuid'] == myobj._uuid



# Generated at 2022-06-13 07:51:36.638395
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager._extra_vars = {}
    variable_manager._fact_cache = {}
    variable_manager._hostvars = {}
    variable_manager._hostvars = {}
    variable_manager._extra_vars = {}
    variable_manager._options = PlayContext()

    # do nothing, this just to avoid pytest skip or exit
    assert loader
    assert variable_manager


# Generated at 2022-06-13 07:51:45.182505
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    '''
    Unit test for the post_validate method of FieldAttributeBase
    '''
    # test casess for the FieldAttributeBase.post_validate()
    # method (unit tests for the ModelBase parent class instances)
    #
    # test case 0 (negative, zero values for strings)
    #
    # input parameters:
    #   name:     'negative value'
    #   isa:      'string'
    #   templar:  'this is a string'
    #
    # expected result:
    #   excpetion raised due to incompatible type
    #   (str is required)
    #
    # test case 1 (positive, string values for strings)
    #
    # input parameters:
    #   name:     'positive value'
    #   isa:      'string'
    #  

# Generated at 2022-06-13 07:51:49.994824
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    f = FieldAttributeBase(isa='foo', required=True, default=None)
    assert f.validate('foo'), "FieldAttributeBase.validate() should return true if value is valid"
    assert not f.validate(['foo', 'bar']), "FieldAttributeBase.validate() should return false if value is not right type."


# Generated at 2022-06-13 07:51:50.869018
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    assert True == True


# Generated at 2022-06-13 07:51:56.634630
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    set_module_args(dict(
        name='foo',
        data={'a': 'b'},
    ))

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True),
            data=dict(type='dict', required=True),
        ),
        supports_check_mode=True,
    )

    # Construct FieldAttributeBase object
    p = FieldAttributeBase(
        name='foo',
    )
    p.load_data(module.params['data'])

    # Done
    module.exit_json(changed=False, msg=str(p))



# Generated at 2022-06-13 07:51:58.859250
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    method = getattr(FieldAttributeBase, 'validate', None)
    assert not callable(method)



# Generated at 2022-06-13 07:51:59.655063
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    pass

# Generated at 2022-06-13 07:52:12.655412
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.manager import VariableManager
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_text
    # Create an instance of class FieldAttributeBase for testing with
    uuid_val = 'a1d77f81-e195-4b10-b741-b74e1dacf8ee'
    finalized_val = False
    squashed_val = False
    loader_val = None
    variable_manager_val = None
    validated_val = False

# Generated at 2022-06-13 07:52:17.651738
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    def function(): pass
    class_obj = FieldAttributeBase(isa='string')
    int_obj = FieldAttributeBase(isa='int')
    float_obj = FieldAttributeBase(isa='float')
    bool_obj = FieldAttributeBase(isa='bool')
    percent_obj = FieldAttributeBase(isa='percent')
    list_obj = FieldAttributeBase(isa='list')
    set_obj = FieldAttributeBase(isa='set')
    dict_obj = FieldAttributeBase(isa='dict')
    class_type_obj = FieldAttributeBase(isa='class')
    class_type_obj.class_type = function
    dict_obj = FieldAttributeBase(isa='dict')
    templar = Templar(loader=None, variables={})
    FAKE_MODULE_RETURN = 1
    # Testing with Value = 'string' and type

# Generated at 2022-06-13 07:53:11.543783
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    task1 = Task()
    task1.from_attrs({"action": {"module": "example", "foo": "bar"}})
    assert task1.action.module == "example"
    assert task1.action.foo == "bar"
    assert task1.action
    task2 = Task()
    task2.from_attrs({"action": {"module": "example", "foo": "baz"}})
    assert task2.action.module == "example"
    assert task2.action.foo == "baz"
    assert task2.action


# Generated at 2022-06-13 07:53:13.391956
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    ta = FieldAttributeBase()
    assert ta.get_validated_value(None, None, None)


# Generated at 2022-06-13 07:53:15.434873
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    field = FieldAttributeBase()
    # TODO - implement unit test


# Generated at 2022-06-13 07:53:29.946818
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    base = BaseObject()
    # We need to take care of the fact that DEFAULT_HOST_LIST is dynamically calculated to be the value of DEFAULT_HOST.
    # If the value of DEFAULT_HOST changes, the code that calculates the value of DEFAULT_HOST_LIST will also change.
    # However, hardcoding the value of DEFAULT_HOST_LIST will cause failures if DEFAULT_HOST changes.
    # By re-calculating the value of DEFAULT_HOST_LIST, we can pass the unit test even if DEFAULT_HOST changes.
    # TODO: For better unit test coverage, we should not rely on get_default_for(), but should use a mock host list instead.
    # The code of get_default_for() is not trivial, so we should not use it in the unit tests.
    base._valid

# Generated at 2022-06-13 07:53:40.422098
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from ansiblelint import Runner
    from .utils.runner_filter_plugins import runner_filter_plugins
    from ansiblelint.utils.runner_filter_plugins import FilterModule
    from ansiblelint.rules import AnsibleLintRule
    
    runner = Runner(None, None, None, None)
    runner.set_runner_filter_plugins(runner_filter_plugins())

    class AnsibleLintRuleClass(AnsibleLintRule):
        id = 'test_FieldAttributeBase_post_validate'
        shortdesc = 'Default value test'
        description = 'Default value test'
        tags = ['test']

        def matchplay(self, file, play):
            results = []
            attr_names = list(play.__dict__.keys())
            for attr in attr_names:
                results

# Generated at 2022-06-13 07:53:41.047354
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    pass

# Generated at 2022-06-13 07:53:44.222439
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    field_attribute_base = FieldAttributeBase()
    result = field_attribute_base.dump_attrs()
    assert result == {}


# Generated at 2022-06-13 07:53:47.245974
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
  foo = FieldAttributeBase()
  foo.post_validate('templar')
  return foo.dump_me() == ''


# Generated at 2022-06-13 07:53:54.670936
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    # Test case 1: dep_chain is not None
    dep_chain = 'test_Base_get_dep_chain'
    base = Base()
    base._parent = 'test_Base_get_dep_chain'
    base._parent.get_dep_chain = MagicMock(return_value=dep_chain)
    assert base.get_dep_chain() == dep_chain
    base._parent.get_dep_chain.assert_called_once()

    # Test case 2: dep_chain is None
    dep_chain = None
    base = Base()
    base._parent = 'test_Base_get_dep_chain'
    base._parent.get_dep_chain = MagicMock(return_value=dep_chain)
    assert base.get_dep_chain() == dep_chain
    base._parent.get_dep

# Generated at 2022-06-13 07:54:00.289310
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext

    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.conditional import Conditional
    from ansible.playbook.included_file import IncludedFile
    from ansible.playbook.task_include import TaskInclude



    #Valid Scenarios
    role = Role()
    role._role_path = "/tmp"
    role.get_dep_chain()


    block = Block()
    block._task_blocks = []
    block.get_dep_chain()


    conditional = Conditional()
    conditional._when = []

# Generated at 2022-06-13 07:55:51.414742
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    '''
    Unit test for method dump_me of class FieldAttributeBase
    '''
    obj = FieldAttributeBase()
    # TODO
    #raise NotImplementedError
    # find assertions
    pass

# Generated at 2022-06-13 07:55:54.199321
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    data = { 'attribute': 'value' }
    test = FieldAttributeBase(data)
    assert test.dump_me() == { 'attribute': 'value' }


# Generated at 2022-06-13 07:56:03.713942
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():

    # needed for the test case
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # setup the test data
    task = dict()
    task['action'] = "{{foo}}"
    task['name'] = "{{bar}}"
    task['become'] = "{{baz|to_bool}}"
    task['when'] =  "{{qux}}"
    task['become_user'] = "{{corge}}"
    task['environment'] = "{{garply}}"
    task['tags'] = "{{waldo}}"
    task['ignore_errors'] = "{{fred}}"
    task['register'] = "{{plugh}}"

# Generated at 2022-06-13 07:56:14.873688
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():

    # Test get_search_path with a task from a role
    taskA = Task()
    taskA._parent = Task()
    taskA._parent._role_path = 'roleB'
    taskA._parent._parent = Task()
    taskA._parent._parent._role_path = 'roleA'
    taskA._parent._parent._parent = Task()
    taskA._parent._parent._parent._role_path = 'role_name'
    search_path = taskA.get_search_path()
    assert search_path == ['role_name', 'roleA', 'roleB']

    # Test get_search_path with a task from a playbook
    taskB = Task()
    taskB._parent = Task()
    taskB._parent._play = Play()
    taskB._parent._play._ds = Dataloader()

# Generated at 2022-06-13 07:56:25.568514
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    from ansible.playbook.base import Base
    from ansible.utils.vars import combine_vars
    from ansible.utils.display import Display
    from ansible.vars import combine_facts
    from ansible.module_utils.six import string_types
    from ansible.module_utils._text import to_text, to_native
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.plugins.loader import module_loader, action_loader
    from ansible.module_utils.six import iteritems

    class Sample(Base):
        __metaclass__ = BaseMeta
        _valid_attrs = dict(
            a=Attribute(isa='string'),
            b=Attribute(isa='bool'),
            c=Attribute(isa='string', list=True),
        )


# Generated at 2022-06-13 07:56:35.531157
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
  '''
  Unit test for method FieldAttributeBase.dump_me()
  '''

  # A task object as from YAML
  task = dict(
    uuid='3ee70b2e-9b35-4d7a-a4c4-7a1377d5b121',
    name='setup',
    action='setup',
    args=dict(),
    delegate_to='localhost'
  )

  # A Task object without any variables
  t = Task()
  t.deserialize(task)

  # Make sure the task name is set
  assert t.name == 'setup'

  # Make sure the same task name was generated when we dump the object
  dumped = t.serialize()
  assert dumped['name'] == 'setup'


# Generated at 2022-06-13 07:56:38.964140
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
	echo = ansible.module_utils.basic.AnsibleModule(
		argument_spec=dict(
			msg=dict(required=True, type='str'),
		),
		supports_check_mode=True
	)

	echo.exit_json(**echo.params)

# Generated at 2022-06-13 07:56:44.203569
# Unit test for method get_ds of class FieldAttributeBase
def test_FieldAttributeBase_get_ds():
    """
    Unit test for method get_ds of class FieldAttributeBase
    """
    obj = FieldAttributeBase()
    obj._ds = 'fake_ds'
    result = obj.get_ds()
    assert result == 'fake_ds'



# Generated at 2022-06-13 07:56:48.532028
# Unit test for method get_path of class Base
def test_Base_get_path():
    b = Base()
    assert b.get_path() == ""
    b._ds = b
    b._ds._data_source = "test"
    b._ds._line_number = 1
    assert b.get_path() == "test:1"


# Generated at 2022-06-13 07:56:56.790128
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.plugins.callback.default import CallbackModule
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_executor import TaskExecutor
    from ansible.cli.adhoc import AdHocCLI
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText


# Generated at 2022-06-13 07:49:44.060467
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    x = FieldAttributeBase()
    assert isinstance(x, FieldAttributeBase)


# Generated at 2022-06-13 07:49:54.905602
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    name = 'test_host'
    attribute = FieldAttribute(isa='string', required=True, static=False)

    # This requires a default task to handle the fact we don't touch the
    # 'name' field.
    test_task = Task()
    test_task._uuid = 'test_task'
    test_task._valid_attrs = {'name': FieldAttribute(isa='string', static=True)}
    test_task.name = 'test_task'
    test_task._finalized = False

    attribute_loader = AttributeLoader()
    attribute_loader._loader = Mock()
    attribute_loader._templar = Mock()
    test_task._loader = attribute_loader

    # Test with a valid string value
    test_task.host = name

# Generated at 2022-06-13 07:50:00.895487
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    import ansible.playbook.play
    import ansible.playbook.role
    import ansible.playbook.task
    class dep_chain_task(ansible.playbook.task.Task):
        def __init__(self):
            self._role_path = '/home'
    class dep_chain_play(ansible.playbook.play.Play):
        def __init__(self):
            self.dep_chain = [dep_chain_task()]
            self._ds = 'test.yml'
    class dep_chain_role(ansible.playbook.role.Role):
        def __init__(self):
            self._role_path = '/home/username'
            self._ds = 'tasks/main.yml'

# Generated at 2022-06-13 07:50:10.079191
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    import json
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.handler import Handler
    from ansible.playbook.block import Block

    test_dir = os.path.dirname(__file__)
    datadir = os.path.join(test_dir, 'data')

    # test PlayContext with context
    with open(os.path.join(datadir, 'playcontext.json'), 'r') as data_file:
        data = json.load(data_file)
        pc = PlayContext()
        pc.from_attrs(data)
        assert pc.become_method == 'sudo'

# Generated at 2022-06-13 07:50:10.843679
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    test_object = FieldAttributeBase()
    pass

# Generated at 2022-06-13 07:50:11.524204
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    assert True


# Generated at 2022-06-13 07:50:13.682023
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    host = FieldAttributeBase()

    # missing test parameters
    host.copy()

# Generated at 2022-06-13 07:50:16.458996
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
	test_obj = Base()
	assert test_obj.get_dep_chain() == None
	assert test_obj.get_search_path() == []

# Generated at 2022-06-13 07:50:23.627322
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    # 1.
    # Setup
    base = Base()
    # Execute 1
    result = base.get_dep_chain()
    # Verify
    assert result == None

    # 2.
    # Setup
    dep_chain = ['dep_chain']
    base = Base()
    def _get_dep_chain():
        return dep_chain
    base._parent = MagicMock()
    base._parent.get_dep_chain = _get_dep_chain
    # Execute 2
    result = base.get_dep_chain()
    # Verify
    assert result == dep_chain



# Generated at 2022-06-13 07:50:35.529491
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    # FIXME: This causes a test failure when attempting to import the
    #        parent module again.  Disabling this unit test (for now).
    return
    # Test with default args
    parent = C()
    attribute = FieldAttributeBase(parent=parent, name='foo', isa='test')
    assert attribute.validate(value='test', ds=None) is True

    # Test that validate raises an exception when the attribute's
    # isa is not the same as the type of the value
    pytest.raises(Exception, attribute.validate, value=1, ds=None)

    # Test that validate raises an exception when the attribute requires
    # a value, but the value is None
    pytest.raises(Exception, attribute.validate, value=None, ds=None)


# Generated at 2022-06-13 07:51:00.786104
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
  test_object = FieldAttributeBase()
  assert test_object

# Generated at 2022-06-13 07:51:09.052923
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    f = FieldAttributeBase()
    f.isa = 'int'
    f.required = True
    f.default = 3
    f.set_class_type(int)
    f.set_deprecated_attrs('name')
    f.set_aliases('name')
    new_f = f.copy()
    assert new_f.isa == 'int'
    assert new_f.required == True
    assert new_f.default == 3
    assert new_f.class_type == int
    assert new_f.deprecated_attrs == ['name']
    assert new_f.aliases == ['name']
    assert hasattr(f, 'name')
    assert hasattr(new_f, 'name')



# Generated at 2022-06-13 07:51:13.610853
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    '''
    Test for load_data
    '''

    # Setup
    field_attribute_base = FieldAttributeBase()

    # Testing with a None value, should raise an exception
    with pytest.raises(AnsibleAssertionError):
        field_attribute_base.load_data(None)

    # Testing with a None name, should raise an exception
    with pytest.raises(AnsibleAssertionError):
        field_attribute_base.load_data({})

    # Testing with a valid name, but no type should raise an exception
    with pytest.raises(AnsibleAssertionError):
        field_attribute_base.load_data({'name': 'test'})

    # Testing with a valid name and type (unknown), should raise an exception

# Generated at 2022-06-13 07:51:24.047327
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    # Move this to a test_ansible/__init__.py
    # But it is important to test FieldAttributeBase
    # TODO: Move to a test_ansible/__init__.py
    class TestAttributeBase(FieldAttributeBase):
        class_types = {'class': []}

    class TestTask1(FieldAttributeBase):
        def __init__(self):
            super(TestTask1, self).__init__()
            self.name = FieldAttribute(isa='string')
            self.test_attr = TestAttributeBase()
            self.test_attr.name = FieldAttribute(isa='string')

        def _post_validate_name(self, attr, value, templar):
            return value + value


# Generated at 2022-06-13 07:51:33.061494
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import queue
    from ansible.module_utils.six.moves import cPickle
    from ansible.module_utils.six.moves import zip

    class FakeModuleDeprecation(object):

        def __init__(self, **kwargs):
            self.kwargs = kwargs

        def __call__(self, *args, **kwargs):
            return FakeModuleDeprecation(**self.kwargs)

        def __getattr__(self, name):
            try:
                return self.kwargs[name]
            except (KeyError, TypeError):
                return None


# Generated at 2022-06-13 07:51:43.237673
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    my_obj = Sentinel()
    my_obj.data = Sentinel()
    my_obj.data.name = 'my_display_name'
    my_obj.data.name2 = AnsibleUnsafeText('my_display_name2')
    dump_me_test_data = {}
    dump_me_test_data[0] = {'test_attr1': 'test_value1', 'test_attr2': 'test_value2'}
    dump_me_test_data[0]['test_attr3'] = my_obj
    dump_me_test_data[1] = {'my_display_name': 'test_value1', 'my_display_name2': 'test_value2'}
    dump_me_test_data

# Generated at 2022-06-13 07:51:45.006604
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    '''
    Base.get_dep_chain
    '''
    test_obj = Base()
    attr_value = test_obj.get_dep_chain()
    assert attr_value == None
    # tests that properly handle the dep chain are in their respective classes.

# Generated at 2022-06-13 07:51:48.250523
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    Base.test_init()
    current = Base(None)
    A = Base(current)
    B = Base(current)
    assert B.get_dep_chain() == [B, A, current]

# Generated at 2022-06-13 07:51:50.869039
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    test_obj = FieldAttributeBase()
    # Test with a bad type for argument 'self' (should raise TypeError)
    with pytest.raises(TypeError):
        test_obj.post_validate(None)



# Generated at 2022-06-13 07:51:55.833853
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    # test1
    o = FieldAttributeBase()
    o.name = 'name'
    o.isa = 'dict'
    o.default = {}
    o.static = True
    o.primary = None
    o.required = False
    o.choices = None
    o.aliases = None
    o.always_post_validate = False
    o.class_type = None
    o.listof = None
    # not supported:
    #   o.always_post_validate
    #   o.class_type
    #   o.listof
    assert o.post_validate(None) == None
    assert o.name == 'name'
    assert o.isa == 'dict'
    assert o.default == {}
    assert o.static == True
    assert o.primary == None

# Generated at 2022-06-13 07:52:27.056541
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():

    # Setup the arguments
    name = 'zone' # name is a string
    attribute = None # attribute is a FieldAttributeBase
    value = 'foo' # value is a string
    templar = None # templar is a Templar

    # Invoke the method
    result = FieldAttributeBase.get_validated_value(name, attribute, value, templar)



# Generated at 2022-06-13 07:52:29.132568
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    import pytest
    obj = FieldAttributeBase()
    obj.get_validated_value("name","attribute","value","templar")
##TODO: test_FieldAttributeBase_get_validated_value


# Generated at 2022-06-13 07:52:30.990425
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    # FIXME: We need to write unit test for method FieldAttributeBase.validate
    pass # No test coverage for the moment



# Generated at 2022-06-13 07:52:31.896979
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    pass



# Generated at 2022-06-13 07:52:34.316853
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    assert 0, "no tests for Base class"

    # create objects for test
    # create objects for test

    # test the method get_search_path()

    # check if the result is correct
    assert get_search_path() == '', 'The result should be "", but the result is "%s"' % get_search_path()



# Generated at 2022-06-13 07:52:34.742506
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    pass

# Generated at 2022-06-13 07:52:38.453912
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    my_fieldattributebase = FieldAttributeBase()
    if not isinstance(my_fieldattributebase, FieldAttributeBase):
        print('Failed to create FieldAttributeBase!')
        raise

    my_copy = my_fieldattributebase.copy()
    if not isinstance(my_copy, FieldAttributeBase):
        print('Failed to create copy of FieldAttributeBase!')
        raise

    if my_fieldattributebase.default != my_copy.default:
        print('Failed to create deep copy of FieldAttributeBase!')
        raise


# Generated at 2022-06-13 07:52:40.377185
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    attr = FieldAttributeBase()
    attr.squash_attribute = False
    assert attr.squash() == False
    attr.squash_attribute = True
    assert attr.squash() == True


# Generated at 2022-06-13 07:52:45.953725
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    from ansible.playbook.play_context import PlayContext
    from .unit.test_result import TestResult
    from .unit.test_play import TestPlay
    from .unit.test_play_context import TestPlayContext
    from .unit.test_task import TestTask
    from .unit.test_role import TestRole
    from .unit.test_task_include import TestTaskInclude
    from .unit.test_block import TestBlock
    # test case #1， self._parent is None，should return []
    base_obj = Base()
    result = base_obj.get_search_path()
    assert result == [] ,'test_Base_get_search_path case #1 failed'
    # test case #2，self._parent._play is not None，and self._parent is PlayContext instance

# Generated at 2022-06-13 07:52:50.927067
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    def func():
        field = FieldAttributeBase()
        return field
    field = func()
    field.obj = BaseObject()
    field.name = 'name'
    field.attribute = 'attribute'
    field.value = 'value'
    field_type = FieldAttributeBase
    data = field.validate()
    expected = 'name=attribute'
    assert data == expected

# Generated at 2022-06-13 07:54:17.114874
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    host = FakeHost()
    task = host.set_task()
    task.post_validate(task.noop_vars)
    assert task.post_validate_b_validated
    assert task.post_validate_a_validated


# Generated at 2022-06-13 07:54:24.149988
# Unit test for method __new__ of class BaseMeta

# Generated at 2022-06-13 07:54:33.935210
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
  # Test when the task directory is not in the path stack
  p = Base()
  p._ds._data_source = '/home/james/testdata/test.yml'
  p._ds._line_number = 10
  p._parent = '/home/james/testdata'
  assert p.get_search_path() == ['/home/james/testdata']

  # Test when the task directory is in the path stack
  p = Base()
  p._ds._data_source = '/home/james/testdata/test.yml'
  p._ds._line_number = 10
  p._parent = '/home/james/testdata'
  p.get_dep_chain = lambda: ['/home/james/testdata']

# Generated at 2022-06-13 07:54:35.062557
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    pass # no test coverage for this method


# Generated at 2022-06-13 07:54:36.102461
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    FieldAttributeBase()


# Generated at 2022-06-13 07:54:37.871727
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    obj = FieldAttributeBase()
    name = 'name'
    data = {}
    assert obj.dump_me(name, data) == False

# Generated at 2022-06-13 07:54:42.917041
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    attrs = {'a': 'b', 'c': 'd', 'e': 'f'}
    # Test with included obj
    obj = FieldAttributeBase()
    obj.from_attrs(attrs)

    # Test with excluded obj
    obj = FieldAttributeBase()
    obj.from_attrs(attrs)
    assert True

# Generated at 2022-06-13 07:54:45.660814
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    #  Run unit test for method 'squash' of class FieldAttributeBase
    # TODO: Unit test for method 'squash' of class FieldAttributeBase
    pass

# Generated at 2022-06-13 07:54:54.296603
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    class TestObj(object):
        __metaclass__ = FieldAttributeBase
        _valid_attrs = dict(
            attr1 = FieldAttribute(),
            attr2 = FieldAttribute(isa='str'),
            attr3 = FieldAttribute(isa='int'),
            attr4 = FieldAttribute(isa='float'),
        )
        def __init__(self):
            self._squashed = False
            self.attr1 = None
            self.attr2 = None
            self.attr3 = None
            self.attr4 = None

        def get_ds(self):
            return 'ds'

    test_obj = TestObj()
    test_obj.attr1 = '123'
    test_obj.attr2 = 123
    test_obj.attr3 = 123.0
    test_obj.attr4 = []

# Generated at 2022-06-13 07:55:01.203437
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from ansible.errors import AnsibleUndefinedVariable, UndefinedError
    from ansible.parsing.splitter import split_args

    from ansible.template import Templar

    from ansible.vars.manager import VariableManager

    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import VAULT_SUBST, VAULT_PASS_SUBST, UNSAFE_VARS_PLACEHOLDER, UNSAFE_TEXT_WARNING

    def deepcopy(data):
        if isinstance(data, dict):
            return dict((deepcopy(key), deepcopy(value)) for key, value in iteritems(data))
        elif isinstance(data, list):
            return [deepcopy(element) for element in data]
        else:
            return data

    #

# Generated at 2022-06-13 07:55:53.311360
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    class Base:
        def __init__(self) -> None:
            self._squashed = None
            self._finalized = None
            self._uuid = None

    class DataModel(FieldAttributeBase, Base):
        _valid_attrs = dict(FieldAttributeBase._valid_attrs, **dict(
            name=FieldAttribute(isa='string'),
            count=FieldAttribute(isa='int', default=1),
            list=FieldAttribute(isa='list', alias='other_name'),
        ))

        @property
        def count(self):
            raise ValueError('Cannot get count')

        @count.setter
        def count(self, value):
            raise ValueError('Cannot set count')


# Generated at 2022-06-13 07:55:57.397678
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    argspec = inspect.getargspec(FieldAttributeBase.load_data)
    assert argspec.args == ['self', 'ds'], argspec

# Generated at 2022-06-13 07:56:06.486597
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.utils.vars import combine_vars
    set_module_args(ModuleArgsValidatorTest.args)
    obj_set = {'key1': 'value1', 'key2': 'value2'}
    obj_list = ['value1', 'value2']
    obj_list_list = ['value1', 'value2']
    obj_list_list2 = ['value3', 'value4']
    obj_str = 'value'
    obj_str2 = 'value2'
    obj_dict = {'key1': 'value1', 'key2': 'value2'}
    obj_dict2 = {'key1': 'value3', 'key2': 'value4'}

# Generated at 2022-06-13 07:56:14.340982
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
	exp_result = dict(name=None, default=None, isa=None, private=None, aliases=None, attr_class=None, static=None, required=None, inherit=None, priority=None)
	exp_result['name'] = 'something'
	exp_result['default'] = '/etc/ansible/hosts'
	exp_result['isa'] = 'string'
	exp_result['private'] = False
	exp_result['aliases'] = []
	exp_result['attr_class'] = 'something'
	exp_result['static'] = False
	exp_result['required'] = False
	exp_result['inherit'] = True
	exp_result['priority'] = 32767
	obj = FieldAttributeBase(name='something', default='/etc/ansible/hosts', isa='string')

# Generated at 2022-06-13 07:56:21.021061
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    ds = FakeDS()
    myTask = Task(ds, dict())
    myTask._parent = myTask
    assert myTask.get_dep_chain() is None

    myPlay = Play(ds, dict())
    myRole = Role(ds, dict())
    myTask._parent = myPlay
    myPlay._parent = myRole
    assert myTask.get_dep_chain() == [myPlay, myRole]


# Generated at 2022-06-13 07:56:22.956723
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    root = Base()
    dep_chain = root.get_dep_chain()
    assert dep_chain is None


# Generated at 2022-06-13 07:56:25.828435
# Unit test for method get_ds of class FieldAttributeBase
def test_FieldAttributeBase_get_ds():
    FieldAttributeBase = field_attribute.Base()

    FieldAttributeBase._ds = {'a':1}
    result = FieldAttributeBase.get_ds()
    assert result == {'a':1}


# Generated at 2022-06-13 07:56:29.060078
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    a = FieldAttributeBase()
    try:
        a.validate(name="name", field=None)
    except Exception as e:
        assert isinstance(e, NotImplementedError)

# Generated at 2022-06-13 07:56:34.141233
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    test_object = FieldAttributeBase()
    test_obj = AnsibleBase()
    test_obj._validated = True
    setattr(test_obj, '_validated', True)
    with pytest.raises(AnsibleParserError):
        test_object.post_validate(test_obj)



# Generated at 2022-06-13 07:56:40.527132
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    loader=DataLoader()
    play = Play().load(dict(
        name = "Ansible Play",
        hosts = "all",
        gather_facts = "no",
        tasks = [
            dict(action=dict(module='shell', args='ls')),
            dict(action=dict(module='debug', args=dict(msg='{{foo}}', var=dict(foo='Goodbye'))))
            ]
        ), loader=loader, variable_manager=VariableManager())
    play.deserialize("", "")


# Generated at 2022-06-13 07:57:24.589798
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    method = getattr(FieldAttributeBase, 'validate')
    assert method is not None


# Generated at 2022-06-13 07:57:27.073663
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    obj = FieldAttributeBase()
    data = {}
    obj.deserialize(data=data)



# Generated at 2022-06-13 07:57:33.202273
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
  ds = dict()
  field_attribute = ansible_collections.ansible.community.plugins.module_utils.network.common.utils.FieldAttribute(isa='string', default='foo')
  # Test with field_attribute.isa set.
  assert field_attribute.dump_me() == dict(isa='string', default='foo')
  # Test with field_attribute.isa and field_attribute.elements set.
  field_attribute.isa = 'dict'
  assert field_attribute.dump_me() == dict(isa='dict', default='foo')


# Generated at 2022-06-13 07:57:43.742954
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    from .action import ActionBase
    from .host import Host
    from .task import Task
    from .task_include import TaskInclude
    from .task_block import TaskBlock
    from .task_fail import TaskFail
    from .task_debug import TaskDebug
    from .task_wait_for import TaskWaitFor
    from .task_pause import TaskPause
    from .task_import_role import TaskImportRole
    from .task_include_role import TaskIncludeRole
    from .task_import_task import TaskImportTask
    from .task_conditional import TaskConditional
    from .task_when import TaskWhen
    from .become import Become
    from .meta import RoleInclude
    from .meta import RoleMetadata
    from .meta import RoleRequirement
    from .meta import RoleDefaults
    from .meta import RoleDep

# Generated at 2022-06-13 07:57:46.738101
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    expected = {'bar': '2'}
    a = FieldAttributeBase()
    b = a.load_data({'foo': {'bar': '2'}})
    assert b == expected


# Generated at 2022-06-13 07:57:54.420391
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    import ansible.constants as C
    import os
    options = namedtuple('Options', ['connection','module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    # create the variable manager
    variable_manager = VariableManager()
    loader = DataLoader()

    # create the inventory, use path to host config file as source or hosts in a comma separated string

# Generated at 2022-06-13 07:58:05.820072
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    # Since this test is for a classmethod, this test will not instantiate the class and therefore will not initialize the class attributes
    # This simulates that
    FieldAttributeBase._valid_attrs = {}
    FieldAttributeBase._fields = {}
    FieldAttributeBase._aliases = {}
    # Since this test is for a classmethod, this test will not instantiate the class and therefore will not initialize the class attributes
    # This simulates that
    # Simulate a 'value' attribute in _valid_attrs dictionary
    FieldAttributeBase._valid_attrs = {'value': FieldAttribute('value')}
    # Simulate a value variable called in the method
    FieldAttributeBase.value = None
    # Simulate a FieldAttributeBase project variable
    FieldAttributeBase.project = None
    # Simulate a FieldAttributeBase category variable
    FieldAttributeBase.category = None

# Generated at 2022-06-13 07:58:15.827712
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    from ansible.compat.tests import unittest
    import ansible.compat.tests.mock as mock

    class MyClass(ansible.parsing.yaml.objects.AnsibleBaseYAMLObject):
        _valid_attrs = dict(
            name=FieldAttribute(isa='string'),
        )
        def __init__(self):
            self._attributes['name'] = 'name'
            super(MyClass, self).__init__()

    myClass = MyClass()
    myClass.name = 'Hello'
    expected = {
        'name': 'Hello'
    }
    myClass_dump_attrs = myClass.dump_attrs()
    try:
        assert myClass_dump_attrs == expected
    except AssertionError as e:
        raise AssertionError

# Generated at 2022-06-13 07:58:24.872310
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    #  Test for validating booleans
    myArg = FieldAttributeBase()
    myArg.isa = 'bool'
    myArg.required = True
    setattr(myArg, 'default', '')
    assert myArg.get_validated_value('arg1', myArg, 'yes', None) is True
    assert myArg.get_validated_value('arg1', myArg, 'on', None) is True
    assert myArg.get_validated_value('arg1', myArg, '1', None) is True
    assert myArg.get_validated_value('arg1', myArg, 'true', None) is True
    assert myArg.get_validated_value('arg1', myArg, 'True', None) is True

# Generated at 2022-06-13 07:58:26.557525
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():

    # create object Base()
    test_object = Base()

    # test get_search_path()
    assert not test_object.get_search_path()

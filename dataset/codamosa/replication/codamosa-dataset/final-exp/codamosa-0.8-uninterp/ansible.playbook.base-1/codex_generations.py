

# Generated at 2022-06-13 07:49:57.870159
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    from ansible.module_utils.six import string_types
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import isidentifier
    from ansible.module_utils._text import to_text
    from ansible.module_utils._text import to_native
    from ansible.errors import AnsibleUndefinedVariable, AnsibleParserError, AnsibleError
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.utils.boolean import boolean
    from ansible.template import Templar
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import Call

# Generated at 2022-06-13 07:49:59.197494
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    FieldAttributeBase()

# Generated at 2022-06-13 07:50:09.647152
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    '''
    Test to ensure post_validatation works for value types such as
    int, float and so forth.
    '''
    name = FieldAttribute(isa='string')
    nameObject = FieldAttributeBase(name)
    nameObject._attributes['name'] = 'ansible'
    nameObject._validate_name('name')
    nameObject._post_validate_name(name, 'ansible', MagicMock())

    nameInt = FieldAttribute(isa='int')
    name_object = FieldAttributeBase(nameInt)
    name_object._attributes['nameInt'] = '20'
    name_object._validate_nameInt('nameInt')
    setattr(name_object, 'nameInt', 20)
    assert name_object.nameInt == 20

# Generated at 2022-06-13 07:50:20.292615
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    attr = FieldAttribute()
    attr.isa = 'string'
    assert to_text(1) == FieldAttributeBase().get_validated_value('foo', attr, 1, None)

    attr = FieldAttribute()
    attr.isa = 'int'
    assert 1 == FieldAttributeBase().get_validated_value('foo', attr, 1, None)
    attr = FieldAttribute()
    attr.isa = 'float'
    assert 1.0 == FieldAttributeBase().get_validated_value('foo', attr, 1, None)
    attr = FieldAttribute()
    attr.isa = 'bool'
    assert True == FieldAttributeBase().get_validated_value('foo', attr, True, None)
    attr = FieldAttribute()
    attr.isa = 'percent'

# Generated at 2022-06-13 07:50:23.491875
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    # Create an instance of FieldAttributeBase
    fb = FieldAttributeBase()

    # Call method get_validated_value of FieldAttributeBase
    fb.get_validated_value('sample','','','')



# Generated at 2022-06-13 07:50:35.379398
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    '''
    Unit test for method get_search_path of class Base
    '''
    # Create a Base object and set the _parent attribute
    base_obj = Base()
    base_obj._parent = base_obj
    base_obj._parent._play = base_obj._parent

    # Create a mock object for the role_path attribute
    role_path = 'role_path'

    # set the search path of the Base object
    path_stack = [role_path]
    base_obj._parent._play._ds = base_obj._parent._play
    base_obj._parent._play._ds._line_number = 1

    # search the path_stack for the role path
    assert base_obj.get_search_path() == path_stack

    # Set the _parent to None and check the role path
    base_obj._

# Generated at 2022-06-13 07:50:39.805178
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    a = FieldAttributeBase('test')
    a.loader = DictDataLoader({'foo': 'bar'})
    a.check_vars = False
    result = a.squash(None, {'foo': 'bar'})
    assert result == {'foo': 'bar'}


# Generated at 2022-06-13 07:50:48.979845
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    test_obj = FieldAttributeBase()
    assert isinstance(test_obj, FieldAttributeBase)
    mock_attr = MagicMock()
    mock_ds = MagicMock()
    mock_ds.get_ds.return_value = mock_ds
    mock_ds.get_ds_type.return_value = "task"
    mock_ds.task_include.return_value = False
    test_obj.validate(mock_attr, mock_ds)


# Generated at 2022-06-13 07:51:01.484961
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.splitter import parse_kv

    dl = DataLoader()
    inv_manager = InventoryManager(loader=dl)
    var_manager = VariableManager(loader=dl, inventory=inv_manager)

    def combine_vars_custom(a,b):
        return combine_vars(a,b)

    def parse_kv_custom(string, errors='ignore'):
        return parse_kv(string, errors=errors)


# Generated at 2022-06-13 07:51:04.744758
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():

    # assert that dump_me raises exception for abstract classes

    with pytest.raises(NotImplementedError, match="This method must be overridden in subclasses"):
        FieldAttributeBase().dump_me()



# Generated at 2022-06-13 07:51:30.942879
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    # The following are examples which must be fixed

    # Initialize and run the test
    fb = FieldAttributeBase()
    fb.validate(fb, None)



# Generated at 2022-06-13 07:51:40.054823
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
  ds = {'a': 1, 'b': 2, 'c':3}
  tests = [
    # (expected, method_name, args)
    ({'a': 1}, 'a'),
    (None, 'a', [None]),
    ({'a': 1, 'b':2, 'c': 3}, None),
    (None, None, [None]),
  ]
  for (expected, method_name, args) in tests:
    result = FieldAttributeBase(ds).dump_me(method_name, args)
    assert result == expected
    # TODO: test AnisbleFail exception


# Generated at 2022-06-13 07:51:48.705332
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    '''
    Test the method FieldAttributeBase.dump_me()
    '''

    obj = FieldAttributeBase()
    x = obj.dump_me('')
    assert x == {}, "Expected: {}, Got: {}".format({}, x)

    obj = FieldAttributeBase(
        vars="vars"
    )
    x = obj.dump_me('vars')
    assert x == {}, "Expected: {}, Got: {}".format({}, x)



# Generated at 2022-06-13 07:51:54.976811
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.callback import CallbackBase
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['source'])
    variable_manager.set_inventory(inventory)
    callback = CallbackBase()
    play_context = PlayContext()
    FABase = FieldAttributeBase(play_context=play_context)
    setattr(FABase, 'name', 'test_value')
    FABase.squash()


# Generated at 2022-06-13 07:51:56.369746
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    b = Base()
    assert b.get_dep_chain() == None
    

# Generated at 2022-06-13 07:51:57.488230
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    FieldAttributeBase.load_data()


# Generated at 2022-06-13 07:52:02.292264
# Unit test for method get_ds of class FieldAttributeBase
def test_FieldAttributeBase_get_ds():
    my_class = FieldAttributeBase(my_attr='my_attr', my_class_type='my_class_type')
    return_value = my_class.get_ds()
    assert return_value == 'my_attr'

# Generated at 2022-06-13 07:52:07.724970
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    field_attribute_base = FieldAttributeBase()
    assert field_attribute_base.dump_me() == {
        '__ansible_module__': 'ansible.parsing.yaml.objects.FieldAttributeBase',
        'required': False,
        'isa': None,
        'listof': None
    }


# Generated at 2022-06-13 07:52:10.533747
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    field_attribute_base = FieldAttributeBase()
    assert field_attribute_base.dump_me('t') == 't'

# Generated at 2022-06-13 07:52:15.482583
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    fixture = FieldAttributeBase(isa = 'some_isa', required = False, )
    assert fixture.isa == 'some_isa'
    assert fixture.required == False
    data = dict()
    assert fixture.post_validate(data) is None
    assert fixture.isa == 'some_isa'
    assert fixture.required == False

# Generated at 2022-06-13 07:52:45.071098
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    # Constructing object
    obj = FieldAttributeBase()

    # Calling method
    obj.squash()

    # Testing for exceptions


# Generated at 2022-06-13 07:52:47.329353
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    object = FieldAttributeBase()
    name = dict()
    raise Exception(object.validate(name))


# Generated at 2022-06-13 07:52:54.495488
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    # Test when nothing is set and no defaults are provided
    f = FieldAttributeBase()
    attrs = dict(key1='val1', key2=2, key3=['list of stuff'])
    f.from_attrs(attrs)
    assert f.key1 == 'val1'
    assert f.key2 == 2
    assert f.key3 == ['list of stuff']
    assert f._finalized
    assert f._squashed

    # Test when defaults are provided
    f = FieldAttributeBase(defaults=dict(key1='val1', key2=2, key3=['list of stuff']))
    attrs = dict(key2=3, key3=['different', 'list'])
    f.from_attrs(attrs)
    assert f.key1 == 'val1'

# Generated at 2022-06-13 07:52:57.903281
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    obj = FieldAttributeBase()
    field_name = 'test_field'
    field_value = 'test_value'
    assert obj.validate(field_name, field_value) is None

# Generated at 2022-06-13 07:53:00.979277
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    '''
    Unit test for method dump_me of class FieldAttributeBase
    '''
    field_attribute_base = FieldAttributeBase()
    assert field_attribute_base.dump_me() is None


# Generated at 2022-06-13 07:53:05.591663
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    fb = FieldAttributeBase()
    fb2 = FieldAttributeBase()
    fb3 = FieldAttributeBase()
    fb.from_attrs({})
    fb2.from_attrs({})
    fb3.from_attrs({})



# Generated at 2022-06-13 07:53:16.118917
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    # set up obj
    obj = AttributeTest()

    # set up expected

# Generated at 2022-06-13 07:53:25.631488
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    # fix pylint false positive bug because of
    # https://github.com/PyCQA/pylint/issues/1811
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             "ansible_test_data/tasks/test_file_include.yaml")
    ds = DataLoader()
    task_ds = ds.load_from_file(file_path)
    tasks = Task.load(task_ds[0], task_ds._play)
    assert tasks[0].get_dep_chain() == None


# Generated at 2022-06-13 07:53:27.915012
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    o = FieldAttributeBase()
    assert o.post_validate(templar=None) is None

# Generated at 2022-06-13 07:53:38.573589
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    data = dict()

    # deserialize
    # test with FieldAttributeBase(name, default=None, isa=None, listof=None, class_type=None, static=False, aliases=['foo'])
    for _name in ['_name', 'name', 'foo']:
        # test with type(None)
        f = FieldAttributeBase(_name)
        before = f.attr_is_set()
        f.deserialize(data)
        after = f.attr_is_set()
        assert before == after
        # test with type(list)
        f = FieldAttributeBase(_name, listof=str)
        before = f.attr_is_set()
        f.deserialize(data)
        after = f.attr_is_set()
        assert before == after
        # test with type(

# Generated at 2022-06-13 07:54:10.982322
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    g = AnsibleGatheringTask()
    g.from_attrs({'name':'gather_facts', 'action':'setup'})


# Generated at 2022-06-13 07:54:13.993354
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    test = FieldAttributeBase(isa='string')
    assert test.get_validated_value('name', test, 'value', 'templar') == 'value'

# Generated at 2022-06-13 07:54:18.470245
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    if __name__ == '__main__':

        # Test for method deserialize (ClassFieldAttributeBase)
        # This is the default, so it does not need to be tested
        my_obj = FieldAttributeBase()
        assert my_obj.deserialize(None, None) == None



# Generated at 2022-06-13 07:54:29.285824
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
  failed_tests = []
  for test_values in test_values_FieldAttributeBase_load_data:
    my_obj = FieldAttributeBase()
    test_params = test_values.get('test_params', {})
    my_attr = test_params.get('my_attr', None)
    ds = test_params.get('ds', None)

    ## set up test values
    my_obj.my_attr = my_attr

    # run test
    try:
      result = my_obj.load_data(ds)
    except Exception as e:
      result = 'Exception'

    # report results

# Generated at 2022-06-13 07:54:36.407001
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    '''
    Post validation of an AnsiobleObject.

    '''
   
    data = dict(
        _loader=dict(),
        _variable_manager=dict(),
        _validated=False,
        _finalized=False,
        _uuid=str(),
        _attributes=dict(),
        _attr_defaults=dict(),
        _alias_attrs=dict(),
        _squashed=False
    )

    # Create mock objects
    obj = FieldAttributeBase()
    obj._loader = mock.Mock(**data)
    obj._variable_manager = mock.Mock(**data)
    obj._validated = mock.Mock(**data)
    obj._finalized = mock.Mock(**data)
    obj._uuid = mock.Mock(**data)
    obj._att

# Generated at 2022-06-13 07:54:47.443141
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    from ansible.compat.tests.mock import MagicMock, patch

    # Data for testing
    class ObjToDump(FieldAttributeBase):
        pass

    obj = ObjToDump()
    obj.vars = dict()
    obj.hosts = []
    obj.connection = 'local'
    obj.delegate_to = None
    obj.no_log = True

    attrs = dict()
    attrs['vars'] = dict()
    attrs['hosts'] = []
    attrs['connection'] = 'local'
    attrs['delegate_to'] = None
    attrs['no_log'] = True

    # Initializing mocks
    mock_type = MagicMock()
    mock_type.__name__ = 'mocktype'

    # Start test
    obj.from_att

# Generated at 2022-06-13 07:54:55.410657
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    target = FieldAttributeBase(required=True, private=False, default=None, always_post_validate=False, attribute=None, class_type=None,
                                choices=None, isa=None, listof=None, static=False)
    target.name = 'name'
    self = target
    # Case 1
    attrs = FieldAttributeBase(required=True, private=False, default=None, always_post_validate=False, attribute=None, class_type=None,
                               choices=None, isa=None, listof=None, static=False)
    attr = attrs
    value = 'value'
    templar = 'templar'
    #assert self.get_validated_value(name, attr, value, templar) == 'value'
    # Case 2
   

# Generated at 2022-06-13 07:54:58.479083
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    # Create the object
    obj = FieldAttributeBase("dummy")

    # Try to call method
    try:
        obj.validate("", "dummy")
    except NotImplementedError:
        pass

# Generated at 2022-06-13 07:55:01.018093
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    o = FieldAttributeBase()
    assert o._post_validate_name(None,True,None) is None


# Generated at 2022-06-13 07:55:11.231429
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    import pytest
    import sys

    # The code below is commented out, as it fails on Python3.
    # # This tests FieldAttributeBase.dump_attrs()
    # # A base object with 1 attribute is created and then parsed and
    # # dumped to a YAML. The dumped YAML is then parsed by the same
    # # parser to give the same object.
    #
    #
    # # This is the string that is dumped to the YAML
    # dumped_yaml_str = """\
    # cat:
    #   name: Fluffy
    #   tags:
    #     - cuddly
    #     - hairy
    #   finalize: true
    #   squashed: false
    #   uuid: c06c48ce-6adf-4505-9d1e-c5

# Generated at 2022-06-13 07:55:42.163864
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    # Given: An object of class FieldAttributeBase
    fieldAttributeBaseInstance = FieldAttributeBase
    # When: test_FieldAttributeBase_dump_me is called
    method_return = fieldAttributeBaseInstance.dump_me()
    # Then: test_FieldAttributeBase_dump_me completes without throwing an exception
    assert True


# Generated at 2022-06-13 07:55:53.182627
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    c = AnsibleCollectionRef()
    t = Task()
    t.deserialize({'name': 'foobar'})
    assert t.name == 'foobar'
    collection_ref = Task()
    collection_ref.deserialize({'collections': [c]})
    assert collection_ref.collections[0] == c
    assert collection_ref.finalized == False
    assert collection_ref.squashed == False
    assert collection_ref._uuid == None
    assert collection_ref.loop_control is None
    assert collection_ref.loop == 'default'
    assert collection_ref.name == 'default'
    assert collection_ref.tags == []
    assert collection_ref.when == ''
    assert collection_ref.always_run == False
    assert collection_ref.private == False

# Generated at 2022-06-13 07:56:02.039314
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    '''
    Unit test for method validate of class FieldAttributeBase
    '''

    # Set up test environment
    test_obj = FieldAttributeBase(
        required=True,
        choices=['yes', 'no'],
        isa='string',
        private=True,
        deprecated=True,
    )

    assert test_obj._kwargs['required'] == True
    assert test_obj._kwargs['choices'] == ['yes', 'no']
    assert test_obj._kwargs['isa'] == 'string'
    assert test_obj._kwargs['private'] == True
    assert test_obj._kwargs['deprecated'] == True


# Generated at 2022-06-13 07:56:03.210291
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    a = FieldAttributeBase()
    a.deserialize(None)

# Generated at 2022-06-13 07:56:04.942747
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    test_object = FieldAttributeBase()
    assert test_object.get_validated_value(None, None, None, None) is None

# Generated at 2022-06-13 07:56:13.469783
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from ansible.errors import AnsibleUndefinedVariable
    from ansible.template import Templar
    from ansible.vars import VariableManager

    obj_FieldAttributeBase = FieldAttributeBase()
    obj_FieldAttributeBase.name = 'name'
    obj_FieldAttributeBase.isa = 'isa'
    obj_FieldAttributeBase.default = 'default'
    obj_FieldAttributeBase.private = False
    obj_FieldAttributeBase.required = False
    obj_FieldAttributeBase.static = False
    obj_FieldAttributeBase.final = False
    obj_FieldAttributeBase.always_post_validate = False
    obj_FieldAttributeBase.serialize = False
    obj_FieldAttributeBase.attribute = False
    obj_FieldAttributeBase.alias = False
    obj_FieldAttributeBase.immutable = False
    obj_FieldAttributeBase.global_

# Generated at 2022-06-13 07:56:23.042188
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    # Create the data structure to pass as the first argument
    # to the method being tested,
    # and convert it to a ModuleData object
    ds = {}
    ds = ModuleData(ds)

    # Create the data structure to pass as the second argument
    # to the method being tested,
    # and convert it to a class object
    #
    # Note that it is not necessary to call 'Base.__init__()',
    # since that method is already called by 'Base.__new__()'
    obj = Base()

    # Call the method being tested
    obj.validate(ds, 'name')

    # Check the results
    assert True is True # implemented later


# Generated at 2022-06-13 07:56:31.444438
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    print('test_FieldAttributeBase_get_validated_value')
    # TODO for now, just test that the protoype of the method
    # takes the expected parameters
    #
    # Note: we do not test this in the unit test, because a lot
    # of the code path requires a valid object, and has other
    # logic based on the object that may adversely affect the
    # tests.
    #
    # The code path is tested in test_task_vars.py
    #
    fb = FieldAttributeBase()
    fb.get_validated_value("name", "attribute", "value", "templar")


# Generated at 2022-06-13 07:56:39.076076
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    '''
    Unit tests for FieldAttributeBase class load_data method
    '''
    obj = FieldAttributeBase()
    assert not obj._finalized
    assert not obj._squashed
    # Test the following:
    obj._load_data(name=None, finalize=None, validate=None, include_role=None, ds=None, loader=None, variable_manager=None)
    assert not obj._finalized
    assert not obj._squashed
    # Test the following:
    obj._load_data(name=None, finalize=False, validate=None, include_role=None, ds=None, loader=None, variable_manager=None)
    assert not obj._finalized
    assert not obj._squashed
    # Test the following:

# Generated at 2022-06-13 07:56:50.646190
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    import unittest
    import sys
    import types
    class TestClass(object):
        __metaclass__ = BaseMeta
        _field1 = FieldAttribute(isa='str', default='value1')
        _field2 = FieldAttribute(isa='str', default='value2')
        _field3 = FieldAttribute(isa='str', default='value3', inherit=False)
        _field4 = FieldAttribute(isa='str', default='value4', alias='f4')
        _field5 = FieldAttribute(isa='str', default='value5', inherit=False, alias='f5')
        def _get_attr_field1(self):
            return '_get_attr_field1'
        def _get_attr_field2(self):
            return '_get_attr_field2'

# Generated at 2022-06-13 07:57:29.583523
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    o = FieldAttributeBase()
    assert o.dump_me() == {'aliases': [],
 'class_type': None,
 'default': None,
 'defined_when': None,
 'elements': None,
 'exclude_parent': None,
 'extend_parent': None,
 'fallback': (None, None),
 'ignore_parent': None,
 'include_parent': None,
 'isa': 'dict',
 'listof': None,
 'prepend_parent': None,
 'required': False,
 'static': False,
 'type': 'dict',
 'version': None}

# Generated at 2022-06-13 07:57:41.413613
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    name = 'name'
    value = 'default'
    default = 'default'
    validator = None
    choices = None
    always_post_validate = False
    class_name = 'class_name'
    class_name_override = 'class_name_override'
    isa = 'isa'
    static = False
    priority = 1
    required = False
    aliases = None
    inherit = False
    bypass_transformation = False

    class_inst = FieldAttributeBase(name, value, default, validator, choices, always_post_validate, class_name, class_name_override, isa, static, priority, required, aliases, inherit, bypass_transformation)
    ds = dict()

    ans = class_inst.load_data(ds)
    assert ans is None

# Generated at 2022-06-13 07:57:43.450551
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():

    # verify that the method behaves as documented
    FieldAttributeBase()



# Generated at 2022-06-13 07:57:52.162029
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    data = dict(
        ds = dict(
            line = 20,
            path = 'test_play.yml',
        ),
        loader = mock.MagicMock(),
    )
    base = FieldAttributeBase(**data)

    # Raise AnsibleParserError if loader is not provided
    data.pop('loader')
    with pytest.raises(AnsibleParserError):
        FieldAttributeBase(**data)

    # Raise AnsibleParserError if ds is not provided
    data['loader'] = mock.MagicMock()
    data.pop('ds')
    with pytest.raises(AnsibleParserError):
        FieldAttributeBase(**data)

    # Raise AnsibleParserError if data is not provided

# Generated at 2022-06-13 07:57:56.787490
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    FieldAttributeBase = SharedBase.FieldAttributeBase

    f = FieldAttributeBase()
    # args=['self', 'name', 'value', 'templar']
    name = 'name'
    value = 'lkj'
    templar = 'templar'
    assert f.get_validated_value(name, value, templar) == value



# Generated at 2022-06-13 07:58:08.234374
# Unit test for method get_path of class Base
def test_Base_get_path():
    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.handler import Handler
    from ansible.playbook.role.include import RoleInclude
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.template import Templar

    def get_hosts(host_names, ds):
        hosts = {}
        for host_name in host_names:
            hosts[host_name] = Host(host_name, port=22)

        return hosts

# Generated at 2022-06-13 07:58:11.576934
# Unit test for method get_path of class Base
def test_Base_get_path():
    base = Base()
    base._ds = DataSource({}, "test")
    base._ds._line_number = 0
    assert base.get_path() == "test:0"


# Generated at 2022-06-13 07:58:19.652567
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    def test_load_data(self, ds):
        if ds is None:
            return
        for (attr, value) in iteritems(ds):
            if attr in self._valid_attrs:
                attribute = self._valid_attrs[attr]
                attribute.load_data(attr, value, self)
        if C.DEFAULT_DEBUG:
            for (attr, value) in iteritems(ds):
                if attr not in self._valid_attrs:
                    display.warning('Ignoring invalid attribute: %s' % attr)
    # Due to ValidationError is being used as a base exception class, and not
    # all of its sub-classes are used as a base in Ansible, following is the
    # hack to import ValidationError class in order to have it correctly
    # mocked in the test.


# Generated at 2022-06-13 07:58:24.531033
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    def TestClass(FieldAttributeBase):
        name = FieldAttribute(isa='string', default=None, priority=FieldAttribute.LOW_PRIORITY)
    test_case = TestClass()
    test_case.deserialize({"name": "test_FieldAttributeBase_deserialize"})
    # Test something we can assume
    assert test_case.serialize()["name"] == "test_FieldAttributeBase_deserialize"



# Generated at 2022-06-13 07:58:29.410482
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    for valid_name in ('test_name', 'test_name2'):
        for dest_name in ('dest_name', 'dest_name2'):
            for src_name in ('src_name', 'src_name2'):
                x = FieldAttributeBase(valid_name)
                x.copy(dest_name, src_name)
                assert x.name == valid_name
                assert x.dest == dest_name
                assert x.src == src_name
    # TODO: Also test that it raises exception on invalid inputs


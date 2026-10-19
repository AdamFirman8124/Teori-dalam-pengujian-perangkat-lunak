

# Generated at 2022-06-13 07:50:02.335548
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():

    # constructor test
    # instance attribute test
    # object attribute test
    ut_obj = FieldAttributeBase()
    assert ut_obj._field_name == "field_name"
    assert ut_obj._default == ""
    assert ut_obj._required is True
    assert ut_obj._always_post_validate is False
    assert ut_obj._static is False
    assert ut_obj._attr_name == "attr_name"
    assert ut_obj._alt_names == []
    assert ut_obj.convert_to == []



# Generated at 2022-06-13 07:50:13.785366
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
  from ansible.parsing.vault import VaultLib
  from copy import copy
  from ansible.parsing.vault import VaultLib
  from copy import copy
  from ansible.template import Templar
  from ansible.vars import VariableManager
  from ansible.inventory.host import Host
  from ansible.inventory.group import Group
  from ansible.playbook.attribute import Attribute, FieldAttribute
  from ansible.playbook.become import Become
  from ansible.playbook.become_loader import BecomeLoader
  from ansible.playbook.block import Block
  from ansible.playbook.task import Task
  from ansible.playbook.conditional import Conditional
  from ansible.playbook.handler import Handler
  from ansible.playbook.helpers import load_list_of_blocks
 

# Generated at 2022-06-13 07:50:22.587020
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    class TestClass(object):
        def __init__(self):
            self._loader = None
            self._variable_manager = None
            self._validated = None
            self._finalized = None
            self._uuid = None

        def get_ds(self):
            return None

        def post_validate(self, templar):
            pass

    field_attribute_base = FieldAttributeBase()
    field_attribute_base.__class__.__name__ = 'FieldAttributeBase'
    field_attribute_base.static = None
    field_attribute_base.isa = None
    field_attribute_base.listof = None
    field_attribute_base.default = None
    field_attribute_base.required = None
    field_attribute_base.always_post_validate = None

# Generated at 2022-06-13 07:50:28.041270
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    obj = FieldAttributeBase()
    obj.load_data({'foo': 1})
    assert obj.foo == 1

    obj = FieldAttributeBase()
    obj.load_data(None)
    assert obj.foo is None

    obj = FieldAttributeBase()
    obj.load_data({})
    assert obj.foo is None



# Generated at 2022-06-13 07:50:39.307388
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    # Create an instance of FieldAttributeBase
    fieldattributebase = FieldAttributeBase()
    # Create an instance of AnsibleTemplate
    ansibletemplate = AnsibleTemplate()
    # Create an instance of AnsibleParserError
    ansibleparsererror = AnsibleParserError()
    # Create a value for the fake 'name' variable of type unicode
    name = u'name'
    # Create a value for the fake 'attribute' variable of type unicode
    attribute = u'attribute'
    # Create a value for the fake 'value' variable of type int
    value = 6
    # Create a value for the fake 'templar' variable
    templar = fieldattributebase.get_validated_value(name, attribute, value, ansibletemplate)
    # Example for assertIsInstance
    assertIsInstance(templar, unicode)
   

# Generated at 2022-06-13 07:50:40.942706
# Unit test for method get_path of class Base
def test_Base_get_path():
    base = Base()
    assert base.get_path() == ''
    base._ds = Base()


# Generated at 2022-06-13 07:50:46.239149
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    attr = FieldAttributeBase(name='test', required=True)
    obj = FieldAttributeBaseTest()
    ds = DataLoader()
    # TODO: improve this test coverage
    obj.post_validate(templar=ds)


# Generated at 2022-06-13 07:50:48.534632
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    obj = FieldAttributeBase()
    assert not hasattr(obj, 'get_validated_value')

# Generated at 2022-06-13 07:50:51.012693
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    item = FieldAttributeBase()
    attrs = {}
    item.from_attrs(attrs)

# Generated at 2022-06-13 07:50:53.004324
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    objBase = Base()
    my_search_path = objBase.get_search_path()
    assert my_search_path == [], "Expected [], got %r" %(my_search_path)


# Generated at 2022-06-13 07:51:30.108430
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    _valid_attrs = {
        'name': FieldAttribute(isa='string', default='foo'),
        'list_var': FieldAttribute(isa='list', default=[1, 2]),
        'dict_var': FieldAttribute(isa='dict', default={'key1': 'value1', 'key2': 'value2'}),
        'tuple_var': FieldAttribute(isa='tuple', default=('item1', 'item2'))
    }
    class test_FieldAttributeBase_class(FieldAttributeBase):
        _valid_attrs = _valid_attrs

    obj = test_FieldAttributeBase_class('', dict())
    obj.name = 'bar'


# Generated at 2022-06-13 07:51:32.152594
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    assert FieldAttributeBase().get_validated_value() == NotImplemented

# Generated at 2022-06-13 07:51:42.562065
# Unit test for method get_validated_value of class FieldAttributeBase

# Generated at 2022-06-13 07:51:46.821648
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():

    # Instantiate an object of class FieldAttributeBase
    obj = FieldAttributeBase()

    # Test attributes
    name = 'some_name'
    attribute = None
    value = 'some_value'
    templar = None

    # Exercise function
    retval = FieldAttributeBase.get_validated_value(obj, name, attribute, value, templar)
    assert retval == 'some_value'
    return True


# Generated at 2022-06-13 07:51:55.271944
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    pd1 = Playbook()
    p1 = Play()
    t1 = Task()
    t1._ds = FakeDataLoader()
    t1._parent = p1
    t1._parent._play = p1
    t1._parent._play._ds = FakeDataLoader()
    t1._parent._play._ds._data_source = 'aaa'
    t1._parent._play._ds._line_number = 100
    t1._role_paths = ['ccc']
    t1._parent._task_paths = ['eee']
    t1._role_path = 'bbb'
    ans = t1.get_search_path()
    assert ans == ['ccc', 'bbb', 'aaa']

# Generated at 2022-06-13 07:51:56.403300
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():

    # Done. Return a value
    return


# Generated at 2022-06-13 07:52:09.192923
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from ansible.parsing.yaml.objects import AnsibleUnicode

    # Set up test environment
    yaml_data="""
        value: this is a test
        int: 12
        float: 12.8
        bool: 'yes'
        percent: '90%'
        list:
          - '1'
          - '2'
          - '3'
        set:
          - '1'
          - '2'
          - '3'
    """
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    test_obj = AnsibleBaseYAMLObject()
    test_obj.base_ghost = False
    test_obj.ansible_pos = (1,8)
    test_obj.value = 'this is a test'

# Generated at 2022-06-13 07:52:18.606815
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    # Or just do this, if you don't like having a full class above,
    # but it has to have a type that doesn't already exist in the system.
    class FooObject(FieldAttributeBase):
        pass

    # Basic usage
    fb = FooObject(name='FooBar', required=True, isa='dict', default={'a': 1},
                   choices={'a', 'b', 'c'}, aliases=['barfoo'], category='Foo')
    assert fb.name == 'FooBar'
    assert fb.required == True
    assert fb.isa == 'dict'
    assert fb.default == {'a': 1}
    assert fb.choices == {'a', 'b', 'c'}
    assert fb.aliases == ['barfoo']

# Generated at 2022-06-13 07:52:26.909196
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    from ansible.module_utils._text import to_bytes, to_text, to_native
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.template import Templar
    import ansible.template.safe_eval

    class MyAttribute(FieldAttributeBase):
        def __init__(self):
            self.isa = 'string'
            self.name = 'Foo'

    class MyObject(AnsibleBaseYAMLObject):
        def __init__(self):
            self._attributes = dict()
            self._valid_attrs = dict()
            self._valid_attrs['foo'] = MyAttribute()
            self._valid_attrs['bar'] = MyAttribute()
            self._valid_attrs['baz'] = MyAttribute()
            self._valid_att

# Generated at 2022-06-13 07:52:32.722653
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    class FieldAttributeBase(object):
        def __init__(self):
            self.name = None
            self.isas = None
            self.default = None
            self.aliases = ['foo', 'bar']


    test = FieldAttributeBase()

    test_copy = test.copy()

    assert test.name == test_copy.name
    assert test.isas == test_copy.isas
    assert test.default == test_copy.default
    assert test.aliases == test_copy.aliases



# Generated at 2022-06-13 07:53:03.006136
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    Obj = object()
    attr = FieldAttributeBase('name', 'default', False, False)
    value = attr.from_attrs(Obj, {'foo': 'bar'})
    assert value == None


# Generated at 2022-06-13 07:53:14.516367
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():

    field = FieldAttributeBase()
    prefix = 'field'
    setattr(field, 'some_attribute', 'old value')
    field.some_attribute = 'old value'
    copy_field = field.copy(prefix)
    assert copy_field is not field
    assert copy_field.some_attribute == 'old value'
    assert field.copy(prefix, some_attribute='new value') is not field
    assert field.copy(prefix, some_attribute='new value').some_attribute == 'new value'
    assert field.copy(prefix, some_attribute='new value').some_attribute != field.some_attribute
    field.some_attribute = 'old value'
    assert field.copy(some_attribute='new value').some_attribute == 'new value'
    # Skip test_attribute_name contains '/'
    # Skip test_attribute

# Generated at 2022-06-13 07:53:29.027930
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():

    def test_FieldAttributeBase_load_data_001():
        '''
        This test case will load data with:
            - name = 'foo'
            - static = False
            - default = 'bar'
            - always_post_validate = False
        '''

        class MyClass(FieldAttributeBase):
            pass

        my_object = MyClass()
        data = {
            'name': 'foo',
            'static': False,
            'default': 'bar',
            'always_post_validate': False,
        }
        my_object.load_data(data)

        assert my_object.name == 'foo'
        assert my_object.static is False
        assert my_object.default == 'bar'
        assert my_object.always_post_validate is False


# Generated at 2022-06-13 07:53:39.713313
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():

    from ansible.module_utils.six import string_types

    from ansible.errors import AnsibleParserError

    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    class AnsibleFakeBaseObject(AnsibleBaseYAMLObject):
        pass

    # the defined test data is a list of tuples
    # each tuple contains these elements:
    # 0) the name of the attribute being set
    # 1) the FieldAttribute object being set
    # 2) the value being set
    # 3) the templar passed to post_validate
    # 4) the expected value returned
    # 5) the exception raised (if any)
    from ansible.utils.vars import combine_vars


# Generated at 2022-06-13 07:53:41.604994
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    fixture = FieldAttributeBase(isattr=False)
    # Call validate() with no required param
    fixture.validate()



# Generated at 2022-06-13 07:53:52.833985
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    from ansible.compat.six import PY3

    class ansible_mock():
        class _ds_mock():
            _line_number = 22
            _data_source = "abc"
        class _parent_mock():
            class _play_mock():
                class _ds_mock():
                    _line_number = 33
                    _data_source = "def"

        _ds = _ds_mock()
        _parent = _parent_mock()

    base_obj = Base()
    base_obj._ds = base_obj
    base_obj._parent = base_obj
    # test get_search_path method
    search_path = base_obj.get_search_path()

# Generated at 2022-06-13 07:53:54.181949
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    # Todo: Add more tests for method validate of class FieldAttributeBase
    assert True


# Generated at 2022-06-13 07:53:58.770120
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    '''
    Unit test for method validate of class FieldAttributeBase
    '''
    fake_class = FakeClass()
    fake_class.fake_instance = FakeClass()
    fake_class.fake_instance.fake_instance = FakeClass()
    attr_base = FieldAttributeBase()
    attr_base.name = 'fake_attr'
    fake_class.fake_instance.fake_instance.fake_attr = 'fake_value'
    assert attr_base.validate(fake_class.fake_instance.fake_instance) == 'fake_value'


# Generated at 2022-06-13 07:53:59.723892
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    assert FieldAttributeBase().load_data(data={}) == {}

# Generated at 2022-06-13 07:54:02.586185
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    base = AnsibleUnicode('FOO', required=False, default='bar')
    data = dict()
    try:
        base.deserialize(data)
    except Exception as e:
        raise AssertionError("deserialize of class FieldAttributeBase not working as expected")

# Generated at 2022-06-13 07:54:34.981013
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.display import Display
    from ansible.utils.vars import load_extra_vars
    display = Display()
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    playbook_path = '/tmp/play'
    variable_manager.extra_vars = load_extra_vars(loader=loader, play=play)
    variable_manager.extra_vars.update(load_extra_vars(loader=loader, play=play))
    variable_manager.extra_vars

# Generated at 2022-06-13 07:54:42.300423
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    '''
    Unit test for method validate of class FieldAttributeBase
    '''
    def test_validate_isa_list(self):
        '''
        Make sure the isa list is correct
        '''
        if isa not in ['string', 'int', 'float', 'bool', 'list', 'set', 'dict', 'class', 'complex', 'none', 'percent']:
            raise AssertionError("isa not one of the valid choices")

    def test_validate_isa_class(self):
        '''
        Make sure isa class is a subclass of Base
        '''
        if isa == 'class' and not issubclass(class_type, Base):
            raise AssertionError("isa set to class but class_type is not a subclass of Base")


# Generated at 2022-06-13 07:54:52.739689
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    '''
    Test method dump_attrs of class FieldAttributeBase
    '''

    f = FieldAttributeBase()

    from ansible.utils.unsafe_proxy import wrap_var

    f.set_serialize_flag(True)
    x = f.dump_attrs()
    assert x == {'serialize_when_field': True}

    f.set_serialize_flag(False)
    x = f.dump_attrs()
    assert x == {'serialize_when_field': False}

    f.set_serialize_when_field('insert')
    x = f.dump_attrs()
    assert x == {'serialize_when_field': 'insert'}

    f.set_serialize_when_field('insert')
    x = f.dump_attrs()

# Generated at 2022-06-13 07:54:55.187762
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    fld = FieldAttributeBase()
    d = fld.dump_me()
    assert(d is not None)

# Generated at 2022-06-13 07:54:57.094383
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    assert FieldAttributeBase().dump_attrs() == {}, "FieldAttributeBase.dump_attrs() == {}"

# Generated at 2022-06-13 07:54:59.235615
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    assert get_search_path(Base()) == []

# end of test_Base_get_search_path



# Generated at 2022-06-13 07:55:09.139040
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    def test_parents(test_parents, test_dct):
        for test_parent in test_parents:
            if hasattr(test_parent, '__dict__'):
                _create_attrs(test_parent.__dict__, test_dct)
                new_dst_dict = test_parent.__dict__.copy()
                new_dst_dict.update(test_dct)
                test_parents(test_parent.__bases__, new_dst_dict)
    
    
    test_name = ''
    test_parents = ()
    test_dct = {}
    _create_attrs = ''
    # create some additional class attributes
    test_dct['_attributes'] = {}
    test_dct['_attr_defaults'] = {}

# Generated at 2022-06-13 07:55:17.889073
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    import json
    import pytest
    from ansible.parsing.yaml.loader import AnsibleLoader

    with open('/home/admiralhelmut/ansible/test/units/unit_test_data/FieldAttributeBase/FieldAttributeBase_import.yml','r') as f:
        yaml_data = f.read()
    data = AnsibleLoader(yaml_data).get_single_data()
    instance_1 = FieldAttributeBase(loader=None, variable_manager=None, **data)
    with open('/home/admiralhelmut/ansible/test/units/unit_test_data/FieldAttributeBase/FieldAttributeBase_export.json','r') as f:
        json_data = f.read()
    data = json.loads(json_data)
    instance_1.from_att

# Generated at 2022-06-13 07:55:18.962695
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    assert False, "Test not implemented"



# Generated at 2022-06-13 07:55:21.301472
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    assert FieldAttributeBase().validate(sentinel.attr, sentinel.attr_class) is None

# Generated at 2022-06-13 07:55:58.769855
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    field_attribute_base = FieldAttributeBase(name='name_value')
    ansible_field_attribute_base = AnsibleFieldAttributeBase(name='name_value')

    field_attribute_base.default = 'default_value'
    ansible_field_attribute_base.default = 'default_value'

    field_attribute_base.required = True
    ansible_field_attribute_base.required = True

    field_attribute_base.static = True
    ansible_field_attribute_base.static = True

    field_attribute_base.unique = False
    ansible_field_attribute_base.unique = False

    field_attribute_base.always_post_validate = False
    ansible_field_attribute_base.always_post_validate = False


# Generated at 2022-06-13 07:56:09.615001
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    # validate(value)
    # test_FieldAttributeBase_validate.py
    #
    # Author:   Benjamin Bengfort <bbengfort@districtdatalabs.com>
    # Created:  Thu Aug 11 12:07:01 2016 -0400
    #
    # Copyright (C) 2016 District Data Labs
    # For license information, see LICENSE.txt
    #
    # ID: test_FieldAttributeBase.py [c33acff] benjamin@bengfort.com $
    #
    """
    Tests the validate method of FieldAttributeBase
    """

    ##########################################
    ## Test the validate method of the base class
    ##########################################

    basefield = FieldAttributeBase()
    basefield.validate('test')

    # Cannot validate None

# Generated at 2022-06-13 07:56:19.655831
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    fake_loader = DictDataLoader({})
    fake_inventory = InventoryManager(loader=fake_loader, sources='')
    variable_manager = VariableManager(loader=fake_loader, inventory=fake_inventory)
    templar = Templar(loader=fake_loader, variables=variable_manager)
    class Test(FieldAttributeBase): pass
    attrs = {u'test1': u'test'}
    obj = Test(variable_manager=variable_manager)
    obj.from_attrs(attrs)
    result = obj.dump_attrs()
    assert result[u'test1'] == u'test'

# Generated at 2022-06-13 07:56:22.745434
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    fieldattrib = FieldAttributeBase(default=None)
    assert fieldattrib == fieldattrib.copy()
    assert fieldattrib == fieldattrib.copy_to(None)


# Generated at 2022-06-13 07:56:24.905378
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    obj = FieldAttributeBase()
    obj.post_validate(templar=templar())
    assert not obj


# Generated at 2022-06-13 07:56:35.237883
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    attr = FieldAttribute()
    attr.name = 'test_name'
    attr.default = 'test_default'
    attr.isa = 'test_isa'
    attr.choices = 'test_choices'
    attr.required = 'test_required'
    attr.static = 'test_static'
    attr.always_post_validate = 'test_always_post_validate'
    attr.private = 'test_private'
    attr.class_type = 'test_class_type'
    attr.listof = 'test_listof'
    assert attr.name == 'test_name'
    assert attr.default == 'test_default'
    assert attr.isa == 'test_isa'
    assert attr.choices == 'test_choices'

# Generated at 2022-06-13 07:56:45.940383
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    # post_validate(self, templar)
    # NOTE: We fake the uuid here as we can't set it up ourselves.
    obj = FieldAttributeBase('/fake/path', dict(
        name = "FAKE",
        attribute = "FAKE_ATTRIBUTE",
        isa = "FAKE_ISA",
        default = "FAKE_DEFAULT",
        uuid = "FAKE_UUID"
    ))
    assert obj.name == "FAKE"
    assert obj.attribute == "FAKE_ATTRIBUTE"
    assert obj.isa == "FAKE_ISA"
    assert obj.default == "FAKE_DEFAULT"
    assert obj._uuid == "FAKE_UUID"
    assert obj.static == False



# Generated at 2022-06-13 07:56:47.706507
# Unit test for method get_ds of class FieldAttributeBase
def test_FieldAttributeBase_get_ds():
    # The result of get_ds is the same instance passed in at construction
    field = FieldAttributeBase(ds='foo')
    assert field.get_ds() == 'foo'

# Generated at 2022-06-13 07:56:54.305457
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from collections import MutableMapping
    # Test the method of class FieldAttributeBase with default attributes
    FieldAttributeBase_e = FieldAttributeBase()
    # Test the method FieldAttributeBase.post_validate with temporary attributes
    FieldAttributeBase_e_post_validate_temporary_attributes = {}
    FieldAttributeBase_e_post_validate_temporary_attributes['templar'] = None
    FieldAttributeBase_e.post_validate(FieldAttributeBase_e_post_validate_temporary_attributes['templar'])

# Generated at 2022-06-13 07:57:05.039264
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    '''
    Unit test for method get_validated_value of class FieldAttributeBase
    '''
    
    # test case 1:
    
    # This method is tested by the various classes that define it.
    #
    #    class MyClass(object):
    #        _valid_attrs = dict(attr=FieldAttribute())
    #
    #        def __init__(self, attr):
    #            self.attr = attr
    #
    #        def post_validate(self, templar):
    #            self.attr = self.get_validated_value('attr', self._valid_attrs['attr'], self.attr, templar)
    #
    #    class TestMyClass(unittest.TestCase):
    #
    #        VALIDATION = {
    #            '

# Generated at 2022-06-13 07:57:54.205127
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    my_mock = FieldAttributeBase()
    my_mock._finalized = True
    my_mock._squashed = True
    my_mock.dump_attrs()
    my_mock.from_attrs(attrs='attrs')



# Generated at 2022-06-13 07:58:05.638035
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    fd = FieldAttributeBase()
    fd.load_data({"type": "str", "required": True, "aliases": [], "default": None, "static": False, "post_validate": None})
    fd.load_data({"aliases": ["argv"], "default": [], "required": False, "static": False, "type": "list", "post_validate": None})
    fd.load_data({"aliases": ["always_run"], "default": "default", "required": False, "static": False, "type": "str", "post_validate": None})
    fd.load_data({"aliases": [], "default": "default", "required": False, "static": False, "type": "str", "post_validate": None})
    fd.load_data

# Generated at 2022-06-13 07:58:13.743378
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    field_attribute_baseInstance = FieldAttributeBase(
        name = 'foo',
        class_type = 'class_type',
        inherits = True,
        required = True,
        default = 'default',
        allow_duplicates = True,
        array = True,
        aliases = 'aliases',
        always_post_validate = True,
        isa = 'isa',
        listof = 'listof',
        static = True,
        vault_files = 'vault_files' 
    )
    assert field_attribute_baseInstance.squash() == None

# Generated at 2022-06-13 07:58:14.671863
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    pass


# Generated at 2022-06-13 07:58:16.545200
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    obj = FieldAttributeBase('Test')
    obj.deserialize('Test')

    assert str(obj) == 'Test'



# Generated at 2022-06-13 07:58:24.693641
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    name = 'foo'
    default = 'bar'
    isa = 'string'
    required = False
    attribute = FieldAttributeBase(name, default, isa, required)
    hostvars = dict(foo=dict(bar=1))
    templar = Templar(loader=None, variables=dict(hostvars=hostvars))
    value = '{{ hostvars["foo"]["bar"] }}'
    got = attribute.post_validate(value, templar)
    assert got == 1

testdata = list()
testdata.append(('test_FieldAttributeBase_post_validate', 'test_FieldAttributeBase_post_validate'))


# Generated at 2022-06-13 07:58:28.061006
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    from ansible.playbook.base import Base
    data = dict(test=dict(testkey='testval',testkey2='testval2'))
    obj = Base.from_attrs(data)
    assert obj.test.testkey == 'testval'
    assert obj.test.testkey2 == 'testval2'


# Generated at 2022-06-13 07:58:30.288705
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    test=Task()
    test.vars={"var":"val"}
    res=test.dump_attrs()
    assert isinstance(res,dict)
    assert res["vars"]=={"var":"val"}


# Generated at 2022-06-13 07:58:42.268796
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():

    # Create a mock class for BaseMeta
    # This class has the following attributes:
    #     _attributes = {}
    #     _attr_defaults = {}
    #     _valid_attrs = {}
    #     _alias_attrs = {}

    #     def __init__():

    #     def __new__():
    #         return MockBaseMeta

    #     def __getattribute__(self):
    #         return super.__getattribute__()

    from unittest.mock import create_autospec

# Generated at 2022-06-13 07:58:47.422407
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    # -------------------------------------------------
    # Variable mocks

    # -------------------------------------------------
    # Test body

    attr = FieldAttribute()
    assert attr.load_data(None, None, None, None) is None


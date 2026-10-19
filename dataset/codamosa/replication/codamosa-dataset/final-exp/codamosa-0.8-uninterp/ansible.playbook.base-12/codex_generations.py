

# Generated at 2022-06-13 07:49:48.314949
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    with pytest.raises(AnsibleAssertionError) as e:
        get_test_instance(FieldAttribute, 'test_FieldAttributeBase_deserialize')
    assert e.value.args[0] == "data (4) should be a dict but is a <type 'int'>"
    with pytest.raises(AnsibleAssertionError) as e:
        get_test_instance(FieldAttribute, 'test_FieldAttributeBase_deserialize')
    assert e.value.args[0] == "data ([]) should be a dict but is a <type 'list'>"
    with pytest.raises(AnsibleAssertionError) as e:
        get_test_instance(FieldAttribute, 'test_FieldAttributeBase_deserialize')

# Generated at 2022-06-13 07:49:57.843782
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    import mock
    class Mockcls(object):
        @staticmethod
        def __new__(cls):
            return cls
    class MockBase(Base):
        def __init__(self):
            pass
        def _load_name(self, value):
            pass
        def _get_attr_name(self):
            pass
    with mock.patch('ansible.playbook.base.BaseMeta', Mockcls):
        with mock.patch('ansible.playbook.base.Base', MockBase):
            b = Base(name='test_name')
            assert '_valid_attrs' in b.__class__.__dict__
            assert b._valid_attrs == {u'name': 'name'}
            assert '_attributes' in b.__class__.__dict__

# Generated at 2022-06-13 07:50:08.813622
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    host = object()
    def _post_validate_foo(self, attr, value, templar):
        return 123

    def _post_validate_bar(self, attr, value, templar):
        return 'abc'

    class MyClass(object):
        is_templateable = False
        def __init__(self):
            self.name = 'my_name'
            self.foo = None
            self.bar = None
            self.var = None

        def get_ds(self):
            return host

        def post_validate(self, templar):
            pass

    m = MyClass()
    attribute = FieldAttributeBase()

# Generated at 2022-06-13 07:50:19.818716
# Unit test for method get_path of class Base
def test_Base_get_path():
    import yaml
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 07:50:21.477226
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    t = FieldAttributeBase()
    assert False # TODO implement your test here


# Generated at 2022-06-13 07:50:22.787248
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    test_object = FieldAttributeBase()
    assert isinstance(test_object.dump_attrs(), dict)

# Generated at 2022-06-13 07:50:25.762277
# Unit test for method get_ds of class FieldAttributeBase
def test_FieldAttributeBase_get_ds():
    obj = FieldAttributeBase()
    try:
        obj.get_ds()
    except NotImplementedError:
        pass

# Generated at 2022-06-13 07:50:28.814536
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    '''
    Unit test for method squash of class FieldAttributeBase
    '''
    # ansible/lib/ansible/playbook/play.py:838
    pass

# Generated at 2022-06-13 07:50:31.882134
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    # Test with a good object (FieldAttributeBase)
    obj = FieldAttributeBase(attribute=FieldAttribute(isa='string'))
    obj._attributes['attribute'] = FieldAttribute(isa='string')
    dumped_obj = obj.dump_me()
    assert 'answer' in dumped_obj
    assert isinstance(dumped_obj['answer'], dict)
    assert obj.attributes_count == 0
    assert dumped_obj['answer']['isa'] == 'string'


# Generated at 2022-06-13 07:50:41.651817
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    x = FieldAttributeBase()
    ds = AnsibleMock()
    ds.vars = "hello world"
    ds.deepcopy.return_value="hello world"
    attr = FieldAttributeBase()
    attr2 = FieldAttributeBase()
    attr.load_data(ds, x)
    attr2._load_data(ds, x)
    assert attr.avail_vars is None
    assert attr.base_class is None
    assert attr.class_type is None
    assert attr.default is None
    assert attr.isa is None
    assert attr.listof is None
    assert attr.private is False
    assert attr.required is False
    assert attr.static is False
    
    

# Generated at 2022-06-13 07:51:14.901641
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    # Test the case where attr is None

    # create an instance of the class
    obj = FieldAttributeBase()

    # make a copy of it
    attr = obj.copy()

    # make sure the copy is equal to the original
    assert attr == obj

    # Test the case where attr is a FieldAttributeBase

    # create an instance of the class
    obj = FieldAttributeBase()

    # create a second instance of the class to use for comparison
    obj2 = FieldAttributeBase()

    # make a copy of it
    attr = obj.copy()

    # make sure the copy is equal to the original
    assert attr == obj2

    # Test the case where attr is a FieldAttributeBase

    # create an instance of the class
    obj = FieldAttributeBase()

    # create a second instance of the class to use for comparison

# Generated at 2022-06-13 07:51:25.502802
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    FieldAttributeBase = ansible_collections.ansible.community.tests.unit.plugins.lang.test.utils.FieldAttributeBase.FieldAttributeBase
    Fa = ansible_collections.ansible.community.tests.unit.plugins.lang.test.utils.FieldAttributeBase.Fa
    import re
    import tempfile
    import shutil
    import os
    import ansible.module_utils.six as six
    from ansible.module_utils._text import to_text, to_bytes
    from ansible.module_utils.common._collections_compat import Mapping
    import json
    import sys
    import copy
    import datetime


# Generated at 2022-06-13 07:51:28.827707
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    obj = FieldAttributeBase()
    name = ""
    attribute = ""
    value = ""
    templar = ""
    assert obj.get_validated_value(name, attribute, value, templar) is None


# Generated at 2022-06-13 07:51:40.536078
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    attribute = FieldAttribute()
    fa = FieldAttributeBase()
    res = fa.get_validated_value('name', attribute, 'value', templar.Templar(loader=Mock()))
    assert res is 'value'
    assert isinstance(res, string_types)
    attribute = FieldAttribute(isa='int')
    res = fa.get_validated_value('name', attribute, '5', templar.Templar(loader=Mock()))
    assert res == 5
    assert isinstance(res, int)
    attribute = FieldAttribute(isa='float')
    res = fa.get_validated_value('name', attribute, '5', templar.Templar(loader=Mock()))
    assert res == 5.0
    assert isinstance(res, float)

# Generated at 2022-06-13 07:51:48.845102
# Unit test for method get_path of class Base
def test_Base_get_path():
    base = Base()
    base._ds = FileLine('/data/file')
    base._ds._line_number = 1
    assert base.get_path() == '/data/file:1'
    del base._ds
    base._parent = Base()
    base._parent._play = Base()
    base._parent._play._ds = FileLine('/data/file')
    base._parent._play._ds._line_number = 2
    assert base.get_path() == '/data/file:2'

# Generated at 2022-06-13 07:51:55.552587
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from ansible.errors import AnsibleParserError

    templar = MagicMock()
    templar.template.return_value, templar.is_template.return_value = [1,2],True
    templar.available_variables = {}
    obj = FieldAttributeBase()
    
    # Do test for isa=='string' 
    setattr(obj, '_attributes', {'name':FieldAttribute(isa='string', required=True)})
    setattr(obj, '_attr_defaults', {'name':FieldAttribute(isa='string', required=True)})
    setattr(obj, '_valid_attrs', {'name':FieldAttribute(isa='string', required=True)})
    obj.post_validate(templar)
    assert(obj.name=="12")


# Generated at 2022-06-13 07:52:08.037842
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from ansible import errors
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.template import Templar

    # Initialize a few objects we can use to stub out other things
    fake_loader = FakeLoader()
    templar = Templar(loader=fake_loader)
    fake_variable_manager = FakeVariableManager()

    # Initialize a FieldAttributeBase using our stub objects
    field_attribute_base = FieldAttributeBase(
        loader=fake_loader,
        variable_manager=fake_variable_manager,
    )

    # Add a field that we can test with
    field_attribute_base._valid_attrs = dict(valid_attr=FakeFieldAttribute())
    field_attribute_base.valid_attr = None

    # Test when attribute is required but not set

# Generated at 2022-06-13 07:52:18.141483
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    # create a class to be able to mock _get_fields
    class TestHost(object):
        def __init__(self):
            # we need to set the loader here to make the __init__ of Base work
            self._loader = DictDataLoader({})

        def _get_fields(self):
            return {'name': FieldAttribute(isa='string', required=True),
                    'groups': FieldAttribute(isa='list', default=[])}

    # setup the host variable used in the test
    host = TestHost()
    setattr(host, 'name', 'host1')

    # create the object with the method to be tested
    result = FieldAttributeBase.get_validated_value(host, 'groups', 'group1', None)

    # assert the result
    assert result == ['group1']

    # create the object with the

# Generated at 2022-06-13 07:52:19.184647
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    pass



# Generated at 2022-06-13 07:52:20.040250
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    # FIXME: test method squash of class FieldAttributeBase
    pass


# Generated at 2022-06-13 07:52:47.745252
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    mock__valid_attrs = dict()
    mock__alias_attrs = dict()
    mock__attributes = dict()
    mock__attr_defaults = dict()
    mock__loader = MagicMock()
    mock__variable_manager = MagicMock()
    mock__validated = False
    mock__finalized = False
    mock__uuid = MagicMock()
    mock_get_ds = MagicMock()
    mock_post_validate = MagicMock()


# Generated at 2022-06-13 07:52:52.736122
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    # Test the squash method
    attr = FieldAttributeBase()

    # Test squashing when the item is a list
    item = ['test1', 'test2']
    assert attr.squash(item) == item

    # Test squashing when the item is not a list
    item = 'test3'
    assert attr.squash(item) == item



# Generated at 2022-06-13 07:53:04.812393
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    from pprint import pprint
    from collections import Mapping
    from sys import getrefcount
    from ansible.errors import AnsibleAssertionError
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.become import Become
    from ansible.playbook.roles import Role
    from ansible.playbook.role import RoleDefinition
    from ansible.playbook.taggable import Taggable
    from ansible.playbook.task_include import TaskInclude
    from ansible.utils.boolean import boolean

    # Create

# Generated at 2022-06-13 07:53:15.644541
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    my_obj = FieldAttributeBase()

    # test string
    attr = FieldAttribute('name_1', isa='string', default='placeholder', required=True)
    res = my_obj.get_validated_value('name_1', attr, 'value', None)
    assert res == 'value'

    # test int
    attr = FieldAttribute('name_2', isa='int', default=99, required=True)
    res = my_obj.get_validated_value('name_2', attr, '123', None)
    assert res == 123

    # test float
    attr = FieldAttribute('name_3', isa='float', default=4.4, required=True)
    res = my_obj.get_validated_value('name_3', attr, '12.3', None)

# Generated at 2022-06-13 07:53:26.709949
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    FA1_class = class_with_fields('FA1', (), {'isa': FieldAttribute(isa='int')})
    FA2_class = class_with_fields('FA2', (), {'isa': FieldAttribute(isa='string')})
    FA3_class = class_with_fields('FA3', (), {'isa': FieldAttribute(isa='float')})
    FA4_class = class_with_fields('FA4', (), {'isa': FieldAttribute(isa='bool')})
    FA5_class = class_with_fields('FA5', (), {'isa': FieldAttribute(isa='percent')})
    FA6_class = class_with_fields('FA6', (), {'isa': FieldAttribute(isa='list', listof='int',required=True)})

# Generated at 2022-06-13 07:53:30.494897
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    # create an instance of FieldAttributeBase
    fb = FieldAttributeBase()
    # this method should be set by a subclass and fail with an NotImplementedError
    
    with pytest.raises(NotImplementedError):
        fb.dump_me()


# Generated at 2022-06-13 07:53:40.848494
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    '''
    Unit test for method dump_me of class FieldAttributeBase
    '''

    from ansible.playbook.attribute import FieldAttributeBase

    # instantiate an object of the class with defaults
    obj = FieldAttributeBase()

    # make an alias of the functionality we are testing
    the_functionality = obj.dump_me

    # ensure the functionality behaves as expected
    # this is a no-op due to the defaults
    assert the_functionality() == {}, \
        "method dump_me failed with default values"

    # set a non-default value for name
    obj.name = "test_name"
    # set a non-default value for isa
    obj.isa = "test_isa"
    # set a non-default value for attr_required
    obj.attr_required = False
    # set a non

# Generated at 2022-06-13 07:53:44.323925
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    '''
    Unit test for method validate of class FieldAttributeBase
    '''
    f = FieldAttributeBase()
    assert f.validate(None, None) is True


# Generated at 2022-06-13 07:53:54.155471
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    FAKE_STRING = "string"
    FAKE_INT = 123
    FAKE_BOOL = True
    FAKE_LIST = ["string", 123, True]
    FAKE_DICT = {"key": "value"}
    FAKE_SET = set(['item'])
    FAKE_CONSTANT = 'foo'

# Generated at 2022-06-13 07:54:05.113514
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
  from ansible.utils.unsafe_proxy import AnsibleUnsafeText
  from ansible.utils.unsafe_proxy import wrap_var
  a = FieldAttributeBase()

  # Test with value None
  v=None
  r = a.squash(v)
  assert r == None

  # Test with value "Some string to use as a basic test"
  v=u"Some string to use as a basic test"
  r = a.squash(v)
  assert isinstance(r, AnsibleUnsafeText)
  assert r == v

  # Test with value "Another string to use as a basic test"
  v=u"Another string to use as a basic test"
  r = a.squash(v)
  assert isinstance(r, AnsibleUnsafeText)
  assert r == v

  # Test with

# Generated at 2022-06-13 07:54:35.663500
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    loader = DictDataLoader({
        "vars.yml": """
                var1: hello
                var2: world
            """
    })
    variable_manager = VariableManager(loader=loader)
    task = Task()
    variable_manager.set_host_variable('test-host', 'var1', 'hello')
    variable_manager.set_host_variable('test-host', 'var2', 'world')
    task._variable_manager = variable_manager
    task.post_validate()
    assert task.dump_attrs() == {}
    task._valid_attrs = {'name': 'test-name'}
    assert task.dump_attrs() == {'name': 'test-name'}


# Generated at 2022-06-13 07:54:37.030429
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    pass



# Generated at 2022-06-13 07:54:37.869514
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    pass


# Generated at 2022-06-13 07:54:40.859269
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    host_obj = HostVars()
    host_obj.user = 'root'
    host_obj.password = 'admin'
    host_obj.port = '22'
    assert host_obj.dump_attrs() == dict(user='root', password='admin', port='22')


# Generated at 2022-06-13 07:54:44.240668
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    class MyObj(base.FieldAttributeBase):
        def post_validate(self, templar):
            return []

    obj = MyObj()
    obj.post_validate(None)



# Generated at 2022-06-13 07:54:46.611297
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    field = FieldAttributeBase()
    # no checks for null or None value
    assert field._dump_me() == {}


# Generated at 2022-06-13 07:54:47.610257
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    pass



# Generated at 2022-06-13 07:54:50.592376
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    # Check error on invalid type for argument data
    data = []
    with pytest.raises(AnsibleAssertionError) as e:
        FieldAttributeBase.deserialize(data)



# Generated at 2022-06-13 07:54:58.208404
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    hostvars = dict({u'memory': u'4G', u'OS': u'RHEL', u'network': u'192.168.1.1', u'cpu': u'i5'})
    runner_data = dict({u'hostvars': hostvars})

# Generated at 2022-06-13 07:55:02.842601
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    '''
    Unit test for method load_data of class FieldAttributeBase
    '''
    # TODO: Testing not implemented for method FieldAttributeBase.load_data.
    #       Testing this will require having a container for creating field attributes
    #       which can be used in the test.
    pass



# Generated at 2022-06-13 07:55:42.045109
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    assert Task().get_search_path() == [os.path.dirname(os.path.abspath('..'))]

    # test dep_chain
    ds = DataSource({'foo': 'bar'})
    dep_chain = [Host('host1', ds), Host('host2', ds)]
    task = Task(dep_chain=dep_chain)
    assert task.get_search_path() == [os.path.dirname(os.path.abspath('..'))]

    dep_chain = [Task(dep_chain=dep_chain)]
    task = Task(dep_chain=dep_chain)
    assert task.get_search_path() == [os.path.dirname(os.path.abspath('..'))]

    # test role_path
    role_path = os

# Generated at 2022-06-13 07:55:48.272568
# Unit test for method get_path of class Base
def test_Base_get_path():
    # Test with a parent
    b = Base()
    b._ds = Mock()
    b._ds._data_source = "data-source"
    b._ds._line_number = 123
    assert b.get_path() == "data-source:123"
    # Test with a parent and a grandparent
    b._parent = Mock()
    b._parent._play = Mock()
    b._parent._play._ds = Mock()
    b._parent._play._ds._data_source = "data-source2"
    b._parent._play._ds._line_number = 456
    assert b.get_path() == "data-source2:456"
    # Test without parent
    b = Base()
    assert b.get_path() == ""
test_Base_get_path.test = True



# Generated at 2022-06-13 07:55:53.002870
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    args = dict()
    obj = FieldAttributeBase(**args)
    assert isinstance(obj, FieldAttributeBase)
    assert obj.name is None
    assert obj.default is Sentinel
    assert not obj.required
    assert obj.aliases == []



# Generated at 2022-06-13 07:55:57.347002
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    data = {'vars': {'a': 'b'}}
    obj = FieldAttributeBase()
    try:
        obj.deserialize(data)
    except AnsibleAssertionError as e:
        assert str(e) == 'data ({}) should be a dict but is a <class \'dict\'>'.format(data)


# Generated at 2022-06-13 07:55:59.272914
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    pass # no need to test, as the method is just a stub

# Generated at 2022-06-13 07:56:07.922371
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    import unittest
    import ansible.parsing.yaml.objects


# Generated at 2022-06-13 07:56:09.123529
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    true_not_false = False
    assert true_not_false


# Generated at 2022-06-13 07:56:10.286868
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    assert True



# Generated at 2022-06-13 07:56:14.494340
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    from ansible.module_utils.ansible_modlib.hashivault import FieldAttributeBase
    from ansible.module_utils.ansible_modlib.hashivault import FieldAttribute
    test_instance = FieldAttributeBase()

    # test the copy() method
    result = test_instance.copy()
    assert isinstance(result, FieldAttribute)
    assert result.default is not None
    assert result.required is not None

# Generated at 2022-06-13 07:56:25.341675
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import fragment_loader
    from ansible.playbook.role import Role
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import module_loader
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.module_utils.six import string_types 
    from ansible.module_utils._text import to_text
    from ansible.playbook.play import Play as Play_inst
    from ansible.plugins.loader import action_loader

# Generated at 2022-06-13 07:56:59.387141
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.display import Display
    display = Display()
    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inv_manager)
    play_context = PlayContext()
    ds = dict(one=1, two="two")
    expected = dict(one=1, two="two")
    actual = FieldAttributeBase.load_data(ds, loader, templar=None)
    assert actual == expected



# Generated at 2022-06-13 07:57:09.538753
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():

    # Arrange
    klass = FieldAttributeBase
    self = FieldAttributeBase(obj=None, name=None, default=None, always_post_validate=None, fallback=None, type=None,
                              choices=None, aliases=None, inherit=True, static=False, required=False,
                              isa=None, no_log=False, ignore_errors=None, listof=None, class_type=None,
                              include=None, exclude=None)

    # Act/Assert
    with pytest.raises(NotImplementedError):
        self.squash(condensed=None)

# Generated at 2022-06-13 07:57:17.586555
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    f = FieldAttributeBase()
    setattr(f, '_valid_attrs', vars(f))
    setattr(f, '_loader', fake_loader)
    setattr(f, '_variable_manager', variable_manager)

    test_ds = dict(name='foo',
                   when="not fizz",
                   tags=['bar'],
                   register="bob")

    f.load_data(test_ds)

    assert isinstance(f.name, string_types)
    assert isinstance(f.when, string_types)
    assert isinstance(f.tags, list)
    assert isinstance(f.register, string_types)


# Generated at 2022-06-13 07:57:20.433800
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    assert FieldAttributeBase.dump_attrs == BaseComposite.dump_attrs


# Generated at 2022-06-13 07:57:32.527473
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    field_attributes = {}
    attr = FieldAttributeBase(False, False, False, False, False, False, False, False, True, None, None, None, None, None, None, None)
    kwargs = {}
    obj = AnsibleBase()

    def test_template(value):
        return True

    templar = MagicMock()
    templar.is_template = test_template
    templar.template = None
    templar._fail_on_undefined_errors = False
    templar.available_variables = {'omit': None}

    with patch.object(obj, '_validate_and_set') as mock_validate_and_set:
        obj._validate_and_set = mock_validate_and_set

# Generated at 2022-06-13 07:57:43.321956
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.utils.collection_loader._collection_finder import _get_collection_metadata_base

    def _create_attrs(src_dict, dst_dict):
        '''
        Helper method which creates the attributes based on those in the
        source dictionary of attributes. This also populates the other
        attributes used to keep track of these attributes and via the
        getter/setter/deleter methods.
        '''
        keys = list(src_dict.keys())
        for attr_name in keys:
            value = src_dict[attr_name]

# Generated at 2022-06-13 07:57:46.232252
# Unit test for method get_ds of class FieldAttributeBase
def test_FieldAttributeBase_get_ds():
    import ansible.utils.unsafe_proxy
    assert isinstance(FieldAttributeBase().get_ds(), ansible.utils.unsafe_proxy.AnsibleUnsafeText)


# Generated at 2022-06-13 07:57:54.053243
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    #
    # Test FieldAttributeBase.dump_attrs()
    #

    from ansible.errors import AnsibleParserError
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager


    # test dump_attrs() with a few basic types and structure
    loader = DataLoader()
    variable_manager = VariableManager()

    task_context = PlayContext()
    task_context.load_from_file = True


# Generated at 2022-06-13 07:57:55.855800
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    a = FieldAttributeBase(isa='foo')
    assert a.from_attrs([]) == {}


# Generated at 2022-06-13 07:57:59.619059
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    b = AnsibleBase()
    (rc, err) = b.dump_attrs()
    assert not rc
    assert err == "AnsibleBase.dump_attrs() is not implemented"

# Generated at 2022-06-13 07:58:50.441653
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.dumper import AnsibleDumper

    field_attribute_base = FieldAttributeBase()
    field_attribute = FieldAttribute()
    field_attribute_base.add_field(field_attribute)

    ansible_base_yaml_object = AnsibleBaseYAMLObject()
    ansible_mapping = AnsibleMapping()
    ansible_mapping.yaml_set_start_comment('test')
    ansible_base_yaml_object._ds = ansible_mapping
    field_attribute_base._ds = ansible_base_yaml_object

# Generated at 2022-06-13 07:58:55.393836
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    obj = FieldAttributeBase()
    obj.foo = 'bar'
    obj.baz = 'qux'
    obj.test_string_attributes = ['test_string_attributes']
    obj.test_int_attributes = 1
    obj.test_bool_attributes = True
    obj.test_percent_attributes = 2
    obj.test_list_attributes = ['test_list_attributes']
    obj.test_dict_attributes = {'key': 'value'}
    obj.test_class_attributes = {}
    result = obj.dump_attrs()

# Generated at 2022-06-13 07:58:58.046477
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    attrs = FieldAttributeBase()
    data = {'vars': {}}
    attrs.deserialize(data)
    attrs._valid_attrs = {}
    data = {'vars': {}}
    attrs.deserialize(data)




# Generated at 2022-06-13 07:59:02.205674
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    import ansible.parsing.yaml.objects
    obj = ansible.parsing.yaml.objects.AnsibleBaseYAMLObject()
    obj.register_loader()
    attr = 'foo'
    data = 'bar'

    # test the with loader
    obj.load_data(attr, data)
    assert obj.attributes[attr] == data

    # test the without loader
    obj.unregister_loader()
    obj.load_data(attr, data)
    assert obj.attributes[attr] == data
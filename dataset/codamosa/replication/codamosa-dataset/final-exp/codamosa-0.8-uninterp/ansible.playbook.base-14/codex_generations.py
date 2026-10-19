

# Generated at 2022-06-13 07:49:40.228140
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    # test_FieldAttributeBase_dump_attrs()
    FieldAttributeBase()


# Generated at 2022-06-13 07:49:52.022139
# Unit test for method get_path of class Base

# Generated at 2022-06-13 07:49:58.554708
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    for c in [object]:
        obj = c()
        attribute = FieldAttributeBase()
        try:
            obj.get_validated_value('name', attribute, value, templar)
        except Exception as e:
            print('Exception raised %s ' % e)


# Generated at 2022-06-13 07:50:09.124770
# Unit test for method from_attrs of class FieldAttributeBase

# Generated at 2022-06-13 07:50:11.255509
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    """Unit test for FieldAttributeBase method dump_me."""
    pass



# Generated at 2022-06-13 07:50:21.108795
# Unit test for method validate of class FieldAttributeBase

# Generated at 2022-06-13 07:50:32.665562
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    from ansible.playbook.task import Task

    data={"name": "test_task", "_uuid": "sdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsfsdf", "when": "fail_task.was_failed", "async_val": 5, "async_seconds": 5, "poll": 0, "_finalized": True, "_squashed": False}
    t = Task()
    t.deserialize(data)
    assert t.name == data['name']
    assert t.async_val == data['async_val']
    assert t.async_seconds == data['async_seconds']
    assert t.when == data['when']
    assert t._uuid == data['_uuid']

# Generated at 2022-06-13 07:50:42.473618
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    # Make sure the FieldAttributeBase can validate the type of the value
    FA = FieldAttributeBase('test', FieldAttributeBase.String)
    FA.validate(None)
    FA.validate(True)
    FA.validate(False)
    FA.validate(0)
    FA.validate(1)
    FA.validate(0.0)
    FA.validate(1.1)
    FA.validate([])
    FA.validate({})
    FA.validate('')
    FA.validate('string')
    FA.validate(u'string')
    FA.validate(b'string')
    # FA.validate(open())
    with pytest.raises(AnsibleAssertionError):
        FA.validate(set())

# Generated at 2022-06-13 07:50:49.253867
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    data = dict()
    data['a'] = 1
    data['b'] = 2
    data['c'] = 3
    data['d'] = 4
    data['e'] = 5

    #Test deserialize of FieldAttributeBase
    field_attribute_base = FieldAttributeBase()
    field_attribute_base.deserialize(data)
    assert field_attribute_base.a == 1

# Generated at 2022-06-13 07:51:01.706366
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    # Create a new instance of FieldAttributeBase and is_empty
    attr = FieldAttributeBase()
    assert attr.name is None
    assert attr.isa is None
    assert attr.default == NOT_SET
    assert attr.required is False
    mock_instance = 'AnsibleBase'
    mock_attr='value'
    mock_value = 'value'
    attr.__set__(mock_instance,mock_value,mock_attr)
    assert mock_instance._attributes[mock_attr] == mock_value
    #calling _load_vars
    attr.__get__(mock_instance,mock_attr)
    assert mock_instance._attributes[mock_attr] == mock_value
    #calling _extend_value
    mock_value = 'value1'

# Generated at 2022-06-13 07:51:31.744019
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    def test(obj, value):
        return obj.validate(value)
    assert test(FieldAttributeBase(isa='string'), 'foo') is True
    assert test(FieldAttributeBase(isa='bool'), True) is True

# Generated at 2022-06-13 07:51:42.254970
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    class TestParent(object):
        attr1 = "I'm an attribute"
    TestParent.__name__ = 'TestParent'
    class TestChild(TestParent):
        def __init__(self, attr2):
            self.attr2 = attr2
    # Test case 1
    #__name__ of TestChild is none
    TestChild.__name__ = None
    if TestChild.__name__ == None:
        print('Test case 1 is failed')
    else:
        print('Test case 1 is passed')
    # Test case 2
    #__name__ of TestChild is not none
    TestChild.__name__ = 'TestChild'
    if TestChild.__name__ == None:
        print('Test case 2 is failed')
    else:
        print('Test case 2 is passed')

test_Base

# Generated at 2022-06-13 07:51:47.531868
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    obj = FieldAttributeBase()
    name = ''
    attribute = FieldAttribute(isa='string')
    value = ''
    templar = ''
    assert isinstance(obj.get_validated_value(name, attribute, value, templar), six.text_type)


# Generated at 2022-06-13 07:51:51.662976
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():

    test = FieldAttributeBase(isa='bool', default=None)

    test.squash(False) == False
    test.squash(True) == True
    test.squash(None) == None


# Unit testing for FieldAttributeBase methods
# Note that most of the logic of FieldAttributeBase is tested via
# test_FieldAttributeBase_squash() and
# test_FieldAttributeBase_merge()


# Generated at 2022-06-13 07:51:52.751918
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    field = FieldAttributeBase()



# Generated at 2022-06-13 07:51:59.485147
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    reload(ansible.parsing.vault)

    # test get_validated_value
    fake_templar = DummyVars()

    # test string
    attr = FieldAttributeBase('test', False, 'str')
    value = Base.get_validated_value('test', attr, 1, fake_templar)
    assert value == '1'

    # test int
    attr = FieldAttributeBase('test', False, 'int')
    value = Base.get_validated_value('test', attr, '1', fake_templar)
    assert value == 1

    # test float
    attr = FieldAttributeBase('test', False, 'float')
    value = Base.get_validated_value('test', attr, '1.1', fake_templar)
    assert value

# Generated at 2022-06-13 07:52:12.512040
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
  from ansible.parsing.yaml.objects import AnsibleUnicode
  from ansible.parsing.yaml.objects import AnsibleSequence
  from ansible.parsing.yaml.objects import AnsibleMapping
  from ansible.parsing.yaml.data import DataLoader
  from ansible.plugins.vars.vars import VarsModule
  from ansible.plugins.vars.parsers.yaml import VarsYAMLParser
  from ansible.plugins.vars.parsers.fact import VarLoader
  from ansible.playbook.play_context import PlayContext
  from ansible.template import Templar
  from ansible.template import Templar
  from ansible.utils.vars import combine_vars
  from ansible.utils.vars import combine_vars
 

# Generated at 2022-06-13 07:52:15.015098
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():

    # FIXME: use factories for base class tests
    obj = FieldAttributeBase()

    ret = obj.dump_attrs()

    assert obj._valid_attrs == ret

# Generated at 2022-06-13 07:52:21.628840
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    f1 = FieldAttribute(isa='bar', required=True)
    f1.validate('foo', 'bar')
    f1.validate('foo', 'baz')
    f2 = FieldAttribute(isa='foo', required=False)
    f2.validate('foo', 'bar')
    f2.validate('foo', 'baz')
    ds = dict()
    f3 = FieldAttribute(isa='foo', required=True)
    try:
        f3.validate('foo', 'baz')
    except AnsibleParserError:
        pass
    try:
        f3.validate('foo', 'baz', ds)
    except AnsibleParserError as e:
        e_obj = e.__dict__
        assert e_obj['_obj'] == ds
    f4 = FieldAttribute

# Generated at 2022-06-13 07:52:25.831342
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    assert False, "Not implemented yet"

    # class Playbook(Base):
    #     pass

# class Base(FieldAttributeBase):
#     def get_search_path(self):
#         path_stack = []
#         return path_stack
# 
#     assert False, "Not implemented yet"
# 
#     # class Playbook(Base):
#     #     pass
# 

    # Unit test for method get_search_path of class Base
    # def test_Base_get_search_path():
    #     assert False, "Not implemented yet"
    # 
    #     # class Playbook(Base):
    #     #     pass
    # 



# Generated at 2022-06-13 07:53:00.536344
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    obj = FieldAttributeBase(class_name='FieldAttributeBase', default=None,
        attribute=None, isa=None, always_post_validate=False,
        exclude=False, static=False, name=None,
        choices=None, boolean=False, secret=False, version_added=None)
    obj.__dict__.update({'_validated': None, '_finalized': None,
        '_loader': None, '_variable_manager': None, '_valid_attrs': {},
        '_attr_defaults': {}, '_final_attrs': {}, '_uuid': None,
        '_alias_attrs': {}, '_attributes': {}, '_ds': None})
    kwargs = dict(name=None, attribute=None, value=None, templar=None)

# Generated at 2022-06-13 07:53:02.627298
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    test_obj = FieldAttributeBase()
    test_obj.copy( )


# Generated at 2022-06-13 07:53:10.273239
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    # check if paths are in the correct order
    task = Task()
    task._dep_chain = ['b', 'a', 'z']
    task._role_path = 'role'
    assert task.get_search_path() == ['role', 'b', 'a', 'z']

    task._ds._data_source = 'path_of_task'
    assert task.get_search_path() == ['role', 'b', 'a', 'z', 'path_of_task']

# Generated at 2022-06-13 07:53:18.351917
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    '''
    FieldAttributeBase.load_data
    '''

    @default('var')
    def default(self):
        return 'type'

    attr = FieldAttributeBase(default=default, always_post_validate=True)

    # Check if 'self' is really an instance of FieldAttributeBase
    assert isinstance(attr, FieldAttributeBase)

    # Check if the type of 'attr' is FieldAttributeBase
    assert type(attr) == FieldAttributeBase

    # Check if the correct value has been assigned to 'attr'
    assert attr == default

    # Check if this attribute has a default value
    assert attr.default == default

    # Check the type and value of 'attr'
    assert type(attr.always_post_validate) == bool
    assert attr.always_post_validate == True

    #

# Generated at 2022-06-13 07:53:26.349332
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
  data = {
    'new_attr': 'attr_value',
    'attr2': 'value2',
    'attr3': 'value3',
  }
  fa = FieldAttributeBase()
  assert fa.new_attr is None
  assert fa.attr2 is None
  fa.load_data(data)
  assert fa.new_attr == 'attr_value'
  assert fa.attr2 == 'value2'
  with pytest.raises(AttributeError):
    assert fa.attr3 == 'value3'

# Generated at 2022-06-13 07:53:27.448210
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    assert True

# Generated at 2022-06-13 07:53:29.535480
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    # FIXME: This is not a good unit test as it does not test
    # anything.
    assert False



# Generated at 2022-06-13 07:53:31.259335
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    # FIXME: Implement unit test
    pass

# Generated at 2022-06-13 07:53:33.288305
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    #Creates and returns a new object with type S, a subtype of T.
    pass


# Generated at 2022-06-13 07:53:38.209866
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    task_gen = TaskGenerator()
    task_vars = {"omit": set(), 'hostvars': {}}

    # test from_attrs
    task_vars = {"omit": set(), 'hostvars': {}}

    task_vars = {"omit": {"omit"}, 'hostvars': {}}


# Generated at 2022-06-13 07:54:05.190693
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    FieldAttributeBase_copy_fixture = [
        ('FieldAttributeBase()',
            FieldAttributeBase(),
            None,
        ),
    ]

    for fixture in FieldAttributeBase_copy_fixture:
        (desc, fld, expect_value) = fixture
        assert fld.copy() == expect_value

# Generated at 2022-06-13 07:54:18.158746
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    from units.mock.loader import DictDataLoader

    mock_loader = DictDataLoader({})

    attr_dict = {
        'aliases': [],
        'class_type': None,
        'default': None,
        'elements': {},
        'error': None,
        'immutable': False,
        'include_role': None,
        'include_tasks': None,
        'include_tasks_from': None,
        'include_vars': None,
        'private': False,
        'register': False,
        'required': False,
        'static': False,
        'vars': None,
        'version_added': None,
        'no_log': False,
        'deprecated': False,
    }


# Generated at 2022-06-13 07:54:24.631364
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    # Unit test for method validate of class FieldAttributeBase
    attr = FieldAttribute()  # noqa
    attr.display = "this is the help string"
    assert attr.validate(None, '/test') is True
    assert attr.validate(None, 23) is True
    assert attr.validate(None, "hello") is True
    assert attr.validate(None, {"key": "value"}) is True
    assert attr.validate(None, dict(key="value")) is True
    assert attr.validate(None, ['key', 'value']) is True
    assert attr.validate(None, ["hello", 23]) is True
    assert attr.validate(None, dict(hello="world")) is True
    assert attr.validate(None, dict(hello=[23]))

# Generated at 2022-06-13 07:54:28.382048
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    test_obj = FieldAttributeBase()
    try:
        test_obj.load_data(ds=None)
    except NotImplementedError:
        pass
    else:
        assert False, "NotImplementedError not raised"

# Generated at 2022-06-13 07:54:35.897583
# Unit test for method dump_attrs of class FieldAttributeBase

# Generated at 2022-06-13 07:54:36.778299
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    pass


# Generated at 2022-06-13 07:54:44.025123
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():

    # initialize test environment
    ans_mock = AnsibleModule(argument_spec={}, supports_check_mode=True)
    my_var = dict(my_var1='a', my_var2='b')
    templar = Templar(loader=None, variables=my_var)
    my_field = FieldAttributeBase('SomeField')
    # Run method with correct params
    result = my_field.post_validate(templar)

    assert result is None


# Generated at 2022-06-13 07:54:48.045971
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    obj = FieldAttributeBase()
    name = "p1"
    attribute = FieldAttribute()
    value = "ten"
    templar = FieldAttributeBase()
    result = obj.get_validated_value(name, attribute, value, templar)
    assert result == "ten"

# Generated at 2022-06-13 07:54:49.936931
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    obj = Base()
    res = obj.get_dep_chain()
    assert res is None


# Generated at 2022-06-13 07:54:51.683762
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    # FieldAttributeBase = ansible.utils.template.FieldAttributeBase
    # assert 
    raise SkipTest 


# Generated at 2022-06-13 07:55:13.635299
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    class MyClass(FieldAttributeBase):
        pass
    o = MyClass()
    o.post_validate(templar=None)

# Generated at 2022-06-13 07:55:14.868787
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    raise SkipTest('unimplemented test')


# Generated at 2022-06-13 07:55:21.471485
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    dep_chain1 = []
    dep_chain2 = ['first', 'second', 'third']
    dep_chain3 = ['first', 'second', 'third', 'fourth']

    test_class1 = Base()
    test_class1._parent = None

    test_class2 = Base()
    test_class2._parent = test_class1

    test_class3 = Base()
    test_class3._parent = test_class2

    test_class4 = Base()
    test_class4._parent = test_class3

    assert test_class1.get_dep_chain() is None
    assert test_class2.get_dep_chain() == dep_chain1
    assert test_class3.get_dep_chain() == dep_chain2
    assert test_class4.get_dep_chain() == dep_chain

# Generated at 2022-06-13 07:55:26.713979
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    obj = FieldAttributeBase()
    # test with bad value
    with pytest.raises(AnsibleParserError):
        obj.get_validated_value(name='name', attribute='attribute', value=None, templar=None)

# Generated at 2022-06-13 07:55:27.797052
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    pass

# Generated at 2022-06-13 07:55:30.174110
# Unit test for method get_path of class Base
def test_Base_get_path():
    base = Base()
    base._name = 'test_Base'
    assert base.get_path() == ''

# Generated at 2022-06-13 07:55:41.373274
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    base_obj = Base()
    assert base_obj.get_search_path() == []

    base_obj._parent = Base()
    base_obj._parent._parent = Base()
    base_obj._parent._parent._parent = Base()
    assert base_obj.get_search_path() == []

    base_obj._parent._role_path = "test_role_path"
    assert base_obj.get_search_path() == [base_obj._parent._role_path]

    base_obj._parent._parent._role_path = "test_role_path"
    assert base_obj.get_search_path() == [base_obj._parent._parent._role_path, base_obj._parent._role_path]

    base_obj._parent._parent._parent._role_path = "test_role_path"


# Generated at 2022-06-13 07:55:47.378329
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    obj = FieldAttributeBase()
    assert isinstance(obj, FieldAttributeBase)
    name = 'foo'
    attribute = 'foo'
    value = 'foo'
    templar = 'foo'
    result = obj.get_validated_value(name, attribute, value, templar)


# Generated at 2022-06-13 07:55:48.819243
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    assert True


# Generated at 2022-06-13 07:56:00.090977
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    from ansible.utils.vars import combine_vars

    class TestTask(object):
        def __init__(self, ds):
            self.vars = {}
            self.test = 'this is a test value'
            self.other = 'other value'
            self.some_vars = {}
            self._valid_attrs = dict(vars=dict(default=[], static=True, type='list'),
                                     test=dict(default='', static=False, type='str'),
                                     other=dict(default='', static=False, type='str'),
                                     some_vars=dict(default=[], static=False, type='list'))
            self._valid_attrs['vars']['isa'] = 'dict'

# Generated at 2022-06-13 07:56:30.820348
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    from ansible.vars import VariableManager
    from ansible.templar.template import Templar
    from ansible.parsing.dataloader import DataLoader

    dataloader = DataLoader()
    variable_manager = VariableManager()
    templar = Templar(loader=dataloader,
                      variables=variable_manager.get_vars(play=dict(name="play.yml")))


    # Create a test object
    baseobj = FieldAttributeBase()

    # Create a sample attribute structure
    attribute = Attribute()
    attribute.isa = 'bool'

    # Create test data
    value = 'True'

    # Test
    result = baseobj.get_validated_value('name', attribute, value, templar)

    # Verify the results
    assert(result == True)

    # Create

# Generated at 2022-06-13 07:56:38.758287
# Unit test for method get_validated_value of class FieldAttributeBase

# Generated at 2022-06-13 07:56:43.585499
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    obj = FieldAttributeBase()
    
    # Call method
    try:
        obj.deserialize(data=[])
        # Test should have failed with a TypeError
        assert False, "TypeError not raised"
    except TypeError:
        pass



# Generated at 2022-06-13 07:56:48.538966
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    '''
    Ensure that the deserialize method of class FieldAttributeBase properly
    sets the default values for a task.
    '''
    repr = dict()
    repr['name'] = 'test_name'
    repr['environment'] = dict()
    repr['environment']['FOO'] = 'BAR'
    repr['async'] = 1
    repr['poll'] = 0
    repr['ignore_errors'] = False
    repr['local_action'] = 'shell'
    repr['transport'] = 'paramiko'
    repr['args'] = 'echo test'
    repr['delegate_to'] = 'localhost'
    repr['run_once'] = False

    task = Task()
    task.deserialize(repr)
    assert task.name == 'test_name'
    assert task.environment == dict()


# Generated at 2022-06-13 07:56:56.728426
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    from _ast import Load
    from ansible.module_utils.six import PY2

    class Dict(dict):
        '''sub class of dict for test_BaseMeta___new__'''
        def __init__(self, *args, **kwargs):
            super(Dict,self).__init__(*args, **kwargs)
            self.prop_name = None
            self.self_ = None
            self.value = None
            self.prop_name = None
            self.self_ = None
            self.attrs = None
            self.dst_dict = None
            self.parents = None
            self.dct = None
            self.cls = None
            self.src_dict = None
            self.name = None
            self.dct = None



# Generated at 2022-06-13 07:56:57.936260
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    raise NotImplementedError


# Generated at 2022-06-13 07:57:10.667909
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    import os
    import tempfile
    import shutil
    import json
    from random import randint
    from six import string_types

    # test normal execution
    # create a dependency chain of roles, which is the same as file path chain
    role_path_chain = create_temp_dirs(randint(2, 5))

# Generated at 2022-06-13 07:57:18.966094
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():

    # create a mock playbook root task
    root_task = MockTask(type='ROOT')
    # create a mock playbook task
    pb_task = MockTask(type='PB', _parent=root_task)
    # create a mock playbook that contains the task
    pb = MockPlaybook(tasks=[pb_task])
    # create a mock role that depends on the playbook
    role = MockRole(_playbook=pb)
    # create a mock task that depends on the role
    dep_task = MockTask(type='ROLE', _parent=role)
    # create a mock task that depends on the previous task
    mock_task = MockTask(type='TASK', _parent=dep_task)

    # test the search path

# Generated at 2022-06-13 07:57:33.232016
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    # Create an instance of FieldAttributeBase()
    fieldattributebase_instance = FieldAttributeBase(attribute_name='',
                                                     attribute_type_name=None,
                                                     attribute_description=None,
                                                     allow_clone=False,
                                                     inherit_only=False,
                                                     required=False,
                                                     static=False,
                                                     sub_spec=None,
                                                     always_post_validate=False,
                                                     default=None,
                                                     choices=None,
                                                     aliases=None,
                                                     python_name=None,
                                                     isa=None,
                                                     listof=None,
                                                     class_type=None)
    # set attriutes of instance.
    fieldattributebase_instance.attribute_name = 'test_attribute_name'

# Generated at 2022-06-13 07:57:40.370106
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    ''' _post_validate_vars is called with the right arguments '''
    field_attribute_base = FieldAttributeBase()
    field_attribute_base.vars = {}
    field_attribute_base._post_validate_vars = lambda x, y, z: x + "_" + y
    assert field_attribute_base._load_vars(0, "test") == "test_"
test_FieldAttributeBase_deserialize()

# Generated at 2022-06-13 07:58:12.744852
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():

    # Set up test environment
    play = dict(
        hostvars = dict(),
        group_names = dict(),
        groups = dict(),
        inventory = dict(),
        _variable_manager = dict(),
        _loader = dict(),
    )

    # Execute the method to be tested
    test_instance = FieldAttributeBase(play)
    data = dict()
    result = test_instance.deserialize(data)
    assert result is None

    # Execute the method to be tested
    test_instance = FieldAttributeBase(play)
    data = 'test'
    with pytest.raises(AnsibleAssertionError) as excinfo:
        result = test_instance.deserialize(data)
    assert 'data (test) should be a dict but is a <' in to_native(excinfo.value)



# Generated at 2022-06-13 07:58:14.551660
# Unit test for method get_path of class Base
def test_Base_get_path():
    with pytest.raises(Exception):
        assert(Base().get_path())


# Generated at 2022-06-13 07:58:23.875103
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    class A(object):
        _valid_attrs = dict(a=FieldAttribute(isa='string', required=True),
                           b=FieldAttribute(isa='int', required=True),
                           c=FieldAttribute(isa='percent', required=True),
                           d=FieldAttribute(isa='bool', required=True),
                           e=FieldAttribute(isa='list', listof='string', required=True),
                           f=FieldAttribute(isa='dict', required=True))
        
        def post_validate(self, templar=None):
            pass
    
    a = A()
    assert a.get_validated_value('a', a._valid_attrs['a'], 'aaaaaaaaaa', None) == 'aaaaaaaaaa'

# Generated at 2022-06-13 07:58:27.999356
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    from collections import Mapping
    from copy import copy
    from copy import deepcopy
    from copy import _EmptyClass

    # Test with args
    # Call copy() with args
    # expected:
    fieldattributebase_instance = FieldAttributeBase('name')
    new_fieldattributebase_instance = fieldattributebase_instance.copy()
    assert new_fieldattributebase_instance._name == 'name'



# Generated at 2022-06-13 07:58:32.875259
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    # test_FieldAttributeBase_dump_attrs: Test dumping field attributes
    # Initialize the class
    obj = FieldAttributeBase()
    assert obj.__class__.__name__ == "FieldAttributeBase", "'__class__.__name__' must be 'FieldAttributeBase' but it is %s" % (obj.__class__.__name__)
    # Test FieldAttributeBase.dump_attrs
    attrs = obj.dump_attrs()
    expected_attrs = {}
    assert attrs == expected_attrs, "attrs is %s, expected_attrs is %s" % (attrs, expected_attrs)


# Generated at 2022-06-13 07:58:45.049748
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    from .test_vars import fake_loader
    from .test_vars import fake_variable_manager
    options = Options()
    my_vars = FakeVarsModule()
    my_variable_manager = VariableManager(loader=fake_loader(),
                                          inventory=None,
                                          version_info=version_info.VersionInfo())

    my_variable_manager._vars_cache = my_vars
    templar = Templar(loader=fake_loader(), variables=my_variable_manager,
                      shared_loader_obj=None, options=options)
    templar.available_variables = my_vars.my_vars
    FAKE_PARSER_ERR = u"fake parser error\n"
    FAKE_PARSER_ERR2 = u"fake parser error2\n"

# Generated at 2022-06-13 07:58:55.863639
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    # No value test
    assert_equal(deserialize({'value': None, 'otherfield': 'value'}), None)

    # Simple dict test
    val = dict(value=True, otherfield='value')
    assert_equal(deserialize(val), val)

    # Dict deep copy test
    val = dict(value=True, otherfield='value')
    res = deserialize(val)
    res['value'] = False
    assert_equal(val, dict(value=True, otherfield='value'))

    # List test
    val = []
    res = deserialize(val)
    assert_equal(val, res)

    # Simple list deep copy test
    val = [1, 2, 3]
    res = deserialize(val)
    res.append(4)
    assert_equal

# Generated at 2022-06-13 07:58:56.416846
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    pass

# Generated at 2022-06-13 07:58:57.772791
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    field_attribute_base = FieldAttributeBase()
    result = field_attribute_base.copy()



# Generated at 2022-06-13 07:58:59.028660
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    myobj = FieldAttributeBase()
    myobj.deserialize()
    assert True
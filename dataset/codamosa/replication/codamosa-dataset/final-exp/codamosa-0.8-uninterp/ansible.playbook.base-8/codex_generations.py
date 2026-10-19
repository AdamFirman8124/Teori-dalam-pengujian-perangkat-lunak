

# Generated at 2022-06-13 07:49:44.481860
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    field = FieldAttributeBase()
    field.validate(None)


# Generated at 2022-06-13 07:49:50.026906
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    # Test base case where we do not have
    subject = FieldAttributeBase()
    # Test that post_validate will call _post_validate_<attr> if it exists
    yield "assert subject.post_validate() is None, 'subject.post_validate() is not None'"


# Generated at 2022-06-13 07:50:03.570272
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    # dumps all attributes to a dictionary
    ####
    # Define a mock for the method we are testing
    ####
    global dump_attrs_mock
    dump_attrs_mock = FieldAttributeBase.dump_attrs = MagicMock()
    global _valid_attrs_mock
    _valid_attrs_mock = FieldAttributeBase._valid_attrs = MagicMock()
    global serialize_mock
    serialize_mock = FieldAttributeBase.serialize = MagicMock()
    mock_attrs = {'some_attr': 'foo', 'some_other_attr': 'bar'}
    _valid_attrs_mock.items.return_value = mock_attrs.items()
    ####
    # Call the method we are testing
    ####
    # Argument to the dump

# Generated at 2022-06-13 07:50:05.966710
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    FA = FieldAttributeBase('name', isa='string', required=True)
    FA.validate('name', 'name')


# Generated at 2022-06-13 07:50:08.801338
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    from ansiblelint.rules.AnsibleLintRule import FieldAttributeBase
    # Test setup
    # Test execution
    d = FieldAttributeBase()

    # Test assertions


# Generated at 2022-06-13 07:50:19.818681
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    f = FieldAttributeBase()
    f.isa = 'string'
    assert f.get_validated_value('name', f, '1', None) == '1'
    f.isa = 'int'
    assert f.get_validated_value('name', f, 1, None) == 1
    f.isa = 'float'
    assert f.get_validated_value('name', f, 1, None) == 1.0
    f.isa = 'bool'
    assert f.get_validated_value('name', f, 'yes', None) == True
    f.isa = 'percent'
    assert f.get_validated_value('name', f, '99%', None) == 99.0
    f.isa = 'list'

# Generated at 2022-06-13 07:50:22.929220
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    #
    # Return the original configuration of the object
    #

    obj = FieldAttributeBase()
    assert obj.dump_attrs() == {'_uuid': None, '_finalized': False, '_squashed': False}


# Generated at 2022-06-13 07:50:26.281352
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    test_obj = FieldAttributeBase()
    # test for the method post_validate(templar)
    test_obj.post_validate(templar)


# Generated at 2022-06-13 07:50:28.804569
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    field_attribute_base = FieldAttributeBase()
    assert field_attribute_base.dump_me() == True


# Generated at 2022-06-13 07:50:39.849053
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    # {'name': 'vars', 'required': False, 'static': False, 'always_post_validate': False, 'isa': 'class', 'class_type': <class 'ansible.parsing.yaml.objects.AnsibleBaseVars'>, 'default': <function AnsibleBaseVars.<lambda>>, 'listof': None}
    # {'name': 'vars', 'required': False, 'static': False, 'always_post_validate': False, 'isa': 'class', 'class_type': <class 'ansible.parsing.yaml.objects.AnsibleBaseVars'>, 'default': <function AnsibleBaseVars.<lambda>>, 'listof': None}
    assert hasattr(FieldAttributeBase, 'post_validate')
    # {'name': 'vars', 'required':

# Generated at 2022-06-13 07:51:06.004164
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
	pass

# Generated at 2022-06-13 07:51:10.945335
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    my_class = type('my_class', (object,), dict(a=BaseObject(), b=BaseObject(), c=BaseObject()))
    fixture = my_class()
    templar = DictData({})
    fixture.post_validate(templar)
    assert fixture.a._post_validate_called == True
    assert fixture.b._post_validate_called == True
    assert fixture.b._post_validate_called == True



# Generated at 2022-06-13 07:51:14.305415
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    '''
    Test if method dump_attrs serializes all attributes of FieldAttributeBase
    '''
    from .. import FieldAttributeBase
    attribute = FieldAttributeBase(field_name='name', isa='string', default='default value')
    assert attribute.dump_attrs() == {'field_name': 'name', 'isa': 'string', 'default': 'default value'}


# Generated at 2022-06-13 07:51:15.328117
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    FieldAttributeBase()

# Generated at 2022-06-13 07:51:19.901467
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
  data = {'finalized': False, 'squashed': False, 'name': 'test1'}
  x = FieldAttributeBase(None)
  x.deserialize(data)
  assert x.squashed == False
  assert x.finalized == False
  assert x.name == 'test1'

# Generated at 2022-06-13 07:51:29.908010
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    # The correct field is being squashed
    # The correct field is being squashed
    # The correct field is being squashed
    obj = FieldAttributeBase()
    fname = 'field'
    obj.declared_fields[fname] = obj.create_field(fname, 'string', default='default')
    val = 'this'
    obj.set_field_attr(fname, val)
    val2 = 'that'
    obj.set_field_attr(fname, val2)
    obj.squash_field(fname)
    assert obj.get_field_attr(fname) == val2
    # The correct field is being squashed
    # The correct field is being squashed
    # The correct field is being squashed
    # The correct field is being squashed
    obj = FieldAttributeBase()
   

# Generated at 2022-06-13 07:51:36.843460
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    config = dict(
        name=dict(required=True),
        src=dict(),
        dest=dict(),
        state=dict(default='present', choices=['present', 'directory', 'absent']),
        force=dict(type='bool', default=False)
    )
    obj = FieldAttributeBase(config)
    assert obj.name == 'FieldAttributeBase'
    assert obj.valid_attrs == config
    result = obj.load_data(dict(state='present', src='hello', dest='world', force=True))
    assert result == True
    assert obj.state == 'present'
    assert obj.src == 'hello'
    assert obj.dest == 'world'
    assert obj.force == True

# Generated at 2022-06-13 07:51:45.288665
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    # Initializing the valid attrs and attribute defaults
    FieldAttributeBase._valid_attrs = construct_valid_attributes()
    FieldAttributeBase._attr_defaults = construct_attribute_defaults()

    FieldAttributeBase._valid_attrs['one_attr'].default = lambda: 'one_attr_default'
    FieldAttributeBase._valid_attrs['two_attr'].default = lambda: 'two_attr_default'

    # Testing the copy function with and without data
    obj = FieldAttributeBase()
    obj.one_attr = "one_attr_data"
    obj.two_attr = "two_attr_data"

    obj_copy = obj.copy()

    assert obj_copy._attributes == obj._attributes
    assert obj_copy._attr_defaults == obj._attr_defaults
    assert obj_copy._

# Generated at 2022-06-13 07:51:48.146724
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    base = FieldAttributeBase()
    base.name = "foo"
    assert base.dump_attrs() == {'name': 'foo'}


# Generated at 2022-06-13 07:51:49.890812
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    assert hasattr(FieldAttributeBase, 'copy') and callable(getattr(FieldAttributeBase, 'copy'))

# Generated at 2022-06-13 07:52:16.513707
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    fake_ds = dict()
    fake_ds['data'] = dict()
    fake_ds['data']['name'] = 'test_deserialize'
    obj = FieldAttributeBase(ds=fake_ds)
    obj.deserialize()
    assert(obj.ds == fake_ds['data'])

# Generated at 2022-06-13 07:52:26.159321
# Unit test for method load_data of class FieldAttributeBase

# Generated at 2022-06-13 07:52:27.747380
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    a = FieldAttributeBase()
    ret = a.validate('abc')
    assert ret == True


# Generated at 2022-06-13 07:52:34.098786
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    p = Play()
    p.load({
        'name': 'play1',
        'hosts': 'localhost',
        'gather_facts': 'no',
        'roles': [
            {
                'role1': {
                    'name': 'role1',
                    'tasks': [
                        {'debug': 'msg=role1:task1'}
                    ]
                }
            },
            {
                'role2': {
                    'name': 'role2',
                    'tasks': [
                        {'include': 'role=role1'}
                    ]
                }
            }
        ],
        'tasks': [
            {'debug': 'msg=play1:task1'},
            {'include': 'role=role2'}
        ]
    })
    p.post_validate

# Generated at 2022-06-13 07:52:35.081469
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    args = dict()
    obj = FieldAttributeBase()
    obj.from_attrs(args)


# Generated at 2022-06-13 07:52:40.401946
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from ansible.errors import AnsibleParserError
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from jinja2.exceptions import UndefinedError
    from yaml.scanner import ScannerError
    
    class TestObj(object):
        
        def __init__(self, attribute_type, answer, data=None, finalize=False):
            
            self._loader = None
            self._variable_manager = None
            self._validated = False
            self._finalized = False
            self._squashed = False
            self._uuid = 'test-uuid'
            

# Generated at 2022-06-13 07:52:41.971848
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    FA = FieldAttributeBase()
    attr = FieldAttributeBase.FieldAttribute()
    FA.get_validated_value(name, attr, value, templar)


# Generated at 2022-06-13 07:52:52.599358
# Unit test for method get_path of class Base
def test_Base_get_path():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    ds = dict(task=dict())
    ds['task']['name']="test_task"
    ds['task']['path']="./test/test_Base_get_path.yml"
    ds['task']['position']=1
    task_ds = DataLoader().load(ds['task']['path'])[0]
    task_ds._line_number = ds['task']['position']
    task_ds._data_source = ds['task']['path']
    #

# Generated at 2022-06-13 07:53:04.994766
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    from ansible.executor.task_queue_manager import TaskQueueManager

    class Dummy(TaskQueueManager):
        pass

    class DummyTask(Dummy):
        _uuid = None
        _finalized = False
        _squashed = False

        # define a class attribute

# Generated at 2022-06-13 07:53:09.589447
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    Y = TypeData(u'string')
    X = TypeData(u'string')
    data = dict(X = X, Y = Y)
    obj = dict()

    a = FieldAttributeBase.deserialize(data, obj)
    assert a is obj


# Generated at 2022-06-13 07:54:08.299261
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    ds = dict(hello='123', world='456')
    field = FieldAttributeBase(class_type='FieldAttributeBase')
    assert field.deserialize(ds) == {}
    assert isinstance(field, FieldAttributeBase)
    ds = dict(hello=123, world='456')
    field = FieldAttributeBase(class_type='FieldAttributeBase')
    assert field.deserialize(ds) == {}
    assert isinstance(field, FieldAttributeBase)

# Generated at 2022-06-13 07:54:19.915475
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    from ansible.errors import AnsibleError
    from ansible.plugins.module_utils.basic import AnsibleModule
    class TestAnsibleModule:
        NO_CLI = True
        def __init__(self, **kwargs):
            self.params = {}
        def fail_json(self, **kwargs): pass
        def exit_json(self, **kwargs): pass
    class TestAnsibleAction(type):
        def __new__(cls, name, parents, dct):
            def _process_parents(parents, dst_dict):
                for parent in parents:
                    if hasattr(parent, '__dict__'):
                        _create_attrs(parent.__dict__, dst_dict)
                        new_dst_dict = parent.__dict__.copy()

# Generated at 2022-06-13 07:54:24.148197
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    value = FieldAttributeBase.get_validated_value('playbook_path', 'string', '', None)
    assert value == ''
    value = FieldAttributeBase.get_validated_value('playbook_path', 'string', None, None)
    assert value is None



# Generated at 2022-06-13 07:54:26.231368
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    '''
    for testing

    :return None:
    '''
    raise Exception("Not implemented")


# Generated at 2022-06-13 07:54:27.963673
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    assert False # XXX TODO implement your test here


# Generated at 2022-06-13 07:54:36.817063
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    class C1(object):
        a1 = 1
        _a2 = 1
        a3 = FieldAttribute()
        a4 = FieldAttribute(default=1)
        a5 = FieldAttribute(default=1, exclude=["a5"])
        _a6 = FieldAttribute(default=1, exclude=["a5"])
        a7 = FieldAttribute(default=1, inherit=False)
        a8 = FieldAttribute(default=1, alias="a8_alias")
        a9 = FieldAttribute(default=1, alias="a9 alias")
        a10 = FieldAttribute(default=1, exclude=["a9 alias"])

    class C2(C1):
        a11 = FieldAttribute()
        a12 = FieldAttribute(default=1)

# Generated at 2022-06-13 07:54:40.198130
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    try:
        assert False
    except:
        BaseMeta.__new__(BaseMeta, "name", "parents", "dct")
        raise

# Generated at 2022-06-13 07:54:47.693585
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    FA = FieldAttributeBase
    attr = FA(default='test_value')
    assert attr.load_data('value') == 'value'
    attr = FA(default='test_value')
    assert attr.load_data(None) == 'test_value'
    attr = FA(default='test_value')
    assert attr.load_data('value', 'name') == 'value'
    attr = FA(default='test_value')
    assert attr.load_data(None, 'name') == 'test_value'


# Generated at 2022-06-13 07:54:51.302971
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    '''
    Unit test dump_me.
    '''
    a = FieldAttributeBase()
    repr = a.dump_me()
    assert repr == {'isa': 'FieldAttribute', 'static': False, 'name': 'FieldAttributeBase', 'required': False}


# Generated at 2022-06-13 07:54:53.601458
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    fa = FieldAttributeBase()
    copy = fa.copy()
    assert copy._uuid is not None


# Generated at 2022-06-13 07:56:14.002529
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    from ansible.executor.task_executor import TaskExecutor
    from ansible.vars import VariableManager
    import ansible.playbook.play

    te = TaskExecutor(play=ansible.playbook.play.Play(), variable_manager=VariableManager())

    t = FieldAttributeBase.from_attrs(dict(ds=dict(type='test'), _loader=None, _variable_manager=None, _validated=False, _finalized=False, _uuid='1234567890', _squashed=False),
                        te)
    assert t.ds.type == 'test'
    assert t._loader == None
    assert t._variable_manager == None
    assert t._validated == False
    assert t._finalized == False
    assert t._uuid == '1234567890'
    assert t._squashed

# Generated at 2022-06-13 07:56:14.833317
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    pass

# Generated at 2022-06-13 07:56:25.579381
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    from copy import copy
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    
    data = dict(a='b', c=9, d=['1', '2', '3'], e=dict(f='g', h='i'), j=False, k=copy(AnsibleUnsafeText('l')))
    target = FieldAttributeBase()
    target.from_attrs(data)
    assert target.a == 'b'
    assert target.c == 9
    assert target.d == ['1', '2', '3']
    assert target.e == dict(f='g', h='i')
    assert target.j is False
    assert target.k == 'l'
    # target.v

# Generated at 2022-06-13 07:56:28.337981
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    field_attribute_base = FieldAttributeBase(answer=42)
    assert field_attribute_base.copy() == FieldAttributeBase(answer=42)


# Generated at 2022-06-13 07:56:31.238079
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    fd = FieldAttributeBase()
    assert fd.get_validated_value('name', 'attribute', 'value', 'templar') is not None



# Generated at 2022-06-13 07:56:33.329952
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    '''
    unit test for method load_data of class FieldAttributeBase
    '''

    return

# Generated at 2022-06-13 07:56:35.237838
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    '''
    Test method from_attrs of class FieldAttributeBase
    '''
    # Test to see if the class can be instantiated.
    myobj = FieldAttributeBase()

    assert_equal(myobj.__class__.__name__, "FieldAttributeBase")

# Generated at 2022-06-13 07:56:36.942000
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    f = FieldAttributeBase()
    assert f.deserialize(None) == None


# Generated at 2022-06-13 07:56:38.120670
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    # TODO: Implement test for the test_load_data method
    pass

# Generated at 2022-06-13 07:56:49.696295
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    # Test the method with a string
    a = FieldAttributeBase()
    a.load_data('why')
    assert a.value == 'why'

    # Test the method with a boolean value
    b = FieldAttributeBase()
    b.load_data(True)
    assert b.value == True

    # Test the method with a set
    c = FieldAttributeBase()
    c.load_data(set(['what', 'how']))
    assert c.value == set(['what', 'how'])

    # Test the method with an integer
    d = FieldAttributeBase()
    d.load_data(42)
    assert d.value == 42

    # Test the method with a list
    e = FieldAttributeBase()
    e.load_data([1, 2, 3])

# Generated at 2022-06-13 07:58:07.707940
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    a = BaseObject()
    b = BaseObject()
    c = BaseObject()
    d = BaseObject()
    e = BaseObject()
    # create dependency chain: a-->b-->c-->d-->e
    a._parent = b
    b._parent = c
    c._parent = d
    d._parent = e
    # this should return the dependency chain
    assert a.get_dep_chain() == [b, c, d, e]


# Generated at 2022-06-13 07:58:08.734547
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    base = FieldAttributeBase()
    assert base.load_data == None


# Generated at 2022-06-13 07:58:10.522923
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    model = FieldAttributeBase()

    # TODO: Add tests
    return

# Generated at 2022-06-13 07:58:12.743946
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    obj = FieldAttributeBase()
    result = obj.squash('foo', 'bar')
    assert True # TODO: implement your test here


# Generated at 2022-06-13 07:58:15.626913
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    field_attribute_base = FieldAttributeBase()
    field_attribute_base.post_validate()
    assert field_attribute_base is not None


# Generated at 2022-06-13 07:58:21.261514
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    foobar = Foobar()
    foobar.deserialize({u'_uuid': '1c0a8d6f-c6e2-4a0c-8fe9-a67b3a1a0f22'})
    assert foobar._uuid == u'1c0a8d6f-c6e2-4a0c-8fe9-a67b3a1a0f22'



# Generated at 2022-06-13 07:58:28.176817
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    # create an instance of the class we want to test
    field_attribute_base = FieldAttributeBase()
    # simulate loading data into field_attribute_base.name
    field_attribute_base.name = 'name'
    # simulate loading data into field_attribute_base.required
    field_attribute_base.required = True
    # simulate loading data into field_attribute_base.static
    field_attribute_base.static = True
    # simulate loading data into field_attribute_base.default
    field_attribute_base.default = 'default'
    # simulate loading data into field_attribute_base.aliases
    field_attribute_base.aliases = ['aliases']
    # simulate loading data into field_attribute_base.always_post_validate
    field_attribute_base.always_post_validate = True
    # simulate loading data

# Generated at 2022-06-13 07:58:34.073789
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    a = FieldAttributeBase(required=True, always_post_validate=True, isa='int')
    b = FieldAttributeBase(required=True, always_post_validate=True, isa='bool')
    c = FieldAttributeBase(required=True, always_post_validate=True, isa='list')
    assert a.post_validate("12345") == 12345
    assert b.post_validate("True") == True
    assert b.post_validate("true") == True
    assert b.post_validate("yes") == True
    assert b.post_validate("y") == True
    assert b.post_validate("1") == True
    assert b.post_validate("False") == False
    assert b.post_validate("false") == False
    assert b.post_valid

# Generated at 2022-06-13 07:58:39.502178
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    field_attribute_base = FieldAttributeBase(init_default=False)
    assert field_attribute_base.dump_me() is False
    field_attribute_base_1 = FieldAttributeBase(init_default=True)
    assert field_attribute_base_1.dump_me() is True

# Generated at 2022-06-13 07:58:50.311456
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    '''
    Make sure the :class:`FieldAttributeBase` post_validate works
    '''

    class Foo(FieldAttributeBase):
        '''
        A test class for FieldAttributeBase
        '''
        def __init__(self, attr, value):
            self.attr = attr
            self.value = value
            super(Foo, self).__init__()

        _valid_attrs = dict(
            foo=dict(isa='list', required=True),
            bar=dict(isa='list')
        )

    obj = Foo('foo', [1,2,3])
    reference = [1,2,3]

    assert obj.foo == reference, "obj.foo should match %s but it is %s" % (reference, obj.foo)

    obj = Foo('foo', 1)
   
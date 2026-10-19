

# Generated at 2022-06-13 07:50:09.453755
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    from ansible.utils.debug import disable_debugger_on_exception
    from ansible.module_utils.six.moves import StringIO

    my_io = StringIO()

    _worker = ansible.module_utils.facts.worker.Worker()
    _worker.action = 'gather'
    _worker.basedir = '/usr/lib/python2.7/site-packages/ansible/modules'
    _worker.get_basedir = lambda: '/usr/lib/python2.7/site-packages/ansible/modules'

    _executor = ansible.plugins.action.ActionModule(_worker, my_io)
    _executor._shared_loader_obj = None
    _executor._config_module = None
    _executor._display = ansible.utils.display.Display()
    _exec

# Generated at 2022-06-13 07:50:20.254213
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():

    # 1. Make an instance of FieldAttributeBase and validate the defaults
    obj = FieldAttributeBase()

    assert obj.default is None
    assert obj.class_type == None
    assert obj.listof == None
    assert obj.protected == False
    assert obj.required == True
    assert obj.static == False
    assert obj.always_post_validate == False

    # 2. Make a copy of the FieldAttributeBase object and validate
    #  the defaults for the copy
    obj_copy = obj.copy()

    assert obj_copy.default is None
    assert obj_copy.class_type == None
    assert obj_copy.listof == None
    assert obj_copy.protected == False
    assert obj_copy.required == True
    assert obj_copy.static == False

# Generated at 2022-06-13 07:50:20.813588
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    pass

# Generated at 2022-06-13 07:50:26.938768
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    setattr_call_count = 0
    def setattr(self, attr, value):
        nonlocal setattr_call_count
        setattr_call_count += 1
        raise Exception('TEST_EXCEPTION')
    def isinstance(o, c):
        return False
    def value_isinstance(o, c):
        return True
    attrs = {}
    class_type = {}
    mocker.patch('ansible.utils.boolean.boolean', return_value=True)
    mocker.patch('ansible.utils.display.warning')
    mocker.patch('ansible.utils.unsafe_proxy.UnsafeProxy', side_effect=lambda s: s)
    mocker.patch('ansible.errors.AnsibleParserError', side_effect=Exception('TEST_EXCEPTION'))

# Generated at 2022-06-13 07:50:38.343121
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.template import Templar

    obj = Play()
    attrs = {'name': 'test1', 'hosts': 'test2', 'roles': 'test3', 'tasks': 'test4'}
    obj.from_attrs(attrs)
    assert obj.name == 'test1'
    assert obj.hosts == 'test2'
    assert obj.roles == 'test3'
    assert obj.tasks == 'test4'

    obj = Task()

# Generated at 2022-06-13 07:50:46.461640
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleMapping
    from ansible.vars.hostvars import HostVars
    from ansible.vars.reserved import Reserved
    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    # Initialize test environment
    # Set up test objects
    test_type = HostVars()

    # Set up test defaults
    FAIL = False
    PASS = True

    ###############################################################################
    # Unit tests for method validate of class FieldAttributeBase
    ###############################################################################
    # Test #1 - Verify that a AnsibleMapping raises the correct exception
    ###############################################################################

# Generated at 2022-06-13 07:50:51.052820
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    Base = Base()
    Base.__dict__['_parent'] = 1
    assert Base.get_search_path() == None

    Base.__dict__['_parent'] = None
    assert Base.get_search_path() == None

    class A():
        def get_dep_chain():
            return [1]

    Base.__dict__['_parent'] = A()
    Base.__dict__['_parent'].get_dep_chain = Base.__dict__['_parent'].get_dep_chain
    Base.__dict__['_parent'].__dict__['_role_path'] = '/home/ansible/'
    assert Base.get_search_path() == ['/home/ansible/']


# Generated at 2022-06-13 07:51:02.895604
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    loader = DataLoader()

    # Test with string isa
    attribute_mock = mock.create_autospec(FieldAttributeBase, FieldAttributeBase())
    attribute_mock.isa = 'string'
    attribute_mock.always_post_validate = True
    attribute_mock.required = False
    attribute_mock.static = False
    attribute_mock.class_type = None

    # Test with string
    field_mock = mock.Mock()
    field_mock.get_ds.return_value = "/etc/ansible/hosts"
    templar = Templar(loader=loader)

# Generated at 2022-06-13 07:51:08.076687
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    # Test with a Role.
    base = Base()
    setattr(base, '_parent', '_parent')
    setattr(base, '_parent', '_parent')
    setattr(base._parent, '_parent', '_parent')
    setattr(base._parent._parent, '_parent', '_parent')

    setattr(base._parent, '_role_path', 'some_role_path')
    setattr(base._parent._parent, '_role_path', 'some_role_path2')
    setattr(base._parent._parent._parent, '_role_path', 'some_role_path3')
    setattr(base._parent._parent._parent._parent, '_role_path', 'some_role_path4')

# Generated at 2022-06-13 07:51:14.538514
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    # Create an instance of FieldAttributeBase
    field_attribute_base_instance = FieldAttributeBase()
    # Create a new data structure with 'name' defined
    data_structure = MagicMock(spec=dict)
    data_structure.get.return_value = 'test-name'
    # Store result of calling the load_data method
    field_attribute_base_instance.load_data(data_structure)
    # Check if the load_data method has been called with the data_structure
    data_structure.get.assert_called_with(field_attribute_base_instance.name, None)
    # Check if the name attribute is set to 'test-name'
    assert field_attribute_base_instance.name == 'test-name'

# Generated at 2022-06-13 07:51:58.323552
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
  # TODO: Implement test
  return


# Generated at 2022-06-13 07:52:00.325590
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    FieldAttributeBase()  # TODO: implement your test here

# Generated at 2022-06-13 07:52:12.242831
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    field_attribute_base = FieldAttributeBase(valid_python=None, valid_yaml=None, valid_ini=None, always_post_validate=None)

    # test_1
    test_1_attr_name = 'attr_name'
    test_1_ds = 'ds'
    test_1_loader = 'loader'
    test_1_validate_only = 'validate_only'
    expected_1_result = None

    test_1_result = field_attribute_base.load_data(test_1_attr_name, test_1_ds, test_1_loader, test_1_validate_only)
    assert test_1_result == expected_1_result




# Generated at 2022-06-13 07:52:16.699723
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    obj = FieldAttributeBase(isa='int', attribute='test')
    kwargs = dict()
    kwargs['name'] = 'test'
    kwargs['attribute'] = 'test'
    kwargs['value'] = 'test'
    kwargs['templar'] = 'test'
    obj._get_validated_value(**kwargs)

# Generated at 2022-06-13 07:52:21.061539
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    module = AnsibleModule(
        argument_spec = dict(
            name = dict(type='str'),
            state = dict(type='str', default='present', choices=['absent', 'present']),
            debug = dict(type='bool', default=False),
        ),
        supports_check_mode=True
    )
    data = module.params
    # deserialize(data)
    obj = FieldAttributeBase()
    obj.deserialize(data)
    result = obj.serialize()
    assert result == data

# Generated at 2022-06-13 07:52:28.740072
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():

    # initialize
    f1 = FieldAttributeBase()
    f2 = FieldAttributeBase()
    f3 = dict
    f4 = FieldAttributeBase()
    f5 = FieldAttributeBase()
    f6 = dict
    f7 = dict
    f8 = dict

    # test
    f1.from_attrs(f3)
    f2.from_attrs(f6)
    f4.from_attrs(f7)
    f5.from_attrs(f8)
    assert f1._finalized == False
    assert f2._finalized == True
    assert f4._squashed == False
    assert f5._squashed == True


# Generated at 2022-06-13 07:52:36.546048
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    # Set up mock objects
    f1 = FieldAttributeBase()
    f1._valid_attrs = {'field_name': 'mock_value'}
    f1._attributes = {'field_name': mock.Mock()}
    f1._attributes['field_name'].value = 'mock_value'

    # Test normal execution
    result = f1.dump_attrs()
    assert result == {'field_name': 'mock_value'}

    # Test with exception
    f1._attributes['field_name'].value = ['mock_value']
    with pytest.raises(AnsibleAssertionError) as excinfo:
        result = f1.dump_attrs()
    assert 'Expected' in to_text(excinfo.value)



# Generated at 2022-06-13 07:52:37.989895
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    o = FieldAttributeBase()
    o._valid_attrs = {}
    b = o.dump_attrs()
    assert b == {}


# Generated at 2022-06-13 07:52:38.439986
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    pass

# Generated at 2022-06-13 07:52:39.701864
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    f = FieldAttributeBase()
    assert f.validate(None) is None
test_FieldAttributeBase_validate()


# Generated at 2022-06-13 07:53:28.182199
# Unit test for method get_path of class Base
def test_Base_get_path():
    """
    returns the absolute path of the playbook object and its line number
    """
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    b = Base()
    play = Play()
    play._ds = '/var/ansible/test/test.yml'
    block = Block()
    block._parent = play
    task = Task()
    task._parent = block
    b._ds = '/var/ansible/test/test.yml'
    b._ds._line_number = 10
    assert b.get_path() == '/var/ansible/test/test.yml:10'

    b._ds = '/var/ansible/test/test.yml'
    b._ds._line_number = None
   

# Generated at 2022-06-13 07:53:29.311085
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    attr = FieldAttributeBase()
    assert attr is not None


# Generated at 2022-06-13 07:53:31.019824
# Unit test for method get_ds of class FieldAttributeBase
def test_FieldAttributeBase_get_ds():
    my_field = module_utils.FieldAttributeBase()



# Generated at 2022-06-13 07:53:41.256272
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
  from ansible.module_utils.six import string_types
  from ansible.module_utils.six import integer_types
  from ansible.module_utils.six import binary_type
  from ansible.module_utils.six import text_type
  from ansible.module_utils.six import PY2
  from ansible.utils.unsafe_proxy import AnsibleUnsafeText
  from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes
  from ansible.errors import AnsibleParserError
  class test_obj():
    def __init__(self, ds):
      self._validated=False
      self._uuid=None
      self._finalized=False
      self._squashed=False
      self.ds=ds
  # Exercise the field_name='port' branch of the if statement

# Generated at 2022-06-13 07:53:44.789927
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    parent = BaseMeta('parent', (), {})
    child = BaseMeta('child', (parent,), {})
    assert child.__dict__ == parent.__dict__



# Generated at 2022-06-13 07:53:54.440373
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    l = []
    task = Task()
    task.get_search_path()
    task._parent = Base()
    l.append(task)
    task._parent = l
    assert task.get_search_path() == None
test_Base_get_search_path()


# Generated at 2022-06-13 07:53:56.402920
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    assert isinstance(FieldAttributeBase.dump_attrs(), dict)

# Generated at 2022-06-13 07:54:05.382114
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    """Test: method dump_me of class FieldAttributeBase."""
    FA = FieldAttributeBase()
    FA.name = 'test'
    FA.isa = 'dict'
    FA.required = True
    FA.always_post_validate = False
    FA.aliases = ['testvar']
    FA.default = dict()
    FA.static = False
    expected = {
        'name': 'test',
        'isa': 'dict',
        'required': True,
        'always_post_validate': False,
        'aliases': ['testvar'],
        'default': dict(),
        'static': False
    }
    assert_equals(FA.dump_me(), expected)



# Generated at 2022-06-13 07:54:08.182563
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    # TODO: test for method load_data of class FieldAttributeBase
    pass

# Generated at 2022-06-13 07:54:10.348581
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    assert True




# Generated at 2022-06-13 07:54:33.005502
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
  test_obj1 = FieldAttributeBase()
  test_obj1.post_validate( templar = [] )


# Generated at 2022-06-13 07:54:36.626057
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    args = {}
    kwargs = {}
    command_name = 'TestCommandName'
    example_value = 'example_value'
    test_obj = FieldAttributeBase(command_name, args, kwargs, example_value)
    # Empty test
    test_obj.post_validate()


# Generated at 2022-06-13 07:54:43.419424
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    #
    # Note: these tests are not meant to be complete.
    #

    # instantiate the class
    fab = FieldAttributeBase()

    # There are no *_attrs attributes in this class,
    # so _valid_to_default and _default_to_valid do not do anything

    # test a string
    value = "string value"
    attribute = FieldAttribute()
    attribute.isa = 'string'
    assert fab.get_validated_value('', attribute, value, None) == value

    # test an integer
    value = "5"
    attribute.isa = 'int'
    assert fab.get_validated_value('', attribute, value, None) == int(value)

    # test a float
    value = "5.5"
    attribute.isa = 'float'
    assert fab.get_valid

# Generated at 2022-06-13 07:54:45.156609
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    BaseMeta._create_attrs()
    BaseMeta._process_parents()


# Generated at 2022-06-13 07:54:54.084733
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    test_obj = FieldAttributeBase()
    test_obj.attributes = {}
    test_obj.attr_defaults = {}
    test_obj.loader = None
    test_obj.variable_manager = None
    test_obj.validated = False
    test_obj.finalized = False
    test_obj.valid_attrs = {}
    test_obj.alias_attrs = {}
    test_obj.groups = {}
    test_obj.required_if = {}
    test_obj._ds = None
    test_obj.post_validate({})
    test_obj._post_validate_name({}, '', {})
    test_obj._post_validate_a({}, '', {})
    test_obj._post_validate_name({}, '', {})
    test_obj._load_v

# Generated at 2022-06-13 07:54:57.210095
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    _me = FieldAttributeBase(name='foo', isa='int')
    _dump = _me.dump_me()
    assert _dump == "name=foo isa=int"


# Generated at 2022-06-13 07:55:00.054180
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    # create test object
    obj = AnsibleBase()
    # run the method with different parameters
    test_get_validated_value(obj)



# Generated at 2022-06-13 07:55:04.369856
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    # Create an object of class FieldAttributeBase
    FieldAttributeBase_obj = FieldAttributeBase()
    
    # Try calling the post_validate method
    # No set up required
    # No clean up required
    # No exceptions should be raised
    FieldAttributeBase_obj.post_validate()

# Generated at 2022-06-13 07:55:14.200639
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    obj = FieldAttributeBase(False, 'str')
    assert obj.get_validated_value(None, None, 'abc', None) == 'abc'
    obj = FieldAttributeBase(False, 'int')
    assert obj.get_validated_value(None, None, '123', None) == 123
    obj = FieldAttributeBase(False, 'float')
    assert obj.get_validated_value(None, None, '123.4', None) == 123.4
    obj = FieldAttributeBase(False, 'bool')
    assert obj.get_validated_value(None, None, 'True', None) == True
    assert obj.get_validated_value(None, None, 'False', None) == False
    assert obj.get_validated_value(None, None, '', None) == False
    obj = Field

# Generated at 2022-06-13 07:55:15.929756
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    field_attribute_base = FieldAttributeBase()
    field_attribute_base.from_attrs()



# Generated at 2022-06-13 07:55:52.793556
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    b1 = Base()
    fake_task = lambda :0
    fake_task.__dict__ = {'_ds': {'_data_source': '/dir1', '_line_number': '10'}, '_parent': {'_play': {'_ds': {'_data_source': '/dir2', '_line_number': '15'}}}}
    b1.__dict__ = {'_parent': {'_role_path': '/dir1/roles/r1'}, '_task': fake_task}
    assert b1.get_search_path() == ['/dir1/roles/r1', '/dir2']

# Generated at 2022-06-13 07:55:54.663472
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    data = {}
    obj = FieldAttributeBase()
    assert obj.load_data(data) == None


# Generated at 2022-06-13 07:56:02.694411
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    import json
    import pprint

    # prepare
    my_instance = FieldAttributeBase()

    # execute
    my_result = my_instance.dump_me()

    # verify
    assert(type(my_result) == dict)
    assert(my_result["version"] == VERSION)

    # debug
    print("my_result:\n%s", pprint.pformat(my_result))
    with open("test_FieldAttributeBase_dump_me.dump", "w") as my_file:
        my_file.write(json.dumps(my_result))
    print("wrote test_FieldAttributeBase_dump_me.dump")



# Generated at 2022-06-13 07:56:11.183840
# Unit test for method get_ds of class FieldAttributeBase
def test_FieldAttributeBase_get_ds():

    # --- Set up test class
    tf = AnsibleTestFramework("FieldAttributeBase")

    # --- Set up test cases

    # default_test
    test1 = tf.get_test( "default_test" )
    result = FieldAttributeBaseTestClass().get_ds()
    test1["pass"] = (result == {"_ds": "default"})

    # fake_ds_test
    test2 = tf.get_test( "fake_ds_test" )
    try:
        result = FieldAttributeBaseTestClass(ds={"_ds":"fake"}).get_ds()
    except AnsibleUndefinedVariable:
        result = False
    test2["pass"] = (result == {"_ds": "_ds"})

    # --- Perform the tests

    tf.run_tests()



# Generated at 2022-06-13 07:56:16.851171
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    my_base = FieldAttributeBase()
    my_base._attributes = {}
    my_base._valid_attrs = {}
    my_base._validated = False
    my_base._loader = None

    # TODO: fix this test after proper implementation of 
    # my_base.get_validated_value()
    return
    try:
        my_base.get_validated_value()
        assert True
    except Exception as e:
        assert False , "unit test for method get_validated_value of class FieldAttributeBase failed - {0}".format(e)

# unit test for method _load_vars of class FieldAttributeBase

# Generated at 2022-06-13 07:56:27.095941
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import UnsafeText
    from ansible.parsing.vault import _get_file_vault_secret
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    from ansible.executor.process.worker import WorkerProcess
    from ansible.executor.task_result import TaskResult
    from ansible.utils.listify import listify

# Generated at 2022-06-13 07:56:36.199836
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    b = BaseObject()
    f = FieldAttributeBase(isa='int', required=True)
    assert f.validate(b, 'attr', 3) == 3
    assert f.validate(b, 'attr', '3') == 3
    assert f.validate(b, 'attr', '3.0') == 3
    assert f.validate(b, 'attr', 3.0) == 3
    b2 = BaseObject()
    f2 = FieldAttributeBase(isa='int', required=True)
    try:
        f2.validate(b2, 'attr', 'foo')
    except AnsibleParserError:
        pass
    else:
        raise AssertionError('AnsibleParserError not raised')


# Generated at 2022-06-13 07:56:37.120675
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    pass



# Generated at 2022-06-13 07:56:41.851002
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    '''
    Test if validate method works as expected
    '''

    # tested class
    class Attribute(FieldAttributeBase):
        pass

    # create object of tested class
    attr = Attribute()

    # check for expected result
    assert attr.validate('string', 'string') == 'string'


# Generated at 2022-06-13 07:56:52.618050
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    class MockBase(Base):
        pass
    # Case 1: self._parent is not None
    base = MockBase()
    base._ds = Mock()
    base._ds._data_source = 'tasks/main.yml'
    base._parent = Mock()
    base._parent.get_dep_chain = Mock(return_value=[Mock()])
    base._parent.get_dep_chain()[0]._role_path = 'roles/role1'
    assert base.get_search_path() == ['roles/role1', 'tasks']
    # Case 2: self._parent is None
    base = MockBase()
    base._ds = Mock()
    base._ds._data_source = 'tasks/main.yml'
    base._parent = None
    assert base.get_search_path()

# Generated at 2022-06-13 07:57:29.714405
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    '''
    Unit test for method FieldAttributeBase.validate()
    '''

    #
    # Initialization
    #

    field_attribute_base_instance = FieldAttributeBase(
        isa='int',
        metadata={
            'description': "Test 'description' metadata",
        },
        validator=lambda obj, attr, value: isinstance(value, int),
        priority=1
    )

    #
    # Run unit test
    #

    field_attribute_base_instance.validate(dict(
        hostname='test_hostname',
        path='/test/path'
    ), 'test_attribute', test_value=1)


# Generated at 2022-06-13 07:57:30.697479
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    assert False

# Generated at 2022-06-13 07:57:35.765062
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    data = dict(hello='world')
    base = FieldAttributeBase(valid_attrs=dict())
    should_be = dict(hello='world')
    obj = base.deserialize(data)
    assert data == should_be, obj

# Generated at 2022-06-13 07:57:40.281734
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    attr = FieldAttributeBase()
    obj = AnsibleBaseYAMLObject()
    value = None
    name = 'test'
    templar = None
        # call the method
    result = obj.get_validated_value(name, attr, value, templar)
    assert result == None


# Generated at 2022-06-13 07:57:47.943468
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    from ansible.vars import VariableManager
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    import ansible.playbook.play
    import ansible.playbook.task
    full_module_name = 'ansible.playbook.play'
    object_name = 'Play'
    __all__ = ['Base', 'BaseVars', 'BaseTask', 'BasePlayContext', 'BasePlay', 'BaseInventory', 'Inventory', 'Playbook', 'PlaybookInventory']

# Generated at 2022-06-13 07:57:52.309295
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    f = Play()
    f.from_attrs({'name': 'test_name'})
    # assert that it worked along
    assert f.name == 'test_name'
    # assert it fails on bad data
    # f.from_attrs({'_ds': {}})
    # assert it fails on bad data
    # f.from_attrs({'_ds': []})
    f.from_attrs({'hosts': 'test_hosts'})
    # assert that it worked along
    assert f.hosts == 'test_hosts'


# Generated at 2022-06-13 07:58:03.298776
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    '''
    Test the get_validated_value method from FieldAttributeBase
    '''
    
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    mock_templar = MagicMock()


# Generated at 2022-06-13 07:58:08.080566
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    # Setup: create an object of type FieldAttributeBase
    obj = FieldAttributeBase()

    # Test: calling from_attrs with args and kwargs that would set
    # an attribute.
    with pytest.raises(NotImplementedError):
        obj.from_attrs(1, 2, 3)



# Generated at 2022-06-13 07:58:11.799541
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    # instantiate class
    # test with fixtures
    post_validate = FieldAttributeBase('post_validate', 'post_validate', 'post_validate', 'post_validate')
    # test method output



# Generated at 2022-06-13 07:58:19.894189
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    from collections import namedtuple

    # If we're not going to test against errors, then what are we doing here?
    #assert False, 'Not implemented'

    # Init a FieldAttributeBase with a name, default and isa
    name = "SomeName"
    default = "SomeDefault"
    isa = "string"
    baseField = FieldAttributeBase(name=name, default=default, isa=isa)

    # Test that an empty string is returned if value is given as an empty string
    value = " "
    templar = "mock"
    result = baseField.get_validated_value(baseField, value, templar)
    assert result == value, 'Empty string is not returned'

    # Test that an int is returned if value is given as an int
    value = 1

# Generated at 2022-06-13 07:58:53.783638
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    pass


# Generated at 2022-06-13 07:59:00.360741
# Unit test for method load_data of class FieldAttributeBase

# Generated at 2022-06-13 07:59:01.911566
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    parm1 = FieldAttributeBase()
    parm2 = FieldAttributeBase()
    assert parm1.copy() == parm2.copy()


# Generated at 2022-06-13 07:59:03.468799
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    attrs = {'name': 'test task'}
    task = Task()
    task.from_attrs(attrs)
    assert getattr(task, 'name') == attrs['name']


# Generated at 2022-06-13 07:59:04.443902
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    result = FieldAttributeBase.copy()
    assert type(result) == MethodType



# Generated at 2022-06-13 07:59:09.077525
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from ansible import errors
    from ansible.executor.task_result import TaskResult
    from ansible.module_utils._text import to_text
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars import DictData
    from ansible.vars import task_vars

    task_vars = {}
    hostvars = {}
    host = 'localhost'
    ds = {}
    templar = Templar(VarsModule(), loader=None, shared_loader_obj=None, variables=task_vars,
                      hostvars=hostvars)
    variables = VariableManager(loader=None, inventory=None, version_info=C.DEFAULT_ANSIBLE_VERSION_INFO_FORMAT)
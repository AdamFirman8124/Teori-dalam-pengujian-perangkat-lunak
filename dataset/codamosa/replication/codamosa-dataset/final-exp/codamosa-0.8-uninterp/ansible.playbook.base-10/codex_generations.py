

# Generated at 2022-06-13 07:50:07.849466
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    # type: () -> None
    # just a quick test of the FieldAttributeBase.dump_attrs() method
    # by writing a fake object we can be sure is fully serializable

    class FakeObject(FieldAttributeBase):
        def __init__(self):
            self._valid_attrs = dict(
                foo=FieldAttribute(isa='str', default='bar'),
                baz=FieldAttribute(isa='int', default=123),
                bam=FieldAttribute(isa='float', default=99.99),
                boo=FieldAttribute(isa='list', default=['1', '2', '3']),
                bar=FieldAttribute(isa='dict', default=dict(a='foo', b='bar')),
                bob=FieldAttribute(isa='bool', default=True),
            )
            super(FakeObject, self).__init__()

# Generated at 2022-06-13 07:50:16.712425
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    '''
    Unit test for method from_attrs of class FieldAttributeBase
    """Returns:
        None"""
    '''
    base = FieldAttributeBase(module=Mock())
    attrs = {u'foo': u'bar', u'baz': u'bak', u'woz': u'wak'}
    base.from_attrs(attrs)
    assert base._attributes['foo'] == u'bar'
    assert base._attributes['baz'] == u'bak'
    assert base._attributes['woz'] == u'wak'


# Generated at 2022-06-13 07:50:22.212952
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    ds = "some_ds"
    pv = mock.MagicMock()
    ta = ansible.module_utils.basic.AnsibleModule._AnsibleModule__TaskAnsibleModule(pv)
    ta.params = {}
    ta.templar = mock.MagicMock()
    f = ansible.parsing.yaml.objects.FieldAttribute(ds=ds)
    f.post_validate(ta)

# Generated at 2022-06-13 07:50:23.266425
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    pass


# Generated at 2022-06-13 07:50:35.121773
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.plugins.loader import get_all_plugin_loaders

    attribute = get_all_plugin_loaders()[0].get('action_plugin', {}).get_loader().get('service')._valid_attrs.get('changed_when')._kwargs
    obj = AnsibleBaseYAMLObject()
    obj._ds = object()
    obj.post_validate = lambda x: None
    obj._valid_attrs = {'test_attr': attribute}

    # Test case #1: isa = 'bool'
    attribute.isa = 'bool'
    attr_value = obj.get_validated_value('test_attr', attribute, 'yes', None)
    assert attr_value == True

    # Test

# Generated at 2022-06-13 07:50:44.320801
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    import yaml

    yaml_data = u"""
---
- name: The task name
  debug:
    var: "this is var"
  notify:
  - Debug
- name: Debug
  debug:
    msg: "this is msg"
  remote_user: jenkins
  become: yes
  become_user: root
  loop: "{{ items }}"
  when:
  - debug.var == 'this is var'
  with_items:
  - this
  - is
  - a
  - list
- name: not_a_task
  debug:
    msg: "this is msg"
  loop: "{{ items }}"
  with_items:
  - this
  - is
  - a
  - list
...
"""

# Generated at 2022-06-13 07:50:47.258516
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():

    # create an instance of the FieldAttributeBase class
    foo = FieldAttributeBase()

    # TODO: test it


# Generated at 2022-06-13 07:51:00.132478
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    # Test with an invalid isa value
    # initialize test object
    fa = FieldAttributeBase()
    with pytest.raises(AnsibleAssertionError) as exec_info:
        setattr(fa, 'isa', 'unknown')
        fa.validate()
    assert 'Unknown isa type: unknown' in to_text(exec_info.value)
    assert exec_info.type == AnsibleAssertionError

    # Test with isa=list and no listof specified
    # initialize test object
    fa = FieldAttributeBase()
    with pytest.raises(AnsibleAssertionError) as exec_info:
        setattr(fa, 'isa', 'list')
        fa.validate()

# Generated at 2022-06-13 07:51:09.165893
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    # create an instance of the class to test
    # initialize with a file for the base class
    obj = FieldAttributeBase(os.path.dirname(__file__) + "/../../../lib/ansible/module_utils/basic.py")
    assert(obj.__class__.__name__ == "FieldAttributeBase")

    # set base class variables that are assumed by post_validate
    obj.loader = DictDataLoader({})
    obj.variable_manager = VariableManager()

    # create an AnsibleTemplate to test templating
    j2_env = Environment(
        loader=DictDataLoader({'A': '42'}),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True
    )

# Generated at 2022-06-13 07:51:14.949148
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from collections import Mapping
    from collections import MutableMapping
    from collections import Mapping
    from collections import MutableMapping
    from collections import Mapping
    from collections import MutableMapping
    from collections import Mapping
    from collections import MutableMapping

    # data
    data = Mapping()
    data = MutableMapping()
    data = Mapping()
    data = MutableMapping()
    data = Mapping()
    data = MutableMapping()
    data = Mapping()
    data = MutableMapping()

    # attr
    attr = Mapping()
    attr = MutableMapping()
    attr = Mapping()
    attr = MutableMapping()
    attr = Mapping()
    attr = MutableMapping()
    attr = Mapping()


# Generated at 2022-06-13 07:52:09.579055
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    obj = FieldAttributeBase(isa='list')
    obj.isa = 'str'
    try:
        obj.validate()
    except ValueError as e:
        assert isinstance(e, ValueError)
    obj.isa = 'list'
    obj.isa = 'str'
    try:
        obj.validate()
    except ValueError as e:
        assert isinstance(e, ValueError)
    obj.isa = 'list'
    obj.isa = 'str'
    try:
        obj.validate()
    except ValueError as e:
        assert isinstance(e, ValueError)
    obj.isa = 'bool'
    obj.isa = 'dict'
    try:
        obj.validate()
    except ValueError as e:
        assert isinstance(e, ValueError)
    obj.isa

# Generated at 2022-06-13 07:52:15.397486
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    x = Base()
    x._parent = None
    x._play._ds = None
    assert x.get_dep_chain() == None
    y = Base()
    y._parent._play._ds._data_source = "C://"
    y._parent._play._ds._line_number = "1"
    assert y.get_dep_chain() == "C://:1"

# Generated at 2022-06-13 07:52:19.745179
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():

    test_data = deepcopy(FieldAttributeBase.FieldAttributeBaseVar)
    # create an instance of FieldAttributeBase
    obj = FieldAttributeBase.FieldAttributeBase(test_data)
    # run method deserialize of FieldAttributeBase with test data
    ret_deserialize = obj.deserialize(test_data["data"])
    assert ret_deserialize == None
    assert obj.attr_name == test_data["attr_name"]
    assert obj.required == test_data["required"]
    assert obj.isa == test_data["isa"]
    assert obj.default == test_data["default"]
    assert obj.static == test_data["static"]
    if 'class_type' in test_data:
        assert obj.class_type == test_data["class_type"]
    else:
        assert obj.class_

# Generated at 2022-06-13 07:52:22.819488
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    # build up a fake task class with a fake dep chain of three roles
    class my_task(Base):
        def get_dep_chain(self):
            chain = []
            for i in range(3):
                chain.append(Base())
            chain.append(self._parent)
            return chain
    t = my_task()
    t._parent = Base()
    assert len(t.get_dep_chain()) == 4
    

# Generated at 2022-06-13 07:52:26.565723
# Unit test for method get_ds of class FieldAttributeBase
def test_FieldAttributeBase_get_ds():

    def setUpModule():
        global datastore

        datastore = DataStore()
        datastore.set_variable('one', 'two')
        datastore.set_variable('three', 'four')

    def tearDownModule():
        pass



# Generated at 2022-06-13 07:52:34.815260
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from ansiblelint.rules.AnsibleLintRule import AnsibleLintRule

    class RuleA(AnsibleLintRule):
        id = 'ANSIBLE0001'
        shortdesc = 'shortdesc'
        description = 'description'
        tags = ['tag']

    assert RuleA()._attributes['tags'] == FieldAttributeBase(
        'tags',
        field_type='list',
        required=True,
        listof=string_types,
        default=[])
    assert RuleA()._attributes['tags'] == FieldAttributeBase(
        'tags',
        field_type='list',
        required=True,
        listof=string_types,
        default=[])
    assert RuleA()._attributes['tags'].name == 'tags'
    assert RuleA()._attributes['tags'].field_

# Generated at 2022-06-13 07:52:40.158375
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

# Generated at 2022-06-13 07:52:41.284839
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    # unit test init
    # FieldAttributeBase.squash() called with no simplejson
    pass

# Generated at 2022-06-13 07:52:45.863730
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    def check_FieldAttributeBase_validate(arg1, expected, test_name):
        with pytest.raises(AnsibleParserError) as excinfo:
            arg1.validate()
        assert 'required' in to_text(excinfo.value)
        assert 'required' in excinfo.value.message
    test_cases = [
        # arg1 value is always the same.
        (FieldAttribute('test_name'), True, 'test_name'),
    ]
    for arg1, expected, test_name in test_cases:
        yield check_FieldAttributeBase_validate, arg1, expected, test_name



# Generated at 2022-06-13 07:52:52.785657
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
  # Initializing the object
  attr = FieldAttributeBase()
  for x in range(0,10):
    name = sys_random.randint(0,10)
    value = sys_random.randint(0,10)
    attribute = sys_random.randint(0,10)
    templar = sys_random.randint(0,10)
    return_val = attr.get_validated_value(name, attribute, value, templar)
    if(return_val == None):
      raise AssertionError('Expected '+str(return_val)+' to be a string')

# Generated at 2022-06-13 07:53:33.311432
# Unit test for method get_ds of class FieldAttributeBase
def test_FieldAttributeBase_get_ds():

    # Create a mock object which will be passed in
    # as the 'obj' parameter.
    #
    # The below code is adapted from:
    # https://docs.python.org/dev/library/unittest.mock.html#unittest.mock.Mock.return_value
    #
    class _MockResponse(object):
        def __init__(self, ds):
            self.ds = ds

    mock_response = _MockResponse(ds={"name": "bar", "enabled": False})

    # Create a mock object for the attribute 'obj' of the class FieldAttributeBase.
    #
    # The below code is adapted from:
    # https://docs.python.org/dev/library/unittest.mock.html#unittest.mock.PropertyMock
    #


# Generated at 2022-06-13 07:53:40.385961
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    # Initialize the class
    obj = FieldAttributeBase(name='foo', private=True, isa='string', required=True, default=None, static=True)

    # Test the method
    assert isinstance(obj.validate, types.MethodType)

    # Test the FieldAttributeBase class
    assert obj._name == 'foo'
    assert obj._private is True
    assert obj._isa == 'string'
    assert obj._required is True
    assert obj._default is None
    assert obj._static is True



# Generated at 2022-06-13 07:53:51.905833
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    x = None
    y = None
    z = None

    # Used for testing if class is:
    # FieldAttributeBase
    #
    # For the following test x, y and z need to be assigned
    # values that represent string, int, float, bool, percent,
    # list and dict types respectively
    #

    #
    # TEST CASE: FieldAttributeBase.get_validated_value
    #
    # INPUTS:
    # x: a string
    # y: an int
    # z: a float
    #
    # EXPECTED RESULT:
    # The expected output is that the given values are
    # returned in the correct expected format
    #

    # See the following for the implementation used for this test
    # https://github.com/ansible/ansible/blob/devel/lib/ans

# Generated at 2022-06-13 07:53:54.281654
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    '''
    Test the deserialize method of FieldAttributeBase
    '''

    fieldattrib = ansible.module_utils.basic.FieldAttributeBase()
    # TODO: add some tests here
    assert False



# Generated at 2022-06-13 07:54:00.427628
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    '''
    This test ensures the behaviour of method dump_me() of class FieldAttributeBase is correct
    '''
    o = FieldAttributeBase()
    o.name = 'somename'
    o.default = 'somedefault'
    o.required = True
    o.description = 'Some description'
    o.version_added = (1, 2, 3)
    o.version_removed = (4, 5, 6)
    assert isinstance(o.dump_me(), dict)

# Generated at 2022-06-13 07:54:10.733905
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    import mock
    
    obj = mock.Mock()
    name = mock.Mock()
    value = mock.Mock()
    templar = mock.Mock()
    
    # 1st test without assertion
    try:
        FieldAttributeBase().validate(obj, name, value, templar)
    except:
        fail("FieldAttributeBase().validate() threw an exception unexpectedly!")
    
    # 2nd test with assertion
    try:
        FieldAttributeBase().validate(obj, name, value, templar)
    except:
        pass
    else:
        fail("FieldAttributeBase().validate() failed to throw an exception as expected!")

# Generated at 2022-06-13 07:54:20.916162
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    '''
    Unit test for FieldAttributeBase.from_attrs()
    '''
    class Task(FieldAttributeBase):
        _valid_attrs = dict(
            _test_attr1 = FieldAttribute(isa='int', default=10),
            _test_attr2 = FieldAttribute(isa='int', default=20),
            _test_attr3 = FieldAttribute(isa='str', default='test'),
        )
    obj = Task()
    attrs = dict(
        _test_attr1 = 100,
        _test_attr2 = 200,
        _test_attr3 = 'testing',
    )
    obj.from_attrs(attrs)
    assert obj._test_attr1 == 100
    assert obj._test_attr2 == 200
    assert obj._test_attr3 == 'testing'

# Generated at 2022-06-13 07:54:23.689967
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    # FieldAttributeBase.dump_me()
    # test for the 'dump_me' method of FieldAttributeBase
    pass


# Generated at 2022-06-13 07:54:27.312378
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    dst = dict(name="test_task", action="test_action", become=True)
    task = Task()
    task.load_data(dst)
    assert task.dump_attrs() == dst


# Generated at 2022-06-13 07:54:30.404890
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    # create random instance of class FieldAttributeBase
    a = FieldAttributeBase()
    
    # read attribute values
    
    # call dump_attrs of instance a
    dump_attrs = a.dump_attrs()
    assert dump_attrs is not None

# Generated at 2022-06-13 07:55:50.595227
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    '''
    Unit test for method load_data of class FieldAttributeBase
    '''
    arg1 = {'class': 'FieldAttributeBase', 'attributes': ''}
    arg2 = {'class': 'FieldAttributeBase', 'attributes': ''}
    t = FieldAttributeBase()
    # This is not an easy test to write, so I will skip it for now
    # The code only raises an exception, so we don't really have something to test against
    # TODO: Write a more complete test
    #t.load_data(arg1, arg2)

# Generated at 2022-06-13 07:56:01.025277
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
  # Valid types of arguments (and some invalid ones):
  valid_types = ['string', 'int', 'float', 'bool', 'percent', 'list', 'set', 'dict', 'class']

  # Some invalid args.
  invalid_args = [None, 'foo']

  for type_ in valid_types:
    for attr in [None, {}, {'required': True}, {'default': 'test'}]:
      t = FieldAttribute(type_, attr)

      # Test post_validate() with valid value.
      try:
        t.post_validate(None, 'test')
      except TypeError as e:
        raise AssertionError("Post-validation failed for valid value and valid attr.")

      # Test post_validate() with invalid value.

# Generated at 2022-06-13 07:56:04.898099
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.utils._text import to_text
    from ansible.template import Templar

# Generated at 2022-06-13 07:56:11.393629
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    """
    Test post_validate
    """
    ansible_stub = StubAnsibleModule()
    ansible_stub.Connection = StubConnection
    ansible_stub.to_text = stub_to_text
    ansible_stub.to_bytes = stub_to_bytes

    module = StubModule()
    templar = Templar(loader=ansible_stub.loader)
    obj = FieldAttributeBase()
    obj.post_validate(templar)
    assert isinstance(obj, FieldAttributeBase)


# Generated at 2022-06-13 07:56:17.971970
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    assert True

    # test Base.get_search_path()
    # Base:  play -> role1 -> role2 -> role3
    play = Play()
    assert play.get_search_path() == []

    role2 = RoleInclude()
    role1 = RoleInclude()
    role1._parent = play
    role2._parent = role1
    play._role_path = '/path/to/play/'
    role1._role_path = '/path/to/play/role1/'
    role2._role_path = '/path/to/play/role2/'
    assert play.get_search_path() == ['/path/to/play/', '/path/to/play/role1/']

# Generated at 2022-06-13 07:56:23.182376
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from ansible import errors
    from ansible.compat import text_type
    from ansible.errors import AnsibleError
    from ansible.errors import AnsibleParserError
    from ansible.executor.task_result import TaskResult
    from ansible.parsing.plugin_docs import read_docstring
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.playbook.attribute import FieldAttribute
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars import combine_vars
    from ansible.utils.display import Display
    from ansible.utils.hashing import checksum_s

# Generated at 2022-06-13 07:56:27.770681
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    field_attribute_base = FieldAttributeBase()

    assert field_attribute_base.validate(None) == None
    assert field_attribute_base.validate('1') == '1'
    assert field_attribute_base.validate(1) == 1
    assert field_attribute_base.validate(1.0) == 1.0



# Generated at 2022-06-13 07:56:37.136594
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    FAKE_LOADER = DictDataLoader({
        'tests/ansible/hosts': """
            [all]
            localhost
        """,

    })

    FAKE_VARS_MANAGER = mock.Mock()
    FAKE_VARS_MANAGER.get_vars = mock.Mock(return_value=[])
    FAKE_VARS_MANAGER.get_host_vars = lambda x: [data.Variable(host='localhost', set_host_var=True, hash_name=x)]

    FAKE_INVENTORY = Inventory(loader=FAKE_LOADER, variable_manager=FAKE_VARS_MANAGER, host_list='tests/ansible/hosts')
    FAKE_PLAYBOOK = Playbook()
    FAKE_PLAY = Play()

    FAKE

# Generated at 2022-06-13 07:56:42.796820
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    # initialized the instance
    load_data_instance1 = FieldAttributeBase('name')
    # setup the test variables
    name = 'name'
    ds = {'name': 'value'}
    attr_class = True
    # run the method with test variables
    result1 = load_data_instance1.load_data(name, ds, attr_class)
    assert result1 is None


# Generated at 2022-06-13 07:56:47.397828
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    """Unit test for post_validate of class FieldAttributeBase"""
    obj = FieldAttributeBase()
    args = dict()
    kwargs = dict()
    # No exception should be raised
    type(obj).post_validate(obj, args, kwargs)

# Generated at 2022-06-13 07:57:23.601422
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    '''
    Unit test for method from_attrs of class FieldAttributeBase
    '''
    obj = FieldAttributeBase()
    assert obj.from_attrs(None) is None

# Generated at 2022-06-13 07:57:30.335725
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    # First test the squash method of the base class.
    # Set up the method call arguments
    # This is a test
    base = FieldAttributeBase(None)
    is_squashed = None
    parent = None

    # Test the method and ensure that all arguments were called properly
    x = base.squash(is_squashed, parent)
    

# Generated at 2022-06-13 07:57:41.812521
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    task = Task()
    assert task.get_search_path() == ['.']
    task._ds._data_source = 'a.yml'
    task._parent = Base()
    task._parent._play = Base()
    task._parent._play._ds._data_source = 'b.yml'
    task._parent._play._parent = Base()
    task._parent._play._parent._role_path = './roles/foo'
    task._parent._play._parent._play = Base()
    task._parent._play._parent._play._ds._data_source = 'c.yml'
    task._parent._play._parent._play._parent = Base()
    task._parent._play._parent._play._parent._role_path = './roles/bar'

# Generated at 2022-06-13 07:57:51.075478
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    '''
    Unit test for method from_attrs of class FieldAttributeBase
    '''
    test_object = FieldAttributeBase()
    attrs = dict()
    # test with empty attrs
    test_object.from_attrs(attrs)

    # test with attrs with value
    test_object = FieldAttributeBase()
    test_object.name = "test_name"
    attrs = {"name":"test_name"}
    test_object.from_attrs(attrs)
    assert test_object.name == attrs["name"]
    # Test with attrs with value and a class object

    test_object = FieldAttributeBase()
    test_object.name = "test_name"
    attrs = {"name":"test_name"}
    test_object.from_attrs(attrs)
    assert test

# Generated at 2022-06-13 07:57:58.405999
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    for param in [{}, {'class_type': None, 'required': None, 'default': None, 'priority': None}]:
        with pytest.raises(TypeError) as error:
            FieldAttributeBase(**param)
        assert error.type == TypeError
        assert "__init__()" in error.value.args[0] and "takes" in error.value.args[0] and "arguments" in error.value.args[0]

    assert FieldAttributeBase(class_type=None, required=None, default=None, priority=None).__class__ == FieldAttributeBase


# Generated at 2022-06-13 07:58:02.217752
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
  obj = FieldAttributeBase()
  # Droups from yaml
  y = '''---
'''
  if y != obj.dump_me(): raise Exception('Test failed')


# Generated at 2022-06-13 07:58:12.704487
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    # This function is not executed, it's only here to provide data for the
    # autodoc generation
    from ansible.module_utils import basic
    module = basic.AnsibleModule(argument_spec={})
    module_result = dict(
        msg=None
    )

    module.exit_json = lambda **kwargs: module_result.update(kwargs)

    # create an object of class FieldAttributeBase for test
    test_obj = FieldAttributeBase()

    # test with the following attributes
    attribute = dict(
        isa='string'
    )
    name = 'test'
    templar = module.templar

    # execute the get_validated_value method
    result = test_obj.get_validated_value(name, attribute, "test", templar)

    # compare the result


# Generated at 2022-06-13 07:58:14.832019
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    # the class
    post_validate = FieldAttributeBase.post_validate

    # No tests for this method
    assert True is True



# Generated at 2022-06-13 07:58:18.909903
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    attr = FieldAttributeBase('test_field')
    assert attr.name == 'test_field'
    assert attr.required is False
    assert attr.default is None
    assert attr.static is False
    assert attr.always_post_validate is False
    assert attr.class_type is None
    assert attr.listof is None
    assert attr.isa == 'string'


# Generated at 2022-06-13 07:58:26.725670
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():

    # Test with a empty dictionary
    test_data = dict()
    assert FieldAttributeBase.squash(test_data) == dict()

    # Test with a dictionary of with only first level key-value pair
    # and value is list 
    test_data = dict(
        first_level_list=list([1,2,3])
    )
    assert FieldAttributeBase.squash(test_data) == test_data

    # Test with a dictionary of with only first level key-value pair
    # and value is dict
    test_data = dict(
        first_level_dict=dict(key1='value1', key2=dict(key3='value3', key4=['value4']))
    )
    assert FieldAttributeBase.squash(test_data) == test_data

    # Test with a dictionary of with only first
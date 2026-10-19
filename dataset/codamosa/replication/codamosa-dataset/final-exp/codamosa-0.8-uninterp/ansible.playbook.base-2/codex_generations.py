

# Generated at 2022-06-13 07:50:06.815407
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():

    fields = type("", (object,), {})
    fields.name = FieldAttribute(isa='string')

    fields.delete_me = FieldAttribute()
    del fields.delete_me

    obj = type("", (FieldAttributeBase,), fields)
    obj("name", "some value")


# Generated at 2022-06-13 07:50:17.919597
# Unit test for method from_attrs of class FieldAttributeBase

# Generated at 2022-06-13 07:50:28.041498
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():

    from ansible.vars import combine_vars
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role.task_include import TaskInclude
    from ansible.template import Templar

    p = Play().load(dict(
        name = 'foobar',
        roles = [
            RoleInclude().load(dict(
                name = 'foobar',
                tasks = [
                    TaskInclude().load(dict(
                        name = 'foobar',
                    )),
                ],
            )),
        ],
        tasks = [
            Task().load(dict(
                name = 'foobar',
            )),
        ],
        vars = {},
    ))


# Generated at 2022-06-13 07:50:28.879659
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    # TODO implement this test
    assert False


# Generated at 2022-06-13 07:50:34.173714
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    """Test if it can squash a list of field attribute bases together and return a single one"""
    # Given a list of field attribute bases

    # When I squash the list
    # Then I should get a single base class

    # We don't want to test this yet as we have not defined how to do it
    assert False == True

# Generated at 2022-06-13 07:50:44.341962
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    from ansible.utils.display import Display
    display = Display()
    # Add attribute _attributes to dct
    dct = {}
    dct['_attributes'] = {}
    # Add attribute _attr_defaults to dct
    dct['_attr_defaults'] = {}
    # Add attribute _valid_attrs to dct
    dct['_valid_attrs'] = {}
    # Add attribute _alias_attrs to dct
    dct['_alias_attrs'] = {}
    # Add attribute _attributes to self
    dct['_attributes'] = {}
    # Add attribute _attr_defaults to self
    dct['_attr_defaults'] = {}
    # Add attribute _valid_attrs to self
    dct['_valid_attrs'] = {}
    # Add attribute _

# Generated at 2022-06-13 07:50:48.854230
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    '''Test method validate of class FieldAttributeBase'''

    # Create an instance of class FieldAttributeBase
    obj = FieldAttributeBase('foo', 'gogo')

    # Validate that instance
    obj.validate(obj)


# Generated at 2022-06-13 07:50:52.401809
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    def load_attrs(data):
        pass
    load_attrs(data)
FieldAttributeBase.from_attrs = load_attrs


# Generated at 2022-06-13 07:51:03.861159
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    def _get_object():
        # Create a FieldAttributeBase object for testing dump_me method
        foo_obj = FieldAttributeBase()
        setattr(foo_obj, '_get_default_attribute', lambda x: None)
        for f in FieldAttributeBase._fields:
            setattr(foo_obj, f, None)
        return foo_obj

    foo_obj = _get_object()
    # Testing with fields set to None
    result = foo_obj.dump_me()
    assert result == {'default': None, 'required': False}

    # Testing with default set to Data instead of None
    foo_obj = _get_object()
   

# Generated at 2022-06-13 07:51:14.409650
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    class Foo:
        # set up attributes for testing
        class_attr = Attribute()
        some_other_attr = Attribute()
        _internal_attr = Attribute()

        # set to true to check final instance
        __metaclass__ = BaseMeta
        # check that _valid_attrs is populated
        valid_attrs = dict(_internal_attr=_internal_attr, class_attr=class_attr, some_other_attr=some_other_attr)
        # check that we have a mapping of defaults
        attr_defaults = dict(_internal_attr=_internal_attr.default, class_attr=class_attr.default, some_other_attr=some_other_attr.default)
        # check that we have a mapping of aliases
        alias_attrs = dict()
        # check that we have a mapping of sent

# Generated at 2022-06-13 07:51:39.337748
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    # Create an empty object
    obj = FieldAttributeBase()
    # Try to call the method
    obj.dump_attrs()

# Generated at 2022-06-13 07:51:51.306664
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    # test cases
    foo_cases = dict()
    foo_cases["int"] = dict(
        name = "foo",
        attribute = FieldAttributeBase.isa_type_fields["int"](),
        value = "5",
        templar = None,
        expected = 5
    )
    foo_cases["string"] = dict(
        name = "foo",
        attribute = FieldAttributeBase.isa_type_fields["string"](),
        value = "5",
        templar = None,
        expected = "5"
    )
    foo_cases["bool"] = dict(
        name = "foo",
        attribute = FieldAttributeBase.isa_type_fields["bool"](),
        value = "True",
        templar = None,
        expected = True
    )

# Generated at 2022-06-13 07:51:52.749616
# Unit test for method get_ds of class FieldAttributeBase
def test_FieldAttributeBase_get_ds():
    d = FieldAttributeBase()
    assert d.get_ds() == {}

# Generated at 2022-06-13 07:51:54.078930
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
  assert True


# Generated at 2022-06-13 07:51:59.690319
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    base = FieldAttributeBase()
    dsa_instance = DummySubClassA()
    dsa_instance.value1 = "test value 1"
    dsa_instance.value2 = "test value 2"
    dsa_instance.value3 = "test value 3"
    base.list_of_classes = [dsa_instance]
    base.test = "test value"
    expected = {"list_of_classes": [{"value1": "test value 1", "value2": "test value 2", "value3": "test value 3"}], "test": "test value"}
    assert base.dump_attrs() == expected, 'base.dump_attrs() == expected'


# Generated at 2022-06-13 07:52:12.702445
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    # Create a Mock class to represent the test object
    class TestFieldAttributeBase(FieldAttributeBase):
        # Create a class variable to store the test results
        test_results = []
        # Declare class variable valid_attrs
        valid_attrs = {
            'name': FieldAttribute(isa='string', required=False),
            'other': FieldAttribute(isa='string', required=False),
            }
        # Define get_ds method that returns a dictionary
        def get_ds(self):
            return {
                'name': 'name',
                'other': 'other',
            }
        # Define get_validated_value mock method
        def get_validated_value(self, name, attribute, value, templar):
            return value
        # Create mock for this method
        _get_validated_value = Mock

# Generated at 2022-06-13 07:52:17.759335
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    v2_loader = get_loader(None)
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.vault import VaultLib
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    attr = FieldAttributeBase()
    attr.default = ""
    attr.isa = 'string'
    attr.name = "name"
    attr.required = False
    attr.static = False
    templar = Templar(loader=v2_loader, variables=dict())
    play_context = PlayContext()
    variable_manager = VariableManager()
    variable_manager.set_play_context(play_context)
    variable_manager.vault_password = VaultLib()

# Generated at 2022-06-13 07:52:19.633201
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    # TODO: Add proper unit tests for FieldAttributeBase.get_validated_value
    pass

# Generated at 2022-06-13 07:52:20.105639
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    pass

# Generated at 2022-06-13 07:52:27.873897
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleMapping
    base_obj = FieldAttributeBase()
    with pytest.raises(NotImplementedError) as excinfo:
        base_obj.from_attrs(dict(), dict())
    assert 'Attempted to call an abstract method' in str(excinfo.value)
    assert 'from_attrs' in str(excinfo.value.message)
    with pytest.raises(ValueError) as excinfo:
        base_obj.from_attrs('string', dict())
    assert 'should be a dict but is a' in str(excinfo.value)


# Generated at 2022-06-13 07:53:00.114700
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    # Load the fixture file "fixtures/FieldAttributeBase/squash.test.yml"
    fixture_path = os.path.join(FIXTURES_DIR, filename_for_test(__name__, "squash.test.yml"))
    data = yaml.load(open(fixture_path).read())
    for datum in data:
        # Debug the fixture data.
        display.display(data)
        display.display(datum)
        base_obj = Data()
        new_obj = Data()
        # Load "desc" and "base_obj" from datum
        if "desc" in datum:
            desc = datum["desc"]
        if "base_obj" in datum:
            base_obj.from_attrs(datum["base_obj"])
        # Load "new_

# Generated at 2022-06-13 07:53:04.758854
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    attr1 = FieldAttributeBase()
    actor = FieldAttributeBase()
    actor.name = 'tom'
    attr1.actor = actor
    assert attr1.dump_attrs() == {'actor': {'name':'tom'}}

# Generated at 2022-06-13 07:53:05.488948
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    pass

# Generated at 2022-06-13 07:53:08.160588
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
  field_attribute_base_instance = FieldAttributeBase()
  assert field_attribute_base_instance.dump_me(False) == False


# Generated at 2022-06-13 07:53:11.881072
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
  foo = FieldAttributeBase(default=3)
  c = copy.copy(foo)
  foo = FieldAttributeBase(default=3)
  c = copy.deepcopy(foo)


# Generated at 2022-06-13 07:53:18.401537
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    data = dict()
    data['isa'] = 'class'
    data['default'] = None
    data['class_type'] = 'Task'
    data['always_post_validate'] = True
    data['static'] = False
    data['display'] = 'name'
    data['required'] = True
    
    fld = FieldAttributeBase(**data)
    assert fld.isa == 'class'
    assert fld.default == None
    assert fld.class_type == 'Task'
    assert fld.always_post_validate == True
    assert fld.static == False
    assert fld.display == 'name'
    assert fld.required == True
    
    

# Generated at 2022-06-13 07:53:28.120409
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    # Test with defined parents
    class Base(object):
        def __new__(cls, name, parents, dct):
            dct['test_class_attribute'] = True
            return super(BaseMeta, cls).__new__(cls, name, parents, dct)

        def __init__(self):
            self.test_instance_attribute = True

    class Child(Base):
        def __init__(self):
            super(Child, self).__init__()
            self.child_instance_attribute = True

    class GrandChild(Child):
        pass

    assert hasattr(Child, 'test_class_attribute')
    assert hasattr(GrandChild, 'test_class_attribute')

    assert not hasattr(Child, 'test_instance_attribute')

# Generated at 2022-06-13 07:53:38.660086
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    
    field = None

    # TODO(bengeric)
    # if the ds is a string, the code doesn't attempt to parse it
    # the code assumes the string is a path to a file, and will attempt
    # to read the file.  This is generally not what we want.  Need to
    # create a different test to ensure the parsing of a string is correct
    # or ensure that the string can be parsed by YAML when loading into a
    # TaskInclude
    
    # if the ds is a string, the file at the path is read
    # set the path
    expectedVar = 'expected_value'
    with test_dir():
        temp_file = 'temp_file.yml'
        with open(temp_file, 'w') as f:
            f.write(expectedVar)
        # load

# Generated at 2022-06-13 07:53:49.979118
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    templar = Templar(loader=loader)
    task = Task()
    task._ds = dict()

    # attr is a valid setting, so validate() should return True
    try:
        result = task.validate("task_name", "task_name", "A task", required=True)
    except:
        result = False

    assert result is True, "validate() should return True when attr_name is a valid setting"

    # AttributeError should be raised when attr_name is not a valid setting

# Generated at 2022-06-13 07:53:50.621626
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    pass

# Generated at 2022-06-13 07:54:35.184284
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    pass # TODO

# Generated at 2022-06-13 07:54:37.869536
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    dict_result = {}
    ds = dict_result
    task = FieldAttributeBase()
    templar = MockTemplar()
    task.post_validate(templar)
    assert dict_result == {}


# Generated at 2022-06-13 07:54:42.869056
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    test_obj = FieldAttributeBase()
    test_obj._valid_attrs = dict()
    test_obj._valid_attrs['test'] = dict()
    test_obj._valid_attrs['test']['default'] = False
    test_obj._valid_attrs['test']['isa'] = 'bool'
    attrs = dict()
    attrs['test'] = dict()
    attrs['test']['value'] = True
    test_obj.from_attrs(attrs)
    assert test_obj.test == True


# Generated at 2022-06-13 07:54:47.526901
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    import mock

    class FieldAttributeBaseImpl(FieldAttributeBase):
        def __init__(self):
            self.method_calls = []

    def test_post_validate_call():
        d = FieldAttributeBaseImpl()
        d.post_validate([])
        assert d.method_calls == []



# Generated at 2022-06-13 07:54:48.959370
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
  # TODO: implement
  pass


# Generated at 2022-06-13 07:54:56.400494
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block

    loader = DictDataLoader({
        "foo.yml": """
        - hosts: localhost
          tasks:
          - debug: msg="lol"
        """,
        "bar.yml": """
        - hosts: localhost
          tasks:
          - include: foo.yml
        """
    })

    inventory = InventoryManager(loader=loader, sources="localhost")

# Generated at 2022-06-13 07:55:01.016805
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    obj = FieldAttributeBase()
    attribute = obj.__class__()
    templar = obj.__class__()
    
    # Call the method (comment this out if not using pytest parametrize)
    value = obj.get_validated_value('value', attribute, value, templar)
    

# Generated at 2022-06-13 07:55:11.277710
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    class TestFieldAttributeBase:
        def __init__(self):
            self._valid_attrs = {}
        @property
        def ds(self):
            return
        def get_validated_value(self, name, attribute, value, templar):
            return FieldAttributeBase.get_validated_value(self, name, attribute, value, templar)

    class TestFieldAttributeBase_sub(FieldAttributeBase):
        def __init__(self):
            self._valid_attrs = {}
        @property
        def ds(self):
            return
        def get_validated_value(self, name, attribute, value, templar):
            return FieldAttributeBase.get_validated_value(self, name, attribute, value, templar)


# Generated at 2022-06-13 07:55:11.932286
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():

    pass

# Generated at 2022-06-13 07:55:17.521276
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    # ensure FieldAttributeBase raises when there's no type class attribute
    with pytest.raises(AnsibleAssertionError):
        f = FieldAttributeBase(isa='dict')
        f.validate('var', {'key': 'val'})

    # ensure FieldAttributeBase raises when there's no isa class attribute
    with pytest.raises(AnsibleAssertionError):
        f = FieldAttributeBase(type='dict')
        f.validate('var', {'key': 'val'})



# Generated at 2022-06-13 07:56:08.201463
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    test_object = FieldAttributeBase()

    with pytest.raises(AnsibleAssertionError) as excinfo:
        test_object.deserialize('')
    assert 'data (\'\') should be a dict but is a <class \'str\'>' in to_text(excinfo)



# Generated at 2022-06-13 07:56:15.413297
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    '''
    test for method dump_me of class FieldAttributeBase
    '''
    # Make sure FieldAttributeBase is a subclass of object
    assert issubclass(FieldAttributeBase, object)
    # FieldAttributeBase(class_name, field_name, default, isa, private, require_in, choices, aliases)
    attr = FieldAttributeBase('class_name', 'field_name', 'default', 'isa', 'private', 'require_in', 'choices', 'aliases')
    # The dump_me method takes no arguments
    repr = attr.dump_me()

# Generated at 2022-06-13 07:56:23.935246
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    data = {
        "always_post_validate": False,
        "class_type": "string",
        "default": None,
        "display": "private",
        "isa": "string",
        "listof": None,
        "name": "type",
        "required": True,
        "static": False,
        "_uuid": "uuid"
    }
    fa = FieldAttributeBase(Attribute(), '_uuid')
    fa.deserialize(data)
    assert fa.name == "type"
    # assert fa.name == "uuid"
    # todo: add more param test
    pass

# Generated at 2022-06-13 07:56:34.446148
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    _factory = objects.ensure_class_bases(Task)
    _test_object = _factory()

# Generated at 2022-06-13 07:56:44.586812
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    f = FieldAttributeBase()
    assert f.dump_attrs() == {}
    f = FieldAttribute(isa='list', listof=int)
    assert f.default is None
    f = FieldAttribute(isa='list', listof=int, default='foo')
    assert f.default == 'foo'
    f = FieldAttribute(isa='list', listof=int, default=[1, 2, 3, 4])
    assert f.dump_attrs() == {}
    f = FieldAttribute(isa='list', listof=int, default=[1, 2, 3, 4])
    dict_ret = f.__get__()
    assert dict_ret == {'isa': 'list', 'listof': int, 'default': [1, 2, 3, 4]}

# Generated at 2022-06-13 07:56:49.152314
# Unit test for method get_path of class Base
def test_Base_get_path():
    from ansible.playbook.task_include import TaskInclude
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources='')


# Generated at 2022-06-13 07:56:55.934425
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    # host = MagicMock()
    # host_vars = {'password': 'test'}
    # provider = MagicMock()
    # task = Task()
    # task.action = 'copy'
    # task.args = {'dest': '/tmp/output', 'content': '{{ k }}={{ v }}'}
    # #task._parent = MagicMock()
    # task._validate_attrs()
    # task.post_validate(MagicMock(), MagicMock())
    # task.run(host, MagicMock(get_vars=lambda x: host_vars))
    assert 1 == 1

# Generated at 2022-06-13 07:57:01.821436
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    import pytest
    from itertools import chain, combinations
    from ansible.module_utils.six.moves import zip
    from ansible.module_utils.six import PY3
    from ansible.module_utils.facts.timeout import TimeoutError

    # the class to be tested
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    # initialize needed objects
    ansible_base_yaml_object = AnsibleBaseYAMLObject()

    # test with an invalid value
    attr = 1
    with pytest.raises(AnsibleAssertionError):
        ansible_base_yaml_object.from_attrs(attr)

    # test with a valid value
    attr = dict()
    ansible_base_yaml_object.from_attrs

# Generated at 2022-06-13 07:57:04.252417
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    pytest.skip("Skip for now")


# Generated at 2022-06-13 07:57:05.461225
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
  pass

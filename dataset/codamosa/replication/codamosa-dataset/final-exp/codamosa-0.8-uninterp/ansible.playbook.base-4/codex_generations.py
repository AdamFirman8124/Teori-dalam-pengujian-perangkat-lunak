

# Generated at 2022-06-13 07:50:01.815828
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    pass


# Generated at 2022-06-13 07:50:12.602686
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    def get_dep_chain(self):
        if hasattr(self, '_parent') and self._parent:
            return self._parent.get_dep_chain()
        else:
            return None
    Base.get_dep_chain = get_dep_chain

    #
    # Test get_dep_chain
    #

# Generated at 2022-06-13 07:50:14.157731
# Unit test for method get_ds of class FieldAttributeBase
def test_FieldAttributeBase_get_ds():
    obj = FieldAttributeBase()
    print(obj.get_ds())


# Generated at 2022-06-13 07:50:22.884092
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    from ansible.parsing.vault import VaultLib

    variable_manager = mock.MagicMock()
    loader = mock.MagicMock()
    vault_secrets = [{'secret': 'secret1', 'secret_type': 'password'}, {'secret': 'secret2', 'secret_type': 'ssh_key', 
        'secret_passphrase': 'passphrase'}]
    vault_secrets_type = 'dict'
    vault_secrets_mapping = {}
    vault_password = 'vault_password'
    vault_prompt = False
    vault_identities = ['identity1', 'identity2']

# Generated at 2022-06-13 07:50:26.218988
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    # test empty definition
    attr = FieldAttributeBase()
    assert attr.dump_me() == '', 'dump_me returned a string other than ""'


# Generated at 2022-06-13 07:50:37.555874
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    base = FieldAttributeBase()
    play = Play()
    play.vars = dict(a=1, b=2)
    play.post_validate(Templar(VariableManager(), loader=DataLoader()))
    # FIXME: this test currently fails with TypeError, as we are not loading a
    # playbook
    # play.load_vars(base.vars, Attribute.VARS, play.vars, play.vars)

# Generated at 2022-06-13 07:50:38.352636
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    pass

# Generated at 2022-06-13 07:50:39.415992
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    assert not False

# Generated at 2022-06-13 07:50:43.904213
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    task = Task()

    setattr(task, '_finalized', True)
    for name in task._valid_attrs.keys():
        setattr(task, name, None)
    task.post_validate(templar=None)


# Generated at 2022-06-13 07:50:45.164110
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    assert_raises(NotImplementedError,Base().get_dep_chain)
    
    

# Generated at 2022-06-13 07:51:13.607329
# Unit test for method get_path of class Base
def test_Base_get_path():
    b = Base()
    b._ds._data_source = "abc.txt"
    b._ds._line_number = 200
    result = b.get_path()
    assert result == "abc.txt:200"

# Generated at 2022-06-13 07:51:21.084690
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    host = FakeHost()
    uuid = AnsibleUnicode('asdf')
    task = FakeTask()
    task.deserialize({'name': uuid, '_uuid': uuid, 'host': host, '_variable_manager': host, '_loader': host})
    assert uuid == task.name
    assert uuid == task._uuid
    assert host == task.host
    assert host == task._variable_manager
    assert host == task._loader


# Generated at 2022-06-13 07:51:26.081023
# Unit test for method get_path of class Base
def test_Base_get_path():
    Playbook = collections.namedtuple("Playbook", ["path"])
    Role = collections.namedtuple("Role", ["path"])
    Task = collections.namedtuple("Task", ["path"])

    play_path = "play.yml"
    role_path = "roles/role1/tasks/task.yml"
    task_path = "site.yml:9"

    # test for playbook object
    playground = Playbook(path=play_path)
    assert Base().get_path(playground) == play_path

    # test for role object
    playground = Role(path=role_path)
    assert Base().get_path(playground) == role_path

    # test for task object
    playground = Task(path=task_path)

# Generated at 2022-06-13 07:51:28.936646
# Unit test for method get_path of class Base
def test_Base_get_path():
    play = Play()
    ds = DataLoader().load_from_file('tests/support/test-copy.yaml')
    play.deserialize(ds[0])
    play.post_validate(templar=MockTemplar())
    assert play.get_path() == 'tests/support/test-copy.yaml:5'


# Generated at 2022-06-13 07:51:32.056074
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    """
    Test dump_me method of FieldAttributeBase
    """
    # Check whether the method dump_me of class FieldAttributeBase is throwing expected exceptions
    assert True


# Generated at 2022-06-13 07:51:42.502296
# Unit test for method from_attrs of class FieldAttributeBase

# Generated at 2022-06-13 07:51:53.588057
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    role = Role()
    role.post_validate(templar=MockTemplar())

    # We did not set the value of tasks, so we get the default
    assert role.tasks == []

    # We set the value of tasks
    role.tasks = ['tasks/main.yml']

    # We set the value of tasks
    role.handlers = ['handlers/main.yml']

    # We did not set the value of files, so we get the default
    assert role.files == []

    # We set the value of files
    role.files = 'files/main.yml'

    # We did not set the value of tasks
    assert role.vars == {}

    # We set the value of tasks
    role.vars = {'foo': 'bar'}

    role.squash()

# Generated at 2022-06-13 07:51:56.932562
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)
    def test_func():
        functools.reduce(lambda f, g: lambda x: f(g(x)), [])
    test_object = FieldAttributeBase(default=test_func)
    test_object.load_data(module)


# Generated at 2022-06-13 07:52:02.181259
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    f = FieldAttributeBase()
    try:
        f.get_validated_value('name', {ObjectAttribute: 'ObjectAttribute', 'isa': 'int'}, 2, {})
    except:
        assert False
    else:
        assert True


# Generated at 2022-06-13 07:52:13.459767
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    class FakeClass:
        class Attr:
            def __init__(self):
                self.isa = None
        attr_1 = Attr()
        attr_2 = Attr()

    obj = FakeClass()
    obj.attr_1.isa = 'test 1'
    obj.attr_2.isa = 'test 2'
    expected_output = FakeClass()
    expected_output.attr_1.isa = 'test 1'
    expected_output.attr_2.isa = 'test 2'
    field_attribute_base = FieldAttributeBase(fields={'attr_1': obj.attr_1, 'attr_2': obj.attr_2})
    assert field_attribute_base.copy() == expected_output

# Generated at 2022-06-13 07:52:42.501278
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    base = FieldAttributeBase()
    cmd = base.dump_attrs()
    assert cmd == {}, 'Base: Expected empty dict'

    base = FieldAttributeBase(some_arg='some_value')
    cmd = base.dump_attrs()
    assert cmd == {}, 'Base: Expected empty dict'



# Generated at 2022-06-13 07:52:45.248249
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    pass  # TODO: unit test not implemented


# Generated at 2022-06-13 07:52:53.563579
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    '''
    Unit test for method dump_me of class FieldAttributeBase
    '''

    # If a field attribute is not defined by another class, the
    # dump_me will return None
    my_field = FieldAttributeBase()
    if my_field.dump_me() is not None: # check if it is None or not
        print("Failed to dump_me of class FieldAttributeBase")
        sys.exit(1) # indicate failure

    # If a field attribute is defined by another class, the
    # dump_me will return the dictionary of the class
    my_field = FieldAttributeBase()
    my_attr = dict(name="myname", default="mydefault")
    my_field = FieldAttributeBase(**my_attr)

# Generated at 2022-06-13 07:52:57.853286
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    argspec = inspect.getargspec(FieldAttributeBase.post_validate)
    assert len(argspec.args) == 2
    assert argspec.varargs is None
    assert argspec.keywords is None
    assert argspec.defaults is None

# Generated at 2022-06-13 07:53:07.839111
# Unit test for method post_validate of class FieldAttributeBase

# Generated at 2022-06-13 07:53:16.010663
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    data = dict(
        a='1',
        b='2',
        c='3',
        d='4',
        e=dict(
            ea='5',
            eb='6',
            ec='7',
            ed='8',
        ),
    )

    f = FieldAttributeBase(name='f')
    f._attributes = data
    f._attr_defaults = {k:None for k in data.keys()}
    f._valid_attrs = {k:FieldAttribute(name=k) for k in data.keys()}
    results = f.dump_attrs()
    assert results == data


# Generated at 2022-06-13 07:53:17.066419
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    pass


# Generated at 2022-06-13 07:53:20.743677
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    '''
    Unit test to check squash of FieldAttributeBase
    '''

    t = FieldAttributeBase()
    assert t.squash() == False

# Generated at 2022-06-13 07:53:32.616631
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    test_alias = 'test alias'
    test_name = 'test name'
    test_default = 'test default'
    test_required = 'test required'
    test_choices = 'test choices'
    test_docs = 'test docs'
    test_private = 'test private'
    test_deprecated_choices = 'test deprecated choices'
    test_deprecated_aliases = 'test deprecated aliases'
    test_version_added = 'test version added'
    test_version_removed = 'test version removed'
    test_isatype = 'test isa type'
    test_class_type = 'test class type'
    test_listof = 'test list of'
    test_deprecated_text = 'test deprecated text'


# Generated at 2022-06-13 07:53:35.879355
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    BaseObj = Base._create_class_with_bases('Base', [BaseObject])
    O = BaseObj()
    O.validate()
    assert True



# Generated at 2022-06-13 07:54:12.515357
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    '''
    Unit test for method post_validate of class FieldAttributeBase
    '''
    obj = FieldAttributeBase()
    expected_result = {'test_FieldAttributeBase_post_validate': 'FieldAttributeBase'}

    # Test with argument: 'obj'
    # assert_equals(obj.post_validate(obj), expected_result)

    # Report test result
    assert 'test_FieldAttributeBase_post_validate' in locals(), "Test method 'test_FieldAttributeBase_post_validate' should be in locals() to be run"
    print ("Test method 'test_FieldAttributeBase_post_validate' passed")


# Generated at 2022-06-13 07:54:13.630235
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    f = FieldAttributeBase()


# Generated at 2022-06-13 07:54:22.454543
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.vault import VaultLib
    import tempfile
    vault_password = b"hello"
    vault_file = tempfile.NamedTemporaryFile()
    vault = VaultLib([(vault_password, )], 1)
    vault_data = vault.encrypt(b"foobar")
    vault_file.write(vault_data)
    vault_file.flush()
    vault_path = vault_file.name
    vault_data2 = vault.encrypt(b"foobar2")
    vault_file.write(b'\n')
    vault_file.write(vault_data2)
    vault_file.flush()
    vault_path2 = vault_file.name


# Generated at 2022-06-13 07:54:32.632522
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    from ansible import constants as C

    from ansible.plugins.loader import action_loader
    from ansible.playbook.base import Base
    from ansible.template import Templar

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    def test_field_class_type():
        f = FieldAttributeBase('', cls=True, class_type=ActionModule)
        f.load_data('test_foo_module', class_only=True)
        assert f.class_type == ActionModule
        assert f.module == 'test_foo_module'
        assert f.static is True
        assert f.static_name == 'test_foo_module'
        assert f.static_module == 'test_foo_module'


# Generated at 2022-06-13 07:54:46.239703
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():

    mock = magicmock()
    mock.dump = MagicMock(return_value = {'mock': 'dump'})

    mock_class_instance = mock()
    mock_instance = magicmock()
    mock_instance.serialize = MagicMock(return_value = {'mock': 'serialize'})
    field_attribute_base = FieldAttributeBase(mock_class_instance)
    field_attribute_base.dump_attrs = MagicMock(return_value = {'mock': 'dump_attrs'})
    field_attribute_base.name = 'mock_name'
    field_attribute_base.isa = 'mock_isa'
    field_attribute_base.default = 'mock_default'
    field_attribute_base.short_help = 'mock_short_help'
   

# Generated at 2022-06-13 07:54:56.535972
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.utils.vars import combine_vars
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.errors import AnsibleParserError
    import pytest
    import sys


# Generated at 2022-06-13 07:55:01.982844
# Unit test for method get_ds of class FieldAttributeBase
def test_FieldAttributeBase_get_ds():

    # Build a simple object for this test
    obj = FieldAttributeBase()

    assert obj._ds is None
    assert obj.get_ds() is None

    # Set a ds value and re-test
    obj._ds = {'foo': 'bar'}
    assert obj._ds == {'foo': 'bar'}
    assert obj.get_ds() == {'foo': 'bar'}



# Generated at 2022-06-13 07:55:10.604681
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():

    # Test for different value of dep_chain

    # Test for dep_chain = None
    myobj = Base()
    assert myobj.get_dep_chain() == None

    # Test for dep_chain = [1,2,3,4]
    dep_chain = [1, 2, 3, 4]

    myobj._parent = dep_chain[0]
    myobj._parent._parent = dep_chain[1]
    myobj._parent._parent._parent = dep_chain[2]
    myobj._parent._parent._parent._parent = dep_chain[3]
    assert myobj.get_dep_chain() == dep_chain



# Generated at 2022-06-13 07:55:13.362773
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    contains(BaseMeta.__doc__, '''
    Metaclass for the Base object, which is used to construct the class
    attributes based on the FieldAttributes available.
    ''')
    pass


# Generated at 2022-06-13 07:55:15.471773
# Unit test for method from_attrs of class FieldAttributeBase

# Generated at 2022-06-13 07:55:47.911022
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    d = {'attr1': 1, 'attr2': 2, 'attr3': '3', 'attr4': [1, 2, 3], 'attr5': {'a': 1}}
    f = FieldAttributeBase()
    for k, v in iteritems(d):
        f.add_field(k)
        setattr(f, k, v)
    assert d == f.dump_attrs()

# Generated at 2022-06-13 07:55:55.394491
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    m = type_utils.FieldAttributeBase()
    m.__dict__ = dict(ANSIBLE_METADATA=Sentinel.ANSIBLE_METADATA,
    COLLECTION_PATHS=Sentinel.COLLECTION_PATHS)
    ret = m.dump_attrs()
    assert ret == dict(ANSIBLE_METADATA=Sentinel.ANSIBLE_METADATA,
    COLLECTION_PATHS=Sentinel.COLLECTION_PATHS)



# Generated at 2022-06-13 07:56:04.445996
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from copy import copy, deepcopy

    # Test when omit_value is None and value is not omit_value
    obj = Test_FieldAttributeBase_post_validate_Obj(new_value = 5)
    assert obj.value == 5
    obj.post_validate(templar=DictVariableManager())
    assert obj.value == 5

    # Test when value is omit_value
    obj = Test_FieldAttributeBase_post_validate_Obj(new_value = '__omit_place_holder__')
    assert obj.value == '__omit_place_holder__'
    obj.post_validate(templar=DictVariableManager())
    assert obj.value == 0

    # Test when omit_value is not None and value is not omit_value
    obj = Test_FieldAttributeBase_post_validate_

# Generated at 2022-06-13 07:56:08.160112
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    field_attrib = FieldAttributeBase()
    with pytest.raises(NotImplementedError) as error:
        field_attrib.validate(None)
    assert "Class FieldAttributeBase must implement validate()" in to_text(error.value)


# Generated at 2022-06-13 07:56:09.603390
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    data = FieldAttributeBase()
    assert data.dump_me() == {}



# Generated at 2022-06-13 07:56:16.399818
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    '''
    Test load_data of class FieldAttributeBase
    '''

    model = FieldAttributeBase()
    sample_data = {
        'test': 'test',
    }

    # Test normal execution
    try:
        model.load_data(sample_data)
    except Exception:
        traceback.print_exc()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        test_method_name = 'test_' + sys.argv.pop()
        if test_method_name in globals():
            globals()[test_method_name]()
        else:
            print("Method %s not found" % test_method_name)
    else:
        test_FieldAttributeBase_load_data()

# Generated at 2022-06-13 07:56:19.153851
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    '''
    Test deserialize
    '''
    task = FieldAttributeBase()
    try:
        repr(task)
        assert False
    except Exception:
        pass


# Generated at 2022-06-13 07:56:20.261885
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    _fi = FieldAttributeBase()
    assert _fi.dump_me() == "NOT IMPLEMENTED"


# Generated at 2022-06-13 07:56:23.254223
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    f = FieldAttributeBase()
    c = TestBaseClass()
    ds = {}
    to_text = lambda x: x
    f.load_data(c, ds, to_text)

# Generated at 2022-06-13 07:56:29.365171
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    config = dict()
    config['attribute'] = FieldAttributeBase
    config['value'] = dict()
    config['exception'] = None
    # Perform the test
    try:
        FieldAttributeBase.validate(config['attribute'], config['value'])
    # Compare exception name with expected output
    except Exception as e:
        config['exception'] = e
        assert type(config['exception']).__name__ == config['exception_name']

# Generated at 2022-06-13 07:57:01.118483
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    play = AnsiblePlay()
    templar = Templar(loader=DictDataLoader({}))
    play.post_validate(templar)
# tests that the post validator works correctly when the `always_post_validate` flag is not set
# TODO: Unit test for method post_validate of class FieldAttributeBase

# Generated at 2022-06-13 07:57:05.639143
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    print("test_copy")
    print("test_copy_1")
    attribute = FieldAttributeBase()
    attribute.name = "name"
    attribute.required = True
    attribute.private = False

    assert(attribute.name == "name")
    assert(attribute.required == True)
    assert(attribute.private == False)
    copy = attribute.copy()

    assert(copy.name == "name")
    assert(copy.required == True)
    assert(copy.private == False)

    print("test_copy_2")
    attribute = FieldAttributeBase()
    attribute.name = "name"
    attribute.required = True
    attribute.private = True

    assert(attribute.name == "name")
    assert(attribute.required == True)
    assert(attribute.private == True)
    copy = attribute.copy()



# Generated at 2022-06-13 07:57:15.644275
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    from ansible.parsing.yaml.objects import AnsibleSequence

    # initialize a new instance of our class
    obj = FieldAttributeBase()

    # create a new AnsibleSequence object
    ansible_sequence = AnsibleSequence()

    # create a new dict object
    data = {
        'vars': {
            'test': 'here'
        },
        'register': 'result',
    }

    # set an attribute of the object
    obj.from_attrs(data)

    # assert that the attribute of the object has the expected value
    assert obj.vars == {'test': 'here'}, obj.vars
    assert obj.register == 'result', obj.register

# Generated at 2022-06-13 07:57:25.681951
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    test_base = Base()
    test_base._parent = Base()
    test_base._parent._parent = Base()
    test_base._parent._role_path = '/root/'
    test_base._parent._parent._role_path = '/root/home/'
    test_base._ds = Base()
    test_base._ds._data_source = '/etc/'
    path_stack = ['/root/','/root/home/','/etc/']
    assert test_base.get_search_path() == path_stack


# Generated at 2022-06-13 07:57:29.694636
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    obj = FieldAttributeBase()
    assert obj.from_attrs('test_data') == None
    assert obj.from_attrs() == None
    assert obj.dump_attrs() == {}

# Generated at 2022-06-13 07:57:40.920452
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    field_attribute_base = FieldAttributeBase()
    field_attribute_base.isa = 'unicode'
    field_attribute_base.required = True
    field_attribute_base.default = AnsibleUnicode()
    field_attribute_base.unique = False
    field_attribute_base.static = False
    field_attribute_base.always_post_validate = False
    field_attribute_base.class_type = AnsibleUnicode
    field_attribute_base.listof = None
    field_attribute_base.class_restrictions = []
    value = AnsibleUnicode()
    field_attribute_base.validate(value)



# Generated at 2022-06-13 07:57:46.684434
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    o = FieldAttributeBase()
    o.foo = 42
    o.bar = 'zorglub'
    assert o.dump_attrs() == {'foo': 42, 'bar': 'zorglub'}
    assert type(o.dump_attrs()['foo']) == int
    assert type(o.dump_attrs()['bar']) == str
 

# Generated at 2022-06-13 07:57:54.359323
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    x = FieldAttributeBase(default=None)
    assert_equals(x.validate(None, None), Sentinel)

    x = FieldAttributeBase()
    assert_raises(TypeError, x.validate, 'name', None)

    x = FieldAttributeBase(always_post_validate=False)
    assert_raises(TypeError, x.validate, 'name', None)

    x = FieldAttributeBase(required=True, always_post_validate=False)
    assert_raises(TypeError, x.validate, 'name', None)

    x = FieldAttributeBase(required=True, always_post_validate=True)
    assert_raises(TypeError, x.validate, 'name', None)

    x = FieldAttributeBase(always_post_validate=True)
    assert_raises

# Generated at 2022-06-13 07:57:56.278175
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    instance = FieldAttributeBase()
    ret = instance.dump_attrs()
    assert ret is None


# Generated at 2022-06-13 07:58:07.708672
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    attr = FieldAttribute(isa='string')
    a = FieldAttributeBase(loader=None, variable_manager=None)
    a._valid_attrs = {'foo': attr}
    a.foo = 'foo'
    repr_data = {'foo': 'foo'}
    a.deserialize(repr_data)
    assert a.foo == 'foo'
    repr_data = {'foo': 'foo', '_uuid': 'bar'}
    a.deserialize(repr_data)
    assert a.foo == 'foo'
    assert a._uuid == 'bar'
    attr = FieldAttribute(isa='string', default=42)
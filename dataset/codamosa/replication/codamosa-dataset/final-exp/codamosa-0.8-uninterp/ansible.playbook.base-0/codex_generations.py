

# Generated at 2022-06-13 07:49:54.163716
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    f = FieldAttributeBase(isa='str', default=None)
    assert f.dump_attrs() == {}


# Generated at 2022-06-13 07:49:56.274619
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    # FIXME: implement tests
    pass


# Generated at 2022-06-13 07:50:08.024547
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    # Test the FieldAttributeBase.get_validated_value() method
    value = 'DummyValue'
    attribute = FieldAttribute()
    fieldattributebase = FieldAttributeBase()

    # If the attribute isa is string, then we should convert to a text
    # type
    attribute.isa = 'string'
    new_value = fieldattributebase.get_validated_value('name', attribute,
                                                        value, 'templar')
    assert (isinstance(new_value, text_type))
    assert (new_value == to_text(value))

    # If the attribute isa is int, then we should convert the value to an
    # int
    attribute.isa = 'int'
    new_value = fieldattributebase.get_validated_value('name', attribute,
                                                        value, 'templar')


# Generated at 2022-06-13 07:50:10.349412
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    field = FieldAttribute()
    assert field.dump_me == "a"


# Generated at 2022-06-13 07:50:20.588832
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.utils.unsafe_proxy import wrap_var
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib

    from ansible.module_utils.six import string_types
    from ansible.module_utils._text import to_text, to_native
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.parsing.splitter import parse_kv


# Generated at 2022-06-13 07:50:32.076860
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    task = Task()

# Generated at 2022-06-13 07:50:40.819745
# Unit test for method get_ds of class FieldAttributeBase
def test_FieldAttributeBase_get_ds():
    # Unit test for method get_ds
    # of class FieldAttributeBase
    #   def get_ds(self):
    #       ''' Returns the display string for the object,
    #           which is used in exception reporting.
    #       '''
    #       return self._ds
    #   def set_ds(self, ds):
    #       self._ds = ds
    #       return self
    #   ds = property(fdel=None, get_ds=get_ds,
    #                 doc='Ansible display string for the object')
    fail_if_not_equal(type(FieldAttributeBase().get_ds),
                      property)

# Generated at 2022-06-13 07:50:53.717994
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    from mock import Mock, patch
    from collections import Mapping, Sequence
    mock_attrs = {'result':{'required': True, 'class_type': bool, 'isa': 'bool', 'default': False, 'type': bool, 'static': False}}
    mock_self = Mock(dict,_valid_attrs=mock_attrs)
    mock_self.result = True
    #patch the mock_self.dump_attrs()
    with patch.object(mock_self,'dump_attrs') as mock_dump_attrs:
        mock_dump_attrs.return_value = {'result': True}
        attrs = mock_self.dump_attrs()

# Generated at 2022-06-13 07:50:54.976123
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    test_obj = FieldAttributeBase()
    assert test_obj.dump_me() is None


# Generated at 2022-06-13 07:50:56.875776
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    obj = FieldAttributeBase()
    assert not hasattr(obj, '_finalized')


# Generated at 2022-06-13 07:51:28.530072
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    f_base = FieldAttributeBase()
    class_obj = FieldAttributeBase()
    f_base._post_validate_class(class_obj, class_obj, class_obj)
    assert class_obj._validated == True


# Generated at 2022-06-13 07:51:31.328542
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    from ansible.playbook.play_context import PlayContext

    play_context = PlayContext()
    base = Base()
    base._parent = play_context
    # test for normal case
    base._parent._play = base
    base._parent._play._role_path = '.'
    assert base.get_search_path() == ['.']

    # test for abnormal case
    base._parent = None
    assert base.get_search_path() == []


# Generated at 2022-06-13 07:51:42.033347
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    _fd = 'some_file.yaml'
    _name = 'foo'
    _path = '/path/to/role'
    _dt = lambda : 0
    _df = lambda : 0
    _dv = lambda : 0
    _dest = lambda : 0
    _lo = lambda : 0
    _default = lambda : 0
    _env = lambda : 0
    _config = lambda : 0
    _aliases = lambda : 0
    _attr = lambda : 0
    _private = lambda : 0
    _required = lambda : 0
    _include = lambda : 0
    _exclude = lambda : 0
    _version_added = lambda : 0
    _choices = lambda : 0
    _no_log = lambda : 0
    _always_post_validate = lambda : 0
    _static = lambda : 0

   

# Generated at 2022-06-13 07:51:50.037320
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    global_args_file = dict(vars_file=[])
    context.CLIARGS = global_args_file

    mock_self = mock.MagicMock()
    dep_chain = mock.MagicMock()
    mock_self.get_dep_chain = mock.MagicMock(return_value=dep_chain)
    assert Base.get_dep_chain(mock_self) == dep_chain
    mock_self.get_dep_chain.assert_called_once()

# Generated at 2022-06-13 07:51:52.412806
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    base = Base()
    search_path = base.get_search_path()
    assert isinstance(search_path, list), 'Search path of each task should be a list'



# Generated at 2022-06-13 07:51:53.038394
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    pass

# Generated at 2022-06-13 07:51:58.582286
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    # Create an instance of FieldAttributeBase to test
    fieldattributebase_class = FieldAttributeBase()
    args = {}


# Generated at 2022-06-13 07:52:03.641211
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    fieldattributebase = FieldAttributeBase()
    name = "test_name"
    attribute = TestObject()
    value = TestObject()
    templar = TestObject()
    fieldattributebase.get_validated_value(name, attribute, value, templar)

# Generated at 2022-06-13 07:52:08.243510
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    '''
    Unit test for function post_validate
    '''

    # Input parameters for the unit test
    FieldAttributeBase_object = FieldAttributeBase()

    # Test implementation of post_validate here
    # Ensure that an exception is raised whenever expected


# Generated at 2022-06-13 07:52:18.141997
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    p = Play()
    p._ds = namedtuple('BaseDataSource', ['_data_source', '_line_number'])('.\\test\\test_yaml\\test_base.yml', 10)
    t = Task()
    t._ds = namedtuple('BaseDataSource', ['_data_source', '_line_number'])('.\\test\\test_yaml\\test_base.yml', 11)
    p._included_files.append('.\\test\\test_yaml\\test_base.yml')
    t._parent = p
    path_stack = t.get_search_path()
    assert path_stack == ['.\\test\\test_yaml']

    p = Play()
    p

# Generated at 2022-06-13 07:52:52.691994
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    from test.support.fixtures import valid_attributes

    # basic tests with all values as dict
    fa = valid_attributes()
    assert fa.deserialize({'foo': 'bar', 'baz': 'qux'}) == {'foo': 'bar', 'baz': 'qux'}

    # Test with a dict with an attribute and a class attribute
    fa = valid_attributes(attributes={'foo': FieldAttribute(isa='class'), 'baz': FieldAttribute()})
    assert fa.deserialize({'foo': 'bar', 'baz': 'qux'}) == {'foo': 'bar', 'baz': 'qux'}

    # Test with dict with class attribute
    fa = valid_attributes(attributes={'foo': FieldAttribute(isa='class')})

# Generated at 2022-06-13 07:52:55.631576
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    field_attr_base = FieldAttributeBase()
    assert field_attr_base.get_validated_value(string, None) == None


# Generated at 2022-06-13 07:53:07.343095
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    root = ansible.utils.module_docs.ANSIBLE_METADATA
    if root is None:
        root = os.path.join(os.path.dirname(ansible.__file__), "..", "..")
        root = os.path.abspath(root)
    docpath = os.path.join(root, "module_utils", "basic.py")
    with open(docpath, "rb") as f:
        source = to_text(f.read(), errors='surrogate_or_strict')


# Generated at 2022-06-13 07:53:17.101393
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    play_context = PlayContext()
    play_context.CLIARGS = {
        'extra_vars': [{'cat': 'meow'}, {'dog': 'woof'}]
    }
    templar = Templar(loader=None, variables=play_context.CLIARGS)

    play = Play.load(
        dict(
            name="Ansible Play",
            connection="local",
            hosts=["all"],
            max_fail_percentage=30,
            gather_facts="no"
        ),
        play_context,
        loader=None,
        variable_manager=play_context.variable_manager
    )

# Generated at 2022-06-13 07:53:24.008815
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from ansible.parsing.yaml.loader import AnsibleLoader

    field = FieldAttributeBase()
    attrs = ['foobar', 'fast', 'async']
    ds = AnsibleLoader(None, attrs).get_single_data()
    with pytest.raises(AnsibleParserError) as excinfo:
        field.post_validate(ds)


# Generated at 2022-06-13 07:53:33.115146
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    ansible_module_data = dict(
        name='name',
        isa='isa',
        default='default',
        category='category',
        always_post_validate='always_post_validate',
        required='required',
        static='static'
    )
    instance = FieldAttributeBase()
    instance.load_data(ansible_module_data)
    assert instance.name == 'name'
    assert instance.isa == 'isa'
    assert instance.default is 'default'
    assert instance.category == 'category'
    assert instance.always_post_validate == 'always_post_validate'
    assert instance.required == 'required'
    assert instance.static == 'static'

# Generated at 2022-06-13 07:53:36.533786
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    f = FieldAttributeBase()
    f._attributes = {
        'attr1': 'value1',
    }

    assert f.dump_attrs() == { 'attr1': 'value1' }


# Generated at 2022-06-13 07:53:44.488472
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    class MockBase(Base):
        def get_search_path(self):
            return super(MockBase, self).get_search_path()

    class MockRole:
        def __init__(self, role_path):
            self._role_path = role_path

    b = MockBase()
    assert b.get_dep_chain() is None
    b._parent = MockBase()
    b._parent._parent = MockBase()
    b._parent._parent._role = MockRole(role_path='mock_role_path')
    assert b.get_dep_chain()[-1]._role_path == 'mock_role_path'
    p = b.get_search_path()
    assert p[-1] == os.path.dirname('mock_role_path')

# Generated at 2022-06-13 07:53:47.524093
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    fieldattr = FieldAttributeBase()
    assert fieldattr.validate({'testkey': 'testval'}) == {}

# Generated at 2022-06-13 07:53:48.987235
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    """Test case for ``FieldAttributeBase.copy``."""
    raise SkipTest

# Generated at 2022-06-13 07:54:53.373318
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.utils.vars import combine_vars

    pb = Play().load({
        'name': 'test play',
        'hosts': 'all',
        'gather_facts': 'no',
        'tasks': [
            {
                'name': 'test',
                'tags': {'foo': '1', 'bar': '2'}
            }
        ]
    }, variable_manager=VariableManager(), loader=DataLoader())

    # Ensure that the var value is retained when the var is undefined
    task = pb.get_tasks()[0]

# Generated at 2022-06-13 07:54:58.053846
# Unit test for method get_ds of class FieldAttributeBase
def test_FieldAttributeBase_get_ds():
    # Load fake data from YAML to dict
    data = load_fixture('FieldAttributeBase_get_ds.yml')

    # Create object with fake data
    field_attribute_base = FieldAttributeBase(data)

    result = field_attribute_base.get_ds()
    assert type(result) == dict
    assert result == data


# Generated at 2022-06-13 07:55:00.142953
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    my_obj = FieldAttributeBase()
    my_obj.validate(None, None, None)

# Generated at 2022-06-13 07:55:02.892363
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    obj = FieldAttributeBase()
    repr = obj.dump_attrs()
    assert repr is not None
    assert repr == {}
    return obj



# Generated at 2022-06-13 07:55:05.826512
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    with pytest.raises(NotImplementedError):
        field_attribute_base = FieldAttributeBase(name='FieldAttributeBase', default=None)
        field_attribute_base.dump_attrs()

# Generated at 2022-06-13 07:55:15.396925
# Unit test for method load_data of class FieldAttributeBase

# Generated at 2022-06-13 07:55:26.402804
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():

    valid_attrs = dict(
        required=dict(type='bool', default=False),
        static=dict(type='bool', default=False),
        listof=None,
        isa=None,
        class_type=None,
        default=None,
        always_post_validate=None,
    )

    # Test without required attributes
    ba = FieldAttributeBase()
    for name in valid_attrs:
        assert getattr(ba, name) == valid_attrs[name]['default']

    # Test with all attributes
    ba = FieldAttributeBase(**{k: 'a' for k in valid_attrs})
    for name, attr in iteritems(valid_attrs):
        assert getattr(ba, name) == 'a'


# Generated at 2022-06-13 07:55:40.840710
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    host_vars = dict(ansible_connection=dict(type='ssh'))
    variable_manager = VariableManager(loader=DataLoader(), inventory=Inventory(host_list=None, variable_manager=variable_manager))
    variable_manager.extra_vars = host_vars
    _test_class = FieldAttributeBase(loader=None, variable_manager=variable_manager, fail_on_undefined_errors=True)
    _test_class.post_validate(templar=variable_manager)
    assert _test_class.get_validated_value(name='ansible_host', attribute=ansible_host, value='10.10.10.10', templar=variable_manager) == '10.10.10.10'

# Generated at 2022-06-13 07:55:42.841264
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 07:55:53.899810
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    import pytest
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.vars import combine_vars
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    import ansible.parsing.yaml.objects
    from ansible.module_utils.six.moves import StringIO
    from ansible.errors import AnsibleParserError
    from collections import namedtuple
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleSequence

# Generated at 2022-06-13 07:56:54.230923
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
  import pytest
  d = dict()

  # Test that if the field is not present in the data, the default
  # value is returned unchanged.
  t = FieldAttributeBase('name', None)
  assert t.load_data(d) is None

  # Test that the field can be loaded from the data
  t = FieldAttributeBase('name', None)
  d['name'] = 'foo'
  assert t.load_data(d) == 'foo'

  # Test that the field is not loaded if the key is not present
  # in the data, and the default value is set instead
  t = FieldAttributeBase('name', None, default='foo')
  d['name'] = 'foo'
  assert t.load_data(d) == 'foo'

  # Test that the field is loaded from the data if the key is present,

# Generated at 2022-06-13 07:57:05.038555
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    from collections import namedtuple
    '''
    Metaclass for the Base object, which is used to construct the class
    attributes based on the FieldAttributes available.
    '''

    # This test is vulnerable to refactoring, since it depends on private
    # details of BaseMeta.  If this test is failing, it could be a refactoring
    # that is not intended to be noticed.  If this is the case, then this test
    # should be removed.
    def _create_attrs(src_dict, dst_dict):
        '''
        Helper method which creates the attributes based on those in the
        source dictionary of attributes. This also populates the other
        attributes used to keep track of these attributes and via the
        getter/setter/deleter methods.
        '''
        keys = list(src_dict.keys())

# Generated at 2022-06-13 07:57:08.550476
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    name='name'
    attribute=FieldAttributeBase()
    data=None
    field=FieldAttributeBase()
    field._validate(name, attribute, data)
    return True

# Generated at 2022-06-13 07:57:18.257567
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    from ansible.cli.playbook import PlaybookCLI
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    from ansible.vars.manager import VariableManager
    from ansible.vars.reserved import Reserved

    playbook = u'---\n- hosts: localhost\n  tasks:\n    - debug:\n        msg: hello world\n'
    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=VariableManager(), host_list=['localhost'])
    pm = PlaybookCLI(playbooks=[playbook])
    passwords = {}
    all_vars = VariableManager()
    all_vars.extra_vars = load_extra

# Generated at 2022-06-13 07:57:28.590396
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    attrib = FieldAttributeBase(unique=True, always_post_validate=False, history=False,
                                class_type=None, isa=None, default=None,
                                required=None, choices=False, aliases=None, ignore_errors=False,
                                attr_name=None, error_text=None, hash_name=None, convert_to=None,
                                always_evaluate=True, fail_on_undefined=False,
                                static=False)

    data = attrib.dump_attrs()

    assert data == {}

# Generated at 2022-06-13 07:57:30.728514
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    fab = FieldAttributeBase()
    assert fab.get_validated_value('test', 'attribute', 'test') == 'test'

# Generated at 2022-06-13 07:57:36.581468
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    # Random tests

    # Bad cases

    # Standard tests
    val = FieldAttributeBase('name', 'class', 'required', True)
    assert val.name == 'name'
    assert val.isa == 'class'
    assert val.static == 'required'
    assert val.required == True


# Generated at 2022-06-13 07:57:38.584039
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    attr = FieldAttribute()
    test_value = 'Foo:Bar'
    result = attr.validate(test_value)
    assert result == test_value


# Generated at 2022-06-13 07:57:39.932183
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    # FIXME: add some tests
    pass

# Generated at 2022-06-13 07:57:50.265433
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    field_attr_1 = FieldAttributeBase()
    field_attr_2 = FieldAttributeBase()
    attrs = {'_valid_attrs': {'foo': field_attr_1}}
    field_attr_2.from_attrs(attrs)
    assert field_attr_2._valid_attrs == {'foo': field_attr_1}
    assert field_attr_2._finalized == True
    assert field_attr_2._squashed == True
    # Test that if the argument attrs is not an instance of dict,
    # the method raises AnsibleAssertionError
    with pytest.raises(AnsibleAssertionError) as pytest_wrapped_e:
        field_attr_2.from_attrs('foo')
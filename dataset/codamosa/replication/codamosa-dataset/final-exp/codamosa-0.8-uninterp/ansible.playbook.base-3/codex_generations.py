

# Generated at 2022-06-13 07:50:21.941203
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    # Setup Mock and test object
    value = 'string'
    templar = MagicMock()
    test = FieldAttributeBase(name='test', isa='string')
    subject = FieldAttributeBase(name='subject', isa='string')
    attr = MagicMock()
    attr.isa = 'string'
    attr.required = True
    attr.listof = string_types
    subject.get_validated_value('name', attr, value, templar)
    subject.get_validated_value('name', test, 424, templar)
    with pytest.raises(TypeError, match="'test' is not a valid identifier"):
        subject.get_validated_value('name', test, value, templar)

# Generated at 2022-06-13 07:50:33.651668
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    Base_test = Base()
    #set up the value of property _parent
    playbook = Playbook()
    play = Play()
    play._ds = DataSource({}, None)
    play._ds._line_number = 23
    playbook._play = play
    playbook._role_path = '/home/myuser/ansible'
    playbook._ds = DataSource({}, None)
    playbook._ds._line_number = 45
    role1 = Role()
    role1._role_path = '/home/myuser/ansible/roles/role1'
    role1._ds = DataSource({}, None)
    role1._ds._line_number = 67
    role2 = Role()
    role2._role_path = '/home/myuser/ansible/roles/role2'

# Generated at 2022-06-13 07:50:36.012678
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    f = Fields()
    assert f.get_validated_value('name', 'boolean', 'True', None) == True



# Generated at 2022-06-13 07:50:44.833519
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    class Task(Base):
        pass
    class Play(Base):
        pass

    task = Task()
    task._ds._data_source = '/base/path'

    play = Play()
    play._ds._data_source = 'test/test'
    play._role_path = '/base'
    play._parent = Task()
    task._parent = play

    # check: run by playbook
    assert task.get_search_path() == ['test/test']

    # check: run by role
    assert task.get_search_path() == ['/base']

    # check: run by role and its dependency
    task._parent._parent._parent = Play()
    task._parent._parent._parent._role_path = '/base/dep'
    assert task.get_search_path() == ['/base/dep', '/base']

# Generated at 2022-06-13 07:50:52.328038
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    # create an instance of the Ansible class
    fieldattributebase_instance = FieldAttributeBase()

    # compute and validate the results of the Ansible class dump_me method
    actual_results = fieldattributebase_instance.dump_me()
    expected_results = {'raw_field_name': 'dump_me',
        'error_text': 'Not Implemented'}
    assert_equal(actual_results, expected_results)



# Generated at 2022-06-13 07:50:57.066645
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    attr = FieldAttribute()
    attr.isa = 'string'
    field = FieldAttributeBase()
    result = field.get_validated_value('name', attr, 'value', templar=None)
    assert result == 'value'

# Generated at 2022-06-13 07:51:00.735468
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    # Create and return a new instance of FieldAttributeBase for test
    post_validate = FieldAttributeBase()
    # Return an instance of FieldAttributeBase after testing method post_validate
    return post_validate


# Generated at 2022-06-13 07:51:04.397942
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    for field_attr, test_data in iteritems(test_data_FieldAttributeBase_post_validate):
        obj = FieldAttributeBase(**field_attr)
        for data in test_data:
            obj.post_validate(data)


# Generated at 2022-06-13 07:51:06.796677
# Unit test for method get_path of class Base
def test_Base_get_path():
    b = Base()
    b.get_path()


# Generated at 2022-06-13 07:51:13.901028
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.module_utils.common._collections_compat import Sequence
    from ansible.module_utils.basic import AnsibleFallbackNotFound
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import PY3
    from ansible.errors import AnsibleError
    # We don't need a templar here, just a play context
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()


# Generated at 2022-06-13 07:51:50.673084
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():

    def call(adict):
        f = FieldAttributeBase()
        return f.dump_me(adict)

    assert call({}) == {}
    assert call({'task3': 'task3_value'}) == {'task3': 'task3_value'}
    assert call({'task5': 'task5_value', 'task6': 'task6_value'}) == {'task5': 'task5_value', 'task6': 'task6_value'}
    assert call({'task8': 'task8_value', 'task9': 'task9_value', 'task10': 'task10_value'}) == {'task8': 'task8_value', 'task9': 'task9_value', 'task10': 'task10_value'}

# Generated at 2022-06-13 07:51:55.611314
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import TaskDefinition
    from ansible.playbook.play import Play
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.plays import PlayIterator
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

# Generated at 2022-06-13 07:51:58.003633
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    attrs = {}
    fm = FieldAttributeBase()
    fm.from_attrs(attrs)



# Generated at 2022-06-13 07:52:07.449850
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    from collections import namedtuple

    FieldAttributeBase = namedtuple('FieldAttributeBase', ['name', 'default', 'isa', 'static', 'required', 'always_post_validate', 'class_type', 'listof'])
    data = {'name': 'joe'}
    attribute = FieldAttributeBase(name='name', default='joe', isa='string', static=False, required=False, always_post_validate=False, class_type='class', listof='listof')
    FieldAttributeBase.from_attrs(attribute, data)


# Generated at 2022-06-13 07:52:17.786823
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    from ansible.utils.vars import combine_vars
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import get_file_vault_secret
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.clean import module_response_deepcopy
    from ansible.vars.clean import strip_internal_keys
    from ansible.vars.clean import strip_internal_keys_unsafe
    from ansible.vars.clean import strip_complex_structure
    from ansible.vars.clean import strip_passwords


# Generated at 2022-06-13 07:52:18.721984
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    assert (not hasattr(FieldAttributeBase, 'get_validated_value'))

# Generated at 2022-06-13 07:52:20.762491
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    # given
    class Base_mock(Base):
        _parent = None

    # when
    result = Base_mock.get_dep_chain(Base_mock)

    # then
    assert result == None

# Generated at 2022-06-13 07:52:28.031013
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    ut_data = {}
    ut_data['test'] = { '_valid_attrs': {'value': FieldAttribute()},
                        '_squashed': False,
                        '_finalized': False }
    ut_data['expected'] = {'_squashed': False, '_finalized': False, 'value': None}
    obj = FieldAttributeBase(loader=BaseLoader())
    for item in ut_data:
        if isinstance(ut_data[item], dict):
            setattr(obj, item, ut_data[item])
    obj.deserialize({'value': 'foo'})
    for item in ut_data['expected']:
        assert getattr(obj, item) == ut_data['expected'][item]
 


# Generated at 2022-06-13 07:52:30.322235
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    # This test checks if the path is returned properly
    obj = Base()
    return [(obj.get_dep_chain(),None),
            ]

# Generated at 2022-06-13 07:52:31.858508
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    obj = FieldAttributeBase()
    raise NotImplementedError("Test has not been implemented yet")


# Generated at 2022-06-13 07:53:05.029747
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    import unittest as testlib
    from ansible.compat.tests import mock
    from ansible.compat.tests import unittest

    @unittest.skipIf(six.PY2, "Python 3 only")
    class FieldAttributeBaseTest(testlib.TestCase):
        def test_from_attrs_no_valid_attrs(self):
            from ansible.parsing.yaml.objects import AnsibleUnicode

            class TestTask(FieldAttributeBase):
                pass    # no attributes defined

            task = TestTask()
            self.assertIsNone(task.from_attrs(dict()))
            self.assertIsNone(task.from_attrs(None))
            self.assertIsNone(task.from_attrs(AnsibleUnicode('')))


# Generated at 2022-06-13 07:53:06.450550
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    result = Base().get_search_path()
    expected = []

    assert result == expected


# Generated at 2022-06-13 07:53:16.586025
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    from ansiblelint.utils import load_plugins
    from collections import namedtuple
    from ansible.vars.manager import VariableManager
    from ansible.errors import AnsibleUndefinedVariable, AnsibleParserError

    def get_display():
        return Display()

    Attribute = namedtuple(
        'Attribute',
        [
            'static',
            'isa',
            'default',
            'required',
            'always_post_validate',
            'class_type',
            'listof',
        ]
    )

    def test_func1(self, attr, value, templar):
        return value

    def test_func2(self, attr, value, templar):
        return value

    def test_func3(self, attr, value, templar):
        return value



# Generated at 2022-06-13 07:53:23.055756
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    myobj = FieldAttributeBase()
    ds = AnsibleUnicode('text')
    templar = FieldAttributeBase()
    myobj.test_attr = 'test'
    myobj._post_validate_test_attr(FieldAttributeBase(), 'test', templar)

# Generated at 2022-06-13 07:53:29.828738
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    # test string value
    f = FieldAttributeBase()
    result = f.get_validated_value(None, boolean(), None, None)
    assert result == None
    result = f.get_validated_value(None, boolean(), False, None)
    assert result == False
    result = f.get_validated_value(None, boolean(), 'False', None)
    assert result == False
    result = f.get_validated_value(None, boolean(), True, None)
    assert result == True
    result = f.get_validated_value(None, boolean(), 'True', None)
    assert result == True
    result = f.get_validated_value(None, boolean(), '0', None)
    assert result == False

# Generated at 2022-06-13 07:53:31.791149
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    field_attribute_base = FieldAttributeBase()
    field_attribute_base.deserialize()

# Generated at 2022-06-13 07:53:40.898088
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    '''
    Unit test for method dump_me of class FieldAttributeBase
    '''
    # FIXME: Implement tests for method dump_me of class FieldAttributeBase

    # Test with a value of: '''string'''
    # Test with a value of: '''int'''
    # Test with a value of: '''float'''
    # Test with a value of: '''bool'''
    # Test with a value of: '''list'''
    # Test with a value of: '''class'''
    # Test with a value of: '''set'''
    # Test with a value of: '''dict'''
    # Test with a value of: '''percent'''


# Generated at 2022-06-13 07:53:52.399151
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    # Unit test for method dump_attrs of class FieldAttributeBase
    # Create a instance of FieldAttributeBase
    # repr = <ansible.executor.task_result.TaskResult object at 0x101e0b190>
    repr = TaskResult()

    # repr1 = <ansible.executor.task_result.TaskResult object at 0x101e0b190>
    repr1 = repr.dump_attrs()

    # repr1 == {'started': None, 'failed': False, 'msg': '', 'skipped': False, 'invocation': <ansible.executor.task_result.TaskExecution object at 0x101e0b150>, 'task': <ansible.playbook.task.Task object at 0x101e0b110>, '_result': {}, '_task_fields': ['action', 'async_

# Generated at 2022-06-13 07:53:54.572035
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    fieldattr = FieldAttributeBase()
    fieldattr.validate()

# Generated at 2022-06-13 07:54:03.048473
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    yaml_dict = {}
    yaml = YAML()
    yaml.default_flow_style = False
    data = yaml.load(open('./test/unit/parsing/yaml/base_object_include_type.yml', 'r'))
    f = FieldAttributeBase()
    expected_result = dict(
        name='from yaml',
        description='A description.',
        author='Ansible',
    )
    assert f.from_yaml(yaml_dict, data) == expected_result
    assert f.dump_attrs() == expected_result


# Generated at 2022-06-13 07:54:27.918811
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    assert True

# Generated at 2022-06-13 07:54:35.559137
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    fieldattributebase_obj = FieldAttributeBase()
    fieldattributebase_obj._valid_attrs = {}

    # Test with get_name()
    # test with return None
    fieldattributebase_obj.get_name = lambda : None
    assert fieldattributebase_obj.dump_me() == ""

    # test with not return None
    fieldattributebase_obj.get_name = lambda: "test"
    assert fieldattributebase_obj.dump_me() == "test"

    # Test with get_name() not equal None
    fieldattributebase_obj._valid_attrs = {'test': "abcd", 'test1': "efgh"}
    fieldattributebase_obj.get_name = lambda: "test1"
    assert fieldattributebase_obj.dump_me() == "test1: efgh"

    # Test with

# Generated at 2022-06-13 07:54:41.224761
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    class DummyFieldAttributeBase(FieldAttributeBase):
        _valid_attrs = dict(
            foo = FieldAttribute(isa='int', default=100),
            bar = FieldAttribute(isa='int'),
        )

    item = DummyFieldAttributeBase()
    dump = item.dump_attrs()
    assert {'foo': 100, 'bar': None} == dump

    item_dup = DummyFieldAttributeBase()
    item_dup.from_attrs(dump)
    dump_dup = item_dup.dump_attrs()

    assert dump == dump_dup



# Generated at 2022-06-13 07:54:42.729915
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
        myFieldAttributeBase = FieldAttributeBase()
        myFieldAttributeBase.deserialize("this is a string")


# Generated at 2022-06-13 07:54:47.734551
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from collections import MutableMapping
    from collections import MutableSequence
    from ansible.playbook.play_context import PlayContext

    test1_validated = False
    test2_validated = False
    class TestClass1(FieldAttributeBase):
        test1 = FieldAttribute(isa='list', default=[], always_post_validate=True)
        test2 = FieldAttribute(isa='list', default=[])

        def _post_validate_test1(self, attr, value, templar):
            global test1_validated
            test1_validated = True
            return value

        def _post_validate_test2(self, attr, value, templar):
            global test2_validated
            test2_validated = True
            return value

    # Create an instance of test class
   

# Generated at 2022-06-13 07:54:50.118760
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    # Given
    obj = FieldAttributeBase()
    data = {}
    obj.deserialize(data)


# Generated at 2022-06-13 07:54:57.572630
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    attr_value = FieldAttributeBase(
        name=Unset,
        default=Unset,
        alias=Unset,
        required=Unset,
        always_post_validate=Unset,
        tasks_include_type=Unset,
        skip_if_conditional=Unset,
        static=Unset,
        isa=Unset)
    attr_value.isa = 'boolean'
    attr_value.static = True

# Generated at 2022-06-13 07:54:59.333111
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    assert Base().get_search_path() == []



# Generated at 2022-06-13 07:55:09.218711
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    '''Unit test for method __new__ of class BaseMeta
    '''
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    dct = dict(_attributes = {}, _attr_defaults = {}, _valid_attrs = {}, _alias_attrs = {})
    parent_dct = dict(__dict__ = dict(foo = 1, bar = 2, __bases__ = tuple(),))
    parent = type('parent', (AnsibleBaseYAMLObject,), parent_dct)

    class Base(object):
        __metaclass__ = BaseMeta
    parent_dct['__dict__'].update(dct)

# Generated at 2022-06-13 07:55:17.277471
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.basic import boolean
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.test.utils import DummyModule
    from ansible.template import Templar
    from collections import namedtuple
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars

    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])

    def hostvars_no_vars(*args, **kwargs):
        return dict()


# Generated at 2022-06-13 07:55:44.944623
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    pass


# Generated at 2022-06-13 07:55:58.886797
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.template import Templar

    data = '---\nfoo: 1.2\n'
    loader = DataLoader()
    variable_manager = VariableManager()
    t = Templar(loader=loader, variables=variable_manager)
    attr = type("AnsibleFacts", (object, ),
                {
                    'isa': 'float',
                    'required': True,
                    'static': True,
                    'always_post_validate': True
                })

# Generated at 2022-06-13 07:56:02.619772
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    import pytest
    x = FieldAttributeBase()
    with pytest.raises(AnsibleAssertionError) as excinfo:
        x.deserialize('')
    assert 'data () should be a dict but is a ' in to_text(excinfo)


# Generated at 2022-06-13 07:56:03.185631
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    pass

# Generated at 2022-06-13 07:56:04.591300
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    FieldAttributeBase.get_validated_value
test_FieldAttributeBase_get_validated_value()

# Generated at 2022-06-13 07:56:15.264098
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    play_context = PlayContext()
    play_context.port = 22
    play_context.remote_user = 'root'
    play_context.become = False
    play_context.become_method = 'sudo'
    play_context.become_user = 'roor'
    equal(play_context.get_search_path(), '', msg=None)
    play_context.become = True
    equal(play_context.get_search_path(), '', msg=None)
    play_context.become_method = 'su'
    play_context.become_user = 'admin'
    equal(play_context.get_search_path(), '', msg=None)
    play_context.become_method = 'sudo'
    play_context.become_user = 'root'

# Generated at 2022-06-13 07:56:25.745928
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    assert get_validated_value({}, '', '', ) == {}
    assert get_validated_value({'1': {}, '2': {}, '3': {}}, '', '', ) == {'1': {}, '2': {}, '3': {}}
    assert get_validated_value({'1': {'1': {}}, '2': {'2': {}}, '3': {'3': {}}}, '', '', ) == {'1': {'1': {}}, '2': {'2': {}}, '3': {'3': {}}}

# Generated at 2022-06-13 07:56:28.474598
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    fd = FieldAttributeBase()
    ds = {}
    result = fd.dump_attrs()
    assert (result == ds)


# Generated at 2022-06-13 07:56:37.575855
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    string_types = ('', u'')

    class ClassType(object):
        pass

    class AttrClass(FieldAttributeBase):
        def __init__(self, *args, **kwargs):
            super(AttrClass, self).__init__(*args, **kwargs)

    class Object(BaseObject):
        def __init__(self):
            super(Object, self).__init__()
            self.attr1 = AttrClass(isa='string', default=None)

    obj = Object()

    # Test the following cases:
    #   * string: return text
    #   * int: return int
    #   * float: return float
    #   * bool: return boolean
    #   * percent: return float
    #   * list: return list
    #   * set: return set
    #   * dict

# Generated at 2022-06-13 07:56:39.496941
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    f = FieldAttributeBase()
    g = f.copy()

    assert isinstance(g, FieldAttributeBase)
    assert g != f


# Generated at 2022-06-13 07:57:16.769212
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():    
    pb = PlaybookBase()
    pb.name = 'AAAAAAAAAA'
    pb._entries = Entries([Host(), Host()])
    pb._tasks = TaskBase()
    pb._handler_blocks = TaskBase()
    pb._roles = RoleBase()
    pb._block = Block()
    pb._post_validate_name = mock.MagicMock()
    pb._post_validate_hosts = mock.MagicMock()
    pb._post_validate_vars = mock.MagicMock()
    pb._post_validate_vars_prompt = mock.MagicMock()
    pb._post_validate_gather_facts = mock.MagicMock()
    pb._post_validate_any_errors_fatal = mock.MagicM

# Generated at 2022-06-13 07:57:30.740861
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    def mock_self__parent(self, value):
        # mock the self._parent
        self._parent = value

    def mock_self__parent__play(self, value):
        # mock the parent._play because the get_search_path is called on _play level
        self._play = value

    # when no _parent
    #####
    b = Base()
    assert b.get_search_path() == []

    # when no dep_chain
    #####
    # inside role
    # scaffold the self._parent
    b._parent = Base()
    b._parent._role_path = "role_1"

    # scaffold the self._parent._play
    b._parent._play = Base()
    b._parent._play._ds = mock.MagicMock()

# Generated at 2022-06-13 07:57:33.089724
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    f = FieldAttributeBase()
    assert f.copy(5, 6, 7) == None



# Generated at 2022-06-13 07:57:36.020453
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():

    # Call method with required parameters
    # returns a boolean
    FieldAttributeBase.post_validate()



# Generated at 2022-06-13 07:57:38.631825
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    fixture = FieldAttributeBase(default=None, always_post_validate=False, isa='string', priority=1, private=True)
    assert fixture.squash is None

# Generated at 2022-06-13 07:57:46.793455
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    """ test for method get_dep_chain of class Base
    of module ansible.playbook.base
    """

    # ansible/playbook/base.py:1746:
    # def get_dep_chain(self):
    #     if hasattr(self, '_parent') and self._parent:
    #         return self._parent.get_dep_chain()
    #     else:
    #         return None

    # Testing with a valid play
    play = Play()
    assert(play.get_dep_chain() == None)

    # Testing with a valid task
    play.load({
        'tasks': [
            { 'debug': {
                'msg': 'test'
            } }
        ]
    })
    task = play.tasks[0]

# Generated at 2022-06-13 07:57:51.264034
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    a = FieldAttributeBase()
    config = {'omit': 'omit'}
    variable_manager = VariableManager()
    variable_manager._extra_vars = config
    templar = Templar(loader=None, variables=variable_manager)
    try:
        a.post_validate(templar)
    except AnsibleUndefinedVariable:
        raise AssertionError()



# Generated at 2022-06-13 07:57:55.068039
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    test_obj = FieldAttributeBase()
    attr_name = "foo"
    with pytest.raises(NotImplementedError) as err:
        test_obj.validate(attr_name, None)
    assert str(err.value) == "FieldAttributeBase.validate is not implemented"



# Generated at 2022-06-13 07:57:56.923144
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    base = Base()
    assert base.get_dep_chain() is None



# Generated at 2022-06-13 07:57:57.895292
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    assert not False
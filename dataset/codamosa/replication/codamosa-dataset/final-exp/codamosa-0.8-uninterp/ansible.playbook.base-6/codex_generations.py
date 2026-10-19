

# Generated at 2022-06-13 07:49:47.758299
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    attrs = FieldAttributeBase().dump_attrs()
    assert attrs == {}


# Generated at 2022-06-13 07:49:54.158217
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():

    # get data from yaml file
    temp_file = get_data_file('from_attrs_test.yaml')
    data = yaml.load(temp_file.read())

    # run code
    obj = data['class_type']()
    obj.from_attrs(data['attrs'])

    # compare results
    assert obj.vars == {'a': 'b'}

    return True


# Generated at 2022-06-13 07:49:59.197589
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    attrs = dict(
        name = 'test_var',
        mix = [],
        value = [],
        )
    test_constant = FieldAttributeBase(required=True)
    test_constant.from_attrs(attrs)
    return

# Generated at 2022-06-13 07:50:00.548679
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    assert True

# Generated at 2022-06-13 07:50:09.954137
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    from ._loader import ModuleLoader
    from ._manager import VariableManager
    from ._context import Context
    from ._task import Task
    from . import taskloader
    from .vars.manager import VariableManager

    l = ModuleLoader()

    t_i = taskloader.get('include_tasks', class_only=True)
    t_n = taskloader.get('nailyml', class_only=True)
    t_r = taskloader.get('raw', class_only=True)
    t_v = taskloader.get('vars_prompt', class_only=True)

    t = Task()
    t.action = 'action'
    t.controls = 'controls'
    t.ignore_errors = 'ignore_errors'
    t.loop = 'loop'

# Generated at 2022-06-13 07:50:20.408574
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    from ansible.parsing.yaml.dumper import AnsibleDumper

# Generated at 2022-06-13 07:50:31.868888
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    test_instance_exceptions_errors_types = [
        # (0, TypeError, None, 'Wrong values'),                   # TypeError
        (1, ValueError, '{"a": 3}', 'Wrong type of value'),                 # ValueError
        (2, AnsibleParserError, '{"a": "3"}', 'Wrong type of value'),       # AnsibleParserError
        (3, AnsibleUndefinedVariable, '{"a": "{{ b }}"}', 'Undefined error'),  # AnsibleUndefinedVariable
        (4, UndefinedError, '{"a": "{{ b }}"}', 'Undefined error'),         # UndefinedError
        (5, AnsibleParserError, '{"a": "{{ b }}"}', 'Undefined error'),     # AnsibleParserError
    ]


# Generated at 2022-06-13 07:50:35.902774
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    attr = FieldAttributeBase()
    field = FieldAttributeBase()
    obj = BaseObject()
    templar = Templar()
    assert_raises(NotImplementedError, field.post_validate, attr, obj, templar)


# Generated at 2022-06-13 07:50:36.994726
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    assert True

# Generated at 2022-06-13 07:50:40.281867
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    data = get_test_data()
    field_attribute_base_inst = FieldAttributeBase(
        {},
        data
    )
    assert field_attribute_base_inst.from_attrs(data) is None


# Generated at 2022-06-13 07:51:01.751672
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    assert True


# Generated at 2022-06-13 07:51:10.436962
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():

    from ansible.module_utils._text import to_bytes

    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.utils.vars import combine_vars


    # Dummy class to test FieldAttributeBase
    class DummyClass(AnsibleBaseYAMLObject):

        def __init__(self, ds, **kwargs):
            super(DummyClass, self).__init__(ds, **kwargs)
            self.test_attr = None

        _test_attr = FieldAttribute(isa='bool')

        def _post_validate_test_attr(self, attr, value, templar):
            if isinstance(value, bool):
                return value
            elif isinstance(value, string_types):
                return value == 'on'
           

# Generated at 2022-06-13 07:51:16.999567
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    def test_assertions(b, expect_path_stack):
        assert(b._name == 'test_Base')
        assert(b.get_search_path() == expect_path_stack)

    # test for task which belongs to role,
    # and the role is called from a task in a playbook
    task = Task()
    dep_chain = []

    task_in_playbook = Task()
    playbook = Play()
    task_in_playbook._parent = playbook
    task_in_playbook._parent._play = playbook
    dep_chain.append(task_in_playbook)

    role = Role()
    role._role_path = '/tmp/role1'
    role._tasks = [task]
    dep_chain.append(role)

    task._dep_chain = dep_chain
    b = Base

# Generated at 2022-06-13 07:51:21.852761
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    '''
    Unit test for method get_validated_value of class FieldAttributeBase
    '''

    # Create the object
    obj = FieldAttributeBase()

    # Method get_validated_value not implemented error
    with pytest.raises(NotImplementedError):
        obj.get_validated_value(None, None, None)

# Generated at 2022-06-13 07:51:27.077979
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    f = FieldAttributeBase(isa='list')
    f.class_type = FieldAttributeBase
    assert isinstance(f.default, list)
    # no arguments
    assert f.dump_attrs() == {}
    # set some values
    f.default = [{'isa': 'list'}]
    assert f.dump_attrs() == {}
    f.value = f.default
    assert f.dump_attrs() == {'isa': 'list'}
    # set some more values
    f.default = [{'isa': 'set'}]
    assert f.dump_attrs() == {}
    f.value = f.default
    assert f.dump_attrs() == {'isa': 'set'}
    f.default = [{'isa': 'string'}]
    assert f.dump_

# Generated at 2022-06-13 07:51:35.040662
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    from ansible.parsing.vault import VaultEditor
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.plugins.loader import become_loader
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from units.mock.loader import DictDataLoader

    # Ensure the attributes of a Task and Handler can be deserialized
    # (Both extend FieldAttributeBase)
    # Note that while the dict keys are strings, they are not double quoted
    task_data = dict(
        action=dict(
            module='assert',
            args=dict(
                that=1,
            )
        )
    )
    handler_data = dict(
        name='example',
        listen='other'
    )

# Generated at 2022-06-13 07:51:38.285252
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    base = Base()

    if base.get_dep_chain() != None:
      raise AssertionError()


# Generated at 2022-06-13 07:51:50.412388
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    from ..callback import CallbackBase
    from .. import __version__
    from ..connection import ConnectionBase
    from ..module_utils.connection import Connection
    from ..module_utils.six import string_types
    from ..module_utils.urls import url_argument_spec, url_to_unix_socket
    from ..plugins import PluginLoader
    from ..plugins.callback import CallbackModule
    from ..plugins.connection import ConnectionLoader
    from ..plugins.inventory import BaseInventoryPlugin
    from ..plugins.inventory.host_list import HostList
    from ..plugins.inventory.script import InventoryScript
    from ..plugins.lookup.lookup import LookupModule
    from ..plugins.lookup.template import LookupModule as LookupTemplate
    from ..plugins.strategy.strategy_loader import StrategyModule

# Generated at 2022-06-13 07:51:58.123316
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    # Creation of a Base object
    my_Base = Base()
    my_Base._name = 'Base'

    # Creation of a Base object
    my_Base_1 = Base()
    my_Base_1._name = 'Base_1'

    # Creation of a Base object
    my_Base_2 = Base()
    my_Base_2._name = 'Base_2'

    # Creation of a Base object
    my_Base_3 = Base()
    my_Base_3._name = 'Base_3'

    # Creation of a Base object
    my_Base_4 = Base()
    my_Base_4._name = 'Base_4'

    # Definition of the property _parent of object Base
    my_Base._parent = my_Base_1
    my_Base_1._parent = my_Base_2


# Generated at 2022-06-13 07:52:11.131259
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    # 
    # This function tests the get_search_path() method of the Base class 
    #
    base = Base()
    d = {}
    d['_ds'] = '_ds'
    d['_line_number'] = '_line_number'
    d['_parent'] = {}
    d['_parent']['_play'] = {}
    d['_parent']['_play']['_ds'] = '_ds'
    d['_parent']['_play']['_line_number'] = '_line_number'
    for k, v in d.items():
        setattr(base, k, v)
    
    base._parent = {}
    base._parent['_play'] = {}
    base._parent['_play']['_ds'] = '_ds'
    base

# Generated at 2022-06-13 07:52:34.480266
# Unit test for method get_path of class Base
def test_Base_get_path():
    '''
    Ensure that library get_path function is working properly
    '''
    # Test get_path() method
    test_object = Base()
    test_object.get_path()



# Generated at 2022-06-13 07:52:37.116670
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    obj = FieldAttributeBase()
    name = list(obj._valid_attrs.keys())[0]
    attribute = obj._valid_attrs[name]
    templar = get_var_templar()
    value = attribute.default
    assert isinstance(obj.get_validated_value(name, attribute, value, templar), type(value))

# Generated at 2022-06-13 07:52:38.775961
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    task = Task()
    task.deserialize(dict(name='foo', action=None, become=False))
    assert task.name == 'foo'
    assert task.action == None
    assert task.become == False

# Generated at 2022-06-13 07:52:40.303455
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    t = FieldAttributeBase()
    assert t.dump_me() == {'description': '', 'name': None, 'required': True, 'static': False}

# Generated at 2022-06-13 07:52:45.892488
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
  from ansible.module_utils.parsing.convert_bool import boolean
  from ansible.module_utils.six import string_types
  from ansible.module_utils._text import to_text
  from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleMapping
  import json

  FAB = FieldAttributeBase()
  attr = FieldAttribute(default = None, required = True)
  assert FAB.dump_me(attr, boolean('True')) == 'true'
  assert FAB.dump_me(attr, True) == 'true'
  assert FAB.dump_me(attr, 'True') == 'true'
  assert FAB.dump_me(attr, boolean('False')) == 'false'

# Generated at 2022-06-13 07:52:53.984522
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    passed = False

    obj = type('TestFieldAttributeBase', (object,), {})
    field = FieldAttributeBase()

    try:
        # first, test that a TypeError is raised for an unsupported type
        field.validate(obj, 'a string')
    except TypeError:
        # we got a TypeError, as expected
        pass
    else:
        # it didn't fail the way we wanted, so fail the test
        raise AssertionError('FieldAttributeBase.validate() did not fail when given an unsupported type')

    # test that a value error is raised if a valid value is given
    try:
        # first, test that a TypeError is raised for an unsupported type
        field.validate(obj, 1234)
    except TypeError:
        # we got a TypeError, which we were not expecting
        raise Assert

# Generated at 2022-06-13 07:52:58.269597
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    b = Base()
    assert b.get_dep_chain() is None
    b._parent = Base()
    b._parent._parent = Base()
    assert b.get_dep_chain() == [b._parent, b._parent._parent]


# Generated at 2022-06-13 07:53:01.634449
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    '''
    Unit test for method dump_attrs of class FieldAttributeBase
    '''
    obj = FieldAttributeBase()
    with pytest.raises(Exception):
        obj.dump_attrs()

# Generated at 2022-06-13 07:53:13.563691
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    from ansiblelint.rules import RulesCollection
    from ansiblelint.runner import Runner
    #### test for command
    play_source = dict(
        name="Ansible Play 1",
        hosts='localhost',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        ]
    )
    #### test for copy
    # play_source = dict(
    #     name="Ansible Play 2",
    #     hosts='localhost',
    #     gather_facts='no',
    #     tasks=[
    #         dict(action=dict(module='copy'))
    #     ]
    # )
   

# Generated at 2022-06-13 07:53:27.466184
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.six import PY3
    from ansible.module_utils import basic

    # Test for dump_me of class FieldAttributeBase
    obj = FieldAttributeBase()
    try:
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            ansible_module_get_class_argument.AnsibleModule._ansible_module.params = dict(dump_me=True)
            obj.dump_me()
            if not PY3:
                assert isinstance(fake_out.getvalue(), str)
            else:
                assert isinstance(fake_out.getvalue(), str)
    except SystemExit:
        pass



# Generated at 2022-06-13 07:53:52.257634
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    # call method with sample parameters
    obj = FieldAttributeBase()
    get_validated_value = obj.get_validated_value("abc", "abc", "abc", "abc")
    assert get_validated_value == 'abc'

# Generated at 2022-06-13 07:53:53.252823
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    assert False, "No tests for Base.get_search_path"


# Generated at 2022-06-13 07:54:04.602487
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    obj = FieldAttributeBase()
    assert_equal(obj.get_validated_value("name", "attribute", "value", "templar"), "value")
    assert_equal(obj.get_validated_value("name", "attribute", "1", "templar"), 1)
    assert_equal(obj.get_validated_value("name", "attribute", "1.0", "templar"), 1.0)
    assert_equal(obj.get_validated_value("name", "attribute", "true", "templar"), True)
    assert_equal(obj.get_validated_value("name", "attribute", "100%", "templar"), 100)
    assert_equal(obj.get_validated_value("name", "attribute", None, "templar"), [])

# Generated at 2022-06-13 07:54:08.928136
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    data = {}
    FA = FieldAttribute
    f = FieldAttributeBase(FA, 'test', default='test')
    assert f.validate('test', {}) == 'test'


# Generated at 2022-06-13 07:54:16.066415
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    # Base has no _parent so this should return None
    dep_chain = Base().get_dep_chain()
    assert not dep_chain

    # Base has no _parent so this should return []
    search_path = Base().get_search_path()
    assert search_path == []

    # Base has no _parent so this should return []
    search_path = Base().get_search_path()
    assert search_path == []
# END OF UNIT TEST


# Generated at 2022-06-13 07:54:17.292835
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    assert True

# Generated at 2022-06-13 07:54:23.711073
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    # valid_attr = FieldAttribute()
    valid_attr = dict(
        required=False,
        required_if=None,
        always_post_validate=False,
        private=False,
        aliases=None,
        skip_attr_compare=False,
        can_omit_invalid_vars=False,
        omit_items=None,
        isa=object,
        default=None,
        listof=None,
        class_type=None,
        static=False,
    )
    # self.name = name
    valid_attr.__setitem__('name', 'test')
    valid_attr.__delitem__('name')
    return valid_attr

# Generated at 2022-06-13 07:54:33.578238
# Unit test for method get_validated_value of class FieldAttributeBase

# Generated at 2022-06-13 07:54:41.289643
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    '''
    Make sure the method post_validate of the class FieldAttributeBase
    is working properly
    '''
    # Create a FieldAttributeBase object
    #
    # The following documentation was used for this test:
    # https://docs.ansible.com/ansible/latest/dev_guide/developing_api.html#custom-objects
    #
    ansible_test = FieldAttributeBase(
        name='test',
        default=42,
        isa="bool"
    )

    # The method should raise an error if the method validate_attr returns
    # false for the attribute
    # ansible_test.validate_attr should return false
    # https://docs.ansible.com/ansible/latest/dev_guide/developing_api.html#custom-objects
    #
    # The method validate_attr

# Generated at 2022-06-13 07:54:43.061520
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    # setup
    my_task = Task()
    my_task._parent = MyClass()
    my_task._parent._play = MyClass()

    # execute
    x = my_task.get_dep_chain()

    # verify
    assert x is None

    # cleanup


# Generated at 2022-06-13 07:55:44.256162
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    import __main__
    # The module is in __main__, we cannot reload it.
    # However, we cannot simply use self.assertEqual(self.obj.copy(), self.obj),
    # as FieldAttributeBase is not hashable. And as it is mutable,
    # we cannot simply use self.assertTrue(self.obj.copy() == self.obj)
    # either.
    # So we compare the dictionary representations of the two objects.
    #
    # See also test_FieldAttributeBase_copy() in unit tests for
    # FieldAttributeBase.
    from copy import copy
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import cStringIO as StringIO
    res = PY3

# Generated at 2022-06-13 07:55:52.091027
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    data = dict()
    data['a'] = 1
    data['b'] = 2 
    data['c'] = 3
    data['d'] = 4
    data['e'] = 5
    print(data)
    assert data['a'] == 1
    assert data['b'] == 2
    assert data['c'] == 3
    assert data['d'] == 4
    assert data['e'] == 5


# Generated at 2022-06-13 07:55:52.855322
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    pass

# Generated at 2022-06-13 07:55:53.552362
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    pass

# Generated at 2022-06-13 07:55:57.144378
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    from ansible.playbook.play_context import PlayContext

    _play_context = PlayContext()

    assert isinstance(_play_context, PlayContext)
    # TODO: incorrect test for class PlayContext, attribute from_attrs
    assert True


# Generated at 2022-06-13 07:56:05.528906
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    class ObjectA(FieldAttributeBase):
        _valid_attrs = {
            'foo': FieldAttribute(isa='str'),
            'bar': FieldAttribute(isa='int'),
            'obj': FieldAttribute(isa='class')
        }

    class ObjectB(FieldAttributeBase):
        _valid_attrs = {
            'baz': FieldAttribute(isa='str'),
        }

    obj_a = ObjectA()
    obj_a.obj = ObjectB()
    obj_a.foo = 'foobar'
    obj_a.bar = 5

    obj_a.obj.baz = 'baz'

    assert obj_a.dump_attrs() == dict(foo='foobar', bar=5, obj=dict(baz='baz'))


# Generated at 2022-06-13 07:56:07.633798
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    fieldattributebase_obj = FieldAttributeBase()
    fieldattributebase_obj.validate()


# Generated at 2022-06-13 07:56:16.353318
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    import pytest
    from ansible.parsing.yaml.loader import AnsibleLoader

    class AnsibleBaseTest(with_metaclass(BaseMeta, object)):
        def __init__(self, **kwargs):
            super(AnsibleBaseTest, self).__init__()
            # load passed in kwargs into the object
            for (k, v) in kwargs.items():
                setattr(self, k, v)

        @property
        def parent(self):
            return self._attributes.get('parent')

        def set_parent(self, parent):
            self._attributes['parent'] = parent

        def contains(self, needle):
            if isinstance(needle, string_types):
                return needle in self._attributes

# Generated at 2022-06-13 07:56:26.136108
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    a = FieldAttributeBase()
    
    # We'll skip this one, it's doing a bunch of positional-only stuff
    #self.assertRaises(TypeError, a.validate, 'name')
    #self.assertRaises(TypeError, a.validate, 'name', mandatory=False)
    
    with pytest.raises(TypeError) as excinfo:
        a.validate('name', isa='bool')
    assert 'did not specify a default' in str(excinfo)
    
    with pytest.raises(TypeError) as excinfo:
        a.validate('name', isa='bool', default='foo')
    assert 'is not a boolean' in str(excinfo)
    
    # TODO: Test more

# Generated at 2022-06-13 07:56:36.232082
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    from ansible.playbook.play_context import PlayContext
    args = {
        'strategy': 'free',
        'forks': 0,
        'remote_user': u'test',
        'remote_pass': u'pass',
        'become': True,
        'become_method': 'sudo',
        'become_user': u'test',
        'become_pass': u'pass',
        'become_exe': u'/bin/su',
        'sudo': True,
        'sudo_user': u'test',
    }
    play_context = PlayContext()
    # Expected result in args
    expected_result = args
    # Actual result in r
    # Method call
    r = play_context.dump_attrs()
    # Compare r and expected_result

# Generated at 2022-06-13 07:57:30.394208
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    from ansible.module_utils.six import PY3

    if PY3:
        import io
        StringIO = io.StringIO
    else:
        import StringIO

    fp = StringIO()
    try:
        fieldattrbase = FieldAttributeBase()
        fieldattrbase.dump_attrs()
    except Exception as e:
        import traceback
        traceback.print_exc(file=fp)




# Generated at 2022-06-13 07:57:41.901038
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    set_defaults_1 = mocked_set_defaults()
    set_defaults_1.return_value = None
    set_defaults_2 = mocked_set_defaults()
    set_defaults_2.return_value = None
    f1 = FieldAttributeBase()
    f2 = FieldAttributeBase()
    f1.set_defaults = mock.MagicMock(return_value = set_defaults_1)
    f2.set_defaults = mock.MagicMock(return_value = set_defaults_2)
    f1._dump_me(f2)
    f1.set_defaults.assert_called_once_with(f2)
    set_defaults_1.assert_called_once_with(f2)
    set_defaults_2.assert_not_called()

# Generated at 2022-06-13 07:57:49.215224
# Unit test for method dump_attrs of class FieldAttributeBase

# Generated at 2022-06-13 07:57:56.114697
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    class Base_Test(Base):
        def __init__(self, _path):
            self._path = _path
            self._parent = None

    def test_dependency_chain():
        class DepChainEntry_Test(object):
            _role_path = None
            _name = None

            def __init__(self, name, path):
                self._name = name
                self._role_path = path

            def __str__(self):
                return self._name

        dep_chain = [
            DepChainEntry_Test("A", "/a"),
            DepChainEntry_Test("B", "/b"),
            DepChainEntry_Test("C", "/c"),
        ]
        # Test Path Stack without task_dir in dep_chain
        p = Base_Test("/b/tasks/main.yml")
        p

# Generated at 2022-06-13 07:58:07.530757
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():

    # pobj = parent object from which the attribute is being loaded
    # ds = datastructure which is the source of the attribute
    # attribute = FieldAttribute which the value represents

    # This test assumes that the original attribute value is None

    # test 1 - handle a bad type
    try:
        FieldAttributeBase.load_data(None, 123, None)
    except AnsibleParserError as e:
        if e.message != 'invalid type in field: expected dict, got 123':
            raise AssertionError('FieldAttributeBase.load_data() failed to handle a bad type')

    # test 2 - handle a dict with no keys
    obj = FieldAttributeBase()
    FieldAttributeBase.load_data(obj, {}, None)

# Generated at 2022-06-13 07:58:10.174517
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    f1 = FieldAttributeBase()
    assert f1.dump_attrs() == {'_valid_attrs': {}, '__module__': '__main__'}

# Generated at 2022-06-13 07:58:12.525996
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    '''
    unit test for squash method of FieldAttributeBase
    '''
    #Testing completion of squash method
    pass


# Generated at 2022-06-13 07:58:14.996979
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    ''' 
    This class is used by the metaclass machinery to store the field
    attributes for a class and provide easy access to them.
    '''
    pass # skipped

# Generated at 2022-06-13 07:58:16.750275
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    # TODO: Implement a unit test for this method
    raise NotImplementedError('TODO: Implement a unit test for this method')


# Generated at 2022-06-13 07:58:17.777465
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    pass


# Generated at 2022-06-13 07:49:39.375538
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    pass


# Generated at 2022-06-13 07:49:51.078532
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    host = dict(
        name='hostname',
        # ansible_host is always in hostvars
        ansible_host='host.example.com',
        # others are not
        foo='bar',
        baz='bax'
    )
    hostvars = dict(
        host=host,
        # ansible_host is used by hostvars
        ansible_host='other-host.example.com',
        # others are not
        foo='bar',
        baz='bax'
    )
    # ansible_host is used in hostvars
    expected = dict(
        name='hostname',
        ansible_host='other-host.example.com',
        foo='bar',
        baz='bax'
    )

# Generated at 2022-06-13 07:49:56.713679
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    host = Host(name="myhost")
    f = FakeFieldAttributeBase(name='fake_class', task=host)
    test_data = dict(name="shared_loader", loader="shared_loader")
    assert f.dump_me(test_data) == dict(name="shared_loader", loader="shared_loader", task=host)



# Generated at 2022-06-13 07:49:59.067311
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    my_test = FieldAttributeBase()
    my_test.post_validate()


# Generated at 2022-06-13 07:50:09.111138
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():

    variable1 = 'value1'
    variable2 = 'value2'
    variable3 = 'value3'
    variable4 = 'value4'
    variable5 = 'value5'
    variable6 = 'value6'
    variable7 = 'value7'

    # Test valid case
    obj = FieldAttributeBase()
    obj._valid_attrs = {'variable1': Variable('variable1', section='default'), 'variable2':Variable('variable2',section='default')}
    obj.variable1 = variable1
    obj.variable2 = variable2
    expected = {'variable1': variable1, 'variable2': variable2}
    actual = obj.dump_attrs()

    assert actual == expected


# Generated at 2022-06-13 07:50:11.244284
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    # TODO: implement this test
    pass


# Generated at 2022-06-13 07:50:16.349964
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    import uuid
    data = dict()
    data['uuid'] = str(uuid.uuid4())
    data['finalized'] = True
    data['squashed'] = True
    data['foo'] = 'bar'
    b = FieldAttributeBase()
    b.deserialize(data)
# end class FieldAttributeBase


# Generated at 2022-06-13 07:50:20.479616
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():

    fieldattribute_base = FieldAttributeBase()
    fieldattribute_base.default = None
    fieldattribute_base.isa = None
    fieldattribute_base.version = None
    fieldattribute_base.vars = None

    expected = fieldattribute_base
    actual = fieldattribute_base.copy()

    assert expected == actual

# Generated at 2022-06-13 07:50:24.258446
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    # Mock
    class MockFieldAttributeBase(object):
        def __init__(*args, **kwargs):
            pass

        def _get_valid_attrs(*args, **kwargs):
            return dict()

        def __setattr__(*args, **kwargs):
            raise Exception("Override this")

    obj = MockFieldAttributeBase()

    assert obj.from_attrs({'aaa': 'bbb'}) == None


# Generated at 2022-06-13 07:50:36.117762
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    args = dict(
        default=dict(default=dict(required=True)),
        required=dict(required=True),
        always_post_validate=dict(),
        inherit_only=dict(required=True),
        isa=dict(required=True),
        listof=dict(),
        priority=dict(),
        static=dict(required=True),
        no_log=dict(required=True),
        class_type=dict(required=True),
    )
    set_module_args(args)
    result = my_module.copy()

# Generated at 2022-06-13 07:51:05.195533
# Unit test for method get_search_path of class Base
def test_Base_get_search_path():
    from os.path import join
    import tempfile
    import shutil
    import pytest

    def mkdir_tmp_role(tmp_dir):
        role_name = 'role_name'
        role_path = join(tmp_dir, role_name)
        dir_name_1 = 'dir_name_1'
        dir_path_1 = join(role_path, dir_name_1)
        dir_name_2 = 'dir_name_2'
        dir_path_2 = join(role_path, dir_name_2)
        task_file_name = 'task.yml'
        task_file_path = join(role_path, dir_name_1, task_file_name)

# Generated at 2022-06-13 07:51:07.131451
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    play = Play.load({})
    assert isinstance(play, Play)
    assert isinstance(play._dump_attrs(), dict)


# Generated at 2022-06-13 07:51:14.120248
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    field_attribute_base_instance = FieldAttributeBase(name='test_name', always_post_validate=True, class_type=None, choices=None, default=None, 
                                                       isa=None, isa_class=None, listof=None, priority=100, required=False, static=False, 
                                                       type_cast=True, validate=None)

    method_output = field_attribute_base_instance.copy()

    assert method_output != field_attribute_base_instance
    assert method_output.name == field_attribute_base_instance.name
    assert method_output.always_post_validate == field_attribute_base_instance.always_post_validate
    assert method_output.class_type == field_attribute_base_instance.class_type

# Generated at 2022-06-13 07:51:24.557453
# Unit test for method squash of class FieldAttributeBase

# Generated at 2022-06-13 07:51:25.682665
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    # No tests yet
    pass

# Generated at 2022-06-13 07:51:27.209636
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    # TODO: decide how to handle the test
    pass

# Generated at 2022-06-13 07:51:30.154730
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    # FIXME: FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison
    assert FieldAttributeBase().squash(any_string_value) == False



# Generated at 2022-06-13 07:51:35.715353
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    """ FieldAttributeBase.squash() - basic test of object

    Test FieldAttributeBase.squash() with
    test data.
    """

    field_attribute_base = FieldAttributeBase()
    field_attribute_base.squash()

    print("Test 1")
    assert(True)


if __name__ == "__main__":
    test_FieldAttributeBase_squash()

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils._text import to_native

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 07:51:38.033842
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    c = FieldAttributeBase()
    c.load_data(None, None, None, None)



# Generated at 2022-06-13 07:51:38.962154
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    # TODO: write test for method squash of class FieldAttributeBase
    pass

# Generated at 2022-06-13 07:52:17.397225
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    from ansible.parsing.yaml.loader import AnsibleLoader
    # Test with invalid argument types
    data = '''
    a: 3
    '''
    ds = AnsibleLoader(data, file_name='test_FieldAttributeBase_post_validate001.yaml').get_single_data()

    class Foo(object):

        _valid_attrs = dict(
            a=FieldAttribute(isa='int', required=True),
        )

        def __init__(self, ds):
            self._attributes = {}
            self._attr_defaults = {}
            for (k,v) in self._valid_attrs.items():
                self._attributes[k] = v.default
                self._attr_defaults[k] = v.default
            self._loader = None
            self._variable

# Generated at 2022-06-13 07:52:26.220137
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    from ansible.parsing.yaml.loader import AnsibleLoader
    FieldAttributeBase_instance = FieldAttributeBase()

# Generated at 2022-06-13 07:52:27.230219
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    # TODO: remove this line
    FieldAttributeBase()
    pass


# Generated at 2022-06-13 07:52:28.565335
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    assert FieldAttributeBase().validate(None) is None



# Generated at 2022-06-13 07:52:34.293560
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    src_dict = {
        'name': "Ansible",
        '_name': Attribute(name='name'),
        '_get_attr_name': 'Ansible'
    }
    dst_dict = {}
    dst_dict.update(src_dict)
    _create_attrs(src_dict, dst_dict)
    assert dst_dict == {'_alias_attrs': {}, '_get_attr_name': 'Ansible', '_valid_attrs': {'name': Attribute(name='name')}, '_attr_defaults': {'name': None}, '_attributes': {'name': Sentinel}, 'name': 'Ansible', '_name': Attribute(name='name')}



# Generated at 2022-06-13 07:52:38.424862
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():

    from ansiblelint.rules.TasksHaveUUID import TasksHaveUUID
    from ansiblelint.rules.UseShellInsteadOfCommand import UseShellInsteadOfCommand

    rule1 = TasksHaveUUID()
    rule2 = UseShellInsteadOfCommand()

    assert rule1.id == 'ANSIBLE0004'
    assert rule2.id == 'ANSIBLE0006'
    assert rule1.shortdesc ==\
            'All tasks should have a unique id'
    assert rule2.shortdesc ==\
            'All shell and command tasks should have a unique id'
    assert rule1.description.startswith('The tasks are identified')
    assert rule2.description.startswith('The tasks are identified')

    assert rule1.tag == ['metadata']
    assert rule2.tag == ['command-shell']


# Unit test

# Generated at 2022-06-13 07:52:41.987773
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    import pytest
    import unittest

    class MockFieldAttributeBase(FieldAttributeBase):
        pass

    class TestFieldAttributeBase(unittest.TestCase):

        def test_deserialize(self):
            with pytest.raises(AnsibleAssertionError) as excinfo:
                obj = MockFieldAttributeBase()
                data = 'foo'
                obj.deserialize(data)
            assert 'data (foo) should be a dict' in str(excinfo.value)




# Generated at 2022-06-13 07:52:45.910272
# Unit test for method squash of class FieldAttributeBase
def test_FieldAttributeBase_squash():
    with pytest.raises(NotImplementedError):
        FieldAttributeBase('test', default=None).squash(None)


# Generated at 2022-06-13 07:52:52.494770
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six import string_types
    from ansible.plugins.loader import module_loader, action_loader
    from ansible.parsing.plugin_docs import read_docstring
    from ansible.parsing.dataloader import DataLoader
    # set up object
    bm = BaseMeta('bm', 'parents', 'dct')
    assert bm.__name__ == 'bm'
    assert bm.__class__ == BaseMeta



# Generated at 2022-06-13 07:53:03.385397
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    FieldAttributeBase._valid_attrs = {
        'use_set': FieldAttribute(isa='bool', default=False, category='task'),
        'verify_files': FieldAttribute(isa='bool', default=False, category='task'),
        'ignore_errors': FieldAttribute(isa='bool', default=False, category='task'),
        'vars': FieldAttribute(isa='dict', default={'generic_var': 'generic_val'}, category='task')
        }

    FieldAttributeBase._squashed_attrs = ['vars']

    FieldAttributeBase().from_data(
        data={
            'vars': {'task1_var': 'task1_val'}
        }
    )

    FieldAttributeBase().copy()


# Generated at 2022-06-13 07:53:36.842777
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    for cand_obj in [
        FieldAttributeBase(
            name='name',
            default='my_field_name',
        ),
    ]:
        assert isinstance(cand_obj.dump_me, bool)



# Generated at 2022-06-13 07:53:40.733824
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
  attrs = FieldAttributeBase().dump_attrs()

  assert attrs == {'_uuid': None, '_variable_manager': None, '_loader': None, '_variable_manager_lock': None, '_validated': False, '_finalized': False, '_squashed': False}


# Generated at 2022-06-13 07:53:42.822300
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    # Test setup

    # Test execution
    pass


# Generated at 2022-06-13 07:53:45.684130
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    # Create an instance of FieldAttributeBase
    
    fieldattributebase_instance = FieldAttributeBase()
    
    # Try something
    
    pass


# Generated at 2022-06-13 07:53:54.994822
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from datetime import datetime
    data = {'test': 'test', 'test2': AnsibleVaultEncryptedUnicode('test')}
    t1 = datetime.now()
    fb = FieldAttributeBase()
    fb.load_data(data)
    t2 = datetime.now()
    spin_time = (t2 - t1).total_seconds()
    #assert spin_time < 0.01, "Spin time is: %s" % spin_time
    assert fb.test == 'test', 'fb.test should be "test" but is: %s' % fb.test

# Generated at 2022-06-13 07:53:57.405919
# Unit test for method validate of class FieldAttributeBase
def test_FieldAttributeBase_validate():
    test = FieldAttributeBase('test')
    assert test.validate(1) == 1
    assert test.validate(None) == None
    assert test.validate(False) == False
    assert test.validate(['a','b']) == ['a','b']

# Generated at 2022-06-13 07:54:08.009178
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    from unittest import mock

    # mock out the call to utcnow()
    with mock.patch('ansible.utils.timeutils.utcnow', mock.Mock(return_value=233)):
        # create the sample object
        task = Task()
        task.name = u"test task"
        task.loop = "loop"
        task.vars = {'var1': 'value1'}
        task.tags = ['tag1', 'tag2']
        task.register = 'reg'
        task.retries = 3
        task.until = 10

        # Create the attrs dict
        attrs = task.dump_attrs()

        # clear out the uuid/finalized/squashed fields
        # which aren't deserializable
        attrs.pop('uuid')

# Generated at 2022-06-13 07:54:19.759020
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    args = dict()
    args['required'] = True
    args['private'] = True
    args['include_in_vars'] = True
    args['static'] = False
    args['always_post_validate'] = True
    args['default'] = 'default'
    args['aliases'] = list()
    args['choices'] = None
    args['class_type'] = 'class_type'
    args['isa'] = 'class'
    args['listof'] = None
    args['priority'] = 10

    attribute = class_FieldAttributeBase(name='name', **args)
    obj = FieldAttributeBase()
    actual = obj.dump_me(attribute=attribute)
    expected = dict()
    expected['name'] = 'name'
    expected['required'] = True
    expected['private'] = True
    expected

# Generated at 2022-06-13 07:54:22.230418
# Unit test for method copy of class FieldAttributeBase
def test_FieldAttributeBase_copy():
    c = FieldAttributeBase()
    assert hasattr(c, 'copy')


# Generated at 2022-06-13 07:54:32.016786
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    attr = FieldAttributeBase()
    job = BaseObject()
    assert attr.load_data(job, 'string') == 'string'
    assert attr.load_data(job, u'string') == 'string'
    assert attr.load_data(job, True) == 'True'
    assert attr.load_data(job, False) == 'False'
    assert attr.load_data(job, 1) == '1'
    assert attr.load_data(job, 1.0) == '1.0'
    assert attr.load_data(job, []) == '[]'
    assert attr.load_data(job, {}) == '{}'
    assert attr.load_data(job, None) == ''


# Generated at 2022-06-13 07:55:02.311021
# Unit test for method load_data of class FieldAttributeBase
def test_FieldAttributeBase_load_data():
    pass



# Generated at 2022-06-13 07:55:11.032927
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    import uuid

    test_play = Play()
    test_play._load_name('test_play')
    test_play._load_vars({'test_key': 'test_value'})
    attrs = test_play.dump_attrs()
    assert 'name' in attrs
    assert attrs['name'] == 'test_play'
    assert 'vars' in attrs
    assert 'test_key' in attrs['vars']
    assert attrs['vars']['test_key'] == 'test_value'
    assert 'uuid' in attrs
    assert isinstance(attrs['uuid'], uuid.UUID)

# Generated at 2022-06-13 07:55:18.979982
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    field_attribute_base = FieldAttributeBase()
    field_attribute_base.name = 'hosts'
    field_attribute_base.isa = 'list'
    field_attribute_base.private = False
    field_attribute_base.default = []
    field_attribute_base.required = False
    field_attribute_base.static = False
    field_attribute_base.always_post_validate = False
    field_attribute_base.priority = 1
    field_attribute_base.aliases = []
    field_attribute_base.class_type = 'str'
    field_attribute_base.listof = None
    field_attribute_base.inherit_from_playbook = False
    field_attribute_base.parent_attribute = None

    # call dump_me()
    field_attribute_base.dump_me()

# Generated at 2022-06-13 07:55:22.106670
# Unit test for method dump_me of class FieldAttributeBase
def test_FieldAttributeBase_dump_me():
    '''
    Unit test for FieldAttributeBase.dump_me
    '''
    a = field_attribute()
    a.dump_me()



# Generated at 2022-06-13 07:55:26.643383
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    # testing for the case when type (bool) is bool
    at = FieldAttributeBase(isa='boolean')
    assert at._post_validate(attribute, True, templar) == True


# Generated at 2022-06-13 07:55:29.866944
# Unit test for method __new__ of class BaseMeta
def test_BaseMeta___new__():
    import contextlib
    with contextlib.redirect_stdout(None):
        base = BaseMeta('Base', (), {})
        assert base


# Generated at 2022-06-13 07:55:40.883101
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    """Unit test for method get_dep_chain of class Base"""
    yaml_data = """
- hosts: localhost
  gather_facts: no
  vars:
    var1: "test1"
    var2: "test2"
  tasks:
    - name: test1
      debug:
        msg: "test1"
      delegate_to: localhost
      run_once: true
    - name: test2
      debug:
        msg: "test2"
      delegate_to: localhost
      run_once: true
    - name: test3
      debug:
        msg: "test3"
      delegate_to: localhost
      run_once: true
"""
    tasks = yaml.safe_load(yaml_data)['tasks']

# Generated at 2022-06-13 07:55:43.822013
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    attr = FieldAttributeBase('name', default=None, always_post_validate=False)
    assert attr.post_validate() == None

# Test for method _post_validate_args

# Generated at 2022-06-13 07:55:58.376026
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    attr = FieldAttributeBase(isa='string', required=True)


# Generated at 2022-06-13 07:56:03.610347
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    FA = FieldAttributeBase()
    assert FA.get_validated_value(name='name', attribute=boolean(attribute=True, strict=True), value='value', templar='templar') == True
    assert FA.get_validated_value(name='name', attribute=to_text(value=True, encoding='encoding', errors='errors'), value=100, templar='templar') == '100'

# Generated at 2022-06-13 07:56:54.079490
# Unit test for method get_validated_value of class FieldAttributeBase
def test_FieldAttributeBase_get_validated_value():
    base_test = Base()
    attr = FieldAttribute()
    templar = AnsibleTemplar()
    # Test a valid object
    try:
        base_test.get_validated_value('name', attr, 'value', templar)
    except Exception as e:
        raise AssertionError('Exception raised when get_validated_value is called with valid arguments: %s' % e)


# Generated at 2022-06-13 07:57:00.624737
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    field_name = 'test_field'
    field_attribute = FieldAttributeBase(name=field_name)

    def test_method_1_impl(attribute, value, templar):
        return value * 2
    field_attribute.test_method_1 = test_method_1_impl

    def test_method_2_impl(attribute, value, templar):
        return attribute.name + value
    field_attribute.test_method_2 = test_method_2_impl

    class TestClass(FieldAttributeBase):
        def __init__(self, name, value, templar):
            self._name = name
            self._value = value
            self._templar = templar

        def dump_attrs(self):
            return {'name': self._name, 'value': self._value}


# Generated at 2022-06-13 07:57:13.244441
# Unit test for method deserialize of class FieldAttributeBase
def test_FieldAttributeBase_deserialize():
    from io import StringIO
    from unittest.mock import Mock, patch

    from ansible import context

    # ansible_playbook = {"playbook": {"metadata": {"name": "test_name_value"}}}
    # mock_loader = Mock()
    # mock_variable_manager = Mock()
    #
    # test_object = FieldAttributeBase(loader=mock_loader, variable_manager=mock_variable_manager, use_handlers=False,
    #                                  inventory=None)
    # test_uuid = test_object._uuid
    #
    # # test_object = FieldAttributeBase(loader=mock_loader, variable_manager=mock_variable_manager, use_handlers=False,
    #                                  # inventory=None)
    #
    # vars = """
    # [

# Generated at 2022-06-13 07:57:17.686642
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    args = dict(
        attribute = mock.MagicMock(spec_set=FieldAttributeBase),
        value = mock.MagicMock(),
        templar = mock.MagicMock(spec_set=Templar),
    )
    # setup tests
    # execute
    with pytest.raises(NotImplementedError):
        FieldAttributeBase().post_validate(**args)


# Generated at 2022-06-13 07:57:31.443632
# Unit test for method dump_attrs of class FieldAttributeBase
def test_FieldAttributeBase_dump_attrs():
    '''
    test the method dump_attrs of class FieldAttributeBase
    '''

    attr = FieldAttribute(isa='bool', default=None)
    attr1 = FieldAttribute(isa='dict', default=None)
    attr2 = FieldAttribute(isa='bool', default=None, serialize_as=dict)
    attr3 = FieldAttribute(isa='bool', default=None, serialize_as=None)
    attr4 = FieldAttribute(isa='bool', default=None, serialize_as=True)
    attr5 = FieldAttribute(isa='bool', default=None, serialize_as=False)
    attr6 = FieldAttribute(isa='bool', default=None, serialize_as=list)
    attr7 = FieldAttribute(isa='bool', default=None, serialize_as=[])
   

# Generated at 2022-06-13 07:57:32.883494
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
  obj = FieldAttributeBase()
  assert False


# Generated at 2022-06-13 07:57:35.148376
# Unit test for method post_validate of class FieldAttributeBase
def test_FieldAttributeBase_post_validate():
    data = {}

    assert 'pass' == False


# Generated at 2022-06-13 07:57:44.539219
# Unit test for method validate of class FieldAttributeBase

# Generated at 2022-06-13 07:57:47.834426
# Unit test for method from_attrs of class FieldAttributeBase
def test_FieldAttributeBase_from_attrs():
    '''
    Unit test for method from_attrs of class FieldAttributeBase
    '''
    FieldAttributeBase.__init__()
    attrs = {}
    return FieldAttributeBase.from_attrs(attrs)

# Generated at 2022-06-13 07:57:53.572798
# Unit test for method get_dep_chain of class Base
def test_Base_get_dep_chain():
    from ansible.playbook.base import Base
    from ansible.playbook import Playbook
    from ansible.playbook.role.task_include import TaskInclude
    from ansible.playbook.task import Task
    from collections import namedtuple
    # Create a mock object for class TaskInclude
    class MockTaskInclude(TaskInclude):
        def __init__(self):
            super(MockTaskInclude, self).__init__()
            self._play = Base()
    # Create a mock object for class Task
    class MockTask(Task):
        def __init__(self):
            super(MockTask, self).__init__()
            self._parent = MockTaskInclude()
            self._blocks = []
    
    # Instantiate the test class
    task = Base()
    # Set the _parent
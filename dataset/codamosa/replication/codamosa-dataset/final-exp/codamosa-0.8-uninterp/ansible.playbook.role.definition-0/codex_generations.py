

# Generated at 2022-06-13 08:41:53.920799
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    class P(object):
        def __init__(self, name):
            self._name = name
        def get_name(self):
            return self._name

    play = P('play_name')
    variable_manager = None
    loader = None

    role_basedir = 'roles'
    role_name1 = 'role1'
    role_params1 = dict()

    role_def1 = dict(role=role_name1)
    rd1 = RoleDefinition(play=play, role_basedir=role_basedir, variable_manager=variable_manager, loader=loader)
    rd1.preprocess_data(role_def1)
    assert rd1.get_name() == role_name1

    role_name = role_name1
    role_path = 'roles/role1'


# Generated at 2022-06-13 08:42:05.985385
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from collections import namedtuple

    from ansible import constants as C

    from ansible.errors import AnsibleError
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.utils.vars import combine_vars

    # fake up some options for the _variable_manager

# Generated at 2022-06-13 08:42:14.898186
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.role.include import RoleInclude
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar

    variable_manager = VariableManager()
    loader = DataLoader()

    # 1. Case: RoleDefinition with name
    #
    # data:
    #   - role: myrole
    #     forks: 5
    #     vars:
    #       - varA: valueA
    #       - varB: valueB

    data = dict(
        role="myrole",
        forks=5,
        vars=dict(
            varA="valueA",
            varB="valueB"
        )
    )

    # create a templar class to template the dependency names, in
    # case they

# Generated at 2022-06-13 08:42:24.848947
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.module_utils._text import to_bytes

    data = '''
    ---
    - hosts: local
      tasks:
        - role:
            name: myrole
            tasks_from: main.yml
            other: thing
    ...
    '''

    loader = DataLoader()
    data = loader.load(to_bytes(data))

    display.debug(data)

    role_def = RoleDefinition()
    role_def.preprocess_data(data['plays'][0]['tasks'][0]['role'])

    assert role_def._role_params['other'] == 'thing'
    assert role_def.role == 'myrole'
    assert role_def._role_path == 'myrole'

# Generated at 2022-06-13 08:42:31.471999
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.module_utils.six import BytesIO

    role_definition = RoleDefinition()

    role_name = {"role": "testrole"}
    role_name_expect = {"role": "testrole"}

    role_path = {'role': 'testrole/'}
    role_path_expect = {'role': 'testrole/'}

    role_path_templated = {'role': 'testrole/{{myvar}}'}
    role_path_templated_expect = {'role': 'testrole/{{myvar}}'}


# Generated at 2022-06-13 08:42:42.348668
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import os
    from ansible.playbook.base import Base

    basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    base = Base.load(dict(
        name='mock',
        hosts=['localhost'],
        roles=['foobar']
    ), loader=None)
    role = RoleDefinition.load(dict(
        role=dict(name='foobar', from_server='foo.bar', foo='bar')
    ), variable_manager=None, loader=None)

    ds = role.preprocess_data(role._ds)
    assert ds.get('role') == 'foobar', 'role name should be foobar'

# Generated at 2022-06-13 08:42:55.226599
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    host_vars = {
        "all": {
            "var1": "v1",
            "var2": "v2"
        }
    }
    play_context = PlayContext()
    loader = DataLoader()
    vars_manager = None

    def _get_basedir(self):
        return os.path.join(loader.get_basedir(), 'roles')

    def _path_exists(self, path):
        return True

    loader._get_basedir = _get_basedir
    loader._path_exists = _path_exists
    vars_manager = None


# Generated at 2022-06-13 08:43:07.354227
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    # Test syntax of role definition
    role_def_dict = {'role': 'foobar'}
    role_def = RoleDefinition(play=None, role_basedir=None, variable_manager=None, loader=None, collection_list=None)
    role_def = role_def.load_from_file(None, role_def_dict)
    assert(role_def.role == 'foobar')
    assert(role_def.get_name() == 'foobar')

    # Test syntax of role definition with a collection
    role_def_dict = {'role': 'foo.bar.baz'}
    role_def = RoleDefinition(play=None, role_basedir=None, variable_manager=None, loader=None, collection_list=['foo.bar'])
    role_def = role_def.load_

# Generated at 2022-06-13 08:43:17.696809
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    """
    test preprocess_data of class RoleDefinition
    """
    role_name = 'remote_role'
    role_path = 'remote_role_path'
    role_params = {'tags': 'all'}
    role_def = AnsibleMapping(role=role_name, **role_params)
    role_def.ansible_pos = None

    class test_play():
        def __init__(self):
            self.name = 'test_play'

    class test_loader():
        def __init__(self):
            self.basedir = '.'
            self.path_exists_called = False

        def path_exists(self, path):
            self.path_exists_called = True
            return True

    class test_vm():
        def __init__(self):
            self

# Generated at 2022-06-13 08:43:27.293230
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # The exception was happening because role_params was being
    # accessed as an ordinal argument, but it wasn't defined as an
    # attribute of the RoleDefinition class. Adding it fixed the
    # exception, but that just revealed that the code was trying to
    # access the key 'role' in a dictionary that didn't exist.

    # the test here is just to make sure that we don't get an
    # unhandled exception when the code tries to access 'role_params'
    rd = RoleDefinition(role_basedir=None)
    try:
        rd.preprocess_data({})
    except:
        assert False

# Generated at 2022-06-13 08:43:39.798836
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # Create a Templar object used to template names. This is required to
    # instantiate the RoleDefinition object.
    vars = dict()
    templar = Templar(loader=None, variables=vars)

    # Test 1: Load a simple role directly from file
    role_definition = RoleDefinition(
        play=None,
        role_basedir='/tmp',
        variable_manager=None,
        loader=None,
        collection_list=[],
    )
    role_definition._loader.path_exists = lambda path: True
    role_definition._loader.get_basedir = lambda: '/tmp'

# Generated at 2022-06-13 08:43:54.553241
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    class BogusRoleDefinition(RoleDefinition):
        def __init__(self):
            super(BogusRoleDefinition, self).__init__()
            self._attributes = Attribute()
            self._attributes['role'] = 'myrole'
            self._role_collection = 'mycollection'
    test1 = BogusRoleDefinition()
    assert 'mycollection.myrole' == test1.get_name(True)
    assert 'myrole' == test1.get_name(False)
    test2 = BogusRoleDefinition()
    test2._attributes['role'] = 'myrole'
    test2._role_collection = None
    assert 'myrole' == test2.get_name(True)
    assert 'myrole' == test2.get_name(False)
    test3 = BogusRoleDefinition()
   

# Generated at 2022-06-13 08:44:05.467352
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    #from ansible.playbook.role_definition import RoleDefinition
    r = RoleDefinition()
    # passing data structure with just role name
    role_def_1 = { 'role': 'apache'}
    assert r.preprocess_data(role_def_1) == {'role': 'apache'}
    # passing data structure with role name and additional parameters
    role_def_2 = { 'role': 'apache', 'some_param': 'values'}
    assert r.preprocess_data(role_def_2) == {'role': 'apache'}
    assert r.get_role_params() == {'some_param': 'values'}
    # passing data structure with name only instead of role
    role_def_3 = { 'name': 'apache'}

# Generated at 2022-06-13 08:44:17.468684
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import shutil
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    C.DEFAULT_ROLES_PATH = '/usr/local/etc/ansible/roles'

    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    loader = AnsibleLoader(None, True, None, None)

    play_path = 'playbooks/test_playbook_with_roles.yml'
    play_path = os.path.join(parent_dir, play_path)
    data = loader.load_from_file(play_path)

# Generated at 2022-06-13 08:44:26.467432
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleUnicode

    # Simple dict, role name is 'test', but role path is /tmp/foo/bar/test,
    # so role_name should be set to 'test' and role_path should be set to /tmp/foo/bar/test
    data = dict(
        role='test',
        tasks=[
            dict(action=dict(module='debug', args=dict(msg='{{message}}')),
                 with_items=['{{items}}'],
                 _line=1),
        ],
        vars=dict(message='Hello, World!', items=['one', 'two', 'three']),
        _line=1,
    )
    # Mocking

# Generated at 2022-06-13 08:44:37.626623
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():

    role_def = RoleDefinition()
    role_def.role = 'my_role'

    assert role_def.get_name() == 'my_role'
    assert '.'.join(role_def.get_name().split('.')[-2:]) == 'my_role'
    assert role_def.get_name(include_role_fqcn=False) == 'my_role'
    assert role_def.get_name(include_role_fqcn=True) == 'my_role'

    from ansible.collection.collection_loader import get_collection_role_spec
    role_def._role_collection = 'my_namespace.my_repo'
    role_spec = get_collection_role_spec('my_namespace.my_repo.my_role')
    role_def._role_collection

# Generated at 2022-06-13 08:44:49.079253
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import os
    import sys
    import unittest
    from ansible.playbook.role_include import RoleInclude

    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import module_loader
    from ansible.plugins.loader import lookup_loader
    from ansible.errors import AnsibleError

    from ansible.template import Templar
    from ansible.utils.display import Display

    from ansible.vars.manager import VariableManager

    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import RoleDefinition

    class TestRoleInclude(RoleInclude):
        _base_role_class = Role


# Generated at 2022-06-13 08:44:56.115736
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    rd = RoleDefinition()
    assert not rd.get_name(), "get_name should return empty string if role is not set"
    rd.role = "rolename"
    assert rd.get_name() == "rolename", "get_name should return role name"
    rd.role_collection = "galaxy_namespace"
    assert rd.get_name() == "galaxy_namespace.rolename", "get_name should return role namespace and name"

# Generated at 2022-06-13 08:45:02.389769
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    result = RoleDefinition.load({'role': 'name'}, variable_manager=None)
    result._load_role_name = Mock(return_value='name')
    result._load_role_path = Mock(return_value=('name', 'role_path'))
    result._split_role_params = Mock(return_value=(dict(), dict()))
    result.preprocess_data({'role': 'name'})

    assert result._ds == {'role': 'name'}
    assert result._role_path == 'role_path'
    assert result._role_params == dict()


# Generated at 2022-06-13 08:45:09.499173
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.utils.vars import combine_vars

    loader = AnsibleLoader(None, {"option1": "value1"}, 'test_preprocess_data')
    variable_manager = VariableManager()
    variable_manager.set_nonpersistent_facts({"option2": "value2"})
    variable_manager.extra_vars = combine_vars(loader=loader, variables=variable_manager.get_vars(play=None))
    variable_manager.set_inventory(loader.inventory)

    # Test 1: Create a RoleDefinition object with invalid type
    #         of data structure
    role_

# Generated at 2022-06-13 08:45:23.215032
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.plugins.loader import role_loader
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.unsafe_proxy import wrap_var

    role_name = 'roles/foo'
    role_name_obj = AnsibleUnicode(role_name)
    role_name_obj.ansible_pos = role_name

    role_prefix = 'roles'
    role_prefix_obj = AnsibleUnicode(role_prefix)
    role_prefix_obj.ansible_pos = role_prefix

    role_prefix_proxy = wrap_var(role_prefix)

    role_name_proxy = wrap_var(role_name)

   

# Generated at 2022-06-13 08:45:35.183212
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    rd = RoleDefinition()
    assert 'test_role' == rd.get_name(include_role_fqcn=False)
    rd.role_collection = 'test_collection'
    assert 'test_collection.test_role' == rd.get_name(include_role_fqcn=True)
    rd.role = 'test_role'
    assert 'test_role' == rd.get_name(include_role_fqcn=False)
    assert 'test_collection.test_role' == rd.get_name(include_role_fqcn=True)
    assert 'test_collection.test_role' == rd.get_name(include_role_fqcn=None)

# Generated at 2022-06-13 08:45:47.335820
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.callback import CallbackBase

    # make sure we're using C.DEFAULT_ROLES_PATH
    C.DEFAULT_ROLES_PATH = '/tmp/role_test'

    # create a play with the role definition
    role_def = dict(
        role='role1',
        other_key='value',
        second_key='value2',
    )
    roles

# Generated at 2022-06-13 08:45:55.631247
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Without name:
    result = RoleDefinition.load({'role': 'common'}, None, None).preprocess_data({'role': 'common'})
    assert result['role'] == 'common'

    # With name:
    result = RoleDefinition.load({'role': 'common'}, None, None).preprocess_data({'name': 'common'})
    assert result['role'] == 'common'

    # If the role is a file name (relative or absolute) the role name will include the entire path
    result = RoleDefinition.load({'role': 'common'}, None, None).preprocess_data('/tmp/common')
    assert result['role'] == '/tmp/common'

    # If the role is a directory name (relative or absolute) the role name will include the directory name

# Generated at 2022-06-13 08:45:59.957767
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Test will check passing a simple string as data
    # Define fake empty play to use in tests
    fake_play = {}
    # Test will check passing a simple string as data
    data = 'role_name'
    p = RoleDefinition(play=fake_play, loader = None)
    assert p.preprocess_data(data) == {'role': 'role_name'}
    # Test will check passing a simple string with a variable as data
    data = 'role${index}'
    p = RoleDefinition(play=fake_play, loader = None)
    assert p.preprocess_data(data) == {'role': 'role${index}'}
    # Test will check passing a dict with a role key as data
    # Define fake empty play to use in tests
    fake_play = {}
    # Test will check passing a

# Generated at 2022-06-13 08:46:13.656626
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    dict_role_def_with_role_fqcn = {
        'role': 'test_role',
        'aio_role_path': '/path/to/role/test_role',
        'collection': 'test_collection',
    }
    role_definition = RoleDefinition(
        role_basedir='/path/to/role',
        variable_manager=None,
        loader=None,
        collection_list=[],
    )
    role_definition._ds = dict_role_def_with_role_fqcn
    role_definition.role = dict_role_def_with_role_fqcn['role']
    role_definition._role_collection = dict_role_def_with_role_fqcn['collection']
    assert role_definition.get_name(include_role_fqcn=True)

# Generated at 2022-06-13 08:46:22.218402
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    '''
    Tests for function RoleDefinition._preprocess_data
    '''
    from ansible.playbook.base import base_datastructure

    def get_data(data, attribute_class=Attribute, loader=None, variable_manager=None, role_basedir=None, collection_list=None):
        '''
        Returns the data of the _ds attribute of the RoleDefinition object after it has been processed
        in preprocess_data() function
        '''
        rd = RoleDefinition(variable_manager=variable_manager, loader=loader, role_basedir=role_basedir, collection_list=collection_list)
        data = rd.preprocess_data(data)
        return data._ds

    # role definition as an empty string
    loader = base_datastructure()
    data = ''
    r = get_data

# Generated at 2022-06-13 08:46:33.504212
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    # Use a random yaml file for the data source
    loader = DictDataLoader({'test.yml': """
---
- hosts: all
  tasks:
  - debug: msg="hello world"
    args: {arg1:value1, arg2:value2}
  - include: role1 role2 role3
"""})

    class TestRoleDefintion(RoleDefinition):
        _valid_attrs = frozenset(('testattr',))

    # TODO: replace this with a 'mock' object
    class TestPlay(Base):
        def __init__(self, loader, variable_manager=None):
            self._loader = loader
            self._variable_manager = variable_manager

    class TestVariableManager(Attribute):
        def get_vars(self):
            return dict(var1=1)

   

# Generated at 2022-06-13 08:46:44.994846
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    yaml_text = """
---
- hosts: all
  roles:
    - localhost:role_name
  vars:
    port: 8080
    protocol: http
    user: root
    password: root
    timeout: 5
  environment:
    SOME_VAR: {{ some_env_var }}
"""
    play_ds = AnsibleLoader(yaml_text, file_name=None).get_single_data()

    play = Play.load(play_ds, variable_manager=None, loader=None)

    role_ds = play_ds[0]['roles'][0]
    role_def = RoleDefinition

# Generated at 2022-06-13 08:46:58.387987
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    def _get_variable_manager(vars=None):
        return FieldAttribute(isa='string', private=True, default=vars)

    def _get_loader():
        return FieldAttribute(isa='string', private=True, default='loader')

    yaml_object = AnsibleBaseYAMLObject({'role': 'test_role', 'option': 'option_value'})

    # Data is a dictonary where role has value of type string and there are options
    role_def = RoleDefinition()
    role_def.preprocess_data(yaml_object)
    assert role_def._role_params == {'option': 'option_value'}
    assert role_def._role_path == 'loader/roles/test_role'
    assert role_def._role == 'test_role'

    # Data is a dict

# Generated at 2022-06-13 08:47:11.020670
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_def = RoleDefinition(role_basedir='/foo/bar')
    role_def._role_collection = 'foo'
    role_def._role = 'bar'
    assert role_def.get_name() == 'foo.bar'

# Generated at 2022-06-13 08:47:22.969517
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    def _remove_roles_path_from_env():
        import os
        import warnings
        env_val = os.environ.pop('ANSIBLE_ROLES_PATH', None)
        if env_val is not None:
            warnings.warn('Test cleanup: ANSIBLE_ROLES_PATH environment variable set, but should not be set')

    class LoaderModule(object):
        def __init__(self):
            self.path_exists = lambda x: True

    loader_mock = LoaderModule()

    vars_mock = VariableManager()
    inventory_mock = InventoryManager(loader=DataLoader())

    # Test with

# Generated at 2022-06-13 08:47:28.022297
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # load_collection is called in the class init for RoleDefinition
    # and is not mocked in tests. Expect failure of the test when
    # collections are not already installed.
    role_collection_list = [AnsibleCollectionRef.from_string('test.test')]
    assert role_collection_list[0].to_string() == 'test.test'

    assert RoleDefinition(None, "/roles").preprocess_data('mysql') == \
        {'role': 'mysql'}


# Generated at 2022-06-13 08:47:34.503510
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_def = RoleDefinition()
    role_def.role = "test_role"
    assert role_def.get_name() == "test_role"
    role_def._role_collection = "test_collection"
    assert role_def.get_name() == "test_collection.test_role"


# Generated at 2022-06-13 08:47:42.055940
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    class MyRoleDefinition(RoleDefinition):
        _valid_attrs = {'role': FieldAttribute(isa='string')}
        _role = FieldAttribute(isa='string')

    rd = MyRoleDefinition()
    rd._role_collection = 'my_collection'
    rd._role = 'my_role'

    assert rd.get_name(include_role_fqcn=True) == "my_collection.my_role"
    assert rd.get_name(include_role_fqcn=False) == "my_role"

# Generated at 2022-06-13 08:47:49.488887
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    r = RoleDefinition()

    # Test role can be a dict
    d = dict(role='base')
    ans = r.preprocess_data(d)
    assert isinstance(ans, dict)
    assert ans['role'] == 'base'
    assert r._role_path == u'base'

    # Test role can be a string
    d = 'base'
    ans = r.preprocess_data(d)
    assert isinstance(ans, dict)
    assert ans['role'] == 'base'
    assert r._role_path == u'base'


# Generated at 2022-06-13 08:48:03.849281
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.plugins.loader import find_plugin
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy

# Generated at 2022-06-13 08:48:15.510965
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook import Play
    from ansible.plugins.loader import load_plugin_filter
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from units.mock.loader import DictDataLoader

    play_context = dict(
        remote_addr='1.1.1.1',
        remote_user='test'
    )

    base_role = dict(
        name='test_role',
        dir_name='foo'
    )


# Generated at 2022-06-13 08:48:22.140393
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_definition = RoleDefinition()
    role_definition._role_collection = 'fake_collection'
    role_definition._role = 'fake_role'
    assert role_definition.get_name() == 'fake_collection.fake_role'
    assert role_definition.get_name(include_role_fqcn=False) == 'fake_role'

    role_definition._role_collection = None
    assert role_definition.get_name() == 'fake_role'


# Generated at 2022-06-13 08:48:33.346453
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    collections_basedir = loader.collection_basedir
    loader._collection_basedir = dict()  # for the test, set collection_basedir to empty dict to get normal role loading

    role_definition = RoleDefinition()
    role_definition._variable_manager = {}
    roles_path = ['/etc/ansible/roles', '/tmp/roles']
    role_definition._loader.set_roles_path(roles_path)
    role_definition._loader.set_basedir('')

    # Test valid 'role' parameter
    ds = dict(role='role_name')
    result = role_definition.preprocess_data(ds)
    expected = dict(role='role_name')
    assert result == expected
    assert role_definition._role_path == '/etc/ansible/roles/role_name'



# Generated at 2022-06-13 08:48:51.742602
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    _role_collection = 'awx_collection.awx'
    _role = 'test_role'
    role_def_1 = RoleDefinition()
    role_def_1.role = _role

    assert _role_collection + '.' + _role == role_def_1.get_name()
    assert _role == role_def_1.get_name(include_role_fqcn=False)

    role_def_2 = RoleDefinition()
    role_def_2._role_collection = _role_collection
    role_def_2.role = _role

    assert _role_collection + '.' + _role == role_def_2.get_name()
    assert _role == role_def_2.get_name(include_role_fqcn=False)

# Generated at 2022-06-13 08:48:55.445679
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_definition = RoleDefinition()
    role_definition._role_collection = 'test'
    role_definition.role = 'test'
    assert role_definition.get_name() == 'test.test'
    assert role_definition.get_name(include_role_fqcn=False) == 'test'

# Generated at 2022-06-13 08:49:10.199824
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    module_utilities = {}
    loader = DictDataLoader({})
    variable_manager = VariableManager()

    role_path = './test_data/test_roles/test_role'
    role_basedir = './test_data/test_roles'

    # Test no params
    ds = 'test_role'
    role_def = RoleDefinition(role_basedir=role_basedir, loader=loader, variable_manager=variable_manager)
    role_def.preprocess_data(ds)
    assert role_def.get_role_path() == role_path
    assert role_def._role_params == {}

    # Test with params
    ds = {'role': 'test_role', 'vars':{'foo': 'bar'}}

# Generated at 2022-06-13 08:49:19.412439
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook import Task

    play_book = Play()
    play_book._variable_manager = VariableManager()

    context = PlayContext()
    loader = DataLoader()
    templar = Templar(loader=loader, variables=dict())


# Generated at 2022-06-13 08:49:33.432346
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    result = RoleDefinition(loader=None, variable_manager=None, collection_list=None).get_name()
    assert result == ''

    result = RoleDefinition(loader=None, variable_manager=None, collection_list=None).get_name(include_role_fqcn=False)
    assert result == ''

    loader = None
    variable_manager = None
    collection_list = None

    role_definition = RoleDefinition(loader=loader, variable_manager=variable_manager, collection_list=collection_list)
    role_definition._role_collection = 'ansible.builtin'
    role_definition._attributes['role'] = 'foo'
    result = role_definition.get_name()
    assert result == 'ansible.builtin.foo'

# Generated at 2022-06-13 08:49:46.149306
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import os
    import sys

    import yaml

    test_files_dir = os.path.join(os.path.dirname(__file__), 'unit', 'files')

    role_basedir = None
    variable_manager = None
    loader = None


# Generated at 2022-06-13 08:49:57.905349
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import os
    import tempfile

    datadir = tempfile.mkdtemp()
    sample_role = os.path.join(datadir, "sample_role")
    os.makedirs(sample_role)

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.base import Base

    loader = AnsibleLoader(None, {})
    data = {'role': sample_role, 'tasks': 'override'}
    rdef = RoleDefinition.load(data, loader=loader)
    assert rdef.get_name() == 'sample_role'

    loader = AnsibleLoader(None, {})
    data = {'role': 'missing_role', 'tasks': 'override'}

# Generated at 2022-06-13 08:50:04.163776
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_definition = RoleDefinition()
    assert role_definition.get_name() == "<no name set>"
    role_definition._role = None
    role_definition._role_collection = "namespace.collection"
    assert role_definition.get_name() == "namespace.collection.<no name set>"
    role_definition._role = "foo"
    assert role_definition.get_name() == "namespace.collection.foo"

# Generated at 2022-06-13 08:50:05.670699
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    assert 'myrole' == RoleDefinition.preprocess_data('myrole')['role']

# Generated at 2022-06-13 08:50:16.403634
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import vars_loader

    # we are not testing the parsing of 'role' here, just the cleanup
    # of the data structure and splitting of role params

# Generated at 2022-06-13 08:50:48.525966
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.collection_loader._collection_finder import _get_collection_role_path

    class TestRoleDefinition(RoleDefinition):
        _valid_attrs = frozenset(('role',))

    variable_manager = VariableManager()
    inventory = InventoryManager(loader=DataLoader(), sources='')
    variable_manager.set_inventory(inventory)

    play_context = PlayContext()

# Generated at 2022-06-13 08:50:55.432397
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    def preprocess_data_tester(input_data, expected_role_path, expected_role_name, expected_role_params, expected_error_message_list,
                               role_basedir, collection_list, variable_manager, loader):
        role_definition = RoleDefinition(role_basedir=role_basedir, collection_list=collection_list,
                                         variable_manager=variable_manager, loader=loader)
        try:
            role_definition.preprocess_data(input_data)
        except AnsibleError as e:
            error_message = str(e)
            assert error_message in expected_error_message_list, "AnsibleError message is not one of the expected messages."
        else:
            assert role_definition._role_params == expected_role_params
            assert role_definition._role_path == expected

# Generated at 2022-06-13 08:51:03.005262
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    """
    This test only validates basic parsing of a role definition.
    """
    mock_loader = object()
    result = RoleDefinition.load({'role': 'mock_role', 'mock_attr': 'mock_value'}, loader=mock_loader,
                                 variable_manager=None)
    assert result._role == 'mock_role'
    assert result._loader == mock_loader
    assert result._role_params == {'mock_attr': 'mock_value'}

# Generated at 2022-06-13 08:51:15.707256
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.play import Play
    loader = AnsibleLoader(None, None)
    ds = AnsibleMapping()
    ds['role'] = 'dev'
    ds['test'] = 'test'
    v = RoleDefinition(play=Play().load(dict(name="test"), variable_manager=None, loader=loader), role_basedir='.', variable_manager=None, loader=loader)
    v.preprocess_data(ds)
    assert v._ds == ds
    assert v._role_path == './dev'
    assert v._role_collection is None
    assert v.test == 'test'
    assert v.get_role

# Generated at 2022-06-13 08:51:24.079229
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    import tempfile
    import os
    import shutil
    import yaml
    from ansible.errors import AnsibleError, AnsibleUndefinedVariable
    from ansible.template import Templar as AnsibleTemplar
    from ansible.parsing.yaml.loader import AnsibleLoader as AnsibleYamlLoader
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins import PluginLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role_include import RoleInclude
    from ansible.plugins.filter import ipaddr as IPaddrFilterModule



# Generated at 2022-06-13 08:51:38.733138
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    '''
    role definition must be a string or a dict with a 'role' or 'name' key in it
    '''
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader
    data_loader = DataLoader()
    yaml_loader = AnsibleLoader(data_loader)

    rd = RoleDefinition(loader=data_loader)

    # test an empty data structure
    assert rd.preprocess_data(yaml_loader.load("")) is None

    # test the yaml_loader returns an array of string role names
    assert isinstance(rd.preprocess_data(yaml_loader.load("role1")), list)

    # test the yaml_loader returns an array of string role names
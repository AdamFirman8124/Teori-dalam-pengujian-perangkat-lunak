

# Generated at 2022-06-13 08:52:10.309077
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = 'test'
    assert isinstance(data, string_types)
    play = 'play'
    RoleInclude.load(data, play)

# Generated at 2022-06-13 08:52:18.016990
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import collection_loader
    from ansible.playbook.role.metadata import RoleMetadata

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'foo': 'bar'}
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager)
    collection_list = [ collection_loader.get('my.ns', collection_loader.get('my_col', None)) ]


# Generated at 2022-06-13 08:52:27.427881
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import json
    import sys
    import os
    import inspect
    import ansible.playbook
    import ansible.inventory
    import ansible.module_utils

    m_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    print("m_path=%s" % m_path)
    sys.path.insert(0, m_path + '/../../lib')
    sys.path.insert(0, m_path + '/..')

# Generated at 2022-06-13 08:52:37.635492
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.executor.task_executor import TaskExecutor
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.display import Display
    options = PlaybookExecutor.load_extra_vars({})
    loader = DataLoader()
    passwords = {}
    inventory = InventoryManager(loader=loader, sources='')

# Generated at 2022-06-13 08:52:47.867737
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """
    Unit test for method load of class RoleInclude
    """
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars import VariableManager

    fake_loader, var_manager, fake_inventory = (
        'fake_loader', VariableManager(), 'fake_inventory'
    )


# Generated at 2022-06-13 08:52:53.016243
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude.load(data={}, play={}, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None)
    assert ri is not None


# Generated at 2022-06-13 08:53:03.670168
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins import plugin_loader

    # Create variable_manager, loader and inventory_manager
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory_manager = InventoryManager(loader=loader, variable_manager=variable_manager)

    # Create empty play
    play = Play().load({}, variable_manager=variable_manager, loader=loader)


# Generated at 2022-06-13 08:53:13.117083
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

    # Mock ansible modules
    import sys
    sys.modules['_internal_ansible'] = sys.modules['ansible']
    sys.modules['_internal_ansible.module_utils'] = sys.modules['ansible.module_utils']

    from ansible.utils.display import Display
    display = Display()

    vault_pass = 'test'
    loader = DataLoader()
    vault_secrets_file = None

# Generated at 2022-06-13 08:53:15.451334
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # c
    curren_role_path = None
    parent_role = None
    variable_manager = None
    loader = None


# Generated at 2022-06-13 08:53:23.515618
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.utils import context_objects as co

    add_all_plugin_dirs()
    loader, inventory, variable_manager = co._init_global_context(playbook_path='/dev/null')

    play_context = PlayContext()
    play_context._set_loader(loader)

    data = {}

    try:
        ri = RoleInclude(play=None, role_basedir=None, variable_manager=None, loader=loader)
        ri.load(data, play_context, current_role_path=None, parent_role=None, variable_manager=variable_manager, loader=loader)
    except AnsibleParserError as ape:
        assert ape.message

# Generated at 2022-06-13 08:53:35.406015
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import ansible.parsing.yaml.objects

    play = None
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None

    # Test exception for invalid role definition.
    data = ['abc']
    try:
        x = RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
        assert False
    except Exception as e:
        assert type(e) == AnsibleParserError

    # Test exception for invalid old style role requirement.
    data = 'abc,def'

# Generated at 2022-06-13 08:53:46.950165
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.collections import AnsibleCollection
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.config.manager import ConfigManager
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role.requirement import RoleRequirement

    collection = AnsibleCollection('testns', 'testcoll')
    req = RoleRequirement.load('testns.testcoll.foobar', collection=collection)
    assert req.get_role_name() == 'testcoll.foobar'

    collection = AnsibleCollection('testns', 'testcoll')
    req = Role

# Generated at 2022-06-13 08:53:52.886297
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import os
    import tempfile
    import yaml

    # Creating a temporary directory
    tmpdir = tempfile.mkdtemp()

    # Creating a file in temporary directory
    yaml_file = \
         '''
# comment
---
- hosts: localhost
  vars:
    foo: bar
  roles:
    - { role: apache, vars: { http_port: 81 }}
    - mysql
    '''

    yaml_filepath = os.path.join(tmpdir, "test.yml")
    with open(yaml_filepath, "w") as f:
        f.write(yaml_file)

    # Creating a role definition file

# Generated at 2022-06-13 08:54:00.330785
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    def test_load_fail(data, exception):
        try:
            ri = RoleInclude()
            ri.load(data)
            assert False
        except AnsibleError as e:
            assert exception in to_native(e)

    data = "something"
    exception = "Invalid role definition"
    test_load_fail(data, exception)

    data = 1
    exception = "Invalid role definition"
    test_load_fail(data, exception)

    data = []
    exception = "Invalid role definition"
    test_load_fail(data, exception)

    data = {}
    ri = RoleInclude()
    ri.load(data)

# Generated at 2022-06-13 08:54:08.539383
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    data = '''
    - name: test_role
    '''
    play = None
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None

    data2 = '''
    - name: test_role
    '''
    ri = RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    assert ri.get_name() == 'test_role'
    data = {"test_role": '''
- name: test_role
'''}

# Generated at 2022-06-13 08:54:18.566462
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import ansible.playbook.role
    ri = ansible.playbook.role.RoleInclude()
    result = ri.load("", "", "", "")
    assert type(result) is ansible.playbook.role.RoleInclude
    result = ri.load(
        {"name": "test_name", "role_path": "test_role_path", "tasks_path": "test_tasks_path", "handlers_path": "test_handlers_path",
         "default_vars": "test_vars", "vars_files": ["test_vars_files"], "meta": "test_meta"}, "", "", "")
    assert type(result) is ansible.playbook.role.RoleInclude

# Generated at 2022-06-13 08:54:27.916117
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    #
    # This unit test should be moved to the test/unit/playbook/test_include.py file
    # as soon as it is created
    #
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    empty_inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=empty_inventory)

    #
    # Test with RoleDefinition
    #
    ri_dict = {'name':'role1'}
    ri

# Generated at 2022-06-13 08:54:39.008302
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    collection_spec = {
        "name": "mystuff.mycollection",
        "version": "1.0.0",
        "namespace": "mystuff",
        "collection_type": "ansible_collection",
        "dependent_collections": [
            {
                "name": "mynamespace.myothercollection",
                "version": "0.3.4",
                "namespace": "mynamespace"
            }
        ]
    }
    coll_mgr = MockCollectionManager()
    coll_mgr.get_collection.return_value = collection_spec
    coll_mgr.list_collections.return_value = [ collection_spec ]

    data = {'name': 'test', 'version': 'test'}

# Generated at 2022-06-13 08:54:44.246344
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude()
    data = {}
    data["hosts"] = ["localhost"]
    data["tasks"] = {
        "t0": {
            "debug": {
                "msg": "t0"
            }
        },
    }
    play = {"name": "play"}
    
    ri.load(data, play)
    assert ri.vars is None
    assert ri.platform is None
    assert ri.roles is None
    assert ri.dependencies is None
    assert ri.meta is None
    assert ri.tasks is data["tasks"]
    assert ri.handlers is None
    assert ri.default_vars is None
    assert ri.pre_tasks is None
    assert ri.post_tasks is None
    assert r

# Generated at 2022-06-13 08:54:50.035528
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play import Play

    pb = Play.load(dict(name="TestPlaybook"), variable_manager=dict(), loader=dict())
    ri = RoleInclude.load(data=dict(name="TestRoleInclude"), play=pb, current_role_path='/',
                          parent_role=None, variable_manager=dict(), loader=dict(), collection_list=None)

    assert isinstance(ri, RoleInclude)

# Generated at 2022-06-13 08:55:03.073302
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    role_include = RoleInclude()
    role_include.play = {'hosts': 'test', 'roles': [{'role': 'test'}]}
    variable_manager = {}
    loader = {}
    data = {}
    role_include.load(data, variable_manager, loader)
    assert role_include.delegate_to == ''
    assert role_include.delegate_facts == 0
    assert role_include.tasks == []

# Generated at 2022-06-13 08:55:14.267357
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    import unittest.mock as mock
    from ansible.parsing.yaml.dumper import AnsibleDumper

    from . import TestPlaybookExecutionV2

    mock_variable = mock.MagicMock(name='mock_variable')
    mock_loader = mock.MagicMock(name='mock_loader')
    mock_collection_list = mock.MagicMock(name='mock_collection_list')

    class AnsibleRole(RoleInclude):
        def load_data(self, data, variable_manager=None, loader=None):
            self.data = data
            self.variable_manager = variable_manager

        def get_data(self):
            return self.data


# Generated at 2022-06-13 08:55:21.283556
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """
    Test the load method of class RoleInclude.
    """
    from ansible.playbook.play_context import PlayContext

    yaml_invalid_role_definition = [
        "[ 'xxx' ]",
        "[ [ 'xxx' ] ]",
        "{ 'xxx' : 'yyy' }",
        "{ 'xxx' : [ 'yyy' ] }",
    ]

    yaml_invalid_role_requirement_list = [
        "[ 'xxx,yyy' ]",
        "[ [ 'xxx,yyy' ] ]",
        "{ 'xxx,yyy' : 'zzz' }",
        "{ 'xxx,yyy' : [ 'zzz' ] }",
    ]


# Generated at 2022-06-13 08:55:29.267053
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    # Generate the necessary parameters
    data = "test-role"
    variable_manager = MagicMock()
    variable_manager.options_vars = {'ansible_run_tags': [], 'ansible_skip_tags': [], 'ansible_vault_password': 'VARIABLE MANAGER VAULT PASSWORD'}
    variable_manager.extra_vars = {}
    loader = MagicMock()

# Generated at 2022-06-13 08:55:39.058564
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    '''
    Test the method load of class RoleInclude.
    '''
    # in this case the __init__ throws an error
    passed = False
    try:
        RoleInclude.load(None, None, None, None)
    except:
        passed = True
    if not passed:
        raise AssertionError("Expected an error for empty role definition")

    # in this case the __init__ throws an error
    passed = False
    try:
        RoleInclude.load({'name': 'fake_role_name'}, None, None, None)
    except:
        passed = True
    if not passed:
        raise AssertionError("Expected an error for invalid role definition")

    passed = False

# Generated at 2022-06-13 08:55:42.391833
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """
    Test the RoleInclude.load method
    """
    # Test load method of class RoleInclude
    result = RoleInclude.load(data="geerlingguy.apache", play=None, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None)
    assert result

# Generated at 2022-06-13 08:55:53.646925
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.errors import AnsibleParserError
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars
    import pytest
    import os
    import pprint
    import sys
    import yaml

    script_dir = os.path.dirname(__file__)
    sample_dir = os.path.join(script_dir, '../unit/sample_data')

# Generated at 2022-06-13 08:55:57.760541
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data= 'test.test'
    play = ''
    current_role_path = ''
    parent_role = ''
    variable_manager = ''
    loader = ''
    RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader)



# Generated at 2022-06-13 08:56:13.539120
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    class AnsiblePlaybook:
        def __init__(self, host_list):
            self.host_list = host_list

    class RoleInclude:
        def __init__(self, play):
            self.play = play

        def load_data(self, data, **kwargs):
            return (self, data)

    class Hosts:
        def __init__(self, host_path):
            self.host_path = host_path

    print(RoleInclude.load('test', AnsiblePlaybook(Hosts('hosts'))))


# Test isinstance(data, string_types)
# a = 'test'
# print(isinstance(a, string_types))

# Test isinstance(data, dict)
# a = {'test': 1}
# print(isinstance(a, dict))


# Generated at 2022-06-13 08:56:21.980664
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play import Play

    play_obj = Play()
    ri = RoleInclude(play_obj)

    data = "foo"
    err = False
    try:
        ri.load(data, play_obj)
    except AnsibleError as e:
        err = e

    assert(type(err) == AnsibleError)

    data = dict()
    err = False
    try:
        ri.load(data, play_obj)
    except AnsibleError as e:
        err = e
    assert(type(err) == AnsibleError)

    data = dict(foo="bar")
    err = False
    try:
        ri.load(data, play_obj)
    except AnsibleError as e:
        err = e

# Generated at 2022-06-13 08:56:41.698178
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.variable_manager import VariableManager
    from ansible.vars.manager import VaultVariableManager

    ds = """
    - name: test_RoleInclude_load_ds1
      become: false
      connection: local
      roles:
        - role-name
    """
    loader, inventory, play_source, play = Play().load_play_from_data(ds)

    hosts = [Host(name='server'), Host(name='client')]
    groups = [Group(name='ungrouped')]
    for h in hosts:
        inventory.add_host(h)
        for g in groups:
            g.add_host(h)

    def check_vars(variable_manager, loader):
        hostv

# Generated at 2022-06-13 08:56:50.800438
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Load test data.
    data = """
- name: Test
  hosts: localhost
  roles:
    - { role: foo, tags: [ 'bar', 'baz' ] }
    - { role: bar, when: ansible_os_family == 'RedHat' }
    - { role: baz, when: 1 == 2 }
    - { role: qux, tags: [ 'one', 'two' ], when: not unix_like }
    - { role: norole }
"""
    # Throw an error if method load() can not accept a string.
    instance = RoleInclude()
    with pytest.raises(AnsibleParserError) as e:
        instance.load(data, play='Test')

# Generated at 2022-06-13 08:56:51.963366
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Arrange
    # Act
    # Assert
    pass

# Generated at 2022-06-13 08:56:59.650765
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    data = {'role': 'test_role', 'dynamic_role': {'variables': {'role': 'test_role_dynamic_role'}}}
    ri = RoleInclude()
    ri.load_data(data)

    assert ri.get_name() == 'test_role'
    assert ri.get_path() == 'test_role_dynamic_role'
    assert ri.get_role_name() == ri.get_name()
    assert ri.get_role_path() == ri.get_path()
    assert ri.get_role_params() == ['role', 'dynamic_role']


# Generated at 2022-06-13 08:57:10.734189
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    class fake_loader:
        def __init__(self):
            self.all_vars = {}

    class fake_variable_manager:
        def __init__(self):
            self.extra_vars = {}
            self.options = {}

        def set_options(self, options):
            self.options = options

        def add_extra_vars(self, extra_vars):
            self.extra_vars = extra_vars

        def all_vars(self):
            return self.extra_vars

    # data is str
    data = 'test_role'
    role = RoleInclude.load(data, None, None, None, None, None)
    assert isinstance(role, RoleInclude)
    assert role.get_name() == 'test_role'

    # data is dict
   

# Generated at 2022-06-13 08:57:12.869367
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    #FIXME: This test is disabled for now.
    assert False


# Generated at 2022-06-13 08:57:28.955576
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    data_type_dict1 = {
        'name': 'MyName'
    }

    data_type_dict2 = {
        'name': 'MyName',
        'any_errors': True
    }

    data_type_dict3 = {
        'name': 'MyName',
        'ignore_errors': True
    }

    data_type_dict4 = {
        'name': 'MyName',
        'ignore_errors': 'True'
    }

    data_type_dict5 = {
        'name': 'MyName',
        'ignore_errors': 'True'
    }

    data = "MyName,AnyErrors"

    res = RoleInclude.load(data, None)
    assert res

    res = RoleInclude.load(data_type_dict1, None)
    assert res



# Generated at 2022-06-13 08:57:30.141843
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    raise NotImplementedError

# Generated at 2022-06-13 08:57:41.257088
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # assert_raises_regexp(AnsibleError, 'Invalid old style role requirement: foo,bar', RoleInclude.load, 'foo,bar')

    # assert_raises_regexp(AnsibleParserError, 'Invalid role definition', RoleInclude.load, 1)

    assert_raises(AnsibleParserError, RoleInclude.load, {'collection': 'foo.bar'})

    assert_raises(AnsibleError, RoleInclude.load, {'role': 'foo.baz'})

# Generated at 2022-06-13 08:57:49.227252
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    p = Play.load(dict(
        name = "foobar",
        hosts = 'all',
        gather_facts = 'no',
        roles = [ 'test_role' ],
    ), variable_manager=VariableManager(), loader=DataLoader())
    r = p.get_roles()
    assert isinstance(r[0], RoleInclude)
    assert r[0].get_name() == 'test_role'
    assert r[0].get_role_path() == u'/etc/ansible/roles'

# Generated at 2022-06-13 08:58:26.114537
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = {
        'name': 'test_role',
        'hosts': 'host.example.org',
        'roles': [
            'role1',
            'role2',
            {'role': 'role3', 'x': '1', 'y': 2},
            'role4,role5',
            {'role': 'role6,role7'},
        ],
    }
    play = None
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None

    expected_output = "Invalid old style role requirement: role4,role5"


# Generated at 2022-06-13 08:58:42.326445
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.utils.display import Display
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    display = Display()
    play_context = PlayContext(variable_manager=VariableManager(), loader=DataLoader(), display=display)

# Generated at 2022-06-13 08:58:46.167574
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # TODO: This unit test requires mocking a lot of Ansible internals
    #       (e.g. play, role_basedir, variable_manager, loader)
    pass


# Generated at 2022-06-13 08:58:51.693620
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook import base_loader
    from ansible.playbook.play_context import PlayContext

    class VariableManager:
        def get_vars(self, loader, path=None, play=None, host=None, task=None, include_hostvars=True, include_delegate_to=True):
            return {}

        def update_vars(self):
            pass

        def update_hostvars(self):
            pass

        # not tested
        def get_hostvars(self, host):
            pass

        # not tested
        def preprocess_vars(self, hostnames, add_nonhost_vars=False):
            pass

        # not tested
        def host_info(self, host):
            pass



# Generated at 2022-06-13 08:58:55.121644
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # TODO: implement unit test
    # assertEqual(expected, RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader))
    assert True # TODO: implement your test here


# Generated at 2022-06-13 08:58:56.258538
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass


# Generated at 2022-06-13 08:58:56.837790
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:58:59.595707
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook import Play

    # Load role definition as a string
    # Load role definition as a dictionary
    # Load role definition as an AnsibleBaseYAMLObject

# Generated at 2022-06-13 08:59:07.082599
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Test using string which raises an AnsibleError
    data = "invalid, another"
    play = None
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None
    try:
        RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    except AnsibleError as e:
        assert e.message == "Invalid old style role requirement: %s" % data
    
    # Test using a string
    data = 'test/data'
    try:
        RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    except AnsibleError as e:
        assert False

# Generated at 2022-06-13 08:59:09.163511
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # 1. RoleInclude.load(data, play, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None)
    pass



# Generated at 2022-06-13 09:00:09.263144
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=[])
    playbook = PlaybookExecutor(playbooks=[os.path.join(os.path.dirname(__file__), 'data', 'test_playbook_data.yaml')],
                                inventory=inventory,
                                variable_manager=variable_manager,
                                loader=loader, options=None)

# Generated at 2022-06-13 09:00:12.109433
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Tests for method load of class RoleInclude
    # TODO: This should not be a static method
    #assert RoleInclude.load(data=None) is None
    #assert RoleInclude.load(data=None, play=None) is None
    pass

# Generated at 2022-06-13 09:00:14.307275
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    role = RoleInclude.load("somesuperhero.yml")
    assert isinstance(role, RoleInclude)

# Generated at 2022-06-13 09:00:24.415776
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars

    data_loader = DataLoader()
    variable_manager = VariableManager()
    collection_loader = AnsibleCollectionLoader(data_loader)

    PlaybookExecutor._load_callbacks.clear()
    PlaybookExecutor._post_validation_callbacks.clear()
    PlaybookExecutor._pre_tasks_callbacks

# Generated at 2022-06-13 09:00:31.160125
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import ansible.playbook.role.include
    def FakeRole():
        return
    # Test 1)
    role1 = FakeRole()
    role1.role_path = './test_roles'
    play1 = FakeRole()
    play1.roles = [role1]
    variable_manager = FakeRole()
    variable_manager.extra_vars = dict()
    loader = FakeRole()
    variable_manager.hostvars = dict()
    variable_manager.hostvars['host1'] = dict()
    variable_manager.hostvars['host1']['host1_var'] = dict()
    variable_manager.hostvars['host1']['host1_var'] = 'host1_var_value'
    variable_manager.hostvars['host2'] = dict()
    variable_

# Generated at 2022-06-13 09:00:40.885376
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import role_loader
    from ansible.errors import AnsibleParserError
    from six import StringIO
    import pytest
    from unittest.mock import patch
    variable_manager = VariableManager()
    loader = DataLoader()

    # Test load with valid data
    test_data = "test_role"
    test_play = Play.load(dict(name="test1", hosts="all"), variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 09:00:43.958061
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude()
    data = 'some_name'
    play = {"collections": []}
    ri.load(data, play)
    # TODO: Mainly test the error raise parts...


# Generated at 2022-06-13 09:00:53.066930
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.parsing.yaml.loader import AnsibleLoader

    def __init__():
        self.variable_manager = None
        self.loader = AnsibleLoader

    data = {'name': 'test', 'parent': '', 'task_files': None, 'metadata': None, 'default_vars': None, 'dependencies': [], 'handlers': None, 'vars_files': None, 'tasks': None}
    ri = RoleInclude(variable_manager=__init__.variable_manager, loader=__init__.loader)

    (result, m_data) = ri.load(data)
    assert type(result) == RoleDefinition

# Generated at 2022-06-13 09:01:01.515458
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    import unittest
    import mock

    class TestRoleInclude(unittest.TestCase):

        @mock.patch('ansible.errors.AnsibleError', new=AnsibleError)
        @mock.patch('ansible.errors.AnsibleParserError', new=AnsibleParserError)
        def test_RoleInclude_load_new_style_role_requirement(self):

            ri_load_mock = RoleInclude.load

            data = 'ansible.builtin.test'
            play = mock.Mock()
            current_role_path = None
            parent_role = None
            variable_manager = mock.Mock()
            loader = mock.Mock()
            collection_list = mock.Mock()


# Generated at 2022-06-13 09:01:02.306753
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert False, 'Test Not Implemented'
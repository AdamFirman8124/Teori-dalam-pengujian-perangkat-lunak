

# Generated at 2022-06-13 08:52:23.313831
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source = dict(
        name="Ansible Play",
        hosts='webservers',
        gather_facts='no',
        roles=[('dummy',dict(name="dummy"))]
    )

# Generated at 2022-06-13 08:52:33.282341
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    yaml_text = """
    - hosts: myhosts
      tasks:
        - include_role:
            name: ansible-role-wordpress
            tasks_from: main
    """
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader
    data = AnsibleLoader(yaml_text, None, AnsibleDumper).get_single_data()
    role_include = RoleInclude.load(data, None, current_role_path='/path/to/ansible/roles/ansible-role-wordpress')
    print(role_include)

# Generated at 2022-06-13 08:52:44.906312
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement

    # Test correct parsing of a string path
    ri = RoleInclude.load("my_role", None)
    assert isinstance(ri, RoleInclude)
    assert isinstance(ri.role_name, RoleRequirement)
    assert ri.role_name.name == "my_role"
    assert ri.role_name.role_name == "my_role"
    assert not ri.role_name.collections

    # Test correct parsing of a dict path
    role_dict = dict(role="my_role")



# Generated at 2022-06-13 08:52:53.173540
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.plugins.loader import find_plugin
    from ansible.plugins.connection import ConnectionBase
    from ansible.plugins.vars.lookup import LookupBase
    from ansible.plugins.filter import FilterModule

    try:
        find_plugin('connection_mock')
    except AnsibleError:
        add_all_plugin_dirs()

    def get_connection(self, *args, **kwargs):
        return ConnectionBase()
    ConnectionBase.get = get_connection

    def get_lookup(self, *args, **kwargs):
        return LookupBase()
    LookupBase.get = get_lookup


# Generated at 2022-06-13 08:53:03.799616
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # create object RoleInclude
    ri = RoleInclude()

    # check method load
    try:
        ri.load(data=['RoleInclude'], variable_manager=None, loader=None)
        assert False
    except AnsibleError:
        assert True

    try:
        ri.load(data='', variable_manager=None, loader=None)
        assert False
    except Exception as e:
        assert str(e) == ("Empty role definition:  in file /etc/ansible/roles/geerlingguy.docker/tasks/main.yml: line 1, column 1, but may be elsewhere in the file depending on the exact syntax problem\n\nThe offending line appears to be:\n\n\n^ here")
        assert True


# Generated at 2022-06-13 08:53:10.781993
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    data = 'role.name'
    # some_object is str type, which is a invalid role definition
    role_include = RoleInclude()
    assert not role_include.load(data=data, play=None, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None)

    data = {'name': 'role.name'}
    object = RoleInclude()
    assert object.load(data=data, play=None, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None)

    data = 'role_1,role_2'
    role_include = RoleInclude()

# Generated at 2022-06-13 08:53:14.514417
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.module_utils._text import to_text, to_bytes
    from ansible.vars.hostvars import HostVarsVars
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude

# Generated at 2022-06-13 08:53:22.993313
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Load RoleInclude
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import VariableManager
    from ansible.compat.tests import unittest

    loader = DataLoader()
    play = Play()
    variable_manager = VariableManager()

    role_include = RoleInclude(play, loader=loader, variable_manager=variable_manager)

    # Test dict
    if isinstance(data, dict):
        ri.update(data)

    # Test string
    if isinstance(data, string_types):
        ri.update({"role": data})

    # Test AnsibleBaseYAMLObject
    if isinstance(data, AnsibleBaseYAMLObject):
        ri.update(data.get_data())



# Generated at 2022-06-13 08:53:30.573269
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = 'test'
    play = None
    variable_manager = None
    loader = None
    collection_list = None
    obj = RoleInclude.load(data=data, play=play, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
    assert not obj.role_basedir
    assert not obj.variable_manager
    assert not obj.loader

if __name__ == '__main__':
    test_RoleInclude_load()

# Generated at 2022-06-13 08:53:38.616625
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret
    from ansible.parsing.vault import AnsibleVaultEncryptedUnicode
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play

    # Create a VaultSecret with a password
    vault_secret = None
    vault_secret = VaultSecret('myvaultpassword')

    vault_password_file = os.path.join(os.path.dirname(__file__), "../../test/test_playbook/vault_password.txt")
    vault_password = open(vault_password_file, 'rb').read().rstrip()

# Generated at 2022-06-13 08:53:50.065021
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import collection_loader
    from ansible.playbook.play import Play
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.loader import filter_loader

    c_loader = collection_loader.get("test")
    test_module = c_loader.get("test_module")
    test_module = c_loader.get("test_module")

    variable_manager = VariableManager()
    variable_manager._fact_cache = dict()
    variable_manager._extra_v

# Generated at 2022-06-13 08:53:54.299380
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    role_include = RoleInclude()
    role_include.load(data=None, play=None, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None)

# Generated at 2022-06-13 08:54:03.747755
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    yaml = '''
- hosts: test
  roles:
    - test-role
'''
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.utils.vars import combine_vars
    from ansible.module_utils.facts.system.distribution import Distribution

    data = yaml
    play = Play().load(yaml, variable_manager=VariableManager(), loader=DataLoader())
    current_role_path = play.basedir() + '/roles'
    parent_role = None
    variable_manager = VariableManager()

# Generated at 2022-06-13 08:54:11.284908
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    def get_data():
        return {'role_name': 'test_role'}

    play = None
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None

    class MockRoleInclude:
        def __init__(self, play=None, role_basedir=None, variable_manager=None, loader=None, collection_list=None):
            self._attributes = {}
            self.role_name = None
            self.role_path = None
            self.is_meta_role = False

        def load_data(self, data, variable_manager=None, loader=None):
            assert(isinstance(data, dict))
            self.role_name = data['role_name']

# Generated at 2022-06-13 08:54:22.851115
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import os
    import ansible.playbook
    from ansible.playbook.play_context import PlayContext

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager

    from ansible.playbook.block import Block
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult

    pb = ansible.playbook.Playbook.load("./test/unit/playbook_tests/role/include/playbook.yml", variable_manager=VariableManager(), loader=DataLoader())
    context = PlayContext()
    pm

# Generated at 2022-06-13 08:54:23.472688
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass


# Generated at 2022-06-13 08:54:28.654591
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = 'test_string'
    play = None
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None

    # Testing for test_string
    try:
        ri = RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
        assert False, 'String role requirement should not be accepted'
    except AnsibleError:
        pass

# Generated at 2022-06-13 08:54:30.563143
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert RoleInclude.load("test", play=None, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None)


# Generated at 2022-06-13 08:54:36.875412
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """
    Test function of RoleInclude.load
    
    """

    ri = RoleInclude()
    
    with pytest.raises(AnsibleParserError):
        ri.load(data=None, play=None)
    with pytest.raises(AnsibleError):
        ri.load(data='test,test', play=None)
    ri.load(data='test', play=None)



# Generated at 2022-06-13 08:54:48.536305
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager.set_inventory(inventory)
    play_context = PlayContext()

    file_name = '../../tests/playbooks/include_role/host_vars/host1.yml'
    include_role = RoleInclude(play=None, role_basedir=os.path.dirname(file_name),
                               variable_manager=variable_manager, loader=loader)
    import yaml

# Generated at 2022-06-13 08:54:59.707685
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import os
    import tempfile
    import yaml

    # Create a temporary directory
    tmp_dir = tempfile.mkdtemp()

    # Create a role file
    role_file = os.path.join(tmp_dir, "main.yml")
    role_data=dict(
        name="test_role",
        description="test_role_description",
        tasks=["task1"],
        handlers=["handler1"],
        meta=dict(
            dependencies=dict(
                - test_dependency
                ),
            ),
        )
    with open(role_file, 'w') as f:
        f.write(yaml.dump(role_data, default_flow_style=False))

    # Test the "load" method with an existing role file
    ri = RoleInclude()
    ri.load

# Generated at 2022-06-13 08:55:05.403328
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    r'''
#! YAML
---
- hosts: all
  tasks:
    - include_role:
        name: include_role_test

...

#! YAML
- hosts: all
  tasks:
    - include_role: name=include_role_test
...
    '''

    from ansible.playbook.play import Play
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager  import InventoryManager
    from ansible.plugins.loader  import plugin_loader

    loader = AnsibleLoader(None, variable_manager=VariableManager(), loader=DataLoader())

# Generated at 2022-06-13 08:55:20.723719
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook import Play
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Create a dummy play to use throughout the unit test
    play = Play()

    # Create a dummy variable manager to use throughout the unit test
    variable_manager = VariableManager()
    variable_manager._options = combine_vars(loader=DataLoader(), variables=dict(var1='bar'))

    # Create a dummy role to use throughout the unit test
    role = RoleInclude(play=play, variable_manager=variable_manager)

    # Test if load raises exceptions when data is not a str or dict

# Generated at 2022-06-13 08:55:24.445570
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude()
    assert hasattr(ri, 'load')
    assert callable(ri.load)


# Generated at 2022-06-13 08:55:28.163678
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    obj = RoleInclude()

    # No data
    data, play, current_role_path, parent_role, variable_manager, loader, collection_list = None, None, None, None, None, None, None
    try:
        obj.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    except AnsibleParserError as e:
        assert to_native(e) == 'Invalid role definition: None'

    # Invalid data type
    data = []
    try:
        obj.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    except AnsibleParserError as e:
        assert to_native(e) == 'Invalid role definition: []'

    # Data type is dict

# Generated at 2022-06-13 08:55:33.561045
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude()
    assert ri.load('geerlingguy.jenkins', variable_manager='variable_manager', loader='loader') == ri
    assert ri.load({"role": "geerlingguy.jenkins"}, variable_manager='variable_manager', loader='loader') == ri


# Generated at 2022-06-13 08:55:41.847387
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    loader = DictDataLoader()
    ri = RoleInclude(play=None, role_basedir=None, variable_manager=None, loader=loader, collection_list=None)

    # Test for invalid data
    def f1():
        ri.load(None, play=None, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None)
    def f2():
        ri.load(42, play=None, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None)

# Generated at 2022-06-13 08:55:53.047482
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import loader as plugin_loader

    def testfunc(self):
        self.assertEqual(args[0], ...)

    test_loader = plugin_loader.PluginLoader('ansible.plugins.test')
    test_loader.add_directory(os.path.join(os.path.dirname(__file__), '../../test_data/playbook_tests/container/'))
    p = test_loader.get('playbook')
    p.play_context = PlayContext()
    assert p.play_context.no_log
    ri = RoleInclude(play=p)
    assert ri._load_name == 'FROM'
    assert ri._load_role
    assert ri.loader
    assert ri.variable_

# Generated at 2022-06-13 08:56:01.188945
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    vm = VariableManager()
    play = Play().load(dict(hosts='localhost', roles=['default_role_path']), variable_manager=vm, loader=DataLoader())
    role_basedir = 'default_role_path'

    # Empty
    data = ''
    try:
        RoleInclude.load(data, play=play, current_role_path=role_basedir, variable_manager=vm, loader=DataLoader())
    except AnsibleParserError:
        pass
    else:
        raise AssertionError('Expected AnsibleParserError')

    # Invalid type
    data = []

# Generated at 2022-06-13 08:56:15.955503
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import connection_loader, module_loader

    host_list = [{"hostname": "testserver1", "ip": "127.0.0.1", "port": 22},
                 {"hostname": "testserver2", "ip": "127.0.0.1", "port": 22}]

    inventory = InventoryManager(loader=DataLoader(), sources="")
    inventory.add_group('test_group')

# Generated at 2022-06-13 08:56:24.988589
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    play, current_role_path, variable_manager, loader, collection_list = mock_load_data()
    ri = RoleInclude.load("test_string", play, current_role_path, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
    unloaded_role = ri._unloaded_role
    assert unloaded_role._role_name == "test_string"
    assert unloaded_role._role_path == "test_string"


# Generated at 2022-06-13 08:56:34.820482
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.role_include import RoleInclude
    from ansible.variable_manager import VariableManager
    from ansible.vars.manager import load_extra_vars
    from ansible.vars.manager import load_options_vars
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    # The data represent the following example:
    # - name: playbook.yaml
    #   hosts: all
    #   tasks:
    #      - name: Test
    #        import_role:
    #          import_playbook: role_include
    #          apply:
    #            to:
    #              - group_a
    #            delegate_to: localhost
    #            delegate_facts: True

# Generated at 2022-06-13 08:56:44.968603
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source = dict(
        name="Ansible Play",
        hosts='local',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='setup', args='')),
        ]
    )
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
    assert isinstance(play, Play)


# Generated at 2022-06-13 08:56:52.875120
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from units.mock.loader import DictDataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.role.definition import RoleDefinition

    loader = DictDataLoader({
        "main.yml"              : """
        - role1:
            role: other_role
            tags:
              - role1_tag
            when: role1_condition
        - role: other_role
            tags:
              - role2_tag
            when: role2_condition
        """,
    })
    inv_data = {
        "all": {
            "hosts": {'test_host': {}},
            "vars": {}
        },
        "_meta": {
            "hostvars": {}
        }
    }
    inventory

# Generated at 2022-06-13 08:56:53.580780
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:56:57.332159
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    RoleInclude.load(
        dict(
            name = 'test',
            foo = 'bar'
        ),
        play = None,
        current_role_path = None,
        variable_manager = None,
        loader = None
    )

# Generated at 2022-06-13 08:57:05.327458
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Test with valid input data
    data = 'test_role'
    play = None
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None
    result = RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    assert result is not None

    # Test with invalid input data
    data = [1, 2, 3]
    try:
        result = RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
        assert False
    except AnsibleParserError:
        assert True

# Generated at 2022-06-13 08:57:10.905589
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    try:
        ri = RoleInclude()
        ri.load([])
    except Exception as e:
        assert isinstance(e, AnsibleError)

    try:
        ri = RoleInclude()
        ri.load('x,x')
    except Exception as e:
        assert isinstance(e, AnsibleError)

    try:
        ri = RoleInclude()
        ri.load('')
    except Exception as e:
        assert isinstance(e, AnsibleError)

    try:
        ri = RoleInclude()
        ri.load('a/b')
    except Exception as e:
        assert isinstance(e, AnsibleError)


# Generated at 2022-06-13 08:57:27.109514
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # test RoleInclude load with input as string type
    roleinclude_obj = RoleInclude.load("role1", play="play", current_role_path="current_role_path", parent_role="parent_role", variable_manager="variable_manager", loader="loader", collection_list="collection_list")
    assert roleinclude_obj.play == "play"
    assert roleinclude_obj.role_basedir == "current_role_path"
    assert roleinclude_obj.loader == "loader"
    assert roleinclude_obj.variable_manager == "variable_manager"
    assert roleinclude_obj.collection_list == "collection_list"

    # test RoleInclude load with input as dict type
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    play_obj = Play

# Generated at 2022-06-13 08:57:34.828617
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    test_play = {}
    test_role_based = ""
    test_variable_manager = {}
    test_loader = {}
    test_collection_list = {}
    test_data = {}
    # Test method load with None data parameter
    # Should raise exception due to invalid role definition when data parameter is not a string, dict, or BaseYAMLObject
    try:
        test_RoleInclude_load_result = RoleInclude.load(test_data, test_play, test_role_based, None, test_variable_manager, test_loader, test_collection_list)
    except AnsibleParserError:
        pass

    # Test method load with string data that contains a comma
    # Should raise exception due to invalid role requirement
    test_data = "test"

# Generated at 2022-06-13 08:57:53.589074
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """Test load method of the RoleInclude class"""
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.hostvars import HostVars
    from ansible.vars.reserved import Reserved
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    vars_dict = {'username': 'admin', 'name': 'test_role'}
    variable_manager._extra_vars = vars_dict
    variable_manager._fact_cache = HostVars(loader=loader)
    variable_manager._fact_cache._fact_

# Generated at 2022-06-13 08:57:54.478321
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass


# Generated at 2022-06-13 08:58:02.892316
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    c=RoleInclude(play=None, role_basedir=None, variable_manager=None, loader=None, collection_list=None)
    data="name1"
    play=None
    current_role_path=None
    parent_role=None
    variable_manager=None
    loader=None
    collection_list=None
    assert c.__class__ == RoleInclude
    assert c.load(data=data, play=play, current_role_path=current_role_path, parent_role=parent_role, variable_manager=variable_manager, loader=loader, collection_list=collection_list).__class__ == RoleInclude

# Generated at 2022-06-13 08:58:10.284484
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Test with a string containing a blank space
    data = "role1 ansible.builtin"
    play = "playbook.yml"
    current_role_path = "./"
    parent_role = "parrent role"
    variable_manager = "variables"
    loader = "loader"
    collection_list = "collections"
    response = RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    assert response == "Invalid role definition: 'role1 ansible.builtin'"
    # Test with a string containing a blank space
    data = "role1 ansible.builtin,role2"
    play = "playbook.yml"
    current_role_path = "./"
    parent_role = "parrent role"
    variable

# Generated at 2022-06-13 08:58:12.271615
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = {'name': 'testrole', 'role': 'testrole'}
    ri = RoleInclude()
    assert(ri.load(data))



# Generated at 2022-06-13 08:58:17.918033
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext

    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    play_context = PlayContext()
    variable_manager = VariableManager()
    inventory = InventoryManager(play_context.loader, variable_manager, play_context.host_list)

    path = "../../../test/integration/targets/role_include"
    play = Play.load(dict(
        name = "Ansible Play",
        hosts = "all",
        gather_facts = "no",
        tasks = [
            dict(action=dict(module="debug", args=dict(msg="Hello World!")))
        ]
    ), variable_manager=variable_manager, loader=play_context.loader)



# Generated at 2022-06-13 08:58:25.285444
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    role_include = RoleInclude()
    assert role_include.load('ansible.builtin.ping') is not None

    role = role_include.load({'role': 'ansible.builtin.ping'})
    assert role is not None
    assert role.name == 'ansible.builtin.ping'

    try:
        role = role_include.load({'role': 'xxx', 'xxx': 'yyy'})
        assert False
    except AnsibleParserError as e:
        assert str(e) == "The role xxx does not have valid meta data"

# Generated at 2022-06-13 08:58:41.995467
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass
#    data = {
#        'name': 'foo',
#        'scenario': 'bar',
#        'some_var': 'baz',
#        'some_list': ['foo', 'bar'],
#        'some_dict': {'foo': 'bar'},
#        'some_dict_from_var': '{{ some_var }}',
#        'some_list_from_var': ['{{ some_var }}', '{{ some_var }}'],
#    }
#    data_2 = {
#        'name': 'foo',
#        'scenario': 'bar',
#        'some_var': 'baz',
#        'some_list': ['foo', 'bar'],
#        'some_dict': {'foo': 'bar'},
#        'some_dict_from

# Generated at 2022-06-13 08:58:49.936615
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook import Play
    from ansible.playbook.role import Role
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.loader import load_callback_plugins

    loader=DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager.set_inventory(inventory)
    loader.set_basedir(os.getcwd())
    load_callback_plugins()
    play = Play.load({}, variable_manager=variable_manager, loader=loader)


# Generated at 2022-06-13 08:59:00.641558
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    import os
    import time
    import tempfile
    import json

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.utils.display import Display
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars


    # Setup test
    display = Display()
    loader = DataLoader()
    variable_manager = VariableManager
    inventory = InventoryManager(loader=loader, sources='dummy')
    playbook_

# Generated at 2022-06-13 08:59:24.210719
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # TODO: implement
    pass


# Generated at 2022-06-13 08:59:32.119317
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.variables.manager import VariableManager

    the_variable_manager = VariableManager()
    the_templar = Templar(loader=None, variables=the_variable_manager, fail_on_undefined=True)
    the_loader = None

    # Test valid role definition
    the_include = RoleInclude()
    the_include.load_data({
        'name': 'test_name',
        'become': 'true',
        'become_user': 'test_become_user',
        'become_method': 'test_become_method',
        'dummy_attribute': 'test_dummy_attribute',
    }, variable_manager=the_variable_manager, loader=the_loader)



# Generated at 2022-06-13 08:59:38.896480
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """
    Unit test for method load of class RoleInclude
    """
    req = '''
---
src:
  roles:
    - role: ansible-role-datadog
      vars:
        datadog_api_key: "{{ lookup('env','DD_API_KEY') }}"
        datadog_app_key: "{{ lookup('env','DD_APP_KEY') }}"
    - role: ansible-role-ganglia
      vars:
        ganglia_gmetad_version: '3.6.0-2'
        ganglia_gmond_version: '3.6.0-2'
        ganglia_web_version: '3.6.0-2'
'''

# Generated at 2022-06-13 08:59:43.918215
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.vars import combine_vars
    from ansible.errors import AnsibleParserError
    from ansible.module_utils._text import to_bytes
    import ansible.constants as C


# Generated at 2022-06-13 08:59:48.119154
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    roleInclude = RoleInclude()
    roleInclude.load({'role': 'test', 'foo': 'bar'}, play=None)
    assert('test' == roleInclude.get_name())
    assert('bar' == roleInclude.get_vars().get('foo'))

# Generated at 2022-06-13 08:59:58.700872
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    class MockRoleInclude:
        def __init__(self):
            pass
        def __eq__(self, other):
            return True

    import mock
    import yaml
    yaml_data = yaml.safe_load("""
- hosts: web
  vars:
    http_port: 80
  tasks:
  - name: test include
    debug: msg="This is a test"
    include: '{{ item }}'
    with_items:
      - role1
      - role2
""")

    mock_play = mock.Mock()
    mock_variable_manager = mock.Mock()
    mock_loader = mock.Mock()
    mock_collection_list = mock.Mock()


# Generated at 2022-06-13 09:00:00.011530
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # FIXME: write me
    pass


# Generated at 2022-06-13 09:00:08.148132
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.parsing.yaml.dumper import AnsibleDumper

    yaml = YAML(typ='safe', indent=4, width=1000, default_flow_style=False)
    yaml.default_style = False
    yaml.indent(mapping=2, sequence=4, offset=2)
    data = {
        'role_name': 'test'
    }

    # RoleInclude.load(data, Play(), None, None)

    configuration = {
        'defaults': {'roles_path': os.path.join(os.path.dirname(__file__), '../../../test/units/lib/ansible/roles')},
        'inventory': None
    }

# Generated at 2022-06-13 09:00:14.970108
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.plugins.loader import find_plugin
    from ansible.playbook.play import Play
    from ansible.plugins.loader import plugin_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.module_utils.common._collections_compat import Sequence
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper

    data = '''
- hosts: all
  remote_user: root
  roles:
   - test-role
'''


# Generated at 2022-06-13 09:00:24.913412
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    # initialize needed objects
    variable_manager = VariableManager()
    loader = DataLoader()
    play_context = PlayContext()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)
    # Instantiate RoleInclude class
    ri = RoleInclude()

    # test load function
    # data is None
    r = ri.load(None, None)
    assert r.__class__.__name__ == 'RoleInclude'

    # data is string
    r = ri.load

# Generated at 2022-06-13 09:01:10.720889
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert True == False

# Generated at 2022-06-13 09:01:19.598969
# Unit test for method load of class RoleInclude

# Generated at 2022-06-13 09:01:30.528213
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Test string types
    role_definitions = [
        "test_role_name",
        "test_role_name,defaults/main.yml",
    ]
    for definition in role_definitions:
        result = RoleInclude.load(definition, None, None, None, None, None)
        assert isinstance(result, RoleInclude)
    # Test AnsibleBaseYAMLObject
    result = RoleInclude.load({},None,None,None,None,None)
    assert isinstance(result, RoleInclude)
    # Test not string or AnsibleBaseYAMLObject
    result = RoleInclude.load(12345, None, None, None, None, None)
    assert not isinstance(result, RoleInclude)
    # Test role with ','

# Generated at 2022-06-13 09:01:44.414015
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    current_role_path = 'C:\\workspace\\ansible-playbook\\tests\\test_playbook\\roles'

# Generated at 2022-06-13 09:01:50.077811
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    os.environ['ANSIBLE_LIBRARY'] = '../../library'
    os.environ['ANSIBLE_MODULE_UTILS'] = '../../module_utils'
    os.environ['ANSIBLE_ROLES_PATH'] = '../../../sample_playbooks/roles'
    ri = RoleInclude()
    result = ri.load("test_role", play=None, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None)
    assert isinstance(ri, RoleInclude)
    assert isinstance(result, RoleInclude)
    assert result._role_name == "test_role"


# Generated at 2022-06-13 09:01:59.048447
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # returns the number of test passed
    nb_passed = 0
    # the number of tests
    nb_tests = 1

    #  determine if you have role_path in ansible.cfg
    role_test_path = None
    if "role_path" in os.environ:
        role_test_path = os.environ["role_path"]

    # role_path not defined in ansible.cfg, add to the environment
    if role_test_path is None:
        from ansible.config.manager import ConfigManager
        my_config = ConfigManager()
        role_path = my_config.get_config_value('DEFAULT', 'roles_path')[0]
        os.environ["role_path"] = role_path

    # create an instance of RoleDefinition for testing

# Generated at 2022-06-13 09:02:03.398123
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
  r = RoleInclude()
  assert r.load("name", None, None, None, None, None) is not None
  assert r.load({"name": "name"}, None, None, None, None, None) is not None
  assert r.load(AnsibleBaseYAMLObject(), None, None, None, None, None) is not None

# Generated at 2022-06-13 09:02:12.990535
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext

    context = PlayContext()
    context.network_os = 'junos'
    context.port = '22'
    context.remote_addr = '1.2.3.4'
    context.remote_user = 'johnd'
    context_dict = {
        'hosts': ['dev1', 'dev2'],
        'name': 'test',
        'connection': 'local'
    }

    from ansible.playbook.play import Play
    play = Play().load(dict(
        name="Ansible Play 1",
        hosts='localhost',
        roles=['l1_roles', 'l2_roles'],
        gather_facts='no',
        context=context_dict), variable_manager=None, loader=None)

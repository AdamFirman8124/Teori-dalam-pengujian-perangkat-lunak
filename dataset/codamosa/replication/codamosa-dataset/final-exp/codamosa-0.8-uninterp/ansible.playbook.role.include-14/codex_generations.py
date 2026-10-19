

# Generated at 2022-06-13 08:52:16.562169
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    current_role_path = "/home/user/project/roles/role_name"
    variable_manager = DummyVars({"tag_name": "tag_value"})
    loader = DummyLoader()
    collection_list = ["one","two"]
    role_data = 'role_name'
    role_data1 = 'role,role1'
    role_data2 = {'role_name': 'param'}
    role_data3 = {'role_name': 'param1', 'role_name1': 'param2'}
    role_data4 = {'role_name': ['param1', 'param2']}
    role_data5 = ['role_name']
    play = Dummy()

    # Test with correct data

# Generated at 2022-06-13 08:52:26.833454
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    # data is string_types (correct)
    ri = RoleInclude()
    data = 'test_string'
    play = 'test_play'
    current_role_path = 'test_current_role_path'
    parent_role = 'test_parent_role'
    variable_manager = 'test_variable_manager'
    loader = 'test_loader'
    collection_list = 'test_collection_list'

    ret = RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    assert isinstance(ret, RoleInclude)

    # data is dict (correct)
    ri = RoleInclude()
    data = {'key': 'value'}


# Generated at 2022-06-13 08:52:37.254006
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    import os
    import shutil
    current_role_path = '/home/zhangjian/Projects/ansible-playbook/roles/ansible-role'
    data = 'role_name'

# Generated at 2022-06-13 08:52:47.654834
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    import ansible.playbook.task as task
    from ansible.utils.collection_loader import AnsibleCollectionConfig

    def _load(data):
        return RoleInclude.load(data=data, play=None, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None)

    # basic
    data1 = dict(
        name='myrole',
        tasks=['foo.yml', 'bar'],
        handlers=['baz'],
        default_vars=dict(
            a=3,
            b=2,
        )
    )

    result = _load(data1)
    assert list(result.task_blocks.keys()) == ['tasks', 'handlers']
    assert len(result.tasks) == 2

    assert isinstance

# Generated at 2022-06-13 08:52:48.212624
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:52:50.415517
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert False

# Generated at 2022-06-13 08:52:58.528926
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    test = "Test"
    if RoleInclude.load(test) is False:
        print ("RoleInclude_load Failed")
        return False

    #Test case when definition is empty and raise AnsibleParserError
    try:
        if RoleInclude.load("") is False:
            print ("RoleInclude_load Failed")
            return False
    except AnsibleParserError:
        print ("RoleInclude_load Failed, definition is empty")
    except:
        print ("RoleInclude_load Failed")
        return False

    print ("RoleInclude_load Passed")
    return True


# Generated at 2022-06-13 08:52:59.590077
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # TODO: write unittest
    pass

# Generated at 2022-06-13 08:53:03.005226
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude()
    ri.load_data({'name':'apache', 'role':'apache'}, variable_manager=None, loader=None)
    assert len(ri.get_vars().keys())==2

# Generated at 2022-06-13 08:53:12.718722
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    import ansible.playbook
    import ansible.constants as C
    import ansible.parsing.dataloader
    from ansible.plugins.loader import vault_loader

    def dummy_display(msg, color=None, stderr=False, screen_only=False, log_only=False):
        pass

    # Create mock objects for AnsiblePlaybook and AnsibleVariableManager
    loader = ansible.parsing.dataloader.DataLoader()
    vault_secrets = vault_loader.VaultSecrets(loader.load_from_file('test/ansible/vault.yml'))
    vault_secrets._finalize()

# Generated at 2022-06-13 08:53:22.929656
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    role_a = {"name": "role_a", "file": "./roles/role_a/meta/main.yml"}
    task_1 = {"include_role":"role_a"}
    # test_1
    ri = RoleInclude(play=None, role_basedir=None, variable_manager=None, loader=None, collection_list=None)
    assert ri.load(task_1,play=None, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None)
    # test_2
    task_2 = {"include_role":"role_a", "name":"usergiven_role_a"}

# Generated at 2022-06-13 08:53:23.692010
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert True

# Generated at 2022-06-13 08:53:35.021250
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    data = {'name': 'myrole', 'hosts': 'host1'}
    ri = RoleInclude()
    result = ri.load_data(data)
    assert result is not None
    assert result._role_name == 'myrole'

    data = 'myrole'
    ri = RoleInclude()
    result = ri.load_data(data)
    assert result is not None
    assert result._role_name == 'myrole'


    data = 'foo,bar'  	# old style
    ri = RoleInclude()
    try:
        result = ri.load_data(data)
        assert False
    except AnsibleError as e:
        assert "Invalid old style role requirement" in to_native(e)

# Generated at 2022-06-13 08:53:46.525672
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    import unittest
    import mock
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.playbook.role.definition import RoleDefinition


# Generated at 2022-06-13 08:53:56.248605
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = {}
    play = object()
    current_role_path = object()
    parent_role = object()
    variable_manager = object()
    loader = object()
    collection_list = object()
    role_include = RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    assert isinstance(role_include, RoleInclude)
    assert role_include._play == play
    assert role_include._role_basedir == current_role_path
    assert role_include._variable_manager == variable_manager
    assert role_include._loader == loader
    assert role_include._collection_list == collection_list

# Generated at 2022-06-13 08:53:57.830645
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """
    Test load method of class RoleInclude
    """
    # Base case
    assert True

# Generated at 2022-06-13 08:54:06.510413
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    #############################################################################
    # test load without any exception
    #############################################################################
    with open('/tmp/foo.yml', 'wb') as f:
        f.write(b'test: load')

    play = {
        'name': 'test_play',
        'connection': 'local',
        'hosts': [],
        'host_pattern': 'all',
        'any_errors_fatal': False,
        'gather_facts': True
    }
    variable_manager = {
        'name': 'test_variable',
        'extra_vars': 'test_extra_vars',
        'options': {},
        'option_order': [],
        'source': []
    }

# Generated at 2022-06-13 08:54:06.891939
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass



# Generated at 2022-06-13 08:54:18.207762
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook.role.meta import RoleMetadata
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.utils.path import unfrackpath
    from ansible.errors import AnsibleParserError
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host, Group

    host = Host(name="localhost")
    group = Group(name="all")
    group.add_host(host)

    inventory = InventoryManager(loader=DataLoader(), sources='')
    inventory.add_group(group)
    inventory

# Generated at 2022-06-13 08:54:27.726162
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    variable_manager = None
    loader = None
    collection_list = None

    # Case 1:
    # data: 'test1'
    # play: object AnsiblePlay() with attribute 'ROLE_CACHE'
    # current_role_path: '/home/devel/test1/'
    # parent_role: None
    # variable_manager: None
    # loader: None
    # collection_list: None
    # Expected result: object RoleRequirement() with attribute 'name' = 'test1'
    data = 'test1'
    play = AnsiblePlay()
    current_role_path = '/home/devel/test1/'
    parent_role = None

# Generated at 2022-06-13 08:54:42.204176
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    print("test_RoleInclude_load")

    from ansible.playbook.play import Play
    from ansible.plugins.loader import find_plugin
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.display import Display
    from ansible.parsing.dataloader import DataLoader

    # build test data
    # test data - list of dicts, each dict is one task definition
    test_role_data = [{'name': 'test_role', 'hosts': 'all'}, {'name': 'test_role_1', 'hosts': 'all'}]

    display = Display()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])

# Generated at 2022-06-13 08:54:46.211743
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement

    p = Play()
    r  = Role()
    rd = RoleDefinition()
    rm = RoleRequirement()

    data = {'name': 'test', 'delegate_to': '127.0.0.1', 'delegate_facts': True}
    ri = RoleInclude.load(data, play=p)
    assert ri.name == 'test'
    assert ri.delegate_to == '127.0.0.1'
    assert ri.delegate_facts is True

# Generated at 2022-06-13 08:54:47.252708
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:54:49.266071
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude()
    assert ri._load_data("role: ansible-role-test") == "ansible-role-test"

# Generated at 2022-06-13 08:54:59.329450
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    play = AnsibleBaseYAMLObject()
    role_basedir = AnsibleBaseYAMLObject()
    variable_manager = AnsibleBaseYAMLObject()
    loader = AnsibleBaseYAMLObject()
    collection_list = AnsibleBaseYAMLObject()
    role_include = RoleInclude(play, role_basedir, variable_manager, loader, collection_list)

    data = AnsibleBaseYAMLObject()

    #assert isinstance(data, string_types) or isinstance(data, dict) or isinstance(data, AnsibleBaseYAMLObject)
    if not (isinstance(data, string_types) or isinstance(data, dict) or isinstance(data, AnsibleBaseYAMLObject)):
        raise AnsibleParserError("Invalid role definition: %s" % to_native(data))

# Generated at 2022-06-13 08:55:10.859806
# Unit test for method load of class RoleInclude

# Generated at 2022-06-13 08:55:19.221824
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    import ansible.constants as C
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from io import StringIO
    from ansible.playbook.play_context import PlayContext
    import pytest


# Generated at 2022-06-13 08:55:19.738490
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:55:30.055666
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role.definition import RoleDefinition


# Generated at 2022-06-13 08:55:39.686524
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = 'a'
    play = {}
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None
    assert RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    
    data = 'a'
    play = {}
    current_role_path = 'a'
    parent_role = None
    variable_manager = 'a'
    loader = None
    collection_list = None
    assert RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)

## Unit test for static method load of class RoleInclude
#def test_RoleInclude__load():
#    data = 'a'

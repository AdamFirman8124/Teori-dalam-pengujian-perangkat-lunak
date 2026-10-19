

# Generated at 2022-06-13 08:52:17.101569
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from io import StringIO
    from ansible.plugins.loader import action_loader, lookup_loader
    from ansible.playbook.play import Play
    from ansible.plugins.loader import module_loader

    try:
        os.mkdir("output")
    except FileExistsError:
        pass

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager)
    variable_manager.set_inventory(inventory)


# Generated at 2022-06-13 08:52:26.168232
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import unittest

    class RoleIncludeTestCase(unittest.TestCase):
        def test_load_string(self):
            result = RoleInclude.load('common', None, None, None)
            self.assertFalse(result)

        def test_load_dict(self):
            result = RoleInclude.load({'role': 'common'}, None, None, None)
            self.assertFalse(result)

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(RoleIncludeTestCase))
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-13 08:52:33.126527
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook import Play
    from ansible.vars.manager import VariableManager

    loader = None

    def _data():
        data = dict()
        data['name'] = 'apache'
        return data

    play = Play()
    variable_manager = VariableManager()
    iterator = RoleInclude.load(_data(), play, variable_manager=variable_manager, loader=loader)
    assert iterator._attributes['name'] == 'apache'

# Generated at 2022-06-13 08:52:44.752243
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    class test_play:
        def __init__(self):
            self.basedir = '/'
        def _get_role_paths(self, role_name, role_basedir):
            return [role_basedir, 'files']

    FakeVariableManager = {'test_var1': 'test_value1', 'test_var2': 'test_value2', 'test_var3': 'test_value3'}
    from ansible.parsing.vault import VaultLib

    fake_loader = VaultLib()

    # Test for empty role
    role_path = '/roles/testRole1'
    role_data = '''---
    name:
    ...
    '''
    test_play_obj = test_play()

# Generated at 2022-06-13 08:52:53.172647
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    variable_manager = VariableManager()
    loader = DataLoader()
    play = Play().load(dict(hosts = ['localhost'], gather_facts = 'no'), variable_manager, loader)
    RoleInclude.load(dict(role='foo', tasks=dict(a='a')), play, None, None, variable_manager, loader)
    RoleInclude.load('foo', play, None, None, variable_manager, loader)
    RoleInclude.load(dict(role='foo'), play, None, None, variable_manager, loader)

# Generated at 2022-06-13 08:53:03.798443
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.parsing.vault import VaultLib
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    data = '''---
- name: 'test_role'
  become: yes
  vars:
    var1: Ansible
'''
 
    fake_loader = DictDataLoader({
        "/path/to/test_role/meta/main.yml": data
    })
    fake_inventory = InventoryManager(loader=None, sources=[])
    variable_manager = VariableManager(loader=fake_loader, inventory=fake_inventory)
    password = "123"

# Generated at 2022-06-13 08:53:10.782009
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    print("Unit test RoleInclude.load")

    import unittest
    import sys
    import os
    import os.path
    import yaml
    import tempfile
    import shutil
    import collections

    # Uncomment the following line to simplify debugging
    # AnsibleParserError.ERROR_STRINGS = {}

    class AnsiblePlaybookModuleTestCase(unittest.TestCase):

        def setUp(self):
            self.test_dir = tempfile.mkdtemp()
            self.yaml_file = os.path.join(self.test_dir, "ansible.yml")

        def tearDown(self):
            shutil.rmtree(self.test_dir)

        def load_data(self, data, variable_manager=None, loader=None):
            data = yaml.dump(data)

# Generated at 2022-06-13 08:53:14.527931
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source = dict(
            name = "Ansible Play",
            hosts = 'all',
            gather_facts = 'no',
            roles = [
                'testRole',
            ]
        )
    play = Play.load(play_source, loader=loader, variable_manager=variable_manager, inventory=inventory)

    current_role_path = 'testPath'
    parent_role = None
    collection_list = []
   

# Generated at 2022-06-13 08:53:15.169181
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:53:23.350032
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Using data from ansible/test/units/parsing/yaml/test_vault.yaml
    # Line '- name: test-vault-password-file'
    # Load RoleInclude using method load and verify value for _role_name
    # Expected Result:
    #   _role_name = 'test-vault-password-file
    data1 = '- name: test-vault-password-file'
    role_basedir = 'ansible/test/units/parsing/yaml/'
    play = None
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None

# Generated at 2022-06-13 08:53:31.005447
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

    # TODO: write tests for this method
    # Both kinds of data input should be tested
    # If it is a string, we need to check whether the string is empty or not
    # If it is a dict, we need to check whether the dict is empty or the type of its value etc.
    # If it is not the correct type, the exception should be raised
    # No return, since this function is not supposed to return anything


# Generated at 2022-06-13 08:53:37.862099
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude()
    try:
        ri.load([1,2,3,4,5])
        assert False
    except AnsibleParserError:
        assert True

    try:
        ri.load(['mysql,common'])
        assert False
    except AnsibleError:
        assert True

    # Test valid input values
    assert [ri.load('mysql'), ri.load(dict(role='mysql')), ri.load(AnsibleBaseYAMLObject('mysql'))]
    # Test invalid input values
    try:
        ri.load(None)
        assert False
    except AnsibleParserError:
        assert True

# Generated at 2022-06-13 08:53:48.220754
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])
    variable_manager = VariableManager(loader=loader)
    variable_manager.set_inventory(inventory)
    variable_manager._options.tags.extend(['ansible'])
    variable_manager._options.skip_tags.extend(['skip_ansible'])

# Generated at 2022-06-13 08:53:48.767539
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:53:59.260781
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import os
    import sys
    import collections
    import pytest
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.plugins.loader import lookup_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleError
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.template import Templar

    from ansible.module_utils import basic

    basic._ANSIBLE

# Generated at 2022-06-13 08:54:00.407388
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    print("RoleInclude_load")

# Generated at 2022-06-13 08:54:08.605530
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    
    # Unit tests to check method load of class RoleInclude
    # A test object of class RoleInclude is created 
    ri = RoleInclude()

    # Invalid role definition is passed as input  and it is checked that error is raised
    data = ["invalid role definition"]
    try:
        result = ri.load(data)
    except AnsibleParserError as e:
        print(e)
    else:
        print("RoleInclude.load(): Invalid role definition is passed as input and it is checked that error is not raised")

    # Invalid old style role requirement is passed as input and it is checked that error is raised
    data = "role: mysql,name: mysql"
    try:
        result = ri.load(data)
    except AnsibleError as e:
        print(e)
    else:
        print

# Generated at 2022-06-13 08:54:14.350186
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Test for correct load of allowlist
    data = {'allowlist': ['task-1', 'task-2'], 'block': [{'task-3': {'a': 1, 'b': 2}}]}
    ri = RoleInclude()
    ri.load_data(data)
    assert ri.tasks == [{'task-3': {'a': 1, 'b': 2}}]

    # Test for correct load of block
    data = {'block': [{'task-1': {'a': 1, 'b': 2}}, {'task-2': {'a': 1, 'b': 2}}]}
    ri = RoleInclude()
    ri.load_data(data)

# Generated at 2022-06-13 08:54:21.808889
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext

    pc = PlayContext()
    # Call the load method to instantiate the object and set its members
    ri = RoleInclude.load(data='role1', play=None, current_role_path=None, parent_role=None, variable_manager=None,
                        loader=None, collection_list=None)

    assert not isinstance(ri, RoleDefinition)

# Generated at 2022-06-13 08:54:29.804362
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    x = DataLoader()
    role_include_data = str({
        'name': 'test-role-include',
        'become': True,
        'hosts': 'all',
        'vars': {
            'role_var1': 'test_value'
        },
        'roles': [
            {
                'role': 'test-role-1',
                'role_var1': 'test_value1',
                'role_var2': 'test_value2'
            }
        ]
    })

    play1 = Play().load(role_include_data, variable_manager=VariableManager(), loader=x)

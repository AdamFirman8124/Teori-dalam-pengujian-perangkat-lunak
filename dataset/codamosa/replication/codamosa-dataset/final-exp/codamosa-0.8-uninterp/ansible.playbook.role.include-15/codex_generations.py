

# Generated at 2022-06-13 08:52:16.759561
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    context = PlayContext()
    loader = DataLoader()
    variable_manager = VariableManager(loader=loader, playcontext=context)

    play = Play().load({
          "name": "Ansible Play",
          "hosts": "localhost",
          "connection": "local",
          "gather_facts": "no"
        },
        variable_manager=variable_manager, loader=loader)


    # Loading an invalid role definition

# Generated at 2022-06-13 08:52:26.833328
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass


    # test_data = [
    #     {'name': 'geerlingguy.nginx', 'version': '1.9.0'},
    #     {'name': 'geerlingguy.nginx', 'version': '1.9.0', 'src': 'https://github.com/geerlingguy/ansible-role-nginx'},
    #     {'name': 'geerlingguy.nginx', 'version': '1.9.0', 'galaxy_info.author': 'geerlingguy', 'galaxy_info.description': 'foo'},
    #     {'name': 'geerlingguy.nginx', 'version': '1.9.0', 'private': True},
    #     {'name': 'geerlingguy.nginx', 'version': '1.9

# Generated at 2022-06-13 08:52:37.283891
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Create mock objects
    mock_data = {}
    mock_play = {}
    mock_current_role_path = {}
    mock_parent_role = {}
    mock_variable_manager = {}
    mock_loader = {}
    mock_collection_list = {}
    ri = RoleInclude(play=mock_play, role_basedir=mock_current_role_path, variable_manager=mock_variable_manager, loader=mock_loader, collection_list=mock_collection_list)

    ######### Test #########
    # Call method load of class RoleInclude
    # Test for excption
    raised = False

# Generated at 2022-06-13 08:52:40.100803
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Create an instance of class RoleInclude
    # Test when role definition is a string or a dict
    # Test when role definition is invalid
    pass

# Generated at 2022-06-13 08:52:48.899048
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ''' Load RoleInclude from YAML
    '''
    from ansible.playbook import Play
    from ansible.parsing.yaml.data import AnsibleDataLoader
    from ansible.vars.manager import VariableManager
    from ansible.errors import AnsibleParserError
    from ansible.utils.collection_loader import AnsibleCollectionLoader

    yaml_data = dict(
        name='role_name',
        description='role description',
        tasks=dict(main=dict(include=dict(role='other_role'))))

    # Create play
    play_obj = Play.load(yaml_data, seed_loader=AnsibleDataLoader())

    # Create variable manager
    vm = VariableManager()

    # Create loader
    loader = AnsibleCollectionLoader()

    # Create role include from YAML with appropriate

# Generated at 2022-06-13 08:52:57.939297
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    # Mock the role definition dictionary
    role_def = {
        'name': 'test_role',
        'tasks': [],
        'defaults': {},
    }

    # Mock the play class
    class PlayClass(object):
        pass
    play_obj = PlayClass()
    play_obj.collections = []

    # get the role definition object
    role_definition_obj = RoleInclude.load(role_def, play_obj)

    # check if the object has the expected properties
    assert role_definition_obj._role_path == 'test_role', "load() method returns an incorrect role_path"

# Generated at 2022-06-13 08:53:06.948281
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from io import StringIO
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import connection_loader
    from ansible.utils.vars import combine_vars
    from ansible.plugins.connection.ssh import Connection

    # Test load method of RoleInclude class
    #--------------------------------------
    loader = DataLoader()
    variable_manager = VariableManager()

# Generated at 2022-06-13 08:53:15.227580
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Data to load
    data = "role1"
    assert (isinstance(data, string_types) or isinstance(data, dict) or isinstance(data, AnsibleBaseYAMLObject)) == True

    # Assume no exception
    # AssertionError: 'Invalid old style role requirement: role1' != None
    #
    # Data to load
    data = "role1,role2"
    assert (isinstance(data, string_types) or isinstance(data, dict) or isinstance(data, AnsibleBaseYAMLObject)) == True

# Generated at 2022-06-13 08:53:26.742728
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    # environ to support fake_loader
    os.environ['ANSIBLE_ROLES_PATH'] = '../../../test/support/'
    os.environ['ANSIBLE_CONFIG'] = '../../../test/support/ansible.cfg'

    # test_role_definition_dump for available roles
    os.environ['ANSIBLE_LIBRARY'] = '../../../test/support/lib/'
    os.environ['ANSIBLE_FILTER_PLUGINS'] = '../../../test/support/filter_plugins/'
    os.environ['ANSIBLE_MODULE_UTILS'] = '../../../test/support/module_utils/'
    os.environ['ANSIBLE_MODULES'] = '../../../test/support/library:../../../test/support/module_utils/'

# Generated at 2022-06-13 08:53:38.153745
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    def dummy_load_data(data, variable_manager, loader):
        return data

    role_include_test = RoleInclude()
    role_include_test.load_data = dummy_load_data

    # Tests for normal values
    assert role_include_test.load('role1', None, None, None, None, None) == 'role1'
    assert role_include_test.load('~/role1', None, None, None, None, None) == '~/role1'
    assert role_include_test.load('{{ role1 }}', None, None, None, None, None) == '{{ role1 }}'
    assert role_include_test.load({ 'role': 'role1' }, None, None, None, None, None) == { 'role': 'role1' }

# Generated at 2022-06-13 08:53:46.003770
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = ['role1']
    play = None
    current_role_path =  None
    variable_manager = None
    loader = None
    collection_list = None
    assert RoleInclude.load(data, play, current_role_path, variable_manager=variable_manager, loader=loader, collection_list=collection_list)



# Generated at 2022-06-13 08:53:52.149421
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    class FakeDataLoader(object):
        pass

    class FakeVariableManager(object):
        pass

    class FakePlay(object):
        pass

    class FakeRole(object):
        def __init__(self):
            self.role_path = 'fake_role_path'
            self.roles = []

    fake_role = FakeRole()

    new_ri = RoleInclude.load(fake_role, FakePlay(), current_role_path=fake_role.role_path, parent_role=fake_role,
                              variable_manager=FakeVariableManager(), loader=FakeDataLoader())

    assert new_ri._role_path == fake_role.role_path
    assert new_ri._play is FakePlay
    assert new_ri._parent is fake_role




# Generated at 2022-06-13 08:54:00.908806
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Test case 1
    role_definition_1 = dict(role='test.test')
    play_1 = dict()
    current_role_path_1 = 'current_role_path'
    parent_role_1 = 'parent_role'
    variable_manager_1 = dict()
    loader_1 = 'loader'
    collection_list_1 = object()

    # Test case 2
    role_definition_2 = 'test.test'
    play_2 = dict()
    current_role_path_2 = 'current_role_path'
    parent_role_2 = 'parent_role'
    variable_manager_2 = dict()
    loader_2 = 'loader'
    collection_list_2 = object()

    # Test case 3
    role_definition_3 = 'test.test,another_test.test'

# Generated at 2022-06-13 08:54:09.034114
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    def check_load(data, name, playbook, parent_role):
        assert isinstance(data, str)
        assert data == name
        assert isinstance(playbook, object)
        assert playbook.get_name() == 'test_playbook'
        assert parent_role is None
        return True

    ri = RoleInclude()
    ri.load_data = lambda data, **kwargs:check_load(data, 'new_role', kwargs['play'], kwargs['parent_role'])

    # Test valid call
    result = RoleInclude.load('new_role', play=object(), current_role_path=os.path.join(os.path.dirname(__file__), 'data'))
    assert result

    # Test invalid call with invalid type for data

# Generated at 2022-06-13 08:54:20.033711
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.utils.path import unfrackpath

    import os
    from ansible.module_utils._text import to_bytes

    loader = DataLoader()
    current_dir = os.getcwd()
    current_path = unfrackpath(os.path.join(current_dir, 'test_data/test_roles/roles/test_role1'))
    play_context = PlayContext()

    inventory = InventoryManager(loader=loader)
    variable_manager = VariableManager(loader=loader, inventory=inventory)



# Generated at 2022-06-13 08:54:31.677420
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play

    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor.playbook_executor import PlaybookExecutor

    from units.mock.loader import DictDataLoader

    loader = DictDataLoader({'mock_foo': dict(
        hosts='webservers',
        roles=['mock_role1', 'mock_role2'],
    )})

    variable_manager = VariableManager()
    variable_manager.extra_vars = ImmutableDict({"hosts": "localhost"})


# Generated at 2022-06-13 08:54:38.427378
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

if __name__ == "__main__":
    import sys
    from ansible.module_utils import basic
    from ansible.module_utils.common.parameters import add_ansible_module_args
    from ansible.module_utils._text import to_bytes
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    try:
        basestring
    except NameError:
        basestring = (str, bytes)

    argument_spec = basic.handle_module_args()

    module = basic.AnsibleModule(
        argument_spec=argument_spec,
        # not checking because of daisy chain to file module
        bypass_checks=True,
    )

    add_ansible_module_args(module, argument_spec)

    pb_based

# Generated at 2022-06-13 08:54:49.844790
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert False, "TODO: Write a unit test"


    def _load_data(self, data, variable_manager=None, loader=None):
        if isinstance(data, string_types):
            include_data = dict(role=data)
        else:
            include_data = data

        self.name = include_data.get('name', None)

        if isinstance(data, string_types):
            role = RoleRequirement.load(data,
                                        parent_role=self.play,
                                        variable_manager=variable_manager,
                                        loader=loader)
            self.role_name = role
        else:
            if 'role' not in include_data:
                raise AnsibleParserError('Role include statements must contain a "role:" key')

# Generated at 2022-06-13 08:55:00.105437
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    target = [{'hosts': 'localhost', 'gather_facts': 'no', 'roles': [{'role': 'test', 'tags': ['test']},
                                                                    {'role': 'test', 'tags': ['test']}]}]

    data = [{'role': 'test', 'tags': ['test']},
            {'role': 'test', 'tags': ['test']}]

    assert len(target) == len(data)
    assert type(target) == type(data)

    for obj in data:
        role_path = "/home/alice/ansible/collections/ansible_collections/nsbl/test/roles/test"

# Generated at 2022-06-13 08:55:11.549117
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # data_input = [
    #     "jdoe.myapp"
    # ]
    data_input = "jdoe.myapp"

    # data_output = [
    #     {
    #         'name': 'jdoe.myapp'
    #     }
    # ]

    data_output = {
        'name': 'jdoe.myapp'
    }
    # load_ansible_error = [
    #     """Invalid role definition: 'jdoe.myapp'"""
    # ]
    load_ansible_error = """Invalid role definition: 'jdoe.myapp'"""
    # load_ansible_parser_error = [
    #     """Invalid role definition: 'jdoe.myapp'"""
    # ]

# Generated at 2022-06-13 08:55:22.724306
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Test 1
    data = 'test_role'
    playbook_vars = {}
    test_directory = os.path.realpath(os.path.dirname(__file__))
    current_role_path = os.path.join(test_directory, '../../../test/units/roles/test_role')
    current_role_path = os.path.realpath(current_role_path)
    current_role_path = os.path.join(current_role_path, '../')
    current_role_path = os.path.realpath(current_role_path)
    play = None
    ri = RoleInclude.load(data, play, current_role_path, None, playbook_vars, None, [])
    assert ri.get_name() == 'test_role'

    #

# Generated at 2022-06-13 08:55:28.243052
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # init the members
    play = RoleDefinition()
    current_role_path = "."
    parent_role = RoleDefinition()
    data = "name"

    # run the method
    result = RoleInclude.load(data, play, current_role_path, parent_role)

    # verifies
    assert result is not None
    assert isinstance(result, RoleInclude)


# Generated at 2022-06-13 08:55:34.368493
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = "foobar"
    play = {'roles': 'roles'}
    current_role_path = 'current_role_path'
    parent_role = 'parent_role'
    variable_manager = 'variable_manager'
    loader = 'loader'
    ri = RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader)

# Generated at 2022-06-13 08:55:40.274974
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    variable_manager = VariableManager()

    play1 = Play().load({
        'hosts': 'hosts',
        'roles': [ 'role1' ],
        'roles_path': './roles'
    }, variable_manager=variable_manager, loader=None)

    result = play1.compile()
    assert result == [{'role': 'role1', 'tags': [], 'when': ''}]

# Generated at 2022-06-13 08:55:45.998065
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # all needed imports
    import os
    import os.path
    import sys
    import tempfile
    import unittest

    # needed to fixate paths
    test_dir = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(os.path.dirname(test_dir))
    sys.path.append(os.environ.get("_MEIPASS2", os.path.abspath(os.path.join(test_dir, "..", ".."))))

    from ansible.playbook import Playbook
    from ansible.plugins import loader as pluginloader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # tests

# Generated at 2022-06-13 08:55:57.401837
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.utils import context_objects as co
    from ansible.vars.hostvars import HostVars
    from ansible.variables.manager import VariableManager

    from ansible.playbook.play import Play
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml import objects

    ri = RoleInclude()

    # Test case: data is not a string, dict or AnsibleBaseYAMLObject
    # Expected result: AnsibleParserError exception
    data = []
    play = Play.load(dict(name='test_play', hosts=['all']), variable_manager=VariableManager(), loader=co.DefaultLoader())

# Generated at 2022-06-13 08:56:03.649416
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.parsing.yaml.loader import AnsibleLoader

    RoleInclude.load(data = {}, play = "", current_role_path = "", parent_role = "", variable_manager = "", loader = AnsibleLoader(stream = ""))

# Generated at 2022-06-13 08:56:15.818475
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import json
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import RoleInclude
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # Load plugins
    get_all_plugin_loaders()

    # Create inventory
    inventory = InventoryManager(loader=None, sources='/tmp/ansible/hosts')

    # Create variable manager
    variable_manager = VariableManager(loader=None, inventory=inventory)

    # Create play

# Generated at 2022-06-13 08:56:23.853653
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_loader(loader)

    variable_manager.set_inventory(Inventory(loader=loader, variable_manager=variable_manager, host_list=['hostname']))

    pc = PlayContext()

    mock_data = b'---\nhosts: webservers\nroles: abc.def'
    mock_data_dict =  yaml.safe_load(mock_data)
    mock_loader = mock.Mock()

    ri = RoleInclude()

# Generated at 2022-06-13 08:56:25.013517
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert RoleInclude.load("test", None) == None

# Generated at 2022-06-13 08:56:44.526503
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    current_role_path = './tests/roles/testRole/'
    play = 'play'
    variable_manager = 'variable_manager'
    loader = 'loader'
    collection_list = 'collection_list'
    r = RoleInclude.load('foobar', play, current_role_path, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
    assert isinstance(r, RoleRequirement), "Not an instance of RoleRequirement."
    assert r._role_name == 'foobar', "Role name not set without options."



# Generated at 2022-06-13 08:56:52.586070
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    class Play(object):
        def __init__(self):
            self.hostvars = {}
        def __getattr__(self, item):
            return None
        def get_variable_manager(self):
            return self.variable_manager
    class VariableManager(object):
        def __init__(self):
            self.host_vars = {}
            self.group_vars = {}
            self.extra_vars = {}
            self.vars_cache= {}
        def set_host_variable(self, host, varname, value):
            self.host_vars[host][varname] = value
        def get_vars(self, loader=None, play=None, host=None, task=None, include_delegate_to=False):
            return {}

# Generated at 2022-06-13 08:57:00.096161
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    # Testing the load method of RoleInclude class
    # Arrange
    import yaml
    yaml.warnings({'YAMLLoadWarning': False})
    data = "role: git"
    current_role_path = '.'
    variable_manager = None
    loader = None
    collection_list = []
    p = Play()

    # Act
    ri = RoleInclude.load(data, p, current_role_path, None, variable_manager, loader, collection_list)

    # Assert
    assert ri._role_name == 'git'
    assert ri._role_path == '.'
    assert ri._role_collection_name == None

# Generated at 2022-06-13 08:57:01.052373
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass


# Generated at 2022-06-13 08:57:11.172554
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.module_utils.six import StringIO

    # Prepare Ansible objects
    test_data = StringIO()
    test_data.write(u'static_yaml: "hi"')
    test_data.seek(0)


# Generated at 2022-06-13 08:57:27.422655
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)
    inventory.clear_pattern_cache()
    play_context = PlayContext(variables=variable_manager)
    play_context._prompt = dict(become_pass=dict(default='test'))
    play_context._always_prompt = dict(become_pass=dict(default='test'))
    play_context._acquire_priv_password = dict(default='test')
    #  play_context._

# Generated at 2022-06-13 08:57:35.002117
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Test for the case when loading is successful
    # Given:
    loader = DictDataLoader({
        os.path.join(os.getcwd(), 'test_role_include_load.yml'):
        """
        - include_role:
            name: test_role
        """,
        os.path.join(os.getcwd(), 'roles', 'test_role', 'tasks', 'main.yml'):
        """
        - name: test role task
          debug:
            msg: hello world
        """
    })
    pi = PlaybookInclude(play=Play(), loader=loader)
    ri = RoleInclude(play=pi)
    # When:
    role = ri.load("test_role_include_load.yml", loader=loader)
    # Then:
   

# Generated at 2022-06-13 08:57:46.462373
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = 'role_name,host1,host2'
    role_name = 'role_name'
    variable_manager = 'variable_manager'
    loader = 'loader'
    collection_list = 'collection_list'

    class Play(object):
        variable_manager = variable_manager
        loader = loader
        collection_list = collection_list
        def __init__(self):
            self.roles = []
            self.role_paths = ['role_paths']
            self.role_names = ['role_names']

    role_inlcude = RoleInclude.load(data, Play, variable_manager=variable_manager, loader=loader, collection_list=collection_list)

    assert role_inlcude.name == role_name

# Generated at 2022-06-13 08:57:51.367712
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    # TODO:
    #   - test a case: data is an instance of class AnsibleBaseYAMLObject
    #   - test a case: data is a string_types with comma, should raise AnsibleError
    #   - test a case: data is not a string_types or dict or AnsibleBaseYAMLObject, raise AnsibleParserError
    pass
# Class RoleInclude

# Class RoleRequirement

# Generated at 2022-06-13 08:57:57.792889
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=[])
    play_context = PlayContext()

    play = Play()
    play._variable_manager = variable_manager
    play._loader = loader
    play._inventory = inventory

    block = Block(play=play)
    templar = Templar(loader=loader, variables=variable_manager)
    block._templar = templar


# Generated at 2022-06-13 08:58:33.114809
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    class FakeVariableManager(object):
        def __init__(self, argument):
            super(FakeVariableManager, self).__init__()

    class FakeLoader(object):
        def __init__(self, argument):
            super(FakeLoader, self).__init__()

    class FakePlay(object):
        def __init__(self, variable_manager, loader):
            super(FakePlay, self).__init__()

    variable_manager = FakeVariableManager('test')
    loader = FakeLoader('test')
    play = FakePlay(variable_manager, loader)
    role_basedir = 'test'
    # Test valid role name
    data = {
        'role1': {'attributes': {}},
        'role2': {'attributes': {}},
    }

# Generated at 2022-06-13 08:58:47.073232
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = "foobar"
    play = {}
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None

    ri = RoleInclude(play=play, role_basedir=current_role_path, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
    ri.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)

    assert (isinstance(ri, RoleInclude))

    data = {"foobar": "test"}
    ri = RoleInclude(play=play, role_basedir=current_role_path, variable_manager=variable_manager, loader=loader, collection_list=collection_list)

# Generated at 2022-06-13 08:58:57.863881
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    '''
        Unit test for method load of class RoleInclude
    '''
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # set up the play context
    loader = DataLoader()
    variable_manager = VariableManager()
    play_context = PlayContext()

    # list of supported Ansible types
    valid_types = ['command', 'shell', 'shell_command']
    # list of unsupported Ansible types
    invalid_types = ['lineinfile', 'blockinfile']

    # check if the object RoleInclude is a subclass of object RoleDefinition
    assert issubclass(RoleInclude, RoleDefinition)

    # check if

# Generated at 2022-06-13 08:59:02.093804
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

    # TODO: better test
    #ri = RoleInclude(play = None)
    #ri.load_data(data = 'ansible.builtin.yum', variable_manager = None, loader = None) # TODO: test call to load_data of parent class
    #assert isinstance(ri, RoleInclude)

# Generated at 2022-06-13 08:59:07.475942
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    print('Test load')
    play = None
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None
    data = {
        'role': 'test_name',
        'name': 'test_name',
        'include': 'test_include'
    }
    role = RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    assert role['name'] == 'test_name'
    assert role['include'] == 'test_include'



# Generated at 2022-06-13 08:59:14.270762
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.role import ROLE_CACHE
    # test_data contains the input data under test.

# Generated at 2022-06-13 08:59:31.493152
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.playbook import Play
    import os

    # Testing load method
    ###############################################################################################

    # Loading a simple string
    fake_loader = AnsibleLoader(None, False, None)
    fake_data = "simple"
    fake_variable_manager = VariableManager()
    fake_play = Play.load(dict(name="fake_play", hosts=[]), loader=fake_loader, variable_manager=fake_variable_manager, use_task_vars=True)
    fake_collection_list = None

# Generated at 2022-06-13 08:59:34.791078
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude()
    ri.load(data=dict(name="RoleIncludeName"), loader=dict(path_mapper=dict(loader1="path")))
    assert ri.name == "RoleIncludeName"
    assert ri._loader.path_mapper == dict(loader1="path")


# Generated at 2022-06-13 08:59:40.565930
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    # Initialization of a new PlayContext
    task_vars = dict(
        example='ansible',
        ansible_connection='local',
        ansible_python_interpreter='/usr/bin/python3',
        ansible_user=os.environ['USER']
    )
    variable_manager = VariableManager()
    variable_manager.extra_vars = task_vars
    loader = DataLoader()


# Generated at 2022-06-13 08:59:49.450423
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """Test load method of class RoleInclude
    """
    data = {'name': 'foobar'}
    play = None
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None
    ri = RoleInclude(play=play, role_basedir=current_role_path,
            variable_manager=variable_manager, loader=loader,
            collection_list=collection_list)
    role = ri.load(data)

    assert role.get_name() == 'foobar'
    assert role.get_role_path() == 'foobar'

# Generated at 2022-06-13 09:00:50.178456
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    # Check role without role_path
    data = "myrole"
    ri = RoleInclude()

    try:
        result = ri.load(data)
    except AnsibleParserError as e:
        result = e
    assert str(result) == "Invalid role definition: myrole"

    # Check role with role_path
    data = "myrole"
    ri = RoleInclude(role_basedir="roles_path")

    try:
        result = ri.load(data)
    except AnsibleParserError as e:
        result = e
    assert str(result) == "Invalid role definition: myrole"

    # Check role without role_path
    data = {}
    ri = RoleInclude()


# Generated at 2022-06-13 09:00:59.517517
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    play_context = PlayContext()
    variable_manager = VariableManager(loader=None, inventory=InventoryManager(loader=None, sources=[]))
    roleInclude = RoleInclude(play=None, role_basedir=".", variable_manager=variable_manager, loader=None, collection_list=None)
    assert isinstance(roleInclude.load(data=None, play=None, current_role_path=".", parent_role=None, variable_manager=variable_manager, loader=None, collection_list=None), AnsibleParserError)

# Generated at 2022-06-13 09:01:05.696265
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import load_extra_vars
    from ansible.cli.color import stringc
    from ansible.utils.display import Display
    import ansible.constants as C
    import os
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.utils.path import unfrackpath

    def display(msg):
        print(stringc(msg, C.COLOR_ERROR))

    display = Display()
    parser = C.DEFAULT_YAML_PARSER


# Generated at 2022-06-13 09:01:07.984752
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # TODO: write unit test for method load of class RoleInclude
    pass

# Generated at 2022-06-13 09:01:24.771633
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import ansible.utils.module_docs as md
    from ansible.module_utils import basic
    class MyLoader():
        @staticmethod
        def load_from_file(self, file_name):
            return False
    class MyAttribute():
        pass
    class MyVariableManager():
        pass
    loader = MyLoader()
    variable_manager = MyVariableManager()
    attribute = MyAttribute()
    md.find_module_path = lambda x,y: '/home/test'
    ri = RoleInclude()
    assert ri.load(None, None, loader=loader, variable_manager=variable_manager) == False
    assert ri.load('', None, loader=loader, variable_manager=variable_manager) == False

# Generated at 2022-06-13 09:01:29.534910
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play import Play
    from ansible.vars import VariableManager

    play = Play()
    variable_manager = VariableManager()
    variable_manager._options = {'roles_path': '/home/user/.ansible/roles'}

    data = {'name': 'test', 'roles': ['role1']}

    role = RoleInclude.load(
        data=data,
        play=play,
        variable_manager=variable_manager
    )
    assert role._role_name == 'role1'



# Generated at 2022-06-13 09:01:34.400645
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """ unit test for method load of class RoleInclude
    """
    import pytest

    ri = RoleInclude()
    data = {'test': 'test'}
    with pytest.raises(AnsibleError) as ex:
        ri.load(data)
    assert "VariableManager not defined." in str(ex.value)

# Generated at 2022-06-13 09:01:35.694713
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert False, "Not implemented yet"

# Generated at 2022-06-13 09:01:46.917712
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # pylint: disable=redefined-outer-name
    import mock

    def _return_value(attr):
        return attr

    def _return_none(attr):
        return None

    def _return_role_basedir():
        return 'roles/role'

    def _return_contained_in_role_basedir():
        return 'roles'

    def _return_empty_list():
        return []

    def _return_empty_dict():
        return {}

    def _raise_AnsibleError():
        raise AnsibleError


# Generated at 2022-06-13 09:01:57.604567
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    p = Play().load({
        'hosts'      : 'all',
        'connection' : 'local',
        'gather_facts': 'no',
        'roles'      : [
            {'role': 'foo'},
            'bar'
        ]
    })
    pc = PlayContext()
    p.set_loader(null_loader)
    p.set_variable_manager(variable_manager)
    p.set_basedir('/home/nperez/ansible/lib/ansible/playbooks')

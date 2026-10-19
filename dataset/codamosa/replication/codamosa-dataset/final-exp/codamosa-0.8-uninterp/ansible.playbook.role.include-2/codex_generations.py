

# Generated at 2022-06-13 08:52:15.592603
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.constants import DEFAULT_HASH_BEHAVIOUR
    from ansible.utils.vars import combine_vars

    import os
    import pytest


    play_context = PlayContext()
    fixture_hostvars = dict(
        ansible_all_ipv4_addresses=['10.0.0.1'],
        ansible_hostname='foo',
        ansible_all_ipv6_addresses=[])

# Generated at 2022-06-13 08:52:23.315258
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = {}
    play = {}
    current_role_path = "/home/dku/RP/ansible/ansible/playbooks/library/mqtt.py"
    parent_role = None
    variable_manager = {}
    loader = {}
    collection_list = []

    rd = RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    assert rd

# Generated at 2022-06-13 08:52:34.739063
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert RoleInclude.load('nginx', play=None, current_role_path=None, parent_role=None, variable_manager=None, loader=None, collection_list=None).__dict__ == {'_role_name': 'nginx', '_role_path': None, '_role_collection': None, '_role_collection_name': None, 'play': None, '_parent_role': None, '_metadata': None, '_variable_manager': None, '_loader': None, '_task_blocks': [], '_handlers': [], '_default_vars': {}, '_role_default_vars': {}, '_role_params': {}, '_dependencies': [], '_collections': [], '_dep_errors': {}}

# Generated at 2022-06-13 08:52:46.322650
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook import Play
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    data = {'test': 'value'}

    play = Play()
    current_role_path = 'role_basedir'
    parent_role = RoleRequirement()
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    play.set_loader(loader)
    play.set_variable_manager(variable_manager)
    play.set_inventory(inventory)


# Generated at 2022-06-13 08:52:50.130350
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    ri = RoleInclude()


    assert ri.load({"role": "common", "foo": "bar"}, None) is not None


#  Unit test for method load of class RoleInclude with error 'Invalid role definition'

# Generated at 2022-06-13 08:52:51.009484
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass


# Generated at 2022-06-13 08:52:52.032744
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # TODO
    assert True

# Generated at 2022-06-13 08:53:02.733351
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import os

    # setup for test
    test_path = 'test/fixtures/role-include/'
    fixture = 'role-include.yml'
    loaded_data = os.path.join(test_path, fixture)
    foo = RoleInclude.load(loaded_data, play='test', current_role_path=test_path, variable_manager=os.path.join(test_path, 'var.yml'), loader=os.path.join(test_path, 'roles.yml'), collection_list=os.path.join(test_path, 'collection_list'))

    # test the data
    assert 'role1' == foo.get_name()
    assert 'role2' == foo.get_name()
    assert 'role3,role4' == foo.get_name()

# Generated at 2022-06-13 08:53:12.497648
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play

    variable_manager=None
    loader=None

    yaml_data="""
- hosts: all
  gather_facts: no
  become: yes
  roles:
    - role: foo
    - role: bar
    - role: baz
    - role: zoo
      become: no
    - role: zab
      become: no
      delegate_to: localhost
    """

    play_ds = dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        become = 'yes',
        roles = [ "foo", "bar", "baz", dict( role="zoo", become="no" ), dict( role="zab", become="no", delegate_to="localhost" ) ]
        )

# Generated at 2022-06-13 08:53:14.918383
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = { 'name': 'role1', 'role_path': '/'}
    ri = RoleInclude.load(data, {})
    assert(ri._role_name == 'role1')


# Generated at 2022-06-13 08:53:18.298667
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:53:19.513886
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    assert False, 'No tests defined'


# Generated at 2022-06-13 08:53:32.291245
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    play_context = PlayContext()
    tqm = None
    variable_manager = VariableManager()
    loader = DataLoader()
    role_definition = RoleInclude(play=None, role_basedir=None, variable_manager=variable_manager, loader=loader, collection_list=None)

    data = "geerlingguy.apache"
    assert role_definition.load(data, play=play_context, current_role_path=None, parent_role=None, variable_manager=variable_manager, loader=loader, collection_list=None) is None

# Generated at 2022-06-13 08:53:33.162406
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert 0, "Test not implemented"

# Generated at 2022-06-13 08:53:40.636263
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    ri = RoleInclude()

    # required is missing
    test_data = dict(tasks='test/tasks')
    ri.load(test_data)
    assert(ri.required == False)

    # required is True
    test_data = dict(required=True, tasks='test/tasks')
    ri.load(test_data)
    assert(ri.required == True)

    # required is False, should not override True
    test_data = dict(required=False, tasks='test/tasks')
    ri.load(test_data)
    assert(ri.required == True)

    # role names are

# Generated at 2022-06-13 08:53:49.800792
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    class Play(object):
        def __init__(self, role_paths=['/test']):
            self._role_paths = role_paths

        @property
        def role_paths(self):
            return self._role_paths

    role_paths = ['/test']
    play = Play(role_paths=role_paths)
    current_role_path = '/test'
    parent_role = None

    class VariableManager(object):
        pass

    variable_manager = VariableManager()

    class Loader(object):
        pass

    loader = Loader()

    class CollectionList(object):
        pass

    collection_list = CollectionList()

    data = 'test_role'

# Generated at 2022-06-13 08:53:59.783383
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.play import Playbook

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='localhost,')
    variable_manager.set_inventory(inventory)

    play = Play().load({
        'name': 'test play',
        'hosts': 'localhost',
        'connection': 'local',
        'gather_facts': 'yes',
    }, variable_manager=variable_manager, loader=loader)

    include = RoleInclude.load(
        'role1',
        play=play
    )


# Generated at 2022-06-13 08:54:04.845216
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    
    loader = None
    collection_list = None
    play_data = dict()
    data = dict()
    current_role_path = "test_current_role_path"
    parent_role = None
    variable_manager = None

    ri = RoleInclude.load(data, play_data, current_role_path, parent_role, variable_manager, loader, collection_list)
    assert isinstance(ri, RoleInclude)

# Generated at 2022-06-13 08:54:08.329086
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    role_include = RoleInclude()
    role_include.load('role1', 'play1', 'roles/role1', 'role2', 'var_manager1', 'loader1', 'collections1')
    assert role_include.get_name() == 'role1'

# Generated at 2022-06-13 08:54:19.227922
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    current_role_path = ''
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None

    # Test the first case
    data = '[role1, role2]'
    try:
        RoleInclude.load(data, None, current_role_path, parent_role, variable_manager, loader, collection_list)
    except AnsibleError as e:
        assert 'Invalid old style role requirement' in to_native(e)

    # Test the second case
    data = '{name: myrole}'
    try:
        RoleInclude.load(data, None, current_role_path, parent_role, variable_manager, loader, collection_list)
    except AnsibleParserError as e:
        assert 'Invalid role definition' in to_native(e)

    # Test the

# Generated at 2022-06-13 08:54:34.745272
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    variable_manager = DummyVarsModule()
    loader = DummyVarsModule()
    role_basedir = './roles'
    play = DummyVarsModule()
    play.ROLE_CACHE = {}
    play.basedir = os.path.join(os.path.dirname(__file__), 'play')
    data = "role1"
    ri = RoleInclude(play=play, role_basedir=role_basedir, variable_manager=variable_manager, loader=loader)
    ri.load(data, play=play, current_role_path=role_basedir, variable_manager=variable_manager, loader=loader)
    print(ri.get_name())
    print(ri.get_vars())

if __name__ == '__main__':
    test_Role

# Generated at 2022-06-13 08:54:40.835840
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.collection_loader import AnsibleCollectionRef
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.plugins.loader import role_loader
    from ansible.utils.vars import combine_vars

    role_path = '/tmp/my-role'
    role_data = {
        'name': 'my-role',
        'collections': [
            AnsibleCollectionRef.from_string('ns.coll'),
        ],
    }

    loader = DataLoader()
    variable_manager = VariableManager()
    play = Play()
    play.hosts = ['localhost']
    play.hosts.vars = {}


# Generated at 2022-06-13 08:54:51.332832
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.playbook.task.include_role import TaskIncludeRole

    role_path = os.path.dirname(os.path.dirname(__file__))
    role_name = os.path.basename(os.path.dirname(role_path))
    current_role_path = os.path.join(role_path, "roles")


# Generated at 2022-06-13 08:54:53.178122
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass


# Generated at 2022-06-13 08:55:00.232000
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play import Play
    from ansible.module_utils.six import PY3
    if PY3:
        # See https://docs.python.org/3/library/unittest.mock.html
        from unittest.mock import patch
    else:
        from mock import patch

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    class RoleMock:
        def get_path(self):
            return 'roles/role_sample_1'

    with patch.object(RoleRequirement, 'get_role') as get_role_mock:
        get_role_mock.return_value = RoleMock()
       

# Generated at 2022-06-13 08:55:11.647454
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    play_context = PlayContext()
    play_context.connection = 'local'
    play_source =  dict(
            name = "Ansible Play",
            hosts = 'all',
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module='shell', args='ls'), register='shell_out'),
                dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
             ]
        )
    play = Play().load(play_source, variable_manager=VariableManager(), loader=None)
    # Return data from method load
    data = dict(name="test")
    role

# Generated at 2022-06-13 08:55:19.773567
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    pb = Play().load({
        'name': 'test',
        'hosts': 'all',
        'roles': 'test1,test2'
    }, variable_manager=VariableManager(), loader=DataLoader())

    rd: RoleDefinition = RoleInclude.load('test1', pb)
    assert(rd.get_name() == 'test1')

    rd: RoleDefinition = RoleInclude.load('test2', pb)
    assert(rd.get_name() == 'test2')


# Generated at 2022-06-13 08:55:30.087739
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import ansible.parsing.yaml.objects

    data = 'role_name'
    play = None
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None

    rg = RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    assert(isinstance(rg, RoleInclude))

    data = 'role_name,'
    play = None
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None

    matched = False

# Generated at 2022-06-13 08:55:30.683456
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:55:40.158890
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    import os
    import tempfile

    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    example_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'examples'))

    # create tmp directory
    temp_path = tempfile.mkdtemp()

    # copy example roles
    command = "cp -r %s/* %s/." % (example_path, temp_path)
    os.system(command)


# Generated at 2022-06-13 08:56:00.258137
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.manager import VariableManager
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.inventory.manager import InventoryManager

    inv_data = {
      "all": {
        "hosts": {
          "localhost": {
            "playbook_dir": "/playbook"
          }
        }
      }
    }

    loader_data = {
      "inventory": inv_data
    }

    # Define variable manager
    variable_manager = VariableManager()

    # Define Inventory
    inventory = InventoryManager(loader=loader_data, variable_manager=variable_manager)
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 08:56:15.516152
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    import copy
    from ansible.parsing.yaml.loader import AnsibleLoader

    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.vars.manager import VariableManager

    loader = AnsibleLoader(None, None, None)

    # Make a dictionary with all the options

# Generated at 2022-06-13 08:56:21.955521
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Initialization part
    play = None
    current_role_path = None
    parent_role = None
    variable_manager = None
    loader = None
    collection_list = None
    # Test part
    test_obj=RoleInclude.load(data="test_string", play=play, current_role_path=current_role_path, parent_role=parent_role, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
    print(test_obj)
    
if __name__ == '__main__':
    test_RoleInclude_load()

# Generated at 2022-06-13 08:56:32.721376
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass


    # def _load(self, data, variable_manager=None, loader=None):
    #     '''
    #     We're overriding the base load() method for RoleDefinitions,
    #     so we can call the base load() and then make additional
    #     modifications.
    #     '''
    #
    #     # first, load the role definition
    #     super(RoleInclude, self)._load(data, variable_manager=variable_manager, loader=loader)
    #
    #     # if this is a string, then it's a single role with no params
    #     if isinstance(data, string_types):
    #         self._role_name = data
    #
    #     # otherwise, it's a hash
    #     else:
    #         # get the name from the hash
   

# Generated at 2022-06-13 08:56:33.270658
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:56:33.870328
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    RoleInclude.load()

# Generated at 2022-06-13 08:56:40.668409
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play import Play
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Host(name='host1')
    variable_manager.set_inventory(inventory)
    play_source = dict(
        name="test_play",
        hosts='host1',
        gather_facts='no',
        roles=[]
    )
    play = Play.load(play_source, variable_manager=variable_manager, loader=loader)
    current_role_path = "/some/path/to/role"

# Generated at 2022-06-13 08:56:50.165558
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    variable_manager.set_inventory(InventoryManager(loader=DataLoader(), sources=['test/inventory']))

    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    play = Play().load({
        'name': 'Ansible Playbook',
        'hosts': 'localhost',
        'tasks': [
            {
                'import_tasks': 'include_role.yml'
            },
        ]}, variable_manager=variable_manager, loader=DataLoader())

    delegatetofieldattribute = Attribute()

# Generated at 2022-06-13 08:57:00.968198
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    myloader = None
    myplay = None
    myvariable_manager = None
    mycurrent_role_path = None
    myparent_role = None
    mycollection_list = None
    myrole = RoleInclude.load(data = 'test', play = myplay, current_role_path = mycurrent_role_path, parent_role = myparent_role, variable_manager = myvariable_manager, loader = myloader, collection_list = mycollection_list)
    assert myrole


# Generated at 2022-06-13 08:57:09.584480
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import re
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    
    def hosts_pattern_callback(host):
        return Host(host)

    loader = DataLoader()
    variable_manager = VariableManager(loader=loader, inventory=InventoryManager(loader=loader, sources=["/home/david/my-ansible/test-inventory"]))


# Generated at 2022-06-13 08:57:37.981960
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass


# Generated at 2022-06-13 08:57:48.119441
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    p = Play()
    c = PlayContext(p)
    v = VariableManager(loader=None, inventory=None, version_info=None)

    result = RoleInclude.load({'name': 'myrole', 'role': 'myrole'}, play=p, variable_manager=v)
    assert isinstance(result, RoleRequirement)

# Generated at 2022-06-13 08:57:54.992358
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import load_extra_vars
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.display import Display
    from ansible.plugins.loader import find_plugin, enable_plugins
    from ansible.plugins.loader import plugin_loader
    from ansible.template import Templar
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    class AnsibleOptions(object):

        def __init__(self):
            self.verbosity = 0
            self

# Generated at 2022-06-13 08:57:58.333819
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    assert RoleInclude.load('test') == 'test'
    assert RoleInclude.load('test,') == 'test'
    assert RoleInclude.load('test,ansible') == 'test'

# Generated at 2022-06-13 08:57:58.944281
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:58:07.523947
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import plugin_loader
    import ansible.constants as C
    import os

    cwd = os.getcwd()


# Generated at 2022-06-13 08:58:13.176952
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.parsing.yaml import objects

# Generated at 2022-06-13 08:58:23.970343
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import json

    play = {
        'hosts':             'all',
        'gather_facts':      'no',
        'connection':        'local',
        'roles':             [],
        'tasks':             [],
        'handlers':          [],
        'vars':              [],
    }
    current_role_path = '/tmp/test_ansible_1'
    parent_role = {'name': 'test_ansible_role_1'}
    variable_manager = object()
    loader = object()

    roleInclude_1 = None

# Generated at 2022-06-13 08:58:24.870191
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:58:40.258625
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    play = 'test'
    data = 'test'
    current_role_path = 'test'
    parent_role = 'test'
    variable_manager = 'test'
    loader = 'test'
    collection_list = 'test'
    ri = RoleInclude(play=play, role_basedir=current_role_path, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
    assert ri.load_data(data, variable_manager=variable_manager, loader=loader)
    assert ri.load(data, play, current_role_path=current_role_path, parent_role=parent_role, variable_manager=variable_manager, loader=loader, collection_list=collection_list)

# Generated at 2022-06-13 08:59:48.332001
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import unittest
    import sys
    import os
    import tempfile
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'lib')))
    import ansible
    from ansible.errors import AnsibleError
    from ansible.module_utils.six import iteritems
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.requirement import RoleRequirement
    from ansible.module_utils._text import to_native
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

# Generated at 2022-06-13 08:59:55.882790
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext

    play_context = PlayContext()

    ri = RoleInclude(play=play_context, role_basedir=None, variable_manager=None, loader=None, collection_list=None)
    data = ri.load(data='defaults/main.yml', play=play_context,
        current_role_path=None, parent_role=None, variable_manager=None,
        loader=None, collection_list=None)

    assert(data is not None)

# Generated at 2022-06-13 09:00:04.888652
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    class FakePlay(object):
        pass

    fake_play = FakePlay
    fake_play.name = "fake_play"

    fake_variable_manager = ""
    fake_loader = ""

    # Test case 1
    print()
    data = 123
    ri = RoleInclude(play=fake_play, role_basedir="fake_basedir", variable_manager=fake_variable_manager, loader=fake_loader)
    try:
        ri.load(data, play=fake_play, current_role_path="fake_current_role_path", parent_role="parent_role", variable_manager=fake_variable_manager, loader=fake_loader)
    except AnsibleParserError as e:
        print(e)

    # Test case 2
    print()
    data = "role1,role2"
   

# Generated at 2022-06-13 09:00:09.435167
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude()
    # Raise exception when data is not a string
    try:
        ri.load(1,1,1,1,1,1)
    except Exception as e:
        assert isinstance(e, AnsibleParserError)

    # Raise exception when data is not a string
    try:
        ri.load('1,1',1,1,1,1,1)
    except Exception as e:
        assert isinstance(e, AnsibleError)


RoleInclude.init()

# Generated at 2022-06-13 09:00:12.006344
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    role = RoleInclude.load('test-role', {}, variable_manager=None, loader=None, collection_list=None)
    assert isinstance(role, RoleRequirement) is True
    assert role.get_name() == 'test-role'

# Generated at 2022-06-13 09:00:19.941814
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    role_basedir = os.path.join(os.path.dirname(__file__), 'test_role_include')
    data = {"name": "test_role_include", "tasks": []}
    ri = RoleInclude.load(data, play=None, current_role_path=role_basedir, parent_role=None, variable_manager=None, loader=None, collection_list=None)

    assert ri.name == 'test_role_include'
    assert isinstance(ri.tasks, list)

# Generated at 2022-06-13 09:00:28.089629
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

    # Load all methods of class RoleInclude decorated with @role_include_argument_spec with their spec and apply those
    #  to the instance of class RoleInclude
    # Consider only those methods of class RoleInclude which are not defined in abc.ABCMeta
    # or its super classes
    # Apply only those methods which do not start with underscore(_)
    # Apply only those attributes of class RoleInclude which are public (do not start with underscore(_))

    # Find list of methods of class RoleInclude which are decorated with @role_include_argument_spec
    # Consider only those methods of class RoleInclude which are not defined in abc.ABCMeta
    # or its super classes

# Generated at 2022-06-13 09:00:35.630676
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    fake_loader = object()
    fake_variable_manager = object()
    ri = RoleInclude()
    data = { 'role': 'foo', 'vars': { 'a': 'b' } }
    ri = RoleInclude.load(data, 'play', variable_manager=fake_variable_manager, loader=fake_loader)
    assert ri.get_name() == 'foo'
    assert ri.vars == { 'a': 'b' }
    assert ri.loader == fake_loader
    assert ri.variable_manager == fake_variable_manager


# Generated at 2022-06-13 09:00:44.596882
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Setup test data
    play = AnsibleBaseYAMLObject()
    current_role_path = "/home/user/ansible/roles/role1"
    parent_role = None
    variable_manager = AnsibleBaseYAMLObject()
    loader = AnsibleBaseYAMLObject()
    collection_list = AnsibleBaseYAMLObject()

    # Test a string type data
    data = "role1"
    test_instance = RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    assert isinstance(test_instance, RoleInclude) == True

    # Test a dict type data
    data = {'roles': 'role1'}

# Generated at 2022-06-13 09:00:54.700511
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.plugins.loader import get_all_plugin_loaders

    t1 = '''
    - hosts: all
      gather_facts: no
      roles:
        - role: A
          vars:
            extra_stuff: 1
            extra_stuff2: 2
        - role: B
    '''

    loader = AnsibleLoader(get_all_plugin_loaders(), 'test_data/test_role_include')
   


# Generated at 2022-06-13 08:41:55.875245
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleVaultEncryptedUnicode
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.loader import AnsibleLoader
    import yaml

    yaml.add_multi_constructor('!vault', AnsibleVaultEncryptedUnicode.from_yaml)


# Generated at 2022-06-13 08:42:05.261000
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_definition = RoleDefinition()
    role_definition._role_collection = 'namespace.collection'
    role_definition.role = 'role_name'
    assert role_definition.get_name() == 'namespace.collection.role_name'
    assert role_definition.get_name(False) == 'role_name'
    role_definition._role_collection = None
    assert role_definition.get_name() == 'role_name'
    role_definition.role = None
    assert role_definition.get_name() is None

# Generated at 2022-06-13 08:42:14.470207
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    display.verbosity = 2

    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager

    class Object(object):
        pass

    variable_manager = VariableManager()
    variable_manager.extra_vars = dict()
    variable_manager.options_vars = dict()
    variable_manager._options = dict()
    variable_manager.set_options(variable_manager._options)
    variable_manager.host_vars = dict()
    variable_manager.group_vars = dict()
    variable_manager.set_group_vars(variable_manager.group_vars)
    variable_manager.set_host_variable(variable_manager.host_vars)

    c = Object()
    c.name = 'localhost'
    c.port = 22

# Generated at 2022-06-13 08:42:24.467519
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext

    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.inventory.host import Host

    # define some default values
    collection_name = 't.c.1'
    role_name = 'test'
    role_params = {
        'test_param': 'test',
    }
    role_def = AnsibleUnicode(u'%s.%s' % (collection_name, role_name))

    # define the default playbook we will use

# Generated at 2022-06-13 08:42:31.285636
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    result = RoleDefinition().preprocess_data(dict(role='myrole'))
    assert 'role' in result
    assert result['role'] == 'myrole'
    result = RoleDefinition().preprocess_data(dict(name='myrole'))
    assert 'role' in result
    assert result['role'] == 'myrole'
    result = RoleDefinition().preprocess_data(dict(name='myrole', foo='bar'))
    assert 'role' in result
    assert result['role'] == 'myrole'
    assert 'foo' in result
    assert result['foo'] == 'bar'
    result = RoleDefinition().preprocess_data(dict(role='myrole', foo='bar'))
    assert 'role' in result
    assert result['role'] == 'myrole'
    assert 'foo' in result

# Generated at 2022-06-13 08:42:43.958017
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    data = """
    - name: test-playbook
      hosts: all
      roles:
        - { role: webtier, tomcat_port: 8080, nginx_ssl_port: 443 }
      vars:
        - httpd_port: 80
    """

    variable_manager = VariableManager()
    loader = AnsibleLoader(data, variable_manager=variable_manager)
    playbooks = loader.get_single_data()

    # generate all the objects
    inventory = InventoryManager(loader=loader, sources=None, variable_manager=variable_manager)
    variable_manager.set_inventory(inventory)
    play = None

# Generated at 2022-06-13 08:42:56.159053
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    r = RoleDefinition()

    # TEST CASE: role names that are simply numbers can be parsed by PyYAML as integers even when quoted
    # as e.g. '{{ 42 }}' in the play
    data = dict(role = '{{ 42 }}')
    ds1 = r.preprocess_data(data)
    assert ds1['role'] == '42'

    # TEST CASE: role names that are simply numbers can be parsed by PyYAML as integers even when quoted
    data = dict(role = '42')
    ds2 = r.preprocess_data(data)
    assert ds2['role'] == '42'

    # TEST CASE: role names that are simply numbers can be parsed by PyYAML as integers even when quoted
    # in some forms of quotes
    data = dict(role = "{{ 42 }}")


# Generated at 2022-06-13 08:43:07.940998
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    # Case 1: include_role_fqcn=True
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars

    loader = DataLoader()
    variable_manager = VariableManager(loader=loader, host_vars=combine_vars())

    role = RoleDefinition(play=None, role_basedir='/path/to/role/', variable_manager=variable_manager, loader=loader, collection_list=[])
    role._role_collection="collection_name"

    assert role.get_name() == "collection_name.role_name"

    # Case 2: include_role_fqcn=False

# Generated at 2022-06-13 08:43:11.209151
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    fqcn = 'namespace.collection_name.role_name'
    rd = RoleDefinition()
    rd._role_collection = fqcn
    rd.role = 'role_name'
    assert rd.get_name() == fqcn

# Generated at 2022-06-13 08:43:22.337144
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.module_utils._text import to_bytes
    from ansible.errors import AnsibleError

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager.set_inventory(inventory)
    play_source =  dict(
            name = "Ansible Play",
            hosts = 'localhost',
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module='setup')),
            ]
        )

# Generated at 2022-06-13 08:43:36.940716
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Load data structure with a string
    ds = "myrole"
    role_def = RoleDefinition()
    assert isinstance(role_def.preprocess_data(ds), AnsibleMapping)
    assert role_def._role_path is None

    # Load data structure with role: name
    ds = {"role": "myrole"}
    role_def = RoleDefinition()
    assert isinstance(role_def.preprocess_data(ds), AnsibleMapping)
    assert role_def._role_path is None

    # Load data structure with name: name
    ds = {"name": "myrole"}
    role_def = RoleDefinition()
    assert isinstance(role_def.preprocess_data(ds), AnsibleMapping)
    assert role_def._role_path is None

    # Load data structure with role:

# Generated at 2022-06-13 08:43:52.109360
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from six import b
    from ansible.module_utils.six.moves.StringIO import StringIO
    from ansible.module_utils.six import PY3

    if PY3:
        unicode = str

    # Testing role name in role definition as string
    role_definition = b('localhost')
    role_definition = StringIO(role_definition)
    role_definition.name = 'role_definition'
    role_definition.mode = 'r'
    rd = RoleDefinition()
    assert rd.preprocess_data(role_definition) == 'localhost'

    # Testing role name in role definition as dict
    role_definition = b('{"role": "localhost"}')
    role_definition = StringIO(role_definition)
    role_definition.name = 'role_definition'

# Generated at 2022-06-13 08:44:00.690492
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    '''
    Provide a known-structured yaml and then compare the returned
    data structure
    '''

    # (1) Test a bare string with no other fields
    test_string = 'test-role'
    rd = RoleDefinition()
    result = rd.preprocess_data(test_string)
    assert isinstance(result, AnsibleMapping)
    assert 'role' in result
    assert result['role'] == test_string

    # (2) Test a dict with a field for role
    test_dict = dict(role='test-role-again')
    rd = RoleDefinition()
    result = rd.preprocess_data(test_dict)
    assert isinstance(result, AnsibleMapping)
    assert 'role' in result
    assert result['role'] == test_dict['role']

    #

# Generated at 2022-06-13 08:44:08.943606
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook

    # Create blocks
    play_book_data = {
        'hosts': 'localhost',
        'roles': [
            {
                'name': 'common',
                'role': {
                    'role1': {
                        'role': 'no_name_role1',
                        'role_var': 'role_var_value'
                    },
                    'name': 'no_name_role2'
                }
            }
        ]
    }

    # Create instances
    loader = DataLoader()
    inventory = InventoryManager(loader=loader)

# Generated at 2022-06-13 08:44:18.582637
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play import Play

    fake_loader = FakeLoader()
    fake_play = Play().load({}, loader=fake_loader)

    # test that empty dict fails
    try:
        RoleDefinition.load(dict(), play=fake_play)
        assert False, "Should always fail"
    except AnsibleError:
        pass

    # test that no 'role' or 'name' field fails
    try:
        RoleDefinition.load({'foo': 'bar'}, play=fake_play)
        assert False, "Should always fail"
    except AnsibleError:
        pass

    # test that a role without a role path fails
    try:
        RoleDefinition.load({'role': 'foo'}, play=fake_play)
        assert False, "Should always fail"
    except AnsibleError:
        pass

# Generated at 2022-06-13 08:44:24.493462
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.vault import VaultLib

    vault_secret = VaultLib()
    vault_secret.load_secret(os.path.expanduser('~/.ansible/vaultpass'))

    role_name = 'role_name'
    role_path = '/path/to/role'
    role_def = {
        'role' : role_name,
        'param1' : 'value1',
        'param2' : 'value2',
        }
    variable_manager_mock = Mock(name='variable_manager')
    loader_mock = Mock(name='loader')

    role_definition = RoleDefinition(variable_manager=variable_manager_mock, loader=loader_mock)
    role_definition_preprocessed = role_definition.preprocess_data(role_def)

   

# Generated at 2022-06-13 08:44:36.856657
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role_basedir = 'roles'
    loader_mock = Mock()
    loader_mock.path_exists = lambda x: True
    loader_mock.get_basedir = lambda: '.'
    variable_manager_mock = Mock()
    variable_manager_mock.get_vars.return_value = {}

    # test with simple string (i.e. role name, without any parameters)
    rd = RoleDefinition(role_basedir=role_basedir,
                        variable_manager=variable_manager_mock,
                        loader=loader_mock)
    ds = 'role_name'
    result = rd.preprocess_data(ds)
    assert result == {'role': 'role_name'}

    # test with a dict containing the role name and a single parameter

# Generated at 2022-06-13 08:44:48.737404
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    vars_manager = mock.Mock()
    loader = mock.Mock()
    play = mock.Mock()
    collection_list = []

    # simple case
    ds = dict(role='foo')
    role_def = RoleDefinition(play=play, variable_manager=vars_manager, loader=loader, collection_list=collection_list)
    result = role_def.preprocess_data(ds)
    assert result == dict(role='foo')

    # complicated case
    role_def = RoleDefinition(play=play, variable_manager=vars_manager, loader=loader, collection_list=collection_list)

    role_name = 'foo'
    ds = dict(role=role_name, become='yes', become_user='root', become_method='sudo')

    vars_manager.get_v

# Generated at 2022-06-13 08:44:53.933162
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    assert RoleDefinition.load({'role': 'somesee.somerole'}).get_name() == 'somesee.somerole'
    assert RoleDefinition.load({'role': 'somesee.somerole-1.0'}).get_name() == 'somesee.somerole-1.0'

# Generated at 2022-06-13 08:45:01.457466
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    inputs = [
        'role_name',
        {'role': 'role_name'},
        {'role': 'role_name', 'attribute': 'value'},
    ]
    expected_outputs = [
        'role_name',
        {'role': 'role_name'},
        {'role': 'role_name', 'attribute': 'value'},
    ]

    for input, expected_output in zip(inputs, expected_outputs):
        role_definition = RoleDefinition.load(data=input)
        output = role_definition.preprocess_data(ds=input)
        assert output == expected_output

# Generated at 2022-06-13 08:45:20.651340
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    test_cases = [
        ({'role': 'test-role'}, {'role': 'test-role'}, None),
        ({'role': 'test-role', 'with_items': []}, {'role': 'test-role'}, None,),
        ({'name': 'test-role'}, {'role': 'test-role'}, None),
        ({'name': 'test-role', 'with_items': []}, {'role': 'test-role'}, None),
        ('test-role', {'role': 'test-role'}, None),
        ('test-role', {'role': 'test-role'}, None)
    ]

# Generated at 2022-06-13 08:45:33.845554
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from collections import namedtuple
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play


    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    host = Host(name='127.0.0.1')
    inventory.add_host(host)
    # host.set_variable('ansible_ssh_pass', 'asdf')
    # host.set_variable('ansible_ssh_user', 'someuser')
    # host.set_variable('ansible_ssh_host', 'somehost')
    print(host.get_vars())

# Generated at 2022-06-13 08:45:40.917271
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # pylint: disable=protected-access
    # setup
    class TestDS(AnsibleBaseYAMLObject):
        """ This class is needed because test_preprocess_data is
            supposed to accept an object of AnsibleBaseYAMLObject
            type.
        """
        def __init__(self):
            super(TestDS, self).__init__()

    current_wd = os.path.dirname(os.path.abspath(__file__))
    test_role_data = {'role': 'test_role_name', 'test_data': True}
    test_ds = TestDS()
    test_ds.update(test_role_data)

    # test preprocess_data with role path
    role = RoleDefinition()

# Generated at 2022-06-13 08:45:52.907131
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    from ansible_collections.sensu.sensu_go.plugins.module_utils.sensu_go.sensu_go_client import SensuGoClient
    from ansible_collections.sensu.sensu_go.plugins.module_utils.sensu_go.helper import SensuGoHelper
    sensu_go_helper = Sens

# Generated at 2022-06-13 08:46:07.607379
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    # import module locally to avoid polluting namespace
    from ansible.playbook.role.definition import RoleDefinition

    # test case 1
    attr_name = {'role': 'apache'}
    role_name = 'apache'
    assert RoleDefinition(attr_name).get_name() == role_name

    # test case 2
    attr_name = {'role': 'apache', 'collections': ['geerlingguy.apache']}
    role_name = 'geerlingguy.apache'
    assert RoleDefinition(attr_name, collection_list=['geerlingguy.apache']).get_name() == role_name

    # test case 3
    attr_name = {'role': 'apache'}
    role_name = 'apache'

# Generated at 2022-06-13 08:46:16.230206
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    loader = AnsibleLoader(None, None)
    play_context = PlayContext()
    variable_manager = VariableManager()
    role_def = RoleDefinition(play=None, role_basedir='/some/basedir/roles', variable_manager=variable_manager, loader=loader)
    role_def.preprocess_data({'role': 'test_role', 'role_var': 'test_var'})
    assert role_def._role == 'test_role'
    assert role_def._role_path == '/some/basedir/roles/test_role'

# Generated at 2022-06-13 08:46:21.846678
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
      expected = '.'.join(x for x in ('aoc', 'apache') if x)
      rd = RoleDefinition()
      rd._role_collection = 'aoc'
      rd._attributes = dict(role='apache')
      actual = rd.get_name()
      assert actual == expected

# Generated at 2022-06-13 08:46:29.021091
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    '''
    test preprocess_data role definition
    '''
    loader = DictDataLoader({})
    variable_manager = VariableManager()
    pd = RoleDefinition(loader=loader, variable_manager=variable_manager)
    ds = {'name': 'foo'}
    new_ds = pd.preprocess_data(ds)
    assert type(new_ds) == dict
    assert new_ds == {'role': 'foo'}

# Generated at 2022-06-13 08:46:36.789459
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext

    display.verbosity = 3
    play = Play().load({
        'name': 'test play',
        'hosts': 'host0,host1',
        'gather_facts': False,
        'tasks': [
            { 'name': 'test task', 'debug': { 'msg': '{{ "role_name" | quote }}' } }
        ]
    }, variable_manager=PlayContext().variables, loader=None)

    play._tasks[0]._role = RoleDefinition(play, 'roles', variable_manager=None, loader=None)

    play._tasks[0]._role.preprocess_data('./roles/role_name')
    assert play._tasks[0]._role._

# Generated at 2022-06-13 08:46:43.602293
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Create the role definition
    role_definition = RoleDefinition()
    role_definition.role = "name"
    role_definition.role_name = "name"
    role_definition.role_path = "./lib/ansible/playbook/role/test_role_definition"
    role_definition.role_params = {}

    new_ds = role_definition.preprocess_data("test_role_definition")

    assert(new_ds['role'] == 'test_role_definition')

# Generated at 2022-06-13 08:47:01.457344
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    play_context = PlayContext()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    templar = Templar(loader=loader, variables=variable_manager.get_vars())

    # Case: normal usage
    role1 = RoleDefinition(play=None, role_basedir='/path/to/role/base/dir', variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 08:47:13.186214
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import os
    import sys
    import yaml
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.plugins.loader import role_loader
    from ansible.utils.collection_loader import AnsibleCollectionRef

    # dict for the test
    test_data = dict()

    # role test 1
    print('\nrole test 1'.center(80, '='))
    test_data['role1'] = {'role': 'test_role_1'}
    test_data['role2'] = {'role': 'test_role_2'}

# Generated at 2022-06-13 08:47:24.809119
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Function gets list of dictionaries, iterates through and
    # verifies that there is role name in role definition and
    # if this is not the case throws an AnsibleError

    # Set up
    play = {}
    variable_manager = {}
    loader = {}
    collection_list = []

    role_paths = (os.path.join(os.path.dirname(__file__), '../../../../'),'')
    for role_path in role_paths:

        # Test data
        # Bad test data
        # Data that does not contain role or name
        ds = {}
        definition = RoleDefinition(play, role_path, variable_manager, loader, collection_list)
        try:
            definition.preprocess_data(ds)
            assert False
        except AnsibleError:
            pass

        # Data

# Generated at 2022-06-13 08:47:38.144644
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    class FakePlay:
        basedir = '/home/test/test/test'
    class FakeVars:
        def __init__(self, variables):
            self.vars = variables
        def get_vars(self, play=None):
            return self.vars
    t = Attribute()
    t.attr_name = 'role_param'
    t.attr_type = 'string'
    t.attr_value = 'role_param_val'
    RoleDefinition._valid_attrs = {'role': t}
    f = FakePlay()
    rd = RoleDefinition(play=f, role_basedir='/home/test/')
    rd.variable_manager = FakeVars({'role_name': 'role_name_val'})

# Generated at 2022-06-13 08:47:49.402195
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from units.mock.loader import DictDataLoader

    res = dict()
    res[0] = dict()
    res[0]['name'] = 'foo'
    res[0]['role'] = 'role_1'
    res[0]['extra_arg'] = 'bla'

    res[1] = dict()
    res[1]['name'] = 'bar'
    res[1]['role'] = 'role_2'
    res[1]['role_var'] = 'value of role_var'

    ds = dict()
    ds['name'] = 'testing_role_def'
    ds['roles'] = res

    loader = DictDataLoader({None: ds})
    role_definition = RoleDefinition.load(ds, loader=loader)
    role_definitions = role

# Generated at 2022-06-13 08:48:02.581070
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    # test when ds is a simple string
    rd = RoleDefinition()
    ds = rd.preprocess_data('test_role')
    assert ds.get('role') == 'test_role'
    assert not ds.get('name')

    # test when ds is a dictionary
    rd = RoleDefinition()
    ds = rd.preprocess_data({'role': 'test_role'})
    assert ds.get('role') == 'test_role'
    assert not ds.get('name')

    # test when ds is a dictionary with an non-default field
    rd = RoleDefinition()
    ds = rd.preprocess_data({'name': 'test_role'})
    assert ds.get('role') == 'test_role'
    assert not ds.get

# Generated at 2022-06-13 08:48:07.239986
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    rd = RoleDefinition()

    #valid case
    ds = dict(
        role="abc.def",
        src="xyz",
        version="latest"
    )
    assert rd.preprocess_data(ds) == ds

    #valid case
    ds = 'abc.def'
    assert rd.preprocess_data(ds) == ds

    #valid case
    ds = dict(
        role="abc.def",
        src="xyz",
        version="latest"
    )
    ds = AnsibleMapping(ds)
    ds.ansible_pos = "file.yml:1:5"
    assert rd.preprocess_data(ds)

    #existing role params

# Generated at 2022-06-13 08:48:20.030529
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.data import AnsibleData
    rdef = RoleDefinition(role_basedir=None, variable_manager=None)
    # Test case 1: role definition with a filepath
    role_name = 'ansible/ansible-modules-core'
    role_path = None
    role_collection = None
    role_params = {}
    ds = AnsibleData('role: test_role')
    processed_data = rdef.preprocess_data(ds)
    assert(processed_data['role'] == 'test_role')


if __name__ == "__main__":
    import sys
    import pytest
    pytest.main(sys.argv)

# Generated at 2022-06-13 08:48:31.932893
# Unit test for method get_name of class RoleDefinition

# Generated at 2022-06-13 08:48:38.957743
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play import Play
    from ansible.template import Templar

    data = {
        'role': 'foo',
        'become': True,
        'bar': 'baz',
    }

    play = Play()
    templar = Templar(loader=None, variables={}, shared_loader_obj=None, fail_on_undefined=False)
    role_def = RoleDefinition(play=play, role_basedir='/path/to/playbook/roles', 
        variable_manager=MockVariableManager(templar), loader=None, collection_list=None)
    new_ds = role_def.preprocess_data(data)

    assert sorted(new_ds.keys()) == ['become', 'role']
    assert new_ds['role'] == 'foo'
    assert new

# Generated at 2022-06-13 08:48:59.299454
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Test   #1: test normal case
    # Input  : role: test_role
    # Output : {'role': 'test_role'}
    print("Test #1: test normal case: role: test_role")
    test_dict1 = {'role': 'test_role'}
    role_def_obj1 = RoleDefinition()
    result1 = role_def_obj1.preprocess_data(test_dict1)
    if result1 == {'role': 'test_role'}:
        print("PASSED")
    else:
        print("FAILED")

    # Test   #2: test normal case
    # Input  : name: test_role
    # Output : {'role': 'test_role'}
    print("Test #2: test normal case: name: test_role")
    test_

# Generated at 2022-06-13 08:49:13.316944
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role_def = RoleDefinition()
    role_name = "role_name"
    role_param_key = "role_param"
    role_param_value = "role_param_value"
    role_attrib_key = "role_attrib"
    role_attrib_value = "role_attrib_value"
    ds = dict()
    ds["role"] = role_name
    ds[role_param_key] = role_param_value
    ds[role_attrib_key] = role_attrib_value
    new_ds = role_def.preprocess_data(ds)
    assert new_ds["role"] == role_name
    assert role_param_key not in new_ds
    assert role_attrib_key in new_ds


# Generated at 2022-06-13 08:49:25.712329
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    '''
    Tests preprocess_data() function of class RoleDefinition.
    '''

    # Creation of a simple AnsibleMapping object
    ds = AnsibleMapping()
    ds['role'] = 'example_role1'

    # Creation of a fake role base directory
    role_basedir = '/example/path'

    # Creation of a RoleDefinition instance
    rd = RoleDefinition(role_basedir=role_basedir)

    # Testing the preprocess_data() function
    new_ds = rd.preprocess_data(ds)

    # Test the result
    assert(new_ds['role'] == 'example_role1')

# Generated at 2022-06-13 08:49:35.924319
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    from ansible.playbook.play import Play
    from ansible.utils.collection_loader import AnsibleCollectionRef
    from ansible.utils.collection_loader._collection_finder import _get_collection_role_path
    from ansible.utils.path import unfrackpath

    display = Display()
    tmp = unfrackpath('~/.ansible/collections')

    base_path = '/Users/dpetzel/ansible/ansible-base/test/utils/collection_loader/test_collections/collections_test'
    collection_name = 'ansible_collections.test.collection1'
    os.environ['ANSIBLE_COLLECTIONS_PATH'] = tmp

# Generated at 2022-06-13 08:49:48.529692
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    p = dict(
        name='test_play',
        hosts='all',
        roles=[
            dict(
                role='test_role',
                loop_control=dict(loop_var='item'),
                ignore_errors=False,
                hosts='all',
                when='{{ not item }}'
            )
        ],
    )
    play_context = PlayContext(p)
    variable_manager = VariableManager()
    variable_manager._fact_cache = dict(item='item')
    rd = RoleDefinition(play=play_context, variable_manager=variable_manager)

# Generated at 2022-06-13 08:49:59.626155
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role_definition_object = RoleDefinition()

    # set up a simple role definition with a parameter 'foo'
    ds = dict(role='test', foo='bar')
    ds_obj = AnsibleBaseYAMLObject(ds)

    # make sure the internal _split_role_params method works
    (new_role_def, role_params) = role_definition_object._split_role_params(ds)
    assert 'role' in new_role_def
    assert 'role' not in role_params
    assert 'foo' in role_params
    assert len(new_role_def.keys()) == 1
    assert len(role_params.keys()) == 1

    # make sure the preprocess_data method works
    assert isinstance(ds, dict)
    new_ds = role_definition_object.preprocess_data

# Generated at 2022-06-13 08:50:03.785259
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_definition = RoleDefinition(collection_list=[])
    role_definition.role = 'role1'
    assert role_definition.get_name() == 'role1'
    role_definition._role_collection = 'namespace'
    assert role_definition.get_name() == 'namespace.role1'

# Generated at 2022-06-13 08:50:12.307299
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.loader import AnsibleLoader

    # Test case for loading string
    ds = AnsibleLoader(None, None, None).load('''
    common
    ''')
    role = RoleDefinition()
    role.preprocess_data(ds)

    # Test case for loading dictionary
    ds = AnsibleLoader(None, None, None).load('''
    name: common
    ''')
    role = RoleDefinition()
    role.preprocess_data(ds)



# Generated at 2022-06-13 08:50:23.383247
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    import unittest
    from ansible.playbook.test.test_role_definition import TestRoleDefinition
    from ansible.playbook.role.definition import RoleDefinition

    class TestRoleDefinition_get_name(unittest.TestCase):
        def test_get_name_without_role_fqcn(self):
            test_role_definition = TestRoleDefinition()
            test_role_definition.runTest_get_name_without_role_fqcn()
        def test_get_name_with_role_fqcn(self):
            test_role_definition = TestRoleDefinition()
            test_role_definition.runTest_get_name_with_role_fqcn()
        def test_get_name_with_role_fqcn_without_role(self):
            test_role_definition = TestRole

# Generated at 2022-06-13 08:50:28.794547
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.errors import AnsibleError
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleMapping
    import os

    loader = None  # FIXME
    variable_manager = VariableManager()
    variable_manager._extra_vars = dict(mytest='test')
    variable_manager._options_vars = dict(mytest='test')
    play_context = PlayContext()
    templar = Templar(loader, play_context, variable_manager)

    # Case 1
    role_def = dict(role='mytest.role', my_var='{{ mytest }}')

# Generated at 2022-06-13 08:50:50.916407
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    display.warning = Mock(return_value=None)
    role_basedir = 'roles_basedir_example'
    role_variable_manager = Mock(get_vars=Mock(return_value={
        'role_example': 'example_role'
    }))
    role_loader = Mock(get_basedir=Mock(return_value='base_directory_example'), path_exists=Mock(return_value=True))
    role_collection_list = [
        'collection_example'
    ]

    role_object = RoleDefinition(role_basedir=role_basedir, variable_manager=role_variable_manager, loader=role_loader,
                                 collection_list=role_collection_list)

    # test string type

# Generated at 2022-06-13 08:51:04.154528
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role_name = 'test_role_name'
    working_directory = "/some/working/directory"
    role_def = {'role': role_name, 'param1': 'param1_value', 'param2': 'param2'}
    play = {'roles_path': ['/some/roles/path']}
    all_vars = {'inventory_dir': working_directory}
    variable_manager = {'get_vars': lambda play: all_vars}
    loader = {'get_basedir': lambda: working_directory}
    collection_list = ['/some/collection/path']
    role_definition = RoleDefinition(play, working_directory, variable_manager, loader, collection_list)

    result = role_definition.preprocess_data(role_def)

# Generated at 2022-06-13 08:51:16.866830
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    variable_manager = None
    loader = None
    collection_list = None
    ds_dict = {'role': 'test_role', 'a': 'b'}
    rd = RoleDefinition(variable_manager=variable_manager, loader=loader, collection_list=collection_list)
    ret_val = rd._split_role_params(ds_dict)
    assert ret_val[0] == {'role': 'test_role'}
    assert ret_val[1] == {'a': 'b'}
    ds_str = 'test_role'
    rd = RoleDefinition(variable_manager=variable_manager, loader=loader, collection_list=collection_list)

# Generated at 2022-06-13 08:51:24.674621
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    options = dict(
        connection='local',
        module_path=os.path.join(os.getcwd(), '../../lib/ansible/modules/'),
        forks=100,
        become=None,
        become_method=None,
        become_user=None,
        check=False,
        diff=False,
        remote_user='johndoe',
        private_key_file='/path/to/private/key',
    )

    loader = DataLoader()
    variable_manager = VariableManager()

    # Case 1: Role name is provided as a dict
    role_name = dict(name='role_name')

# Generated at 2022-06-13 08:51:39.281093
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    from ansible.module_utils.urls import open_url
    from ansible.module_utils._text import to_text

    from tempfile import NamedTemporaryFile as NTF
    from jinja2 import Template as j2template

    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.utils.vars import combine_vars

    def get_url(url):
        rsp = open_url(url)
        data = to_text(rsp.read(), errors='surrogate_or_strict')
        return data

    def get_template(url):
        return j2template(get_url(url))

    # TODO: convert to use the proper context manager when all supported
    #       Python versions are > 2.
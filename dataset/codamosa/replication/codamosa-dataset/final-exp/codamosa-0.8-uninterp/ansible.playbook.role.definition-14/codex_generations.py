

# Generated at 2022-06-13 08:41:55.159964
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    variable_manager = VariableManager()
    variable_manager.extra_vars = dict(foo='bar')

    loader = DictDataLoader({
        "test.yml" : """
            - include_role:
                role: role1
            - include_role:
                role: role2
                vars:
                    subrole_var: 'subrole_value'
        """
    })

    play_context = PlayContext()

    play = Play().load(
        ds=dict(
            hosts=['foo'],
            gather_facts=False,
            roles=[]
        ),
        variable_manager=variable_manager,
        loader=loader
    )

    roles_def = []
    role_

# Generated at 2022-06-13 08:42:08.090016
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    '''
    Test for method preprocess_data of class RoleDefinition
    '''

    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.yaml.loader import AnsibleLoader

    import sys
    sys.path.append('../lib')
    from collections import namedtuple

    # Create a Mock VariableManager
    all_vars = {}
    vars_manager = VariableManager()
    vars_manager._fact_cache = {}
    vars_manager._extra_vars = {}
    vars_manager._options_vars = {}
    vars_manager._variables = all_vars

    # Create a Mock PlayContext
    play_context = Play

# Generated at 2022-06-13 08:42:15.895404
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.role_include import RoleInclude
    from ansible.parsing.yaml.objects import AnsibleSequence
    import copy
    import textwrap

    # test data only
    test_playbook = AnsibleMapping()
    test_playbook.ansible_pos = (42, 42, 42)
    test_loader = None

    # test data only
    test_data = copy.deepcopy(RoleDefinition._valid_attrs)
    test_data.update({'name': 'ansible.unit.test'})

    # test data only
    test_data_1 = copy.deepcopy(RoleDefinition._valid_attrs)
    test_data_1.update({'role': 'ansible.unit.test'})

    # test data only
    test_data_2 = copy.deepcopy

# Generated at 2022-06-13 08:42:25.646083
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import sys
    import os

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role

    class MockOptions(object):
        def __init__(self, host_file, module_path, forks, become, become_method, become_user, check, diff, syntax, start_at_task, remote_user):
            self.host_file = host_file
            self.module_path = module_path
            self.forks = forks
            self.become = become
            self.become_method = become_method
            self.become_user = become_user
            self.check = check

# Generated at 2022-06-13 08:42:37.557395
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    loader = 'loader'
    play = 'play'
    role_basedir = 'tests/unit/fixtures/role_definition'
    role = 'test_role'
    name = 'name'
    role_params = {'one': 1, 'two': 2}
    role_path = 'tests/unit/fixtures/role_definition'
    collection = 'collection'

    fake_collection = object()
    class FakeCollectionsLoader():
        def load(self, collections):
            return {'collection': fake_collection}

    class FakeLoader():
        def path_exists(self, path):
            return True

        def get_basedir(self):
            return 'ansible'


# Generated at 2022-06-13 08:42:39.915660
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    '''
    Unit test for method RoleDefinition.preprocess_data
    '''
    pass

# Generated at 2022-06-13 08:42:53.603358
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Create a test environment
    class MockPlay(object):
        variable_manager = None
    play = MockPlay()

    class MockVariableManager(object):
        def get_vars(self, play=None):
            return dict()
    variable_manager = MockVariableManager()

    class MockAnsibleLoader(object):
        def get_basedir(self):
            return '/bar'

        def path_exists(self, path):
            if path == '/bar/roles/foo':
                return True
            else:
                return False
    loader = MockAnsibleLoader()

    # The constructor should work on these data
    role_definitions = [
        {'role': 'foo'},
        {'name': 'foo'},
        'foo'
    ]

# Generated at 2022-06-13 08:43:05.954277
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    # Case 1:
    # Set "include_role_fqcn" param to False and check if get_name
    # returns the value of "role" attribute
    s_role_cls = {'role': 'role_name'}
    role_def = RoleDefinition()
    role_def.__dict__.update(s_role_cls)
    assert role_def.get_name(include_role_fqcn=False) == s_role_cls['role']

    # Case 2:
    # Set "include_role_fqcn" param to True and check if get_name
    # returns FQCN of the role definition
    s_role_cls = {'role': 'role_name', '_role_collection': 'galaxy.lab.com'}
    role_def = RoleDefinition()
   

# Generated at 2022-06-13 08:43:10.675685
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    def run(data, expected):
        variable_manager = None
        loader = None
        rd = RoleDefinition()
        processed = rd.preprocess_data(data)
        assert processed == expected

    def run_fails(data):
        variable_manager = None
        loader = None
        rd = RoleDefinition()
        try:
            rd.preprocess_data(data)
            assert False, "'%s': expected an exception" % data
        except AnsibleError:
            pass

    run('foo', {'role': 'foo'})
    run('foo.bar', {'role': 'foo.bar'})
    run('foo.bar.baz', {'role': 'foo.bar.baz'})

# Generated at 2022-06-13 08:43:21.626615
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.vars import combine_vars

    loader = DataLoader()
    role_basedir = "roles"
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    tasks = [
        dict(meta=dict(role="foo")),
        dict(meta=dict(role="bar")),
        dict(role="baz", name="test_role", othername="ignore_othername"),
        dict(meta=dict(role="test")),
    ]


# Generated at 2022-06-13 08:43:36.970555
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Create object and set _ds
    role_def = RoleDefinition()
    role_def._ds = {
        'role': 'my_role',
        'my_param': {'my_sub_param': 'my_sub_param_value'}
    }

    # Test 1, call preprocess_data function
    result = role_def.preprocess_data(role_def._ds)

    # Assert results
    assert result['role'] == 'my_role'
    assert result['my_param']['my_sub_param'] == 'my_sub_param_value'

    # Test 2, create role_def object with string _ds
    role_def = RoleDefinition()
    role_def._ds = 'my_role'

    # Test 1, call preprocess_data function
    result = role_def.pre

# Generated at 2022-06-13 08:43:48.262688
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    class TestRoleDefinition(RoleDefinition):
        pass
    test_role_def = TestRoleDefinition()
    # neither role_collection nor role attributes are not set
    assert test_role_def.get_name() == ''
    test_role_def._role_collection = 'collection1'
    test_role_def.role = 'role1'
    assert test_role_def.get_name() == 'collection1.role1'
    test_role_def._role_collection = None
    assert test_role_def.get_name(include_role_fqcn=True) == 'role1'
    assert test_role_def.get_name(include_role_fqcn=False) == 'role1'

# Generated at 2022-06-13 08:43:57.708556
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Method: role: <role>,<params>
    # Test the role definitions with role name and parameters
    # Test case: The Data structure is not dict or string
    try:
        display.debug("Test the data structure is not dict or string")
        role = RoleDefinition()
        role.preprocess_data(int(123))
        print('Failed')
        exit(1)
    except AnsibleAssertionError:
        display.debug("The test for role definition with role name and parameters is successful")

    # Test case: The Data structure is dict

# Generated at 2022-06-13 08:44:13.161425
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    from ansible.module_utils.six import PY3
    from ansible.parsing.dataloader import DataLoader
    import yaml

    def _load_role_name(data):
        rd = RoleDefinition()
        return rd._load_role_name(data)

    def _load_role_path(data):
        rd = RoleDefinition()
        return rd._load_role_path(data)

    def _split_role_params(data):
        rd = RoleDefinition()
        return rd._split_role_params(data)


# Generated at 2022-06-13 08:44:24.218188
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    # Base case
    ds_dict_1 = dict(role='test')
    role_def_1 = RoleDefinition()
    role_def_1.preprocess_data(ds_dict_1)
    assert(role_def_1.role == 'test')

    # Include numbers in role name to avoid integer parsing
    ds_dict_2 = dict(role='test2')
    role_def_2 = RoleDefinition()
    role_def_2.preprocess_data(ds_dict_2)
    assert(role_def_2.role == 'test2')

    # Include a variable in the role name that should be templated
    variable_manager = VariableManager()
    ds_dict_3 = dict(role='{{test}}')
    role_def_3 = RoleDefinition()

# Generated at 2022-06-13 08:44:36.766696
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    def get_name(role_definition, fqcn, include_role_fqcn=True):
        role_definition.get_name.__dict__['_role_collection'] = fqcn
        assert role_definition.get_name(include_role_fqcn) == (
            fqcn + '.' + role_definition.get_name.__dict__['role'] if fqcn else role_definition.get_name.__dict__['role']
        )

# Generated at 2022-06-13 08:44:48.656621
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import imp
    from ansible.module_utils._text import to_text
    from ansible.parsing.yaml import objects
    import ansible.parsing.yaml.loader

    role_name = "sample_role"

    # RoleDefinition.preprocess_data does not require a Play object
    # but requires a VariableManager object that requires
    # a loader and a Play object
    play = imp.new_module('play')
    play.ROLE_PATH = ["./test/units/playbooks/",
                      "./test/units/playbooks/extra_role_path/"]
    role_basedir = None
    play.loader = ansible.parsing.yaml.loader.AnsibleLoader(None)
    # check with valid role name
    data = {"role": role_name}

# Generated at 2022-06-13 08:44:59.330821
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Test data
    data = {
        'role': 'testrole',
        'force': False,
        'param1': 'val1',
        'param2': 'val2'
    }

    # Create RoleDefinition object from data
    role_defn = RoleDefinition()
    role_defn.preprocess_data(data)

    # Verify returned role params
    role_params = role_defn.get_role_params()
    assert 'param1' in role_params
    assert role_params['param1'] == 'val1'
    assert 'param2' in role_params
    assert role_params['param2'] == 'val2'

    # Verify base class attributes
    assert role_defn._attributes['force'] is False
    assert role_defn._attributes['role'] == 'testrole'

   

# Generated at 2022-06-13 08:45:07.421745
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.utils.path import makedirs_safe

    from ansible.parsing import load_yaml_guess_encoding
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    def _get_play_context(loader):
        variable_manager = VariableManager()
        variable_manager.set_inventory(Inventory(loader=loader))
        play_context = PlayContext()
        # set play_context to have the loader so we can make sure the right
        # paths are created for included files
        # play_context._loader = loader
        return play_context


# Generated at 2022-06-13 08:45:17.689550
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role_definition = RoleDefinition()
    role_definition.preprocess_data([
        {
            'role': 'APACHE',
            'foo': 6,
        },
    ])
    assert role_definition._role_params == {'foo': 6}
    assert role_definition._role_path == 'APACHE'

    role_definition = RoleDefinition()
    role_definition.preprocess_data([
        '',
    ])
    assert role_definition._role_params == {}
    assert role_definition._role_path == ''

    role_definition = RoleDefinition()
    try:
        role_definition.preprocess_data([
            {},
        ])
    except AnsibleError:
        pass


# Generated at 2022-06-13 08:45:35.858520
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible import context
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext

    context._init_global_context(PlaybookCLI(args=['ansible-playbook']))

    play_context = PlayContext()
    play_context._set_task_and_variable_override(play_context.CLIARGS, variables=dict())

    play = Play.load(dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        roles = [
            {
                'role': 'test_role_1',
                'name': 'test_role_2',
                'foo': 'bar',
            }
        ],
    ), variable_manager=play_context.variable_manager, loader=None)



# Generated at 2022-06-13 08:45:47.927830
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_definition = RoleDefinition()
    role_definition.role = 'test_role'
    assert role_definition.get_name() == 'test_role'
    assert role_definition.get_name(include_role_fqcn=False) == 'test_role'
    role_definition._role_collection = 'test_collection'
    assert role_definition.get_name() == 'test_collection.test_role'
    assert role_definition.get_name(include_role_fqcn=False) == 'test_role'
    role_definition.role = ''
    assert role_definition.get_name() == 'test_collection.'
    assert role_definition.get_name(include_role_fqcn=False) == ''
    role_definition._role_collection = ''
    assert role_definition.get_name()

# Generated at 2022-06-13 08:46:00.562573
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    current_dir = os.path.dirname(__file__)
    test_dir = os.path.join(current_dir, '../unit_tests/playbook/')
    loader = DataLoader()
    test_inventory = InventoryManager(loader=loader, sources=[test_dir + 'test_inventory.yml'])
    test_variable_manager = VariableManager(loader=loader, inventory=test_inventory)
    test_variable = {'var_host': 'host', 'var_port': 22, 'var_user': 'root', 'var_password': '1234'}
    test_variable_manager

# Generated at 2022-06-13 08:46:12.977916
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # create the ds
    ds = AnsibleMapping(key1="{{ foo }}", key2=[1, 2, 3], key3={'a': 'b', 'c': 'd'}, key4=True)
    ds.ansible_pos = (1, 2, 3)

    # create the role definition and call the preprocess_data method
    role_definition = RoleDefinition()
    result = role_definition.preprocess_data(ds)

    # verify the result
    assert isinstance(result, AnsibleMapping)
    # assert that the new object has the same position info as the original
    assert result.ansible_pos == (1, 2, 3)
    # and that the resulting data structure is correct
    assert result.key1 == "{{ foo }}"

# Generated at 2022-06-13 08:46:21.630778
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    def run(ds=None, role_basedir=None, **kwargs):
        rd = RoleDefinition(role_basedir=role_basedir, **kwargs)
        return rd.preprocess_data(ds)
    assert run(role_basedir=C.DEFAULT_ROLES_PATH[0],
               variable_manager=lambda: {},
               loader=lambda: {},
               ds='foo') == {'role': 'foo'}
    # This won't always pass, but will sometimes fail and that shouldn't
    # cause any errors.

# Generated at 2022-06-13 08:46:33.128152
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    import unittest

    class TestRoleDefinition(unittest.TestCase):

        def test_preprocess_data(self):
            result_mapping = dict(name=u'role-name', role=u'role-name')

            role_definition = RoleDefinition()
            result = role_definition.preprocess_data(result_mapping)

            self.assertEqual(result['role'], u'role-name')

        def test_preprocess_data_exception(self):
            role_definition = RoleDefinition()

            with self.assertRaises(AnsibleError):
                role_definition.preprocess_data(None)

            with self.assertRaises(AnsibleAssertionError):
                role_definition

# Generated at 2022-06-13 08:46:44.766999
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role = RoleDefinition()

    # Test case 1: role is a dict, with name: test
    ds = dict(role='test')
    role.preprocess_data(ds)
    assert role._role == 'test', 'role name is not test'

    # Test case 2, 3: role is a dict, with name: text and {role, name}.
    ds = dict(name='test')
    role.preprocess_data(ds)
    assert role._role == 'test', 'role name is not test'

    # Test case 4: role is a dict, with name: text and {role, name}.
    ds = dict(name=dict(role='test'))
    role.preprocess_data(ds)
    assert role._role == 'test', 'role name is not test'

    # Test case 5: role is

# Generated at 2022-06-13 08:46:58.699895
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role_definition = RoleDefinition()
    role_definition._role_basedir = '/home'

    role = 'foo'
    definition = role
    role_definition._role_path = None
    role_definition._loader = None
    role_definition._role_params = dict()
    result = role_definition.preprocess_data(definition)
    assert result['role'] == role
    assert role_definition._role == role
    assert role_definition._role_params == {}

    role = 'bar'
    definition = 'name: ' + role
    role_definition._role_path = None
    role_definition._loader = None
    role_definition._role_params = dict()
    result = role_definition.preprocess_data(definition)
    assert result['role'] == role
    assert role_definition._role == role
    assert role

# Generated at 2022-06-13 08:47:10.052295
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role_init = RoleDefinition(role_basedir='foo')
    assert str(type(role_init.preprocess_data('role1'))) == "<class 'ansible.parsing.yaml.objects.AnsibleMapping'>"
    assert str(type(role_init.preprocess_data(7))) == "<class 'ansible.parsing.yaml.objects.AnsibleMapping'>"
    assert str(type(role_init.preprocess_data(dict(role='role2')))) == "<class 'ansible.parsing.yaml.objects.AnsibleMapping'>"
    assert str(type(role_init.preprocess_data(dict(role=8)))) == "<class 'ansible.parsing.yaml.objects.AnsibleMapping'>"

# Generated at 2022-06-13 08:47:21.696490
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.template import Templar

    from units.mock.loader import DictDataLoader

    mock_ds = dict(
        name='some_role_name',
        when='some_role_condition',
        tags='some_role_tag',
        become='some_role_become'
    )

    mock_loader = DictDataLoader({})
    mock_variable_manager = dict()
    mock_collection_list = list()

    role_def = RoleDefinition(loader=mock_loader, variable_manager=mock_variable_manager, collection_list=mock_collection_list)

    ds = AnsibleLoader(mock_ds, mock_loader).get_single_data()

    rds = role_def.preprocess_data

# Generated at 2022-06-13 08:47:39.346275
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import ansible.plugins.module_utils.network.f5.common.util as f5_common_util
    import os
    import sys
    import unittest
    import textwrap

    data_dir = os.path.join(os.path.dirname(sys.argv[0]), 'unit_tests/data')
    sys.path.append(data_dir)
    import playbook_fixture
    import playbook_run_tests_fixture

    class TestPlaybookRun(playbook_run_tests_fixture.TestPlaybookRun):

        def setUp(self):
            self._ds_role = None
            self._ds_role_basedir = None
            self._ds_variable_manager = None
            self._ds_loader = None
            self._ds_collection_list = None


# Generated at 2022-06-13 08:47:50.104863
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    class NoopVars(object):
        def __init__(self):
            self.vars = {}

        def get_vars(self, play=None):
            return self.vars

    class NoopLoader(object):
        def get_basedir(self):
            return os.path.join(os.path.dirname(__file__), '..')

        def path_exists(self, path):
            return True

    class NoopPlay(object):
        pass

    display_mock = Display()
    display_mock.info = lambda *args, **kwargs: None

    noop_vars = NoopVars()
    noop_loader = NoopLoader()
    noop_play = NoopPlay()
    noop_play._loader = noop_loader

    # Test with simple string

# Generated at 2022-06-13 08:48:00.820788
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader

    ds = """
    - name: unit test for RoleDefinition.get_name()
      hosts: localhost
      connection: local
      roles:
        - { role: galaxy.namespace.role }
    """

    role_block = AnsibleLoader(ds, DataLoader()).get_single_data()['roles'][-1]
    rd = RoleDefinition.load(role_block, None, None)
    assert(rd.get_name() == 'galaxy.namespace.role')

# Generated at 2022-06-13 08:48:06.690651
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    from ansible.parsing.utils.addresses import parse_address

    host = parse_address('localhost')
    task = dict(action=dict(module='ping', args={}))
    role = RoleDefinition()
    role.role = 'test'
    role._role_collection = 'mycolection'

    assert (role.get_name(False) == 'test'), "the get_name method return the wrong value"
    assert (role.get_name(True) == 'mycolection.test'), "the get_name method return the wrong value"



# Generated at 2022-06-13 08:48:21.388453
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    
    variable_manager = VariableManager()
    loader = DataLoader()
    role_object = RoleDefinition.load(
        'role: name', 
        variable_manager=variable_manager, 
        loader=loader,
        collection_list=None
    )
    assert role_object.get_role_params()['name'] == 'name'
    assert role_object.role == 'role'

    role_object = RoleDefinition.load(
        {'role': 'name', 'user': 'localuser'}, 
        variable_manager=variable_manager, 
        loader=loader,
        collection_list=None
    )
    assert role_object.get_role_params()['user'] == 'localuser'
    assert role_object.role == 'name'


# Generated at 2022-06-13 08:48:32.839061
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from collections import namedtuple
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role

    Host = namedtuple('Host', ['name', 'port'])
    host = Host(name='localhost', port=22)

    _loader = DictDataLoader({
        '/roles/myrole/tasks/main.yml': """
            - name: task
              action: ping
              register: result
        """,
    })

    play_ds = dict(
        name='foobar play',
        hosts='all',
        gather_facts='no',
        roles=[dict(role='myrole', task='task')],
    )

    play = Play.load(play_ds, variable_manager=None, loader=_loader)

# Generated at 2022-06-13 08:48:45.855682
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    loader = None
    variable_manager = None
    collection_list = None
    play = None
    role_basedir = None

    loader = FakeLoader()
    variable_manager = FakeVariableManager()
    PlaybookInclude = namedtuple('PlaybookInclude', ['name'])
    play = PlaybookInclude(name="play")
    role_basedir = "./test/test_data/test_role_definition/test1"
    roles_path = os.path.join(role_basedir, 'roles')
    loader.paths.append(os.path.join(roles_path, 'role2'))
    loader.paths.append(os.path.join(roles_path, 'role1'))


# Generated at 2022-06-13 08:48:52.199229
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    yaml_data = """
    - hosts: localhost
      roles:
        - role: setup
    """
    loader = DictDataLoader({None: yaml_data})
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play = Play().load(yaml_data, variable_manager=variable_manager, loader=loader)
    role_defs = play.get_roles()
    assert len(role_defs[0]._role_params) == 0
    assert role_defs[0]._ds['role'] == 'setup'

# Generated at 2022-06-13 08:48:59.791465
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    role_def = RoleDefinition("test_playbook", None, variable_manager, loader)

    # 'role' has a special meaning and raises an error, if it is used as a key
    # in the role definition. This error is raised by the _split_role_params method.
    ds = {'role': 'some_role'}
    with pytest.raises(AnsibleError) as err_wrapper:
        role_def.preprocess_data(ds)
    assert "role definitions must contain a role name" in err_wrapper.value.message

    # Special meaning: 'role' and 'name' are synonyms.

# Generated at 2022-06-13 08:49:13.253489
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    '''
    Test case for the method preprocess_data of the class RoleDefinition
    '''
    display.verbosity = 3
    import json
    import sys

    from collections import namedtuple
    from ansible.module_utils._text import to_text
    from ansible.parsing.dataloader import DataLoader

    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.plugins.callback import CallbackBase
    from ansible.inventory.host import Host

# Generated at 2022-06-13 08:49:23.483385
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play

    # Init patch
    loader = (
        "ansible.playbook.role_include.RoleDefinition._load_role_name = lambda self, ds: ds\n"
        "ansible.playbook.role_include.RoleDefinition._load_role_path = lambda self, role_name: (role_name, role_name)\n"
        "ansible.playbook.role_include.RoleDefinition._split_role_params = lambda self, ds: (ds, ds)\n"
    )
    loader += "import ansible.constants as C; C.DEFAULT_ROLES_PATH=['/etc/ansible/roles']"

   

# Generated at 2022-06-13 08:49:28.913984
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import os
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    file_loader = DataLoader()
    display = Display()
    templar = Templar(loader=file_loader, variables={})
    role = RoleDefinition(loader=file_loader,
                          variable_manager=VariableManager(loader=file_loader, variables={}))
    role_name1 = "test_role"
    role_name2 = "role_name"
    role_name3 = {"role_name": "test_role"}
    role_name4 = {"role": "test_role"}
    role_name5 = {"name": "test_role"}

# Generated at 2022-06-13 08:49:37.019058
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    variable_manager = None
    loader = None
    collection_list = None
    play = None
    role_basedir = None

    role_def = RoleDefinition(play=play, role_basedir=role_basedir, variable_manager=variable_manager, loader=loader,
                              collection_list=collection_list)

    # valid role definition
    ds = {'role': 'test'}
    processed_ds = role_def.preprocess_data(ds)
    assert processed_ds.__class__ == AnsibleMapping
    assert processed_ds['role'] == 'test'

    # role name is of valid type, but none of file, path or name
    ds = {'some_key': 'test'}

# Generated at 2022-06-13 08:49:49.449645
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    role_params = dict(b=2, c=3)
    role_def = dict(role='test', a=1)
    role_def.update(role_params)

    all_vars = dict(stub_ds=role_def)

    play_context = PlayContext()
    templar = Templar(loader=None, variables=all_vars)
    role_def = RoleDefinition(variable_manager=VariableManager(loader=None, play_context=play_context), loader=None)
    ds = role_def.preprocess_data(role_def._ds)
    assert ds['role'] == 'test'
    assert ds['a'] == 1

    role_params = role_

# Generated at 2022-06-13 08:49:54.794443
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    ''' test preprocess_data method of RoleDefinition class '''

    def _test(*args, **kwargs):
        ''' Test class '''
        return RoleDefinition._load_role_name(*args, **kwargs)

    roles_path = [
        "/tmp/bar:/tmp/foo",
        "/tmp/foo",
        "/tmp/bar"
    ]
    name = _test({'name': 'test'}, roles_path)
    fqname = '.'.join([os.path.basename(roles_path[0]), name])
    assert name == 'test'
    assert fqname == _test({'name': 'test'}, roles_path, include_role_fqcn=True)

    name = _test({}, roles_path)

# Generated at 2022-06-13 08:49:59.152500
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # FIXME: these tests need to be re-enabled when we have a better simulation of loading
    # FIXME: and validating data structures. For now, these tests generate a number of
    # FIXME: warnings about trying to load roles via the deprecated 'roles' keyword in
    # FIXME: the playbook, and a bunch of other irrelevant error messages from yaml/jinja
    # FIXME: so disabling until they are more relevant.
    return
    r = RoleDefinition()
    # following should all result in a parsed role name of 'test'

# Generated at 2022-06-13 08:50:10.966079
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    assert RoleDefinition({'role': 'myrole'})._pre_validate_data() == {'role': 'myrole'}

    # role names that are simply numbers can be parsed by PyYAML
    # as integers even when quoted, so turn it into a string type
    assert RoleDefinition('1')._pre_validate_data() == '1'
    assert RoleDefinition('1').get_role_params() == {}
    assert RoleDefinition(1)._pre_validate_data() == '1'
    assert RoleDefinition(1).get_role_params() == {}


# Generated at 2022-06-13 08:50:14.616641
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    # test a role name
    assert RoleDefinition().get_name() == 'RoleDefinition'
    # test a role FQCN
    assert RoleDefinition().get_name(include_role_fqcn=True) == 'ansible.builtin.RoleDefinition'

# Generated at 2022-06-13 08:50:21.051781
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # pylint: disable=unused-argument
    def mocked_Templar_template(self, args):
        return args

    def mocked_path_exists(self, value):
        return True

    def mocked_get_basedir(self):
        return "/playbook/dir"

    import sys
    if sys.version_info[0] == 2:
        old_class = "__builtin__.classobj"
    else:
        old_class = "builtins.type"

    mocked_variables = {
        "loader": {
            "path_exists": mocked_path_exists,
            "get_basedir": mocked_get_basedir,
        }
    }


# Generated at 2022-06-13 08:50:31.589391
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    """Unit test for method RoleDefinition.get_name"""
    display.verbosity = 2
    display.debug("Unit test for method RoleDefinition.get_name")
    role_def = RoleDefinition()
    role_def._role_collection = "my_collection"
    role_def._attributes["role"] = "my_role"
    expected = "my_collection.my_role"
    returned = role_def.get_name(True)
    assert returned == expected
    expected = "my_role"
    returned = role_def.get_name(False)
    assert returned == expected
    role_def._role_collection = None
    expected = "my_role"
    returned = role_def.get_name(True)
    assert returned == expected
    expected = "my_role"
    returned = role_def.get

# Generated at 2022-06-13 08:50:50.488807
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    def run_get_name_test(collection, expected):
        returncode = 0
        try:
            testrole = RoleDefinition()
            testrole._role_collection = collection
            testrole.role = "name"
            result = testrole.get_name()
            assert result == expected
        except AssertionError as e:
            returncode = 1
            print("Assertion error: %s" % e)
        except Exception as e:
            print("Unexpected exception: %s" % e)
        finally:
            return returncode

    run_get_name_test("collection", "collection.name")
    run_get_name_test("", "name")
    run_get_name_test("collection.subcollection", "collection.subcollection.name")

# Generated at 2022-06-13 08:51:03.729880
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    b = RoleDefinition()
    assert b.get_role_params() == dict()
    assert b._role_path is None
    assert b.get_name() is None

    # A simple definition
    a = RoleDefinition.load('xyz', None, None)
    assert a.get_name() == 'xyz'

    # role_path is None for an external role
    assert a._role_path is None
    assert a.get_role_params() == dict()
    data = dict(role='xyz', tags=['foo', 'bar'], become=True)
    #import pdb; pdb.set_trace()
    a = RoleDefinition.load(data, None, None)
    assert a._role_path is None
    assert a.get_name() == 'xyz'
    assert a.get_role_

# Generated at 2022-06-13 08:51:10.449655
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    assert RoleDefinition({'role': 'myrolename'}).get_name() == 'myrolename'
    assert RoleDefinition({'role': 'my.rolename'}).get_name() == 'my.rolename'
    assert RoleDefinition({'role': 'my.rolename'}).get_name(include_role_fqcn=False) == 'rolename'

# Generated at 2022-06-13 08:51:17.223792
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_definition = RoleDefinition()
    role_definition._role_collection = 'collection'
    role_definition.role = 'role'
    assert role_definition.get_name() == 'collection.role'
    assert role_definition.get_name(False) == 'role'
    role_definition._role_collection = None
    assert role_definition.get_name() == 'role'
    assert role_definition.get_name(False) == 'role'

# Generated at 2022-06-13 08:51:28.616002
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    # Create test role definition
    role_def = RoleDefinition()

    # Create test role definition with parameters
    role_def_with_params = RoleDefinition()
    role_def_with_params._valid_attrs['first'] = Attribute(required=False)
    role_def_with_params._valid_attrs['second'] = Attribute(required=False)
    role_def_with_params._valid_attrs['third'] = Attribute(required=False)
    role_def_with_params._valid_attrs['fourth'] = Attribute(required=False)

    # Create test VariableManager
    variable_manager = VariableManager()

# Generated at 2022-06-13 08:51:40.113435
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    # case1: test simple role definition
    role_yaml = '''
    - role:
        name: myrole_1
        tasks:
          - debug: msg="hello world"
    '''

    data = yaml.safe_load(role_yaml)

    for play in data:
        for (k, v) in iteritems(play.items()):
            if k == 'role':
                role = RoleDefinition(role_basedir = '/home/vagrant/ansible_project')
                role.load_data(v)
                role_path = role.get_role_path()
                assert role_path == '/home/vagrant/ansible_project/roles/myrole_1'

    # case2: test role definition with a path
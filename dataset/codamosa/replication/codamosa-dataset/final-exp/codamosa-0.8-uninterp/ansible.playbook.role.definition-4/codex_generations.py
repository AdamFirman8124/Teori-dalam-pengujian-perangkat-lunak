

# Generated at 2022-06-13 08:41:46.968901
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    rd = RoleDefinition()
    '''
    rd.preprocess_data()
    '''
    return

# Generated at 2022-06-13 08:41:56.520334
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():

    import collections

    test_cases = collections.OrderedDict()
    test_cases['simple_role_name'] = dict(include_role_fqcn=False, role_name='dummy_role', expected_result='dummy_role')
    test_cases['role_name and collection_name'] = dict(include_role_fqcn=True, role_name='dummy_role', expected_result='dummy_collection.dummy_role')


    for test_case, test_data in test_cases.items():
        test_instance = RoleDefinition()
        test_instance._role = test_data['role_name']
        test_instance._role_collection = 'dummy_collection'

        result = test_instance.get_name(test_data['include_role_fqcn'])
        assert result == test

# Generated at 2022-06-13 08:42:09.491022
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    role_definition = RoleDefinition()
    role_definition.role = "test"

    # key 'role'
    ds = {
        'role': 'test',
        'unknown_key1': 'unknown',
        'unknown_key2': 'unknown',
        'tags': ['tag1', 'tag2'],
    }
    new_ds = role_definition.preprocess_data(ds)
    assert new_ds == {'role': 'test', 'tags': ['tag1', 'tag2']}
    assert role_definition.get_role_params() == {'unknown_key1': 'unknown', 'unknown_key2': 'unknown'}

    # key 'name'

# Generated at 2022-06-13 08:42:20.611131
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # dummy AnsiblePlaybook
    class AnsiblePlaybook():
        pass
    class AnsiblePlaybook_AnsiblePlaybook():
        pass
    AnsiblePlaybook.AnsiblePlaybook = AnsiblePlaybook_AnsiblePlaybook
    class AnsiblePlaybook_AnsiblePlaybook_set_loader():
        def __init__(self, root_loader):
            self._loader = '_loader_for_AnsiblePlaybook'
    AnsiblePlaybook.AnsiblePlaybook.set_loader = AnsiblePlaybook_AnsiblePlaybook_set_loader
    class AnsiblePlaybook_AnsiblePlaybook_get_loader():
        def __init__(self, root_loader):
            self._loader = '_loader_for_AnsiblePlaybook'
    AnsiblePlaybook.AnsiblePlaybook

# Generated at 2022-06-13 08:42:27.286558
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    class CustomRoleDefinition(RoleDefinition):
        _valid_attrs = frozenset(list(RoleDefinition._valid_attrs) + ['name'])

        def __init__(self, *args, **kwargs):
            super(CustomRoleDefinition, self).__init__(*args, **kwargs)
            self.name = None

    class CustomTestCollection:
        def __init__(self, namespace=None, name=None):
            self.namespace = namespace
            self.name = name

    assert (CustomRoleDefinition({'role': 'role_name'}).get_name() == 'role_name')
    assert (CustomRoleDefinition({'role': 'role_name'}, collection_list=[CustomTestCollection()]).get_name() == 'role_name')

# Generated at 2022-06-13 08:42:40.829208
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role_name = "test_role"
    # Prepare bare minimum objects required for testing
    play = object()
    role_basedir = "/roles_basedir"
    class VariableManager(object):
        def get_vars(self, *args, **kwargs):
            return { "var1": "value1", "var2": "value2" }
    variable_manager = VariableManager()
    class Loader(object):
        def get_basedir(self):
            return "/playbook_basedir"
        def path_exists(self, path):
            return True
    loader = Loader()
    collection_list = [ 'c1' ]

    # Test 1: Role defined with just name
    ds = role_name
    errors = []

# Generated at 2022-06-13 08:42:54.225604
# Unit test for method preprocess_data of class RoleDefinition

# Generated at 2022-06-13 08:43:00.097835
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role_def = RoleDefinition()
    assert role_def.role is None

    ds = dict(
        role="foobar"
    )

    ds = role_def.preprocess_data(ds)

    assert role_def.role == "foobar"
    assert role_def._ds == ds



# Generated at 2022-06-13 08:43:01.412522
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    raise AnsibleError("not implemented")

# Generated at 2022-06-13 08:43:11.171969
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    import os

    loader = DataLoader()
    inv = Inventory(loader=loader, variable_manager=VariableManager(), host_list=[])
    RoleDefinition._valid_attrs = None
    ds = {
        "role": "apache",
        "foo": "bar",
    }
    rd = RoleDefinition(loader=loader, variable_manager=VariableManager(), role_basedir=os.path.dirname(os.path.realpath(__file__)))
    assert rd.preprocess_data(ds) == {'role': 'apache', 'foo': 'bar'}, "RoleDefinition.preprocess_data should return input dictionary with 'foo' as key/value pair"

   

# Generated at 2022-06-13 08:43:28.204574
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.module_utils.six.moves import StringIO
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader

    yaml_loader = AnsibleLoader(None, vault_password_file=None)

    # Role name contains variables (vars = {"test": "test"})
    stream = StringIO(u"---\nrole: '{{ test }}'\n")
    ds = yaml_loader.get_single_data(stream)
    role_def = RoleDefinition.load(ds, variable_manager=None)
    role_def.preprocess_data(ds)
    assert role_def._role_path

# Generated at 2022-06-13 08:43:37.725502
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    data1 = {
        'role': 'common',
        'become': 'root'
    }

    data2 = {
        'role': 'mahesh',
        'x': '123'
    }

    data3 = {
        'role': 'hello',
        'x': '123',
        'vars': 'xyz'
    }

    data4 = {
        'role': 'ansible.builtin',
        'x': '123',
        'vars': 'xyz'
    }

    data5 = {
        'role': 'ansible.builtin',
        'x': '123',
        'vars': {
            'xyz': '123'
        }
    }


# Generated at 2022-06-13 08:43:52.662510
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    # Create objects to test
    play = {}
    role_basedir = None
    variable_manager = {}
    loader = {}
    collection_list = None
    role_definition = RoleDefinition(play, role_basedir, variable_manager, loader, collection_list)
    role_definition._attributes = {'role': None}
    role_definition._role_collection = None
    # Test that get_name returns the role's name,
    # if the role has no collection
    role_definition._attributes['role'] = 'testrole'
    assert role_definition.get_name() == 'testrole'
    # Test that get_name returns the role's name prefixed by the collection it is
    # part of, if the role has a collection
    role_definition._attributes['role'] = 'testrole'
    role_definition._

# Generated at 2022-06-13 08:44:00.806402
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    # mock role name
    role_name = 'role_name'

    # mock role path
    role_path = 'role_path'

    # mock list of collections
    collection_list = ['collection_list']

    # mock role params
    role_params = {
        'k1': 'v1',
        'k2': 'v2'
    }

    # mock a role definition object
    rd = RoleDefinition()

    # mock the method _load_role_name
    def _mock_lrn(ds):

        # mock being called by preprocess_data
        rd._load_role_name = _mock_lrn

        # check the ds passed to preprocess_data
        assert ds == role_name

        # return the role name
        return role_name

    # mock the method _load_

# Generated at 2022-06-13 08:44:10.600622
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    '''
    test RoleDefinition.preprocess_data(ds)
    '''

    # Fixture for the data structure
    _ds = {
        'role' : 'test_role'
    }
    _role_name = _ds['role']
    _role_path = unfrackpath(os.path.join(C.DEFAULT_ROLES_PATH[0], _role_name))

    # Create a role definition object
    _role_def = RoleDefinition()
    # run test
    _new_ds = _role_def.preprocess_data(_ds)
    # check result
    assert _new_ds.get('role') == _role_name
    assert _role_def._role_path == _role_path
    assert _role_def._role_params == dict()

# Generated at 2022-06-13 08:44:21.734754
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    # Create role definition
    role_definition = RoleDefinition(role_basedir=None)
    role_definition._role_collection = 'ansible.builtin'
    role_definition._attributes['role'] = 'debug'
    name = role_definition.get_name()
    assert name == 'ansible.builtin.debug'

    # Create role definition
    role_definition = RoleDefinition(role_basedir=None)
    role_definition._role_collection = 'ansible.builtin'
    role_definition._attributes['role'] = 'debug'
    name = role_definition.get_name(include_role_fqcn=False)
    assert name == 'debug'

if __name__ == '__main__':
    test_RoleDefinition_get_name()

# Generated at 2022-06-13 08:44:34.301491
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Create an empty Playbook
    play = Playbook()

    # Create a dict suitable as input to method preprocess_data
    data = dict(
        role='test',
        become='test',
        vars=dict(
            a=1,
            b=2,
            c=3
        ),
        foo='bar'
    )

    # Create a RoleDefinition object
    role_definition = RoleDefinition(play)

    # Preprocess the data
    role_definition.preprocess_data(data)

    # Check the result of preprocess_data
    assert role_definition._role_path == os.path.join(role_definition._loader.get_basedir(), 'roles', 'test')

    # Check the result of preprocess_data
    assert role_definition.role == 'test'
    assert role_definition.get

# Generated at 2022-06-13 08:44:46.482773
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():


    from ansible.playbook.play_context import PlayContext


# Generated at 2022-06-13 08:44:57.129555
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    # mocking
    class object:
        def preprocess_data(self, ds):
            return(ds)

    class object1:
        def template(self, ds):
            return(ds)

    class object2:
        def get_vars(self, play=None):
            return(dict())

    class object3:
        def get_basedir(self):
            return(dict())

    class object4:
        def path_exists(self, ds):
            return(True)

    # Passing dict
    role = RoleDefinition()
    assert role.preprocess_data({'role': ['role1', 'role2']}) == {'role': ['role1', 'role2']}

    # Passing string
    role = RoleDefinition()

# Generated at 2022-06-13 08:45:05.791993
# Unit test for method preprocess_data of class RoleDefinition

# Generated at 2022-06-13 08:45:17.032326
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # 1. Test without variable_manager
    rd = RoleDefinition()
    ds = {'role': 'role_1'}
    result = rd.preprocess_data(ds)
    expected = {'role': 'role_1'}
    assert result == expected, 'unexpected result %s' % str(result)

    # 2. Test with variable_manager
    rd = RoleDefinition()
    rd._variable_manager = {}
    ds = {'role': '{{role_1}}'}
    result = rd.preprocess_data(ds)
    expected = {'role': '{{role_1}}'}
    assert result == expected, 'unexpected result %s' % str(result)



# Generated at 2022-06-13 08:45:31.704636
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    loader.set_basedir(C.DEFAULT_MODULE_PATH)
    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
    )

    # RoleDefinition where role: is defined
    ds = {'role': 'test_role',
          'tags': ['all']}

# Generated at 2022-06-13 08:45:40.083233
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.playbook.role.definition import RoleDefinition

    rd = RoleDefinition(loader=None)

    # Test when params are present
    ds = AnsibleMapping()
    ds['role'] = 'test_role'
    ds['become'] = 'true'
    new_ds = rd.preprocess_data(ds)
    assert new_ds is ds
    assert new_ds['role'] == 'test_role'
    assert new_ds['become'] == 'true'
    assert len(rd._role_params) == 0

    # Test when params are not present
    ds = AnsibleMapping()
    ds['role'] = 'test_role'
    new_ds = rd.preprocess_

# Generated at 2022-06-13 08:45:52.408492
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    """ Unit test for preprocess_data method of class RoleDefinition"""

    import json
    import sys
    import unittest2 as unittest

    from ansible.inventory.host import Host
    from ansible.vars import VariableManager

    from units.mock.loader import DictDataLoader
    from units.mock.path import prepended_to_loadpath

    variable_manager = VariableManager()

    def get_host_with_vars(vars_dict):
        host = Host(name='some_host')
        variable_manager.set_host_variable(host, vars_dict)
        return host


# Generated at 2022-06-13 08:46:00.250669
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    # test getting the role name with FQCN
    rd = RoleDefinition()
    rd.role='test'
    assert rd.get_name() == 'test'

    # test getting the role name with FQCN disabled
    rd = RoleDefinition()
    rd.role='test'
    assert rd.get_name(include_role_fqcn=False) == 'test'

# Generated at 2022-06-13 08:46:12.813814
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    # Method RoleDefinition.get_name:
    # 1. For Role name is simple string, not include_role_fqcn, return a simple string
    assert RoleDefinition(role_basedir="/tmp")._get_role_name("foobar", include_role_fqcn=False) == "foobar"
    # 2. For Role name is simple string, include_role_fqcn,  return a simple string
    assert RoleDefinition(role_basedir="/tmp")._get_role_name("foobar", include_role_fqcn=True) == "foobar"
    # 3. For Role name is full_qualified_collection_name, not include_role_fqcn, return simple string

# Generated at 2022-06-13 08:46:21.508859
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    data = dict(
        role='test_role_name',
    )

    class MockLoader:
        def __init__(self, search_path=None, base_path=None):
            self.search_path = search_path
            self.base_path = base_path

    basedir = '/tmp/ansible_roles'
    loader = MockLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = dict(
        role_basedir=basedir,
        role_paths=['/tmp/ansible_roles'],
        roles_path=['/tmp/roles_path']
    )


# Generated at 2022-06-13 08:46:33.126419
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import ansible.playbook
    import ansible.constants
    import ansible.errors
    import ansible.utils.collection_loader
    import tempfile

    def setup_file_fixture(content):
        _, filepath = tempfile.mkstemp()
        with open(filepath, "w") as f:
            f.write(content)
        return filepath

    def test_build_role_definition(role_name, role_dir, role_basedir, role_path, loader, ds):
        """
        Builds a RoleDefinition from the given parameters
        """
        rb = RoleDefinition(variable_manager=ansible.playbook.VariableManager(),
                            loader=loader, role_basedir=role_basedir)
        rb._role = role_name
        loaded_ds = rb.pre

# Generated at 2022-06-13 08:46:44.766619
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    from ansible.playbook.role.definition import RoleDefinition
    from ansible.vars.manager import VariableManager

    variable_manager = VariableManager()
    variable_manager.set_nonpersistent_facts(dict(
        ansible_vault_password='xxx',
    ))

    role_name = RoleDefinition(play=None, role_basedir=None, variable_manager=variable_manager)

    # Test simple role name
    assert role_name.preprocess_data(u'common') == dict(role=u'common')

    # Test a dict data structure with the role definition
    validation_dict = dict(
        name=u'common',
        description=u'Provides common roles tasks.',
    )
    assert role

# Generated at 2022-06-13 08:46:58.699755
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    from ansible import constants as C
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    yaml_loader = AnsibleLoader(None, None)
    template_dirs = C.DEFAULT_TEMPLATE_PATH
    vault_secrets_filename = C.DEFAULT_VAULT_PASSWORD_FILE
    vault_secrets = []

    play_context = PlayContext()
    all_vars = dict(a='1', b='2', c='3', d='4')

# Generated at 2022-06-13 08:47:13.442418
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    loader = DataLoader()
    pb = Playbook()
    context = PlayContext()

    r = RoleDefinition(loader=loader, play=pb, role_basedir="roles")

    role_data = dict(name="test_role", role="test_role")
    new_role_data = r.preprocess_data(role_data)

    # print(new_role_data)

    # assert new_role_data['role'] == 'test_role'
    # assert r._role_path == 'roles'

# Generated at 2022-06-13 08:47:24.978705
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    variable_manager = None
    loader = None
    collection_list = None
    play = None
    role_basedir = None
    rd = RoleDefinition(play=play, role_basedir=role_basedir, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
    rd._role_collection = "test_role_collection"

    # Case #1: set role, include_role_fqcn=True
    rd.role = "test_role"

    assert rd.get_name(include_role_fqcn=True) == "test_role_collection.test_role", "get_name(..., True) failed"

    # Case #2: set role, include_role_fqcn=False

# Generated at 2022-06-13 08:47:27.926020
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    display.verbosity = 3
    obj = RoleDefinition()
    role_name = obj.preprocess_data({'role': 'a_role', 'dummy': 'var'})
    assert(role_name == {'role': 'a_role'}), "preprocess_data() failed"



# Generated at 2022-06-13 08:47:38.554825
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    i = InventoryManager(loader=DataLoader(), sources='')
    v = VariableManager(loader=DataLoader(), inventory=i)
    role = RoleDefinition(
        play=None,
        role_basedir=None,
        variable_manager=v,
        loader=DataLoader(),
        collection_list=None,
    )

    assert role.preprocess_data(42) == '42'
    assert role.preprocess_data('42') == '42'

# Generated at 2022-06-13 08:47:49.903437
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    import unittest
    import collections
    import ansible.playbook.role_definition

    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role_definition import RoleDefinition

    class TestRoleDefinitionCls(unittest.TestCase):
        def setUp(self):

            self.loader = DataLoader()

        def test_simple_name_role(self):

            # test role: test_role_name, with default params
            ds = dict(
                role='test_role_name',
            )

            test_role_def = RoleDefinition()
            test_role_def.preprocess_data(ds)


# Generated at 2022-06-13 08:47:56.590463
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role = RoleDefinition()
    role.role = 'test'
    assert role.get_name() == 'test'
    role.role = 'test'
    role._role_collection = 'collection'
    assert role.get_name() == 'collection.test'
    role.role = 'test'
    role._role_collection = None
    assert role.get_name() == 'test'

# Generated at 2022-06-13 08:48:03.612846
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    assert RoleDefinition().get_name() == ''
    assert RoleDefinition(role='a').get_name() == 'a'
    assert RoleDefinition(role='a', role_collection='b').get_name() == 'b.a'
    assert RoleDefinition(role='a', role_collection='b').get_name(include_role_fqcn=False) == 'a'


# Generated at 2022-06-13 08:48:15.187443
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager)
    pb = PlaybookExecutor(playbooks=C.DEFAULT_PLAYBOOK_PATH,
                          inventory=inventory,
                          variable_manager=variable_manager,
                          loader=loader)

# Generated at 2022-06-13 08:48:27.332186
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.utils.display import Display
    display = Display()

    role_name = 'myrole'
    role_path = '/path/to/myrole'

    role_ds = AnsibleMapping()
    role_ds.ansible_pos = (1, 1, 2)
    role_ds['role'] = AnsibleUnicode(role_name)
    role_ds['some_attr'] = 'some_value'
    role_ds['with_vars'] = '{{ my_var }}'
    role_ds['with_vars_list'] = ['{{ my_var1 }}', '{{ my_var2 }}']

# Generated at 2022-06-13 08:48:36.195118
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    from ansible.playbook.play_context import PlayContext

    play_context = PlayContext()
    loader = None
    variable_manager = None
    rd = RoleDefinition(play=play_context, role_basedir=None, variable_manager=variable_manager, loader=loader, collection_list=None)

    # test with collection_list
    collection_list = ['namespace.collection']
    collection_name = 'collection_name'
    role_name = 'role_name'
    test_role = '.'.join([collection_list[0], collection_name, role_name])
    rd._role_path = '%s/%s/roles/%s' % (play_context._basedir, collection_list[0], collection_name)
    rd._role_collection = collection_name
    rd._

# Generated at 2022-06-13 08:48:50.064400
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    import os

    variable_manager = VariableManager()
    loader = DataLoader()

    role_definition = RoleDefinition(variable_manager=variable_manager, loader=loader)
    role_definition._role_basedir = 'test/test_role_1'
    role_definition.preprocess_data('test_role_3')

    assert role_definition.role == 'test_role_3'
    assert role_definition._role_path == os.path.join('test/test_role_1/', 'test_role_3')
    assert role_definition._role_params == {}

# Generated at 2022-06-13 08:48:58.250922
# Unit test for method preprocess_data of class RoleDefinition

# Generated at 2022-06-13 08:49:12.468718
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    class TestVarsModule:
        def __init__(self):
            self.vars = dict()

        def get_vars(self):
            return self.vars

    # Test data structure
    ds = dict(
        role = dict(
            name = 'about_to_be_overridden',
            param1 = 1,
            param2 = 2,
        )
    )

    # Variable manager for templating
    vars_mgr = TestVarsModule()
    vars_mgr.vars = dict(
        test_role = 'test_role_name'
    )

    # Role search paths, in this case hidden by ROLE_NAME
    role_basedir = dict(
        roles = '/roles/directory'
    )

    # Create RoleDefinition instance

# Generated at 2022-06-13 08:49:24.136272
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    # Create a RoleDefinition object
    rd = RoleDefinition()

    # Given a dict containing role and role_params
    key = "customvalue"
    value = "value"
    ds = dict(role="test_role",
        role_params = {key: value})

    # When preprocess_data is called
    new_ds = rd.preprocess_data(ds)

    # Then a dict containing role and the new role_params is returned
    assert new_ds == dict(role="test_role", role_params = {})
    assert rd._role_params["customvalue"] == "value"

# Generated at 2022-06-13 08:49:27.380519
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    assert RoleDefinition().get_name() == '<no name set>'
    assert RoleDefinition(role='common').get_name() == 'common'

# Generated at 2022-06-13 08:49:36.521587
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    def test_cases():

        ### Case 1
        ### Simple invocation, role name is "testrole"
        ###
        yield(
            dict(
                datastructure = dict(role = "testrole"),
                expected = dict(role = "testrole")
            )
        )

        ### Case 2
        ### Simple invocation, role name is "testrole" and an empty dict
        ### for role_params
        ###
        yield(
            dict(
                datastructure = dict(role = "testrole"),
                expected = dict(role = "testrole")
            )
        )

        ### Case 3
        ### Invocation of a role called "testrole" with a dict of
        ### role_params
        ###

# Generated at 2022-06-13 08:49:49.041586
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    '''Unit test for preprocess_data method of class RoleDefinition'''
    # First try to test when the data structure is a string
    data_structure = "teststring"
    role_definition = RoleDefinition(role_basedir="test_basedir")
    role_definition.preprocess_data(data_structure)
    assert role_definition._role_params == {}

    # Now, try with a dictionary
    data_structure = {"role": "test_role", "role_parm1": "role_param1", "role_param2": "role_param2"}
    role_definition = RoleDefinition(role_basedir="test_basedir")
    role_definition.preprocess_data(data_structure)

# Generated at 2022-06-13 08:49:59.976193
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    rd = RoleDefinition()

    # case: role collection
    rd._role_collection = 'test.collection'
    rd._attributes['role'] = 'test_role'
    assert rd.get_name() == 'test.collection.test_role'

    # case: include_role_fqcn=False
    rd._role_collection = 'test.collection'
    rd._attributes['role'] = 'test_role'
    assert rd.get_name(include_role_fqcn=False) == 'test_role'

    # case: no role collection, no role
    rd._role_collection = None
    rd._attributes['role'] = None
    assert rd.get_name() == ''

    # case: no role collection, has role

# Generated at 2022-06-13 08:50:11.506376
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    
    # Create a mock class that can be used in place of Ansible.
    # In this case, all we're doing is checking if the functions
    # DEFAULT_ROLES_PATH and DEFAULT_ROLES_PATH are called
    # (although they return nothing).

    class AnsibleMock :
        def __init__(self) :
            self.DEFAULT_ROLES_PATH_called = False
            self.DEFAULT_ROLES_PATH_return = None
        def DEFAULT_ROLES_PATH():
            self.DEFAULT_ROLES_PATH_called = True
            return self.DEFAULT_ROLES_PATH_return

    # two simple tests with valid roles
    role1 = RoleDefinition()
    role1_data = {'role': 'foo'}
    result = role1.preprocess

# Generated at 2022-06-13 08:50:19.220016
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    class temp():
        pass
    loader = temp()
    loader.get_basedir = lambda : "/etc/ansible/playbooks"

    variable_manager = temp()
    variable_manager.get_vars = lambda : {}

    play = temp()
    collection_list = ['collection-test']


# Generated at 2022-06-13 08:50:33.313445
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    from ansible.module_utils.six.moves import StringIO
    from ansible.parsing.vault import VaultEditor


    # from ansible.parsing.vault import VaultEditor
    # from ansible.parsing.vault.util import load_vault_secrets
    # from ansible.playbook.play_context import PlayContext
    # from ansible.vars.clean import module_response_deepcopy
    # from ansible.vars.hostvars import HostVars
    # from ansible.vars.manager import VariableManager
    # from ansible.vars.reserved import Reserved

    
    # ==========================================================================
    # FUTURE TODO
    # ==========================================================================
    #
    # For future testing, we plan to use Ansible's test/lib/ansible_test/_internal

# Generated at 2022-06-13 08:50:40.324279
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleMapping

    ds = dict(role=dict(role_name=dict(name="foo")))

    rd = RoleDefinition()
    ds = rd.preprocess_data(ds)

    assert isinstance(ds, AnsibleMapping), ds



# Generated at 2022-06-13 08:50:50.097879
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext

    class Play:
        def __init__(self):
            self.connection = 'local'
            self.network_os= 'nxos'

    class PlayContext:
        def __init__(self):
            self.connection = 'local'
            self.network_os= 'nxos'

    def get_vars():
        return dict()

    def get_loader():
        return 'loader'

    def get_basedir():
        return 'basedir'

    class Blocks:
        def __init__(self):
            self.block = Block()

    ########################################################################
    # Test case1: normal condition
    ########################################################################
    # Define data structure
    ds = dict()

# Generated at 2022-06-13 08:51:03.353127
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    # Test with dict
    ds = dict(
        role='rolename'
    )

    VariableManager = None
    loader = DataLoader()
    rd = RoleDefinition(variable_manager=VariableManager, loader=loader, role_basedir='./test/roles')
    actual = rd.preprocess_data(ds)
    expected = dict(
        role='rolename'
    )

    assert actual == expected

    # Test with string
    ds = 'rolename'

    VariableManager = None
    loader = DataLoader()
    rd = RoleDefinition(variable_manager=VariableManager, loader=loader, role_basedir='./test/roles')
    actual = rd.preprocess_data(ds)

# Generated at 2022-06-13 08:51:16.079484
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block

    play_ds  =  {
        'name': "test_role_definition role_name",
        'hosts': "test_hosts",
        'roles': [
            {
                'role': "test_role"
                }
            ]
    }

    play = Play().load(play_ds, variable_manager=None, loader=None)
    play._included_file = dict(path='/tmp/test_playbook.yml', name='test_playbook')

    block_ds = [
        {
            "block": {
                'role': "test_role"
            }
        }
    ]

    block = Block()
    block._parent = play

# Generated at 2022-06-13 08:51:24.281733
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    import os

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost'], variable_manager=variable_manager)
    play_source =  dict(
            name = "Ansible Play",
            hosts = 'localhost',
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module='shell', args='ls'), register='shell_out'),
                dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
             ]
        )

    # Create play object,

# Generated at 2022-06-13 08:51:28.912027
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_name = "test_name"
    role_definition = RoleDefinition()
    role_definition.role = role_name

    assert role_definition.get_name() == role_name
    assert role_definition.get_name(False) == role_name

# Generated at 2022-06-13 08:51:30.497332
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    pass
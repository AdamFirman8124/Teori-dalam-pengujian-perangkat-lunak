

# Generated at 2022-06-13 08:41:55.507194
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Create a load object
    load = Base.load

    # Use the load object to load a dictionary that is meant to
    # represent the datastructure used to create a RoleDefinition object
    #
    # In this case the datastructure is a simple string.
    ds = "testrole"
    obj = load(ds)

    # Check the object created is of the correct type
    assert(isinstance(obj, RoleDefinition))

    # Check the role name contained in the dictionary has been saved in the
    # object.
    role_name = obj._attributes['role']
    assert(role_name == "testrole")

    # Use the load object to load a dictionary that is meant to
    # represent the datastructure used to create a RoleDefinition object
    #
    # In this case the datastructure contains a role name that is
   

# Generated at 2022-06-13 08:42:08.578128
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib

    role_def_dict = dict(role=b'role_name')
    role_def_dict_with_role_params = dict(role=b'role_name', role_param_1=b'role_param_1')
    role_def_str = b'role_name'

    #----
    # Test with a simple dictionary object
    #----
    # template a plain dictionary object

# Generated at 2022-06-13 08:42:15.047894
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    variable_manager = VariableManager()
    loader = DataLoader()
    mock_ds = AnsibleLoader(None, variable_manager).load(dict(
        role='foobar',
        loop_var=7,
    ))
    role_def = RoleDefinition.load(mock_ds, loader=loader, variable_manager=variable_manager)
    assert role_def.role == 'foobar'
    assert isinstance(role_def, RoleDefinition)

# Generated at 2022-06-13 08:42:24.972433
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    '''
    Validate proper return value of preprocess_data method.
    '''
    import warnings
    warnings.simplefilter('ignore', DeprecationWarning)

# Generated at 2022-06-13 08:42:36.343994
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext

    play_context = PlayContext()

    # * This tests normal case
    data = {'role': 'nginx', 'foo': 'bar'}
    role_def = RoleDefinition.load(data=data, variable_manager=None, loader=None)

    assert role_def.preprocess_data(ds=data) == {'role': 'nginx'}

    # * This tests case with role_name contains variable
    data = {'role': '{{ role_name }}', 'foo': 'bar'}
    role_def = RoleDefinition.load(data=data, variable_manager=None, loader=None)

    assert role_def.preprocess_data(ds=data) == {'role': '{{ role_name }}'}

    # * This tests case with role

# Generated at 2022-06-13 08:42:49.970598
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import unittest2 as unittest
    from ansible.parsing.dataloader import DataLoader

    # Create a RoleDefinition instance with a dict as init parameter
    # The dict is an example of a task definition which imports its
    # corresponding role
    class TestRoleDefinition(unittest.TestCase):

        def setUp(self):
            self.loader = DataLoader()
            self.variable_manager = None
            self.test_role_definition = RoleDefinition(variable_manager=self.variable_manager, loader=self.loader)
            self.test_dict = {'role': 'myrole'}

            # Expected dict as a result of method preprocess_data
            self.expected_dict = {
                'role': 'myrole'
            }

        def tearDown(self):
            pass


# Generated at 2022-06-13 08:43:03.957450
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role_basedir = u'/root/roles'
    variable_manager = MagicMock()
    loader = MagicMock()
    collection_loader = MagicMock()
    collection_loader.get_role_path = MagicMock(return_value=[u'/root/plugins/roles/abc', None])
    collection_loader.list_collections = MagicMock(return_value=[u'test.dummy'])
    collection_loader.path_exists = MagicMock(return_value=True)
    collection_list = [collection_loader]

    # Case 1: Test the data structure is empty.
    ds1 = {}
    role_definition1 = RoleDefinition(role_basedir=role_basedir, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
    role_definition1

# Generated at 2022-06-13 08:43:10.876340
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.dumper import AnsibleDumper
    import sys
    import os

    def print_obj(obj):
        if isinstance(obj, AnsibleBaseYAMLObject):
            obj = obj.copy()

        if isinstance(obj, AnsibleMapping):
            result = ""
            for (k,v) in obj.iteritems():
                if isinstance(v, string_types):
                    result += "   %s: %s" % (k, v)
                else:
                    result += "   %s: " % k
                    result += print_obj(v)
            return result

# Generated at 2022-06-13 08:43:18.268951
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    """
        Load a role definition and return a list of the result
    """
    loader = DictDataLoader(dict())
    variable_manager = VariableManager()

    result = None
    try:
        role_definition = RoleDefinition(variable_manager=variable_manager, loader=loader)
        data = dict(
            role = "test-role",
            extra_var = "extra"
        )
        result = role_definition.preprocess_data(data)
    except:
        raise

    assert result['role'] == 'test-role'
    assert 'extra_var' not in result

# Generated at 2022-06-13 08:43:30.638474
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.playbook.play_context import PlayContext
    import os

    def load_data(ds, variable_manager=None, loader=None):
        rd = RoleDefinition(play=None, role_basedir=None, variable_manager=variable_manager, loader=loader)
        return rd.preprocess_data(ds)

    def assert_result(ds, role_name, role_path):
        assert(isinstance(ds, AnsibleMapping))
        assert(ds.get('role') == role_name)
        rd = RoleDefinition(play=None, role_basedir=None, variable_manager=None, loader=None)
        rd._role_path = role_path

# Generated at 2022-06-13 08:43:51.490078
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Set required variables to run the test
    loader = None
    variable_manager = None

    # Test role as a dict
    role_def = RoleDefinition.load({'role': 'test-role'}, variable_manager=variable_manager, loader=loader)
    try:
        assert role_def._role == 'test-role'
        assert role_def._role_path.endswith('test-role')
    except:
        raise
    else:
        return True

    # Test role as an ansible base yaml object
    role_def = RoleDefinition.load(['test-role'], variable_manager=variable_manager, loader=loader)
    try:
        assert role_def._role == 'test-role'
        assert role_def._role_path.endswith('test-role')
    except:
        raise

# Generated at 2022-06-13 08:44:00.568526
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    fake_loader = DictDataLoader({
        "/etc/ansible/roles/test/tasks/main.yml": "/etc/ansible/roles/test/tasks/main.yml",
        "test/tasks/main.yml": "test/tasks/main.yml",
        "/etc/ansible/roles/test/meta/main.yml": "/etc/ansible/roles/test/meta/main.yml",
        "test/meta/main.yml": "test/meta/main.yml",
    })
    fake_play = Base()
    fake_play.roles_path = "/etc/ansible/roles"
    fake_variable_manager = VariableManager()
    fake_variable_manager.extra_vars = dict(a=1, b=2)

# Generated at 2022-06-13 08:44:08.689753
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play import Play

    class VarManager:
        def get_vars(self, play):
            return dict()

    class Loader:
        def path_exists(self, path):
            return path == '/home/username/ansible/ok.yml'

        def get_basedir(self):
            return '/home/username/ansible'

    ds = dict(role = 'ok.yml')
    variable_manager = VarManager()
    loader = Loader()
    play = Play()

    role_definition = RoleDefinition(play=play, variable_manager=variable_manager, loader=loader)
    role_definition.preprocess_data(ds)

    assert role_definition._role_path == '/home/username/ansible/ok.yml'

# Generated at 2022-06-13 08:44:10.165973
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    pass



# Generated at 2022-06-13 08:44:18.941322
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Role name with playbook path and role name
    rd = RoleDefinition()
    ds = dict(role=dict(name='test-role', path='/path/to/playbook'))
    rd.preprocess_data(ds)
    expected = dict(role='test-role', path='/path/to/playbook')
    assert rd._attributes == expected, 'RoleDefinition parse dict should have path and name keys'

    # Role name with playbook path and role name as a string
    ds = 'test-role'
    rd.preprocess_data(ds)
    expected = dict(role='test-role')
    assert rd._attributes == expected, 'RoleDefinition parse dict should have only a name key'

    # Role name with playbook path and role name as a string, with a role param
    ds = dict

# Generated at 2022-06-13 08:44:24.825144
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Test data
    data1 = {"role": None}
    data2 = {"role": None, "a": "b"}
    data3 = {"name": None, "a": "b"}
    data4 = {"role": "a", "a": "b"}
    data5 = {"role": ["a"], "a": "b"}
    data6 = {"name": ["a"], "a": "b"}
    data7 = {"role": "a"}
    data8 = {"name": "a"}
    data9 = "a"

    # Expected data
    expected1 = {"role": None}
    expected2 = {"role": None}
    expected3 = {"role": None}
    expected4 = {"role": "a"}
    expected5 = {"role": ["a"]}
    expected6 = {"role": ["a"]}


# Generated at 2022-06-13 08:44:36.959638
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()

    # role def with role name as a dict
    role_def = dict(role='foo')
    role_def = RoleDefinition(variable_manager=variable_manager, loader=loader).preprocess_data(role_def)
    assert role_def['role'] == 'foo'

    # role def with role name as a dict with params
    role_def = dict(role='foo', params={'x': 1, 'y': 2})
    role_def = RoleDefinition(variable_manager=variable_manager, loader=loader).preprocess_data(role_def)
    assert role_def['role'] == 'foo'

    # role def role name as

# Generated at 2022-06-13 08:44:48.774451
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    class TestScope:
        class TestPlay:
            class TestModuleManager:
                import re
                class TestLoader:
                    class TestPathFinder:
                        re = re
                    path_finder = TestPathFinder()
                loader = TestLoader()
            module_manager = TestModuleManager()
        play = TestPlay()

    def test(scope, role, include_role_fqcn, expected):
        role_definition = RoleDefinition(play=scope, variable_manager=None, loader=scope.play._variable_manager.loader)
        role_definition._attributes = {'role': role}
        actual = role_definition.get_name(include_role_fqcn)
        if actual != expected:
            print("actual:%s, expected:%s" % (actual, expected))
        assert actual == expected


# Generated at 2022-06-13 08:44:59.451793
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import tempfile
    import shutil
    import os
    import sys

    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.module_utils.facts import default_collectors


# Generated at 2022-06-13 08:45:07.541701
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.module_utils.six import PY3

    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.vars.manager import VariableManager
    from ansible.vars import HostVars

    # for testing, we don't actually need a playbook as the variable manager
    # does not need a play to function, but we still need to create one
    # to pass in as the argument and so that we can set the basedir
    class Play(object):
        pass
    play = Play()

    # create a variable manager which we need to provide to the RoleDefinition
    # class, which will be used to template any variables in the role name
    variable_manager = VariableManager()

# Generated at 2022-06-13 08:45:20.608289
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    loader = DictDataLoader({})
    variable_manager = VariableManager()
    play = Play().load({}, variable_manager=variable_manager, loader=loader)
    role = RoleDefinition(play, role_basedir="/tmp/test_role_basedir", variable_manager=variable_manager, loader=loader)
    role.preprocess_data({'role': 'foo'})
    assert role.role == 'foo'
    assert role._role_path == '/tmp/test_role_basedir/foo'
    assert role._role_collection is None

# Generated at 2022-06-13 08:45:33.791833
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role_mock = RoleDefinition()
    role_name = "roles/test"
    ds = dict(role="roles/test")
    new_ds = role_mock.preprocess_data(ds)
    assert 'role' in new_ds
    assert new_ds['role'] == role_name

    # Rolename with a variable
    role_name = "{{ test }}"
    ds = dict(role=role_name)
    new_ds = role_mock.preprocess_data(ds)
    assert 'role' in new_ds
    assert new_ds['role'] == role_name

    # Set a rolename with a variable and loader
    loader_mock = Mock()
    loader_mock.path_exists.return_value = True
    var_manager_mock = Mock

# Generated at 2022-06-13 08:45:40.904755
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    display.verbosity = 0
    role_name = 'myrole'
    role_path = 'myrole'
    role_params = dict(myparam1='myparam1value', myparam2='myparam2value')
    data = dict(role=role_name)
    data.update(role_params)
    inventory = InventoryManager(loader=None, sources=[])
    variable_manager = VariableManager(loader=None, inventory=inventory)
    play_context = PlayContext()
    role_definition = RoleDefinition(play_context, role_path, variable_manager)

    # add fake role path

# Generated at 2022-06-13 08:45:52.920735
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.role.definition import RoleDefinition
    import os

    this_directory = os.path.dirname(os.path.realpath(__file__))

    # 1 - Good case
    input_ds = {
        'name': 'good_name',
        'role': 'good_role_name',
        'bad_key': 'bad_value'
    }
    input_role_basedir = os.path.join(this_directory, "fixtures", "role_definition_tests")
    role_definition = RoleDefinition(role_basedir=input_role_basedir)

    expected_result = {
        'role': 'good_name',
    }
    result = role_definition.preprocess_data(input_ds)
    assert result == expected_result

    # 2 - Bad case: the value

# Generated at 2022-06-13 08:46:07.608535
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role_definition = RoleDefinition()
    role_definition.preprocess_data(dict())
    role_definition.preprocess_data('')
    role_definition.preprocess_data(1)
    try:
        role_definition.preprocess_data(list())
    except AssertionError:
        pass
    else:
        raise AssertionError('should have thrown AssertionError')
    try:
        role_definition.preprocess_data(set())
    except AssertionError:
        pass
    else:
        raise AssertionError('should have thrown AssertionError')
    try:
        role_definition.preprocess_data(object())
    except AssertionError:
        pass
    else:
        raise AssertionError('should have thrown AssertionError')


# Generated at 2022-06-13 08:46:16.229943
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    """
    Verify that preprocess_data of class RoleDefinition behaves as expected
    """
    # Simple string is passed
    data = "role_name"
    # Create an instance of the class
    role_def = RoleDefinition()
    # Call the method
    new_ds = role_def.preprocess_data(ds=data)
    # Check that the output is as expected
    assert isinstance(new_ds, AnsibleMapping)
    assert new_ds == {'role': 'role_name'}

    # Dictionary is passed
    data = dict(role='role_name')
    # Create an instance of the class
    role_def = RoleDefinition()
    # Call the method
    new_ds = role_def.preprocess_data(ds=data)
    # Check that the output is as expected

# Generated at 2022-06-13 08:46:29.230975
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper

    # data structure for testing code
    test_ds = AnsibleMapping()

    # a single bare string, indicating only a name/path to a role
    test_ds['simple_string'] = AnsibleMapping()
    test_ds['simple_string']['role'] = 'my_role'
    test_ds['simple_string']['expected_result'] = {'role': 'my_role'}

    # a dictionary with a name/path to a role
    test_ds['role_name'] = AnsibleMapping()

# Generated at 2022-06-13 08:46:36.893092
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from units.mock.loader import DictDataLoader
    from ansible.vars.manager import VariableManager

    # TODO: remove this once `test_get_name_from_role_definition` test case is implemented
    #       in `test_role_definition` unit test case of `test_role.py`
    def _get_role_collection(name, collection_list=None):
        return _get_collection_role_path(name, collection_list)


# Generated at 2022-06-13 08:46:46.443387
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    loader = None
    variable_manager = None

    data = {'role': 'myrole'}
    rd = RoleDefinition(variable_manager=variable_manager, loader=loader)
    rd.preprocess_data(data)
    assert rd._role_path == 'myrole'
    assert rd._ds == {'role': 'myrole'}

    data = {'role': 'myrole', 'when': 'true'}
    rd = RoleDefinition(variable_manager=variable_manager, loader=loader)
    rd.preprocess_data(data)
    assert rd._role_path == 'myrole'
    assert rd._ds == {'role': 'myrole', 'when': 'true'}

    data = {'role': 'myrole', 'myparam': 'myvalue'}
    r

# Generated at 2022-06-13 08:46:59.825916
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.module_utils.six import PY3
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.config.manager import ConfigManager
    from ansible.playbook.block import Block

    args = dict(
        name='test_preprocess_data',
        connection='local',
        become=False,
        become_method=None,
    )
    play_context = PlayContext(**args)
    variable_manager = VariableManager()
    loader = DataLoader()
    if PY3:
        config_data = dict()
    else:
        config_data = ConfigManager.instance()

# Generated at 2022-06-13 08:47:15.707242
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    # Case 1: Check that get_name returns the role name (and not the collection) when the method is called without any keyword argument
    role_definition = RoleDefinition(role_basedir='/path/to/roles/dir', collection_list=[os.path.join(os.path.dirname(__file__), '../fixtures/collections/ansible_collections/example_collection/')])
    role_definition.preprocess_data(ds='example_collection.webserver.example')
    assert role_definition.get_name() == 'example'

    # Case 2: Check that get_name returns the role name (and not the collection) when the method is called with the argument include_role_fqcn=False

# Generated at 2022-06-13 08:47:21.438050
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_definition = RoleDefinition()
    assert role_definition.get_name() == "undefined"

    # noinspection PyProtectedMember
    role_definition._role_collection = "namespace"
    role_definition.role = "role_name"
    assert role_definition.get_name() == "namespace.role_name"

# Generated at 2022-06-13 08:47:29.321102
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import pytest
    from ansible.module_utils.six import PY3
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.playbook.role.definition import RoleDefinition

    data = AnsibleMapping()

    # create fake object instances
    play = object()
    role_basedir = 'role_basedir'
    variable_manager = object()
    loader = object()
    collection_list = ['col1', 'col2']

    # create test object
    rd = RoleDefinition(
        play=play,
        role_basedir=role_basedir,
        variable_manager=variable_manager,
        loader=loader,
        collection_list=collection_list)

    # TEST: role name is instance of a string
    data['role'] = 'role_name'


# Generated at 2022-06-13 08:47:44.016232
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    # Test cases
    testCases = (
        # Test case 1.
        # Indices of test case 1
        # role_collection, role, expected_result
        # Index 0: test empty role_collection
        # Index 1: test empty role
        # Index 2: test expected result
        (None, None, None),
        (None, 'apache', 'apache'),
        ('geerlingguy.apache', 'apache', 'geerlingguy.apache.apache'),
        ('geerlingguy.apache', '', 'geerlingguy.apache'),
        ('geerlingguy', 'apache', 'geerlingguy.apache'),
        ('', 'apache', 'apache'),
    )

    # Test get_name
    for i in range(len(testCases)):
        role_def = RoleDefinition()
        role_def._

# Generated at 2022-06-13 08:47:52.854685
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader

    # create RoleDefinition object
    loader = AnsibleLoader(None, play_context=PlayContext())

# Generated at 2022-06-13 08:47:58.723466
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_definition = RoleDefinition(collection_list=['test.collection'])
    role_definition.role = 'test.collection.test_role'
    assert role_definition.get_name() == 'test.collection.test_role'
    assert role_definition.get_name(include_role_fqcn=False) == 'test_role'

# Generated at 2022-06-13 08:48:07.256180
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    # Note: This test does not follow the usual pattern of a separate test module
    #       for the class being tested. Instead, it uses the module for the class
    #       (module role_definition.py)
    from ansible.playbook.play_context import PlayContext

    # create a play_context for use by the RoleDefinition to be tested
    play_context = PlayContext()

    # create a variable_manager for use by the RoleDefinition to be tested
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    variable_manager = VariableManager(loader=None, inventory=InventoryManager())

    # create a role_definition object to test
    role_definition = RoleDefinition(play=None, role_basedir=None, variable_manager=variable_manager, loader=None, collection_list=None)

# Generated at 2022-06-13 08:48:21.680111
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.yaml.objects import AnsibleMapping

    # Fake a role definition as if it was parsed from a YAML text
    # faking the ansible_pos too
    role_definition = AnsibleMapping()
    role_definition.ansible_pos = "fake-ansible-pos"
    role_definition['name'] = dict(a=1)
    role_definition['role'] = "rolename"
    role_definition['foo'] = "bar"
    role_definition['tags'] = ['foo', 'bar']

    play_context = PlayContext()
    definition = RoleDefinition(play=None, role_basedir=None, variable_manager=None, loader=None)

# Generated at 2022-06-13 08:48:33.054254
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.plugins.loader import role_loader
    from ansible.parsing.yaml.objects import AnsibleUnicode

    rd = RoleDefinition()

    # Test dictionary syntax
    result = rd.preprocess_data({'role': 'geerlingguy.apache'})
    assert result == {'role': 'geerlingguy.apache'}

    # Test string syntax
    result = rd.preprocess_data('geerlingguy.apache')
    assert result == {'role': 'geerlingguy.apache'}

    # Test number syntax
    result = rd.preprocess_data(12345)
    assert result == {'role': '12345'}

    # Test parameter syntax

# Generated at 2022-06-13 08:48:46.170048
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    all_vars = dict(
        role_search_path = '/path/to/roles',
        role_basedir = '/path/to/roles2',
        working_directory = '.',
        roles_path = ['roles', '/roles2'],
        ansible_version = '1.3.3',
        ansible_system = 'getos',
        ansible_pkg_mgr = 'deb'
    )
    variable_manager = VariableManager(loader=loader, variables=all_vars)

    play = Play()
    role_basedir = None
    role_definition = RoleDefinition(play=play, role_basedir=role_basedir, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 08:49:11.505975
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    # With include_role_fqcn=True
    role_definition = RoleDefinition() #pylint: disable=no-member
    role_definition.role = 'role_foo' #pylint: disable=attribute-defined-outside-init
    assert role_definition.get_name() == 'role_foo'
    role_definition._role_collection = 'collection_bar' #pylint: disable=protected-access
    assert role_definition.get_name() == 'collection_bar.role_foo'
    role_definition.role = None #pylint: disable=attribute-defined-outside-init
    assert role_definition.get_name() == 'collection_bar'
    # With include_role_fqcn=False
    assert role_definition.get_name(include_role_fqcn=False) == None

# Generated at 2022-06-13 08:49:20.145477
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # Mocks
    class MockPlay:
        def __init__(self):
            self._variable_manager = None

    class MockTemplar:
        def __init__(self):
            self._loader = None
            self._variables = {}

        def template(self, name):
            if name == 'true':
                return True
            elif name == 'false':
                return False
            elif name == '1':
                return 1
            elif name == '"1"':
                return "1"
            elif name == '1.1':
                return 1.1
            elif name == '"1.1"':
                return "1.1"

# Generated at 2022-06-13 08:49:24.008895
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    rd = RoleDefinition()
    rd._role_collection = "foo.galaxy.ansible.com"
    rd._valid_attrs.role = Attribute(name='role', default=None)
    rd.role = "bar"
    assert(rd.get_name() == "foo.galaxy.ansible.com.bar")
    assert(rd.get_name(include_role_fqcn=False) == "bar")

# Generated at 2022-06-13 08:49:29.419663
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():

    class FakeLoader(object):
        def path_exists(self, path):
            return True

        def get_basedir(self):
            return '.'

    class FakeCollection(object):
        def __init__(self, collection_name):
            self.collection_name = collection_name

        @property
        def command_name(self):
            return self.collection_name

        @property
        def collections(self):
            return [self]

    def get_collection_role_path(role_name, collection_list):
        ns, name = role_name.split('.')
        return name, '.', FakeCollection(ns)

    rd = RoleDefinition(play=None, role_basedir=None, variable_manager=None,
                        loader=FakeLoader(), collection_list=[])
    rd._split_role

# Generated at 2022-06-13 08:49:37.187017
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    '''
    Test cases for method preprocess_data of class RoleDefinition in file
    ansible/playbook/role/definition.py
    '''

    import imp
    import unittest

    from ansible.errors import AnsibleError, AnsibleAssertionError
    from ansible.playbook.role.definition import RoleDefinition

    # Mock class to provide an object with the attributes required by the
    # method we want to test.
    class MockLoader():
        def get_basedir(self):
            return '/home/testuser/workspace'

        def path_exists(self, path):
            return True
    mockLoader = MockLoader()

    # Create a class to mock class Base.

# Generated at 2022-06-13 08:49:49.550987
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    myrole = dict(
        foo='bar',
        some_param1='baz',
        some_param2='bax',
    )

    def _get_loader(data):
        return DataLoader()

    def _get_variable_manager(data, loader):
        return VariableManager()

    play = Play().load(dict(
        name="foobar",
        hosts=['127.0.0.1'],
        roles=[myrole],
        gather_facts='no',
    ), _variable_manager=_get_variable_manager, _loader=_get_loader)

    # make sure that role_basedir is taken into account
    p

# Generated at 2022-06-13 08:49:54.889633
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    # Test 1: Create object and set fully-qualified collection (FQC) role name.
    #         Test that role name and role path are returned after calling
    #         method preprocess_data.

    def _create_role_path(role_namespace, role_name):
        return os.path.join('/path/to/collections', role_namespace, 'ansible_collections', role_namespace, 'roles', role_name)

    role_name = 'example.role1'
    role_namespace = 'example'
    role_path = _create_role_path(role_namespace, role_name)

    role_definition = RoleDefinition(collection_list=['/path/to/collections'])
    role_definition.role = role_name

# Generated at 2022-06-13 08:50:03.916077
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role = RoleDefinition()
    role._role_collection = 'collection_name'
    role._attributes['role'] = 'role_name'
    role_fqcn = 'collection_name.role_name'
    assert role.get_name() == role_fqcn
    assert role.get_name() == role_fqcn
    assert role.get_name(False) == 'role_name'
    assert role.get_name(include_role_fqcn=False) == 'role_name'

    role_name = 'role_name'
    role = RoleDefinition()
    role._attributes['role'] = role_name
    assert role.get_name() == role_name

    role_name = 'role_name'
    role = RoleDefinition()
    role._attributes['role'] = role_name


# Generated at 2022-06-13 08:50:15.124068
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence

    # test role str
    role = RoleDefinition()
    role_data = role.preprocess_data('role1')
    assert type(role_data) == AnsibleMapping
    assert role_data.get('role') == 'role1'

    # test role: role1 syntax
    role = RoleDefinition()
    role_data = role.preprocess_data({"role": "role1"})
    assert type(role_data) == AnsibleMapping
    assert role_data.get('role') == 'role1'

    # test name: role1 syntax
    role = RoleDefinition()
    role_data = role.preprocess_data({"name": "role1"})
    assert type(role_data) == AnsibleM

# Generated at 2022-06-13 08:50:27.438266
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.utils.display import Display
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.utils.path import unfrackpath

    display = Display()
    role_search_paths = [
        os.path.join(unfrackpath('roles/'), u'roles'),
    ]
    ds = { 'role': 'foobar' }
    role_name = 'foobar'
    role_root = unfrackpath('roles')
    role_path = os.path.join(role_root, 'roles', role_name)
    all_vars = { 'role_root': role_root }


# Generated at 2022-06-13 08:50:52.330474
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    # Test when `ds` is a string
    ds = "localhost"
    role_definition = RoleDefinition()
    result = role_definition.preprocess_data(ds)
    assert result.keys() == ['role']
    assert 'localhost' in result.values()

    # Test when `ds` is a dict
    ds = dict(name='localhost')
    role_definition = RoleDefinition()
    result = role_definition.preprocess_data(ds)
    assert result.keys() == ['role']
    assert 'localhost' in result.values()

    # Test when `ds` is an integer (should pass through)
    ds = 42
    role_definition = RoleDefinition()
    result = role_definition.preprocess_data(ds)
    assert result.keys() == ['role']
    assert 42 in result.values()

# Generated at 2022-06-13 08:51:02.345126
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    assert RoleDefinition().get_name() == "<no name set>"
    assert RoleDefinition(role='role_name').get_name() == "role_name"
    assert RoleDefinition(role='role_name').get_name(include_role_fqcn=False) == "role_name"
    assert RoleDefinition(role='namespace.role_name').get_name() == "namespace.role_name"
    assert RoleDefinition(role='namespace.role_name').get_name(include_role_fqcn=False) == "role_name"

# Generated at 2022-06-13 08:51:14.708735
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    class TestRoleDefinition(RoleDefinition):
        _role = 'testrole'

    # Test that it returns the name of the role when no collection is given
    role = TestRoleDefinition()
    assert role.get_name() == 'testrole'

    # Test that it returns the name of the role with the collection
    role = TestRoleDefinition()
    role._role_collection = 'testcol'
    assert role.get_name() == 'testcol.testrole'

    # Test that it returns the name of the role when no collection is given and
    # include_role_fqcn is False
    role = TestRoleDefinition()
    assert role.get_name(include_role_fqcn=False) == 'testrole'

    # Test that it returns the name of the role with the collection and
    # include_role_fqcn is False

# Generated at 2022-06-13 08:51:23.571342
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    # No ansible.cfg for a consistent testing environment
    os.environ['ANSIBLE_CONFIG'] = ''

    from ansible.playbook.play_context import PlayContext

    play_context = PlayContext()

    ########################################################################
    #### first test : role name as string
    ########################################################################
    rd = RoleDefinition()

    playbook = './test/ansible/playbooks/test_role_definition.yml'
    loader = DataLoader()
    play_ds = loader.load_from_file(playbook)

# Generated at 2022-06-13 08:51:27.324045
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    ds = dict(role='foo.bar')
    dsobj = RoleDefinition.load(ds)
    assert dsobj.get_name() == 'foo.bar'

# Generated at 2022-06-13 08:51:41.377109
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    loader = DataLoader()
    role_basedir = 'roles/'
    role_definition = RoleDefinition(role_basedir=role_basedir, loader=loader)
    role_definition.preprocess_data({'role': 'foo'})
    assert role_definition._role_path == 'roles/foo'
    assert role_definition.role == 'foo'
    assert role_definition._role_params == {}
    role_definition.preprocess_data({'role': 'foo', 'param': 'bar'})
    assert role_definition._role_path == 'roles/foo'
    assert role_definition.role == 'foo'
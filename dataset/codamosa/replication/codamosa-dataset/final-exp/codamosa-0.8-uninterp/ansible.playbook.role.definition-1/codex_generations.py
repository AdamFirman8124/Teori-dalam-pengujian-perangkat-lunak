

# Generated at 2022-06-13 08:41:43.546793
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    assert False, "Not yet implemented."

# Generated at 2022-06-13 08:41:54.731024
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    # Test an error, no role name
    data = dict(a='1', b='2')
    role_def = RoleDefinition(loader=loader)
    try:
        role_def.preprocess_data(data)
        assert False, 'Should have raised an AnsibleError'
    except AnsibleError:
        pass
    # Test with simple role name
    data = 'test'
    role_def = RoleDefinition(loader=loader)
    new_data = role_def.preprocess_data(data)
    assert new_data == {'role': 'test'}
    # Test with role name and role param
    data = dict(role='test', a='1')
    role_def = RoleDefinition(loader=loader)


# Generated at 2022-06-13 08:41:55.785813
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Not implemented
    pass

# Generated at 2022-06-13 08:42:08.860592
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from collections import namedtuple
    from ansible.parsing import vault

    # mock data (role_params not used)
    rp = dict()
    role_ds = dict()
    role_ds['role'] = 'test'
    role_ds['role_path'] = 'test_path'
    role_ds['role_params'] = rp
    role_ds['role_collection'] = None
    role_ds['role_name'] = 'test'

    # mock objects
    class TestType:
        def __init__(self, attr, value):
            self.value = value
            self.attr = attr

        def __call__(self, value):
            return self.value

    class MockVarManager:
        def __init__(self):
            self.data = dict()


# Generated at 2022-06-13 08:42:15.694348
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import yaml

    yamlStr = yaml.dump({'role': 'webservers', 'vars': {'var_a': 'var_a_val'}})
    role_def = RoleDefinition.load(yamlStr)
    role_def.preprocess_data(yamlStr)

    assert isinstance(role_def._ds, AnsibleMapping)
    assert isinstance(role_def.role, string_types)
    assert isinstance(role_def._role_params, dict)
    assert role_def.role == 'webservers'
    assert role_def._role_params.get('vars') == {'var_a': 'var_a_val'}

# Generated at 2022-06-13 08:42:25.489339
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    class FakeLoader:
        def get_basedir(self):
            return '/playbook_dir'
        def path_exists(self, path):
            return path in {'/playbook_dir/roles/my-role',
                            '/playbook_dir/roles/my-role/tasks/main.yml',
                            '/playbook_dir/my-role',
                            '/my-role'}

    class FakeVariableManager:
        def get_vars(self, play=None):
            return dict()

    loader = FakeLoader()
    variable_manager = FakeVariableManager()
    display.verbosity = 3

    # Test role definition with full path
    my_role_full_path = RoleDefinition(loader=loader,
                                       variable_manager=variable_manager,
                                       role_basedir=None)

# Generated at 2022-06-13 08:42:34.183558
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():

    # Arrange
    test_data = [
        # (expected_result, role_collection, role)
        ('foo', None, 'foo'),
        ('foo', 'bar', 'foo'),
        ('bar.foo', 'bar', 'foo'),
        ('foo', '', 'foo'),
        ('bar.foo', '', 'bar.foo'),
    ]

    for expected, role_collection, role in test_data:
        rd = RoleDefinition()
        rd._role_collection = role_collection
        rd.role = role

        # Act
        actual = rd.get_name()

        # Assert
        assert expected == actual

# Generated at 2022-06-13 08:42:44.839505
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # prepare for the test
    # an example of a role name that is a dictionary
    role_name_dict = {'role': 'test_role'}
    # an example of a role name that is a string
    role_name_string = 'test_role'
    # an example of a role name that includes a variable
    role_name_var = '{{ test }}'
    # create a temporary object of class RoleDefinition
    role_definition = RoleDefinition()
    # set the role path
    role_definition._role_path = '/path/to/role'

    # run the preprocess_data method twice
    # 1st, it receives a role name that is a dictionary
    # 2nd, it receives a role name that is a string
    for i in range(2):
        # run the method
        role_definition.preprocess_data

# Generated at 2022-06-13 08:42:53.205486
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    role_path = unfrackpath(unfrackpath(__file__) + "/../../test/roles/test_role")
    role_basedir = None

    role = RoleDefinition(play=Play().load({}, variable_manager=variable_manager, loader=loader),
                          role_basedir=role_basedir, variable_manager=variable_manager,
                          loader=loader)

# Generated at 2022-06-13 08:43:06.771474
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    class TestRoleDefinition(RoleDefinition):
        _valid_attrs = frozenset(['a', 'b', 'role'])
        _valid_assocs = frozenset([])

    ############################
    # Case 1: role is a simple string
    ############################

    role_data = 'a_role'
    role_def = TestRoleDefinition()
    new_role_data = role_def.preprocess_data(role_data)
    assert isinstance(new_role_data, AnsibleMapping)
    assert 'role' in new_role_data
    assert new_role_data['role'], 'a_role'
    assert not role_def.get_role_params()
    assert role_def._role_path, 'a_role'

    ############################
    # Case 2: role

# Generated at 2022-06-13 08:43:21.569750
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    attr_dict = {'role': 'foo.bar'}

    role_def = RoleDefinition()

    # Test data structure passed to method
    new_ds = role_def.preprocess_data(attr_dict)
    if not isinstance(new_ds, AnsibleMapping):
        raise AssertionError()
    if new_ds.get('role') != 'foo.bar':
        raise AssertionError()

    # Test string passed to method
    new_ds = role_def.preprocess_data('foo.bar')
    if not isinstance(new_ds, AnsibleMapping):
        raise AssertionError()
    if new_ds.get('role') != 'foo.bar':
        raise AssertionError()

# Generated at 2022-06-13 08:43:33.437570
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Note: the loader vey much needs to be mocked in order to fully test
    #       the preprocess function.
    from ansible.parsing.vault import VaultLib
    from ansible.parsing.vault import VaultSecret

    from ansible.parsing.vault import VaultAES256
    from ansible.parsing.vault import VaultAES256CBC

    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    dl = DataLoader()
    vault = VaultLib([(VaultSecret('foo', VaultAES256.ALIAS), VaultAES256())])

    var_manager = VariableManager()
    var_manager.extra_vars = dict(foo='bar')


# Generated at 2022-06-13 08:43:46.001424
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    #AnsibleError: role definitions must contain a role name
    with open("test_yaml/role_definition_test.yml",'r') as f:
        data = AnsibleMapping.load(f)
    r = RoleDefinition()
    result = r.preprocess_data(data)
    assert result.get("role") == "testrole"

    #AnsibleError: the role 'testrole' was not found
    with open("test_yaml/role_definition_test.yml",'r') as f:
        data2 = AnsibleMapping.load(f)
    r2 = RoleDefinition(role_basedir = "")
    result2 = r2.preprocess_data(data2)
    assert result2.get("role") == "testrole"


# Generated at 2022-06-13 08:43:53.191981
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_definition = RoleDefinition()
    role_definition.role = 'foo'

    assert role_definition.get_name(include_role_fqcn=False) == 'foo'
    assert role_definition.get_name(include_role_fqcn=True) == 'foo'

    role_definition._role_collection = 'collection'

    assert role_definition.get_name(include_role_fqcn=False) == 'foo'
    assert role_definition.get_name(include_role_fqcn=True) == 'collection.foo'

# Generated at 2022-06-13 08:44:01.029138
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # when here's no connection attribute in the role definition,
    # the connection attribute of the returned object should be
    # 'smart' by default.
    depend = RoleDefinition.load('role', variable_manager=dict(), loader=None, collection_list=[])
    assert depend.connection == 'smart'

    # if 'delegate_to' is specified in the role definition,
    # 'delegate_to' and 'connection' should be set to the value
    # in the role definition.
    depend = RoleDefinition.load(dict(role='role', delegate_to='dummy'), variable_manager=dict(), loader=None, collection_list=[])
    assert depend.connection == 'smart'
    assert depend.delegate_to == 'dummy'

    # if 'connection' is specified in the role definition,
    # 'delegate_to' and

# Generated at 2022-06-13 08:44:11.116324
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    # 1. Testing with include_role_fqcn=True
    # 1.1. Testing with role_collection=None and role=None
    attribute = Attribute()
    role_def = RoleDefinition()
    role_def.role = attribute
    assert role_def.get_name() == ''

    # 1.2. Testing with role_collection=None and role='role1'
    attribute = Attribute(value='role1')
    role_def = RoleDefinition()
    role_def.role = attribute
    assert role_def.get_name() == 'role1'

    # 1.3. Testing with role_collection='collection1' and role=None
    role_def = RoleDefinition(role_collection='collection1')
    role_def.role = attribute
    assert role_def.get_name() == 'collection1'



# Generated at 2022-06-13 08:44:20.369224
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_definition = RoleDefinition()
    role_definition._role_collection = None
    role_definition.role = "role1"
    assert role_definition.get_name() == "role1"
    assert role_definition.get_name(include_role_fqcn=False) == "role1"

    role_definition._role_collection = "collection"
    assert role_definition.get_name() == "collection.role1"
    assert role_definition.get_name(include_role_fqcn=False) == "role1"


# Generated at 2022-06-13 08:44:27.755912
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.loader import role_loader

    loader = DataLoader()

# Generated at 2022-06-13 08:44:37.705218
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # test with a simple string
    rb = RoleDefinition()
    ds = 'simple_string'
    new_ds = rb.preprocess_data(ds)
    assert new_ds['role'] == 'simple_string'

    # test with an empty dict
    rb = RoleDefinition()
    ds = dict()
    new_ds = rb.preprocess_data(ds)
    assert new_ds['role'] is None

    # test with a dict containing a name
    rb = RoleDefinition()
    ds = dict(name='simple_name')
    new_ds = rb.preprocess_data(ds)
    assert new_ds['role'] == 'simple_name'

    # test with a dict containing a role
    rb = RoleDefinition()
    ds = dict(role='simple_role')

# Generated at 2022-06-13 08:44:49.110821
# Unit test for method preprocess_data of class RoleDefinition

# Generated at 2022-06-13 08:44:57.517027
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role_def = RoleDefinition()
    role_def.preprocess_data( {} )

# Generated at 2022-06-13 08:45:06.102183
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_def = dict()
    rd = RoleDefinition(role_basedir=None, variable_manager=None, loader=None, collection_list=None)

    assert rd.get_name() == "", "Test #1 - RoleDefinition get_name"
    rd.role = "foo"
    assert rd.get_name() == "foo", "Test #2 - RoleDefinition get_name"
    rd._role_collection = "collection.action"
    assert rd.get_name() == "collection.action.foo", "Test #3 - RoleDefinition get_name"

    print("Test #4 - RoleDefinition get_name")
    rd.role = None
    try:
        rd.get_name()
    except AnsibleAssertionError:
        pass

# Generated at 2022-06-13 08:45:14.394340
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    class Options:
        connection = 'ssh'
        remote_user = 'remote_user'
        become = False
        become_method = 'sudo'
        become_user = 'root'
        check = False
        diff = False
        verbosity = 3

    loader = DataLoader()
    variable_manager = VariableManager()
    display = Display()
    play_context = PlayContext(loader=loader)

    # Simple role definition
    role_ds = 'my_role'
    ds = RoleDefinition(loader=loader, variable_manager=variable_manager, collection_list=[])

# Generated at 2022-06-13 08:45:23.606030
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    mock_ansible_module = dict(
        ANSIBLE_MODULE_ARGS=dict(
            role_basedir='/test',
            role_name='test.role'
        )
    )
    role_def = dict(
        role='test.role',
        with_items=[
            'test1',
            'test2'
        ],
        tasks=[
            dict(debug=dict(msg='test'))
        ]
    )
    rd = RoleDefinition.load(
        role_def,
        variable_manager=None,
        loader=None
    )
    preprocessed_role_def = rd.preprocess_data(role_def)
    assert preprocessed_role_def.keys() == ['role', 'with_items', 'tasks']
    assert preprocessed_role_

# Generated at 2022-06-13 08:45:36.235562
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext

    fake_play = Mock(name='play', spec=PlayContext)
    fake_variable_manager = Mock(name='variable_manager')
    fake_loader = Mock(name='loader')

    fake_loader.get_basedir.return_value = os.path.dirname(__file__)

    # Init RoleDefinition
    fake_rd = RoleDefinition(fake_play, '/default/roles/path', fake_variable_manager, fake_loader)

    # Test with valid ds
    agreed_ds = {
        'role': 'test1',
        'when': 'test2',
        'tags': 'test3',
        'ignore_errors': 'test4',
    }

    # Test behavior when ds is a string
    ds = 'test1'


# Generated at 2022-06-13 08:45:44.205746
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    """
    Basic check for role definition preprocess
    """
    rdef_string = "some_role"
    rdef_yaml_string = "role: some_role"
    mgr = AttributeDict()
    rdef_string.preprocess_data(mgr)
    assert rdef_string._ds == "some_role"
    rdef_yaml_string.preprocess_data(mgr)
    assert rdef_yaml_string._ds == {"role": "some_role"}

# Generated at 2022-06-13 08:45:54.380975
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    data = """

    - name: r1
      role:
        name: webserver
        something: else
      x: 2
    """
    # the data structure created by this is too complex, so we
    # just test the process with something simple
    ds = dict(name='r2', role='common')

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()

# Generated at 2022-06-13 08:46:09.151186
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext

    play_context = PlayContext()
    role_name = 'test_role'

    role_def = RoleDefinition()
    role_def._play = play_context
    role_def._loader = None
    role_def._role_basedir = u'roles'
    role_def._variable_manager = None

    # Test with a single-line yaml string
    ds = 'test_role'
    rv = role_def.preprocess_data(ds)

    assert role_def._role == role_name
    assert rv == role_name
    assert role_def._role_path == u''
    assert role_def._role_params == {}

    # Test with a role definition with just name

# Generated at 2022-06-13 08:46:16.675485
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible import constants as C
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.utils.collection_loader import AnsibleCollectionLoader

    # Instantiate a PlayContext
    play_context = PlayContext()

    # Instantiate a VariableManager
    variable_manager = VariableManager()

    # Instantiate a loader
    loader = DataLoader()

    # Instantiate a RoleDefinition
    role_definition = RoleDefinition(play=None, role_basedir=None, variable_manager=variable_manager, loader=loader)

    ############################################################################
    #
    # Test 1:
    #
    # Test with the following ds:
    #   ds = 'foo'
    #
    # The preprocessed ds should be:
    #   ds = {'

# Generated at 2022-06-13 08:46:29.886717
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Ensure RoleDefinition.preprocess_data() can handle a string
    ds = 'role_name'
    role_definition = RoleDefinition()
    role_definition.preprocess_data(ds)
    assert role_definition._ds == 'role_name'
    assert role_definition._role_params == dict()

    # Ensure RoleDefinition.preprocess_data() can handle an AnsibleMapping
    ds = AnsibleMapping()
    ds['role'] = 'role_name'
    ds['foo'] = 'bar'
    role_definition = RoleDefinition()
    role_definition.preprocess_data(ds)
    assert role_definition._ds == ds
    assert role_definition._role_params == dict(foo='bar')

    # Ensure RoleDefinition.preprocess_data() can handle an AnsibleBaseYAMLObject

# Generated at 2022-06-13 08:46:45.626264
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    def get_role_name(role_path, expected_name):
        collection_name = 'acme.test'
        collection_list = []
        if 'ansible_collections' in role_path:
            role_path, collection_name = role_path.split('/')
            collection_list = [collection_name]
        role_def = RoleDefinition(role_basedir='/path/to/role_basedir', collection_list=collection_list)
        role_def._ds = AnsibleMapping()
        role_def._ds['role'] = role_path
        assert role_def.get_name(include_role_fqcn=True) == '.'.join([collection_name, expected_name])
        assert role_def.get_name(include_role_fqcn=False) == expected_name



# Generated at 2022-06-13 08:46:59.367780
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Test preprocessing with name:role
    def test_name():
        role_definition = RoleDefinition(play=None, role_basedir=None, variable_manager=None, loader=None)
        ds = {'name': 'example'}

        new_ds = role_definition.preprocess_data(ds)

        assert new_ds == {'role': 'example'}

    test_name()

    # Test preprocessing with role:role
    def test_role():
        role_definition = RoleDefinition(play=None, role_basedir=None, variable_manager=None, loader=None)
        ds = {'role': 'example'}

        new_ds = role_definition.preprocess_data(ds)

        assert new_ds == {'role': 'example'}

    test_role()

    # Test

# Generated at 2022-06-13 08:47:02.804515
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    """
    Test to validate method get_name of class RoleDefinition
    """
    roleResource = RoleDefinition()
    roleResource._role_collection = "abc"
    roleResource.role = "def"
    name = roleResource.get_name()
    assert name == "abc.def"
    name = roleResource.get_name(False)
    assert name == "def"

# Generated at 2022-06-13 08:47:10.154193
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_name = "foo"
    role_collection = "namespace.collection"

    role_definition = RoleDefinition()
    role_definition.role = role_name

    assert role_name == role_definition.get_name(include_role_fqcn=False)

    role_definition._role_collection = role_collection
    assert role_collection + "." + role_name == role_definition.get_name(include_role_fqcn=True)

# Generated at 2022-06-13 08:47:21.801311
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    test_cases = [
        # test case tuple format:
        # (role_name, role_collection, include_role_fqcn, expected value)
        ('example.role', None, False, 'example.role'),
        ('example.role', None, True, 'example.role'),
        ('example.role', 'example.collection', False, 'example.role'),
        ('example.role', 'example.collection', True, 'example.collection.example.role'),
    ]
    for data in test_cases:
        test_case_name = 'RoleDefinition.get_name(role_name=%s, role_collection=%s, ' \
            'include_role_fqcn=%s)' % data[0:3]
        role_name, role_collection, include_role_fqcn, expected_value = data

# Generated at 2022-06-13 08:47:29.499232
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import os
    import sys
    import unittest

    if not os.path.exists('./test/units/module_utils/basic.py'):
        raise unittest.SkipTest("can't find basic.py in ./test/units/module_utils")
    sys.stdout.write('--- TESTING RoleDefinition.preprocess_data() ---\n')

    from ansible.plugins import module_loader
    from ansible.vars.manager import VariableManager

    try:
        from ansible.parsing.dataloader import DataLoader
    except ImportError:
        from ansible.vars.dataloader import DataLoader

    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition


# Generated at 2022-06-13 08:47:30.360402
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    pass

# Generated at 2022-06-13 08:47:45.129760
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    class Loader(object):
        @staticmethod
        def get_basedir():
            return None

    class VariableManager(object):
        @staticmethod
        def set_nonpersistent_facts(dict):
            return None

        @staticmethod
        def set_facts(dict):
            return None

    class Play(object):
        def __init__(self):
            self.sent_capabilities_list = ['network_cli', 'network_api']
            self.default_vars = None

    role_name = 'role_name'
    role = RoleDefinition(variable_manager=VariableManager(), play=Play(), loader=Loader())
    # assert that values returned by the method get_name() is the same as the role name in the RoleDefinition class
    assert role.get_name(include_role_fqcn=True) == role

# Generated at 2022-06-13 08:47:53.561271
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    class MockBaseClass(Base):
        def __init__(self):
            self._attributes = dict()
            self._loader = None
            self._valid_attrs = dict()

    class MockRoleDefinition(RoleDefinition):
        def __init__(self, play, role_basedir, variable_manager, loader, collection_list):
            RoleDefinition.__init__(self, play, role_basedir, variable_manager, loader, collection_list)

            class MockAttribute(Attribute):
                def __init__(self):
                    Attribute.__init__(self)

            self._valid_attrs['role'] = MockAttribute()
            self._valid_attrs['name'] = MockAttribute()

    # make a mock object that acts like the loader object to avoid
    # needing to set up a full-blown ansible environment for this test


# Generated at 2022-06-13 08:48:05.710997
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # import pdb; pdb.set_trace()
    testname = type(test_RoleDefinition_preprocess_data).__name__

    rd = RoleDefinition(dict())

    # test with simple string role name
    test = "test"
    expected = {"role": "test"}
    actual = rd.preprocess_data(test)

# Generated at 2022-06-13 08:48:23.529387
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import sys
    from ansible.parsing.vault import VaultLib
    from ansible.plugins.loader import get_all_plugin_loaders

    # Initialize Ansible
    from ansible.module_utils.six import PY3
    if PY3:
        from ansible.utils.unsafe_proxy import AnsibleUnsafeText
        unsafe_proxy_type = AnsibleUnsafeText
    else:
        from ansible.utils.unsafe_proxy import unicode as AnsibleUnsafeText
        unsafe_proxy_type = AnsibleUnsafeText

    # role_basedir = '/etc/ansible/roles'
    playbook_path = '/home/sandeepkumar/ansible/test/test_role/test1.yml'
    # hostname = "localhost"


# Generated at 2022-06-13 08:48:34.037117
# Unit test for method preprocess_data of class RoleDefinition

# Generated at 2022-06-13 08:48:47.854783
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
  import json
  import os
  import os.path
  import shutil
  import tempfile
  import unittest

  from ansible.playbook.role_definition import RoleDefinition
  from ansible.playbook.play_context import PlayContext
  from ansible.template import Templar
  from ansible.vars.manager import VariableManager

  class TestRoleDefinition(unittest.TestCase):
    def setUp(self):
      pass

    def tearDown(self):
      pass

    def test_RoleDefinition_preprocess_data_with_role_as_string(self):
      datastructure_for_test = 'role-1'
      expected_result = {'role': 'role-1'}

      role_definition = RoleDefinition()

# Generated at 2022-06-13 08:48:55.619239
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleMapping
    role_def = RoleDefinition(name='')
    role_name = role_def._load_role_name('role')
    assert role_name == 'role'
    ds = AnsibleMapping(dict(role='role_path'))
    ds.ansible_pos = dict()
    role_name, role_path = role_def._load_role_path('role_path', ds.ansible_pos)
    assert role_name == 'role_path'
    assert role_path == 'role_path'
    ds = dict(role='role_path', force=True)
    new_ds, role_params = role_def._split_role_params(ds)

# Generated at 2022-06-13 08:49:10.344694
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import ansible.playbook.role_include as role_include
    play = None
    variable_manager = None
    loader = None
    collection_list = None
    fqr = 'ns.col.role'
    fqr_dict_1 = dict(role=fqr)
    fqr_dict_2 = dict(name=fqr)

    # Test 1 (role)
    rd = RoleDefinition(play=play, variable_manager=variable_manager, loader=loader, collection_list=collection_list)
    rd._load_role_name = lambda x: x
    rd._load_role_path = lambda x: (x, x)
    rd._split_role_params = lambda x: (x, {})
    rd.preprocess_data(fqr)

# Generated at 2022-06-13 08:49:19.505295
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    os.environ['ANSIBLE_CONFIG'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ansible.cfg")
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    loader = DataLoader()
    play = Play().load('test_role', loader=loader, variable_manager=VariableManager(), loader_basedir='.', inventory=InventoryManager(loader=loader, sources=[]))
    variable_manager = VariableManager()
    variable_manager.set_inventory(InventoryManager(loader=loader, sources=[]))

# Generated at 2022-06-13 08:49:33.502309
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role_def = RoleDefinition()
    base_attrs = frozenset(['connection','become','remote_user'])
    test_attrs = frozenset(['str_attr', 'dict_attr', 'int_attr'])

    # make a dict of test names, role definition dicts, and expected results
    # the role definition dicts contain valid and invalid attributes

# Generated at 2022-06-13 08:49:34.157848
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    pass

# Generated at 2022-06-13 08:49:47.018772
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # testing simple string data
    ds = "test_role_name"
    role_definition = RoleDefinition()
    assert role_definition.preprocess_data(ds) == "test_role_name"
    assert role_definition._ds == "test_role_name"
    assert role_definition._role_params == dict()

    # testing role: foo ...
    ds = dict()
    ds['role'] = "test_role_name"
    role_definition = RoleDefinition()
    assert role_definition.preprocess_data(ds) == ds
    assert role_definition._ds == ds
    assert role_definition._role_params == dict()

    # testing name: foo ...
    ds = dict()
    ds['name'] = "test_role_name"
    role_definition = RoleDefinition()
   

# Generated at 2022-06-13 08:49:57.904734
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_definition = RoleDefinition()
    role_definition._role_collection = ''
    role_definition.role = 'role'
    assert role_definition.get_name() == 'role'

    role_definition._role_collection = None
    assert role_definition.get_name() == 'role'

    role_definition._role_collection = 'namespace'
    assert role_definition.get_name() == 'namespace.role'

    role_definition.role = 'role_name'
    assert role_definition.get_name() == 'namespace.role_name'

    # Test with include_role_fqcn=False
    assert role_definition.get_name(include_role_fqcn=False) == 'role_name'

# Generated at 2022-06-13 08:50:14.096194
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():

    import six
    from ansible.collection_loader._collection_finder import CollectionFinder
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    from units.compat.mock import MagicMock, patch
    from units.mock.loader import DictDataLoader

    # Set up for a simple collection
    collection_name = 'simple'
    collection_path = '/tmp/%s' % collection_name
    collection_ns = '.'
    collection_version = '1.0.0'

    # Create a mock collection
    collection_obj = MagicMock()
    collection_obj.__getitem__ = lambda s, key: {
        'ns': collection_ns,
        'name': collection_name,
        'version': collection_version,
    }[key]
    collection_finder

# Generated at 2022-06-13 08:50:20.710032
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.utils.collection_loader import AnsibleCollectionRef
    from ansible.plugins.loader import add_all_plugin_dirs

    add_all_plugin_dirs()

    Playbook = AnsibleCollectionRef.from_string('ansible.posix')

    Inventory = AnsibleCollectionRef.from_string('ansible_collections.community.general.plugins.inventory.host')

    r = RoleDefinition()
    r._role_basedir = "/Users/user/ansible_repos/ansible/lib/ansible/roles"
    r._collection_list

# Generated at 2022-06-13 08:50:28.167761
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Base test role_name is a string
    role_name = "dummy-role"
    rd = RoleDefinition()

    # Test role_name is a string
    rd.preprocess_data(role_name)
    assert rd._role == "dummy-role"

    # Test role_name is a integer
    ds = dict(name=12345)
    rd.preprocess_data(ds)
    assert rd._role == "12345"

# Generated at 2022-06-13 08:50:37.443050
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_definition = RoleDefinition()

    assert role_definition.get_name() == 'ansible.legacy.role', "Unexpected role name for Ansible role"

    role_definition = RoleDefinition()
    role_definition._role_collection = 'namespace.collection'
    role_definition._attributes.get('role', 'role_name')

    assert role_definition.get_name(include_role_fqcn=False) == 'role_name', "Unexpected role name for role from collection"
    assert role_definition.get_name(include_role_fqcn=True) == 'namespace.collection.role_name', "Unexpected role name for role from collection"

# Generated at 2022-06-13 08:50:47.801305
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    """
    Test the preprocess_data method from the RoleDefinition class
    """
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.role import Role

    role_ds = '''
- name: test1
  role: test1_role
  become: no
'''
    loader = AnsibleLoader(role_ds)
    results = []
    for role_ds in loader.get_single_data():
        r = RoleDefinition(None, '.', None, None)
        r.preprocess_data(role_ds)
        results.append(r)

    # this role definition should have a role name of "test1_role"
    # and no role params

# Generated at 2022-06-13 08:50:54.788797
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader

    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost,', 'otherhost,'])
    variable_manager.set_inventory(inventory)

    play_context = PlayContext()
    play_context.network_os = 'ios'

    role_definition = RoleDefinition(loader=loader, variable_manager=variable_manager, play=play_context)

    assert dict(name="foo") == role_definition.preprocess_data(dict(name="foo"))

# Generated at 2022-06-13 08:51:05.702509
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_result import TaskResult
    from ansible.executor.play_iterator import PlayIterator
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    display.verbosity = 3

    inventory = InventoryManager(loader=DataLoader())
    h1 = Host('h1')
    h2 = Host('h2')
    h3 = Host('h3')
    g = Group('g')
    g.add_

# Generated at 2022-06-13 08:51:18.099292
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    # Case 1
    # Data structure not valid
    # Input:
    #   ds: 1234
    # Expected output:
    #   AnsibleAssertionError exception
    try:
        rd = RoleDefinition()
        rd.preprocess_data(1234)
        assert False
    except AnsibleAssertionError:
        assert True

    # Case 2
    # Simple role name as string
    # Input:
    #   ds: 'galaxy'
    # Expected output:
    #   new_ds: 'galaxy'
    rd = RoleDefinition()
    new_ds = rd.preprocess_data('galaxy')
    assert 'galaxy' == new_ds

    # Case 3
    # Role name as string with variables
    # Input:
    #   ds: 'galaxy

# Generated at 2022-06-13 08:51:28.879438
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.utils.vars import combine_vars

    role = 'role1'
    role_path = './path/to/role/' + role
    role_params = {'foo': 'bar'}

    vars = {'name': role, 'role': role, 'role_path': role_path}
    vars.update(role_params)

    # create data structure
    yaml_data = AnsibleMapping()
    yaml_data.ansible_pos = {'line': 1, 'col': 1}
    yaml_data.update(vars)

# Generated at 2022-06-13 08:51:40.253539
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    class Play:

        class RoleDefinition(RoleDefinition):

            pass

    class VariableManager:

        def get_vars(self, play):
            return dict()

    class Loader:

        def __init__(self):
            self.basedir = '/path/to/ansible/playbook'

        def get_basedir(self):
            return self.basedir

        def path_exists(self, path):
            if path == '/path/to/ansible/playbook':
                return True
            return False

    # test role name included in the role definition data structure
    role_def = Play.RoleDefinition()
    ds = 'test_role_1'
    result = role_def.preprocess_data(ds)
    assert result == ds

    role_def = Play.RoleDefinition()
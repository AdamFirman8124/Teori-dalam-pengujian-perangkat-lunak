

# Generated at 2022-06-13 08:41:56.765212
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    role = ("common", "/tmp/common", None)
    collection_list = [('testcoll', {'name': 'testcoll', 'path': '/tmp'},
                        [role])]
    # test passing a bare string
    rd = RoleDefinition()
    rd._variable_manager = variable_manager
    rd._loader = loader
    rd._collection_list = collection_list

    data = 'common'
    new_data = rd.preprocess_data(data)
    assert isinstance(new_data, dict)
    assert new_data.get('role') == 'common'

# Generated at 2022-06-13 08:42:09.578485
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play import Play

    # valid role definition with single string
    class_to_test = RoleDefinition(Play())
    yaml_data = 'common'
    expected_data = {'role': 'common'}
    class_to_test._valid_attrs = {'role': Attribute()}
    assert expected_data == class_to_test.preprocess_data(yaml_data)

    # valid role definition with single string and special_var
    yaml_data = 'common_{{ my_var }}'
    expected_data = {'role': 'common_{{ my_var }}'}
    assert expected_data == class_to_test.preprocess_data(yaml_data)

    # valid role definition with role: and name:

# Generated at 2022-06-13 08:42:20.729169
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.utils.vault import VaultLib
    from ansible.utils.encrypt import do_encrypt_text

    # Mock objects
    class Playbook(object):
        def __init__(self, loader=None, variable_manager=None):
            self._loader = loader
            self._variable_manager = variable_manager


# Generated at 2022-06-13 08:42:23.874632
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    display = Display()
    name = display.test_role.__name__
    display.test_role.__name__ = 'my namespace.mycollection.myrole'
    obj = RoleDefinition()
    obj.role = 'my namespace.mycollection.myrole'
    result = obj.get_name()
    assert(display.test_role.__name__ == result)
    display.test_role.__name__ = name

# Generated at 2022-06-13 08:42:28.205267
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    """
    Test RoleDefinition.preprocess_data
    """
    # Simple role
    data = dict(name='my_role')
    role_def = RoleDefinition()
    data = role_def.preprocess_data(data)
    assert data['role'] == 'my_role'

    assert role_def._role_path is not None
    assert role_def._role_params == {}
    assert role_def._role_defined is True

# Generated at 2022-06-13 08:42:37.438864
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role_name = 'role_name'
    role_path = '/path/to/role'

    # Make a RoleDefinition object
    # rd = RoleDefinition(role_basedir=role_path)
    # # rd.preprocess_data(role_name)
    # assert 1==2

    # # Make a RoleDefinition with a dict
    # rd = RoleDefinition(role_basedir=role_path)
    # rd.preprocess_data({'name': role_name})
    # assert 1==2

# Generated at 2022-06-13 08:42:50.763161
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    def _test_process(ds, out):
        rd = RoleDefinition()
        rd.preprocess_data(ds)
        assert rd._attributes == out

    # Test for a string as ds
    test_data = "{'foo': 'bar'}"
    expected_data = {'role': '{foo}'}
    _test_process(test_data, expected_data)

    # Test for integer as ds
    test_data = 42
    expected_data = {'role': '42'}
    _test_process(test_data, expected_data)

    # Test for integer as ds
    test_data = 'foo'
    expected_data = {'role': 'foo'}
    _test_process(test_data, expected_data)

    # Test for dictionary as ds
   

# Generated at 2022-06-13 08:43:04.861217
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    vars_manager = VariableManager()

    # FIXME: the test case below should eventually be handled by the playbook loader
    #        as it does not currently, we have to do it here

    test_case = dict(
        name='test-role',
        role='test-role',
    )

    role_def_obj = RoleDefinition()
    role_def_obj.preprocess_data(test_case)

    assert role_def_obj._role_path == 'test-role', "The role path must be 'test-role'"

    test_case = dict(
        name='test-role',
        role=dict(name='test-role'),
    )

    role_def_

# Generated at 2022-06-13 08:43:09.265754
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_definition = RoleDefinition()
    role_definition._role = 'role_name'
    role_definition._role_collection = 'collection_name'

    assert role_definition.get_name() == 'collection_name.role_name'
    assert role_definition.get_name(include_role_fqcn=False) == 'role_name'

    role_definition._role_collection = ''

    assert role_definition.get_name() == 'role_name'

# Generated at 2022-06-13 08:43:18.492870
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    def get_loader(data):
        loader = DataLoader()
        data_yaml = loader.load(data)
        return AnsibleLoader(data_yaml)

    loader = get_loader("""
        - name: foo
          role:
            name: test
            foo: bar
    """)

    loader2 = get_loader("""
        - name: foo
          role: test
    """)

    va = VariableManager()

    # Test with string
    rd = RoleDefinition(loader=loader, variable_manager=va)
    rd.preprocess_data("test")
    assert rd.role

# Generated at 2022-06-13 08:43:36.763826
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    '''
    Unit test for method preprocess_data of class RoleDefinition
    '''

    import os
    import tempfile

    tempdir = tempfile.mkdtemp(prefix='ansible-test-role')
    td = tempdir
    role_def = {
        'role': 'foobar'
    }
    role_params = {
        'role': 'foobar'
    }

    rd = RoleDefinition()
    rd._role_basedir = tempdir
    rd._role_path = os.path.join(td, 'roles', 'foobar')
    rd._role_params = dict(role_params)

    role_def_1 = {
        'role': 'bazqux'
    }

# Generated at 2022-06-13 08:43:51.957932
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    #Fails with TypeError: super(type, obj): obj must be an instance or subtype of type
    #expected value: instance of 'RoleDefinition'
    #actual value: RoleDefinition(role='nginx')
    #assert_raises(TypeError, RoleDefinition, 'role', 'nginx')
    #assert_raises(AssertionError, RoleDefinition, {'role': 123})
    #assert_raises(AnsibleError, RoleDefinition, role='nginx')
    assert_raises(AnsibleError, RoleDefinition, 'nginx')
    assert_raises(AnsibleError, RoleDefinition, {})
    assert_raises(AnsibleError, RoleDefinition, {'name': 'nginx'})
    assert_raises(AnsibleError, RoleDefinition, {'role': 'test'})



# Generated at 2022-06-13 08:44:00.630906
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    # Create test instances of role definition
    role_definition_1 = RoleDefinition()
    role_definition_2 = RoleDefinition()
    role_definition_3 = RoleDefinition()
    # True parameter
    # No collection
    assert role_definition_1.get_name(True) == ""
    # No collection
    role_definition_2._role_path = "C:/Ansible/Collection/Namespace/Role"
    role_definition_2.role = "Namespace.Role"
    assert role_definition_2.get_name(True) == "Namespace.Role"
    # Collection
    role_definition_3._role_path = "C:/Ansible/Collection/Namespace/Role"
    role_definition_3._role_collection = "Namespace.Collection"

# Generated at 2022-06-13 08:44:08.897610
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Definition of dict
    dict1 = dict(dict1='1', dict2='2', dict3='3')
    dict2 = dict(dict1='1', dict2='2', dict3='3')
    dict3 = dict(dict1='1', dict2='2', dict3='3')
    dict4 = dict(role='role_name', dict4='4')
    dict_list = [dict1, dict2, dict3, dict4]

    # expected role name dict for dict1, dict2, dict3
    role_name_dict_expected = dict(name='dict1', role='role_name')

    # expected role_params dict for dict1, dict2, dict3
    role_params_dict_expected = dict(dict2='2', dict3='3')

    # expected role_path string
    role_path

# Generated at 2022-06-13 08:44:18.558125
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    class MockRoleDefinitionPlay(object):
        pass
    class MockRoleDefinitionVariableManager(object):
        class MockRoleDefinitionPlayVariableManager_get_vars(object):
            pass
        def get_vars(self):
            return self.MockRoleDefinitionPlayVariableManager_get_vars()
    class MockRoleDefinitionLoader(object):
        pass
    play = MockRoleDefinitionPlay()
    variable_manager = MockRoleDefinitionVariableManager()
    loader = MockRoleDefinitionLoader()
    role_basedir = '/tmp/'

    role_definition = RoleDefinition(play, role_basedir, variable_manager, loader)
    yaml_object = AnsibleBaseYAMLObject()
    role_name = 'httpd'
    role_name_path = '/tmp/httpd'
    role_name_params = dict()
    role

# Generated at 2022-06-13 08:44:26.892557
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    fake_all_vars = dict()
    fake_templar = Templar(loader=None, variables=fake_all_vars)

    class FakeLoader:
        def get_basedir():
            return "get_basedir_fake_return"

    class FakeVariableManager:
        def __init__(self, all_vars):
            self.fake_all_vars = all_vars
        def get_vars(self, play=None):
            return self.fake_all_vars

    fake_role_def = RoleDefinition(play=None, role_basedir=None, variable_manager=FakeVariableManager(fake_all_vars), loader=FakeLoader(), collection_list=None)

    assert fake_role_def._load_role_name('test_role') == 'test_role'
    assert fake_

# Generated at 2022-06-13 08:44:33.507729
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    variable_manager = VariableManager()
    variable_manager.set_inventory(loader.load_from_file('tests/inventory'))


# Generated at 2022-06-13 08:44:44.890578
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    def test_case(expected, value1, value2):
        role_def = RoleDefinition()
        role_def._role_collection = value2
        role_def.role = value1
        assert role_def.get_name(False) == expected

    test_case('ansible_galaxy.role1', 'role1', 'ansible_galaxy')
    test_case('ansible_galaxy.role1', 'role1', None)
    test_case('role1', 'role1', None)
    test_case('ansible_galaxy.role1', 'role1', 'ansible_galaxy')
    test_case('role1', 'role1', 'ansible_galaxy')

# Generated at 2022-06-13 08:44:51.682790
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.tests.unit.test_attribute import TestAttribute
    import ansible.playbook.role_include as role_include
    from ansible.template import Templar
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    import ansible.plugins.loader as plugins_loader

    class FakeVars:
        def get_vars(self, play=None):
            return dict()

    class FakeLoader:
        def get_basedir(self):
            return '/path/to/basedir'

        def path_exists(self, path):
            return True

    fake_vars = FakeVars()
    fake_loader = FakeLoader()

    # Test 1: If a role name is a string

# Generated at 2022-06-13 08:45:01.685867
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    # test a malformed role definition
    try:
        RoleDefinition.preprocess_data(None)
    except AnsibleAssertionError:
        pass
    else:
        raise AssertionError('should not get here. I think the previous instruction should fail!')

    # test a malformed role definition
    try:
        RoleDefinition.preprocess_data(123)
    except AnsibleAssertionError:
        pass
    else:
        raise AssertionError('should not get here. I think the previous instruction should fail!')

    # test a malformed role definition
    try:
        RoleDefinition.preprocess_data({})
    except AnsibleAssertionError:
        pass
    else:
        raise AssertionError('should not get here. I think the previous instruction should fail!')

    # test a malformed role definition

# Generated at 2022-06-13 08:45:23.179887
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.plugins.loader import connection_loader

    # Define a mock object for the loader
    class MockLoader(object):
        def get_basedir(self):
            return ''

        def path_exists(self, path):
            return True

    # Define a mock object for the variable manager
    class MockVariableManager(object):
        def get_vars(self, play=None):
            return dict()

    # Define a mock object for the PlayContext
    class MockPlayContext(object):
        connection = 'smart'

    # Create a connection plugin to return when that is requested. This can
    # just be used to synthetically create a

# Generated at 2022-06-13 08:45:35.889505
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.template import Templar
    from ansible.utils.shlex import shlex_split

    play_context = PlayContext()
    variable_manager = VariableManager()
    loader = None
    play = Play().load({}, variable_manager=variable_manager, loader=loader)
    playbook = PlaybookExecutor()
    templar = Templar(loader=loader, variables=variable_manager.get_vars(play=play))
    role_basedir = playbook.get_role_basedir(play)

    example_ds1 = {'role': 'my_role'}
   

# Generated at 2022-06-13 08:45:50.392518
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible import constants as C

    role_definition_path = 'test/units/lib/ansible_test_{0}/test_data/ansible-role-requirements/'
    ansible_roles_path = 'test/units/lib/ansible_test_{0}/test_data/ansible-role-requirements/ansible-roles/'
    ansible_collections_path = 'test/units/lib/ansible_test_{0}/test_data/ansible-role-requirements/ansible-collections/'

    C.ANSIBLE_ROLES_PATH = ansible_roles_path.format('2.8')
    C.ANSIBLE_COLLECTIONS_PATHS = [ansible_collections_path.format('2.8')]


# Generated at 2022-06-13 08:46:03.523673
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    # Initialize
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    variable_manager = VariableManager()
    inventory = Inventory(variable_manager, '/tmp')
    variable_manager.set_inventory(inventory)
    play_context = dict()

    class Play(object):
        def __init__(self):
            self.ROLE_CACHE = dict()
            self.basedir = '/tmp'
            self.context = play_context
            self.name = 'test_play'
            self.tags = ['all']
            self.vars = dict()

        def set_variable_manager(self, variable_manager):
            self.variable_manager = variable_manager

        def set_loader(self, loader):
            self.loader = loader


# Generated at 2022-06-13 08:46:16.429281
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Test with simple string
    ds = 'role_name'
    rd = RoleDefinition()
    preprocessed_data = rd.preprocess_data(ds)
    assert preprocessed_data == dict(role=ds)

    # Test with dict
    ds = dict(role_name=dict(role='role_name', become=True, tags=['test']))
    rd = RoleDefinition()
    preprocessed_data = rd.preprocess_data(ds)
    assert preprocessed_data == dict(role='role_name', become=True, tags=['test'])

    # Test with invalid datastructure
    ds = [1, 2, 3, 4]
    rd = RoleDefinition()

# Generated at 2022-06-13 08:46:25.836543
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    rd = RoleDefinition()
    rd.role = 'test'
    assert rd.get_name(include_role_fqcn=False) == 'test'
    assert rd.get_name(include_role_fqcn=True) == 'test'
    rd._role_collection = 'test_col'
    assert rd.get_name(include_role_fqcn=False) == 'test'
    assert rd.get_name(include_role_fqcn=True) == 'test_col.test'

# Generated at 2022-06-13 08:46:35.402607
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role_definition = RoleDefinition()

    assert role_definition.preprocess_data(
        dict(role='common', become='true')
    ) == dict(role='common', become='true')

    assert role_definition.preprocess_data(
        dict(name='common', become='true')
    ) == dict(role='common', become='true')

    assert role_definition.preprocess_data(
        dict(role='common', become='true', unknown_key='unknown')
    ) == dict(role='common', become='true')

    assert role_definition.preprocess_data(
        dict(role='common', become='true', unknown_key='unknown')
    ) == dict(role='common', become='true')


# Generated at 2022-06-13 08:46:40.826806
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_definition = RoleDefinition()
    role_definition.role = 'rolename'
    role_definition._role_collection = 'namespace'

    assert 'namespace.rolename' == role_definition.get_name()
    assert 'rolename' == role_definition.get_name(False)

# Generated at 2022-06-13 08:46:54.749354
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    """
    This method tests the get_name method of class RoleDefinition
    """

    # Testing with include_role_fqcn parameter = False
    role_definition_obj = RoleDefinition()
    role_definition_obj.role = "role_name"
    assert role_definition_obj.get_name(include_role_fqcn=False) == "role_name"

    # Testing with include_role_fqcn parameter = True but _role_collection parameter is None
    role_definition_obj._role_collection = None
    assert role_definition_obj.get_name(include_role_fqcn=True) == "role_name"

    # Testing with include_role_fqcn parameter = True and _role_collection parameter is not None
    role_definition_obj._role_collection = "collection_name"
    assert role

# Generated at 2022-06-13 08:47:00.774168
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    # Test with empty string for both _role_collection and role
    # Expected: return ''
    r = RoleDefinition()
    assert r.get_name() == ''

    # Test with non-empty string for _role_collection and empty string for role
    # Expected: return 'namespace.collection'
    r = RoleDefinition()
    r._role_collection = 'namespace.collection'
    assert r.get_name() == r._role_collection

    # Test with empty string for _role_collection and non-empty string for role
    # Expected: return 'role'
    r = RoleDefinition()
    r.role = 'role'
    assert r.get_name() == r.role

    # Test with non-empty string for _role_collection and non-empty string for role
    # Expected: return 'namespace.collection

# Generated at 2022-06-13 08:47:29.424401
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.module_utils.six import PY3
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.vars.manager import VariableManager

    # For now we can't test without the loader and variable_manager,
    # so we'll just skip these tests on python3 where we know we can't load
    # the python2 code
    if PY3:
        return

    loader = DataLoader()

    # init vars
    all_group_vars = combine_vars(loader=loader, variables={'all': {u'foo': u'fooval'}})
    host_vars = combine_vars(loader=loader, variables={'hostvars': {u'bar': u'barval'}})
    group

# Generated at 2022-06-13 08:47:44.153857
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.template import Templar
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.parsing.yaml.loader import AnsibleLoader

    play_context = PlayContext()
    variable_manager = VariableManager()
    loader = AnsibleLoader(None, variable_manager=variable_manager)
    play = Play()

    role_definition = RoleDefinition(play=play, variable_manager=variable_manager, loader=loader)
    role_def = loader.load_from_string(dict_to_load, variable_manager=variable_manager, loader=loader)

    expected_role_def = loader.load_from_string(expected_dict, variable_manager=variable_manager, loader=loader)

   

# Generated at 2022-06-13 08:47:50.185099
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role = RoleDefinition(role_basedir='/etc/ansible/roles', variable_manager=None, loader=None)
    role.role = 'apache'
    assert 'apache' == role.get_name()

    role.role = 'test'
    role._role_collection = 'galaxy'
    assert 'galaxy.test' == role.get_name()

    role._role_collection = ''
    assert 'test' == role.get_name()

# Generated at 2022-06-13 08:48:03.269660
# Unit test for method get_name of class RoleDefinition

# Generated at 2022-06-13 08:48:14.535391
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    settings = dict(
        connection='local',
        gather_facts='no',
        log_path='/tmp/ansible.log',
        roles_path='',
    )

    play_source = dict(
        name="Ansible Play",
        hosts='localhost',
        gather_facts='no',
        roles=['common', 'webservers'],
    )

    pc = Playbook.load_from_file('/tmp/hosts', loader=DataLoader(), variable_manager=VariableManager())

    pb = Play().load(play_source, variable_manager=pc.variable_manager, loader=pc._loader)

    assert pb.roles == ['common', 'webservers']

    pb.preprocess_data()


# Generated at 2022-06-13 08:48:21.790850
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    loader = DictDataLoader({})
    role_basedir = 'roles/'
    role_data = dict(
        name = 'test.role',
        sudo = True,
        sudo_user = 'user1',
        tags = ['tag1', 'tag2']
    )

    # test the functionality for a dict structure for the RoleDefinition
    role_object = RoleDefinition.load(data=role_data, loader=loader, role_basedir=role_basedir)
    role_object.finalize()

    role_name = role_object.get_name()
    role_path = role_object.get_role_path()
    role_params = role_object.get_role_params()
    assert role_name == 'test.role'
    assert role_path == 'roles/test.role/'
   

# Generated at 2022-06-13 08:48:33.138776
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():

    rd = RoleDefinition()
    assert rd.get_name() == '<no name set>'

    # the role_name parameter is a string
    rd = RoleDefinition()
    rd._attributes['role'] = 'test'
    assert rd.get_name() == 'test'

    # the role_name parameter is a FQCN string
    rd = RoleDefinition()
    rd._attributes['role'] = 'test.test'
    assert rd.get_name() == 'test.test'

    # the role_name parameter is a FQCN string and the collection_list
    # parameter is not empty
    rd = RoleDefinition()
    rd._role_collection = 'test'
    rd._attributes['role'] = 'test.test'

# Generated at 2022-06-13 08:48:46.301148
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.group import Group
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    display = Display()
    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)

    # RoleDefinition with only role name as a string
    role_def1 = RoleDefinition()
    role_name = role_def1.preprocess_data('test-role')
    assert role_name == 'test-role'
    assert role_def1._role_path is None

    # RoleDefinition with role name as a string and role_basedir set
    role_def2 = RoleDefinition(role_basedir='/tmp')

# Generated at 2022-06-13 08:48:54.288258
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources=None)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()


# Generated at 2022-06-13 08:48:57.788323
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    rd = RoleDefinition(role_basedir='.')
    rd._role_collection = None
    rd.role = 'role-name'
    assert rd.get_name() == 'role-name'

    rd._role_collection = 'collection-name'
    assert rd.get_name() == 'collection-name.role-name'

# Generated at 2022-06-13 08:49:46.447948
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    rd = RoleDefinition()
    assert rd.get_name() == ''
    rd._role = 'role'
    assert rd.get_name() == 'role'
    rd._role_collection = 'namespace.collection'
    assert rd.get_name() == 'namespace.collection.role'
    rd._role = ''
    assert rd.get_name() == 'namespace.collection'


# Generated at 2022-06-13 08:49:49.348221
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    r = RoleDefinition()
    assert r.get_name() == '.'.join(x for x in (None, r.role) if x)


# Generated at 2022-06-13 08:50:00.194223
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    collections_paths = C.COLLECTIONS_PATHS
    C.COLLECTIONS_PATHS = [os.path.join(os.path.dirname(__file__), '../../../test/data/collections')]

    # Without role names
    role_def = RoleDefinition(role_basedir='/a/b/c')
    role_def.role = 'test'
    assert role_def.get_name() == 'test'

    # Namespace Role
    collections_paths = C.COLLECTIONS_PATHS
    C.COLLECTIONS_PATHS = [os.path.join(os.path.dirname(__file__), '../../../test/data/collections')]
    role_def = RoleDefinition(role_basedir='/a/b/c')
    role_

# Generated at 2022-06-13 08:50:10.086416
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    play = Base()
    play.role_search_path = ''
    rd = RoleDefinition(play=play)
    rd._role = 'role1'
    assert rd.get_name() == 'role1'

    play.role_search_path = 'roles'
    rd = RoleDefinition(play=play)
    rd._role = 'role1'
    assert rd.get_name() == 'role1'

    play.role_search_path = ''
    rd = RoleDefinition(play=play)
    rd._role = 'role1'
    rd._role_collection = 'namespace'
    assert rd.get_name() == 'namespace.role1'

# Generated at 2022-06-13 08:50:18.632123
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    rd = RoleDefinition(role_basedir='/home/vagrant/test')
    ds = 'TestName'
    actual_new_ds = rd.preprocess_data(ds)
    assert actual_new_ds == 'TestName'

    ds = dict(role='TestName')
    actual_new_ds = rd.preprocess_data(ds)
    assert actual_new_ds == dict(role='TestName')

    ds = dict(role='TestName', not_param=dict())
    expected_new_ds = dict(role='TestName')
    expected_params = dict(not_param=dict())
    actual_new_ds = rd.preprocess_data(ds)
    assert actual_new_ds == expected_new_ds
    assert rd._role_params == expected_params



# Generated at 2022-06-13 08:50:30.680620
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    template_variables = {
        'role_name': 'test_role'
    }
    template_loader = DictDataLoader({
        "role_name": "[{role_name}]"
    })
    template_variable_manager = VariableManager(loader=template_loader, inventory=None)
    template_variable_manager.set_nonpersistent_facts(template_variables)

    role = RoleDefinition(variable_manager=template_variable_manager, loader=template_loader)
    role_dict = role.load(data={"role": "role_name"}, variable_manager=template_variable_manager, loader=template_loader)
    assert isinstance(role_dict, AnsibleMapping)
    assert role_dict.ansible_pos is None
    assert role_dict['role'] == 'test_role'

# Generated at 2022-06-13 08:50:36.171738
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    rd = RoleDefinition()
    data = {'role': 'name-of-role'}
    rd.preprocess_data(data)
    assert rd.get_name(include_role_fqcn=True) == 'name-of-role'
    assert rd.get_name(include_role_fqcn=False) == 'name-of-role'

# Generated at 2022-06-13 08:50:50.623493
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    test_data = {
        "name": "geerlingguy.ntp",
        "version": "3.0.0",
        "allow_duplicates": True,
        "when": "ansible_os_family == 'Debian'",
        "become": True,
        "become_user": "root"
    }
    variable_manager = None
    loader = None
    collection_list = None

    role_definition = RoleDefinition.load(test_data, variable_manager, loader)
    role_definition.preprocess_data(role_definition._ds)

    assert role_definition.get_name() == "geerlingguy.ntp"
    assert role_definition.become is True
    assert role_definition.when == "ansible_os_family == 'Debian'"
    assert role_definition

# Generated at 2022-06-13 08:51:03.847228
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import copy

    # A simple named role definition
    test1 = dict(
        role = "test_role"
    )

    # A simple named role definition with params
    test2 = dict(
        role = "test_role",
        vars = dict(
            x = "y"
        )
    )

    # A role definition referencing a role collection
    test3 = dict(
        role = "my.collection.test_role"
    )

    # A role definition referencing a role collection, with params
    test4 = dict(
        role = "my.collection.test_role",
        vars = dict(
            x = "y"
        )
    )

    # A role definition specifying a role path
    test5 = dict(
        role = "/path/to/test_role",
    )

    # A

# Generated at 2022-06-13 08:51:11.172307
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    rd = RoleDefinition()
    rd._role_collection = None
    rd.role = 'apache'
    assert rd.get_name() == 'apache'
    rd._role_collection = 'foo.bar'
    assert rd.get_name() == 'foo.bar.apache'
    assert rd.get_name(include_role_fqcn=False) == 'apache'
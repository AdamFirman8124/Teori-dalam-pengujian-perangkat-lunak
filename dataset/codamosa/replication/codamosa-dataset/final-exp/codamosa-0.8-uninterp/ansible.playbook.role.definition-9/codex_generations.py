

# Generated at 2022-06-13 08:41:54.486960
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    class TestRoleDefinition(RoleDefinition):
        _valid_attrs = dict(foo=Attribute(isa='string'))

    valid_role_def = dict(
        role='testrole',
        foo='bar',
    )
    rd = TestRoleDefinition.load(valid_role_def, '/tmp/ansible-test/baa')
    rd_obj = rd.preprocess_data(valid_role_def)
    assert rd_obj['role'] == 'testrole'
    assert rd_obj['foo'] == 'bar'

    invalid_role_def = dict(
        role='testrole',
        foo='bar',
        baz='qux',
    )


# Generated at 2022-06-13 08:42:07.174504
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    module = AnsibleModule(argument_spec={})
    loader = DataLoader()
    variable_manager = VariableManager()
    play = Play().load(dict(
        name="Ansible Play",
        hosts='all',
        gather_facts='no',
        roles=[dict(role='foo')]
    ), variable_manager=variable_manager, loader=loader)
    play._role_paths = ['roles']
    role_definition = play.roles[0]
    result = role_definition.preprocess_data(dict(role='foo'))
    assert result == dict(role='foo')
    assert role_definition._role_name == 'foo'
    assert role_definition._role_path == 'roles/foo'
    result = role_definition.preprocess_data(dict(role=dict(name='bar')))

# Generated at 2022-06-13 08:42:15.488682
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.plugins.loader import role_loader

    my_role = RoleDefinition()
    my_role.role = 'test_role'
    my_role._attributes['role'] = my_role.role

    # Test that preprocess_data raises an AnsibleAssertionError when given a string
    with pytest.raises(AnsibleAssertionError):
        my_role.preprocess_data('test_role')

    # Test that preprocess_data raises an AnsibleError when given a role with neither role: nor name:
    with pytest.raises(AnsibleError):
        my_role.preprocess_data({'fubar': 'test_role'})

    # Test that preprocess_data sets the role name when a role: name is given

# Generated at 2022-06-13 08:42:25.332398
# Unit test for method preprocess_data of class RoleDefinition

# Generated at 2022-06-13 08:42:30.574553
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    rd = RoleDefinition()
    ds = {
        'role': 'test_role',
        'test_key': 'test_value'
    }
    ds_processed = rd.preprocess_data(ds)
    assert ds_processed['role'] == 'test_role'
    assert ds_processed['test_key'] == 'test_value'
    assert ds_processed.get('name') is None

# Generated at 2022-06-13 08:42:43.897881
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    # setup dummy objects needed for properly initializing RoleDefinition
    dummy_play = type('Play', (object,), {})
    dummy_variable_manager = type('VariableManager', (object,), {})
    dummy_loader = type('DataLoader', (object,), {'path_exists': lambda path: True})
    dummy_collection_list = type('CollectionsFinder', (object,), {'get_collections': lambda: None})

    # input data set

# Generated at 2022-06-13 08:42:52.589454
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    from ansible.playbook.play import Play

    p = Play.load(dict(
        name="test",
        hosts='all',
        gather_facts='no',
        roles=dict(
            role='test'
        )
    ), variable_manager=None, loader=None)

    rd = p.get_roles()[0]

    assert rd.get_name() == 'test'
    assert rd.get_name(include_role_fqcn=False) == 'test'

    rd._role_collection = 'collection'

    assert rd.get_name() == 'collection.test'
    assert rd.get_name(include_role_fqcn=False) == 'test'

# Generated at 2022-06-13 08:43:06.398883
# Unit test for method get_name of class RoleDefinition

# Generated at 2022-06-13 08:43:16.095382
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    test1 = dict(
        role='docker',
        name='redis',
        image='redis:3.2',
    )

    test2 = dict(
        role='docker',
        image='redis:3.2',
        name=dict(x='y'),
    )

    try:
        RoleDefinition(play=None, role_basedir=None).preprocess_data(test1)
        RoleDefinition(play=None, role_basedir=None).preprocess_data(test2)
    except Exception as e:
        raise Exception("Unexcepted error: %s" % e)



# Generated at 2022-06-13 08:43:27.985980
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory import Inventory

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='localhost')

    # r1 is a role definition that can be preprocessed
    r1 = { 'role': 'some_role' }
    rp1 = RoleDefinition(play=None, role_basedir=None, variable_manager=variable_manager, loader=loader)
    rp1.preprocess_data(r1)

    # r2 is a role definition containing an unknown key

# Generated at 2022-06-13 08:43:46.720025
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    loader = None
    variable_manager = None
    display = Display()


# Generated at 2022-06-13 08:43:57.234790
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.utils.display import Display
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # setup
    display = Display()
    loader = DataLoader()
    variable_manager = VariableManager()
    play_context = PlayContext()
    play = Play.load({}, variable_manager, loader, display)

    add_all_plugin_dirs()
    role_def = RoleDefinition(play=play, variable_manager=variable_manager, loader=loader)
    role_def.post_validate(play_context, {}, False)

    # test

# Generated at 2022-06-13 08:44:12.017045
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Test for the case when ds is a string
    role_name = 'test'
    ds = 'test'
    test_instance = RoleDefinition(role_basedir='test/test/test')
    ret = test_instance.preprocess_data(ds)
    assert ret == {'role': role_name}
    assert test_instance._role_path == role_name

    # Test for the case when ds is a dictionary
    role_name = 'test1'
    ds = dict()
    ds['role'] = role_name
    test_instance = RoleDefinition(role_basedir='test/test/test')
    assert test_instance.preprocess_data(ds) == {'role': role_name}
    assert test_instance._role_path == role_name

# Generated at 2022-06-13 08:44:23.799852
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # test handling of role name as string without params
    r = RoleDefinition()
    ds = 'test_role'
    expected_ds = {'role': 'test_role'}
    assert r.preprocess_data(ds) == expected_ds
    # test handling of role name as string with params
    r = RoleDefinition()
    ds = {'role': 'test_role', 'params': {'foo': 'bar'}}
    expected_ds = {'role': 'test_role'}
    r.preprocess_data(ds)
    assert r._role_params == {'foo': 'bar'}
    assert r._ds == ds
    assert r._attribute_class_map == {}
    assert r._ds == ds
    assert r._attributes == {'role': 'test_role'}

# Generated at 2022-06-13 08:44:36.488313
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager

    role_name = 'test_role'
    collection_name = 'my_collection'
    fixture_root = os.path.join(os.path.dirname(__file__), 'fixtures')
    test_data_root = os.path.join(fixture_root, 'test_role_definition')
    role_path = os.path.join(test_data_root, 'roles', role_name)

    playbook = Playbook()
    playbook._basedir = test_data_root
    playbook._loader = playbook._loader = playbook._loader = playbook._

# Generated at 2022-06-13 08:44:48.495181
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.inventory.group import Group
    from ansible.parsing.yaml.objects import AnsibleSequence

    group = Group()
    group.name = 'mygroup'
    group.vars = dict(
        a=1,
    )
    group.hosts = dict(
        localhost=False,
    )

    fake_loader = object()

    ds1 = "foo"
    rd1 = RoleDefinition(group, fake_loader)
    new_ds = rd1.preprocess_data(ds1)
    assert ds1 == new_ds

    ds2 = AnsibleSequence()
    rd2 = RoleDefinition(group, fake_loader)
    new_ds = rd2.preprocess_data(ds2)
    assert ds2 == new_ds

    d

# Generated at 2022-06-13 08:44:59.163031
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    '''
    Test preprocess_data function of class RoleDefinition.

    This method converts a dictionary to an AnsibleMapping object, by calling
    the method preprocess_data of the super class Base.

    As it also changes role names as needed, this method needs to be tested.
    '''

    # 1) Test if a given strong is returned unchanged
    role_name = "test_role"
    ds = role_name
    role_definition = RoleDefinition()
    expected_result = ds
    result = role_definition.preprocess_data(ds)
    assert result == expected_result

    # 2) Test if a given dict is returned as a AnsibleMapping object
    ds = { "role": "test_role", "other_key": "other_value" }
    role_definition = RoleDefinition()
    expected_result

# Generated at 2022-06-13 08:45:07.300482
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    name, path = RoleDefinition._load_role_path('role.name')
    assert name == 'role.name'
    assert path == 'roles/role.name'

    variable_manager = VariableManager()
    play_context = PlayContext()
    templar = Templar(loader=None, variables=variable_manager.get_vars(play=None))

    role_def = {'role': role}
    role_def, role_params = RoleDefinition._split_role_params(role_def)
    assert role_def == {'role': role}
    assert role_params == {}

    role_def = {'role': role, 'param': templar.template('test_param')}
    role

# Generated at 2022-06-13 08:45:18.703730
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # test string role name, no params
    role = RoleDefinition()
    assert role.preprocess_data('testrole') == {'role': 'testrole'}

    # test dict role name and params
    role = RoleDefinition()
    assert role.preprocess_data({'role': 'testrole', 'one': 'two'}) == {'role': 'testrole'}

    # test integer role name, no params; should be converted to string
    role = RoleDefinition()
    assert role.preprocess_data(123) == {'role': '123'}

    # test list role name, no params; should raise error
    try:
        role = RoleDefinition()
        role.preprocess_data(['one', 'two'])
        assert False
    except AnsibleAssertionError:
        pass

    # test dict role name and

# Generated at 2022-06-13 08:45:23.204072
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_def = RoleDefinition()
    role_def._role_collection = "namespace.collection"
    role_def._role = "role_name"
    assert role_def.get_name() == "namespace.collection.role_name"
    assert role_def.get_name(False) == "role_name"

# Generated at 2022-06-13 08:45:46.961044
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_inventory(InventoryManager(loader=loader))

    # test role name as string
    data = 'foo'
    role = RoleDefinition(variable_manager=variable_manager, loader=loader)
    role.preprocess_data(data)
    assert role._role_path == os.path.join(os.path.expanduser('~'), '.ansible/roles/foo')

    # test role name and path are unchanged (as strings)
    data = 'foo.bar'
    role = RoleDefinition(variable_manager=variable_manager, loader=loader)
    role

# Generated at 2022-06-13 08:45:51.713236
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role_definition = RoleDefinition()
    data = {'role': 'test_role'}
    role_definition.preprocess_data(data)
    assert role_definition._role_params.__str__() == '{}'
    assert role_definition._role_path.__str__() == 'roles/test_role'

# Generated at 2022-06-13 08:46:05.082830
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    collection_loader = AnsibleCollectionLoader(loader)
    collection_paths = collection_loader.paths()
    role_name_to_check = 'geerlingguy.docker'
    role_path_to_check = '/home/mikail/.ansible/collections/ansible_collections/geerlingguy/docker/'

    # Create a PlayContext for the test
    play_context = PlayContext()
    play_context.network_os = 'ios'

    # Create a VariableManager for the test
    variable_manager = VariableManager

# Generated at 2022-06-13 08:46:17.356401
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import mock
    from ansible.utils.vars import combine_vars

    # Create some variables and set them in the variable manager
    local_vars = dict(foo="bar",
                      foo_dict=dict(hello="world"),
                      port_lookup=dict(http="80",
                                       https="443"))
    variable_manager = mock.Mock()
    variable_manager.get_vars.return_value = combine_vars(loader=None,
                                                          variables=local_vars)

    # Create a minimal RoleDefinition object
    role_def = RoleDefinition(variable_manager=variable_manager)

    # Test a basic dict with a string in a dict with key 'role':
    ds = dict(role=dict(name="helloworld"))
    role_def.preprocess_data(ds)
   

# Generated at 2022-06-13 08:46:29.977726
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.module_utils.six import BytesIO
    from ansible.parsing.yaml.loader import AnsibleLoader as YamlLoader
    from ansible.parsing.vault import VaultLib

    data = """---
role:
- { role: common, when: inventory_hostname == 'localhost' }
- { role: another_common }
- { role: vmware_guest, vcenter_hostname: vc.example.org}
- bad_syntax
"""

    role_defs = []
    for role in YamlLoader(BytesIO(data)).get_single_data():
        # Initialize required arguments
        role_basedir = '/etc/ansible/roles'
        role_def = RoleDefinition(None, role_basedir, None, None)
        role_def.post_valid

# Generated at 2022-06-13 08:46:41.887945
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    data = dict(
        role = 'foo',
        my_var = 'bar'
    )
    rd = RoleDefinition()
    new_data = rd.preprocess_data(data)
    assert new_data == {'role': 'foo'}
    assert rd.get_role_params() == {'my_var': 'bar'}
    assert rd.get_name() == 'foo'

    data = 'foo'
    rd = RoleDefinition()
    new_data = rd.preprocess_data(data)
    assert new_data == {'role': 'foo'}
    assert rd.get_role_params() == {}
    assert rd.get_name() == 'foo'

    data = 'my_role'
    rd = RoleDefinition()
    new_data = rd

# Generated at 2022-06-13 08:46:55.713583
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils._text import to_bytes
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar

    role_def = u'web_server'
    role_def_path = u'../roles/web_server'
    role_def_dict = u"{role: 'web_server', connection:'fake', become:true, become_method:'sudo', become_user:'root'}"
    role_def_dict_path = u"{role: '../roles/web_server', connection:'fake', become:true, become_method:'sudo', become_user:'root'}"


# Generated at 2022-06-13 08:47:03.855146
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    class AnsibleCollectionRefFake(object):
        def __init__(self, collection_name):
            self.collection_name = collection_name

        def __str__(self):
            return self.collection_name

        def __repr__(self):
            return self.collection_name

        @staticmethod
        def is_valid_fqcr(fqcr):
            return True

    # mocking all we can for this test
    class FakeAnsibleLoad(object):
        def __init__(self, d, vm = None, l = None, cl = None):
            self._ds = d['data']
            self._role_path = d['role_path']
            self._role_collection = d['collection_name'] if 'collection_name' in d else None
            self._role_params = dict()


# Generated at 2022-06-13 08:47:14.433770
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    ds = {
        'role': 'foobar',
        'users': ['bob', 'alice'],
        'foobar': True
    }

    rd = RoleDefinition()
    rd.preprocess_data(ds)

    # attrs is a dictionary, so no order is guaranteed
    # Lets manually check, if the relevant data is there
    assert 'role' in rd._attrs, 'The role attribute is missing'
    assert rd._attrs['role'] == 'foobar', 'The role attribute has the wrong value: %s' % rd._attrs['role']
    assert 'users' in rd._attrs, 'The users attribute is missing'
    assert rd._attrs['users'] == ['bob', 'alice'], 'The users attribute has the wrong value: %s' % rd._

# Generated at 2022-06-13 08:47:25.662681
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inv_manager)
    play_context = PlayContext()
    c = PlayContext()
    c._vars_files = list()
    c._vars_files.append("/path/to/main.yml")
    c._vars_files.append("/path/to/group_vars/group_1.yml")
    c._vars_

# Generated at 2022-06-13 08:47:48.495078
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    display.verbosity = 4

    from ansible.playbook.play import Play
    from ansible.playbook import Playbook
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    templar = Templar(loader=loader)
    playbooks = [ Playbook.load('./test/units/modules/test_role_definition/data/preprocess_data.yml', loader=loader, variable_manager=VariableManager()) ]
    result = []
    for playbook in playbooks:
      plays = [ Play.load(playbook, variable_manager=VariableManager(), loader=loader) ]
      for play in plays:
          roles_definitions = play._entries[0]

# Generated at 2022-06-13 08:48:01.945853
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    loader = AnsibleLoader(dict(), None)

    role_name = 'some_role'
    role_def = dict(role=role_name)

    role_def_instance = RoleDefinition.load(role_def, loader=loader)
    assert(role_def_instance._role_path == 'roles/' + role_name)

    # Test that preprocess_data returns the original dict when it's a string
    assert(role_def_instance.preprocess_data(role_name) == dict(role=role_name))

    # Test that preprocess_data raises error when the role definition is not
    # a dict or a string

# Generated at 2022-06-13 08:48:09.440306
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    class FakeLoader(object):
        def __init__(self):
            self.basedir = 'fake_dir'
            self.paths = ['fake_dir']

        def get_basedir(self):
            return self.basedir

        def path_exists(self, path_file):
            if path_file in self.paths:
                return True
            return False

    class FakeVM(object):
        def __init__(self, vars):
            self._vars = vars

        def get_vars(self, play=None):
            return self._vars

    # test role with role name containing variable
    ds = {'role': '{{ role_name }}'}
    variable_manager = FakeVM(vars={'role_name': 'role_0'})
    role_definition = RoleDefinition

# Generated at 2022-06-13 08:48:23.012339
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    play_context = PlayContext()
    variable_manager = None
    role_name = 'foo'
    role_path = '/path/to/foo'

    # first test, simple string
    role_def = RoleDefinition(variable_manager=variable_manager, loader=loader)
    role_ds = role_def.preprocess_data(role_name)
    assert(isinstance(role_ds, AnsibleMapping))
    assert(role_ds.get('role') == role_name)
    assert(role_def._role_params == dict())
    assert(role_def._role_path == '/path/to/foo')

    # now with a dict
   

# Generated at 2022-06-13 08:48:33.755785
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    import sys
    import os
    import collections
    import unittest
    import mocking


    mock_basic_conf = collections.namedtuple("mock_basic_conf", ["DEFAULT_ROLES_PATH"])
    mock_basic_conf.DEFAULT_ROLES_PATH = ['~/.ansible/roles/', '/etc/ansible/roles']

    role_name = 'roleName'
    role_path = os.path.join('role_basedir', role_name)

    fake_playbook_path = os.path.join('playbook_basedir', 'playbook.yml')
    fake_role_path = os.path.join(os.path.expanduser('~/.ansible/roles'), 'roleName')

# Generated at 2022-06-13 08:48:47.227292
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader

    display = Display()
    context = PlayContext()
    loader = DataLoader()
    role = RoleDefinition(play=None, role_basedir=None, loader=loader, variable_manager=None)

    # Test case 1: role: example
    data = dict(role='example')
    new_ds = role.preprocess_data(data)
    assert 'role' in new_ds
    assert new_ds['role'] == 'example'

    # Test case 2: role: example:vars
    data = dict(role='example:vars')
    new_ds = role.preprocess_data(data)
    assert 'role' in new_ds

# Generated at 2022-06-13 08:48:53.108294
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    role_def_data = AnsibleMapping()
    role_def_data.ansible_pos = 'dummy'
    role_def_data['role'] = 'test_role'
    role_def_data['test_key'] = 'test_value'

    role_def = RoleDefinition()
    assert role_def._split_role_params(role_def_data) == (dict(role='test_role'), dict(test_key='test_value'))
    assert role_def.preprocess_data(role_def_data) == dict(role='test_role')

# Generated at 2022-06-13 08:48:57.720007
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    role_definition = RoleDefinition()
    role_definition.role = 'test_role'

    # when calling get_name with include_role_fqcn=True, we expect the role name to
    # be prefixed with the role collection
    assert role_definition.get_name() == 'test_role'

    # when passing False, the role name should be returned without the role collection
    assert role_definition.get_name(False) == 'test_role'

# Generated at 2022-06-13 08:49:08.810226
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    # Test that preprocess_data raises an error when a role definition is an int
    rd_1 = RoleDefinition()
    ds_1 = 5
    try:
        rd_1.preprocess_data(ds_1)
    except AnsibleAssertionError:
        pass
    else:
        raise AssertionError("AnsibleAssertionError was not raised")

    # Test that preprocess_data raises an error when a role definition is a list
    rd_2 = RoleDefinition()
    ds_2 = [ "list" ]
    try:
        rd_2.preprocess_data(ds_2)
    except AnsibleAssertionError:
        pass
    else:
        raise AssertionError("AnsibleAssertionError was not raised")

    # Test that preprocess_data raises

# Generated at 2022-06-13 08:49:16.374482
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    v = VariableManager()
    l = DataLoader()
    i = InventoryManager(loader=l, sources=['tests/ansible-test/basic'])
    p = Play().load({'name': 'test',
                     'hosts': 'all',
                     'roles': [{'role': 'i_am_a_role'}]},
                    variable_manager=v,
                    loader=l)

    r = p.roles[0]
    # Data structure is correct
    assert isinstance(r,RoleDefinition)
    # name and path are correct

# Generated at 2022-06-13 08:49:30.849281
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    data = {
        'role': 'test',
        'foo': 'bar'
    }

    role_definition = RoleDefinition()
    role_definition.preprocess_data(data)
    assert role_definition._role_params['foo'] == 'bar'

# Generated at 2022-06-13 08:49:37.584070
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    variable_manager = VariableManager()
    loader = DataLoader()
    role_basedir = ['/b', 'c']

    rd = RoleDefinition()

    # Case 1
    try:
        rd.preprocess_data(4)
    except AnsibleError as e:
        assert "role definitions must contain a role name" in to_text(e)

    # Case 2
    try:
        rd.preprocess_data("test_role")
    except AnsibleError as e:
        assert "role definitions must contain a role name" in to_text(e)

    # Case 3

# Generated at 2022-06-13 08:49:49.941322
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.task.include import TaskInclude
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.utils.collection_loader._collection_finder import _get_collection_role_path

    # test role names with a simple string
    role_def = RoleDefinition()
    role_name = role_def.preprocess_data("role_name")
    assert role_name['role'] == "role_name"

    # test role names with a simple string, but with a var
    role_def = RoleDefinition(path_name = "role_name")
    all_vars = dict(path_name = "role_name_var")
    role_var_name = role_def.preprocess_data("{{ path_name }}")

# Generated at 2022-06-13 08:50:00.611522
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Setup test environment
    display.verbosity = 2
    yaml_data = {
        'role': 'some.collection.role'
    }

    role_definition = RoleDefinition()

    # Execute preprocess_data() with Exception
    role_definition.preprocess_data(yaml_data)

    assert role_definition is not None

    # Execute preprocess_data() with Exception
    yaml_data['role'] = ''
    try:
        role_definition.preprocess_data(yaml_data)
    except AnsibleError:
        pass

    # Execute preprocess_data() with empty role (string)
    role_definition.preprocess_data('')
    assert role_definition._role_path is None
    assert role_definition._role_params == dict()

    # Setup test environment with role and variable

# Generated at 2022-06-13 08:50:12.152386
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():

    from ansible.playbook.role.include import RoleInclude
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    def _role_dummy_data():
        data = {
            'role': 'test',
            'x': 'y',
            'z': 'a',
        }
        return data

    def _check_role_data(data):
        assert isinstance(data, AnsibleMapping)
        assert len(data) == 4
        assert 'role' in data
        assert 'x' in data
        assert 'z' in data
        assert 'tags' in data
        assert not data['tags']

    role_include = RoleInclude()
    variable_manager = VariableManager()
    loader = DataLoader()

    # test preprocess_

# Generated at 2022-06-13 08:50:19.522502
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.playbook.play import Play

    ds = dict(  role='common',
                src='http://foo.com/myapp.git',
                version='v1')

    new_ds = AnsibleMapping(  role='common',
                              src='http://foo.com/myapp.git',
                              version='v1')

    variable_manager = None
    loader = None

    rd = RoleDefinition(play=Play(), variable_manager=variable_manager, loader=loader)

    rd.preprocess_data(ds)

    assert rd._ds == ds
    assert rd._role_params == dict()
    assert rd._role_path == 'common'

    ds = 134
    new_ds = 134


# Generated at 2022-06-13 08:50:31.224513
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Source: https://gist.github.com/bennylope/2999704

    # This is a nested dict which represents the content of a sample
    # roles/web.yml file. The content is as follows:
    #
    """
    - name: Sample web role
      author: John Doe
      min_ansible_version: 2.0
      galaxy_info:
        author: John Doe
        description: A sample role to show role dependencies
      dependencies:
      - { role: common }
      - { role: database, when: ansible_os_family == 'Debian' }
    """

# Generated at 2022-06-13 08:50:41.880728
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    display = Display()
    #load options
    options = FakeOpts()
    loader = DataLoader()
    variable_manager = VariableManager()

    #load role definition
    role_ds = 'test_role'
    role_basedir = os.path.join(C.DEFAULT_ROLES_PATH[0], role_ds)
    role = RoleDefinition(role_basedir=role_basedir, variable_manager=variable_manager, loader=loader)

    #check preprocess data success
    display.display('Test RoleDefinition load success')
    assert role.preprocess_data(role_ds) == 'test_role'
    assert role._role_path == role_basedir

    #check preprocess

# Generated at 2022-06-13 08:50:51.476036
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():

    # Ensures the function returns None for any object other than RoleDefinition
    assert RoleDefinition.get_name(1) is None
    assert RoleDefinition.get_name('x') is None
    assert RoleDefinition.get_name([]) is None
    assert RoleDefinition.get_name({}) is None
    assert RoleDefinition.get_name([1]) is None
    assert RoleDefinition.get_name([None]) is None

    role_def = RoleDefinition()

    # Ensures the function returns None when the RoleDefinition object has no _role_collection
    assert role_def.get_name() is None

    # Ensures the function returns just the role name when include_role_fqcn is False
    role_def._role_collection = 'namespace.collection'
    role_def.role = 'role_name'
    assert role_def.get_

# Generated at 2022-06-13 08:51:04.467729
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader, inventory, variable_manager = (None, None, None)

    variable_manager = VariableManager(loader=loader, inventory=inventory)
    variable_manager._extra_vars = dict(
        role_name='test_role',
        role_path='test_collections/my_collection/roles/test_role'
    )

    data = dict(role='{{ role_name }}',
                name='{{ role_path }}',
                port=1234)

    role_def = RoleDefinition(play=None, role_basedir=None, variable_manager=variable_manager, loader=None)
    role_def.preprocess_data(data)


# Generated at 2022-06-13 08:51:23.109503
# Unit test for method get_name of class RoleDefinition
def test_RoleDefinition_get_name():
    name = "test.collection.role_name"

    # name is valid collection-relative name
    display.warning(name)
    rd = RoleDefinition()
    rd.role = name
    assert rd.get_name() == name
    assert rd.get_name(include_role_fqcn=False) == 'role_name'

    # name is invalid collection-relative name
    display.warning("role_name")
    rd = RoleDefinition()
    rd.role = "role_name"
    assert rd.get_name() == "role_name"

    # name is fqcn
    display.warning("collections.test_name.role_name")
    rd = RoleDefinition()
    rd.role = "collections.test_name.role_name"
    assert rd.get

# Generated at 2022-06-13 08:51:37.729536
# Unit test for method preprocess_data of class RoleDefinition
def test_RoleDefinition_preprocess_data():
    # Tests for loading of the role name

    # Test: valid value of dictionary variable
    # Expected: "name"
    ds1 = dict(name="name")
    role_def1 = RoleDefinition()
    role_def1.preprocess_data(ds1)
    assert role_def1._ds == ds1
    assert role_def1._attributes["role"] == "name"

    # Test: valid value of string variable
    # Expected: "name"
    ds2 = "name"
    role_def2 = RoleDefinition()
    role_def2.preprocess_data(ds2)
    assert role_def2._ds == ds2
    assert role_def2._attributes["role"] == "name"

    # Test: no "name" key in the dictionary
    # Expected: exception

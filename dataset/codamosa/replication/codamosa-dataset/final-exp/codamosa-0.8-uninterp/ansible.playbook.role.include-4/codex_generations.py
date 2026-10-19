

# Generated at 2022-06-13 08:52:18.095340
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook import Play
    from ansible.plugins.loader import find_plugin
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,',])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_source = dict(
        name="Ansible Play",
        hosts='localhost',
        gather_facts='no',
        roles=[
            dict(
                role='test',
                tasks=list()
            )
        ]
    )

# Generated at 2022-06-13 08:52:23.354646
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = dict(
        name='myRole',
        tasks=[
            dict(action=dict(module='debug', args=dict(msg='{{bar}}')))
        ]
    )

    role_include = RoleInclude.load(data, None)
    assert data['name'] == role_include._role_name

# Generated at 2022-06-13 08:52:25.154898
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    raise NotImplementedError("TODO: write this test")

# Generated at 2022-06-13 08:52:36.139253
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play import Play
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.template import Templar
    from ansible.variable_manager import VariableManager
    from ansible.utils.vars import combine_vars

    data = {u'name': u'Common',
            u'hosts': u'localhost,host2',
            u'roles': [u'Role1',
                       {u'role': u'Role2', u'become': u'yes', u'become_user': u'admin'}]
            }

    variable_manager = VariableManager()


# Generated at 2022-06-13 08:52:46.868982
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop


    class AnsibleOptions(object):
        def __init__(self, verbose=False):
            self.verbose = verbose

    class AnsibleContext(object):
        def __init__(self, loader, variables):
            self._loader = loader
            self._variables = variables
            self.CLIARGS = AnsibleOptions()

    class AnsibleRunner(object):
        def __init__(self, variable_manager, loader):
            self._variable_manager = variable_manager
            self._loader = loader
            self._context = AnsibleContext(loader, variable_manager)

    from ansible.playbook.play import Play

# Generated at 2022-06-13 08:52:53.759127
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    import ansible.plugins.loader
    # Test with string data
    data = "name"
    play = ansible.plugins.loader.load_plugin('localhost', 'play')
    current_role_path = "."
    variable_manager = ansible.plugins.loader.load_plugin('localhost', 'variable_manager')
    loader = ansible.plugins.loader.load_plugin('localhost', 'loader')
    assert RoleInclude.load(data, play, current_role_path, variable_manager, loader).name == "name"
    # Test with dict data
    data = {}
    assert not RoleInclude.load(data, play, current_role_path, variable_manager, loader)
    assert RoleInclude.load(data, play, current_role_path, variable_manager, loader)._attributes == {}
    # Test with

# Generated at 2022-06-13 08:53:04.333202
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """
    Unit test for method load of class RoleInclude
    """

    # No data to load
    try:
        RoleInclude.load(None, None, None, None, None, None)
        assert False
    except AnsibleParserError as e:
        assert str(e) == "Invalid role definition: None"

    # Data to load is not a string or a dictionary
    try:
        RoleInclude.load(5, None, None, None, None, None)
        assert False
    except AnsibleParserError as e:
        assert str(e) == "Invalid role definition: 5"

    # Data to load is an old style role (with a comma)

# Generated at 2022-06-13 08:53:13.549099
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import ROLE_CACHE
    play = Play().load({
        'name': 'test',
        'hosts': 'all',
        'roles': [
            {
                'test': {
                    'tasks': [
                        {'debug': 'msg={{x}}'},
                    ]
                }
            },
            {
                'test': {
                    'vars': {'x': 'value'}
                }
            }
        ]
    }, variable_manager={})
    assert len(play.roles) == 2
    assert isinstance(play.roles[0], RoleInclude)
    assert isinstance(play.roles[1], RoleInclude)

# Generated at 2022-06-13 08:53:22.535838
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    def load_data(self, data, variable_manager=None, loader=None, play=None):
        return True

    RoleInclude.load_data = load_data
    assert RoleInclude.load(None, None)

    def load_data(self, data, variable_manager=None, loader=None, play=None):
        raise AnsibleParserError("Invalid role definition: %s")

    RoleInclude.load_data = load_data
    try:
        RoleInclude.load(None, None)
    except Exception as err:
        assert err.args[0] == "Invalid role definition: %s"

    def load_data(self, data, variable_manager=None, loader=None, play=None):
        raise AnsibleError("Invalid old style role requirement: %s")


# Generated at 2022-06-13 08:53:34.873902
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    # Pass in a very valid role with multiple metadata.yaml content in
    # variable_manager.  This will be overridden with the _load_role_data
    # method in this code.
    variable_manager = mock.Mock()
    variable_manager.get_vars.return_value = {
        'ansible_collections': {'collection1': {'version': '0.0.1'},
                                'collection2': {'version': '0.0.1.dev0'},
                                'collection3': {'version': '0.1.0'}}}

# Generated at 2022-06-13 08:53:47.780547
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    # create a mock ClassLoader to use while running the test
    class Loader():
        def load_from_file(self, filename, as_name=None, cache=True):
            if filename == 'hello.py':
                return 'hello'
            return None

    loader = Loader()

    # create a mock VariableManager to use while running the test
    class VariableManager():
        def __init__(self):
            self.options = {}

        def extra_vars(self):
            return self.options

    variable_manager = VariableManager()

    # create a mock Play to use while running the test
    class Play():
        def __init__(self):
            self.variable_manager = variable_manager
            self.loader = loader
            self.options = variable_manager

        def get_variable_manager(self):
            return variable

# Generated at 2022-06-13 08:53:58.459974
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    loader_args = {
        '_ansible_selective_tags': ['selective_tag'],
        '_ansible_skip_tags': ['skip_tag'],
        '_ansible_verbosity': 4,
        '_ansible_version': '2.5.5',
    }

    # Testing with a string
    data = "role_name"
    variable_manager = None
    loader = None
    current_role_path = "."
    play = None
    parent_role = None

    ri = RoleInclude.load(data, play=play, current_role_path=current_role_path, parent_role=parent_role,
                          variable_manager=variable_manager, loader=loader)
    assert ri.get_name() == data


    # Testing with a dict

# Generated at 2022-06-13 08:54:03.592727
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    test_play = Play()
    test_parent_role = Role()
    test_parent_role._role_path = 'test_parent_role._role_path'
    test_role_include = RoleInclude.load('test string', test_play, test_parent_role._role_path, test_parent_role)
    assert isinstance(test_role_include, RoleInclude)
    assert test_role_include._role_name == 'test string'

# Generated at 2022-06-13 08:54:11.202697
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Test with a list
    data = [{"role": "common"}]
    assert RoleInclude.load(data, "play") is not None
    assert RoleInclude.load(data, "play") == [{'role': 'common'}]
    # Test with a string
    data2 = "common"
    assert RoleInclude.load(data2, "play") is not None
    assert RoleInclude.load(data2, "play") == ['common']
    # Test with a nested list
    data3 = [{"role": "common"}, {"role": "database"}]
    assert RoleInclude.load(data3, "play") is not None
    assert RoleInclude.load(data3, "play") == [{'role': 'common'}, {'role': 'database'}]

# Generated at 2022-06-13 08:54:12.814206
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # pylint: disable=no-value-for-parameter
    pass

# Generated at 2022-06-13 08:54:24.111441
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    # TODO: This is broken because it calls RoleInclude with None for the
    # loader argument, which causes the call to RoleInclude.load_data()
    # to fail because play isn't passed as an argument. But it's not clear
    # why play isn't passed when this method is called (it's mocked out in
    # the test fixture, but it's not clear why it's mocked out).
    assert False

    # This method is copied from test_RoleInclude_load() in
    # lib/ansible/playbook/tests/unit/test_role.py.

    # Create a mock loader
    class MockLoader:
        paths = ['/tmp']

    # Create a mock variable manager
    class MockVariableManager:
        def __init__(self):
            self.vars_cache = {}

# Generated at 2022-06-13 08:54:24.744775
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    pass

# Generated at 2022-06-13 08:54:35.484551
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Load a valid role include
    role_include = RoleInclude.load("role_include", "play", "current_role_path")
    assert isinstance(role_include, RoleInclude)
    assert role_include.get_name() == "role_include"
    assert role_include.get_role_path() == "current_role_path"

    # Load an invalid role include
    loaded_role_include = None
    try:
        RoleInclude.load(None, "play", "current_role_path")
    except AnsibleParserError as e:
        assert str(e) == "Invalid role definition: None"
    except Exception as e:
        assert False

    # Load an invalid role include
    loaded_role_include = None

# Generated at 2022-06-13 08:54:47.540858
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Test RoleInclude.load with a string for data
    rii = RoleInclude.load(data='foo', play='bar', current_role_path=None, parent_role=None, variable_manager=None, loader=None)

    assert isinstance(rii, RoleInclude)
    assert rii._role_name == 'foo'

    # Test RoleInclude.load with a dict for data

# Generated at 2022-06-13 08:54:50.503332
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude('play_1', 'current_role_path', 'variable_manager', 'loader', 'collection_list')
    ri.load_data('data', 'variable_manager', 'loader')
    assert ri


# Generated at 2022-06-13 08:55:00.475046
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook import Play
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils.common.collections import ImmutableDict

    variable_manager = VariableManager()
    loader = DataLoader()
    inv_manager = InventoryManager(loader=loader, sources=[])

# Generated at 2022-06-13 08:55:02.417972
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    """ role_include.py - test case to test load method of class RoleInclude """
    pass

# Generated at 2022-06-13 08:55:08.432028
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    data = "some-role-name"
    play = None
    current_role_path = None
    parent_role = None
    variable_manager = object()
    loader = object()
    collection_list = object()
    ri = RoleInclude.load(data, play, current_role_path, parent_role, variable_manager, loader, collection_list)
    assert isinstance(ri, RoleInclude)

# Generated at 2022-06-13 08:55:17.881583
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader

    ri = RoleInclude()

    ri.load('role1', play=Play())
    ri.load({'role': 'role1'}, play=Play())

    bad_role_definitions = [False, 'no_role', '']

    for bad_role_definition in bad_role_definitions:
        try:
            ri.load(bad_role_definition, play=Play())
        except AnsibleParserError:
            pass
        else:
            assert False

    loader = DataLoader()
    ri.load('role1', play=Play(), variable_manager=None, loader=loader)

# Generated at 2022-06-13 08:55:28.849975
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import plugin_loader
    from ansible.variable_manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    def test_role(loader, inventory, variable_manager, datadir, role_name='test_role'):
        p = Play().load({}, loader=loader, variable_manager=variable_manager)
        context = PlayContext()
        p._set_loader(loader)
        p._set_inventory(inventory)
        p._set_variable_manager(variable_manager)

# Generated at 2022-06-13 08:55:37.932761
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # Test load with str
    ri = RoleInclude()
    ri.load_data("test data")
    assert ri.get_name() == 'test data'

    # Test load with dict
    ri = RoleInclude()
    ri.load_data({'name': 'test_data'})
    assert ri.get_name() == 'test_data'
    assert ri.get_role_path() is None

    # Test load with AnsibleBaseYAMLObject
    ri = RoleInclude()
    ri.load_data(AnsibleBaseYAMLObject('test data'))
    assert ri.get_name() == 'test data'


# Generated at 2022-06-13 08:55:44.691784
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    # test with string 
    role_name = 'RoleA'
    role_include = RoleInclude._load(role_name, play=None)
    assert role_include._role_name == role_name
    assert isinstance(role_include, RoleRequirement)
    # test with dict
    role_name = 'RoleA'
    role_extra_var = {'var1':'abc'}
    role_include = RoleInclude._load({'role':role_name, 'var':role_extra_var}, play=None)
    assert role_include._role_name == role_name
    assert role_include._role_vars['var1'] == role_extra_var['var1']
    assert isinstance(role_include, RoleRequirement)
    # test with unknown object

# Generated at 2022-06-13 08:55:56.264241
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import filter_loader
    import ansible.constants as C
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    import json
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader

    filter_loader.add_directory(C.FILTER_PLUGINS)
    loader = DataLoader()
    inv = InventoryManager(loader, sources=C.DEFAULT_HOST_LIST)
    if C.DEFAULT_HOST_LIST:
        inv.load_sources()
    variable_manager = VariableManager(loader=loader, inventory=inv)
    play_context = PlayContext()
    all_v

# Generated at 2022-06-13 08:56:11.759723
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():

    #TODO: Make a proper unittest

    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager.set_inventory(inventory)

    play_context = PlayContext()
    playbook_path = '/tmp/ansible/test/'

    role_path = playbook_path + "/roles/somewhere"


# Generated at 2022-06-13 08:56:13.962012
# Unit test for method load of class RoleInclude
def test_RoleInclude_load():
    ri = RoleInclude()

#---------------------------------------------------------------------------------------
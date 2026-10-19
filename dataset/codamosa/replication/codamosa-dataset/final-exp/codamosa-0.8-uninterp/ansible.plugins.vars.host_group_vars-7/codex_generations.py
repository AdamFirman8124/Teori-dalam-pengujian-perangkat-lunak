

# Generated at 2022-06-13 15:17:43.621024
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible import inventory
    import os

    # create a Host/Group instance and then pass them to VarsModule class to test
    h = Host('www.example.com')
    g = Group('foo')
    fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'host_group_vars')
    inv = inventory.InventoryManager(loader=None, sources=fixture_path)
    vm = VarsModule(inventory=inv)
    # get_vars for Host
    var = vm.get_vars(loader=inv.loader, path=fixture_path, entities=h)
    assert var == {'var1': '1', 'var2': '2'}
    # get_vars for Group

# Generated at 2022-06-13 15:17:52.832315
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    # Create context for testing
    context = PlayContext()
    context._basedir = os.getcwd()
    context.vars_plugins = VarsModule()
    context.vars_plugins.loaders = DataLoader()
    context.vars_plugins.set_options()
    context.vars_plugins.set_context(context)
    context.vars_plugins.set_loader(context.vars_plugins.loaders)
    context.vars_plugins.basedir = context._basedir

    # Create VariableManager for testing
    variable_manager = VariableManager()
    variable_manager._fact_cache = dict()
    variable_

# Generated at 2022-06-13 15:18:02.153918
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import ansible.plugins.loader
    
    # Test with Host entity
    my_host = Host('test_host')
    my_host.name = 'test_host'
    my_host.port = 22
    my_host.vars = dict()
    my_host.aliases = list()
    my_host.groups = list()
    
    var_files = ['/etc/ansible/host_vars/test_host.yml']
    ansible.plugins.loader.CACHE = dict()
    ansible.plugins.loader.CACHE['/etc/ansible/host_vars/test_host.yml'] = dict()
    ansible.plugins.loader.CACHE['/etc/ansible/host_vars/test_host.yml']['data'] = dict()
   

# Generated at 2022-06-13 15:18:08.876690
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    # Create instance of class VarsModule.
    v = VarsModule()

    # Mock class Host and create instance of class Host.
    h = Host()
    h.name = "hostname"

    # Mock class Group and create instance of class Group.
    g = Group()
    g.name = "groupname"

    # Mock class BaseVarsPlugin and create instance of class BaseVarsPlugin.
    b = BaseVarsPlugin()

    # Prepare parameters for method get_vars of class VarsModule.
    path = "/path/to/directory"
    loader = "loader"
    cache = True
    # Execute method get_vars of class VarsModule.
    v.get_vars(loader, path, h, cache)
    v.get_vars(loader, path, g, cache)

# Generated at 2022-06-13 15:18:18.036656
# Unit test for method get_vars of class VarsModule

# Generated at 2022-06-13 15:18:29.277320
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import os
    import tempfile
    import shutil
    import json

    # Create temporary directory
    tmpdir = tempfile.mkdtemp()
    os.mkdir(tmpdir+"/group_vars")
    os.mkdir(tmpdir+"/host_vars")
    os.mkdir(tmpdir+"/other_vars")
    os.mkdir(tmpdir+"/group_vars/all")
    os.mkdir(tmpdir+"/host_vars/all")
    os.mkdir(tmpdir+"/other_vars/all")
    os.mkdir(tmpdir+"/group_vars/group")
    os.mkdir(tmpdir+"/host_vars/host")

# Generated at 2022-06-13 15:18:37.087828
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import sys
    import re
    test_VarsModule_get_vars.__self__.assertIsInstance(_VarsModule__get_vars(), re._pattern_type)
    test_VarsModule_get_vars.__self__.assertIsInstance(VarsModule(), AnsibleParserError)
    test_VarsModule_get_vars.__self__.assertIsInstance(_VarsModule__get_vars(), Host)
    test_VarsModule_get_vars.__self__.assertIsInstance(VarsModule(), Group)

# Generated at 2022-06-13 15:18:47.030084
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # Test with a valid input
    def _get_entity(name):
        class _entity:
            name = name
            def __str__(self):
                return name
        return _entity()

    class _loader:
        def find_vars_files(self, path, name):
            if name == 'foo':
                return ['/path/to/file']
            elif name == 'bar':
                return None
            else:
                return []

        def load_from_file(self, filepath, cache=True, unsafe=True):
            if filepath == '/path/to/file':
                return {'dict_key': 'dict_value'}
            else:
                return {}

    entities = [_get_entity('foo'), _get_entity('bar')]

# Generated at 2022-06-13 15:18:52.185181
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    # We need to make sure the path is a valid unicode string, otherwise it will
    # cause a UnicodeDecodeError if we try to create a VarsModule instance
    # with it later.
    basedir = to_text(C.DEFAULT_LOCAL_TMP)

    basedir_path = os.path.join(basedir, b'plugins/inventory/host_group_vars')
    os.makedirs(basedir_path)

    host_vars_test_file_path = os.path.join(basedir_path, b'host_vars/test')
    with open(host_vars_test_file_path, 'w') as host_vars_test_file:
        host_vars_test_file.write('v1: 1')

    group_vars_test_file_path

# Generated at 2022-06-13 15:18:59.250289
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.plugins.loader import vars_loader
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars import combine_vars

    group = Group("test_group")
    host = Host("test_host")

    test_vars = {
        "foo": "bar",
        "yo": "yo"
    }

    test_host_vars = {
        "foo": "foo",
        "yo": "yo"
    }

    test_group_vars = {
        "foo": "bar bar bar",
        "yo": "yo",
        "baz": "foo"
    }

    class TestVarsModule(VarsModule):
        def __init__(self):
            self.vars = None


# Generated at 2022-06-13 15:19:12.645208
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    # Create variations of vars files 
    with open('./host_vars/test_group/test', 'w') as f:
        f.write("hello : 'world'")
    with open('./host_vars/test_group/test.yaml', 'w') as f:
        f.write("hello : 'world'")
    with open('./host_vars/test_group/test.yml', 'w') as f:
        f.write("hello : 'world'")
    with open('./host_vars/test_group/test.json', 'w') as f:
        f.write('{"hello": "world"}')

    # Create variations of inv files 

# Generated at 2022-06-13 15:19:22.279690
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.plugins.loader import vars_loader

    # class host, group has no get_vars method, but vars_loader.get_vars() needs host, group
    class Host:
        def __init__(self, name):
            self.name = name

    class Group:
        def __init__(self, name):
            self.name = name

    class Loader:
        def __init__(self):
            self.paths = ['test/data/host_group_vars']

        # This fake method just returns the path as found_files
        def find_vars_files(self, path, name):
            return [path]

        # load_from_file returns data in the path

# Generated at 2022-06-13 15:19:29.427701
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import sys
    import os
    import yaml
    from ansible.plugins.loader import vars_loader
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.dumper import AnsibleDumper
    path = "PATH"
    hostname = 'localhost'
    the_vars = {'Foo': 'Bar'}
    fake_entities = [Host(hostname), Group(name=path)]
    # Setup inventory and loader
    inventory = InventoryManager(loader=vars_loader, sources=path)

# Generated at 2022-06-13 15:19:38.532417
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import os
    import tempfile
    from ansible.vars.manager import VariableManager
    from ansible.parsing.model import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.display import Display

    basedir = tempfile.mkdtemp(prefix='ansible_host_group_vars')
    groups_dir = os.path.join(basedir, 'group_vars')
    hosts_dir = os.path.join(basedir, 'host_vars')
    os.makedirs(groups_dir)
    os.makedirs(hosts_dir)

    localhost = os.path.join(hosts_dir, 'localhost')

# Generated at 2022-06-13 15:19:42.156157
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    ''' test get_vars method of class VarsModule '''
    loader = AnsibleLoader(None)
    path = '/hosts_test08/host_vars'
    entity = ['host_name']
    data = VarsModule().get_vars(loader, path, entity)
    assert data == {'var': 'host_var'}


# Generated at 2022-06-13 15:19:54.310749
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    vm = VarsModule()

    class TestInventory:
        name='TestInventory'
        hosts=['host1', 'host2', 'host3']

    class MockInventory:
        def __init__(self):
            self.inventory = TestInventory()

        def get_host(self, hostname):
            if hostname not in self.inventory.hosts:
                raise Exception("Unknown host %s" % hostname)
            class TestHost:
                name=hostname
                groups=[]
                vars={
                    'testvar1': 'value1',
                    'testvar2': 'value2'
                }
            return TestHost
        def get_group(self, groupname):
            class TestGroup:
                hostnames=['host1', 'host2', 'host3']
            return TestGroup
    Mock

# Generated at 2022-06-13 15:19:58.412588
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    try:
        # Using 'VarsModule'
        VarsModule.get_vars()
    except Exception as e:
        raise AssertionError("Failed to call get_vars method of VarsModule class")


# Generated at 2022-06-13 15:20:07.512960
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # Set up test environment
    from ansible import context
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    context.CLIARGS = ImmutableDict(tags={}, listtags=False, listtasks=False, listhosts=False, syntax=False,
                                    connection='local', module_path=None, forks=100, private_key_file=None, diff=False,
                                    vault_password_files=[], verbosity=0, check=False)

    loader = DataLoader()

# Generated at 2022-06-13 15:20:13.994638
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    # Create a sample host and a sample group both with the same name 'sample'
    # This name is the same as the name of files in the directories group_vars and host_vars
    # The content of the file group_vars/sample is '{"group_vars": {"group_variable": "group_value"}}'
    # The content of the file host_vars/sample is '{"host_vars": {"host_variable": "host_value"}}'

    myHost = Host('sample')
    myGroup = Group('sample')
    # Create the object VarsModule which will parse the variables to fill in the host and group
    VarsModuleObject = VarsModule()

    # Get the content of the host_vars file that was parsed and stored in the ansible host object
    host_vars = VarsModuleObject.get_

# Generated at 2022-06-13 15:20:18.605822
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    vars_obj = VarsModule()
    vars_obj._basedir = 'test/unit/plugins/vars'
    assert vars_obj.get_vars(object, 'host_vars', [Host('host_name_1')]) == {'host_var_1': 'value_1'}
    assert vars_obj.get_vars(object, 'group_vars', [Group('group_name_1')]) == {'group_var_1': 'value_1'}

# Generated at 2022-06-13 15:20:30.437911
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    host = Host(name="testhost")
    group = Group(name="testgroup")
    VarsModule().get_vars(loader=None, path=None, entities=host)
    VarsModule().get_vars(loader=None, path=None, entities=group)

# Generated at 2022-06-13 15:20:41.322020
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    # get ansible.cfg for the host
    config_file = C.CONFIG_FILE_NAME
    # add config file to the module_utils search path
    C.MODULE_UTILS_PATH.append(os.path.dirname(config_file))

    from ansible.plugins.vars import VarsModule

    import os
    import sys
    import json

    # add path to this plugin to the module_utils search path
    parent_dir = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(parent_dir)
    test_dir = parent_dir + '/test'
    sys.path.append(test_dir)

    # initialize the VarsModule
    vm = VarsModule()
    vm.HAS_JSON = True

    # method get_vars of

# Generated at 2022-06-13 15:20:51.117410
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    # imports
    from ansible.plugins.loader import vars_loader
    from ansible.utils.vars import combine_vars

    # prep test
    class Params:
        def __init__(self, inventory_filename=None):
            self.inventory = inventory_filename

    class FakeLoader:
        def __init__(self, basedir):
            self._basedir = basedir

        @staticmethod
        def find_vars_files(path, entity):
            return [ os.path.join(path, entity) ]

        def load_from_file(self, filename, cache=True, unsafe=True):
            if filename.endswith('.json'):
                return {'json':'loaded'}
            return {'yaml':'loaded'}


# Generated at 2022-06-13 15:20:51.678165
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    pass

# Generated at 2022-06-13 15:20:59.667604
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    # Get a vars plugin
    vm = VarsModule()

    # Create a loader
    loader = DictDataLoader({'group_vars': {'foo': {'host1': {'result.yaml': '{"foo": "this is foo"}'}}}})
    loader.path_exists = lambda x: True

    # Create a host
    host = Host('host1')

    res = vm.get_vars(loader, 'basedir', host)
    assert res == {'foo': 'this is foo'}, res

    # Create a group
    group = Group('foo')

    res = vm.get_vars(loader, 'basedir', group)
    assert res == {'foo': 'this is foo'}, res

# Generated at 2022-06-13 15:21:08.707987
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    # Create a group object to test the method
    test_group = Group()
    test_group._name = 'test_group'
    test_group._basedir = 'dir'

    # Create a host object to test the method
    test_host = Host()
    test_host._name = 'test_host'
    test_host._basedir = 'dir'
    test_host._groups = []
    test_host._groups.append(test_group)

    # Unit test for method get_vars of class VarsModule

# Generated at 2022-06-13 15:21:15.018133
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import pytest
    from ansible.parsing import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    vars_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])
    inventory.subset('testgroup')
    inventory.set_playbook_basedir('/etc/ansible/playbooks')
    vm = inventory.get_host('testgroup')
    group = inventory.get_group('testgroup')
    vars_plugin = VarsModule()
    vars_plugin.set_options(direct=dict(staging='force'))
    vars_plugin._basedir = '/etc/ansible'

# Generated at 2022-06-13 15:21:24.292600
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    class MockHost(object):
        def __init__(self, name):
            self.name = name
            self.vars = {}

    class MockGroup(object):
        def __init__(self, name):
            self.name = name
            self.vars = {}

    class MockLoader(object):
        def __init__(self):
            self.base_path = "/foo"
            self.inventory_directory_path = "/foo"
            self.group_pattern = 'teaparty/(.+)'
            self.host_pattern = 'teaparty/(.+)'

        def find_vars_files(self, path, entity_name):
            return []

        def load_from_file(self, path, cache=False, unsafe=False):
            return {}

    vm = VarsModule()
    vm._

# Generated at 2022-06-13 15:21:32.827867
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    """Tests the get_vars method of the VarsModule"""

    l_module = VarsModule()

    from ansible import context
    from ansible.vars import VariableManager
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugin.loader import vars_loader

    l_var_manager = VariableManager()

    # Note: The hosts.yml file contains globally defined host variables and host variables defined under host_vars.
    l_inventory_manager = InventoryManager(loader=DataLoader(), sources=['test/units/module_utils/hosts.yml'])

    # Create a dummy play (required for host)

# Generated at 2022-06-13 15:21:38.312693
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # testing without ansible.cfg file
    module = VarsModule()
    entities = [Host('test_host1'), Group('test_group1')]
    cache = {}
    path = './test_cases/test_data/inventory_vars/'
    loader = mock_loader()
    module.set_loader(loader)
    module.set_basedir(path)
    result = module.get_vars(loader, path, entities, cache=cache)
    host_vars_data = {'host_specific_var': 'host_specific_value'}
    group_vars_data = {'group_specific_var': 'group_specific_value'}
    assert result == {'test_host1': host_vars_data,
                      'test_group1': group_vars_data}

# Generated at 2022-06-13 15:21:46.169104
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    def mock(entities):
        return 'entities mocked'

    class mock_self:
        def __init__(self):
            self._basedir = 'mocked'
            self._display = 'mocked'

    class mock_loader:
        def find_vars_files(*args):
            return 'find_vars_files mocked'

        def load_from_file(*args):
            return 'load_from_file mocked'

    class mock_super:
        def get_vars(self, loader, path, entities, cache=True):
            return 'get_vars mocked'

    def mock_os_path_realpath(path):
        return 'os.path.realpath(%s) mocked' % path

    def mock_os_path_exists(path):
        return path == 'mocked'

   

# Generated at 2022-06-13 15:21:52.848401
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # subtest get_vars: get vars of host and group.
    # Given
    mock_loader = Mock()
    mock_host = Host('test')

    # When
    result = VarsModule(mock_loader).get_vars(mock_loader, 'test', [mock_host])

    # Then
    assert os.path.isdir.called and os.path.isdir.call_args_list == [call(os.path.join(mock_loader.get_basedir.return_value, 'host_vars'))]

# Generated at 2022-06-13 15:22:05.417505
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    class loader(object):
        def find_vars_files(self):
            return ["exists_file"] if exists_file else []
    exists_file = True
    ENTITIES = [Host("unit_var_plugin"), Group("unit_var_plugin")]
    for entity in ENTITIES:
        vm = VarsModule()
        vm._basedir = "/path"
        vm.get_vars(loader=loader(), path="/path", entities=entity)
        assert len(FOUND) > 0
        FOUND.clear()

    exists_file = False
    vm = VarsModule()
    vm._basedir = "/path"
    vm.get_vars(loader=loader(), path="/path", entities=ENTITIES)
    assert len(FOUND) == 0
    FOUND.clear()

# Generated at 2022-06-13 15:22:14.862171
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.plugins.loader import VarsModule

    # load vars
    loader = VarsModule()
    data = {}

# Generated at 2022-06-13 15:22:19.697988
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.plugins.loader import vars_loader

    # Create an instance of class VarsModule
    test_obj = VarsModule()

    # Create an instance of class DataLoader
    test_loader = vars_loader.VarsAttributeFileLoader()

    # Create an instance of class Group
    test_entity = Group()

    test_entity.name = 'myhost1'
    test_entity.vars = {'account': 'netapp', 'ansible_user': 'admin'}

    test_obj.get_vars(test_loader, '', test_entity)

    # test_obj_vars = dict({'account': 'netapp', 'ansible_user': 'admin'})

    # assert test_obj.get_vars(test_loader, '', test_entity) == test_obj_vars

# Generated at 2022-06-13 15:22:23.531683
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    var_plugin = VarsModule()
    var_plugin.get_vars('loader', __file__, ['host', 'group'])

# Generated at 2022-06-13 15:22:33.343989
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import tempfile
    import shutil
    tmpdir = tempfile.mkdtemp()


# Generated at 2022-06-13 15:22:38.782935
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    '''
    Test for method get_vars of class VarsModule
    '''

    def get_vars_mock(loader_object, path, entity_object, cache=True):
        '''
        Mock to get_vars of class VarsModule
        '''
        return

    test_vars_module = VarsModule()
    test_vars_module.get_vars = get_vars_mock
    test_vars_module.get_vars(loader_object='loader_object', path='path',
                              entities='entities', cache=True)

# Generated at 2022-06-13 15:22:49.160131
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    plugin = VarsModule()
    # Create a Host object
    host = Host('test_host')
    # Create a Group object
    group = Group('test_group')
    # Set basedir
    plugin._basedir = os.getcwd()
    # Call method get_vars
    plugin.get_vars('loader', os.getcwd(), [host, group])

    # Create a Host object
    host = Host('/chroot')
    # Create a Group object
    group = Group('/chroot')
    # Call method get_vars
    plugin.get_vars('loader', os.getcwd(), [host, group])

if __name__ == "__main__":
    test_VarsModule_get_vars()

# Generated at 2022-06-13 15:22:56.742958
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # Create a test Host() with the hostname 'test_host'
    host = Host(name="test_host")

    # Instantiate class VarsModule(), which inherits from BaseVarsPlugin()
    vars_module = VarsModule()

    # Create a fake variables dictionary
    data = {
        'test_variable': "test_value"
    }

    # Mock a fake inventory file structure and set it as the path for the test host
    mock_path = "test_vars_dir"
    host.set_variable("inventory_dir", mock_path)

    # Define the path to the test file
    b_test_file = to_bytes("test_vars_dir/host_vars/test_host.yaml")

    # Mock the open() method of the fake file

# Generated at 2022-06-13 15:23:18.666768
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    class DummyLoader:
        ''' Dummy class for class Loader '''

        def __init__(self):
            self.vars_file_name_extensions = ['.yaml']
            self.base_path = os.path.realpath(os.path.join(os.getcwd(), 'test/unit/plugins/inventory/test_data/test_vars_from_files'))

        def load_from_file(self, path, cache=True, unsafe=False, show_content=True):
            if path.endswith('host_vars.yaml'):
                return {'host': {'var_file': 'host_vars_content'}}

# Generated at 2022-06-13 15:23:26.289920
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from ansible.utils.vars import combine_vars
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager

    basedir = "/etc/ansible/host_vars"
    entity_name = "test1"
    entities = [entity_name]
    cache = True
    class B:
        def __init__(self,d):
            self.name = d.name
    class D:
        def __init__(self,name):
            self.name = name


# Generated at 2022-06-13 15:23:37.185880
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import os
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.plugins.loader import vars_loader

    my_host_name = 'myhost'
    my_group_name = 'mygroup'
    my_host_vars = {'var_host': 'host_var'}
    my_group_vars = {'var_group': 'group_var'}
    my_inventory_directory = './my_inventory_directory'

    my_host = Host(my_host_name)
    my_group = Group(my_group_name)

    class VarsLoader():

        def find_vars_files(self, opath, host_name):
            if host_name == my_host_name:
                file_path = os.path.join

# Generated at 2022-06-13 15:23:40.930508
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    vars = VarsModule()
    vars.vars_cache = {}
    vars._display = DummyDisplay()
    vars._basedir = 'test_path'
    vars.get_vars(DummyLoader(), path='test_path', entities=['localhost'])
    # Only one call expected to load_from_file
    assert DummyLoader.from_file_call_count == 1


# Generated at 2022-06-13 15:23:50.967773
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import pytest
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

    # Define entities
    HOST_NAME = 'localhost'
    HOST_VARS = {'host_var_one':True}
    GROUP_NAME = 'laptop'
    GROUP_VARS = {'group_var_one':False}
    entities = [Host(HOST_NAME), Group(GROUP_NAME)]

    def test_get_vars_mock(self, *args, **kwargs):
        ''' Mock method get_vars of class VarsModule '''
        data = {}

# Generated at 2022-06-13 15:23:59.487331
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    loader = DataLoader()
    inv = InventoryManager(loader=loader, sources=['/tmp'])
    group = Group('group_a')
    group.name = 'group_a'
    group.vars = {}
    host = Host('test.example.org')
    host.name = 'test.example.org'
    host.groups = []
    host.groups.append(group)
    var_manager = VariableManager(loader=loader, inventory=inv)

# Generated at 2022-06-13 15:24:07.154985
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import os
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    inv = InventoryManager(loader=DataLoader())
    inv.add_group('group1')
    inv.add_host(Host('host1'))

    inv.add_group('group2')
    inv.add_host(Host('host2'))

    inv.add_group('group3')
    inv.add_host(Host('host3'))
    inv.add_host(Host('dhost'))
    inv.add_host(Host('ohost'))
    inv.add_host(Host('chroot'))
    inv.add_child('group3', 'child1')


# Generated at 2022-06-13 15:24:17.881316
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.plugins.loader import vars_loader
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    basedir = os.path.join(os.path.dirname(__file__), 'files', 'test_host_group_vars_plugin')
    inventory = InventoryManager(loader=DataLoader(), sources=[os.path.join(basedir, 'hosts')])
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    class Namespace():
        def __init__(self):
            self.subdir = 'test_subdir'
            self.path = os.path.join(basedir, self.subdir)
            self.stage = 'not_parsed'

# Generated at 2022-06-13 15:24:25.193726
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import ansible.plugins.vars.host_group_vars
    # setup some fake objects to make the test work
    loader_obj = ansible.plugins.vars.host_group_vars.VarsModule()
    loader_obj._basedir = 'some_path'
    loader_obj._display = ansible.utils.display.Display() # does not use verbosity

    # This is what is returned from find_vars_files and we need in the test
    found_files = ['some_path/group_vars/group_name', 'some_path/host_vars/host_name']

    # mock the find_vars_files call
    def mocked_find_vars_files(path, name):
        return found_files
    loader_obj.find_vars_files = mocked_find_vars_

# Generated at 2022-06-13 15:24:32.006760
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    module = VarsModule()
    class MockFileLoader:
        def __init__(self):
            self.cache = {}
        def find_vars_files(self, opath, entity_name):
            return ['host_vars/test_host.yml']
        def load_from_file(self, found, cache=True, unsafe=True):
            return {'key': 'test_value'}
    loader = MockFileLoader()
    entities = [Host(name='test_host', port=None)]
    for entity in entities:
        if isinstance(entity, Host):
            subdir = 'host_vars'
        elif isinstance(entity, Group):
            subdir = 'group_vars'

# Generated at 2022-06-13 15:24:50.076192
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    pass

# Generated at 2022-06-13 15:24:57.619171
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=DataLoader(), sources=C.DEFAULT_HOST_LIST)

    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    current_path = os.path.dirname(os.path.realpath(__file__))

    vars_module = VarsModule()

    # Tests with groups
    test_group1 = Group('test_group1')
    vars_module.get_vars(variable_manager._loader, to_text(current_path) + "/test_host_group_vars/", test_group1)

# Generated at 2022-06-13 15:25:02.836404
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import pytest
    from ansible.plugins.loader import vars_loader
    from ansible.plugins.vars import vars_cache
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    FOUND.clear()

    mybasedir = './testdata/plugins/vars/'
    mypath = './testdata/plugins/vars/testdata/'
    myentities = []
    myentities.append(Host(name='test0', port=22))

    mymodule = VarsModule()
    mymodule._basedir = mybasedir
    mymodule._display = False
    mymodule._loader = vars_loader
    mymodule._cache = vars_cache

    result = mymodule.get_vars(mymodule._loader, mypath, myentities)


# Generated at 2022-06-13 15:25:13.382119
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from .mock_playcontext import MockPlayContext

    basedir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'vars_plugin_data')

    # Initialize plugin
    plugin = VarsModule()
    loader = DataLoader()
    MockPlayContext._basedir = basedir
    inventory = MockPlayContext(loader=loader)

    # Load vars
    plugin._basedir = basedir
    plugin._display = MockDisplay()
    plugin._get_files_from_searchpath = plugin._get_files_from_searchpath_safe

# Generated at 2022-06-13 15:25:22.132931
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    '''
    This is a test for the method get_vars of the VarsModule class.
    '''

    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.plugins.vars.host_group_vars import VarsModule
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    plugin_dirs = [os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_data")]
    add_all_plugin_dirs(plugin_dirs)

    empty_plugin_dirs = []
    add_all_plugin_dirs(empty_plugin_dirs)

    # Test 1: Vars directory is present
    # test_data/inventory is present which

# Generated at 2022-06-13 15:25:30.464461
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    modules_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    inv = os.path.join(modules_dir, "host_group_var_stub", "hosts")
    hv1 = os.path.join(modules_dir, "host_group_var_stub", "host_vars", "host1")
    hv2 = os.path.join(modules_dir, "host_group_var_stub", "host_vars", "host2")
    gv = os.path.join(modules_dir, "host_group_var_stub", "group_vars", "all")
    host1 = Host(name="host1")
    host2 = Host(name="host2")
    group = Group(name="all")



# Generated at 2022-06-13 15:25:34.512823
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # get_vars() called in VarsModule.get_vars()
    # get_vars() is used to get the data from the files and return the data
    # This method is tested in test_PluginLoader.test_vars_plugins()
    pass

# Generated at 2022-06-13 15:25:44.442533
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
  import os
  from ansible.parsing.dataloader import DataLoader
  from ansible.inventory.manager import InventoryManager
  from ansible_collections.ansible.community.tests.unit.compat import unittest
  # This test does not load any plugin, so no plugin is whitelisted.
  # It is necessary to whitelist manually the plugin under test.
  C.WHITELIST_PLUGINS.append('host_group_vars')

  class TestVarsModule(unittest.TestCase):
    """
    Unit tests for VarsModule.get_vars.
    """

    def setUp(self):
      self.basedir = os.path.join(os.path.dirname(__file__), 'vars_plugin_staging')

# Generated at 2022-06-13 15:25:52.728511
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    plugin = VarsModule()
    plugin.path = 'test-path'
    plugin.patterns = ''
    plugin._basedir = 'test-base-dir'
    plugin._display = object()

    loader = object()
    loader.find_vars_files.return_value = ['test-file-name']
    loader.load_from_file.return_value = {'test_key': 'test_value'}

    path = '/etc/ansible/'
    entities = [Host(name='test-host'), Group(name='test-group')]
    expected_data = {'test_key': 'test_value'}
    data = plugin.get_vars(loader, path, entities, cache=True)
    assert expected_data == data

# Generated at 2022-06-13 15:26:00.830578
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import pytest
    from ansible.vars.manager import VariableManager
    vars_loader = VariableManager()
    vars_module = VarsModule()
    entities = []
    for name in ['host', 'group']:
        entity = Host(name=name)
        entities.append(entity)
        entity = Group(name=name)
        entities.append(entity)
    data = vars_module.get_vars(vars_loader, path="", entities=entities)
    assert data == {}

# Generated at 2022-06-13 15:26:45.598754
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    class VarsLoader():
        def find_vars_files(self, path, entity_name):
            return [path]

        def load_from_file(self, path, cache=True, unsafe=True):
            return {'data':'test'}

    class Host():
        def __init__(self, name):
            self.name = name

    class Group():
        def __init__(self, name):
            self.name = name

    vm = VarsModule() # fake configManager, super call
    vm.get_vars(VarsLoader(), 'test_path', Host('test_host'))
    assert 1 == 1

# Generated at 2022-06-13 15:26:49.628348
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    plugin = VarsModule()
    host = Host()
    host.name = 'localhost'
    data = plugin.get_vars(loader=None, path='/tmp', entities=host)
    assert isinstance(data, dict)
    assert len(data) == 0

# Generated at 2022-06-13 15:26:57.362162
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import ansible.plugins.vars.host_group_vars as host_group_vars
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    import os
    import shutil
    import tempfile

    current_dir = os.path.dirname(os.path.abspath(__file__))
    group_vars_dir = 'group_vars'
    host_vars_dir = 'host_vars'
    group_name = 'testgroup'
    host_name = 'testhost'
    fake_host_name = 'fakehost'
    var_name = 'testvar'
    var_value = 'testvalue'

    fake_loader = BaseVarsPlugin()

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = os

# Generated at 2022-06-13 15:26:57.794431
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    assert 1 == 1

# Generated at 2022-06-13 15:27:03.246194
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import ansible.plugins.loader as plugin_loader
    from ansible.module_utils._text import to_bytes
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager

    # Required to register the plugin
    plugin_loader.add_directory(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'vars'))


# Generated at 2022-06-13 15:27:03.752460
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    return None

# Generated at 2022-06-13 15:27:09.954938
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    test_path = '/path/to/test/host_vars'
    test_name = 'myhost'

    class Entity:
        def __init__(self, name):
            self.name = name

    class Host(Entity):
        pass

    class Group(Entity):
        pass

    class Loader:
        def __init__(self):
            self.files = {}
            self.files['/path/to/test/group_vars/g1.yml'] = {'k': 'v'}
            self.files['/path/to/test/group_vars/g2.yml'] = {'k': 'v2'}
            self.files['/path/to/test/host_vars/p.yml'] = {'kk': 'vv'}

# Generated at 2022-06-13 15:27:20.598568
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import os
    import pytest
    from ansible.module_utils._text import to_bytes
    from ansible.plugins.vars import BaseVarsPlugin

    # Create vars_plugins directory and
    # add host_group_vars.py to it
    basedir = '/tmp/vars_plugins'
    pyfile = os.path.join(basedir, 'host_group_vars.py')

    # create vars_plugins directory
    os.mkdir(basedir)

    # copy host_group_vars.py to vars_plugins directory

# Generated at 2022-06-13 15:27:26.654085
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'hostvars': {'test1': 'test1'}}
    variable_manager.options_vars = {'hostvars': {'test2': 'test2'}}

    group_vars = VarsModule()
    group_vars.get_vars(loader=loader, path='/tmp/group_vars', entities=Group(name='group'))
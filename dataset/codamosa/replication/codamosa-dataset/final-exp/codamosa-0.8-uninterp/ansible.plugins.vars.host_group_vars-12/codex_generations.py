

# Generated at 2022-06-13 15:17:46.263447
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    ''' Unit test for method get_vars of class VarsModule '''
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    inventory = InventoryManager(loader=DataLoader())

    vars_module = VarsModule()
    path = ""
    entities = []
    cache = False

    # Test 1: Return empty dict
    vars_module.get_vars(inventory, path, entities, cache)

    # Test 2: Return dict with vars data
    entity = Host(name="")
    path = "./test/integration/inventory/host_vars/single_var"
    entities = [entity]
    vars_module.get_vars(inventory, path, entities, cache)
    entity = Host(name="")

# Generated at 2022-06-13 15:17:47.764809
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    v = VarsModule()
    v.get_vars()

# Generated at 2022-06-13 15:17:55.345099
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    from ansible.parsing.vault import VaultLib
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    vars_module = setup_custom_vars_module()

    loader = vars_module._loader

    # Setup a VaultSecret for testing
    vault_id = {'vault_password': 'password'}

    # Create a group and a host for testing
    group_name = 'test_group'
    group = Group(name=group_name)


# Generated at 2022-06-13 15:18:04.359142
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    ''' Test get_vars method of VarsModule class '''
    ###############################################################################################
    # Test scenario
    ###############################################################################################

    # Test result
    class TestVarsModule(VarsModule):
        pass

    class TestHost:
        def __init__(self, name):
            self.name = name
    class TestGroup:
        def __init__(self, name):
            self.name = name

    class TestModuleUtils:
        def __init__(self, value):
            self.value = value

        def find_vars_files(self, opath, entity_name):
            return self.value

        def load_from_file(self, found, cache=True, unsafe=True):
            return {'a': 1}

    # Create test objects
    test_obj

# Generated at 2022-06-13 15:18:11.893167
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleMapping
    from ansible.plugins.loader import find_plugin
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager

    loader_plugin = find_plugin('vars', 'vars_plugin_base')
    loader = loader_plugin()

    entities = [
        Host(name='localhost'),
        Host(name='localhost2'),
        Host(name='localhost3'),
        Host(name='localhost4'),
        Host(name='localhost5'),
        Host(name='localhost6'),
    ]

# Generated at 2022-06-13 15:18:25.694182
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    def _same(x, y):
        return (x > y) - (x < y)

    loader = None
    path = "/tmp/inventory"
    entities = [
        Host(name="devbox01"),
        Host(name="devbox02"),
        Host(name="prodbox01"),
        Group(name="devs"),
        Group(name="prods"),
        Group(name="devops")
    ]

    varsModule = VarsModule()
    # Test method get_vars with valid parameters
    try:
        varsModule.get_vars(loader, path, entities)
        assert 1 == 2
    except:
        assert 1 == 1

    # Test method get_vars with valid parameters

# Generated at 2022-06-13 15:18:36.766805
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    """ Method get_vars of class VarsModule """

    import sys
    sys.modules['ansible.module_utils.six'] = __import__('six')
    sys.modules['ansible.module_utils.six.moves'] = __import__('six.moves')
    sys.modules['ansible.module_utils.six.moves.configparser'] = __import__('six.moves.configparser')

    import ansible.inventory.manager
    import ansible.vars.manager
    import ansible.plugins.loader
    import ansible.parsing.dataloader

    manager = ansible.inventory.manager.InventoryManager(loader=ansible.parsing.dataloader.DataLoader())

# Generated at 2022-06-13 15:18:43.893661
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    """
    Unit test for method get_vars
    """

    # standard test case
    b_vars_dir = to_bytes(os.path.join(os.path.dirname(__file__), 'host_group_vars_test_dir'))
    vars_dir = to_text(b_vars_dir)
    assert(os.path.exists(b_vars_dir))
    assert(os.path.isdir(b_vars_dir))
    b_host_vars_dir = os.path.join(b_vars_dir, to_bytes('host_vars'))
    assert(os.path.exists(b_host_vars_dir))
    assert(os.path.isdir(b_host_vars_dir))
    host_obj = Host

# Generated at 2022-06-13 15:18:54.610673
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    class entity_host(Host):
        def __init__(self,name):
            self.name = name

    class entity_group(Group):
        def __init__(self,name):
            self.name = name

    loader_mock = None
    path = "path/to/modules"
    entities = [entity_host("host1"),entity_host("host2"),entity_host("host3"),entity_host("host4"),entity_host("host5"),entity_host("host6"),entity_host("host7"),entity_group("group1"),entity_group("group2"),entity_group("group3"),entity_group("group4"),entity_group("group5")]
    cache = True
    obj = VarsModule()
    result = obj.get_vars(loader_mock, path, entities, cache)

# Generated at 2022-06-13 15:18:57.306256
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    module = VarsModule()
    assert module.get_vars(None, None, None) == {}


# Generated at 2022-06-13 15:19:05.281659
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    for entity in [Group(name='test'), Host(name='test')]:
        yml = VarsModule({'name':'test'})
        yml.get_vars(loader, '/test_path', entity)
        assert entity.name == 'test'



# Generated at 2022-06-13 15:19:10.241021
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # setup
    b_module_path = os.path.realpath(to_bytes(__file__))
    module_path = to_text(b_module_path)
    host_name = "SOME_HOST"
    host_group_name = "SOME_HOST_GROUP"
    host = Host(host_name)
    group = Group(host_group_name)

    # prepare data for unit test
    b_basedir = os.path.dirname(b_module_path)
    basedir = to_text(b_basedir)
    b_subdir1 = os.path.join(b_basedir, to_bytes("subdir1"))
    subdi1 = to_text(b_subdir1)

# Generated at 2022-06-13 15:19:13.162362
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # Test get_vars(self, loader, path, entities, cache=True):
    m = VarsModule()
    # TODO: Do a test
    pass

# Generated at 2022-06-13 15:19:17.758049
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    VarsModule_object = VarsModule()
    class VarsModule_get_vars_mock:
        def merge_data(self, data, new_data):
            return data
    VarsModule_object.get_vars(VarsModule_get_vars_mock(), "path", "entities")

# Generated at 2022-06-13 15:19:26.001318
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # this is needed in order to create the config objects in the right order
    C.config = None

    # create an instance of VarsModule class
    vm = VarsModule()

    # retrieve the method to test
    get_vars = vm.get_vars

    # this is a hack to get the parent's object in order to
    # be able to call the method from the BaseVarsPlugin class
    vm.BaseVarsPlugin.get_vars = object.__getattribute__(vm, 'get_vars')

    # create an instance of BaseLoader class
    loader = vm.BaseVarsPlugin.get_loader(to_bytes('path'))

    # create an instance of Host class
    h = Host(to_bytes('myhost'))

    # call the method to test
    # get_vars(loader, path,

# Generated at 2022-06-13 15:19:36.384210
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory import Inventory
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    # preparing data
    origin_hosts = ['/host1', 'host2', '/host3']
    hosts = []

# Generated at 2022-06-13 15:19:38.460570
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    """ An empty test function for VarsModule class.
        This class is tested manually.
    """
    pass

# ----------------------------------------------------


# Generated at 2022-06-13 15:19:44.705597
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.plugins.loader import vars_loader

    test_host = Host(name='host_name')
    test_group = Group(name='group_name')

    subdir = 'host_vars'
    test_path = os.path.realpath(os.path.join(C.DEFAULT_VARS_PATH, subdir))

    basename = test_host.name
    valid_filenames = C.YAML_FILENAME_EXT
    invalid_filenames = ['.swp', '.swx', '.pyc', '.bak', '.tmp']
    # file extension
    for ext in valid_filenames:
        filename = '%s%s' % (basename, ext)
        file_path = os.path.join(test_path, filename)

# Generated at 2022-06-13 15:19:46.858611
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    vm = VarsModule()
    vm.get_vars(None, "", "")

# Generated at 2022-06-13 15:19:56.316466
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import sys
    from ansible.parsing.dataloader import DataLoader

    subdir = 'vars_host_group_vars'       # subdir of tests/test_utils/test_data/
    basedir = 'vars_host_group_vars/test_dir'  # base dir to find vars directory

    groups = ('test_group',)
    host = Host(name='test_hostname')
    entity_list = [host, groups]

    # create a dummy config for the plugin

# Generated at 2022-06-13 15:19:59.510012
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    assert(False)

# Generated at 2022-06-13 15:20:08.233506
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # test case data
    data = {
        "vars": {
            "VarsModule": {
                "extends_documentation_fragment": {
                    "vars_plugin_staging": {}
                }
            },
            "path": "tests/unit/plugins/inventory/host_group_vars/",
            "entities": [
                {
                    "data": {
                        "name": "host_name"
                    },
                    "class": "Host"
                },
                {
                    "data": {
                        "name": "group_name"
                    },
                    "class": "Group"
                }
            ]
        }
    }

    vars_module = VarsModule()
    config = C.ConfigParser()
    null_display = C.Display()

    # test case
    #

# Generated at 2022-06-13 15:20:14.570933
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import os
    import sys

    # Change directory to test directory
    test_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(test_dir)

    # Need to mock several methods/attributes of loader to run method get_vars
    import ansible.plugins.loader as loader
    import ansible.parsing.dataloader
    import ansible.inventory.manager
    import ansible.vars.manager
    import ansible.utils.display
    import ansible.utils.vars
    # Dict with values required by method find_vars_files

# Generated at 2022-06-13 15:20:21.026656
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    import os

    source = '''
[all:vars]
ansible_user="automation"
ansible_password="automation"
ansible_port=22
ansible_connection="ssh"
ansible_become_pass="automation"
ansible_become="true"

[localhost]
provisioner

[provisioner]
1.1.1.1'''

    current_dir = os.getcwd()

    # Create a dummy inventory

# Generated at 2022-06-13 15:20:32.447300
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    vars_module = VarsModule()
    vars_module._basedir = os.path.realpath('.')
    group = Group('localhost')
    group_vars_found = vars_module.get_vars(None, None, group)
    assert group_vars_found == {'group_variable': 'group.yml', 'group_var_files': 'group_var_files.yml', 'group_var_files_var': 'group_var_files_var.yml'}
    host = Host('localhost')
    host_vars_found = vars_module.get_vars(None, None, host)

# Generated at 2022-06-13 15:20:43.112126
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
  from ansible.inventory.manager import InventoryManager
  from ansible.playbook.play_context import PlayContext

  class _loader(object):
    def get_basedir(self):
      return '/home/user'

    def get_inventory(self):
      return InventoryManager(loader=self, sources=['localhost'])

    def find_vars_files(self, path, entities):
      files = ['/home/user/group_vars/all.yml']
      self.called_times += 1
      if self.called_times == 1:
        assert path == '/home/user/group_vars'
        assert entities == 'all'
        assert files == ['/home/user/group_vars/all.yml']
      else:
        assert 'should not reach here'
      return files


# Generated at 2022-06-13 15:20:52.698400
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.plugins.loader import vars_loader

    class TestInventory():
        def __init__(self, file):
            self.hosts_list = [
                        Host(name='testhost1'),
                        Host(name='testhost2'),
                        Host(name='testhost3'),
                        ]
            self.groups_list = [
                        Group(name='testgroup1'),
                        Group(name='testgroup2'),
                        Group(name='testgroup3'),
                        ]

            self.groups_list[0].add_child_group(self.groups_list[1])
            self.groups_list[2].add_child_group(self.groups_list[0])
            self.groups_list[1].add_host(self.hosts_list[0])
            self.groups_list[1].add_

# Generated at 2022-06-13 15:21:00.989787
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # the test_vars_plugin needs to be initialized with a fake inventory
    test_result = {}
    class fake_display:
        def __init__(self):
            pass
        def debug(self, msg):
            if 'processing dir' in msg:
                test_result['debug_msg'] = msg
    test_vars_plugin = VarsModule()
    test_vars_plugin._display = fake_display()
    entity = Group('all')
    # simulate inventory directory structure for this test
    test_vars_plugin._basedir = '/fake/path'
    loader = FakeLoader()
    test_path = to_text(os.path.join(test_vars_plugin._basedir, 'group_vars'))

# Generated at 2022-06-13 15:21:05.167690
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

  # To initialize VarsModule class
  vars_module = VarsModule()

  # To initialize Host class
  host = Host('127.0.0.1')

  # Calling get_vars method of class VarsModule 
  data = vars_module.get_vars('loader','path','entities')
  return data

# Generated at 2022-06-13 15:21:12.662255
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    test_file = os.path.join(os.path.dirname(__file__), 'vars_plugin_staging_test.yml')

    class MockLoader(object):
        def __init__(self):
            self.paths = [test_file]

    class MockConfig(object):
        def __init__(self):
            self.vars_plugin_staging = {
                'env': 'ANSIBLE_VARS_PLUGIN_STAGE'
            }

    class MockDisplay(object):
        def __init__(self):
            pass

    class MockHost(object):
        def __init__(self, name, port):
            self.name = name
            self.port = port


# Generated at 2022-06-13 15:21:25.216642
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # Testing for method get_vars(self, loader, path, entities, cache)
    # Testing for exception in get_vars()
    # Raised when the supplied entity is not either Host or Group
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.utils.display import Display
    from ansible.module_utils.six import StringIO
    data = '''
    [all]
    test_host
    '''
    vars_module = VarsModule()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=data)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play

# Generated at 2022-06-13 15:21:33.604793
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import os
    import pytest
    from ansible.errors import AnsibleParserError
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.plugins.loader import VarsLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins.vars.host_group_vars import VarsModule
    from ansible.utils.vars import combine_vars
    from io import BytesIO

    loader = DataLoader()
    host = Host("myhost")
    group = Group("mygroup")

    vars_module = VarsModule()
    vars_loader = VarsLoader()

    basedir = os.getcwd()

    vars_module._basedir = basedir


# Generated at 2022-06-13 15:21:46.444128
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import random, string
    # Create a temp directory
    import tempfile
    import shutil
    import re
    import os.path

    tmpdir = tempfile.mkdtemp(prefix='ansible_vars_test_dir')
    tmpdir2 = tempfile.mkdtemp(dir=tmpdir)
    tmpdir3 = tempfile.mkdtemp(dir=tmpdir)

    # Populate the tmp directory
    group_vars_dir = os.path.join(tmpdir2, 'group_vars')
    os.makedirs(group_vars_dir)
    host_vars_dir = os.path.join(tmpdir3, 'host_vars')
    os.makedirs(host_vars_dir)

    # Create our Host and Group objects

# Generated at 2022-06-13 15:21:54.899620
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from collections import Mapping
    from ansible.plugins.loader import vars_loader

    from ansible import constants as C
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    current_dir = os.path.dirname(os.path.realpath(__file__))
    target_dir = os.path.normpath(os.path.join(current_dir, '../../../test/integration/inventory/host_group_vars/'))

    loader = DataLoader()

    inv = InventoryManager(
        loader=loader,
        sources=target_dir
    )

    results = inv.get_hosts(pattern='group_vars_exist_group')
    assert len(results) == 1

# Generated at 2022-06-13 15:22:07.165357
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    class FakeHost():
        def __init__(self, name):
            self.name = name
            self.vars = {}

    class FakeGroup():
        def __init__(self, name):
            self.name = name

    class BaseClassForTest_get_vars():
        def __init__(self):
            self._display = BaseVarsModule()
            self._basedir = os.path.dirname(os.path.realpath(__file__))

    class FakeLoader():
        def __init__(self, basedir):
            self._basedir = basedir


# Generated at 2022-06-13 15:22:15.052286
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import tempfile
    from ansible.module_utils.common._collections_compat import UserDict
    from ansible.module_utils.common.collections import is_sequence

    b_path = tempfile.mkdtemp(prefix='ansible_vars_host_group_vars_unittest_')
    path = to_native(b_path, errors='surrogate_or_strict')
    os.chmod(b_path, 0o777)

    b_subdir = os.path.join(b_path, b'host_vars')
    subdir = to_native(b_subdir)
    os.mkdir(b_subdir)
    os.chmod(b_subdir, 0o777)


# Generated at 2022-06-13 15:22:26.968544
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.module_utils.six import StringIO
    from ansible.utils import plugins
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib

    plugins._load_plugins(C.DEFAULT_VARS_PLUGIN_PATH, 'vars')


# Generated at 2022-06-13 15:22:29.335279
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
  VarsModule.get_vars()


# Generated at 2022-06-13 15:22:37.787511
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    vars_module = VarsModule(None)

    class MockInventory:
        def __init__(self):
            self.basedir = 'fake_path'

    class MockHost:
        def __init__(self, name):
            self.name = name

    class MockGroup:
        def __init__(self, name):
            self.name = name

    class MockLoader:
        def find_vars_files(self, opath, name):
            return None
        def load_from_file(self, found, cache, unsafe):
            return None

    # Test case with host and loader which specify a real path
    mock_host = MockHost('fake_path')
    mock_loader = MockLoader()

    vars_module.get_vars(mock_loader, None, mock_host)

    # Test

# Generated at 2022-06-13 15:22:41.539604
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    vars_module = VarsModule()
    vars_module._basedir = "./"
    vars_module._display = True
    hosts = [Host(name="h1"), Host(name="h2")]
    paths = "./multiple_groups.yaml"
    empty_groups = [Group(name="g1"), Group(name="g2")]
    result_dict = vars_module.get_vars(loader=None, path=paths, entities=hosts)
    print(result_dict)

# Generated at 2022-06-13 15:22:58.116161
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    # Create test host
    test_host = Host('localhost')

    # Generate expected value based on test_host
    expected_value = {'ansible_connection': 'local', 'ansible_user': 'root'}

    # Create object of class VarsModule
    vars_module = VarsModule()

    # Test get_vars method
    assert vars_module.get_vars(test_host, '/ansible/test/host_vars', test_host) == expected_value

    # Create test group
    test_group = Group('webservers')

    # Generate expected value based on test_group
    expected_value = {'port': '80'}

    # Test get_vars method

# Generated at 2022-06-13 15:23:06.732309
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    filename = "test_VarsModule_get_vars.py"
    # Loading constants.py to enable set_constants()
    constants = __import__("ansible.constants")
    constants.set_constants(load_config=False)

    # Creating host and group objects
    h_obj = Host('host_name')
    g_obj = Group('group_name')
    entity_objs = [h_obj, g_obj]

    for entity_obj in entity_objs:
        class Dummy(object):
            def __init__(self, b_opath, s_opath):
                self.basedir = b_opath
                self.path = s_opath
                self.vault_password = None
                self.get_basedir = lambda: b_opath

# Generated at 2022-06-13 15:23:08.281515
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    vmod_obj = VarsModule()
    # TODO: write unit test


# Generated at 2022-06-13 15:23:11.040604
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    assert 'host_group_vars' in C.config.list_plugin_classes()
    plugin = C.config.plugin_loader.get('host_group_vars', class_only=True)()
    plugin.get_vars(loader=None, path='path', entities=['ent1', 'ent2'])

# Generated at 2022-06-13 15:23:14.334717
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    plugin = VarsModule()
    entities = [Host(name='localhost')]
    data = plugin.get_vars(object(), path='/etc/ansible/inventory', entities=entities)
    assert isinstance(data, dict)
    assert data == {}

# Generated at 2022-06-13 15:23:21.737450
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    class MockVarsPlugin(object):
        def __init__(self):
            self._basedir = os.path.join(os.path.dirname(__file__), 'data')
            self._display = None

    # Normal case: a file called "var_file" is found
    vars_module = VarsModule()
    mock_host = Host()
    mock_host.name = 'host_name'
    vars_module._basedir = os.path.join(os.path.dirname(__file__), 'data')
    results = vars_module.get_vars(MockVarsPlugin(), 'file_name', mock_host)
    assert results == {'var': 'value'}, "get_vars should return the content of real file"

    # Abnormal case: a file called "var_file

# Generated at 2022-06-13 15:23:27.946987
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    plugin = VarsModule()
    loader = DictDataLoader({})
    path = os.path.join(C.DEFAULT_LOCAL_TMP, "ansible_vars_plugin_test_VarsModule")
    if not os.path.exists(path):
        os.makedirs(path)

    path_subdir = os.path.join(path, "group_vars")
    if not os.path.exists(path_subdir):
        os.makedirs(path_subdir)

    p1 = os.path.join(path_subdir, "host.yml")
    with open(p1, "w") as f:
        f.write("""---
a:
  - b
  c
""")


# Generated at 2022-06-13 15:23:38.450155
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # Create the vars module object
    v = VarsModule()

    # Create the host object
    h = Host()
    h.name = "somehost"

    # Create the loader object
    l = AnsibleLoader()
    l._basedir = "."
    # Create the vars dictionnary
    d = "./host_vars/somehost"
    data = {"host_file": "host_vars/somehost"}
    # Fake an existing path
    os.path.exists = lambda: True
    os.path.isdir = lambda: True
    # Fake the find_vars_file method
    l.find_vars_files = lambda a, b: [d]
    # Fake the load_from_file method
    l.load_from_file = lambda a, b: data
    # Fake the

# Generated at 2022-06-13 15:23:48.622108
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    class DummyEntity(object):
        def __init__(self, name):
            self.name = name

    class DummyLoader(object):
        def __init__(self, path):
            self.path = path
            self._search_paths = []

        def set_search_path(self, search_path):
            self._search_paths.append(search_path)

        def find_vars_files(self, path, entity_name):
            return ["host_vars/" + entity_name]

        def load_from_file(self, path, cache=True, unsafe=True):
            return {"_test_VarsModule_get_vars": "yes"}


    plugin = VarsModule()

    loader = DummyLoader('')

# Generated at 2022-06-13 15:23:52.060270
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    class TestModule(BaseVarsPlugin):
        def get_vars(self, loader, path, entities, cache=True):
            return {'test_var': True}

    assert VarsModule.REQUIRES_WHITELIST
    assert not TestModule.REQUIRES_WHITELIST

# Generated at 2022-06-13 15:24:10.268929
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    '''
    Basic import, pass through test
    '''
    import os
    mock_loader = type('', (), {'find_vars_files': lambda x, y: ['./test/testdata/group_vars/'], 'load_from_file': lambda x: {'testvar': 'testvalue'}})
    v = VarsModule()
    v.set_options({'basedir': 'test/testdata'}) # set basedir so that find_vars_files works
    group = type('', (), {'name': 'localhost'})()
    # FOUND is a class level variable that is used for caching, reset to empty
    VarsModule.FOUND = {}
    vars = v.get_vars(mock_loader, 'test/testdata', group)

# Generated at 2022-06-13 15:24:19.915204
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    '''
    Unit test for method get_vars of class VarsModule
    '''
    from ansible.plugins.loader import vars_loader
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager

    var_manager = VariableManager()

    group = Group('group_name')
    group.vars = {'group_var1': 'group_var1_value'}

    host = Host(name='host_name')
    host.vars = {'host_var1': 'host_var1_value'}
    host.groups.append(group)

    vars_module = VarsModule()
    vars_module._basedir = os.path.dirname(__file__)

# Generated at 2022-06-13 15:24:26.539574
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.module_utils.six import PY3
    from ansible.module_utils.six.moves import StringIO
    data = {}
    data['basedir'] = "/tmp"
    data['playbook_basedir'] = "/tmp"
    data['inventory_basedir'] = "/tmp"
    data['inventory_basedir_expanded'] = "/tmp"
    data['inventory_dirname'] = "/tmp"
    data['vars_plugins'] = []
    data['hostvars'] = {}
    data['host'] = Host(name='127.0.0.1')
    data['group_names'] = []
    data['group_names'].append('group1')
    data['group'] = Group(name='group1')

# Generated at 2022-06-13 15:24:32.721396
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    group_vars = VarsModule()

    from ansible.plugins.loader import vars_loader

    my_base_dir = "/home/shanto/projects/ansible/plugins/vars/"

    my_group_vars_path = "/home/shanto/projects/ansible/plugins/vars/group_vars/"

    # create a mock class to return the required data
    class VarsLoader():
        def __init__(self):
            pass

        @staticmethod
        def find_vars_files(opath, entity_name):
            group_vars_file_name = entity_name + ".yaml"
            group_vars_file_path = my_group_vars_path + group_vars_file_name


# Generated at 2022-06-13 15:24:42.010865
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.plugins.vars import get_vars_loader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    # find valid extensions
    loader = get_vars_loader()
    extensions = loader._get_valid_extensions()
    # create a path to host/group_vars/
    host_vars_path = os.path.join(os.path.dirname(__file__), 'host_vars', '*')
    # get recursively all files in host_vars_path
    host_vars_files = loader.path_dwim_relative(host_vars_path)

    host = Host()

# Generated at 2022-06-13 15:24:52.410250
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    import ansible.plugins.vars.host_group_vars
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    import os

    ansible_path = os.path.dirname(ansible.plugins.vars.host_group_vars.__file__)
    base_path = os.path.join(ansible_path, os.path.pardir, os.path.pardir)

    loader = DataLoader()
    inv = InventoryManager(loader=loader, sources=os.path.join(base_path, 'tests', 'inventory'))

# Generated at 2022-06-13 15:24:59.246174
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # prepare
    entities = [
        Host(name='test_host_1', port=22),
        Host(name='test_host_2', port=22),
        Group(name='test_group_1'),
        Group(name='test_group_2')
    ]
    path = '/test/mock/path/'
    loader = MagicMock()
    cache = True
    vars_module = VarsModule()
    vars_module._basedir = path

    # test
    vars_module.get_vars(loader, path, entities, cache)

    # verify
    loader.find_vars_files.assert_any_call('/test/mock/path/host_vars/test_host_1', 'test_host_1')
    loader.find_vars_files.assert_

# Generated at 2022-06-13 15:25:09.318352
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    from ansible.plugins import vars_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    current_dir = os.getcwd()
    os.chdir(os.path.join(current_dir, 'data', 'inventory_vars_plugin'))
    loader = vars_loader.VarsLoader()
    vars_manager = VariableManager()
    inv_manager = InventoryManager(loader=loader, sources=['hosts'])
    group = Group('group')
    group.vars = {'var1': 'group_var1', 'var2': 'group_var2'}
    host = Host

# Generated at 2022-06-13 15:25:19.711293
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    from ansible.module_utils.common.collections import ImmutableDict

    import os
    import collections
    import tempfile
    import shutil
    import sys

    # Python 2 and 3 compatible way to compare dictionaries
    if sys.version_info >= (2, 7):
        def compare_dicts(d1, d2):
            return collections.Counter(d1) == collections.Counter(d2)
    else:
        def compare_dicts(d1, d2):
            return d1 == d2

    # Create a temporary directory
    tmp_dir = tempfile.mkdtemp()
    host_vars_dir = os.path.join(tmp_dir, 'host_vars')
    group_vars_dir = os.path.join(tmp_dir, 'group_vars')

# Generated at 2022-06-13 15:25:23.580896
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    # test if the plugin can find it
    assert VarsModule.find_plugin() is not None
    # test if the plugin has the required attribute
    assert hasattr(VarsModule, 'get_vars')

# Generated at 2022-06-13 15:25:52.495378
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    c = ["FoO", "BaR"]
    loader = None
    path = "/path/to/file"
    g1 = Host(name="g1")
    g2 = Host(name="g2")
    entities = [g1, g2]
    cache = True

    # Test with entities as list of Host objects
    obj = VarsModule()
    assert obj.get_vars(loader, path, entities, cache) == {}

    # Test with entities as Host object
    assert obj.get_vars(loader, path, g1, cache) == {}

    # Test with entity as Group object
    g3 = Group(name="g3")
    obj.get_vars(loader, path, g3, cache)

# Generated at 2022-06-13 15:25:54.416550
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    assert 0


# Generated at 2022-06-13 15:26:04.584603
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    from ansible.plugins.loader import action_loader
    from ansible.plugins.loader import connection_loader
    from ansible.plugins.loader import shell_loader
    from ansible.plugins.loader import strategy_loader
    from ansible.plugins.loader import lookup_loader
    from ansible.plugins.loader import module_loader
    from ansible.plugins.loader import filter_loader
    from ansible.plugins.loader import callback_loader
    from ansible.plugins.loader import test_loader
    from ansible.plugins.loader import fragment_loader
    from ansible.plugins.loader import cache_loader


# Generated at 2022-06-13 15:26:12.783577
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    basedir = '/path/to/basedir'
    class TestHost:
        def __init__(self, hostname):
            self.name = hostname
    class TestGroup:
        def __init__(self, groupname):
            self.name = groupname


# Generated at 2022-06-13 15:26:22.688802
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    """Test method get_vars of class VarsModule"""

    # Inventory path not absolute and supplied entity is Host
    mock_entity = Host('hostname', port=22)
    class mock_loader(object):
        @staticmethod
        def find_vars_files(path, entity_name):
            return [os.path.join(path, entity_name + '.yml')]
        @staticmethod
        def load_from_file(path, cache=True, unsafe=True):
            return {'host_var': 'host_var_value'}
    assert VarsModule(mock_loader(), '/tmp', [mock_entity]).get_vars(mock_loader, '/tmp', [mock_entity]) == {'host_var': 'host_var_value'}

    # Inventory path not absolute and supplied entity is

# Generated at 2022-06-13 15:26:29.635692
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    class MockVarsModule(VarsModule):
        def __init__(self):
            pass

        def _get_basedir(self, path):
            return os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../', path))

        def _get_paths(self, path):
            return [self._get_basedir(path)]

        @staticmethod
        def _get_subdir(path):
            return "subdir"

    host = Host()
    host.name = "testing_load"
    mocked = MockVarsModule()

# Generated at 2022-06-13 15:26:34.112803
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    class Fake_Inventory():
        class Fake_Group():
            def __init__(self, name):
                self.name = name

            def __str__(self):
                return 'Group: %s' % self.name

        def __init__(self, name):
            self.name = name

        def __str__(self):
            return 'Fake_Inventory: %s' % self.name

        def _restructure(self):
            return Fake_Inventory(self.name)

        def get_host(self, hostname):
            return Host(hostname)

        def get_group(self, groupname):
            return Fake_Group(groupname)


# Generated at 2022-06-13 15:26:35.270639
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():

    assert VarsModule.get_vars() == False

# Generated at 2022-06-13 15:26:43.838942
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    """
    Test get_vars method of VarsModule
    """
    # Define variables
    # Test 1
    root_inventory_path = os.path.join(os.path.dirname(__file__), "test_data", "lots_of_files")
    Host_name = "node1"
    Host_address = "localhost"
    Host_port = "22"
    Host_vars = None
    Host_set_variable = None
    Host_groups = None
    Host_group_names = None
    Host_set_group_variable = None
    Host_set_effective_vars = None
    Host_set_effective_group_vars = None
    Host_set_parent_groups = None
    Host_set_group_vars = None
    Host_set_host_vars = None

# Generated at 2022-06-13 15:26:53.658189
# Unit test for method get_vars of class VarsModule
def test_VarsModule_get_vars():
    """test the get_vars method of VarsModule"""

    # create a test inventory object
    test_inventory = {
        "test_host_1": {"ansible_ssh_host": "192.0.2.0",
                        "foo": "bar",
                        "testvar": "testvalue"},
        "test_host_2": {"ansible_ssh_host": "192.0.2.1",
                        "foo": "baz",
                        "testvar": "testvalue"}
    }

    # create a file in the role's host_vars directory
    import tempfile, shutil
    temp_dir = tempfile.mkdtemp()
    temp_host_vars = os.path.join(temp_dir, "host_vars")
    os.mkdir(temp_host_vars)
    temp
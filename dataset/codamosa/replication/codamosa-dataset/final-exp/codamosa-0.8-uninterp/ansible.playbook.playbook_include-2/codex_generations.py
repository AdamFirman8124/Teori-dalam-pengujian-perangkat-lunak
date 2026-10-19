

# Generated at 2022-06-13 08:41:56.961563
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.utils.collection_loader._collection_finder import AnsibleCollectionFinder
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.playbook.play import Play

    basedir = os.path.join(os.path.dirname(__file__), 'data', 'playbook_include')
    loader = DataLoader()
    fake_collections = [os.path.join(basedir, 'namespace', 'collection', 'plugins')]
    AnsibleCollectionConfig.configured = True
    AnsibleCollectionConfig.collection_paths = fake_collections

# Generated at 2022-06-13 08:42:09.578532
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # __import__ will import PlaybookInclude
    PlaybookInclude = __import__('ansible.playbook.play_include',
                                 fromlist=['PlaybookInclude']).PlaybookInclude
    from ansible.utils.collection_loader import AnsibleCollectionConfig

    # load collection
    collections_path = os.path.join(os.path.dirname(__file__),
                                    '../../../test/sanity/collection_tests/collection_examples/ansible_collections/test_ns/test_coll',
                                    'files/test_playbook_with_role.yml')

    resource = _get_collection_playbook_path(collections_path)
    if resource is not None:
        playbook = resource[1]
        playbook_collection = resource[2]

# Generated at 2022-06-13 08:42:20.714731
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.playbook.playbook_include as playbook_include
    import ansible.playbook.playbook as playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.task_include import TaskInclude

    basedir = os.getcwd()

    play1 = PlaybookInclude()
    play1._load_playbook_data(file_name='test_include_playbook1.yml', basedir=basedir)


# Generated at 2022-06-13 08:42:27.321435
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    import ansible.playbook.playbook_include as playbook_include

    ds = AnsibleMapping()
    ds.ansible_pos = (1,0)

    # Case 1: Merge parameters and vars
    ds_1 = ds.copy()
    ds_1['import_playbook'] = "file_name"
    ds_1['tags'] = "tag_1"

    new_ds_1 = ds_1.copy()
    new_ds_1['import_playbook'] = "file_name"
    new_ds_1['tags'] = ["tag_1"]

    ds_2 = ds_1.copy()
    ds_2['vars'] = {}

    ds_2['vars']['param_1'] = "val_1"
    ds

# Generated at 2022-06-13 08:42:34.639432
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    ds = {'import_playbook': '../other.yml', 'tags': 'tag_01,tag_02'}
    ds2 = {'import_playbook': '../other.yml', 'vars': {'foo': 'bar'}}
    ds3 = {'import_playbook': '../other.yml', 'vars': {'foo': 'bar'}, 'tags': 'tag_01,tag_02'}
    ds4 = {'import_playbook': '../other.yml', 'vars': {'foo': 'bar'}, 'tags': 'tag_01,tag_02'}

# Generated at 2022-06-13 08:42:36.122342
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # TODO: implement unit test
    pass

# Generated at 2022-06-13 08:42:37.103797
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:42:50.494639
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.template import Templar

    # initialize
    data = AnsibleMapping()
    data.ansible_pos = (1,1)
    templar = Templar(loader=None)

    # test simple case
    data['import_playbook'] = 'test_playbook.yml'
    result = PlaybookInclude().preprocess_data(data)
    expected = AnsibleMapping()
    expected.ansible_pos = data.ansible_pos
    expected['import_playbook'] = 'test_playbook.yml'
    assert(result == expected)

    # test simple case with tags

# Generated at 2022-06-13 08:43:04.508087
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    import os

    basedir = os.path.join(os.path.dirname(os.path.realpath(__file__)),'..','..')
    file_name = 'include_test_include.yml'

    import_task = Task()
    import_task.name = 'sample task'
    import_task.action = 'debug'
    import_task.tags = ['debug']
    import_task.when = ['a']

    import_handler = Handler()
    import_handler.name = 'sample handler'
    import_handler.tags = ['handler']

    import_play = Play()
    import_play.name

# Generated at 2022-06-13 08:43:05.542805
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass


# Generated at 2022-06-13 08:43:20.331040
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # pylint: disable=unused-argument

    import ansible.playbook.play
    import ansible.playbook.playbook

    class MockAnsiblePlaybook:
        def __init__(self):
            self.vars = {'role_name': 'test'}
            self.tags = ['test: tag']
            self.playbook = None
            self._included_path = None

    class MockAnsiblePlay:
        def __init__(self):
            self.name = "test play"
            self.vars = {'role_name': 'test'}
            self.tags = ['test: tag']
            self._included_path = None


# Generated at 2022-06-13 08:43:32.204423
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    # Prepare the environment
    p = PlaybookInclude()
    basedir = os.path.join(os.path.dirname(__file__), 'playbook')
    ds = {}
    loader = DataLoader()
    vars_manager = VariableManager()

    # Test if the method returns a playbook
    pb = p.load_data(ds={'import_playbook': os.path.join(basedir, 'import_playbook.yml')}, basedir=basedir, loader=loader, variable_manager=vars_manager)
    assert type(pb) is type(Playbook())

    # Test if the method raises an exception for empty playbook

# Generated at 2022-06-13 08:43:33.920354
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # Create a new PlaybookInclude
    test_object = PlaybookInclude()

    assert test_object != None

# Generated at 2022-06-13 08:43:46.136342
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.play_context import PlayContext

    playbook_dir = '/path/to/playbook'

    # Test playbook include without variables
    ds = dict(import_playbook='/path/to/playbook/task_file.yml')
    pb_inc = PlaybookInclude().load(ds, playbook_dir)

    assert pb_inc.import_playbook == '/path/to/playbook/task_file.yml'
    assert pb_inc.vars == {}
    assert pb_inc.tags == []

    # Test playbook include with variables
    ds = dict(import_playbook='/path/to/playbook/task_file.yml', vars=dict(foo='bar'))
    pb_inc = PlaybookInclude().load(ds, playbook_dir)

# Generated at 2022-06-13 08:43:56.289422
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # Test preprocess_data method
    data = dict(
        import_playbook='playbook.yml',
        vars=dict(
            key1=1,
            key2=2
        ),
        tags=['tag1', 'tag2'],
    )
    data = PlaybookInclude(data, dict())
    data.preprocess_data(data.__dict__)
    assert data._data['import_playbook'] == 'playbook.yml'
    assert data.import_playbook == 'playbook.yml'
    assert data._data['vars']['key1'] == 1
    assert data._data['vars']['key2'] == 2
    assert data.vars['key1'] == 1
    assert data.vars['key2'] == 2

# Generated at 2022-06-13 08:44:11.938851
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    # Test 1: no vars specified
    ds = {'import_playbook': 'roles.yml'}
    new_ds = PlaybookInclude.preprocess_data(ds)
    assert isinstance(new_ds, dict)
    assert new_ds == {'import_playbook': 'roles.yml'}

    # Test 2: with vars specified
    ds = {'vars': {'var1': 'abc', 'var2': 'def'}, 'import_playbook': 'roles.yml'}
    new_ds = PlaybookInclude.preprocess_data(ds)
    assert isinstance(new_ds, dict)

# Generated at 2022-06-13 08:44:23.718752
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    obj = PlaybookInclude()

    result1 = obj.preprocess_data({'import_playbook': "../../another.yml", 'vars': {'var1': 'value1'}})
    assert result1 == {'import_playbook': '../../another.yml', 'vars': {'var1': 'value1'}}

    result2 = obj.preprocess_data({'import_playbook': "../../another.yml", 'var1': 'value1'})
    assert result2 == {'import_playbook': '../../another.yml', 'vars': {'var1': 'value1'}}

    result3 = obj.preprocess_data({'import_playbook': '../../another.yml', 'tags': "tag1,tag2"})

# Generated at 2022-06-13 08:44:26.038062
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import_playbook = PlaybookInclude.load(data={'import_playbook': 'play3.yml'}, basedir='/')
    assert isinstance(import_playbook, PlaybookInclude)
    assert import_playbook.import_playbook == 'play3.yml'


# Generated at 2022-06-13 08:44:37.577909
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    class inventory:
        def __init__(self):
            self.hosts = 'all'

    import os
    mock_loader = {
        'module_loader': None,
        'file_loader': None,
    }
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    basedir = '%s/data/playbook_include' % curr_dir

    def load_vars_file(filename, loader, vault_password=None, vars_dict=None):
        return {}

    class mock_variable_manager:
        def __init__(self, inventory):
            self.inventory = inventory
            self.extra_vars = {}
            self.vault_pass = None
            self.vars_files = []
            self.options_vars = []

# Generated at 2022-06-13 08:44:49.049305
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()

    # Test to check if import_playbook is working as expected.
    # Use the below statements in a playbook to include 1.yml in 2.yml
    # import_playbook: 1.yml
    yml_string = '''- import_playbook: 1.yml'''
    data = loader.load(yml_string)

    # Now lets try to parse the above data.
    # We are expecting 'import_playbook' instead of '- import_playbook'
    # and the value to be 1.yml instead of '1.yml'

# Generated at 2022-06-13 08:45:06.368761
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.constants import DEFAULT_VAULT_PASSWORD_FILE, DEFAULT_VAULT_IDENTITY_LIST
    from ansible.parsing.vault import get_vault_secrets, VaultSecret, VaultLib

    # Ansible-mock initialization:
    #
    # Mock encrypted_file_text that encrypts "secret" as "secret-encrypted".
    # This ensures that, in decrypt_text() below, the encrypted text
    # "secret-encrypted" is interpreted as "secret".

# Generated at 2022-06-13 08:45:14.616291
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import tempfile
    import os
    import shutil
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.included_file import IncludedFile
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    # construct a fake parent playbook
    pb = Playbook()
    fake_included_file = IncludedFile(name='fake-included-file-1.yaml',
                                      path='/fake/path/to/main.yaml')
    pb._included_files.append(fake_included_file)

    # create a temporary directory and playbook for testing
    tmp_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 08:45:23.744812
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    play_ds = dict(
        hosts='all',
        roles=[dict(role='foo')]
    )
    templar = Templar(loader=None, variables=dict())

    # Create a dummy PlaybookInclude and load the data
    pi = PlaybookInclude()
    pi._load_data = lambda ds: ds
    ds = dict(
        import_playbook='bar.yml',
        vars=dict(
            tags='special'
        ),
        when=dict(
            test='{{ test_value }}'
        )
    )

    # Create a dummy Playbook

# Generated at 2022-06-13 08:45:28.827526
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    '''
    Unit test for method load_data of class PlaybookInclude
    '''
    test_obj = PlaybookInclude()
    test_obj.load_data = MagicMock(name='load_data')
    test_obj.load_data()



# Generated at 2022-06-13 08:45:37.864759
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Setup playbooks and roles path and test data
    pb_path = os.path.join(os.path.dirname(__file__),'../../unit/playbooks')
    r_path = os.path.join(os.path.dirname(__file__),'../../unit/roles')
    test_data = {
        'import_playbook': 'included_playbook.yml',
    }

    # Setup test class
    pi = PlaybookInclude()
    pi.load_data(ds=test_data, basedir=pb_path)

if __name__ == "__main__":
    test_PlaybookInclude_load_data()

# Generated at 2022-06-13 08:45:39.212972
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # TODO
    pass

# Generated at 2022-06-13 08:45:49.824344
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.parsing.yaml import objects
    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.task
    import sys
    import types
    import os

    sys.modules['ansible.playbook'] = types.ModuleType('ansible.playbook')
    sys.modules['ansible.playbook'].Playbook = ansible.playbook.Playbook
    sys.modules['ansible.playbook'].play = types.ModuleType('play')
    sys.modules['ansible.playbook'].play.Play = ansible.playbook.play.Play
    sys.modules['ansible.playbook'].task = types.ModuleType('task')
    sys.modules['ansible.playbook'].task.Task

# Generated at 2022-06-13 08:46:02.901472
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

    # initialize global variables
    pb_include = PlaybookInclude()
    pb_include._entries = []
    playbook = Playbook()
    playbook._entries = []
    play = Play()
    play._entries = []
    task = Task()
    task._attributes = {}
    block = Block()
    block._attributes = {}
    task_list = [task]
    block_list = [block]

    # initialize test varibales
    ds = {}
    basedir = "."
    variable_manager = None
    loader = None

    # populate ds

# Generated at 2022-06-13 08:46:14.346883
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.plugins.loader import callback_loader

    # create a new PlayContext object
    play_context = PlayContext()

    # create a simple playbook with two tasks
    yaml_data = '''
playbook:
  tasks:
    - name: sample
      debug:
        msg: sample
    - name: result
      debug:
        msg: result
'''
    # load the test playbook
    pb = PlaybookInclude.load(yaml_data, '', PlayContext())

    # create a simple playbook to include

# Generated at 2022-06-13 08:46:22.482717
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager

    ds = dict(
        import_playbook='playbook.yml',
        tags=['foo', 'bar', 'baz'],
        vars=dict(
            foo='bar',
            baz='quix',
        )
    )

    variable_manager = VariableManager()
    pb_inc = PlaybookInclude().load_data(ds, variable_manager=variable_manager)
    assert isinstance(pb_inc, Playbook)
    assert len(pb_inc._entries) == 1
    entry = pb_inc._entries[0]
   

# Generated at 2022-06-13 08:46:47.072683
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # import here to avoid a dependency loop
    from ansible.playbook.play import Play

    # set up test variables
    my_vars = dict(foo="bar")
    my_tags = ["baz", "qux"]

    # construct test object
    my_playbook_include = PlaybookInclude()
    my_playbook_include.import_playbook = 'test_playbook'
    my_playbook_include.vars = dict(my_vars)
    my_playbook_include.tags = my_tags

    # generate test data structure (ds)
    ds = dict(import_playbook='test_playbook',
              vars=my_vars)

    # create test Playbook() object

# Generated at 2022-06-13 08:47:00.139797
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    data = dict(
        import_playbook='rabbitmq.yml',
        when='rabbitmq_enabled',
        tags=['networking', 'rabbitmq']
    )

    # 1. Test with all parameters
    pb_include = PlaybookInclude()
    pb = pb_include.load_data(data, '.')

    assert pb_include.import_playbook == 'rabbitmq.yml'
    assert pb_include.when == ['rabbitmq_enabled']
    assert pb_include.tags == ['networking', 'rabbitmq']

    # 2. Test with only import_playbook parameter
    data = dict(
        import_playbook='rabbitmq.yml',
    )
    pb_include = PlaybookInclude()
   

# Generated at 2022-06-13 08:47:08.254908
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    pb = PlaybookInclude.load({'import_playbook': "test.yml", 'vars': {'a': 10, 'b': 20}})
    assert isinstance(pb, Playbook)
    assert pb.name == u'test.yml'
    assert len(pb._entries) == 1
    assert isinstance(pb._entries[0], Play)
    assert len(pb._entries[0].tasks) == 2


# Generated at 2022-06-13 08:47:09.189522
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:47:20.287447
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook_include import PlaybookInclude
    import os
    import sys
    import tempfile

    # mock the playbooks
    included_playbook = tempfile.mkstemp('-include-mock.yml')
    included_playbook_fd = os.fdopen(included_playbook[0], 'wb')
    included_playbook_fd.write(b'---\n- hosts: localhost\n  tasks:\n    - debug:\n        msg: included playbook\n')
    included_playbook_fd.close()
    included_playbook = included_playbook[1]

    playbook_include = tempfile.mkstemp('-playbook-include-mock.yml')
    playbook_include_fd = os.fdopen

# Generated at 2022-06-13 08:47:28.625626
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader

    # import here to avoid a dependency loop
    from ansible.playbook import Playbook

    p = PlaybookInclude()
    ds = {'import_playbook': './import_playbook.yml', 'vars': {'var1': 5, 'var2': 'test'}}

    # preprocess data
    ds = p.preprocess_data(ds)

    # load data
    p.load_data(ds, '/playbook_dir', None, DataLoader())

    # check results
    assert isinstance(p, Playbook)
    assert p.entries[0].vars['var1'] == 5
    assert p.entries[0].vars['var2'] == 'test'

# Generated at 2022-06-13 08:47:29.399528
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:47:32.242103
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    playbook = PlaybookInclude()

    assert playbook.load_data is not None



# Generated at 2022-06-13 08:47:46.598076
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    # define the fake path to be used to load the playbook
    fake_path = 'fake_path'
    fake_filename = 'fake_filename'
    fake_basedir = 'fake_basedir'
    fake_playbook_data = 'fake_playbook_data'

    # fake the playbook object to be returned by the method _load_playbook_data
    class FakePlaybook:
        _entries = [1,2,3]
        def _load_playbook_data(self, file_name, variable_manager, vars):
            assert fake_path == file_name
            assert fake_playbook_data == vars
            return self
    fake_playbook = FakePlaybook()

    # fake the loader object to be used

# Generated at 2022-06-13 08:47:54.247658
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from copy import copy

    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.reserved import Reserved
    v = VariableManager()
    v.extra_vars = {'foo': 'foo_value'}
    v.options_vars = {'foo': 'foo_options_value'}
    v.reserved = Reserved('foo')
    v.update_vars({'foo': 'foo_update_value'})

    # Create an instance of PlaybookInclude
    p = PlaybookInclude()

    # Create a basic playbook
    data = {
        '- import_playbook': 'playbook.yml'
    }


# Generated at 2022-06-13 08:48:24.008007
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    ds = dict(
        import_playbook='../../another_playbook.yaml',
        tags='httpd',
        vars=dict(foobar='bam')
    )
    variable_manager = None
    loader = None
    basedir = '/home/user/project/provisioning/roles'
    my_PBI = PlaybookInclude().load_data(ds, basedir, variable_manager, loader)
    assert type(my_PBI) == type('something')
    del ds['vars']
    ds['import_playbook'] = '../../another_playbook.yaml'
    my_PBI = PlaybookInclude().load_data(ds, basedir, variable_manager, loader)
    assert type(my_PBI) != type('something')


# Generated at 2022-06-13 08:48:34.352607
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import get_all_plugin_loaders, get_loader
    global display
    display = Display()

    # A fake host
    host = type('host', (), {})()
    host.name = 'host1'
    host.vars = {'my_var': 'value'}

    # A fake play
    play_context = PlayContext()
    play_context._hostvars = {host.name: host.vars.copy()}
    play_context.variable_manager = lambda: None
    play_context.variable_manager.get_vars = lambda: play_context._hostvars

    # A fake inventory
    inventory = type('inventory', (), {})()
    inventory.hosts = {host.name: host}


# Generated at 2022-06-13 08:48:39.853657
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    #  pb = PlaybookInclude().load_data(ds=data, basedir='/path/to/basedir', loader=loader)
    pass


# Generated at 2022-06-13 08:48:50.563572
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import shutil
    from ansible.module_utils._text import to_bytes
    from ansible.utils.path import unfrackpath
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    # Create temporary directory
    tmp_dir = os.path.realpath(unfrackpath("$TMPDIR/ansible_PlaybookInclude_load_data"))
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)

    os.mkdir(tmp_dir)
    cwd = os.getcwd()
    os.chdir(tmp_dir)

    # Create files

# Generated at 2022-06-13 08:48:58.632929
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    '''
    Unit test for method load_data of class PlaybookInclude
    '''
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.template import Templar

    base_dir = "../../../test/units/parsing/yaml/import_playbook/"
    if os.path.exists(base_dir):
        utils_dir = "../../../lib/ansible/utils/"
        if os.path.exists(utils_dir):
            utils_dir = os.path.abspath(utils_dir)
            if utils_dir not in sys.path:
                sys.path.append(utils_dir)
        import lookup_loader
        import test_loader
        import jin

# Generated at 2022-06-13 08:49:12.698532
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play

    def mock_display_deprecated(message):
        # don't fail on deprecated warnings
        pass

    def mock_get_collection_name_from_path(file_path):
        if file_path.startswith('collection://'):
            return 'mock.collection'
        return None

    def mock_get_collection_playbook_path(file_path):
        if file_path.startswith('collection://'):
            return ('mock.collection', 'playbook.yml', 'mock.collection')
        return None

    def mock_load(data, basedir, variable_manager=None, loader=None):
        return data

    basedir = 'test/ansible'

    variable_manager = None


# Generated at 2022-06-13 08:49:14.121806
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass



# Generated at 2022-06-13 08:49:29.613380
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    # simple play
    input_data = '''
- hosts: all
  name: test play
  tasks:
    - name: debug
      debug:
        msg: "hello"
'''
    pb = PlaybookInclude.load(input_data, basedir='.')
    assert len(pb._entries) == 1
    for e in pb._entries:
        assert isinstance(e, Play)
    assert e.get_name() == "test play"
    assert len(e.get_tasks()) == 1
    # simple play with tags

# Generated at 2022-06-13 08:49:30.476365
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:49:41.799350
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook

    incl = PlaybookInclude()
    incl.load_data(ds={}, basedir='')
    incl.load_data(ds={'import_playbook': 'common.yml'}, basedir='')
    incl.load_data(ds={'import_playbook': "common.yml"}, basedir='.')
    play = Play()
    play.load = lambda data, basedir: Play.load(None, None)
    play.load_data = lambda data: Play.load_data(None, None)
    pb = Playbook()
    pb.load = lambda data, basedir: Playbook.load(None, None)
    pb.load_data = lambda data: Playbook.load_

# Generated at 2022-06-13 08:50:23.317692
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook
    from ansible.parsing.splitter import parse_kv
    from ansible.utils.vars import combine_vars

    parser = PlaybookInclude()

    # with simple import_playbook
    data = {
        'import_playbook': 'test.yml'
    }
    pb = parser.load_data({}, '.', variable_manager=None, loader=None)._entries[0]
    assert type(pb) is Playbook
    assert len(pb._entries[0]._entries) == 1
    assert type(pb._entries[0]._entries[0]) is Play
    assert pb._entries[0]._entries[0].vars == {}

    # with parameter

# Generated at 2022-06-13 08:50:32.705719
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    import os
    import tempfile
    import shutil
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.play import Play
    from ansible.utils.collection_loader import AnsibleCollectionConfig

    # reset AnsibleCollectionConfig
    AnsibleCollectionConfig.reset()


# Generated at 2022-06-13 08:50:47.872719
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    from ansible.utils.collection_loader._collection_finder import AnsibleCollectionFinder

    pb = PlaybookInclude()

    # prepare a playbook to test
    test_playbook_path = os.path.join('test', 'units', 'library', 'playbook_include_playbook')
    test_playbook_file_name = os.path.join(test_playbook_path, 'playbook.yml')
    test_playbook_resource = (os.path.dirname(os.path.dirname(os.path.dirname(__file__))), test_playbook_path, None)
    test_playbook = Playbook()

    from ansible.utils.collection_loader import AnsibleCollectionConfig
    Ansible

# Generated at 2022-06-13 08:50:54.844605
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.yaml.objects import AnsibleMapping

    pb = PlaybookInclude.load({'import_playbook': '../../../../../../../stuff/import_playbook_test.yml'}, basedir='/etc/ansible/')

    assert isinstance(pb, Playbook)
    assert len(pb._entries) == 2
    assert pb._entries[0].name == 'first_play'
    assert pb._entries[1].name == 'second_play'
    assert isinstance(pb._entries[0], Play)
    assert isinstance(pb._entries[1], Play)

   

# Generated at 2022-06-13 08:50:59.045361
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook.play import Play

    basedir = "test/test_data"


# Generated at 2022-06-13 08:51:07.748009
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.module_utils._text import to_bytes
    from ansible.parsing.yaml.loader import AnsibleLoader

    path = os.path.join(os.path.dirname(__file__), "../../test_data/yaml")

    collection_paths = [
        os.path.join(path, 'test_collection_include')
    ]

    # test import
    AnsibleCollectionConfig.playbook_paths = collection_paths
    AnsibleCollectionConfig.default_collection = 'test_collection_include'


# Generated at 2022-06-13 08:51:19.351142
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.plugins
    ansible.plugins.lookup.squash_lookup = lambda *args, **kwargs: []

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.playbook.task import Task

    context = PlayContext()
    loader = DummyLoader()

    # play
    play_content = """
        - hosts: localhost
          import_playbook: myfile.yml
    """
    play = Play.load(play_content, variable_manager=None, loader=loader)

# Generated at 2022-06-13 08:51:22.330744
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # pylint: disable=unused-variable
    # pylint: disable=unused-argument
    # pylint: disable=redefined-outer-name
    pass

# Generated at 2022-06-13 08:51:24.785650
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    PlaybookInclude.load_data()


# Generated at 2022-06-13 08:51:26.856901
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play_context import PlayContext

    # TODO: add test
    pass




# Generated at 2022-06-13 08:41:52.647510
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.playbook.playbook_include
    playbook_include = ansible.playbook.playbook_include.PlaybookInclude()
    assert playbook_include.load_data(ds={}, basedir='') is not None
    playbook_include.load_data(ds={}, basedir='')


# Generated at 2022-06-13 08:41:53.342110
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # TODO: review this one
    pass

# Generated at 2022-06-13 08:41:53.791208
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:42:05.740988
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    playbook_include_data = AnsibleMapping({
        'include': 'file.yml',
        'vars': {
            'var1': 'value1',
            'var2': 'value2'
        }
    })
    playbook_include_obj = PlaybookInclude()
    playbook_include_obj.preprocess_data(playbook_include_data)
    assert playbook_include_obj.import_playbook == 'file.yml'
    assert playbook_include_obj.vars['var1'] == 'value1'
    assert playbook_include_obj.vars['var2'] == 'value2'

    playbook_include_data = AnsibleMapping({
        'import_playbook': 'file.yml'
    })
    playbook_include_obj = PlaybookInclude()
    playbook_include_obj

# Generated at 2022-06-13 08:42:14.787541
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook

    # empty playbook
    ds = '''
- hosts: all
  tasks:
  - debug: msg="hello"
  pre_tasks:
  - debug: msg="hello"
  roles:
  - myrole
    pre_tasks:
    - debug: msg="hello"
    tasks:
    - debug: msg="hello"
    post_tasks:
    - debug: msg="hello"
    handlers:
    - debug: msg="hello"
  post_tasks:
  - debug: msg="hello"
'''
    ds = PlaybookInclude.load([ds], ".", variable_manager=None, loader=None)
    assert isinstance(ds, Playbook)

# Generated at 2022-06-13 08:42:21.603726
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    test_PlaybookInclude = PlaybookInclude()
    test_data = '{"hosts": "local", "import_playbook": "/etc/ansible/roles/role1/tasks/main.yml", "vars": {}}'
    basedir = '/etc/ansible/test_playbooks'
    variable_manager = None
    loader = None
    assert test_PlaybookInclude.load_data(test_data, basedir, variable_manager, loader) == None


# Generated at 2022-06-13 08:42:29.549352
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    a = {
        'import_playbook': 'playbook.yml',
        'vars': {
            'k': 'v',
            'ansible_vault_pass': AnsibleVaultEncryptedUnicode(b'vault_password')
        },
        'tags': []
    }
    b = PlaybookInclude().load_data(ds=a, basedir='.', variable_manager=None, loader=None)
    assert len(b._entries) == 1

# Generated at 2022-06-13 08:42:40.898468
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    class AnsibleModuleFake:
        def __init__(self, argument_spec):
            self.params = argument_spec
            self.check_mode = False
    class VariableManagerFake:
        def set_inventory(self, inventory):
            pass
    class PlaybookIncludeFake(PlaybookInclude):
        def __init__(self):
            self.playbook_include = AnsibleModuleFake({})
            self.variable_manager = VariableManagerFake()
    playbook_include = PlaybookIncludeFake()
    playbook_include.load_data('/tmp/foo.yml', None)

# Generated at 2022-06-13 08:42:54.275306
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    pb = PlaybookInclude()

    data = {
        'include': 'playbook.yml',
        'vars': {
            'foo': 'bar'
        }
    }

    p = AnsibleBaseYAMLObject()
    p.ansible_pos = (1, 1)
    data['ansible_pos'] = (1, 1)

    playbook = pb.load_data(ds=data, basedir=".")

    assert isinstance(playbook, Playbook)
    assert isinstance(playbook._entries[0], Play)
    assert playbook.basedir == '.'
    assert playbook._entries[0].vars['foo'] == 'bar'
    assert playbook._entries[0]._in

# Generated at 2022-06-13 08:43:06.316521
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    import_playbook = PlaybookInclude(loader=None, variable_manager=None, loader_basedir=None)
    ds = AnsibleMapping(ansible_pos=dict())
    new_ds = AnsibleMapping(ansible_pos=dict())

    # Test import_playbook statement with a single string argument
    ds[C._ACTION_IMPORT_PLAYBOOK] = "a_string"
    import_playbook._preprocess_import(ds, new_ds, C._ACTION_IMPORT_PLAYBOOK, "a_string")
    assert dict(new_ds) == dict(import_playbook=u"a_string")

    # Test import_playbook statement with a single string argument and a single valid parameter
    ds[C._ACTION_IMPORT_PLAYBOOK] = "a_string --var1=123"

# Generated at 2022-06-13 08:43:17.581054
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # import here to avoid a dependency loop
    from ansible.playbook import Playbook

    # Create a variable_manager
    variable_manager = mock_variable_manager()

    # Create a loader
    loader = mock_loader()

    # Create a Playbook object that only contains a PlaybookInclude
    pb = Playbook(loader=loader)
    pb._entries.append(PlaybookInclude.load({u'import_playbook': u'playbook.yml'}, '.', variable_manager=variable_manager, loader=loader))

    # The PlaybookInclude should be a play on the Playbook (so it should
    # contain 1 entry)
    assert(len(pb._entries) == 1)

    # The Playbook should be a Playbook with a tasks list (so it should
    # have a 'tasks'

# Generated at 2022-06-13 08:43:29.994655
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # test setup
    import ansible.playbook.playbook
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role

    pc = ansible.playbook.playbook.PlayContext()
    options = ansible.playbook.playbook.PlaybookExecutorOptions()
    playbook = ansible.playbook.playbook.Playbook.load(path='test-playbook.yaml', variable_manager=None)

    # actual test
    ansible.playbook.playbook_include.PlaybookInclude.load(data=dict(import_playbook='test-playbook-2.yaml', tags=['include']), basedir='.', variable_manager=None, loader=None)

# Generated at 2022-06-13 08:43:38.678437
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # Arrange
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block

    from ansible.playbook.task import Task
    from ansible.playbook.role import Role

    from ansible.template import Templar

    class TestVarManager(object):

        def get_vars(self):
            return dict()

    class TestLoader(object):

        def __init__(self, basedir):
            self.basedir = basedir

    var_manager = TestVarManager()
    loader = TestLoader('.')
    templar = Templar(loader=loader, variables=var_manager.get_vars())

    # Verify playbook with deprectated parameters
    playbook = PlaybookInclude()

# Generated at 2022-06-13 08:43:39.487727
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:43:40.881535
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # TODO
    pass

# Generated at 2022-06-13 08:43:41.931164
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:43:49.182599
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.playbook
    playbook_include = ansible.playbook.playbook_include.PlaybookInclude()
    playbook_include._entries = 'entries'
    assert playbook_include._entries == 'entries'

    playbook_include._load_data('data', 'basedir', 'variable_manager', 'loader')
    assert playbook_include._entries == 'entries'

# Generated at 2022-06-13 08:43:53.610251
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.yaml.objects import AnsibleMapping
    ds = AnsibleMapping()
    ds.update({u'a.yml': ''})
    playbook_include = PlaybookInclude()
    from ansible.playbook import Playbook
    assert isinstance(playbook_include.load_data(ds, '', None), Playbook)

# Generated at 2022-06-13 08:44:02.049789
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.yaml.loader import AnsibleLoader

    host_data_1 = {"host1": {}, "host2": {}}
    host_data_2 = {"host2": {"remote_user": "test_user2"}, "host3": {"remote_user": "test_user3"}}
    host_data_3 = {"host4": {"remote_user": "test_user4"}, "host5": {"remote_user": "test_user5"}}


# Generated at 2022-06-13 08:44:11.294628
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role

    # Use the defaults (i.e. Ansible default settings and inventory)
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=["inventory.ini"])

# Generated at 2022-06-13 08:44:27.812424
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.role import Role
    from ansible.vars.manager import VariableManager

    test_data = dict(
        import_playbook='/tmp/test.yaml',
        vars=dict(
            ansible_connection='local',
            test_tasks=True,
        ),
        tags=['test'],
    )

    playbook_path = os.path.join(os.path.dirname(__file__), 'test_playbooks', 'test_include.yaml')

# Generated at 2022-06-13 08:44:34.127027
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pb = PlaybookInclude.load(data={u'import_playbook': u'../../tasks/main.yml'}, basedir='/root')
    assert pb.entries[0].included_path == os.path.normpath('/root/../../tasks')
    assert pb.entries[0]._ds[0]['task']['name'] == 'show info about container'

# Generated at 2022-06-13 08:44:34.763714
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:44:35.387516
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:44:37.136666
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # '''
    # Test for PlaybookInclude.load_data
    # '''
    pass


# Generated at 2022-06-13 08:44:37.972292
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:44:39.121553
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:44:49.441088
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

    # Create variable manager object
    variable_manager = DummyVars()

    # Create object of Playbook class
    playbook_include = PlaybookInclude()

    # Load ds with values of datastructure of include_playbook
    ds = dict(
        import_playbook='example.yml',
        vars=dict(var1='foo')
    )
    basedir = '/etc/ansible/'
    loader = DummyLoader()

    # Call load_data method of class PlaybookInclude with datastructure of import_playbook

# Generated at 2022-06-13 08:44:54.719199
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    new_obj = PlaybookInclude()
    new_obj.vars = {}
    new_obj.import_playbook = 'test.yml'
    assert isinstance(new_obj, PlaybookInclude)
    assert isinstance(new_obj.vars, dict)
    assert new_obj.import_playbook == 'test.yml'

# Generated at 2022-06-13 08:44:55.920002
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass



# Generated at 2022-06-13 08:45:21.629086
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    import yaml

    dataloader = DataLoader()
    templar = Templar(loader=dataloader)
    variable_manager = VariableManager()
    variable_manager._extra_vars = dict()

    ds = dict(tags=['tag1', 'tag2'], vars=dict(var1='value1'), import_playbook='imported_playbook.yml')
    ds_yaml = yaml.full_dump(ds)

    pi = PlaybookInclude.load(ds, '.')

# Generated at 2022-06-13 08:45:34.867561
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    test_context = PlayContext(variable_manager=VariableManager(loader=DataLoader()), inventory=InventoryManager(loader=DataLoader()))
    test_templar = Templar(loader=DataLoader())

    ds = {'import_playbook': 'test_collection.test_play.yml'}
    test_playbook_include = PlaybookInclude.load(ds, 'test_path', variable_manager=test_context.variable_manager, loader=test_context.loader)

# Generated at 2022-06-13 08:45:46.961831
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook, Play
    from ansible.playbook.play import Play
    import tempfile
    import os
    import sys
    import json
    if sys.version < '3':
        import io as StringIO
    else:
        import io
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    # Create fake data
    include_playbook = '''
    - import_playbook: included_playbook.yml
      hosts: included_hosts
      vars:
        var1: val1
        var2: val2
    '''


# Generated at 2022-06-13 08:45:55.489336
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # Test load_data (1)

    pb = PlaybookInclude()

    fake_loader = FakeLoader()
    fake_loader.get_basedir.return_value = '/path/to/playbooks'

    fake_ds = ansible.parsing.yaml.objects.AnsibleMapping()
    fake_ds['import_playbook'] = '../../../../../etc/passwd'

    res = pb.load_data(fake_ds, '/path/to/playbooks', loader=fake_loader)
    assert res == False

    # Test load_data (2)

    pb = PlaybookInclude()

    fake_loader = FakeLoader()
    fake_loader.get_basedir.return_value = '/path/to/playbooks'

    fake_ds = ansible.parsing.y

# Generated at 2022-06-13 08:46:08.266665
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    basedir = './tests/utils/collection_playbooks/'
    file_name = './tests/utils/collection_playbooks/ansible_collections/my_namespace/my_collection/playbook.yml'

    p1 = PlaybookInclude()
    p1.import_playbook = file_name
    p1.vars = {}

    res = p1.load_data(p1, basedir)

    assert isinstance(res, Playbook)
    assert len(res._entries) == 1

    p2 = next(iter(res._entries))

    assert isinstance(p2, Play)
    assert p2.name == 'my_play'



# Generated at 2022-06-13 08:46:11.803578
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    import sys
    sys.path.insert(0, "lib")

    PlaybookInclude.load_data(ds="task other_key=val", basedir="roles/foo", variable_manager=None, loader=None)

# Generated at 2022-06-13 08:46:20.829866
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # init vars
    playbook_include_object = PlaybookInclude()
    basedir = 'base_dir'
    dict_str = 'dict_str'

    # init mocks
    mock_import_playbook = MagicMock(return_value=True)
    mock_vars = MagicMock(return_value=True)
    mock_ds = MagicMock()
    mock_ds.import_playbook.return_value = mock_import_playbook()
    mock_ds.vars.return_value = mock_vars()

    # run test
    playbook_include_object.load_data(ds=mock_ds, basedir=basedir)

    # assert
    mock_ds.import_playbook.assert_called_once_with()
    mock_import_playbook.assert_called_once_

# Generated at 2022-06-13 08:46:32.830620
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.playbook_include import PlaybookInclude

    ds = dict(
        tasks = list(),
        import_playbook = 'test.yml',
        tags = list(),
        vars = dict()
    )

    o = PlaybookInclude.load(ds, None)
    assert isinstance(o.vars, dict)
    assert o.import_playbook == 'test.yml'

    #
    # This should fail and raise an exception.
    #
    ds = dict(
        tasks = list(),
        import_playbook = 'test.yml',
        tags = list(),
        vars = dict()
    )


# Generated at 2022-06-13 08:46:44.569082
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook

    os.environ['ANSIBLE_INVENTORY'] = "./test/inventory/test_inventory"

    import_playbook = PlaybookInclude()
    import_playbook.import_playbook = "./test/playbooks/import_playbook_test1.yml"

    playbook_obj = import_playbook.load_data(import_playbook, "./test/playbooks")
    assert isinstance(playbook_obj, Playbook)
    assert len(playbook_obj._entries) == 2
    assert isinstance(playbook_obj._entries[0], Play)
    assert isinstance(playbook_obj._entries[1], Play)

    # Also test that included variables are correctly set in the play

# Generated at 2022-06-13 08:46:57.834455
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook

    playbook = PlaybookInclude()
    _test_data = {
        'import_playbook': 'test2.yml',
        'vars': {
            'test_var': 'foo'
        }
    }

    result = playbook.load_data(_test_data, '.')
    assert isinstance(result, Playbook)
    assert len(result._entries) == 1
    assert result._entries[0]._included_path == '.'
    assert isinstance(result._entries[0], Play)
    assert result._entries[0].vars == {'test_var': 'foo'}



# Generated at 2022-06-13 08:47:48.123509
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    # Create data
    ds = dict(import_playbook='playbook.yml')
    basedir='/tmp'

    # Execute load_data
    pbi = PlaybookInclude()
    pb = pbi.load_data(ds, basedir)

    # Check result
    assert pb
    assert len(pb._entries) == 1

    # Check the result type and values of the first entry
    assert isinstance(pb._entries[0], Play)
    play = pb._entries[0]

    assert play.vars == dict()
    assert play.tags == []
    assert play.post

# Generated at 2022-06-13 08:48:01.479711
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.module_utils.six import StringIO
    from ansible.playbook.playbook import Playbook

    yaml_text = """
- host_one:
    vars:
        var_one: 'var_one'
        var_two: 'var_two'
    tasks:
    - ping:
- include: fake_playbook.yml
    vars:
        include_var_one: 'include_var_one'
        var_one: 'var_one_override'
        var_two: 'var_two_override'
- host_two:
    tasks:
    - ping:
- include: fake_playbook.yml
    vars:
        var_one: 'var_one_override_again'
        var_three: 'var_three'
"""

    playbook

# Generated at 2022-06-13 08:48:09.213095
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    import tempfile
    with tempfile.NamedTemporaryFile() as test_file:
        with open(test_file.name, 'w') as test_file_w:
            test_file_w.write('---\n- hosts: localhost\n  tasks:\n  - shell: echo test')
        pb_inc = PlaybookInclude()
        pb = pb_inc.load_data(ds = {'import_playbook': test_file.name}, basedir = '/')
        assert isinstance(pb, Playbook)
        assert len(pb._entries) == 1
        assert isinstance(pb._entries[0], Play)
        assert pb._entries[0].hosts == 'localhost'
       

# Generated at 2022-06-13 08:48:21.388902
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    import yaml
    with open('test_file.yml', 'r') as f:
        data = yaml.load(f)
    collection = PlaybookInclude.load(data=data, basedir='./')
    assert isinstance(collection, Play)
    assert collection.name == "test_play"
    assert isinstance(collection.tasks[0], Task)
    assert collection.tasks[0].name == "test task"
    assert collection.tasks[0].action == "test"
    os.remove('test_file.yml')

# Generated at 2022-06-13 08:48:22.777301
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass


# Generated at 2022-06-13 08:48:27.958098
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.parser import DataLoader

    loader = DataLoader()
    variable_manager = None

    play = PlaybookInclude()
    play.load_data(
        '''
        - import_playbook: test_playbook.yml
        ''', '/', variable_manager, loader
    )
    assert play.import_playbook == 'test_playbook.yml'

# Generated at 2022-06-13 08:48:36.619253
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    collection_name = 'ansible_collections.nsbl.playbook_test'
    import ansible_collections.nsbl.playbook_test # pylint: disable=unused-variable, import-error
    if not hasattr(ansible_collections, 'nsbl'):
        raise AnsibleParserError('Test collection is not installed')

    # simple
    playbook_include = PlaybookInclude.load(
        { 'import_playbook': 'simple.yml'},
        '.',
        None,
        None
    )
    assert len(playbook_include._entries) == 1
    assert playbook_include._entries[0].tags == []
    assert playbook_include._entries[0].vars == {}

    # tags

# Generated at 2022-06-13 08:48:48.556804
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import pytest
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml import objects
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    ds = AnsibleMapping()
    ds.update({'import_playbook': 'test_playbook.yml'})
    ds.update({'tags': 'tags_test'})
    ansible_loader = AnsibleLoader(ds, None, variable_manager=VariableManager())
    playbook_include = PlaybookInclude.load(ansible_loader, None, None, None)
    assert playbook_include.import_playbook

# Generated at 2022-06-13 08:48:56.182017
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import datetime
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook

    ds = AnsibleMapping()
    ds['hosts'] = 'host1,host2'
    ds['vars'] = {'all': {'k1': 'v1'}}
    ds['tasks'] = [
        AnsibleMapping({'block': [
            AnsibleMapping({'task': AnsibleMapping({'local_action': 'setup', 'register': 'setup_result'})}),
            AnsibleMapping({'rescue': []}),
            AnsibleMapping({'always': []})
        ]})
    ]

    pi = PlaybookInclude()
    pi._load_playbook_data(ds)


# Generated at 2022-06-13 08:49:07.117349
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.playbook
    import ansible.playbook.play
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_inventory(InventoryManager(loader=loader, sources=[]))

    # ds is the data structure to be tested
    ds = dict(
        include='../../../examples/ansible.cfg',
        tags=['mytag'],
    )

    # call the tested method
    new_obj = PlaybookInclude.load(data=ds, basedir='../../../examples',
        variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 08:49:36.684565
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:49:49.247074
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play

    class MockPlay(Play):
        def __init__(self, roles):
            self._roles = roles

        def roles(self):
            return self._roles

    inc = PlaybookInclude()
    inc.load_data(
        dict(
            import_playbook='coll1.example.play',
            vars=dict(a=1, b=2),
            tags=[]
        ), basedir='/base', variable_manager=None, loader=None
    )

    inc.load_data(
        dict(
            import_playbook='coll2.foo.play',
            vars=dict(a=1, b=2),
            tags=[]
        ), basedir='/base', variable_manager=None, loader=None
    )


# Generated at 2022-06-13 08:49:50.256184
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass



# Generated at 2022-06-13 08:49:58.451038
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.playbook import Playbook

    data = dict(
        import_playbook="test.yml",
        vars=dict(
            a=1,
            b=2
        )
    )

    obj = PlaybookInclude.load(data)

    assert obj.import_playbook == "test.yml"
    assert obj.vars == dict(
        a=1,
        b=2
    )



# Generated at 2022-06-13 08:50:00.415863
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass
    # FIXME: Unit test not yet implemented


# Generated at 2022-06-13 08:50:01.656237
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    """
    Unit test for method load_data of class PlaybookInclude
    """
    pass

# Generated at 2022-06-13 08:50:02.842517
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass



# Generated at 2022-06-13 08:50:14.259743
# Unit test for method load_data of class PlaybookInclude

# Generated at 2022-06-13 08:50:26.346009
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleError

    filename = 'playbook_include.yaml'
    test_playbook_include_obj = PlaybookInclude()

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager.set_inventory(inventory)

    try:
        playbook_include_obj = test_playbook_include_obj.load(filename, loader=loader, variable_manager=variable_manager)
    except AnsibleError as e:
        print(e)

    # Check for imported playbook variable

# Generated at 2022-06-13 08:50:27.310716
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass
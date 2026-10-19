

# Generated at 2022-06-13 08:41:55.692012
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    pbi = PlaybookInclude()
    import yaml
    yaml_str = '''
- import_playbook: file1
- import_playbook: file2 vars:
    a: 1
    b: 2
- import_playbook: file3
- import_playbook: file4 vars:
    a: 1
    b: 2
- import_playbook: file5
'''
    yaml_obj = yaml.load(yaml_str)
    data = pbi.preprocess_data(yaml_obj)
    assert data[0]['import_playbook'] == 'file1'
    assert data[1]['import_playbook'] == 'file2'
    assert data[1]['vars']['a'] == 1
    assert data[1]['vars']['b']

# Generated at 2022-06-13 08:42:08.768737
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    pb_include = PlaybookInclude()
    pb_include.preprocess_data({'import_playbook': './test_dir/test.yml', 'vars': {'a': 1}, 'tags': ['a','b']})
    assert pb_include.tags == ['a','b']
    assert pb_include.import_playbook == './test_dir/test.yml'
    assert pb_include.vars == {'a':1}

    pb_include.preprocess_data({'import_playbook': './test_dir/test.yml', 'vars': {'a': 2}, 'tags': 'c'})
    assert pb_include.tags == ['c']
    assert pb_include.import_playbook == './test_dir/test.yml'


# Generated at 2022-06-13 08:42:16.229606
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # given
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.role import Role
    from ansible.vars.manager import VariableManager
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.errors import AnsibleParserError
    from ansible.galaxy.requirement import GalaxyRequirement
    from io import StringIO
    from ansible.executor.task_queue_manager import TaskQueueManager

    fake_loader = None

# Generated at 2022-06-13 08:42:24.595182
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    basedir = '.'
    variable_manager = None
    loader = None

    pb = PlaybookInclude()
    pb.import_playbook = 'test_play.yml'
    pb.vars['foo'] = 'bar'

    pb_ret = pb.load_data(pb, basedir, variable_manager, loader)

    assert isinstance(pb_ret, Playbook)

    p_ret = pb_ret._entries[0]
    assert isinstance(p_ret, Play)
    assert p_ret.vars['foo'] == 'bar'

# Generated at 2022-06-13 08:42:32.817212
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Test that PlaybookInclude.load_data() returns a Playbook object
    import os
    import tempfile

    from ansible.playbook.play import Play

    # create a temporary directory to store the includes
    file_dir = tempfile.mkdtemp()

    # create an empty PlaybookInclude object
    obj = PlaybookInclude()

    # create a main playbook and a sub-playbook
    # the main playbook contains a single task that stops
    # the sub-playbook contains a single task that starts
    main_playbook = tempfile.NamedTemporaryFile(mode='w', delete=False, prefix='main_playbook_')
    sub_playbook = tempfile.NamedTemporaryFile(mode='w', delete=False, prefix='sub_playbook_')

    # create a main playbook
    main_playbook

# Generated at 2022-06-13 08:42:47.515821
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    playbook_include = PlaybookInclude()
    result = playbook_include.preprocess_data({})
    assert result == {}, "PlaybookInclude.preprocess_data({}) == {}"

    result = playbook_include.preprocess_data({'a': 1, 'b': 2})
    assert result == {'a': 1, 'b': 2}, "PlaybookInclude.preprocess_data({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}"

    result = playbook_include.preprocess_data({'import_playbook': 'playbook.yml'})

# Generated at 2022-06-13 08:43:02.005014
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.playbook.task_include import TaskInclude

    # Test the dict form
    playbook_include = PlaybookInclude()
    ds = AnsibleMapping({"_ansible_ignore_errors": True, "import_playbook": "test.yml bar=test1 foo=test2", "tags": ["foo", "bar"], "when": "true"})
    ds = playbook_include.preprocess_data(ds)

    assert isinstance(ds, AnsibleMapping), "ds should be a AnsibleMapping object"
    assert ds["import_playbook"] == "test.yml", "import_playbook should be test.yml"

# Generated at 2022-06-13 08:43:11.591086
# Unit test for method load_data of class PlaybookInclude

# Generated at 2022-06-13 08:43:12.400281
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    pass

# Generated at 2022-06-13 08:43:23.406906
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.playbook.playbook import Playbook
    from ansible.plugins.loader import add_all_plugin_dirs

    add_all_plugin_dirs()
    p = Playbook.load('test/ansible_collections/testns/testcoll/test_playbook.yml')
    i = p._entries[0]
    assert isinstance(i, PlaybookInclude)

    i = PlaybookInclude(vars={'magic': 'someval'})
    d = i.preprocess_data({'import_playbook': 'test/ansible_collections/testns/testcoll/test_playbook.yml', 'tags': 'foo,bar'})

# Generated at 2022-06-13 08:43:37.254110
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.playbook.play as Play
    import ansible.playbook.task as Task
    import ansible.playbook.block as Block
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.utils.collection_loader import AnsibleCollectionConfig

    # set default namespace
    AnsibleCollectionConfig.default_namespace = 'my.namespace'


# Generated at 2022-06-13 08:43:51.747474
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    b = dict(
        import_playbook='/tmp/dummy.yml',
    )

    plb = PlaybookInclude(basedir='/home/user/ansible', variable_manager=VariableManager(), loader=None)
    plb._load_playbook_data(file_name='/home/user/ansible/tmp/dummy.yml', variable_manager=None, vars=None)

    assert isinstance(plb, PlaybookInclude)
    assert isinstance(plb.load_data(b, '/home/user/ansible', variable_manager=None, loader=None), Playbook)


# Generated at 2022-06-13 08:43:53.120829
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:44:01.000992
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader

    basedir = os.getcwd()
    templar = Templar(loader=DataLoader())
    dir_name = os.path.join(basedir, 'playbooks')

    # Test conditional playbook
    ds = dict(
        import_playbook="test-playbook.yml",
        when=["foo == 'bar'"]
    )
    pbi = PlaybookInclude()
    pbi._load_data(ds, templar=templar, basedir=dir_name)
    assert pbi._import_playbook == "test-playbook.yml"
    assert pbi._conditional == "foo == 'bar'"

    # Test conditional playbook with params

# Generated at 2022-06-13 08:44:09.064184
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook

    playbook_include = PlaybookInclude(import_playbook="included_playbook.yaml", tags='tag1,tag2')

    class LoadedPlaybook(object):
        tags = ['tag3']

    # mocks

# Generated at 2022-06-13 08:44:09.971786
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # TODO: add unit test
    pass

# Generated at 2022-06-13 08:44:20.933661
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    try:
        from unittest import mock
        from unittest.mock import MagicMock
    except ImportError:
        import mock
        from mock import MagicMock
    from ansible.playbook import Playbook

    m = mock.mock_open()
    with mock.patch("ansible.parsing.dataloader.DataLoader.load_from_file", m):
        try:
            from __main__ import display
        except ImportError:
            from ansible.utils.display import Display
            display = Display()

        basedir = "tests/playbooks"
        ds = dict(
            import_playbook = "include.yaml"
        )

# Generated at 2022-06-13 08:44:25.577532
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play

    data = {'import_playbook': 'main.yml'}
    pb = PlaybookInclude.load(data, '.')
    assert isinstance(pb, PlaybookInclude)
    assert pb.import_playbook == 'main.yml'

    new_pb = pb.load_data(pb, '.')
    assert isinstance(new_pb, Playbook)
    assert new_pb.file_name == 'main.yml'
    assert len(new_pb._entries) == 1
    assert isinstance(new_pb._entries[0], Play)

# Generated at 2022-06-13 08:44:37.324182
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Arguments
    ds = AnsibleMapping()
    ds['import_playbook'] = '/path/to/hello.yaml'
    ds[0] = AnsibleBaseYAMLObject()
    ds[0].ansible_pos = 'asdf'
    basedir = '/root'
    variable_manager = AnsibleMapping()
    variable_manager['vars'] = AnsibleMapping()
    variable_manager['vars']['to'] = 'hi'
    variable_manager['vars']['dummy'] = 'dummy'
    variable_manager['_extra_vars'] = AnsibleMapping()
    variable_manager['_extra_vars']['to'] = 'hi'
    loader = AnsibleMapping()
    loader['_basedir'] = '/root'

    #

# Generated at 2022-06-13 08:44:48.960869
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.constants as C
    import ansible.playbook as playbook
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.vars.manager import VariableManager

    task_ds = AnsibleMapping()
    task_ds['import_playbook'] = '../../my_collections/my_ns/my_coll/tasks/main.yml'
    task_ds['vars'] = dict(name='sample', age=21)

    basedir = C.DEFAULT_PLAYBOOK_PATH[0]
    variable_manager = VariableManager()
    playbook_include = playbook.PlaybookInclude()

    playbook = playbook_include.load_data(task_ds, basedir, variable_manager)

    #

# Generated at 2022-06-13 08:45:14.091342
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook.play import Play
    from ansible.playbook.role import Role

    # Run the test case
    #
    # Create the playbook include
    playbook_include = PlaybookInclude()
    playbook_include.import_playbook = "include.yml"
    playbook_include.tags = ['some_tag']
    playbook_include.vars = {'some_var': 123}

    # Create the playbooks
    from ansible.playbook.playbook import Playbook
    playbook = Playbook()
    role_playbook = Playbook()

    # Create the plays
    play = Play()
    role_play = Play()

    # Populate the include.yml playbook
    playbook._entries.append(play)

    # Create the roles
    role = Role()
    role_role = Role()



# Generated at 2022-06-13 08:45:23.381049
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # TODO: Improve these tests
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    pb = Playbook()

    # Test basic functionality
    import_playbook = "test/test_playbook/import_playbook_test_playbook.yml"
    playbook_obj = PlaybookInclude("import_playbook=" + import_playbook)
    assert isinstance(playbook_obj.load_data(playbook_obj.dump_data(), playbook=pb), Playbook)

    # Test the when option
    playbook_obj = PlaybookInclude("import_playbook=" + import_playbook + " when: test_condition")
    pb = playbook_obj.load_data(playbook_obj.dump_data(), playbook=pb)
    assert len(pb.get_plays())

# Generated at 2022-06-13 08:45:36.061170
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play

    options = namedtuple('Options', ['listtags', 'listtasks', 'listhosts', 'syntax',
                                     'connection','module_path', 'forks', 'remote_user',
                                     'private_key_file', 'ssh_common_args', 'ssh_extra_args',
                                     'sftp_extra_args', 'scp_extra_args', 'become',
                                     'become_method', 'become_user', 'verbosity', 'check'])

# Generated at 2022-06-13 08:45:48.082679
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.handler import Handler
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.become import Become

    pb = PlaybookInclude()
    pb.load_data({'import_playbook': 'playbook.yml'})
    assert pb.import_playbook == 'playbook.yml'

    pb = PlaybookInclude()
    pb.load_data({'import_playbook': 'playbook.yml', 'vars': {'foo': 'bar'}})

# Generated at 2022-06-13 08:45:52.768828
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # import here to avoid a dependency loop
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude

    # PlaybookInclude object
    obj = PlaybookInclude()
    assert obj.load_data('import_playbook: playbook.yml')
    assert obj.import_playbook == 'playbook.yml'
    assert obj.vars == {}
    assert obj.load_data('import_playbook: playbook.yml vars: { var1: "value" }')
    assert obj.import_playbook == 'playbook.yml'
    assert obj.vars == { 'var1': "value" }

# Generated at 2022-06-13 08:46:01.823593
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.parsing.dataloader import DataLoader

    dl = DataLoader()
    pb = PlaybookInclude.load(data={'import_playbook': 'test_playbook.yml', 'vars': {'var1': 'value1', 'var2': 'value2'}},
                              basedir='/', variable_manager=None, loader=dl)
    assert isinstance(pb, Playbook)

# Generated at 2022-06-13 08:46:13.816537
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play

    result = PlaybookInclude.load({}, 'foo')
    assert type(result) is PlaybookInclude
    result = PlaybookInclude.load({'import_playbook': 'foo'}, 'foo')
    assert type(result) is PlaybookInclude
    result = PlaybookInclude.load({'import_playbook': 'foo:bar'}, 'foo')
    assert type(result) is PlaybookInclude
    result = PlaybookInclude.load({'include': 'bar'}, 'foo')
    assert type(result) is PlaybookInclude
    result = PlaybookInclude.load({'import_playbook': 'foo', 'when': 'foo'}, 'foo')
    assert type(result) is PlaybookInclude

# Generated at 2022-06-13 08:46:22.334022
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.parsing.yaml.loader import AnsibleLoader
    import ansible.parsing.yaml.objects

    # initilaize loader
    loader = AnsibleLoader(None, None)

    # empty dict for variable manager
    variable_manager = {}

    # set data for playbook
    data = {'import_playbook': 'test.yml'}

    # set basedir
    basedir = '.'

    # initialize PlaybookInclude
    my_playbook_include = PlaybookInclude.load(data, basedir, variable_manager, loader)

    # check that PlaybookInclude is instance of Playbook
    assert isinstance(my_playbook_include, Playbook)

    # initialize new Playbook


# Generated at 2022-06-13 08:46:33.622692
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader

    display.verbosity = 3

    # Test when no playbook to include is defined
    obj = PlaybookInclude()
    playbook_include = obj.load(ds="", basedir="/tmp/", 
        variable_manager=None, loader=DataLoader())
    # Should return a PlaybookInclude object
    assert(isinstance(playbook_include, PlaybookInclude)) 
    # Should have no entries
    assert(playbook_include._entries == []) 

    # Test when a playbook to include is defined (vars not set)
    obj = PlaybookInclude()
    playbook_include = obj.load(ds="test.yml", basedir="/tmp/", 
        variable_manager=None, loader=DataLoader())

# Generated at 2022-06-13 08:46:45.108515
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Test no import_playbook provided
    try:
        PlaybookInclude.load(data=dict(), basedir='')
    except AnsibleAssertionError as e:
        if 'ds () should be a dict but was a' not in "".join(e.args):
            raise

    # Test import_playbook is not a dict
    try:
        PlaybookInclude.load(data='test', basedir='')
    except AnsibleAssertionError as e:
        if 'ds (test) should be a dict but was a' not in "".join(e.args):
            raise

    # Test invalid value of variable_manager

# Generated at 2022-06-13 08:47:00.118011
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.plugins.loader import action_loader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    import tempfile
    import sys
    import os

    AnsibleCollectionConfig.clear_collection_paths()

    # create temporary playbook directory
    temp_dir = tempfile.mkdtemp()

    # create temporary playbook file
    playbook = temp_dir + '/test_play.yml'
    playbook_file = open(playbook, 'w')
    playbook_file.write('- hosts: localhost\n')
    playbook_file.write('  tasks:\n')
    playbook_

# Generated at 2022-06-13 08:47:12.233787
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    try:
        PlaybookInclude.load({}, '.')
    except AnsibleParserError as e:
        assert str(e) == 'playbook import parameter is missing'
    else:
        raise AssertionError('AnsibleParserError not raised')

    try:
        PlaybookInclude.load({'import_playbook': 'x'}, '.')
    except AnsibleParserError as e:
        assert str(e) == 'vars for import_playbook statements must be specified as a dictionary'
    else:
        raise AssertionError('AnsibleParserError not raised')


# Generated at 2022-06-13 08:47:16.493520
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.utils.collection_loader
    assert ansible.utils.collection_loader.__name__ == 'ansible.utils.collection_loader'

    PlaybookInclude.load_data(None, basedir=None)


# Generated at 2022-06-13 08:47:26.042415
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook

    playbook_include = PlaybookInclude()
    playbook_include.import_playbook = 'fake_playbook_path'
    playbook_include.vars = {'key1': 'value1', 'key2': 'value2'}
    playbook_include.tags = ['tag1', 'tag2']

    playbook = Playbook()
    playbook._load_playbook_data(file_name='fake_playbook_path', variable_manager=None, vars=playbook_include.vars)
    assert playbook == playbook_include.load_data(ds=None, basedir=None, variable_manager=None, loader=None)

# Generated at 2022-06-13 08:47:39.346126
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.vars.unsafe_proxy import UnsafeProxy

    obj = PlaybookInclude()

    # set dummy values for debug output
    obj.__dict__['_ds'] = {'import_playbook': 1}
    obj.__dict__['_basedir'] = 2
    obj.__dict__['_variable_manager'] = 3
    obj.__dict__['_loader'] = 4

    # test correct play (not FQCN)
    dirc = os.path.join(os.path.dirname(__file__), 'playbooks')
    play = 'playbook_include.yml'
    basedir = dirc
    variable_manager = None
    loader = None

# Generated at 2022-06-13 08:47:40.181177
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:47:50.596388
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.plugins.loader as plugins_loader
    from ansible.utils.collection_loader import AnsibleCollectionLoader

    os.environ["ANSIBLE_COLLECTIONS_PATHS"] = os.path.join(os.path.dirname(__file__), "../data/collection_loader/")
    collection_loader = AnsibleCollectionLoader()

    # create the mock loader object
    fake_loader = plugins_loader.PluginLoader(
        '',
        '',
        '',
        '',
        '',
        '',
        collection_loader=collection_loader,
    )

    # test with collection playbook
    playbook_path = "my_col.my_ns.import_playbook.yml"

# Generated at 2022-06-13 08:48:04.108432
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os

    # Required parameters
    params = dict(import_playbook="test.yml")

    # Instantiate
    pbi = PlaybookInclude()

    # Execute on the good parameters
    pb = pbi.load_data(params, ".")

    # Execute without a playbook
    params.pop("import_playbook")
    try:
        pb = pbi.load_data(params, ".")
        assert False
    except AssertionError:
        pass

    # Execute with a playbook that does not exist
    params["import_playbook"] = "idontexist.yml"
    try:
        pb = pbi.load_data(params, ".")
        assert False
    except AnsibleParserError:
        pass

    # Execute with a playbook that does exist

# Generated at 2022-06-13 08:48:15.986613
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook

    display.verbosity = 0
    p1 = Play()
    p1._load_data({'hosts': 'all', 'roles': [{'name': 'role1'}]}, play=p1)
    p2 = Play()
    p2._load_data({'hosts': 'all', 'roles': [{'name': 'role2'}]}, play=p2)
    p3 = Play()
    p3._load_data({'hosts': 'all', 'roles': [{'name': 'role3'}]}, play=p3)

    pb1 = Playbook()
    pb1._entries = [p1, p2]

    pb2 = Playbook()
    p

# Generated at 2022-06-13 08:48:27.254245
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # pylint: disable=too-many-locals
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task, TaskInclude
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.block import Block
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    data = {'import_playbook': 'playbook/playbook.yml', 'tags': ['tag1', 'tag2'], 'vars': {'var1': 'value1'}}
    basedir = '.'
    variable_manager = VariableManager()
    loader = 'dummy_loader'


# Generated at 2022-06-13 08:48:48.297374
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    '''
    Test PlaybookInclude.load_data method
    '''
    class fake_loader():
        def __init__(self, data):
            self.data = data

    class fake_var_mgr():
        def __init__(self, vars):
            self.data = vars

        def get_vars(self):
            return self.data

    d = dict(import_playbook="./fake_playbook.yml", tags=['tag1', 'tag2'], vars={'var1': 'val1', 'var2': 'val2'})
    d_exp = AnsibleMapping(import_playbook="./fake_playbook.yml", tags=['tag1', 'tag2'], vars={'var1': 'val1', 'var2': 'val2'})

# Generated at 2022-06-13 08:48:56.008614
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    playbook_include = PlaybookInclude()
    playbook_include.name = 'test_load_data'
    playbook_include.import_playbook = 'test_load_data.yaml'
    playbook_include.when = 'test_when'
    playbook_include.tags = 'test_tags'
    playbook_include.vars = {'test_var':'test_value'}

    playbook = playbook_include.load_data(ds=playbook_include.serialize(), basedir='.', variable_manager=None, loader=None)
    assert isinstance(playbook, Playbook)
    assert playbook.name == playbook_include.name
    assert playbook._entries
    for entry in playbook._entries:
        assert isinstance

# Generated at 2022-06-13 08:48:56.791340
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass



# Generated at 2022-06-13 08:49:11.618881
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Play
    from ansible.playbook.play import Playbook
    from ansible.template import Templar

    loader = None
    variable_manager = None
    templar = Templar(loader=loader, variables=variable_manager)
    basedir = os.path.join(os.getcwd(), "tests/unit/playbook/include_playbook")
    yaml_doc = list()
    yaml_doc.append({"import_playbook": "playbooks/playbook1.yaml", "vars": {"hostvars": {"host1": {"hostvar1": "host1value1", "hostvar2": "host1value2"}}}})

# Generated at 2022-06-13 08:49:18.345524
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # import here to avoid a dependency loop
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude

    pb = PlaybookInclude()
    basedir = os.getcwd()
    data = dict(
        import_playbook="a_playbook.yml",
        vars=dict(
            a_key="a_value",
        )
    )

    # This is the expected data from running pb.preprocess_data,
    # since the load_data method runs that to clean up the data first

# Generated at 2022-06-13 08:49:30.799685
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play

    pb = PlaybookInclude()
    pb._import_playbook = "./test_playbooks/include_play.yml"
    pb_object = pb.load_data(pb, basedir=".")
    assert pb_object.entries[0].name == "This is an import test", "Name in first entry should match."
    assert pb_object.entries[0].vars == {'key': 'value'}, "Vars in first entry should match."
    assert isinstance(pb_object.entries[0], Play), "First entry should be a play."


# Generated at 2022-06-13 08:49:37.563809
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook.play import Play

    from ansible.playbook.task_include import TaskInclude

    # load_data for PlaybookInclude should return a correctly instantiated Playbook
    # object
    data = dict(
        import_playbook='test_playbook_include_load_data.yaml',
        tags=['tag1', 'tag2']
    )

    basedir = os.path.abspath(os.path.dirname(__file__) + '/../../')
    pb = PlaybookInclude.load(data, basedir=basedir)

    assert pb.__class__.__name__ == 'Playbook'
    assert len(pb._entries) == 2

    # both entries in the included playbook should be Plays

# Generated at 2022-06-13 08:49:42.785689
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    playbook_include = PlaybookInclude.load(data={'include': 'hello_world.yml'}, basedir='.')
    assert playbook_include is not None
    assert playbook_include.import_playbook == 'hello_world.yml'


# Generated at 2022-06-13 08:49:43.477335
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:49:55.285840
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook import Playbook

    parser = PlaybookInclude()

    # valid .load_data call
    playbook_data = {'import_playbook':'file.yml'}
    playbook_include = parser.preprocess_data(playbook_data)
    playbook_include_2 = parser.load_data(ds=playbook_include, basedir='.')
    assert isinstance(playbook_include_2, Playbook)

    # Invalid call, not a dict
    playbook_data = 'import_playbook:file.yml'
    playbook_include = parser.preprocess_data(playbook_data)
    try:
        playbook_include_2 = parser.load_data(ds=playbook_include, basedir='.')
    except AssertionError:
        pass

# Generated at 2022-06-13 08:50:29.303774
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars
    from ansible.utils.collection_loader._collection_finder import _get_collection_name_from_path
    import os
    import os.path
    import tempfile
    import unittest

    # Create a temporary directory
    tmp_dir = tempfile.mkdtemp()
    playbook_path = os.path.join(tmp_dir, 'playbook.yaml')

    # Create the playbook
    playbook = Playbook()

# Generated at 2022-06-13 08:50:40.417303
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import stat
    from ansible.errors import AnsibleParserError
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.collection_loader._collection_finder import _get_collection_name_from_path, _get_collection_playbook_path
    from ansible.utils.collection_loader import AnsibleCollectionConfig

    data_loader = DataLoader()
    basedir = os.getcwd()
    variable_manager = None
    loader = None

    #
    # test: load with no arguments
    #
    try:
        PlaybookInclude.load(data=None, basedir=basedir, variable_manager=variable_manager, loader=data_loader)
    except AnsibleParserError as e:
        assert e.message == 'import_playbook parameter is missing'



# Generated at 2022-06-13 08:50:40.965376
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:50:50.665311
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    # :mkhl test:
    # Initialize a PlaybookInclude object
    pbi = PlaybookInclude()
    assert pbi
    # Initialize a VariableManager object
    vm = ansible.utils.plugins.loader.VariableManager()
    assert vm
    # Initialize a playbook object
    playbook = ansible.playbook.playbook.Playbook(loader=ansible.parsing.dataloader.DataLoader(), variable_manager=vm)
    assert playbook
    # PlaybookInclude.load_data is supposed to return a new Playbook() object

# Generated at 2022-06-13 08:51:03.605154
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    ds = {
      'import_playbook': "./included-playbook.yml",
      'vars': {
        'myvar': 'myvalue'
      }
    }
    basedir = "./"
    variable_manager = None
    loader = None
    playbook_include = PlaybookInclude()
    pb = playbook_include.load_data(ds, basedir, variable_manager, loader)
    assert isinstance(pb, Playbook)
    assert len(pb._entries) == 1
    assert isinstance(pb._entries[0], Play)
    assert pb._entries[0].vars['myvar'] == 'myvalue'

# Generated at 2022-06-13 08:51:16.365208
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.module_utils.six.moves import StringIO
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.parsing.yaml.objects import AnsibleSequence

    file_name = os.path.join(os.path.dirname(__file__), 'ansible_module_meta_template.retry')
    try:
        stream = open(file_name)
    except IOError as e:
        print("Error: Unable to open '%s', (%s)" % (file_name, str(e)))
        raise Exception()

    yaml_text = "".join(stream.readlines())
    yaml_

# Generated at 2022-06-13 08:51:17.197539
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:51:24.775744
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    import os
    import unittest

    class TestPlaybookInclude(unittest.TestCase):

        def setUp(self):
            self.loader = DataLoader()
            self.variable_manager = VariableManager()
            self.inventory = InventoryManager(loader=self.loader, sources=[])

        def tearDown(self):
            del self.loader
            del self.variable_manager
            del self.inventory

        # a rudimentary test to verify that the load works correctly

# Generated at 2022-06-13 08:51:39.420760
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

    # Test case 1 - playbook import_playbook with vars
    # Test playbookInclude.load_data() to load import_playbook with vars
    loader = DataLoader()
    variable_manager = VariableManager()
    path = './tests/unit/playbook/test_import_playbook/import_playbook_1.yml'
    playbook_data = loader.load_from_file(path)

    playbookInclude = PlaybookInclude()
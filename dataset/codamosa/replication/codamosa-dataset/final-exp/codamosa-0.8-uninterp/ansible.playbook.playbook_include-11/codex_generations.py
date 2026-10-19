

# Generated at 2022-06-13 08:41:54.390538
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.template import Templar

    basedir = '/some/dir'
    data = {'import_playbook': 'some_playbook.yml'}

    pb = PlaybookInclude.load(data, basedir)
    assert isinstance(pb, Play)
    assert pb.name == 'some_playbook'
    assert pb._entries == []
    assert pb.vars == {}

    templar = Templar(loader=None, variables={'some_var': 'foo'})
    templar.basedir = basedir

    pb = PlaybookInclude.load(dict(data, tags=['some_tag']), templar.basedir, templar)

# Generated at 2022-06-13 08:42:07.015137
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    '''
    Test PlaybookInclude._load_data method
    '''

    from ansible.utils.collection_loader import AnsibleCollectionConfig

    # Test for a path with no directories
    ds = "filename.yml"
    basedir = ""
    new_obj = PlaybookInclude()._load_data(ds, basedir)
    assert 'filename.yml' == new_obj._import_playbook

    # Test for a path with directories
    ds = "test/test_files/test_file.yml"
    basedir = ""
    new_obj = PlaybookInclude()._load_data(ds, basedir)
    assert 'test/test_files/test_file.yml' == new_obj._import_playbook

    # Test for a relative path with directories

# Generated at 2022-06-13 08:42:07.687139
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:42:17.809954
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Simulate a loading on a host to test the method
    from ansible.playbook import Playbook
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.options import Options
    # Options for playbook
    options = Options()
    options.connection = 'local'
    options.module_path = 'library'
    options.forks = 1
    options.become = False
    options.become_method = 'sudo'
    options.become_user = 'root'
    options.check = False
    options.listhosts = None
    options.listtasks = None
    options.listtags = None
    options.syntax = None
    options.step = None
    options.start_at_task

# Generated at 2022-06-13 08:42:27.019345
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    
    playbook_content = """
    - hosts: all
      vars:
        test1: "val1"
      tasks:
        - name: testplay
          import_playbook: "/tests/test1.yml"
          vars:
            test2: "val2"
            test3: "val3"
    """

    playbook_result = """
    - hosts: all
      vars:
        test1: "val1"
      tasks:
        - name: testplay
          vars:
            test2: "val2"
            test3: "val3"
    """
    

# Generated at 2022-06-13 08:42:31.618676
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    """
    This function tests parameters of PlaybookInclude.load_data()
    """
    from ansible.playbook import Playbook

    # initialize test objects
    playbook_include = PlaybookInclude()
    base = Base()
    conditional = Conditional()
    taggable = Taggable()
    assert playbook_include.load_data(
        ds=None, basedir=None, variable_manager=None, loader=None) == Playbook()

# Generated at 2022-06-13 08:42:43.527248
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    '''
    Test load_data method of PlaybookInclude
    '''

    # Create PlaybookInclude object
    pbi = PlaybookInclude()
    pbi.import_playbook = 'test.yml'
    pbi.vars = {'var1': 'value'}

    # Create new PlaybookInclude object based on the attributes of pbi
    new_pbi = pbi.load_data(ds=pbi, basedir='/tmp')
    assert new_pbi.import_playbook == pbi.import_playbook
    assert new_pbi.vars == pbi.vars


# Generated at 2022-06-13 08:42:52.770066
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    import ansible.constants as C

    pbi = PlaybookInclude()

    pb = pbi.load_data({'import_playbook': 'playbook.yml', 'tags': ['foo', 'bar'], 'vars': {'var': 'val'}})
    assert isinstance(pb, Playbook)
    assert len(pb._entries) == 2
    assert pb._entries[0].vars == {'var': 'val'}
    assert pb._entries[1].vars == {'var': 'val'}
    assert pb._entries[0].tags == ['foo', 'bar']
    assert pb._entries[1].tags == ['foo', 'bar']


# Unit

# Generated at 2022-06-13 08:43:06.502078
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    temp = PlaybookInclude()
    ds = {'import_playbook': './data/test_playbooks/include_playbook_test.yml', 'tags': 'tagvalue'}
    basedir = '.'
    variable_manager = None
    loader = None
    new_obj = temp.load_data(ds, basedir, variable_manager, loader)

    #import pdb; pdb.set_trace()
    first_play = new_obj.get_entries(Play)[0]

    assert first_play.name == 'first_play'
    assert first_play.tags[0] == 'tagvalue'

    #import pdb; pdb.set_trace()
    second_play = new_obj.get_entries(Play)[1]
   

# Generated at 2022-06-13 08:43:17.662341
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleSequence

    # the following datastructure should yield exactly the same thing as that
    # found in test_preprocess_data_simple()
    ds = AnsibleMapping()
    ds['include'] = "./some/file.yml"

    pb = PlaybookInclude()
    pb.basedir = './some/dir'
    new_ds = pb.preprocess_data(ds)

    assert type(new_ds) == AnsibleMapping
    assert len(new_ds.keys()) == 2, new_ds.keys()

    assert 'import_playbook' in new_ds, "Expected key 'import_playbook' not found in: %s" % new_ds.keys()
    assert new_ds['import_playbook']

# Generated at 2022-06-13 08:43:37.351226
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    import_playbook = PlaybookInclude()
    import_playbook.preprocess_data({'import_playbook': 'test.yml'})
    temp = import_playbook.vars
    assert 'x' not in temp
    assert 'y' not in temp
    assert 'tags' not in temp
    assert import_playbook.import_playbook == 'test.yml'

    import_playbook.preprocess_data({'import_playbook': 'test.yml', 'vars': {'x': '10'}})
    temp = import_playbook.vars
    assert temp['x'] == '10'
    assert 'y' not in temp
    assert 'tags' not in temp
    assert import_playbook.import_playbook == 'test.yml'

    import_playbook.preprocess_

# Generated at 2022-06-13 08:43:52.382538
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    import yaml

# Generated at 2022-06-13 08:44:00.746549
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    '''Unit test for method load_data of class PlaybookInclude'''
    import sys
    import os
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.playbook.playbook import Playbook

    # Add the directory tests/playbooks to the system path and set the current directory
    # for this test to tests/playbooks. tests/playbooks contains the playbooks
    # test_playbook_include.yml and test_playbook_include.yml.
    #
    # See file tests/playbooks/test_playbook_include.yml to understand how test_PlaybookInclude_load_data()
    # is tested.
    sys.path.insert(1, os.getcwd() + "/tests/playbooks")

# Generated at 2022-06-13 08:44:06.942696
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    playbook_include = PlaybookInclude()
    data = {'foo': 'bar'}
    basedir = '/tmp'
    pb = playbook_include.load_data(ds=data, basedir=basedir)
    assert isinstance(pb, Playbook)
    assert len(pb._entries) == 1
    assert pb._entries[0] is not None
    assert pb._entries[0]._included_path is not None
    assert pb._entries[0]._included_path == '/tmp'



# Generated at 2022-06-13 08:44:17.929517
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.mod_args import ModuleArgsParser
    import ansible.playbook.play as play
    import ansible.playbook.task as task
    import ansible.playbook.block as block
    # Create a temporary directory
    import tempfile
    tmpdir = tempfile.mkdtemp()
    data = dict(import_playbook="../playbook.yml")
    playbook_file = os.path.join(tmpdir, "playbook.yml")
    with open(playbook_file, 'w') as f:
        f.write("""
        - hosts: all
          vars:
            hostfile: /etc/hosts
          serial: 1
          tasks:
            - name: Just a test of include, really
              ping: """)

# Generated at 2022-06-13 08:44:26.641402
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    import sys
    import os
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch
    from StringIO import StringIO

    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.playbook.playbook_include import PlaybookInclude

    playbook_include = PlaybookInclude()

    # The preprocess_data method should raise an exception if the parameter is not a dictionary
    new_stdout = StringIO()
    with patch.object(sys, 'stdout', new_stdout):
        assert playbook_include.preprocess_data('foo') == False

    # The preprocess_data method should return a reference to the parameter
    # if it is a dictionary but has no playbook import line
    result = playbook_include.preprocess_data

# Generated at 2022-06-13 08:44:33.268796
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook

    # create a fake Playbook
    pb = Playbook()
    pb._entries = [Play()]
    pb._entries[0].vars = {"a": "1"}

    # create a PlaybookInclude
    pbi = PlaybookInclude()
    pbi.vars = {"b": "2"}

    # inject the fake Playbook into the PlaybookInclude
    pb_loaded = pbi.load_data("<some_file.yml>", pb)

    # check the result
    assert pb_loaded.vars["b"] == "2"
    assert pb_loaded.vars["a"] == "1"

    # create a fake Playbook
    pb = Play

# Generated at 2022-06-13 08:44:33.754729
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:44:35.011624
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass


# Generated at 2022-06-13 08:44:47.094851
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    playbook_include = PlaybookInclude()

    # Not a valid yaml document
    with pytest.raises(AnsibleParserError) as ex:
        playbook_include.load_data('foobar')
    assert ex.value.message == 'Invalid YAML'

    # Not a dict
    with pytest.raises(AnsibleParserError) as ex:
        playbook_include.load_data([])
    assert ex.value.message == 'playbook load expects a YAML dictionary'

    # Not a valid playbook include
    with pytest.raises(AnsibleParserError) as ex:
        playbook_include.load_data('- include: foo')
    assert ex.value.message == "import_playbook statements must specify the file name to import"

    # No playbook loader

# Generated at 2022-06-13 08:45:01.424171
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    ds = dict(
       import_playbook='test.yml',
    )
    ds = PlaybookInclude.load_data(data=ds, basedir='.')._ds
    assert isinstance(ds, dict)
    assert isinstance(ds, AnsibleBaseYAMLObject)
    assert ds['import_playbook'] == 'test.yml'

    ds = dict(
       import_tasks='test.yml',
    )
    ds = PlaybookInclude.load_data(data=ds, basedir='.')._ds
    assert isinstance(ds, dict)
    assert isinstance(ds, AnsibleBaseYAMLObject)

# Generated at 2022-06-13 08:45:08.918344
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager

    source = """
---
- hosts: localhost
  vars:
    - var1: val1
  import_playbook: ./test.yml
  tasks:
    - debug: var=var1
    """

    data = yaml.load(source)
    included_source = """
    ---
    vars:
      var1: val2
    tasks:
      - debug: msg="{{ var1 }}"
    """

    included_data = yaml.load(included_source)

    # Create play
    play = Play.load(data[0], variable_manager=VariableManager(), loader=None)

    # Create included play

# Generated at 2022-06-13 08:45:16.509374
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # This is a fail conditions for load_data method
    # (a) File does not exists
    # (b) Playbook is not exist

    from ansible.parsing.utils.addresses import parse_address
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.playbook.playbook_include import PlaybookInclude as PlaybookIncludeNew
    import os.path

    # Check for file exist

# Generated at 2022-06-13 08:45:21.379817
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    #for ds, basedir, variable_manager, loader in [ ]:
    #    obj = PlaybookInclude.load(ds, basedir, variable_manager, loader)
    #    assert obj == PlaybookInclude()
    return

# Generated at 2022-06-13 08:45:34.511891
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    playbook_include = PlaybookInclude()
    ds = AnsibleMapping()
    ds.ansible_pos = (1, 1)
    # test case with no import_playbook
    res = playbook_include.preprocess_data(ds)
    assert res == {}
    # test case with import_playbook
    # - simple
    ds.clear()
    ds['import_playbook'] = 'playbook.yml'
    res = playbook_include.preprocess_data(ds)
    assert res['import_playbook'] == 'playbook.yml'
    assert res['vars'] == dict()
    # - with vars
    ds.clear()
    ds['import_playbook'] = 'playbook.yml'
    ds['vars'] = dict(foo='bar')


# Generated at 2022-06-13 08:45:35.645087
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # TODO: Test with a collection
    pass

# Generated at 2022-06-13 08:45:47.719320
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    #valid input
    ds1 = dict(import_playbook=dict(tags='tag1,tag2', vars=dict(a=1, b=2), file='file1'))
    play_include = PlaybookInclude()
    play_include.preprocess_data(ds1)
    assert play_include.vars == dict(a=1,b=2)
    assert play_include.import_playbook == 'file1'
    assert play_include.tags == ['tag1','tag2']

    ds2 = dict(import_playbook='file2')
    play_include.preprocess_data(ds2)
    assert play_include.vars == dict()
    assert play_include.import_playbook == 'file2'
    assert play_include.tags == []

    #invalid input
   

# Generated at 2022-06-13 08:46:00.184927
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # Basic structure of data to test load_data
    import tempfile
    import filecmp
    import os

    c = dict(
        hosts = dict(
            localhost = dict(
                host_specific_var = 'foo',
                host_specific_list = ['item1', 'item2'],
            ),
            remotehost = dict(
                host_specific_var = 'bar',
            ),
        ),
        vars = dict(
            always_present = dict(
                var = 'foo',
            ),
        ),
    )

    # Temp file for playbook to be included
    f = tempfile.NamedTemporaryFile(delete=False)
    f.close()

    # Temp file for file with vars to be included
    f_vars = tempfile.NamedTemporaryFile(delete=False)
    f

# Generated at 2022-06-13 08:46:13.855020
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task.include import TaskInclude
    from ansible.playbook.task import Task
    import ansible.playbook.playbook as playbook

    test_playbook = 'test_playbook_include.yml'
    playbook.ROOT_DIR = 'test/integration/playbooks'

    with open(playbook.ROOT_DIR + '/' + test_playbook, 'r') as fh:
        data = fh.read()
    #test_obj = PlaybookInclude(variable_manager=None, loader=None)
    test_obj = PlaybookInclude()
    playbook = test_obj.load(data, '.')
    assert playbook is not None
    # Check the entries
    assert len(playbook._entries) == 1

# Generated at 2022-06-13 08:46:14.847906
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:46:34.084671
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.collection_loader.collection_finder import _get_collection_path
    from ansible.template import Templar
    from ansible.playbook.play import Play

    # Use fake collection data for testing
    collection_dirs = ['/home/foo/ansible_collections/ns_name/collection_name',
                       '/home/foo/ansible_collections/ns_name2/coll2_name2']
    _get_collection_path.cache_clear()
    _get_collection_path.cache_clear()
    _get_collection_path.cache_clear()
    _get_collection_path.cache_clear()
    _get_collection_path.cache_clear()
    _get_collection_path.cache_clear()
    _get_collection_path.cache_clear()
    _get_collection_path

# Generated at 2022-06-13 08:46:45.412849
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import sys
    import ansible.plugins.loader
    import ansible.constants as C
    import ansible.template
    sys.path.insert(0, os.path.dirname(__file__) + "/../../")
    sys.path.insert(0, os.path.dirname(__file__) + "/../../ansible_collections")
    sys.path.insert(0, os.path.dirname(__file__) + "/../../ansible_collections/ansible_collections/test_collection")
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.utils.loader import DataLoader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

# Generated at 2022-06-13 08:46:47.955017
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    print("Testing load_data")
    # TODO: implement
    return


# Generated at 2022-06-13 08:46:49.447764
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # test code
    # TODO
    pass

# Generated at 2022-06-13 08:46:52.780144
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    playbook_include = PlaybookInclude
    playbook_include.load_data("import_playbook: "+"test_playbook_include.yml")

# Generated at 2022-06-13 08:47:00.274643
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude
    import sys

    test_import_playbook = "./test_playbook_import.yaml"
    basedir = "test_dir"

    # test with no handler and no vars

# Generated at 2022-06-13 08:47:12.356854
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Initialize a mock PlaybookInclude object
    playbookinclude = PlaybookInclude()
    playbookinclude.name = "web_pack.yml"
    playbookinclude.tags = "web"
    playbookinclude._import_playbook = "base_pack.yml"
    playbookinclude._vars = {"key1": "value1", "key2": "value2"}

    # Initialize a mock Playbook object
    playbook = Playbook()
    playbook.name = "base_pack"
    playbook.tags = "base"

# Generated at 2022-06-13 08:47:13.696830
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass


# Generated at 2022-06-13 08:47:14.324533
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:47:19.738548
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    pb = PlaybookInclude.load({'import_playbook': 'test.yml'}, '/playbooks')
    assert pb.is_playbook()
    assert pb._entries[0].is_play()
    assert pb._entries[0].__class__ == Play

# Generated at 2022-06-13 08:47:40.262431
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import pytest
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role import Role
    from ansible.playbook.role_include import RoleInclude

    # Setup test data
    data = {'import_playbook': 'test.yml'}
    basedir = '~/ansible'
    variable_manager = None
    loader = None
    pb = PlaybookInclude.load(data, basedir, variable_manager, loader)
    assert isinstance(pb, Playbook)
    assert len(pb._entries) == 2
    assert isinstance(pb._entries[0], Play)
    assert p

# Generated at 2022-06-13 08:47:50.682241
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Create a test PlaybookInclude instance and a test Playbook instance
    playbookInclude = PlaybookInclude()
    playbook = Playbook()

    # Load the PlaybookInclude instance with data
    playbook_include_obj = playbookInclude.load_data(
        ds={'import_playbook': 'tests/import_playbook/shared_variables/shared_variables.yml'},
        basedir='tests/import_playbook'
    )

    # Load the test Playbook instance with data from the shared variables playbook
    # that was loaded in the PlaybookInclude instance,
    # this is the playbook we want to compare with

# Generated at 2022-06-13 08:47:51.703363
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:47:52.397929
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
   pass

# Generated at 2022-06-13 08:48:04.457401
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play

    # this is a temporary hack until the preprocess_data method can implement
    # all the tests it needs to implement, but it allows the test to be written
    # here and shared by both classes
    class PlaybookIncludeSub(PlaybookInclude):
        _data = None
        def preprocess_data(self, ds):
            return ds

    playbook_include_sub = PlaybookIncludeSub()

    # mocking the function inside the playbook include to make sure it is called
    # only within the given file check

# Generated at 2022-06-13 08:48:16.249858
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.play import Play

    test_data = {
        'include': 'roles/foo.yml',
        'include_vars': 'vars/foo.yml'
    }
    pbi = PlaybookInclude().load(test_data, '')
    preprocessed_data = pbi.preprocess_data(test_data)

# Generated at 2022-06-13 08:48:28.365146
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Setup data
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    data_loader = DataLoader()
    variable_manager = VariableManager()
    basedir = '/path/to/playbooks'
    
    # Test
    playbook_include = PlaybookInclude(
        import_playbook="import_playbook.yml",
        task_include="task_include.yml"
    )


    # Result
    pb = playbook_include.load_data(data_loader, basedir, variable_manager)
    assert isinstance(pb, Playbook)

    # Setup data

# Generated at 2022-06-13 08:48:36.109432
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import tempfile

    playbook_path = os.path.join(tempfile.mkdtemp(), 'playbook.yml')
    with open(playbook_path, 'w') as fh:
        fh.write('---\n')
        fh.write('- hosts: localhost\n')
        fh.write('  tasks:\n')
        fh.write('    - name: test\n')
        fh.write('      assert: that=false\n')

    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()

    pb = PlaybookInclude

# Generated at 2022-06-13 08:48:48.333800
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    def _get_play_name(play):
        return play.name

    from ansible.playbook.play import Play

    pb_include = PlaybookInclude()

    # Example playbook entry
    playbook_entry = """
        - import_playbook: test_playbook.yml
    """

    # Example playbook entry with parameters
    playbook_entry_with_parameters = """
        - import_playbook: test_playbook.yml vars:
            param1: value1
    """

    # Example playbook entry with a conditional
    playbook_entry_with_conditional = """
        - import_playbook: test_playbook.yml
          when: param1 == value1
    """

    # Example playbook entry with a conditional on included plays

# Generated at 2022-06-13 08:48:56.035909
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.bundle import Bundle
    from ansible.playbook.play import Play
    pbi = PlaybookInclude()

    # Test on empty param
    data = pbi.load_data(ds={}, basedir='.', variable_manager={}, loader={})
    assert isinstance(data, Bundle)
    assert len(data._entries) == 0

    # Test on no value
    data = pbi.load_data(ds={'import_playbook': None}, basedir='.', variable_manager={}, loader={})
    assert isinstance(data, Bundle)
    assert len(data._entries) == 0

    # Test on relative path
    lunbox_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Generated at 2022-06-13 08:49:14.835326
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.parsing.vault import VaultAwareParameterParser

    playbook_includ_path = os.path.join(os.path.dirname(__file__), 'test_data', 'import_playbook')
    playbook_pp_includ_path = os.path.join(os.path.dirname(__file__), 'test_data', 'import_playbook_preprocessed')
    playbook_includ_path_py = os.path.join(os.path.dirname(__file__), 'test_data', 'import_playbook.py')

# Generated at 2022-06-13 08:49:15.682429
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:49:16.564656
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:49:32.011817
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.parsing.dataloader import DataLoader

    data = dict(
        import_playbook='playbook.yml',
        tags=['a', 'b', 'c']
    )

    p = PlaybookInclude()
    pb = p.load_data(data, '/tmp', DataLoader())
    assert type(pb) is Playbook
    assert len(pb._entries) == 1
    assert type(pb._entries[0]) is Play

    data = dict(
        import_playbook='playbook.yml',
        tags=[],
        when='somecondition'
    )

    p = PlaybookInclude()

# Generated at 2022-06-13 08:49:44.230736
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.executor.playbook_executor import PlaybookExecutor

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=['localhost'])
    variable_manager.set_inventory(inventory)

    # We have to pretend to be an ansible-playbook run to do this.
    # All of these objects need to be passed to the PlaybookExecutor,
    # which is the object that will take care of running the included
    # playbook.
    #
    # The good new is the setup is pretty simple; we need a Playbook

# Generated at 2022-06-13 08:49:52.896167
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    # Create object and load
    my_pb = PlaybookInclude()
    obj = my_pb.load_data({'import_playbook': 'playbook.yml', 'vars': {'a': 1, 'b':2}}, '/tmp')
    # Check object
    assert obj._entries[0].__class__ == Play
    assert len(obj._entries) == 1
    assert obj._entries[0].vars['a'] == 1
    assert obj._entries[0].vars['b'] == 2

# Generated at 2022-06-13 08:50:01.924006
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    loader = AnsibleLoader(None, dict())
    ds = dict(import_playbook='./path/to/playbook.yml')
    basedir = '/tmp/'
    test_object = PlaybookInclude.load(data=ds, basedir=basedir, variable_manager=None, loader=loader)
    test_object._load_playbook_data(file_name='./path/to/playbook.yml', variable_manager=None, vars={})
    assert test_object._entries is not None
    assert test_object._entries[0]._included_path == os.path.join(basedir, 'path/to')


# Generated at 2022-06-13 08:50:13.377354
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    v1 = PlaybookInclude()
    ds1 = {'import_playbook': "test_play.yml"}
    new_ds1 = v1.preprocess_data(ds1)
    assert isinstance(new_ds1, dict)
    assert new_ds1.get('import_playbook') == "test_play.yml"
    assert new_ds1.get('tags') == None

    v2 = PlaybookInclude()
    ds2 = {'import_playbook': 'test_play.yml tags=tag_1,tag_2 vars={"a": "1", "b": "2"}'}
    new_ds2 = v2.preprocess_data(ds2)
    assert isinstance(new_ds2, dict)

# Generated at 2022-06-13 08:50:20.271763
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.template import Templar
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.module_utils.six import string_types
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    # Pass
    ds = AnsibleMapping()
    ds.update({
        'import_playbook': 'pbook.yml',
        'vars': {
            'var1': 'value1',
            'var2': 'value2'
        }
    })
    pbi = PlaybookInclude.load(ds, '/tmp')
    assert pbi._entries[0].vars['var1'] == 'value1'
    assert pbi._ent

# Generated at 2022-06-13 08:50:31.327566
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    loader = None
    display = Display()

    ##
    # Test with an uninitialized AnsibleBaseYAMLObject
    #
    display.display(msg='Test PlaybookInclude load with an uninitialized AnsibleBaseYAMLObject')
    display.display(msg='Test should fail due to an assertion error')
    try:
        PlaybookInclude.load(data=None, basedir=None, variable_manager=None, loader=loader)
    except AssertionError:
        pass

    # Test with a valid AnsibleBaseYAMLObject
    display.display(msg='Test PlaybookInclude load with a valid AnsibleBaseYAMLObject')
    display.display(msg='Test should not fail')

# Generated at 2022-06-13 08:50:48.267303
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    PlaybookInclude.load_data()
    PlaybookInclude()
    PlaybookInclude().load_data(ds='test_ds', basedir='test_basedir', variable_manager='test_var', loader='test_loader')
    import os
    import yaml
    PlaybookInclude().load_data(yaml.load("""
        ---
        import_playbook: test_file
        """), os.getcwd(), variable_manager='test_var', loader='test_loader')
    PlaybookInclude().load_data(yaml.load("""
        ---
        - import_playbook: test_file
        """), os.getcwd(), variable_manager='test_var', loader='test_loader')

# Generated at 2022-06-13 08:50:49.165648
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:51:02.396173
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.cli.playbook import PlaybookCLI
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    loader = AnsibleLoader(list(), playbooks=[PlaybookCLI.base_parser().parse_args([])], variable_manager=VariableManager())

    dataset = '''
- import_playbook: playbook.yml tags: [tag1,tag2]
  vars:
    key1: value1
    key2: value2
- import_playbook: playbook.yml vars: key3: value3 key4: value4
    '''

    result = PlaybookInclude.load(dataset, None, loader=loader)
    assert result is not None

# Generated at 2022-06-13 08:51:14.868874
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # input: playbook_include = PlaybookInclude()
    # input: ds = [{'import_playbook': 'test.yml'}]
    # input: basedir = ''
    # input: variable_manager = ''
    # input: loader = string_types
    # output: None

    # code to be executed
    obj = {}
    assert not PlaybookInclude().load_data(obj, '')

    # input: playbook_include = PlaybookInclude()
    # input: ds = {'import_playbook': None}
    # input: basedir = ''
    # input: variable_manager = ''
    # input: loader = string_types
    # output: AnsibleParserError

    # code to be executed
    obj = {'import_playbook': None}


# Generated at 2022-06-13 08:51:23.631082
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import shutil, tempfile
    from ansible.playbook.playbook import Playbook
    from ansible.module_utils._text import to_text
    from ansible.vars.manager import VariableManager

    class LoaderDummy:
        def __init__(self):
            self.path = None

    # set up a dummy loader
    temp_dir = tempfile.mkdtemp()
    shutil.copyfile('./test/units/module_utils/a.yml', os.path.join(temp_dir, 'a.yml'))
    loader = LoaderDummy()
    loader.path = temp_dir

    # set up a dummy variable manager
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'extra_var': 'extra_var_value'}

    # load

# Generated at 2022-06-13 08:51:38.439844
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    from ansible.playbook.play import Play
    cur_dir = os.getcwd()
    top_dir = os.path.abspath(os.path.join(cur_dir, os.pardir, os.pardir))
    yaml_path = os.path.join('test', 'yaml')
    yaml_file = os.path.join(yaml_path, 'include_playbook.yml')
    data = "<test/yaml/include_playbook.yml"
    basedir = top_dir
    ds = {"import_playbook": data}
    #default module args
    module_args = {'variable_manager': None,
                   'loader': None
                   }
    #Play class instance
    play = Play()
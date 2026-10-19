

# Generated at 2022-06-13 08:41:57.141427
# Unit test for method load_data of class PlaybookInclude

# Generated at 2022-06-13 08:41:58.690432
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # TODO: fix test
    pass

# Generated at 2022-06-13 08:42:10.451927
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    pb = PlaybookInclude.load(dict(import_playbook='main.yml'), basedir='.', variable_manager=None, loader=None)
    pb.load_data(ds=dict(), basedir='.', variable_manager=None, loader=None)

    print(pb)
    assert pb.__class__ == Playbook
    # Check if all loaded entries have the included_path.
    for e in pb._entries:
        assert e._included_path


# Generated at 2022-06-13 08:42:21.782534
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.parsing.yaml.dumper import AnsibleDumper

    class_under_test = PlaybookInclude()
    data = dict(
        import_playbook='sub/sub.yml',
        vars=dict(one='1', two='two', three='3'),
        tags=['abc', 'def', 'ghi']
    )
    # this will have been converted to a dict by the time it reaches here
    new_ds = class_under_test.preprocess_data(data)

    assert new_ds['import_playbook'] == "sub/sub.yml"
    assert type(new_ds['vars']) == dict
   

# Generated at 2022-06-13 08:42:22.363247
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:42:22.948771
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:42:30.417850
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook.play import Play

    pbi = PlaybookInclude()

    pbi.load_data({'import_playbook': 'test_file.yml'}, os.path.dirname(__file__))

    assert pbi._import_playbook == 'test_file.yml'

    pbi.load_data({'import_playbook': 'test_file.yml', 'vars': {'key': 'value'}}, os.path.dirname(__file__))

    assert pbi._import_playbook == 'test_file.yml'
    assert pbi._vars['key'] == 'value'


# Generated at 2022-06-13 08:42:45.092717
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    #
    # include: file_name [vars]
    #
    ds = {'include': 'file_name'}
    ds_processed = PlaybookInclude.load(ds=ds, basedir=None, variable_manager=None, loader=None)
    assert 'import_playbook' in ds_processed
    assert not 'tags' in ds_processed

    ds = {'include': 'file_name tags=tag1,tag2'}
    ds_processed = PlaybookInclude.load(ds=ds, basedir=None, variable_manager=None, loader=None)
    assert 'import_playbook' in ds_processed
    assert 'tags' in ds_processed
    assert 'tag1' in ds_processed['tags']

# Generated at 2022-06-13 08:42:53.290170
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # Create a ds and set import_playbook to 'test.yml'
    ds = {'import_playbook': 'test.yml'}

    # As there are no pre_tasks, role and tasks, the method returns a Playbook object
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    pb = PlaybookInclude().load_data(ds, '.')
    assert isinstance(pb, Playbook)

    # Now add a role
    ds['pre_tasks'] = [{'debug': {'msg': 'test1'}}]
    ds['role'] = {
        'a_role': {},
    }
    pb = PlaybookInclude().load_data(ds, '.')
    assert isinstance(pb, Playbook)



# Generated at 2022-06-13 08:42:58.225750
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    pb = PlaybookInclude().load(data="test.yml", basedir="/tmp")
    assert type(pb) is Playbook, type(pb)
    assert len(pb._entries) == 1, len(pb._entries)
    assert type(pb._entries[0]) is Play, type(pb._entries[0])


# Generated at 2022-06-13 08:43:17.590255
# Unit test for method load_data of class PlaybookInclude

# Generated at 2022-06-13 08:43:29.995279
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play


# Generated at 2022-06-13 08:43:35.879210
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook import Playbook
    from ansible.playbook import Play

    # Try with a simple include
    obj = PlaybookInclude()
    obj.load_data(ds={'import_playbook': 'install-server.yml'}, basedir='/tmp')
    assert isinstance(obj, Playbook)

    # Now try with a more complicated include
    obj = PlaybookInclude()
    obj.load_data(ds={'import_playbook': 'install-server.yml',
                      'tags': 'install,server',
                      'vars': {'foo': 'bar'}}, basedir='/tmp')
    assert isinstance(obj, Playbook)

    # The above two cases covered all the conditional items specified on the
    # PlaybookInclude object.  The next two tests will cover the jobs
   

# Generated at 2022-06-13 08:43:48.679555
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    import sys
    import os
    import json

    ansible_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    sys.path.insert(0, ansible_root)
    from lib.ansible.playbook.playbook_include import PlaybookInclude
    from lib.ansible.parsing.dataloader import DataLoader

    DATA = """
    - include_playbook:
        name: test
        vars:
          test:
            - data
          test2:
            - data2
    """

    pi = PlaybookInclude().load(data=json.loads(DATA), basedir='/tmp')
    assert isinstance

# Generated at 2022-06-13 08:43:58.289646
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.errors import AnsibleParserError
    from ansible.utils.collection_loader import AnsibleCollectionConfig

    try:
        del os.environ['ANSIBLE_INTERNAL_TEMPLATES']
    except KeyError:
        pass

    try:
        del os.environ['ANSIBLE_CONFIG']
    except KeyError:
        pass
    main_playbook_path = os.path.join(os.getcwd(), 'test_playbook_include.yml')

# Generated at 2022-06-13 08:44:13.233598
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    import mock

    playbook = PlaybookInclude()
    playbook_data = mock.Mock()
    playbook_basedir = mock.Mock()
    playbook_variable_manager = mock.Mock()
    playbook_loader = mock.Mock()

    playbook_load_data_method = mock.Mock()
    playbook._load_data = playbook_load_data_method
    playbook.load_data(playbook_data, playbook_basedir, playbook_variable_manager, playbook_loader)

    assert playbook_load_data_method.called, "Failed to call _load_data of class PlaybookInclude"
    assert playbook_load_data_method.call_count == 1, "Failed to call _load_data of class PlaybookInclude exactly 1 time"


# Generated at 2022-06-13 08:44:15.194224
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # No tests here yet.
    # See also test_loader.py
    pass

# Generated at 2022-06-13 08:44:25.287758
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    import os
    import pytest


# Generated at 2022-06-13 08:44:33.238151
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    ''' Make sure the load_data of PlaybookInclude returns Playbook '''
    from ansible.playbook import Playbook

    data = 'test.yml'
    basedir = './test'
    playbook_include = PlaybookInclude()

    playbook = playbook_include.load_data(data, basedir)
    assert playbook is not None
    assert isinstance(playbook, Playbook)

# Generated at 2022-06-13 08:44:43.690843
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import ansible.playbook.play

    base_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'lib')
    vars_manager = None
    loader = None
    data_structure = {
        'import_playbook': 'test.yml'
    }

    playbook_include = PlaybookInclude.load(data_structure, base_dir, vars_manager, loader)

    # PlaybookInclude.load() returns a new Playbook() object
    assert isinstance(playbook_include, ansible.playbook.play.Playbook)

# Generated at 2022-06-13 08:44:56.892561
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    yaml_data = """
        - name: playbook include
          hosts: all
          include_tasks:
            - include_playbook: '{{ playbook_dir }}/playbook_vars.yaml'
              vars:
                param: value
        """

    yaml_data1 = """
        - name: playbook include
          hosts: all
          tasks:
            - name: mock task
              debug:
                msg: 'This is mock task'
        """
    inventory = InventoryManager(loader=None, sources='localhost,')

# Generated at 2022-06-13 08:45:05.595815
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Test with directory path
    basedir = './'
    ds = PlaybookInclude.load({'import_playbook': 'main.yml'}, basedir)
    assert ds._entries[0]._included_path == './'

    basedir = './'
    ds = PlaybookInclude.load({'import_playbook': './main.yml'}, basedir)
    assert ds._entries[0]._included_path == './'

    basedir = './'
    ds = PlaybookInclude.load({'import_playbook': 'bar/main.yml'}, basedir)
    assert ds._entries[0]._included_path == 'bar/'

    basedir = './'

# Generated at 2022-06-13 08:45:13.989673
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook

    # Test load_data method with two playbooks
    path = './test/integration/targets/ansible/test_validate-dependencies/'
    collection_name = 'ansible.posix'
    playbook_path = path + 'import_playbook_test_1.yaml'
    playbook_to_import_path = path + 'import_playbook_test_2.yaml'

    AnsibleCollectionConfig.playbook_paths.append(playbook_path)
    AnsibleCollectionConfig.playbook_paths.append(playbook_to_import_path)
    AnsibleCollectionConfig.default_collection = collection_name


# Generated at 2022-06-13 08:45:23.318245
# Unit test for method preprocess_data of class PlaybookInclude

# Generated at 2022-06-13 08:45:35.975906
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    # given
    src_path = os.path.join(os.path.dirname(__file__), '..', '..', 'examples', 'include_playbook')

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=src_path + '/hosts')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # when

# Generated at 2022-06-13 08:45:37.479080
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:45:38.795618
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass


# Generated at 2022-06-13 08:45:49.697758
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import textwrap

# Generated at 2022-06-13 08:46:02.910800
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # these lines ensure this test can be run from the test dir
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.executor.task_result import TaskResult
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    playbook_include = PlaybookInclude()
    test_pb = playbook_include.load_data(ds={'import_playbook': '../common/test_playbook.yml'},
                                         basedir='ansible/playbooks/',
                                         variable_manager=VariableManager(),
                                         loader=None)

    assert isinstance(test_pb, Playbook)

# Generated at 2022-06-13 08:46:04.887602
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # tests the logic of load_data method of class PlaybookInclude
    pass

# Generated at 2022-06-13 08:46:32.741550
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    pb = PlaybookInclude()
    # mocked 'playbook' object
    playbook = Playbook()
    # mocked 'play' object
    play = Play()
    # mocked 'entry' object
    entry = Play()

    # add mocked play to mocked playbook
    playbook._entries.append(entry)

    # mocked 'ds' object
    ds = Play()

    # mocked 'variable_manager' object
    variable_manager = Play()

    # call method load_data
    pb.load_data(ds, playbook, variable_manager)

    # check if mocked object 'playbook' has been changed
    assert playbook._entries == []

    # check if mocked object 'play' has been changed
    assert play.tags == []


# Generated at 2022-06-13 08:46:44.569632
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    display.verbosity=0
    print('UNIT TEST OUTPUT\n')
    import ansible.module_utils.atomic_move
    import ansible.module_utils.basic
    import ansible.module_utils.file
    import ansible.module_utils.net_tools
    import ansible.module_utils.os
    import ansible.module_utils.selinux
    import ansible.module_utils.setup
    import ansible.module_utils.system
    import ansible.module_utils.text
    import ansible.module_utils.vars

    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader


# Generated at 2022-06-13 08:46:45.757934
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass


# Generated at 2022-06-13 08:46:59.409728
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()

    data = {'import_playbook': 'my_pb.yml',
            'vars': {'var_a': 'abc'},
            'tags': ['tag1', 'tag2'],
            'when': 'test_variable'}

    ds = PlaybookInclude.load(data, '/', loader=loader)
    assert ds is not None
    assert len(ds._entries) == 1
    assert ds._entries[0].tasks[0].action == 'debug'
    assert ds._entries[0].tasks[0].vars['var_a'] == 'abc'
    assert ds._entries[0].tasks[0].tags == ['tag1', 'tag2']
   

# Generated at 2022-06-13 08:47:05.636327
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    playbook_include = PlaybookInclude()
    assert playbook_include.preprocess_data({}) == {}
    assert playbook_include.preprocess_data({'import_playbook': 'test_yaml_files/playbook.yml'}) == {'import_playbook': 'test_yaml_files/playbook.yml'}
    assert playbook_include.preprocess_data({'import_playbook': 'test_yaml_files/playbook.yml', 'vars': {'foo': 'bar'}}) == {'import_playbook': 'test_yaml_files/playbook.yml', 'vars': {'foo': 'bar'}}

# Generated at 2022-06-13 08:47:06.120505
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:47:15.507565
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role import Role

    ds = {
        'import_playbook': 'test_include.yml',
        'vars': {
            'var1': 'val1',
            'var2': 'val2',
        }
    }
    loader = DataLoader()
    pi = PlaybookInclude.load(ds, './test', loader)
    assert len(pi._entries) == 2
    assert isinstance(pi._entries[0], Role)
    assert pi._entries[0].name == 'test_role'
    roles = pi._entries[1].get_roles()
    assert len(roles) == 1
    assert roles[0].name == 'test_role'



# Generated at 2022-06-13 08:47:26.381872
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook

    playbook = Playbook()
    # Build a PlaybookInclude object with an import_playbook element containing
    # the path to a playbook file that exists
    # Setup loader so that collections are found as a fake collection
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    loader = DataLoader()
    loader.set_basedir("./test/units/module_loader")
    roles_path = ['./test/units/module_loader/my_collection/tests/roles']
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources="hosts", variable_manager=variable_manager)

# Generated at 2022-06-13 08:47:39.433046
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    # Test inclusion of an entire playbook, including task parameters
    playbook = PlaybookInclude.load({"import_playbook": "other_playbook.yml role_a=1 role_b=2 role_c=3"}, basedir="")

    # Test inclusion of an entire playbook, including task parameters
    assert isinstance(playbook, Playbook)
    assert len(playbook._entries) == 2
    assert playbook._entries[0].name == 'include 1'
    assert playbook._entries[1].name == 'include 2'
    assert playbook._entries[0]._included_path is None
    assert playbook._entries[1]._included_path is None

    # Test inclusion of a play, including task parameters
    other

# Generated at 2022-06-13 08:47:40.051482
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    pass

# Generated at 2022-06-13 08:48:16.350167
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    import sys

    play = Play()
    pbi = PlaybookInclude()
    res = pbi.load_data(ds = '{ import_playbook: "include.yml", tags: "include", vars: { var1: 1 } }', basedir = '.', variable_manager = None, loader = None)
    for e in res.get_entries():
        if isinstance(e, Play):
            play.load_data(e.get_data(), basedir = '.', variable_manager = None, loader = None)
        else:
            play.load_data([e.get_data()], basedir = '.', variable_manager = None, loader = None)
    # Check whether the imported

# Generated at 2022-06-13 08:48:17.184946
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass


# Generated at 2022-06-13 08:48:29.700303
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import shutil
    import tempfile

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager


# Generated at 2022-06-13 08:48:36.927601
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import unittest

    class UnitTest(unittest.TestCase):
        def test_playbook_include_load_data(self):
            ds = dict(import_playbook='playbook.yml', tags=['all'], vars=dict(test_var=1))
            basedir = 'test/test_playbook_include'

            pb = PlaybookInclude.load(data=ds, basedir=basedir)

            # test if we get a playbook object
            self.assertTrue(isinstance(pb, Playbook))

            # test if the playbook has 3 plays (two from include, one from main playbook)
            self.assertEqual(len(pb.get_plays()), 4)

            # test if the include play has a vars

# Generated at 2022-06-13 08:48:48.412694
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook import Play

    import_playbook = "import_playbook.yml"
    path = os.path.dirname(os.path.realpath(__file__))
    basedir = os.path.join(path, 'data')
    expected_path = os.path.join(basedir, import_playbook)

    test_data = {'import_playbook': import_playbook}
    playbook_include = PlaybookInclude.load(test_data, basedir=basedir)
    result_pb = playbook_include.load_data(test_data, basedir=basedir)

    assert isinstance(result_pb, Playbook)
    assert isinstance(result_pb._entries[0], Play)

# Generated at 2022-06-13 08:48:56.110542
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # This test only checks that the class can process the given values
    # and returns a result.
    # The result is not checked.
    import os

    import ansible.parsing.yaml.objects
    import ansible.utils.collection_loader._collection_finder
    import ansible.utils.collection_loader.collection_finder
    import ansible.utils.collection_loader.paths

    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()

    basedir = os.path.abspath(os.path.dirname(__file__))
    variable_manager = VariableManager()

    playbook_include = ansible.playbook.playbook_include.PlaybookInclude

# Generated at 2022-06-13 08:49:07.040413
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.module_utils.six import StringIO

    # Test with file without playbook_paths
    data = '''
        ---
        - include: test.yml
          vars:
           test:
    '''

    pbi = PlaybookInclude.load(data, '')
    assert pbi._entries[0].vars['test'] == ''
    assert pbi._entries[0].vars.get('test2') is None

    # Test with file with playbook_paths
    data = '''
        ---
        - include: test.yml
          vars:
           test:
           test2: 2
    '''

    pbi = PlaybookInclude.load(data, '', loader=None)
    assert pbi._entries[0].vars['test'] == ''

# Generated at 2022-06-13 08:49:13.929096
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    # init
    basedir = "/tmp"
    ds = dict(import_playbook="import.yml")
    var_manager = dict(a=1)
    loader = dict(a=1)

    # init objects
    playbook_include = PlaybookInclude()

    # call method
    ret = playbook_include.load_data(ds, basedir, var_manager, loader)

    # check result
    #ansible_module.exit_json(changed=False, meta=descr)



# Generated at 2022-06-13 08:49:14.899700
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:49:17.510689
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    playbook_include = PlaybookInclude()
    playbook_include.load_data(dict(),'testpath', None, None)

# Generated at 2022-06-13 08:50:00.895220
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import tempfile
    import ansible.constants as C

    basedir = os.path.join(tempfile.mkdtemp(), 'test_data')
    with open(os.path.join(basedir, 'file_name.yml'), 'w') as f:
        f.write('''
- hosts: all
  tasks:
    - ping:
- hosts: all
  tasks:
    - ping:
''')

# Generated at 2022-06-13 08:50:01.621922
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass


# Generated at 2022-06-13 08:50:13.076181
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.play import Play

    # using a fixture playbook_include.yaml located in unit tests fixtures directory
    import_file = "playbook_include.yaml"

    pc = PlaybookInclude.load(import_file, ".")
    assert isinstance(pc, Playbook)
    # check if playbook entries are Play instances
    assert all(isinstance(entry, Play) for entry in pc._entries)
    assert len(pc._entries) == 1
    assert pc._entries[0].hosts == ['localhost']
    assert pc._entries[0].name == 'async test'

# Generated at 2022-06-13 08:50:23.972022
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.loader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    data = '''
- hosts: all
  vars:
    hello: world
  tasks:
    - debug: msg="Hello, world!"
'''
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['127.0.0.1,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    pb = PlaybookInclude.load(data, basedir='.', variable_manager=variable_manager, loader=loader)
    assert pb._entries[0].vars['hello'] == 'world'

# Generated at 2022-06-13 08:50:33.170249
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # we need to mock the whole ansible module for this test, Else it fails if ansible is installed
    from unittest.mock import MagicMock
    from ansible.module_utils import basic
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.executor.playbook_executor import PlaybookExecutor
    import ansible.constants as C

    # We will use the saved path of the current ansible directory to restore it after the mock
    real_ansible_path = C.DEFAULT_MODULE_PATH[0]

# Generated at 2022-06-13 08:50:48.038587
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.task import Task
    import sys
    import ast

    class FakeVariableManager:

        def __init__(self):
            self._vars = {}

        def set_nonpersistent_facts(self, facts):
            self._vars.update(facts)

        def get_vars(self):
            return self._vars

    class FakeVarsModule:

        @staticmethod
        def load_vars(ds, basedir, variable_manager, loader):
            return {}

    class FakeDS:

        def __init__(self, filename, basedir):
            self.filename = filename
            self.basedir = basedir

    fake_variable_manager = FakeVariableManager()
    fake

# Generated at 2022-06-13 08:50:54.940607
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import pytest
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.utils.collection_loader._collection_finder import _get_collection_name_from_path
    collection = _get_collection_name_from_path('ansible.builtin')
    assert 'ansible.builtin' == collection
    playbook_include_obj = PlaybookInclude()
    collection_name = _get_collection_name_from_path('tests/data/collections/myns/mycoll/plays/main.yml')
    assert 'myns.mycoll' == collection_name
    source_play

# Generated at 2022-06-13 08:51:05.771119
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import unittest


# Generated at 2022-06-13 08:51:18.145056
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.play_context import PlayContext

    loader = AnsibleLoader(None, None)
    basedir = '/tmp'

    test_ds = dict(
        import_playbook='./test/test.yml',
        tags=['test1', 'test2']
    )
    from ansible.template import Templar
    t = Templar(loader=loader, variables={})
    pb = PlaybookInclude.load(test_ds, basedir, variable_manager=None, loader=loader)
    assert len(pb.entries) == 4
    assert isinstance(pb.entries[1], Play)
    assert pb.entries[1].tags == ['test1', 'test2']

# Generated at 2022-06-13 08:51:28.912025
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from . import load_fixture
    from ansible.playbook.role import Role
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    pbi = load_fixture('playbook_include.yml')[0]
    playbook = pbi.load_data(pbi._ds, os.path.dirname(os.path.realpath(__file__)))

    assert isinstance(playbook, Playbook)

    play = playbook._entries[0]
    assert isinstance(play, Play)

    assert pbi.import_playbook == 'include_playbook.yml'
    assert pbi.vars.get('foo') == 'bar'
    assert pbi.tags == ['foo']

    assert play.name == 'Included Play'
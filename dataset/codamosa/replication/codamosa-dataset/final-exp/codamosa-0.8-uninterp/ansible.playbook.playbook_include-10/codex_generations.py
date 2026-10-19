

# Generated at 2022-06-13 08:41:57.446498
# Unit test for method load_data of class PlaybookInclude

# Generated at 2022-06-13 08:42:00.947287
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    import sys
    import doctest
    import ansible.playbook.playbook_include
    sys.exit(doctest.testmod(ansible.playbook.playbook_include)[0])

# Generated at 2022-06-13 08:42:12.051106
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # Import here to avoid a dependency loop
    from ansible.playbook.play import Play

# Generated at 2022-06-13 08:42:13.618567
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # TODO: fix the code to test it!
    return

# Generated at 2022-06-13 08:42:23.783610
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    playbook_include = PlaybookInclude()
    ds = dict(
        import_playbook = "foo.yml",
        some_parameter  = "bar",
    )
    expected = dict(
        import_playbook = "foo.yml",
        vars = dict(
            some_parameter = "bar",
        )
    )
    assert playbook_include._preprocess_import(ds, dict(), "import_playbook", ds["import_playbook"]) == expected
    assert playbook_include.preprocess_data(ds) == expected
    ds = dict(
        import_playbook = "foo.yml some_parameter=bar",
    )
    assert playbook_include.preprocess_data(ds) == expected

# Generated at 2022-06-13 08:42:32.395051
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.attribute import FieldAttribute
    from ansible.playbook.become import Become
    from ansible.playbook.connection import Connection

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.utils.path import unfrackpath

    global temp_dir
    temp_dir = '~/.ansible/test_collections_path'
    temp_dir = unfrackpath(temp_dir)
    play_context = PlayContext()
    play_context._become

# Generated at 2022-06-13 08:42:47.183590
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    pb = PlaybookInclude.load(dict(import_playbook=['tasks/main.yml']), './test/loader/fixtures/', None, None)
    assert isinstance(pb, Playbook)
    assert len(pb._entries) == 1
    assert isinstance(pb._entries[0], Play)
    assert pb._entries[0].name == 'all'
    assert isinstance(pb._entries[0].tasks, tuple)
    assert len(pb._entries[0].tasks) == 2
    assert pb._entries[0].tasks[0] == dict(action=dict(module='shell', args='ls'), tags=['shell'])

# Generated at 2022-06-13 08:42:54.643245
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    ds = {'import_playbook': 'my-playbook.yml'}
    include = PlaybookInclude()
    new_ds = include.preprocess_data(ds)
    assert new_ds['import_playbook'] == 'my-playbook.yml'
    assert 'vars' not in new_ds
    assert 'tags' not in new_ds

    ds = {'import_playbook': 'my-playbook.yml var1=hello var2=world'}
    include = PlaybookInclude()
    new_ds = include.preprocess_data(ds)
    assert new_ds['import_playbook'] == 'my-playbook.yml'
    assert new_ds['vars']['var1'] == 'hello'

# Generated at 2022-06-13 08:43:06.552142
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.template import Templar
    import ansible.constants as C

    templar = Templar(loader=None, variables={})

    # Test data structure
    ds = AnsibleMapping()
    ds['import_playbook'] = 'test_playbook'
    ds['tags'] = 'tag1,tag2'
    ds['other_param'] = 'value'
    ds['vars'] = dict(wibble=1, wibble2=2)

    pi = PlaybookInclude()

    # Check that the preprocess_data method raises an error if used with invalid input

# Generated at 2022-06-13 08:43:16.443414
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook import PlaybookInclude

    ds = dict(
        pre_tasks=dict(
            ignore_errors=True,
            shell='ps aux',
        ),
        import_playbook='test.yaml tags=tag1,tag2 vars=var1=1 var2=2',
    )
    pi = PlaybookInclude.load(ds, 'test 123')
    assert len(pi.pre_tasks) == 1
    assert pi.import_playbook == 'test.yaml'
    assert pi.tags == ['tag1', 'tag2']
    assert pi.vars == dict(var1='1', var2='2')

# Generated at 2022-06-13 08:43:33.482214
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'var1': 'foo'}

    loader = DataLoader()

    obj = PlaybookInclude()
    basedir = 'basedir'

    # ds with vars in dict
    ds = dict(import_playbook='bar', vars=dict(var2='bar'))
    result = obj.load_data(ds=ds, basedir=basedir, variable_manager=variable_manager, loader=loader)
    # test that 1 play exists
    assert len(result._entries) == 1
    # test

# Generated at 2022-06-13 08:43:34.544993
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:43:46.780165
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook
    from io import StringIO
    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader

    YAML_DATA = StringIO(u'''
---
- import_playbook: test_playbook
  vars:
    test_var: value
''')
    PlayData = namedtuple('PlayData', 'play_ds vars_files extra_vars loader')

    fake_loader = DataLoader()
    fake_play = Play().load(YAML_DATA, variable_manager=None, loader=fake_loader)


# Generated at 2022-06-13 08:43:57.290900
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    import tempfile
    import os

    mock_loader = {}

    data_1 = {'import_playbook': 'test.yml'}
    data_2 = {'import_playbook': 'test.yml', 'vars': {'var1': 'test_var1', 'var2': 'test_var2'}}
    data_3 = {'import_playbook': 'test.yml', 'vars': {'var1': 'test_var1', 'var2': 'test_var2'}, 'when': {'test_var': 'test_value'}}

# Generated at 2022-06-13 08:44:12.712255
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.template.template import Templar


    playbook_include = PlaybookInclude()
    ds = dict(
        become='yes',
        become_user='root',
        sudo='yes',
        sudo_user='root',
        import_playbook=['test_playbook.yml', 'var=value'],
    )
    ds['vars'] = dict(
        foo='bar',
        baz='bat'
    )
    result_ds = playbook_include.preprocess_data(ds)
    assert result_ds['become'] == 'yes'

# Generated at 2022-06-13 08:44:23.961224
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude

    # Simple task: only a name
    simple_task = Task()
    simple_task.name = 'simple task'
    # Full task: name and with_items
    full_task = Task()
    full_task.name = 'full task'
    full_task.loop = 'items'
    # Simple import: only include
    simple_import = PlaybookInclude()
    simple_import.import_playbook = 'simple_import.yml'
    # Full import: include and with_items
    full_import = PlaybookInclude()

# Generated at 2022-06-13 08:44:28.692152
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    '''
    Unit test for method load_data of class PlaybookInclude.
    '''
    pass


# Generated at 2022-06-13 08:44:37.925244
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Arrange
    import os
    import sys
    import unittest
    import collections
    import ansible.playbook.playbook_include
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    test_dir = os.path.dirname(sys.modules[__name__].__file__)
    playbook_dir = os.path.join(test_dir, '../data/ansible_playbook', 'playbook_include')

    playbook_include = ansible.playbook.playbook_include.PlaybookInclude()

    # Act
    # After calling load_data method, pb object should be a Playbook type

# Generated at 2022-06-13 08:44:49.169864
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.play import Play
    # simple load
    pbi = PlaybookInclude()
    ds = {}
    ds['import_playbook'] = 'file1'
    ds['tags'] = 'play,play1'
    ds['vars'] = {'a': 1, 'b': 2}
    # return object is Playbook object
    assert(isinstance(pbi.load_data(ds, 'basedir', None), Playbook))
    # # test adding variable
    # ds = {}
    # ds['import_playbook'] = 'file1'
    # ds['tags'] = 'play,play1'
    # ds['vars'] = {'a': 1, 'b': 2}
    # p

# Generated at 2022-06-13 08:44:59.858610
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # Test the cases where import_playbook is a single argument with no other options
    input_data = dict(import_playbook='/path/filename')
    expected = dict(import_playbook='/path/filename')
    new_obj = PlaybookInclude.load(data=input_data, basedir='/')
    result = new_obj.preprocess_data(ds=input_data)
    assert (result == expected)

    # Test the cases where import_playbook is a single argument with other options
    input_data = dict(import_playbook='/path/filename', force_handlers=True, any_errors_fatal=False, tags='tag1')
    expected = dict(import_playbook='/path/filename', force_handlers=True, any_errors_fatal=False, tags='tag1')
   

# Generated at 2022-06-13 08:45:11.369387
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook.play import Play

    import_playbook = "../import.yml"
    ds = {}
    ds['import_playbook'] = import_playbook
    pb = PlaybookInclude().load_data(ds, ".")

    assert isinstance(pb._entries[0], Play)
    entry = pb._entries[0]
    assert entry.name == "import"



# Generated at 2022-06-13 08:45:21.346875
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.playbook_include import PlaybookInclude
    data = {
        'include': 'foo.yml',
        'include_tasks': 'bar.yml',
        'import_playbook': 'baz.yml',
    }
    res = {
        'import_playbook': 'foo.yml',
    }
    pi = PlaybookInclude()
    res2 = pi.preprocess_data(data)
    assert res['import_playbook'] == res2['import_playbook']
    res = {
        'import_playbook': 'baz.yml',
    }
    res2 = pi.preprocess_data(data)
    assert res['import_playbook'] == res2['import_playbook']

# Generated at 2022-06-13 08:45:34.596580
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import tempfile
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.role.include import RoleInclude
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.utils.path import unfrackpath

    # create a dummy play and role path
    (play_fd, play_path) = tempfile.mkstemp()
    (role_fd, role_path) = tempfile.mkstemp()

    # create dummy play and role that extend each other

# Generated at 2022-06-13 08:45:46.679918
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # here is the data to be used in the test
    ds_structure = """
    {
        "import_playbook": "test_import.yml",
        "vars": {
            "foo": "bar"
        }
    }
    """
    ds_data = ds_structure.strip()

    # set up the variables and test args we need
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    p = Play()
    p._ds = ds_data

# Generated at 2022-06-13 08:45:47.938255
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    assert False


# Generated at 2022-06-13 08:46:00.563064
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import ansible.constants as C
    from ansible.inventory.manager import InventoryManager
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=C.DEFAULT_INVENTORY_SOURCES)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    current_dir = os.path.dirname(os.path.abspath(to_bytes(__file__)))
    playbooks_dir = os.path.join(current_dir, 'playbooks')

# Generated at 2022-06-13 08:46:02.200534
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    b = PlaybookInclude()
    res = b.load_data('include: foo.yml k=v', '/test/test/test')
    assert res.file_name == 'foo.yml'
    assert res.vars['k'] == 'v'



# Generated at 2022-06-13 08:46:03.007115
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:46:11.637970
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.playbook
    from ansible.playbook.play import Play

    pb_include = PlaybookInclude()
    pb_include.import_playbook = '/PathToPlaybook.yml'
    pb = pb_include.load_data(pb_include, '.')
    assert (type(pb).__name__ == 'Playbook')
    assert (len(pb._entries) > 0)
    assert (type(pb._entries[0]).__name__ == 'Play')

# Generated at 2022-06-13 08:46:20.688830
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import unittest
    import ansible.playbook
    import ansible.playbook.play

    #Testing case with variables in playbook
    data = {'import_playbook': 'playbook_file.yml', 'vars': {'key1': 'value1', 'key2': 'value2'}}
    basedir = '/var/lib/awx/projects/my_project'
    variable_manager = None
    loader = 0
    playbook_include = ansible.playbook.PlaybookInclude.load(data=data, basedir=basedir, variable_manager=variable_manager, loader=loader)
    pb = playbook_include.load_data(ds=data, basedir=basedir, variable_manager=variable_manager, loader=loader)
    pb_entries = pb._entries

# Generated at 2022-06-13 08:46:33.872675
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.module_utils.six import string_types
    from six import assertCountEqual
    from ansible.template import Templar

    data = """
        - name: Play 1
          hosts: localhost
          tasks:
          - include: test-include.yml
          
        - name: Play 2
          hosts: localhost
          tasks:
          - import_playbook: test-include.yml
    """

    loader = AnsibleLoader(data, None, 'yaml')

    # get the data structure from the loader
    ds = loader.get_single_data()

    # we should have one entry
    assert len(ds) == 2

    # get the first item
    new_ds = ds[0]

    # should have ans

# Generated at 2022-06-13 08:46:45.244171
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    test_data = dict(
        import_playbook='./myplaybook.yml',
        vars={'x': 3},
        when=[dict(conditional='string_contains', register='foo', search='bar')],
        tags=['t1', 't2', 't3'],
    )

    playbook_include = PlaybookInclude()
    playbook_include.load_data(test_data, './')

    playbook = playbook_include.load_data(test_data, './')
    assert isinstance(playbook, Playbook)

    entries = playbook._entries

# Generated at 2022-06-13 08:46:58.497151
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    """
    This method test the load_data method.
    PlaybookInclude.load_data method fails in case, the file name is not specified.
    This test method validates the same.
    """
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook

    loader = DataLoader()
    variable_manager = VariableManager()
    play_context = PlayContext()

# Generated at 2022-06-13 08:47:02.929018
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    b_ds = {"import_playbook":"import_playbook.yml"}
    new_obj = PlaybookInclude.load(ds=b_ds, basedir="/dev/null",variable_manager=None, loader=None)
    assert isinstance(new_obj, PlaybookInclude), "Check import_playbook.yml returns instance of PlaybookInclude"

# Generated at 2022-06-13 08:47:13.869744
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', 'lib/ansible/playbook/play_include'))

# Generated at 2022-06-13 08:47:24.246075
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # import ansible.playbook.play
    # import ansible.playbook.playbook

    # create a PlaybookInclude object
    pi = PlaybookInclude()
    basedir = "/base/dir"
    data = dict()
    data['import_playbook'] = "foo.yml"
    pi.load_data(ds = data, basedir = basedir)
    assert pi.import_playbook == "foo.yml", "load_data did not set import_playbook to foo.yml: %s" % pi.import_playbook
    assert pi._basedir == basedir, "load_data did not set basedir to %s: %s" % (basedir, pi._basedir)

# Generated at 2022-06-13 08:47:36.338038
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # import here to avoid a dependency loop
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook

    p = PlaybookInclude()
    p._load_data(ds={}, basedir=None, variable_manager=None, loader=None)
    assert type(p) == Playbook

    # make sure that targets are properly loaded
    pb = Playbook()
    pb._entries = [Play(name="foo")]
    assert pb._entries[0]._included_path == None
    pb._load_data(ds={}, basedir=None, variable_manager=None, loader=None)
    assert pb._entries[0]._included_path != None

# Generated at 2022-06-13 08:47:36.833854
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:47:48.157624
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = None # we do not need a loader for this test
    basedir = '.'

    # We need to setup the test environment on the fly
    # to have a temporary playbook to import

    # first, create the playbook to import

# Generated at 2022-06-13 08:47:54.993970
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook

    pbi = PlaybookInclude()
    ds = dict(import_playbook = 'abc.yml', vars = dict(a=1, b=2), tags=['c'])

    pb = pbi.load_data(ds, '/some/path', None, None)
    assert isinstance(pb, Playbook)

# Generated at 2022-06-13 08:48:08.362920
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.module_utils.six import PY3

    if PY3:
        raise unittest.SkipTest('(%s) does not apply to python3' % __file__)


# Generated at 2022-06-13 08:48:22.373085
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play

    pbi = PlaybookInclude.load({
        'import_playbook': 'import.yml',
        'when': ['test'],
        'vars': {
            'var1': 'val1',
        },
        'tags': ['tag1', 'tag2']
    }, '/foo/bar')

    assert len(pbi._entries) == 2

    # test the first entry
    e1 = pbi._entries[0]
    assert isinstance(e1, Play)  # The first entry should be a play
    assert e1._included_path == '/foo/bar/import.yml'
    assert e1.vars['var1'] == 'val1'
    assert e1._included_conditional == ['test']

    # test the second

# Generated at 2022-06-13 08:48:33.428823
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import tempfile

    generate_playbook = lambda collection, playbook: '''---
    omit: ['tasks']
    hosts: all
    import_playbook: {}#{}
    '''.format(collection, playbook)

    generate_playbook_declaration = lambda collection, playbook: '''---
    - hosts: all
      tasks:
        - import_playbook: {}#{}
    '''.format(collection, playbook)

    def _load_data_from_playbook(collection_name, playbook_name, playbook_file_name, declaration):
        from ansible.playbook.play import Play
        from ansible.playbook.playbook import Playbook
        from ansible.playbook.task import Task
        from ansible.playbook.task_include import TaskInclude

# Generated at 2022-06-13 08:48:46.748847
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    temp_dir = tempfile.mkdtemp()
    in_inventory = os.path.join(temp_dir, "inventory")
    with open(in_inventory, 'w') as f:
        f.write('localhost\n')

    in_playbook = os.path.join(temp_dir, "main.yaml")
    with open(in_playbook, 'w') as f:
        f.write("""
- hosts: localhost
  connection: local
  vars:
    var1: val1
  import_playbook: test.yaml
  tasks:
    - debug: msg="main"
    - include: imported.yaml
""")

    in_playbook2 = os.path.join(temp_dir, "test.yaml")

# Generated at 2022-06-13 08:48:48.092434
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    '''
    Function to test load_data of PlaybookInclude class
    '''
    pass

# Generated at 2022-06-13 08:48:55.831247
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.play import Play

    import_playbook_structure = {'import_playbook': 'my_include.yml', 'vars': {'foo1': 'bar1', 'foo2': 'bar2'}, 'tags': 'my_include_tag'}
    playbook_inlclude = PlaybookInclude()
    playbook_inlclude.load_data(ds=import_playbook_structure, basedir='my_basedir')
    playbook_inlclude._loader.set_basedir = 'my_basedir'
    playbook = Playbook()
    playbook.load_from_file = lambda x: None
    playbook.set_loader = lambda x: None
    playbook.set_variable_manager = lambda x: None
    playbook.top

# Generated at 2022-06-13 08:49:05.371259
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    x = PlaybookInclude()
    x_obj = x.load_data(ds={'import_playbook': 'playbook.yml'}, basedir='./')

    # Now check that the object returned is in fact a playbook
    assert isinstance(x_obj, Playbook)

    # Check that the first entry in the playbook is in fact a play
    assert isinstance(x_obj._entries[0], Play)

# Generated at 2022-06-13 08:49:13.657129
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    pb = PlaybookInclude()
    # not a dictionary
    try:
        pb.load_data('string', '.')
        assert False
    except AnsibleAssertionError:
        assert True
    # missing import_playbook
    try:
        pb.load_data({}, '.')
        assert False
    except AnsibleParserError:
        assert True
    # not a string
    try:
        pb.load_data({'import_playbook': 0}, '.')
        assert False
    except AnsibleParserError:
        assert True
    # import_playbook is empty

# Generated at 2022-06-13 08:49:29.076312
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook

    playbook_include = PlaybookInclude()
    playbook = playbook_include.load_data(ds={'import_playbook': './test_playbook_include.yaml'}, basedir='./')

    # assert playbook is an instance of the Playbook class
    assert isinstance(playbook, Playbook)

    # assert all three loaded plays are instances of the Play class
    assert isinstance(playbook._entries[0], Play)
    assert isinstance(playbook._entries[1], Play)
    assert isinstance(playbook._entries[2], Play)

    # assert plays names and hosts are correct
    assert playbook._entries[0].name == 'Play 1'
    assert playbook._entries[0].host

# Generated at 2022-06-13 08:49:37.068741
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # tests for the method load_data of class PlaybookInclude

    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'test': 'test'}

    # test 1: simple playbook with vars
    import_playbook = 'include apb.yaml vars=test.yaml'
    playbook_include = PlaybookInclude(loader=loader)
    playbook = playbook_include.load_data(ds=import_playbook, basedir=os.getcwd(), variable_manager=variable_manager, loader=loader)

    assert playbook._entries[0].vars['test'] == 'test'

# Generated at 2022-06-13 08:49:57.195882
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    from ansible.cli.console import ConsoleCLI
    from ansible.module_utils.urls import open_url
    import ansible.module_utils.six as six
    from ansible.utils.collection_loader._collection_finder import AnsibleCollectionConfig
    import shutil
    from ansible.playbook.play import Play
    import tempfile

    test_playbook = """
    - import_playbook: test_play.yml
    """
    host_list = 'localhost'

    # setup tmp directory to host test playbook
    temp_directory = tempfile.mkdtemp()
    playbook_path = os.path.join(temp_directory, "test_playbook.yml")
    test_playbook_path = os.path.join(temp_directory, "test_play.yml")

    test

# Generated at 2022-06-13 08:50:02.484439
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    assert isinstance(PlaybookInclude.load({'import_playbook': 'first'}, None), Playbook)
    assert isinstance(PlaybookInclude.load({'import_playbook': 'first', 'vars': {'var1': 'val1'}}, None), Playbook)

# Generated at 2022-06-13 08:50:13.929092
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    # This PlaybookInclude is based on data for nested imports in the docs
    ds = dict(
        import_playbook="overridden.yml",
        vars=dict(
            foo=42,
            bar=23
        ),
        tags=["include_tag"]
    )

    basedir = './lib/ansible/playbook/tests/import_playbook'
    loader = DataLoader()
    variable_manager = VariableManager()
    pb_incl = PlaybookInclude.load(ds, basedir, variable_manager, loader)

    assert pb_incl.__class__

# Generated at 2022-06-13 08:50:26.047516
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.parsing.dataloader import DataLoader

    # sample variables data
    data = '{"test_var_1":"test_val_1"}'
    variable_manager = VariableManager()
    variable_manager._extra_vars = variable_manager._vars_cache = variable_manager._host_vars = variable_manager._group_vars = variable_manager._task_vars = variable_manager._merged_vars = variable_manager.static_vars = load_extra_vars(loader=DataLoader(), variables=data)

    # sample playbook include data
    includes_data = {'vars': {'test_1': 'test_val_1'}, 'import_playbook': 'test_include.yml', 'tags': 'test_tag'}


# Generated at 2022-06-13 08:50:26.918970
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:50:38.421680
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import sys
    import shutil
    import tempfile
    from AnsibleModuleMock import AnsibleModuleMock
    from ansible.playbook.play import Play
    from ansible.utils.collection_loader import AnsibleCollectionConfig

    # Create a temp directory
    tmpdir = tempfile.mkdtemp()

    # Create a collection
    collection_dir = os.path.join(tmpdir, "ansible_collections", "my_namespace", "my_collection")
    my_module_dir = os.path.join(collection_dir, "plugins", "modules")
    os.makedirs(my_module_dir)
    my_module_file = os.path.join(my_module_dir, "my_module.py")
    open(my_module_file, 'w').close()

   

# Generated at 2022-06-13 08:50:48.827950
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # Execute under a temporary directory since we're importing
    with utils.set_tmp_directory_on_unset():
        loader = DataLoader()
        variable_manager = VariableManager()
        playbook_basedir = utils.test_vars.playbook_dir
        playbook_path = os.path.join(playbook_basedir, 'test_playbook_include.yml')
        playbook = PlaybookInclude.load(
            data=loader.load_from_file(filename=playbook_path),
            basedir=playbook_basedir,
            variable_manager=variable_manager,
            loader=loader,
        )
        # ensure we got a Playbook() object back
        assert isinstance(playbook, Playbook)
        assert len(playbook._entries) == 1

        # Check the vars passed to

# Generated at 2022-06-13 08:50:55.505078
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    import yaml
    yaml_data = '''---
- import_playbook: other_play.yml
  when: foo
  tags:
    - foo
  vars:
    var1: value1
    var2: value2
'''
    inputs = yaml.safe_load(to_bytes(yaml_data))
    # input value is expected to be non empty list
    assert len(inputs) == 1
    # set the variable to be used in the playbook
    variable_manager = FakeVarManager()
    variable_manager.extra_vars = {'foo': 'yes'}
    # return the playbook
    pb = PlaybookInclude.load(inputs, 'tests/lib/ansible/playbook/data', variable_manager)
    # if the

# Generated at 2022-06-13 08:51:06.305481
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    pb = PlaybookInclude()
    # Try normal usage
    my_ds = {'import_playbook': 'test_1.yml'}
    res = pb.load_data(my_ds, '.')
    assert isinstance(res, Playbook)
    assert res._entries[0]._entry_type == 'import_playbook'
    # Try import_playbook with additional parameters
    my_ds = {'import_playbook': 'test_1.yml my_param=my_value vars: other_param=other_value'}
    res = pb.load_data(my_ds, '.')
    assert res._entries[0].vars['my_param'] == 'my_value'

# Generated at 2022-06-13 08:51:18.460949
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.utils.vars import combine_vars
    import yaml

    # create needed objects
    loader = None
    variable_manager = None
    basedir = './test/unit/playbook_tests'

    # create a playbook include object
    playbook_include = PlaybookInclude()

    # test load_data without variable_manager
    # test playbook include with list


# Generated at 2022-06-13 08:41:47.652911
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    '''
    Unit test for method load_data of class PlaybookInclude
    '''
    pass

# Generated at 2022-06-13 08:41:56.863281
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.play_context import PlayContext

    context = PlayContext()
    ds = dict(
        import_playbook='playbook.yml',
        import_playbook_tags='tag_one,tag_two',
        import_playbook_vars=dict(
            var1='value1',
            var2='value2',
            ),
        var3='value3',
        vars=dict(
            var4='value4',
            var5='value5',
            ),
        )


# Generated at 2022-06-13 08:42:08.036467
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.play_context import PlayContext

    import_playbook_data = dict(
        import_playbook = "someplay.yml",
        vars = dict(
            foo = "bar",
        )
    )
    expected_result = dict(
        import_playbook = "someplay.yml",
        vars = dict(
            foo = "bar",
        )
    )
    playbook_include_object = PlaybookInclude().load_data(import_playbook_data, "", variable_manager=PlayContext())
    assert playbook_include_object.preprocess_data(import_playbook_data) == expected_result

# Generated at 2022-06-13 08:42:18.273692
# Unit test for method preprocess_data of class PlaybookInclude

# Generated at 2022-06-13 08:42:27.399286
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.module_utils.six import PY3
    import sys

    if PY3:
        from io import StringIO
    else:
        from StringIO import StringIO

    # test 1: normal dict
    data = dict(
        import_playbook='test_playbook.yml',
        tags='test_tag1'
    )
    data = PlaybookInclude.load(data, '.', variable_manager=None, loader=None)
    assert data.import_playbook == 'test_playbook.yml'
    assert data.tags == ['test_tag1']

    # test 2: list

# Generated at 2022-06-13 08:42:34.689246
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.utils.vars import combine_vars

    loader = DictDataLoader({
        'import_playbook': '''
        hosts: all
        user: root
        gather_facts: False
        tasks:
          - name: ping!
            ping:
            tags: always

        ''',
    })

    p = Play().load(ds=dict(
        name="test play",
        hosts='all',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='ping', args=dict())),
        ]
    ), loader=loader, variable_manager=variable_manager)
    context = p.make_play_context(variable_manager)


# Generated at 2022-06-13 08:42:42.853139
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.parsing.yaml.constructor import AnsibleConstructor

    constructor = AnsibleConstructor(typemap={'!include': PlaybookInclude})
    data = '''
    - !include playlist.yaml tags=tag_one,tag_two var1=val1 vars=
        key1: value1
        key2: value2
      other_key: other_value
    - !include example.yml
    '''
    result = constructor.construct_yaml_map(data)

    assert result[0]['vars'] == {'other_key': 'other_value', 'key1': 'value1', 'key2': 'value2'}
    assert result[0]['tags'] == ['tag_one', 'tag_two']

# Generated at 2022-06-13 08:42:52.528104
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.playbook_include import PlaybookInclude

# Generated at 2022-06-13 08:43:04.302143
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.parsing.dataloader
    import ansible.playbook.play
    import ansible.vars.manager

    display.verbosity = 3
    dataloader = ansible.parsing.dataloader.DataLoader()
    variable_manager = ansible.vars.manager.VariableManager()
    p = PlaybookInclude.load(data={'import_playbook': 'playbook.yml'}, variable_manager=variable_manager, loader=dataloader)
    assert isinstance(p, ansible.playbook.base.Base)
    assert isinstance(p._entries[0], ansible.playbook.play.Play)

# Generated at 2022-06-13 08:43:10.985533
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.playbook.play import Play
    import os
    print(sys.argv)
    test_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'include_link_test_1.yaml')
    print(test_file)
    host_obj = yaml.load(open(test_file))
    # host_obj = {'import_playbook': '../somefile.yaml'}
    # res = PlaybookInclude.load(host_obj, '/tmp', None, None)

    # if isinstance(res, Playbook):
    #     print 'res is Playbook'
    # else:
    #     print 'res is not Playbook'

   

# Generated at 2022-06-13 08:43:28.714659
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext

    variable_manager = VariableManager()
    variable_manager._extra_vars = {'extra_var': 'extra_value'}

    pi = PlaybookInclude()
    pi._load_data({'import_playbook': './test_playbook'}, variable_manager=variable_manager)
    assert pi.import_playbook == './test_playbook'
    assert pi.vars == {'extra_var': 'extra_value'}

    pi = PlaybookInclude()

# Generated at 2022-06-13 08:43:35.099991
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.errors import AnsibleError
    import os

    inventory_manager = InventoryManager(loader=None, sources='localhost,')
    variable_manager = VariableManager(loader=None, inventory=inventory_manager)

    test_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    os.chdir(test_dir)
    data = {}
    data['import_playbook'] = './test/units/lib/ansible_test/_data/playbook_include.yml'

# Generated at 2022-06-13 08:43:47.695695
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import tempfile
    import shutil
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude

    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    # create a fake playbook
    playbook_path = temp_dir + "/playbook.yml"
    with open(playbook_path, "w") as file:
        file.write("""
- hosts: localhost
  tasks:
  - debug:
      msg: Hello World
""")
    # create a fake ansible.cfg file
    ansible_cfg_path = temp_dir + "/ansible.cfg"
    with open(ansible_cfg_path, "w") as file:
        file.write

# Generated at 2022-06-13 08:43:48.880446
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass


# Generated at 2022-06-13 08:43:49.517117
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:43:58.893761
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    path = os.path.realpath(__file__)
    path = os.path.dirname(path)
    file_name = os.path.join(path, '../test_playbooks/playbook-import_playbook-with_role.yml')
    loader = DataLoader()
    variable_manager = VariableManager()
    ds = loader.load_from_file(file_name)
    obj = PlaybookInclude()
    ds = obj.load_data(ds, path, variable_manager, loader)
    assert isinstance(ds, Play)

# Generated at 2022-06-13 08:44:14.445875
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    """ PlaybookInclude: load_data()
    """

    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.playbook.block import Block
    import ansible.playbook.playbook_include as pb

    # make sure we are working with the right modules
    assert(pb.__name__ == 'PlaybookInclude')
    assert(Play.__name__ == 'Play')
    assert(Task.__name__ == 'Task')
    assert(Inventory.__name__ == 'Inventory')
    assert(VariableManager.__name__ == 'VariableManager')
    assert(Block.__name__ == 'Block')


# Generated at 2022-06-13 08:44:18.632095
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    test_ds = AnsibleMapping()
    test_ds["import_role"] = "my_role"
    test_ds["vars"] = AnsibleMapping()
    test_ds["vars"]["red"] = "rojo"
    test_ds["vars"]["blue"] = "azul"
    test_ds["vars"]["green"] = "verde"
    test_ds["tags"] = "test_tag"

    preprocess_data = PlaybookInclude().preprocess_data(test_ds)
    assert len(preprocess_data) == 4

    assert preprocess_data["import_playbook"] == "my_role"
    assert preprocess_data["tags"] == "test_tag"
    assert preprocess_data["vars"]["red"] == "rojo"
   

# Generated at 2022-06-13 08:44:24.555079
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.playbook.play as base_play
    from ansible.playbook import Playbook
    from ansible.parsing.yaml.objects import AnsibleUnicode
    class MockTemplar:
        def __init__(self, loader=None, variables=None):
            pass
        def template(self, data):
            return data
    class PlaybookBase(Base):
        @classmethod
        def load_data(self, ds, basedir, variable_manager=None, loader=None):
            data = AnsibleMapping()
            data['vars'] = AnsibleMapping()
            data['vars']['var1'] = 'var1'
            data['import_playbook'] = 'test_playbook'
            data['tags'] = 'tag1'
            return PlaybookInclude.load

# Generated at 2022-06-13 08:44:36.884457
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    file_name = "the_import_file.yml"

    # Valid playbook import entries
    input = dict(
        import_playbook=file_name,
    )
    expected = dict(
        import_playbook=file_name,
    )
    result = PlaybookInclude.load(input, basedir='.', variable_manager=None, loader=None).preprocess_data(input)
    assert result == expected

    input = dict(
        include=file_name,
    )
    expected = dict(
        import_playbook=file_name,
    )
    result = PlaybookInclude.load(input, basedir='.', variable_manager=None, loader=None).preprocess_data(input)
    assert result == expected


# Generated at 2022-06-13 08:44:50.207855
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.errors import AnsibleAssertionError
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.template import Templar

    playbook_include = PlaybookInclude()

    # Check that we cannot load an empty data structure
    try:
        playbook_include.load_data( ds=None, variable_manager=None, loader=None)
        assert False, "We should not arrive here"
    except AnsibleAssertionError as e:
        print("Caught expected exception passing 'None' in ds: %s" % e)

    # Check that we cannot load a data structure which is not a dict

# Generated at 2022-06-13 08:45:00.717765
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    loader = DataLoader()
    variable_manager = VariableManager()
    playbook_include = PlaybookInclude().load_data(dict(import_playbook="test_playbook.yml", vars={"a": "b"}), C.DEFAULT_PLAYBOOK_PATH, variable_manager, loader)
    playbook_tasks = playbook_include.get_tasks()
    expected_task_name = "name"
    task = playbook_tasks[0]
    actual_task_name = task.name
    assert expected_task_name == actual_task_name
    expected_var_a_value = "b"
    actual_var_a_value = task.vars['a']
    assert expected_

# Generated at 2022-06-13 08:45:08.507183
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    '''
    test PlaybookInclude.load_data
    '''
    from ansible.playbook import Playbook
    mock_pb = Playbook()
    mock_pb._load_playbook_data = lambda file_name, variable_manager, vars: mock_pb
    mock_obj = PlaybookInclude()
    mock_obj.load_data = lambda ds, basedir, variable_manager, loader: mock_obj
    mock_obj.preprocess_data = lambda ds: {'import_playbook': 'mock_file'}
    mock_obj.preprocess_data = lambda ds: {'import_playbook': 'mock_file'}
    mock_obj._load_data = lambda ds: mock_obj

# Generated at 2022-06-13 08:45:16.233733
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # stackoverflow.com/questions/2682745/creating-a-dictionary-with-dictionary-comprehension-in-python
    def dict_eq(d1, d2):
        return set(d1.items()).difference(d2.items()) == set()

    ds = dict(
        import_playbook="path/to/pb1.yml",
        vars=dict(one=1, two=2)
    )

    pi = PlaybookInclude()
    new_ds = pi.preprocess_data(ds)
    assert dict_eq(new_ds, ds)


# Generated at 2022-06-13 08:45:30.850836
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import sys
    import unittest

    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars import VariableManager
    import ansible.constants as C

    variable_manager = VariableManager()

    class Collector(object):
        def __init__(self):
            self.tasks  = []
            self.blocks = []
            self.plays  = []

        def add(self, obj, entity_type):
            if entity_type == "task":
                self.tasks.append(obj)
            elif entity_type == "play":
                self.plays.append(obj)

# Generated at 2022-06-13 08:45:36.019019
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.playbook import Playbook

    pbi = PlaybookInclude()
    empty_data = {}
    basedir = '.'
    pb = pbi.load_data(empty_data, basedir)
    assert(isinstance(pb, Playbook))

# Generated at 2022-06-13 08:45:48.032509
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    def test_case(ds, result):
        new_pb = PlaybookInclude.load(ds, './', {}).get_data()
        if new_pb != result:
            raise AssertionError("%s != %s" % (new_pb, result))

    test_case("main.yml", dict(import_playbook="main.yml",
                               tags=[], vars=dict()))

    test_case("httpd.yml", dict(import_playbook="httpd.yml",
                                tags=[], vars=dict()))

    test_case("subdir/httpd.yml", dict(import_playbook="subdir/httpd.yml",
                                       tags=[], vars=dict()))


# Generated at 2022-06-13 08:46:00.747700
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    import os
    import ansible.constants as C

    # when playbook_paths is empty, it should still be able to load
    C.DEFAULT_PLAYBOOK_PATH = [os.path.join(os.path.dirname(__file__), 'data/playbooks')]

    from ansible.playbook import PlaybookInclude
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.role import Role
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 08:46:13.105375
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # setup a playbookInclude with some data
    playbookInclude = PlaybookInclude()
    data = '''
    - import_playbook: test.yml
      vars:
        var1: value1
        var2: value2
    '''
    # covert data to ansible object
    import_yaml
    data = import_yaml(data)
    # convert data to list
    data = [data]
    # convert to ansible object
    data = AnsibleBaseYAMLObject.construct_ansible_object(data, None)
    # preprocess data
    playbookInclude._preprocess_data(data)
    # check if 'import_playbook' is in the playbookInclude
    assert 'import_playbook' in playbookInclude.__dict__
    # check the value of import_playbook
   

# Generated at 2022-06-13 08:46:18.283311
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # Create a dict for import_playbook "pre_tasks/main.yml"
    data = {
        'import_playbook': 'pre_tasks/main.yml',
    }

    # Check the result returned by preprocess_data method
    # The final result should be like the result of a Task
    # Data structure
    pbi = PlaybookInclude.load(data, None)
    expected_result = {'import_playbook': 'pre_tasks/main.yml'}

    assert expected_result == pbi._ds

    # This test is for a "vars" key in param of the import_playbook
    # format
    # Create a dict for import_playbook "pre_tasks/main.yml vars='{a:1}'"

# Generated at 2022-06-13 08:46:34.751067
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Create a fake PlaybookInclude object
    playbookInclude = PlaybookInclude()
    # Create a fake VariableManager
    import ansible.playbook.variable_manager
    variable_manager = ansible.playbook.variable_manager.VariableManager()
    # Load some fake data
    data = dict()
    data['name'] = 'roles/common/tasks/main.yml'
    playbookInclude.load_data(ds=data, basedir='/path/to/playbook', variable_manager=variable_manager)
    # Check the result
    assert playbookInclude.import_playbook == 'roles/common/tasks/main.yml'



# Generated at 2022-06-13 08:46:36.817117
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    #import ansible.playbook.playbook_include
    pass

# Generated at 2022-06-13 08:46:37.492179
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:46:46.727500
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import pytest
    from ansible.playbook.play import Play

    pb = PlaybookInclude()
    test_string = "import_playbook=test/test.yaml tags=collect,debug"
    test_dict = { 'import_playbook': "test/test.yaml", 'tags': "collect,debug", 'vars': {'a': 'b', 'c': 'd'}}

    # Test 1
    included_playbook = pb.load(test_string, basedir=".")
    assert isinstance(included_playbook, Play)
    assert len(included_playbook._entries) == 1
    assert included_playbook._entries[0].tags == ['collect', 'debug']

    # Test 2

# Generated at 2022-06-13 08:46:59.947550
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.yaml.loader import AnsibleLoader

    class FakeVariableManager(object):
        def __init__(self, variables=None):
            self._vars = variables or {}

        def get_vars(self, loader=None, play=None, host=None, task=None):
            return self._vars


    def fake_loader(templar, ds, base_basedir):
        cls = ds.pop('class', None)
        if cls:
            return cls.load(ds, base_basedir, templar.variable_manager, templar._loader)
        return dict(ds)

    class FakePlay(PlaybookInclude):
        def __init__(self, ds):
            self._ds = ds


# Generated at 2022-06-13 08:47:12.067178
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.playbook import Playbook


# Generated at 2022-06-13 08:47:24.245383
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    """
    Creates a PlaybookInclude object and checks if it is correctly processed by the
    load_data method of the PlaybookInclude class.
    """
    
    # PlaybookInclude object
    pbio = PlaybookInclude()
    
    # Data structure to be processed
    ds = AnsibleMapping()
    ds['import_playbook'] = '"test_playbook.yml"'
    ds['vars'] = AnsibleMapping()
    ds['vars']['var1'] = 'val1'
    ds['vars']['var2'] = 'val2'
    ds['tags'] = ['tag1', 'tag2']
    
    
    # Expected result
    pbo = Playbook()

# Generated at 2022-06-13 08:47:37.587606
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    results = []

    # 1. load YAML with import_playbook and args
    new_ds = dict(import_playbook='test1.yml', tag_name='test')
    pbi = PlaybookInclude()
    pbi.load_data(new_ds)
    results.append(pbi.import_playbook == 'test1.yml')
    results.append(pbi.tags == ['test'])

    # 2. load YAML with import_playbook and args and vars

# Generated at 2022-06-13 08:47:38.359491
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass



# Generated at 2022-06-13 08:47:49.698561
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    basedir = os.path.expanduser('~')
    import_playbook = os.path.join(basedir, 'test.yml')
    data_loader = None
    variable_manager = None

    # test for import_playbook keyword
    ds = AnsibleMapping()
    ds['import_playbook'] = import_playbook
    pb = PlaybookInclude()
    pb.load_data(ds, basedir, variable_manager, data_loader)

    # test for include_playbook keyword
    ds = AnsibleMapping()
    ds['include_playbook'] = import_playbook
    pb = PlaybookInclude()
    pb.load_data(ds, basedir, variable_manager, data_loader)

    # test for playbook keyword
    ds

# Generated at 2022-06-13 08:48:05.712175
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # test load_data without imported playbook
    try:
        ds = dict(import_playbook="test.yaml")
        PlaybookInclude().load_data(ds, "/home/ansible/playbooks/")
    except AnsibleParserError as e:
        # pass the test if we get a parse error
        pass

    # test load_data with imported playbook
    from ansible.playbook import Playbook
    import os

    playbook_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../test/sanity/playbook/test_import.yml'))
    ds = dict(import_playbook=playbook_path)
    imported_playbook = PlaybookInclude().load_data(ds, "/home/ansible/playbooks/")


# Generated at 2022-06-13 08:48:17.121429
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()

    var_manager = VariableManager()
    var_manager.set_inventory(loader.load_inventory(path='tests/unit/vars/hosts'))

    ds = {'import_playbook': 'cisco_router_common.yml', 'vars': {'hostname': 'test'}}

    obj = PlaybookInclude()
    res = obj.load_data(ds, basedir='tests/unit/playbooks', variable_manager=var_manager, loader=loader)

    expected = '''<Playbook(include) (1): cisco_router_common.yml>'''
    assert repr(res) == expected


# Generated at 2022-06-13 08:48:29.607286
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pb = PlaybookInclude()

    # test invalid playbook import param
    # test invalid playbook import param
    ds = AnsibleMapping({'import_playbook': [1, 2]})
    with pytest.raises(AnsibleParserError, match="playbook import parameter must be a string indicating a file path, got list instead"):
        pb.load_data(ds, basedir='/tmp')
    ds = AnsibleMapping({'import_playbook': 'my_playbook.yml'})
    playbook = pb.load_data(ds, basedir='/tmp')
    assert playbook._entries[0]._included_path == '/tmp'

# Generated at 2022-06-13 08:48:37.475508
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.block import Block
    from ansible.inventory.host import Host

    basedir = os.path.join(os.path.dirname(__file__), 'playbook')
    variable_manager=None

    # test a basic playbook with no conditions nor tags
    playbook = PlaybookInclude.load(
        data={'import_playbook': 'subdir/subdir_playbook.yml'},
        basedir=basedir,
        variable_manager=variable_manager,
    )

# Generated at 2022-06-13 08:48:48.965883
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # First we create a minimally valid ds.
    from ansible.parsing.dataloader import DataLoader
    ds = dict(import_playbook='my_playbook')

    # Next we create minimally valid basedir and variable_manager
    from ansible.playbook.variable_manager import VariableManager
    basedir = 'tests/'
    variable_manager = VariableManager()

    # Finally we can test load_data
    from ansible.playbook.playbook_include import PlaybookInclude
    playbook_include = PlaybookInclude()
    playbook_include.load_data(ds, basedir, variable_manager)

    # The result of this test is a PlaybookInclude object,
    # which is not what is required as a result
    # I don't know how to deal with this
    # assert playbook_include

# Generated at 2022-06-13 08:48:57.549375
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Import here to avoid dependency loop
    from ansible.playbook import Playbook
    import pytest
    with pytest.raises(AnsibleParserError) as excinfo:
        PlaybookInclude.load(data={'import_playbook': ''}, basedir='.')
    assert 'playbook import parameter is missing' in str(excinfo.value)
    with pytest.raises(AnsibleParserError) as excinfo:
        PlaybookInclude.load(data={'import_playbook': 123}, basedir='.')
    assert 'playbook import parameter must be a string' in str(excinfo.value)

# Generated at 2022-06-13 08:48:58.163436
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:49:12.410859
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task.include import IncludeTask
    # import here to avoid a dependency loop
    from ansible.playbook import Playbook

    # test loading a simple playbook include
    ds = dict(
        import_playbook='../vms.yml'
    )

    # load it up!
    pb_include = PlaybookInclude.load(ds, '/path/to/my/dir', None, None)

    # and assert that the new instance has proper attributes
    assert isinstance(pb_include, Playbook)
    assert len(pb_include._entries) == 1
    assert pb_include._entries[0].name is None
    assert isinstance(pb_include._entries[0], Play)

# Generated at 2022-06-13 08:49:25.185624
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook
    pb = Playbook.load('/tmp/test_plays.yml', 'localhost')
    assert isinstance(pb, Playbook)
    assert len(pb._entries) == 2
    assert isinstance(pb._entries[0], Play)
    assert isinstance(pb._entries[1], Play)
    # noinspection PyProtectedMember
    assert pb._entries[0]._included_path == '/tmp'
    # noinspection PyProtectedMember
    assert pb._entries[1]._included_path == '/tmp'


# Generated at 2022-06-13 08:49:27.938388
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    """
    Test cases for method load_data of class PlaybookInclude
    """
    pass

# Generated at 2022-06-13 08:49:46.555917
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.playbook
    import ansible.inventory
    import ansible.parsing.dataloader
    import ansible.vars
    import ansible.template
    import ansible.constants as C

    fake_loader = DictDataLoader({
        "test_playbook_include_load.yml": """
        ---
        - hosts: all
          gather_facts: no
          import_playbook: tasks.yml
        """,
        "tasks.yml": """
        ---
        - name: test
          shell: echo hello world
        """,
    })

    p = PlaybookInclude.load(dict(import_playbook='test_playbook_include_load.yml'), basedir='/does/not/matter', loader=fake_loader)

    # p should be a playbook


# Generated at 2022-06-13 08:49:58.247498
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.playbook.play as play
    import ansible.playbook.plays as plays
    import ansible.playbook.block as block
    from ansible.utils.sentinel import Sentinel

    # Create an empty PlaybookInclude object
    playbook_include_obj = PlaybookInclude()

    # Create a Playbook object with a single play
    play_obj = play.Play()
    task_obj = play_obj.add_block(block.TaskBlock())
    task_obj.add_task(dict(action=dict(module='ping')))

    # Create a Playbook object with a single play
    playbook_obj = plays.Playbook()
    playbook_obj.add_play(play_obj)

    # Get the ds to load in our PlaybookInclude object
    ds = playbook_obj.get_data_

# Generated at 2022-06-13 08:50:10.037490
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.handler import Handler
    from ansible.vars import VariableManager

    layout = '''
    ---
    - hosts: test
      var1:
        test: "{{ blah }}"
    '''.strip()

    def create_playbook_include(layout):
        import tempfile
        import shutil
        import ansible.playbook.playbook_include as PlaybookInclude
        tmpdir = tempfile.mkdtemp(prefix='ansible_')
        include_file = os.path.join(tmpdir, 'test_playbook.yml')

# Generated at 2022-06-13 08:50:15.656546
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    
    from ansible.playbook import Playbook
    
    playbook_include = PlaybookInclude()
    playbook_include.vars = dict()
    playbook_include.import_playbook = "playbook.yml"
    
    playbook_include.load_data(ds=dict(), basedir="", variable_manager=None, loader=None)
    
    result = isinstance(playbook_include, Playbook)
    assert result

# Generated at 2022-06-13 08:50:28.121218
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook

    pbi = PlaybookInclude()

    # test import_playbook: fails when no variable_manager is provided
    ds = AnsibleMapping(dict(import_playbook="test_playbook"))
    try:
        result = pbi.load_data(ds, ".")
        assert False, "Should have raised Exception but didn't"
    except Exception as err:
        assert isinstance(err, AnsibleParserError)

    # test import_playbook: fails when variable_manager is not a dict
    ds = AnsibleMapping(dict(import_playbook="test_playbook"))

# Generated at 2022-06-13 08:50:38.733842
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import sys
    # stubs
    class stub_loader:
        def path_dwim(self, s):
            return s

    class stub_variable_manager:
        class stub_variable_manager_getter:
            def get_vars(self):
                return {'a': 'b'}
        getter = stub_variable_manager_getter()

    class stub_Templar:
        def __init__(self, loader=None, variables=None):
            pass
        def template(self, s):
            return s

    class stub_PlayBook:
        def __init__(self, loader=None):
            pass

# Generated at 2022-06-13 08:50:49.174718
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import unittest
    import sys

    try:
        from unittest.mock import patch, mock_open, MagicMock
    except ImportError:
        from mock import patch, mock_open, MagicMock

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject

    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    from ansible.playbook.include import PlaybookInclude

    loader = DataLoader()
    variable_manager = VariableManager()

    PlaybookInclude.load_data = MagicMock()

    test_playbook_include_file = __file__

    my_base = None

# Generated at 2022-06-13 08:51:02.397341
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    import os
    import ansible.playbook.playbook
    import ansible.playbook.task
    import ansible.playbook.taggable
    import ansible.playbook.role
    import ansible.playbook.block

    playbook_include = ansible.playbook.playbook_include.PlaybookInclude()

    basedir = '/home/sherlock/workspace/ansible/test/unit/playbooks'
    # playbook = "playbook.yml"
    # playbook = "/home/sherlock/workspace/ansible/test/unit/playbooks/playbook.yml" #TODO: fixme
    playbook = os.path.join(basedir, 'playbook.yml')
    variable_manager = None
    loader = None

    data = {'import_playbook': playbook}
   

# Generated at 2022-06-13 08:51:14.761959
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.utils.collection_loader import AnsibleCollectionConfig

    AnsibleCollectionConfig.clear_defaults()

    dname = os.getcwd()
    file_name = '../../lib/ansible/playbook/data/playbook_include_preprocess_data.yml'
    file_name = os.path.join(dname, file_name)

    with open(file_name) as f:
        yaml_text = f.read()
        playbook_include = PlaybookInclude()
        playbook_include.load_data(yaml_text)

# Generated at 2022-06-13 08:51:23.639609
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import json
    from ansible.playbook.play_context import PlayContext

    # sample Playbook entry
    playbook_include_data = '''
    - hosts:
      - alpha
      connection: local
      gather_facts: no
      import_playbook: 'test.yml'
      vars:
        upstream: 'foo'
      tags:
        - foo_tag
        - bar_tag
      roles:
        - { role: some_role, x: 42 }
      tasks:
        - name: task 1
          debug:
            msg: task 1
    '''
    playbook_include_ds = AnsibleMapping.load(playbook_include_data)

    x = PlaybookInclude()
    basedir = './'
    variable_manager = PlayContext()


# Generated at 2022-06-13 08:41:54.516291
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook import Playbook
    from ansible.vars import VariableManager
    from ansible.module_utils.common._collections_compat import Sequence

    print("Testing PlaybookInclude.load_data()")

    dl = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=dl, variable_manager=variable_manager, host_list="localhost")
    pb = Playbook()

    # Load a single playbook
    pb.load("../lib/ansible/playbook/test/playbooks/playbook_include1.yml", variable_manager=variable_manager, loader=dl)

# Generated at 2022-06-13 08:42:04.024417
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import io
    ds = io.StringIO('''---
    - include: /etc/ansible/include.yml
      tags:
        - true
      with_items:
         - 1
         - 2
         - 3
      vars:
        - x: 1
          l: 2
      when: false
      register: foo
    ''')

    from ansible.playbook import Playbook
    pb = PlaybookInclude.load(yaml_data=ds, basedir='/etc/ansible/')
    assert isinstance(pb, Playbook)

# Generated at 2022-06-13 08:42:13.615296
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    data = {
        'one': 'two',
        'three': 'four'
    }
    pi = PlaybookInclude()
    new_ds = pi.preprocess_data(data)
    assert(isinstance(new_ds, dict))
    assert(len(new_ds)) == 2
    assert('one' in new_ds)
    assert('two' == new_ds['one'])
    assert('three' in new_ds)
    assert('four' == new_ds['three'])

    data = {
        'import_playbook': 'path',
        'one': 'two'
    }
    pi = PlaybookInclude()
    new_ds = pi.preprocess_data(data)
    assert(isinstance(new_ds, dict))
    assert(len(new_ds)) == 2


# Generated at 2022-06-13 08:42:23.728690
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # Given
    playbook_include = PlaybookInclude()


# Generated at 2022-06-13 08:42:30.886864
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.playbook.playbook
    import ansible.playbook.play as play
    import ansible.playbook.block as block

    # ---
    # Setup tests
    # ---
    pb = PlaybookInclude()
    basedir = "/path/to/basedir"

    # ---
    # Test exception when the playbook include is not an AnsibleMapping
    # ---
    ds = {"import_playbook": "test.yml"}

    try:
        pb.load_data(ds, basedir)
        assert False, "Should have raised an AnsibleAssertionError"
    except AnsibleAssertionError:
        pass

    # ---
    # Test exception when playbook include is missing playbook key
    # ---
    ds = AnsibleMapping()


# Generated at 2022-06-13 08:42:34.120588
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Use relative path for playbook_include.yml file
    test_dir = os.path.dirname(os.path.abspath(__file__))
    test_file = os.path.join(test_dir, 'playbook_include.yml')

    # Verify data are properly loaded
    PlaybookInclude.load(data=test_file)

# Generated at 2022-06-13 08:42:35.643976
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # TODO
    pass

# Generated at 2022-06-13 08:42:43.055969
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    class AnsibleMock(object):
        class AnsibleMapping(object):
            def __init__(self):
                self._data = dict()

            def __getitem__(self, name):
                return self._data

            def __setitem__(self, key, value):
                self._data[key] = value

    # Mock display
    class DisplayMock(object):
        def deprecated(self, msg, version):
            pass

    class PlaybookIncludeMock(PlaybookInclude):
        def __init__(self):
            pass

    pi = PlaybookIncludeMock()
    pi.display = DisplayMock()

    # Test import_playbook with no parameters and no vars
    am = AnsibleMock()
    ds = am.AnsibleMapping()

# Generated at 2022-06-13 08:42:51.601989
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # Create a sample dictionary to use as input
    input_ds = {
        'import_playbook': 'playbook.yml',
        'tags': ['foo'],
        'vars': {
            'foo': 'gaz'
        }
    }

    # Instantiate a PlaybookInclude object
    playbook_include = PlaybookInclude()

    # Call preprocess_data
    output_ds = playbook_include.preprocess_data(input_ds)

    # Check the resulting object
    assert output_ds == { 'import_playbook': 'playbook.yml', 'tags': ['foo'], 'vars': { 'foo': 'gaz' } }

# Generated at 2022-06-13 08:43:05.813179
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import RoleInclude

    import ansible.constants as C
    C.ANSIBLE_INCLUDES_DIRS = ["./test/include"]

    import os

    def get_playbook_inclusion_file(filename):
        playbook_inclusion_file = os.path.join(os.path.split(__file__)[0], "..", "..", "..", "test", "playbook", "inclusions", filename)
        return playbook_inclusion_file

# Generated at 2022-06-13 08:43:23.064112
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.playbook.playbook import Playbook
    from ansible.template import Templar


    test_hosts = "hostname1\nhostname2\n"
    test_vars = "{'a': 'A', 'b': 'B'}"
    test_name = 'test'
    test_tasks = [
        {"name": "task1", "action": "action1"},
        {"name": "task2", "action": "action2"}
    ]


    # Test when playbook.yml is included.

# Generated at 2022-06-13 08:43:34.565908
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # Mock Playbook
    class PlaybookClass:
        def __init__(self):
            self._entries = []
        def _load_playbook_data(self, file_name, variable_manager, vars):
            pass


    # Mock Play
    class PlayClass:
        def __init__(self):
            self._included_conditional = None
            self._included_path = None
            self.vars = {}
            self.tags = []
            self.pre_tasks = []
            self.tasks = []
            self.post_tasks = []
            self.roles = []
        pre_tasks = []
        tasks = []
        post_tasks = []
        roles = []

    # Mock Base

# Generated at 2022-06-13 08:43:46.769338
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    # create object
    import_playbook = PlaybookInclude()

    # check that empty dictionary throws an exception
    data = {}
    try:
        import_playbook.preprocess_data(data)
    except AnsibleAssertionError:
        pass
    else:
        raise AssertionError('Empty dictionary should throw AssertionError')

    # check that non-dictionary data throws an exception
    data = AnsibleBaseYAMLObject()
    try:
        import_playbook.preprocess_data(data)
    except AnsibleAssertionError:
        pass
    else:
        raise AssertionError('Non-dict object should throw AssertionError')

    # check that import_playbook without a file path throws an exception
    data = AnsibleMapping({'import_playbook': None})

# Generated at 2022-06-13 08:43:55.413261
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.play import Play
    import os

    curr_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(curr_dir, '..', 'fixtures', 'deprecation_warning')

    # build the include object
    ds = dict(
        import_playbook=os.path.join(base_dir, 'playbook2.yml'),
        vars=dict(a=1)
    )
    pb = PlaybookInclude.load(ds, curr_dir)

    # test the resulting object
    assert isinstance(pb, Play)
    #assert isinstance(pb.t

# Generated at 2022-06-13 08:44:05.917628
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    '''
    Non-regression test for function load_data.
    '''
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.loader import AnsibleLoader

    # Test without a variable manager
    import_playbook_path = "./test_playbook_include.yml"
    variable_manager = None
    loader = 'AnsibleLoader'
    basedir = os.path.dirname(__file__)
    yaml_data = b'''
    - import_playbook: {0}
      vars:
        imported_variable_def: 42
      tags:
        - imported_tag
        - imported_tag_bis
    '''.format(import_playbook_path)

# Generated at 2022-06-13 08:44:10.079020
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    import ansible.playbook.play
    pb = Playbook()
    assert isinstance(pb, Playbook)



# Generated at 2022-06-13 08:44:18.920085
# Unit test for method preprocess_data of class PlaybookInclude

# Generated at 2022-06-13 08:44:27.037155
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    #import here to avoid loop
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    class MockLoader(object):
        pass

    basedir = os.path.abspath("test_data/test_playbook_include")
    file_name = os.path.join(basedir, "play_to_include.yml")

    pb_include = PlaybookInclude(loader=MockLoader())

    data = {
        "import_playbook": file_name,
        "tags": "",
        "when": ""
    }

    # Call the load_data of PlaybookInclude
    pb = pb_include.load_data(data, basedir)

    # Confirm we got a Playbook object
    assert isinstance(pb, Playbook)
    assert len

# Generated at 2022-06-13 08:44:37.693603
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    playbook_data = """
    - hosts: all
      import_playbook: test.yml
    """
    import_playbook_data = """
    - hosts: localhost
      tasks:
        - debug:
            msg: test
    """

    # For testing, we need to mock the open function
    import __builtin__
    import StringIO
    class Open(object):
        def __init__(self):
            self.count = 0
            self.file_name = ''

        def __call__(self, file_name):
            self.count += 1
            self.file_name = file_name
            if self.count == 1:
                return StringIO.StringIO(playbook_data)
            elif self.count == 2:
                return StringIO.StringIO(import_playbook_data)
           

# Generated at 2022-06-13 08:44:43.846721
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    playbook_include = PlaybookInclude()
    playbook = Playbook(loader=None)
    playbook_include.load_data("test_data.yaml", "/tmp/path/")
    assert isinstance(playbook_include, PlaybookInclude)

# Generated at 2022-06-13 08:44:59.451345
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    import sys
    import json

    from collections import namedtuple

    from ansible.parsing.yaml.loader import AnsibleLoader

    FakeArgs = namedtuple('FakeArgs', ['tags', 'skip_tags', 'syntax'])

    # Make a fake args object
    args = FakeArgs(tags='all', skip_tags='none', syntax='ansible')

    # Make a fake loader object
    loader = AnsibleLoader(args, None, sys.stdin)

    # Create a fake ds
    ds = {
        'include_tasks': 'roles/foo/tasks/main.yaml',
        'tags': 'foo,bar',
        'vars': {'ansible_connection': 'local'},
    }

    # Call method PlaybookInclude.preprocess_data
    result = Playbook

# Generated at 2022-06-13 08:45:04.435442
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    '''
    Function to test method load_data of class PlaybookInclude

    :return:
    '''

    ds = './test/unit/parsing/yaml/fixtures/playbook_include.yml'
    basedir = './test/unit/parsing/yaml/fixtures/playbook_include'

    try:
        import_playbook = PlaybookInclude().load_data(ds=ds, basedir=basedir)

    except Exception as e:
        assert False, "Test failed stub: {}".format(e)

    else:
        assert True

# Generated at 2022-06-13 08:45:15.102245
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext

    class MockPlaybook(Playbook):
        def __init__(self):
            self.playbook = "./playbooks/internal.yml"
            self.vars = {
                'internal_var': "internal_value",
            }
            self.extra_vars = {
                'external_var': "external_value",
            }
            self.variable_manager = "variable_manager"
            self.loader = "loader"
            self.options = "options"
            self.passwords = "passwords"
            self.inventory = "inventory"
            self.loader_cache = "loader_cache"
            self.play_context = "play_context"
            self.basedir = "."

# Generated at 2022-06-13 08:45:23.563977
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    ds = AnsibleMapping({
        'import_playbook': 'my_play.yml',
        'vars': {
            'name': 'Test',
            'tags': 'test'
        },
        'tags': 'TestOne',
        'when': '1'
    })
    import_obj = PlaybookInclude()
    new_ds = import_obj.preprocess_data(ds)
    # Check if the returned value is what we expect
    assert new_ds['vars'] == {'name': 'Test'}
    assert new_ds['tags'] == ['TestOne']
    assert new_ds['when'] == ['1']
    assert new_ds['import_playbook'] == 'my_play.yml'


# Generated at 2022-06-13 08:45:36.187566
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    import imp
    import sys

    from ansible.playbook import Playbook
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.display import Display
    from ansible.utils.vars import combine_vars
    from ansible.plugins.callback import CallbackBase

    display = Display()

    # ansible python API
    class CallbackModule(CallbackBase):
        CALLBACK_VERSION = 2.0
        CALLBACK_TYPE = 'stdout'
        CALLBACK_NAME = 'debug'

        def v2_runner_on_ok(self, result):
            host = result._host

# Generated at 2022-06-13 08:45:48.179041
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # Test for error handling
    result = {'import_playbook': None}
    obj = PlaybookInclude()
    with pytest.raises(AnsibleParserError) as excinfo:
        obj.preprocess_data({'import_playbook': None})
    assert excinfo.value.message == 'playbook import parameter is missing'

    with pytest.raises(AnsibleParserError) as excinfo:
        obj.preprocess_data({'import_playbook': 1})
    assert excinfo.value.message == 'playbook import parameter must be a string indicating a file path, got <class \'int\'> instead'

    with pytest.raises(AnsibleParserError) as excinfo:
        obj.preprocess_data({'import_playbook': 'test.yml'})
    assert excinfo.value

# Generated at 2022-06-13 08:46:00.998014
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible import context
    from ansible.config.manager import ConfigManager
    from ansible.module_utils.common.removed import removed_module
    from ansible.variable_manager import VariableManager

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    def setUpModule():
        context._init_global_context(ConfigManager())

    def tearDownModule():
        context._clear_global_context()

    setUpModule()

    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    class TestPlaybookIncludeLoadData(unittest.TestCase):

        playbook_include = None
        variable_manager = None


# Generated at 2022-06-13 08:46:13.397818
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.playbook.play as play
    import ansible.playbook.playbook as playbook
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    # def load_data(self, ds, basedir, variable_manager=None, loader=None):

    # TODO: variable_manager and loader are not tested

    import sys
    import tempfile
    import shutil
    import os
    import json

    # test creating a temp directory
    temp_dir = tempfile.mkdtemp()

    # create a simple playbook with single play
    playbook_name = temp_dir + os.sep + 'test_PlaybookInclude_load_data.yaml'

# Generated at 2022-06-13 08:46:21.993764
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    # Test without when
    vars = dict()
    vars["foo"] = "Foo"
    vars["bar"] = "Bar"
    pb = PlaybookInclude().load_data(ds="foo.yml", basedir="/tmp", variable_manager=vars, loader="")
    assert isinstance(pb, Playbook)
    assert len(pb.get_plays()) == 1
    assert isinstance(pb.get_plays()[0], Play)
    assert pb.get_plays()[0].vars["foo"] == "Foo"
    assert pb.get_plays()[0].vars["bar"] == "Bar"

    # Test with when
    vars = dict()

# Generated at 2022-06-13 08:46:33.370356
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    import os
    import tempfile
    import shutil

    test_dir = tempfile.mkdtemp()
    test_playbook_path = os.path.join(test_dir, 'main.yml')
    with open(test_playbook_path, 'w') as f:
        f.write('''
- include_playbook: included.yml
  vars:
    include_var: "{{ play_var }}"
    play_var: defined in main
''')

    test_include_playbook_path = os.path.join(test_dir, 'included.yml')

# Generated at 2022-06-13 08:46:46.830762
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from unit.mock.loader import DictDataLoader

    pbi = PlaybookInclude()
    data = dict(import_playbook='../test_playbook.yml', 
        vars=dict(a=1, b='foo'),
        when=['a > 1', 'b == "foo"'])

# Generated at 2022-06-13 08:47:00.027394
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import yaml
    from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleMapping
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task

    data = yaml.safe_load("""
---
- hosts: all
  import_playbook: test_playbook_import.yml
  vars:
    var1: value1
    var2: value2
    var3:
        - value3_1
        - value3_2
        - value3_3
  tasks:
  - name: task1
  - name: task2
""")

    # test normal behaviour

# Generated at 2022-06-13 08:47:05.462662
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    pb = PlaybookInclude.load(
        data={'hosts': 'localhost', 'connection': 'local', 'import_playbook': 'test-playbook.yml', 'vars': {'a': 2}},
        basedir="/home/user",)
    assert isinstance(pb, Playbook)

# Generated at 2022-06-13 08:47:07.002591
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    raise NotImplementedError


# Generated at 2022-06-13 08:47:14.731091
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import yaml
    yaml_obj = yaml.load("""
    - hosts: all
      tasks:
        - import_playbook: nested.yml
          vars:
            var1: value1
            var2: value2
          tags: tag1,tag2
        - include_tasks: tag1
    """)
    playbook = PlaybookInclude()
    data = playbook.load_data(yaml_obj[0], "/some/path/to/a/playbook")
    assert playbook._entries[0]._entries[1].vars == {'var1': 'value1', 'var2': 'value2' }

# Generated at 2022-06-13 08:47:25.853828
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    loader = None
    variable_manager = None
    basedir = None

    # Mock constructor of class PlaybookInclude
    playbook_include = PlaybookInclude

    # Mock constructor of class AnsibleMapping
    ansible_mapping = AnsibleMapping
    ansible_mapping.update = lambda *args, **kwargs: None
    ansible_mapping.copy = lambda *args, **kwargs: None
    ansible_mapping.keys = lambda *args, **kwargs: None
    ansible_mapping.__getitem__ = lambda *args, **kwargs: None
    ansible_mapping.__setitem__ = lambda *args, **kwargs: None
    ansible_mapping.__contains__ = lambda *args, **kwargs: None

# Generated at 2022-06-13 08:47:39.258519
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.role.include import RoleInclude
    # test playbook_inventory
    pb_include = PlaybookInclude()
    pb_include.vars = {'var1': 'abc', 'var2': 123}
    pb = pb_include.load_data(ds='playbook_inventory', basedir='/tmp/', variable_manager=None, loader=None)
    assert isinstance(pb, Playbook)
    assert len(pb._entries) == 3
    assert isinstance(pb._entries[0], Play)
    assert isinstance(pb._entries[1], Play)
    assert isinstance(pb._entries[2], Play)
    assert pb._entries[0].name == 'Create instances'
    assert pb._

# Generated at 2022-06-13 08:47:40.186861
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:47:43.763544
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pl = PlaybookInclude.load(
        """
    import_playbook: foo/bar.yml
    vars:
        foo: bar
    """, basedir='/')



# Generated at 2022-06-13 08:47:52.456560
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # set up the object
    playbook_include = PlaybookInclude()
    # create the test data
    data = {
        'import_playbook': 'test_import.yml',
        'vars': {'var_1': 'test'},
        'test': 'test',
        'test2': 'test2'
    }
    # call the method under test
    new_data = playbook_include.preprocess_data(data)
    # assert the result is what we expect
    assert isinstance(new_data, AnsibleMapping)
    assert len(new_data.keys()) == 2
    assert 'import_playbook' in new_data
    assert 'vars' in new_data
    assert new_data['vars'] == {'var_1': 'test'}

# Generated at 2022-06-13 08:48:06.380519
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    import platform, textwrap
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.playbook.play import Play

    # Arrange
    data = textwrap.dedent(
        """\
        hosts: all
        gather_facts: no
        tasks:
          - name: uname
            command: /bin/uname -a
        """)

    data2 = textwrap.dedent(
        """\
        import_playbook: test.yml
        """)

    tmpdir_name = tempfile.mkdtemp()
    path = os.path.join(tmpdir_name, 'test.yml')
    with open(path, 'w') as file:
        file.write(data)

    tmpdir_name2 = tempfile.mkdtemp()


# Generated at 2022-06-13 08:48:07.436217
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:48:08.612132
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    assert PlaybookInclude.load({}) is None

# Generated at 2022-06-13 08:48:22.458584
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    pi = PlaybookInclude()
    ds = { "playbookA.yml" : None }
    pi.preprocess_data(ds)
    assert pi.import_playbook == "playbookA.yml"
    assert pi.vars == {}
    ds = { "playbookA.yml" : "difficult_to_parse.yml" }
    pi.preprocess_data(ds)
    assert pi.import_playbook == "difficult_to_parse.yml"
    assert pi.vars == {}
    ds = { "playbookA.yml" : '"some vars"' }
    pi.preprocess_data(ds)
    assert pi.vars == {}
    ds = { "playbookA.yml" : "Some" }
    pi.preprocess_

# Generated at 2022-06-13 08:48:24.366267
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # TODO: Write test
    # print("TODO: Write test")
    pass

# Generated at 2022-06-13 08:48:34.583300
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    import_playbook = {'include': 'book.yaml'}
    playbook_include = PlaybookInclude()
    playbook_include.preprocess_data(import_playbook)
    assert playbook_include.import_playbook == 'book.yaml'

    # Check that we can mix include statements with variables

# Generated at 2022-06-13 08:48:48.067614
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.role
    import ansible.playbook.block

    #########################################################
    # Test load_data of PlaybookInclude
    #########################################################

    # test_load_data_ok: test when a PlaybookInclude is correctly loaded
    def test_load_data_ok(monkeypatch):

        import tempfile

        # The PlaybookInclude object to be tested
        PlaybookInclude_obj = PlaybookInclude()

        # Input data to be loaded
        ds = {
            'import_playbook': 'myPlaybook.yml'
        }

        # Expected output
        play1 = ansible.playbook.play.Play()

# Generated at 2022-06-13 08:48:55.804812
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    pytest_check = False


# Generated at 2022-06-13 08:49:10.557737
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook as AnsiblePlaybook
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.block import Block

    test_yaml = '''
    - import_playbook: test_import_playbook.yml
      vars:
        foo: "bar"
        baz: "quux"
        tags: name
      when: false
    '''
    test_yaml_object = PlaybookInclude.load(data=test_yaml, basedir=".")
    assert isinstance(test_yaml_object, PlaybookInclude)
    assert isinstance(test_yaml_object.load_data(data=test_yaml, basedir="."), AnsiblePlaybook)
   

# Generated at 2022-06-13 08:49:19.629242
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.playbook.play import Play
    from ansible.playbook.playbook_include import PlaybookInclude

    playbook = """
    - hosts: localhost
      vars:
          var1: foo
      import_playbook: imported.yaml
      tasks:
      - name: task1
        debug: msg="hello world"
        when: var1 != "foo"
    """

    imported_playbook = """
    - hosts: all
      vars:
        var2: bar
      tasks:
      - name: task2
        debug: msg="{{ var2 }}"
    """

    import os
    import shutil


# Generated at 2022-06-13 08:49:38.057175
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    import ansible.playbook.playbook
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.task import Task

    yaml_tag = u'!include'
    yaml_content = u'playbook.yml\n'

    kwargs = {
        '_import_playbook':u'playbook.yml',
        '_vars':{}
    }
    pb_include = PlaybookInclude(**kwargs)

    vars = {'a':'b', 'b':'c'}
    basedir = "."
    variable_manager = 'dummmy'
    loader = 'dummy'

    playbook = 'playbook.yml'
    playbook_collection = None

    pb = pb

# Generated at 2022-06-13 08:49:50.254965
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    test_data = """
        # import some tasks
        - import_playbook: common.yml
        - import_playbook: common.yml vars: foo: 5
        - import_playbook: common.yml vars:
            foo: 5
            baz: 6
        - import_playbook: common.yml tags: foobar,baz
        - import_playbook: common.yml someparam: barfoo tags: foobar,baz
        - import_playbook: common.yml someparam: barfoo tags: foobar,baz
          vars: foo: 5
        - import_playbook: common.yml vars: foo: 5
          someparam: barfoo tags: foobar,baz
    """

    from ansible.playbook.play_context import PlayContext

# Generated at 2022-06-13 08:50:00.833332
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    import os
    import pprint
    from ansible.playbook import Play

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib

    collections_paths = [f'{os.path.dirname(__file__)}/../../../'
                         f'../../ansible_collections/nsweb/test']

    collection_loader = AnsibleCollectionConfig(collections_paths=collections_paths,
                                                ansible_config=None)
    loader = AnsibleLoader(None, variable_manager=None, collection_loader=collection_loader)
    ds = loader.load_from_file('playbook_include.yml')[0]

    assert ds[0].import_playbook == 'test_playbook.yml'

# Generated at 2022-06-13 08:50:12.361508
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Test without a variable manager
    p = PlaybookInclude()
    ds = dict()
    ds['import_playbook'] = "test.yaml"
    ds['tags'] = ['test']
    ds['vars'] = dict()
    ds['vars']['var1'] = "var1"
    basedir = os.path.abspath(os.path.dirname(__file__))
    new_pb = p.load_data(ds, basedir)
    assert new_pb is not None
    assert len(new_pb._entries) == 1
    assert(new_pb._entries[0].tags == ['test'])
    assert(new_pb._entries[0].vars == dict(var1="var1"))

# Generated at 2022-06-13 08:50:23.491505
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import mock

    ds = dict(
        _import_playbook='test.pb',
    )

    Variable_mock = mock.MagicMock()
    Variable_mock.get_vars.return_value = dict()
    Runner_mock = mock.MagicMock()
    Runner_mock.return_value.get_subset_vars.return_value = dict()
    Runner_mock.return_value.noop_task_vars = dict()

    p = PlaybookInclude.load(data=ds, basedir='', variable_manager=Variable_mock, loader=None)

    assert p._import_playbook == 'test.pb'
    assert p._vars == dict()
    assert p.tags == list()
    assert p.when == list()

# Generated at 2022-06-13 08:50:32.826658
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.vars.clean import module_response_deepcopy

    import yaml
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    yaml.add_representer(
        AnsibleVaultEncryptedUnicode,
        lambda dumper, value: dumper.represent_scalar(u'tag:yaml.org,2002:str', u'')
    )

    # test if an import_playbook works with a regular playbook
    from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-13 08:50:33.459608
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:50:41.646379
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    pb_inc = PlaybookInclude()
    pb = pb_inc.load_data('test.yml', None, None)
    assert isinstance(pb, Playbook)
    assert len(pb._entries) == 1
    assert isinstance(pb._entries[0], Play)

# Generated at 2022-06-13 08:50:51.248530
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()

    variable_manager = VariableManager()
    variable_manager.extra_vars = {'test_var': 'test_value'}
    variable_manager.options_vars = {'test_option_var':'test_option_value'}

    play_context = PlayContext()


# Generated at 2022-06-13 08:51:04.298465
# Unit test for method load_data of class PlaybookInclude

# Generated at 2022-06-13 08:51:29.821877
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    p = PlaybookInclude()

    # Test role and a collection role
    basedir = '/test/basedir'
    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_host_variable('host1', 'var1', 'value1')
    variable_manager.set_host_variable('host2', 'var1', 'value2')

    # Test variable merging

# Generated at 2022-06-13 08:51:31.521621
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # FIXME
    pass

# Generated at 2022-06-13 08:51:41.146951
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    # TEST1
    # Case where ds is valid and both import_playbook and vars keywords are present.
    # Also, Testing that the method handles duplicate key names.
    ds = {'import_playbook': 'ansible/playbook.yml', 'tags': ['one','two'], 'vars': {'foo': 'bar'}, 'import_playbook': 'another.yml'}

    new_ds = AnsibleMapping()
    new_ds['import_playbook'] = 'another.yml'
    new_ds['tags'] = 'one,two'
    new_ds['vars'] = {'foo': 'bar'}
    pbinclude = PlaybookInclude()

    test_ds = pbinclude.preprocess_data(ds)
    assert new_ds == test_ds
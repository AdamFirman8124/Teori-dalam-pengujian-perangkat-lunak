

# Generated at 2022-06-13 08:41:54.305634
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import tempfile
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    # Prepare a temporary folder for testing
    temp_folder = tempfile.mkdtemp()
    test_file_path = os.path.join(temp_folder, 'include_playbook_test.yml')

    # Write playbook data to the temporary file
    playbook_data = """
    - hosts: localhost
      vars:
        a: 1
        b: 2
      tasks:
        - debug:
            msg: "{{ a }}"
    """


# Generated at 2022-06-13 08:42:06.854480
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    # Test import_playbook in dict format
    ds = dict(
        import_playbook='playbook.yml',
        vars=dict(
            x='a'
        )
    )
    ds = PlaybookInclude(ds=ds, collection_loader=None, variable_manager=None)._preprocess_data(ds)
    assert 'import_playbook' in ds
    assert 'vars' in ds

    # Test import_playbook in list format
    ds = dict(
        import_playbook=['playbook.yml', 'x=a']
    )
    ds = PlaybookInclude(ds=ds, collection_loader=None, variable_manager=None)._preprocess_data(ds)
    assert 'import_playbook' in ds

# Generated at 2022-06-13 08:42:15.318252
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import yaml
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    virtualenv = os.environ.get('VIRTUAL_ENV')
    if virtualenv:
        ansible_base = os.path.join(virtualenv, 'lib', 'python%s' % sys.version_info[0], 'site-packages', 'ansible')
    else:
        ansible_base = os.path.dirname(__file__)

    # FIXME
    # basedir = os.path.join(os.path.dirname(ansible_base), 'lib', 'ansible', 'playbooks')
    basedir = 'playbooks'

    print(basedir)

    loader = DataLoader()



# Generated at 2022-06-13 08:42:25.173868
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    """Test for PlaybookInclude.preprocess_data"""


# Generated at 2022-06-13 08:42:26.056402
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    assert False, "Test not implemented"



# Generated at 2022-06-13 08:42:33.759306
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role

    import os

    dir_current = os.path.dirname(os.path.realpath(__file__))
    dir_parent = os.path.normpath(os.path.join(dir_current, '../'))
    dir_test = os.path.join(dir_parent, 'lib/ansible/playbook/test_data')

    variable_manager = DummyVars()
    loader = DummyLoader()

    base = PlaybookInclude()

# Generated at 2022-06-13 08:42:48.138079
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import json
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager

    variable_manager = VariableManager()
    loader = DataLoader()
    context = {}
    variable_manager.extra_vars = context

    # Open playbook
    examples_playbook = os.path.abspath("../../../examples/playbook.yml")
    workspace = os.path.abspath("../../../examples/workspace")
    inventory_file = os.path.abspath("../../../examples/inventory/localhost")

# Generated at 2022-06-13 08:42:56.108830
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook

    # create playbookInclude object
    pb = PlaybookInclude()
    # create data
    data = {'import_playbook': 'playbook.yml'}
    # set current working dir
    basedir = '.'

    # execute load_data method
    result = pb.load_data(data, basedir)

    # test result
    assert isinstance(result, Playbook)

# Generated at 2022-06-13 08:43:07.884862
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.utils.addresses import parse

    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.playbook.pre_task import PreTask
    from ansible.playbook.post_task import PostTask
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsV

# Generated at 2022-06-13 08:43:17.358154
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler

    # A single task in a play that invokes a role
    spec = '''
    - hosts: localhost
      tasks:
        - name: role test task
          include_role:
            name: myrole
    '''

    play = Play.load(spec, variable_manager=None, loader=None)

    # A single task that invokes an import_playbook
    spec = '''
    - import_playbook: test_import_playbook.yml
    '''

    import_playbook = PlaybookInclude.load(spec, basedir='/tmp', variable_manager=None, loader=None)

    # A single task that invokes an import_playbook with additional

# Generated at 2022-06-13 08:43:25.995554
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    print("TODO")



# Generated at 2022-06-13 08:43:36.286790
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    collection_name = 'ansible_namespace.collection_name'

    abs_playbook_path = '/home/user/playbook.yml'
    abs_playbook_dir = os.path.dirname(abs_playbook_path)
    rel_playbook_path = 'playbook.yml'

    def test_case(expected_playbook_path, original_path_param, playbook_collection, playbook_paths):
        """
        Returns a PlaybookInclude loaded from the given params for testing load_data
        """
        class DummyVarManager:
            def get_vars(self):
                return {}
        from ansible.playbook.task.include_tasks import _load_include_tasks
        from ansible.playbook.task.include_role import _load_include_role
        import os


# Generated at 2022-06-13 08:43:38.254322
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    #TODO: write unit test
    pass


# Generated at 2022-06-13 08:43:50.812634
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    pb_include = PlaybookInclude()

    ds = {'import_playbook':'test_playbook.yml',
          'vars':{'foo': 'bar'},
          'tags':{'tag1', 'tag2'},
          'when':'not test_flag'}

    pb_include.load_data(ds, '/')
    assert pb_include.import_playbook == 'test_playbook.yml'
    assert pb_include.vars == ds['vars']
    assert pb_include.tags == ds['tags']
    assert pb_include.when == ds['when']


# Generated at 2022-06-13 08:44:01.236657
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import PlaybookInclude
    from ansible.playbook.play import Play
    import tempfile
    import shutil
    import copy

    # populate the config with some vars to be used
    config = {}
    config['vars'] = {
        'test1': 'test1',
        'test2': 'test2'
    }

    config_orig = copy.deepcopy(config)
    vars_orig = copy.deepcopy(config['vars'])

    # create a temp dir
    tmpdir = tempfile.mkdtemp()

    # create a test playbook
    playbook = '''
        ---
        - hosts: all
          tasks:
            - name: test play
              debug:
                msg: "test play msg"
    '''

    # create the playbook

# Generated at 2022-06-13 08:44:11.179436
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    class Options(object):
        def __init__(self):
            self.connection = "local"
            self.module_path = None
            self.forks = 5
            self.become = None
            self.become_method = None
            self.become_user = None
            self.check = False
            self.listhosts = None
            self.listtasks = None
            self.listtags = None
            self.syntax = None
            self.diff = False
            self.v = False
            self.private_key_file = None

    class FakeVariableManager(VariableManager):

        def __init__(self):
            pass

    options = Options()
    loader = DataLoader

# Generated at 2022-06-13 08:44:20.063521
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    loader = ':memory:'
    variable_manager = 'memory'
    fake_ds = '{"include": "/etc/ansible/roles/common/tasks/main.yml"}'
    pb = PlaybookInclude.load(fake_ds, loader, variable_manager)

    # test preprocess_data
    expected_results = '{"import_playbook": "/etc/ansible/roles/common/tasks/main.yml"}'
    assert pb.preprocess_data(fake_ds) == expected_results

# Generated at 2022-06-13 08:44:27.588661
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    import os
    import sys
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleMapping
    from ansible.plugins.loader import get_all_plugin_loaders

    for plugin_type, loader_class in get_all_plugin_loaders().items():
        for name, plugin_class in loader_class.all(class_only=True).items():
            if hasattr(plugin_class, '_preprocess_data') and not plugin_class.BYPASS_HOOK:
                ds = plugin_class(None).preprocess_data(None)
                if isinstance(ds, list):
                    ds = AnsibleSequence().load(ds)
                elif isinstance(ds, dict):
                    d

# Generated at 2022-06-13 08:44:37.703750
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleUnicode

    # test: 1
    data_str1 = '- include_playbook: "./example_playbook_1.yml"'
    ds1 = AnsibleSequence([AnsibleUnicode(data_str1)])
    new_ds1 = PlaybookInclude().preprocess_data(ds1)
    assert new_ds1 == {'import_playbook': './example_playbook_1.yml'}

    # test: 2
    data_str2 = '- include_playbook: "./example_playbook_2.yml" vars: '
    data_str2 += '  when: "{{ t_2 }}"'
    data

# Generated at 2022-06-13 08:44:38.951289
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:44:56.807074
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    class FakeDSAction(object):
        # Fake object to create a 'valid' datastructure
        def __init__(self, ds):
            self.ds = ds

        def __getattr__(self, name):
            return self.ds[name]

    # create a valid datastructure
    ds = FakeDSAction({
        'import_tasks': 'tasks/main.yml'
    })

    # run preprocess_data
    playbookInclude = PlaybookInclude()
    playbookInclude.preprocess_data(ds)

    # verify results
    assert playbookInclude.import_playbook == 'tasks/main.yml'


# Generated at 2022-06-13 08:45:02.467232
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    p = Playbook()
    p._entries = [PlaybookInclude(),]
    p.vars = {"test": "test2"}
    p.load_data({"import_playbook": "my/path/to/my/playbook/test.yaml", "vars": {"test": "test"}}, ".")
    assert isinstance(p.get_entries()[0], Play)

# Generated at 2022-06-13 08:45:10.161587
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    import_playbook = '../common/tasks/main.yml'
    playbook_include = {
        'import_playbook': import_playbook,
        'vars': {
            'test_var': 'test_value'
        },
        'tags': ['test_tag'],
    }
    playbook = PlaybookInclude.load(playbook_include, basedir='/home/user/ansible_project/playbooks')

    assert playbook._entries[0]._entries[0]._included_path is not None
    assert playbook._entries[0]._entries[0]._included_path == os.path.dirname(os.path.realpath(import_playbook))
    assert playbook._entries[0]._entries[0]._included_file is not None
    assert playbook

# Generated at 2022-06-13 08:45:20.436965
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # create a data structure
    ds = AnsibleMapping()
    ds.ansible_pos = (None, (1, 0))

    # create another data structure
    ds2 = AnsibleMapping()
    ds2.ansible_pos = (None, (3, 0))
    ds2['import_playbook'] = 'play1.yml'
    ds2['vars'] = {'var1': 'value1'}

    # create a third data structure
    ds3 = AnsibleMapping()
    ds3.ansible_pos = (None, (11, 0))
    ds3['import_playbook'] = 'play2.yml'
    ds3['some_other_param'] = 'some_other_value'

    # create a fourth data structure
    ds

# Generated at 2022-06-13 08:45:22.637141
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    #TODO: Implement unit test for method load_data of class PlaybookInclude
    raise NotImplementedError

# Generated at 2022-06-13 08:45:35.429027
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # make sure that when using an import, we still get the objects with the
    # tags and vars from the included object
    ds = dict(
        import_playbook='test_playbook.yml',
        tags=['foo'],
        vars=dict(a=7, b=8, c=9)
    )
    obj = PlaybookInclude()
    obj = obj.load_data(ds=ds, variable_manager=None, loader=None, basedir='/tmp')
    assert isinstance(obj, list)
    for entry in obj:
        assert isinstance(entry, Play)
        assert entry.vars['a'] == 7
        assert entry.vars['b'] == 8
        assert entry.vars['c'] == 9
        assert entry.tags == ['foo']

# Generated at 2022-06-13 08:45:36.598479
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass


# Generated at 2022-06-13 08:45:46.390357
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # initiate an instance of PlaybookInclude
    test_pb = PlaybookInclude()

    # load_data method works for dict
    test_pb.load_data(ds={'a': 'b'}, basedir='/tmp')

    # load_data method works for AnsibleBaseYAMLObject
    test_pb.load_data(ds=AnsibleBaseYAMLObject(), basedir='/tmp')

    # load_data method fails for list
    try:
        test_pb.load_data(ds=['a', 'b'], basedir='/tmp')
    except AnsibleAssertionError:
        pass



# Generated at 2022-06-13 08:45:55.266301
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    playbook_include = PlaybookInclude(None)

    invalid_formats = [
        '',
        [],
        {'import_playbook': 'test',
         'tags': [],
         'vars': {}},
        {'import_playbook': 'test',
         'import_playbook': 'test',
         'tags': [],
         'vars': {}},
        {'import_playbook': 'test',
         'tags': [],
         'tags': [],
         'vars': {}},
        {'import_playbook': 'test',
         'tags': [],
         'vars': {},
         'vars': {}},
    ]


# Generated at 2022-06-13 08:46:09.656947
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    yaml_text = u"""---
import_playbook: other.yml
vars:
  a: 1
  b: 2
  c: 3
  tags: foobar
when: (1==1) and (2==2) and (3==3)
...
"""
    ds = AnsibleMapping(yaml_text)
    pbi = PlaybookInclude()
    new_ds = pbi.preprocess_data(ds)

    assert 'import_playbook' in new_ds
    assert isinstance(new_ds['import_playbook'], string_types)
    assert new_ds['import_playbook'] == "other.yml"

    assert 'vars' in new_ds
    assert isinstance(new_ds['vars'], dict)

# Generated at 2022-06-13 08:46:21.118992
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import unittest.mock as mock
    from ansible.playbook.base import Base
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    data = {'import_playbook': 'some-playbook.yml'}
    data_class = PlaybookInclude.load(data, 'some-basedir', variable_manager, loader)
    assert type(data_class) == Base
    assert data_class._entries is None

# Generated at 2022-06-13 08:46:33.043991
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import sys
    import tempfile
    import yaml
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.utils.vars import merge_hash

    # Write playbook to a temporary file
    tmp_dir = tempfile.mkdtemp()
    playbook_file = os.path.join(tmp_dir, "main.yml")

# Generated at 2022-06-13 08:46:44.688974
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play

    vars = {"foo": "bar"}

    playbook = PlaybookInclude()
    import_playbook_file_name = 'include.yml'
    play_file_name = 'play.yml'
    playbook_vars = {"foo": "baz"}

    playbook_data = {
        'import_playbook': import_playbook_file_name,
        'vars': playbook_vars
    }
    playbook_data = playbook.preprocess_data(playbook_data)
    with open(play_file_name, "w") as play_opened_file:
        play_data = {
            'hosts': 'all',
            'vars': vars,
        }
        play_data = Play().preprocess_data(play_data)
       

# Generated at 2022-06-13 08:46:58.656472
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook.play import Play

    import_playbook = "import_playbook.yml"
    vars = {"vars": "value"}

    obj = PlaybookInclude()
    pb = obj.load_data({"import_playbook": import_playbook, "vars": vars}, "/example/path/")

    assert pb._entries[0].name == "collection.role"
    assert pb._entries[0].tags == ["tag1", "tag2"]
    assert pb._entries[0].vars == vars
    assert isinstance(pb._entries[1], Play)
    assert pb._entries[1].name == "play name"
    assert pb._entries[1].tags == ["tag1", "tag2"]
    assert pb._entries

# Generated at 2022-06-13 08:46:59.073665
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:47:05.469611
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook

    playbook_include = PlaybookInclude()

    # test load a playbook not in a collection
    playbook = playbook_include.load_data(
        ds={'import_playbook': '../../library/win_copy.yml', 'vars': {'src': 'bar'}},
        basedir='/home/user/ansible/demo/collections',
        variable_manager={},
        loader={}
    )
    assert isinstance(playbook, Playbook)
    assert [x for x in playbook._entries if isinstance(x, Play)]
    assert playbook._entries[0].vars == {'src': 'bar'}

    # test load a playbook in a collection
    playbook = playbook_include

# Generated at 2022-06-13 08:47:06.045746
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass # No unit-testable code in this function

# Generated at 2022-06-13 08:47:08.912541
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    playbook_include = PlaybookInclude()
    playbook_include.load_data(ds={}, basedir='.')



# Generated at 2022-06-13 08:47:16.634847
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    Display.verbosity = 4
    import yaml
    yaml.warnings({'YAMLLoadWarning': False})

    # Test processing of import_playbook that does not specify any variables
    data = yaml.safe_load('''
    - import_playbook: test_playbook.yml
    ''')
    # Test processing of import_playbook that specifies variables
    data = yaml.safe_load('''
    - import_playbook: test_playbook.yml
      vars:
        key1: value1
        key2: value2
    ''')
    # Test processing of import_playbook that specifies tags
    data = yaml.safe_load('''
    - import_playbook: test_playbook.yml
      tags: always
    ''')
    # Test processing

# Generated at 2022-06-13 08:47:17.318229
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:47:25.779996
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    p = PlaybookInclude()
    assert isinstance(p.load_data({'import_playbook': 'test.yml'}, 'c:/my_playbooks/'), Playbook)


# Generated at 2022-06-13 08:47:27.196487
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    pass

# Generated at 2022-06-13 08:47:39.120836
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    file_name = 'file1.yml'
    file_path = '/path/to/file1.yml'

    pb = PlaybookInclude.load(data={'import_playbook': file_name}, basedir='/path/to')
    assert file_name == pb._entries[0]._included_path
    assert file_name == pb._entries[0]._playbook_path

    pb = PlaybookInclude.load(data={'import_playbook': file_path}, basedir='/path/to')
    assert '/path/to' == pb._entries[0]._included_path
    assert file_path == pb._entries[0]._playbook_path

# Generated at 2022-06-13 08:47:40.507869
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass


# Generated at 2022-06-13 08:47:50.807317
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar

    import_playbook = "../../../test/test_roles/foo/import_playbook.yml"
    # this is the fake variable_manager from test_variable_manager

# Generated at 2022-06-13 08:47:57.845599
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    fail_msg = 'PlaybookInclude should return Playbook object on success'
    pb = PlaybookInclude()
    pb_loaded = pb.load_data(ds={
        'import_playbook': 'test_playbook.yaml'
    }, basedir=os.path.dirname(os.path.abspath(__file__)))

    assert(isinstance(pb_loaded, Playbook)), fail_msg


# Generated at 2022-06-13 08:48:06.918965
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    """
    Test that _load_playbook_data of class PlaybookInclude correctly loads a playbook
    """

    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.attribute import FieldAttribute
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    basedir = '/a/b/c'

    PlaybookInclude._valid_attrs = frozenset([
        'import_playbook',
        'vars'
    ])

    playbook_include = PlaybookInclude()


# Generated at 2022-06-13 08:48:08.431781
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # TODO: Add unit tests
    assert False

# Generated at 2022-06-13 08:48:10.997845
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # load_data method of class PlaybookInclude is tested in test_load_data of class PlaybookInclude
    pass

# Generated at 2022-06-13 08:48:16.138021
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    '''
    Makes sure load_data returns a Play object
    '''
    import ansible.playbook.play

    assert isinstance(PlaybookInclude.load_data({}, '/foo'), ansible.playbook.play.Play)

# Generated at 2022-06-13 08:48:32.018700
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.splitter import parse_kv, parse_yaml_from_text, split_args

    # Prepare test-bed

    data = '''
- include_playbook: test_playbook_include_playbook.yml
'''
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = Variable

# Generated at 2022-06-13 08:48:39.013673
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    import os
    import pytest

    src = os.path.join(os.path.dirname(__file__), "../playbooks")
    loader = DataLoader()

    args = dict(basedir=os.path.join(src, "i_vars"),
                loader=loader,
                variable_manager=VariableManager())

    ds = dict(import_playbook='../vars/main.yml', tags=['include_test'])
    pbi = PlaybookInclude.load(ds, **args)
    data = pbi.load_data(ds, **args)._entries[0]._ds


# Generated at 2022-06-13 08:48:50.151864
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.utils.vars import combine_vars
    ds = AnsibleMapping()
    ds['import_playbook'] = 'somefile.yml'
    play = Play()
    play._tasks = [
        TaskInclude(),
        TaskInclude()
    ]
    pb_include = PlaybookInclude()
    pb = pb_include.load_data(ds=ds, basedir="/path/to/directory/", variable_manager=combine_vars(dict(one="{{test_var}}"), dict(two="{{test_var2}}")))
    assert not pb._variable_

# Generated at 2022-06-13 08:48:56.314299
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # Define a test object
    class test_class:
        def __init__(self, _id):
            self._id = _id

    # test_obj = test_class("test")

    # instance of PlaybookInclude class
    test_instance = PlaybookInclude()

    # Define some data structure
    ds = {'import_playbook': 'test.yml'}
    basedir = './'

    # call method
    result = test_instance.load_data(ds, basedir)

    # Check the result
    assert(result is not None)

# Generated at 2022-06-13 08:48:56.808035
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:49:11.541361
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import sys
    import yaml

    old_argv = sys.argv
    sys.argv = ["ansible-playbook","--list-tasks"]

    #Initiate
    data =  yaml.load('''
    - strategy: free
      hosts: foo
    - import_playbook: test_include.yml
      vars:
        var1: "foo"
      tags:
        - bar
      when: ansible_os_family == "Debian"
    ''')

    basedir = './tests/unit/playbook_include/'

    # Test
    p = PlaybookInclude()
    p.load_data(data, basedir)

    # Verify
    assert p._entries[1].vars['bar'] == 'baz'
    assert p._

# Generated at 2022-06-13 08:49:18.255124
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    def mock_pb_entry_load_data(self, ds, variable_manager, loader):
        self._ds = ds
        self.vars = dict(a=1)
        self.tags = []

    def mock_pb_load_data(self, file_name, variable_manager, vars=None):
        self._file_name = file_name
        self._variable_manager = variable_manager
        self._vars = vars
        self._entries = [PlaybookIncludeEntry()]

    def mock_pb_load_data_with_tasks(self, file_name, variable_manager, vars=None):
        self._file_name = file_name
        self._variable_manager = variable_manager
        self._vars = vars

# Generated at 2022-06-13 08:49:32.880887
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.yaml.objects import AnsibleMapping
    import ansible.playbook.playbook_include
    import ansible.playbook.play
    from ansible.vars.manager import VariableManager
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.utils.collection_loader._collection_finder import AnsibleCollectionFinder
    from ansible.playbook.play_context import PlayContext

    # create a variable manager and use it to load the playbook
    variable_manager = VariableManager()
    variable_manager._extra_vars = {'inventory_dir': 'tests/unit/inventory', 'inventory_file': 'tests/unit/inventory/test1', 'playbook_dir': 'tests/unit/playbooks'}

# Generated at 2022-06-13 08:49:33.720543
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass


# Generated at 2022-06-13 08:49:46.554449
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition

    # create playbook
    p = PlaybookInclude()
    playbook_name = 'test.yml'

    # create variable manager
    variable_manager = dict()

    # create task
    task = dict()
    task['name'] = 'Test task'
    task['action'] = {"module": "shell", "args": "echo ok" }
    task['tags'] = 'test'

    # create task list
    task_list = list()
    task_list.append(task)

    # create role definition
    role_definition = RoleDefinition()
    role_definition._entries = task_list

    # create list role definition
    role_definition_list = list()

# Generated at 2022-06-13 08:50:00.323069
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    pb = PlaybookInclude.load(data=dict(import_playbook='a.yml'), basedir='.', variable_manager=None, loader=None)
    assert isinstance(pb, Playbook)
    assert pb._entries[0]._file_name == 'a.yml'
    assert pb._entries[0].get_vars() == {}
    assert pb._entries[0].tags == []


# Generated at 2022-06-13 08:50:01.447598
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass



# Generated at 2022-06-13 08:50:07.810682
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    '''
        This is to unit test method load_data of class PlaybookInclude
    '''
    from ansible.playbook.play import Play

    test_obj = PlaybookInclude()
    test_ds = {}
    test_basedir = "/test_dir"
    test_pb = test_obj.load_data(test_ds, test_basedir)
    assert isinstance(test_pb, Play)
    assert test_obj._included_path == "/test_dir"

# Generated at 2022-06-13 08:50:17.616331
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import shutil
    import tempfile
    import unittest

    from ansible.errors import AnsibleError, AnsibleParserError
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    class TestPlaybookInclude(unittest.TestCase):
        def setUp(self):
            self._test_dir = tempfile.mkdtemp()
            self._loader = DataLoader()
            self._basedir = os.getcwd()
            os.chdir(self._test_dir)

            self._datadef = dict(
                import_playbook='main.yml',
                tags=['foo'],
                vars=dict(a=1))
            self._playbooks = dict

# Generated at 2022-06-13 08:50:29.938128
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.handler_include import HandlerInclude
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager

    create_loader = lambda x: DataLoader()

    import_playbook = 'test_pb'
    pb = PlaybookInclude.load({'import_playbook': import_playbook}, '.', loader=create_loader('.'))
    assert isinstance(pb, Play)
    assert len(pb._entries) == 1
    assert isinstance(pb._entries[0], Block)


# Generated at 2022-06-13 08:50:40.753524
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Play
    from ansible.vars.manager import VariableManager

    # Configuration for test
    task1 = dict(action=dict(module="debug", args=dict(msg='task 1')))
    task2 = dict(action=dict(module="debug", args=dict(msg='task 2')))
    pre_tasks = [task1]
    tasks = [task2]
    play = dict(
        name="test",
        hosts="all",
        pre_tasks = pre_tasks,
        tasks = tasks
    )
    include = dict(
      import_playbook = "test.yml",
      vars = dict(
        foo = "bar"
      )
    )
    ds = [include, play]


# Generated at 2022-06-13 08:50:43.868528
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # purpose: test loading data is ok
    # precondition: instance of AnsibleCollectionConfig exist
    # postcondition: return is json
    # Test if data is json
    # Test if data is not None
    # Test if data is not empty dictionary
    # Test if data is not empty list
    # Test if data is not empty string, int, zero, bool
    assert True is True

# Generated at 2022-06-13 08:50:47.758666
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    import_obj = PlaybookInclude().load_data(ds="import_playbook: file.yaml", basedir="")
    assert Play in import_obj._entries[0].__class__.__mro__


# Generated at 2022-06-13 08:50:54.762686
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.attribute import FieldAttribute
    from ansible.playbook.role.definition import compile_role_definition
    from ansible.parsing.yaml.objects import AnsibleMapping, AnsibleSequence
    from ansible.utils.collection_loader._collection_finder import _get_collection_playbook_path, _get_collection_role_path
    from ansible.utils.display import Display
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    display = Display()

    # use parent method to load new_obj
    new_obj = Base().load_data(AnsibleMapping({'import_playbook': 'test_playbook.yml'}))
    # rely on _load_playbook_data to set "entries"

# Generated at 2022-06-13 08:51:05.695964
# Unit test for method load_data of class PlaybookInclude

# Generated at 2022-06-13 08:51:30.019913
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    PlaybookInclude_load_data_expected_result = {
        u'import_playbook': u'./../../examples/backup.yml',
        u'tags': [u'always'],
        u'vars': {u'var1': u'value1'}
    }

    data = {
        u'import_playbook': u'./../../examples/backup.yml',
        u'tags': [u'always'],
        u'vars': {u'var1': u'value1'}
    }

    basedir = u'/tmp/test'
    variable_manager = None
    loader = None

    play_book_include = PlaybookInclude()
    result = play_book_include.load_data(data, basedir, variable_manager, loader)

    assert result

# Generated at 2022-06-13 08:51:31.100988
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:51:40.913624
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.play import Play

    loader = AnsibleLoader(None, 'myfile')
    ds = loader.load_from_data({'include': 'myimport.yml'})
    data = ds[0]

    assert isinstance(data, dict), 'Expected dictionary'
    assert data['include'] == 'myimport.yml', 'Expected include: myimport.yml'

    basedir = '/tmp'
    pb = PlaybookInclude.load(data, basedir=basedir)

    assert isinstance(pb, PlaybookInclude), 'Expected PlaybookInclude instance'
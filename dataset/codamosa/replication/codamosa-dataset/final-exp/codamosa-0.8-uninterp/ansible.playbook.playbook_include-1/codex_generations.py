

# Generated at 2022-06-13 08:41:53.695190
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    # Create a fake PlaybookInclude object
    # with initial values for its attributes
    pb_include = PlaybookInclude()
    pb_include.import_playbook = 'test_playbook.yml'
    pb_include.vars = {}

    # Create a fake templar object
    # that returns the raw value of the
    # import_playbook
    templar = Templar(loader=None, variables={})
    def template(data):
        return data
    templar.template = template

    # Create a fake Playbook object
    #

# Generated at 2022-06-13 08:42:01.730134
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    playbook_include_instance = PlaybookInclude()
    playbook_include_instance.import_playbook = "testdata/play.yml"
    playbook_include_instance.vars = {'var1': 'val1'}
    playbook_include_instance.tags = ['tag1']
    playbook_include_instance.when = ['var1=val1']

    result = playbook_include_instance.load_data(ds={'import_playbook': 'testdata/play.yml'}, basedir='.', variable_manager=None, loader=None)
    assert result != None

# Generated at 2022-06-13 08:42:12.593485
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook.play import Play

    # Test of import_playbook on a single variable with basic path
    ds = dict(
        import_playbook = dict(
            path = 'path/to/playbook.yml',
        )
    )
    pb = PlaybookInclude.load(ds, 'test_PlaybookInclude_load_data', variable_manager=None, loader=None)
    assert len(pb._entries) == 1
    assert type(pb._entries[0]) == Play
    assert pb._entries[0].name == 'path/to/playbook.yml'
    assert len(pb._entries[0].tasks) == 1

# Generated at 2022-06-13 08:42:22.987032
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    loader = DataLoader()
    variable_manager = VariableManager()

    # 'import_playbook' test
    test_playbook_include = PlaybookInclude.load({}, None)
    assert test_playbook_include.preprocess_data({'import_playbook': 'test.yml'}) == {'import_playbook': 'test.yml'}, "A single string parameter should set 'import_playbook' to the value"
    test_playbook_include = PlaybookInclude.load({}, None)

# Generated at 2022-06-13 08:42:30.444716
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    class DummyPlaybookInclude(PlaybookInclude):
        def preprocess_data(self, ds):
            self.preprocessed_data = super(DummyPlaybookInclude, self).preprocess_data(ds)
            return self.preprocessed_data

    class DummyDs(object):
        pass

    test_ds = DummyDs()

    # test with correct set
    correct_ds = dict(
        import_playbook='test.yml',
        tags='tag1,tag2'
    )

    test_ds.__dict__ = dict(correct_ds)
    test_obj = DummyPlaybookInclude()
    new_ds = test_obj.preprocess_data(test_ds)
    assert new_ds == correct_ds, 'preprocess_data does not preserve tags'
    expected

# Generated at 2022-06-13 08:42:45.154821
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    play_vars = dict(var1='val1')
    play_tags = ['tag1', 'tag2']

    orig_play = Play.load(dict(hosts='hosts', roles='role1', vars=play_vars, tags=play_tags),None, None)
    orig_play._included_path = None

    pb = PlaybookInclude.load(dict(import_playbook='pb.yml', vars=dict(var2='val2')), None, None)

    assert isinstance(pb, Playbook)
    assert len(pb._entries) == 1
    assert isinstance(pb._entries[0], Play)

# Generated at 2022-06-13 08:42:45.690468
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:42:53.885647
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    """ This methods creates an object of class PlaybookInclude and
    checks the correctness of load_data method.

    import_playbook : test_data/import_file.yml
    vars :
        var1 : "value1"

    import_playbook : test_data/import_file.yml var1="value1"
    """

    # Creating object of class PlaybookInclude
    playbook_include = PlaybookInclude()

    # Making data set
    ds1 = AnsibleMapping()
    ds1['import_playbook'] = "test_data/import_file.yml"
    ds1['vars'] = {'var1' : "value1"}

    with open(os.devnull, 'w') as fnull:
        # Running load_data for the above tests
        playbook1 = playbook

# Generated at 2022-06-13 08:43:00.495219
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    ds = {'include': 'foo.yml', 'vars': {'foo': 'bar'}}
    new_ds = {'import_playbook': 'foo.yml', 'vars': {'foo': 'bar'}}
    assert new_ds == PlaybookInclude.load(ds=ds, basedir='').data

# Generated at 2022-06-13 08:43:10.428175
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler

    play = Play.load(dict(name='the play', hosts='all', roles=['foo'], tasks={'name': 'test'}),
                     variable_manager=None, loader=None)

    assert isinstance(play, Play)

    task = Task.load(dict(name='the task', include_role=dict(name='role1')),
                     variable_manager=None, loader=None)
    assert isinstance(task, Task)

    block = Block.load(dict(name='the block', tasks=[task]),
                       variable_manager=None, loader=None)
    assert isinstance(block, Block)

    handler = Handler

# Generated at 2022-06-13 08:43:30.201293
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import sys
    import os
    
    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.block
    import ansible.playbook.handler
    import ansible.playbook.included_file
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.parsing.yaml.objects import AnsibleMapping

    ### preparation
    
    playbook_include = ansible.playbook.PlaybookInclude()

    # prepare ds
    ds = AnsibleMapping()
    ds.data = { 'import_playbook': './my_playbook.yml' }
    variable_manager = None
    loader = None

# Generated at 2022-06-13 08:43:30.660089
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:43:36.336429
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.template import Templar
    import os
    import json

    # create mock objects
    my_loader = AnsibleLoader(None, None, True)
    my_variable_manager = VariableManager()
    my_inventory = InventoryManager(loader=my_loader, sources=['/etc/ansible/hosts'])
    my_playbook = Playbook()
    my_play = Play()

    # initialize objects
    my_playbook._loader = my_loader
    my_playbook._variable_manager = my_variable_manager
   

# Generated at 2022-06-13 08:43:38.156342
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    print("TODO")


# Generated at 2022-06-13 08:43:53.011890
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    import pytest
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    display = Display()
    loader, inventory, variable_manager = CBaseLoader(), CInventory(), CVariableManager()
    variable_manager.extra_vars = {'foo': 'foo_value', 'bar': 'bar_value'}

    # create mock object for ds
    ds = {}
    ds['import_playbook'] = 'myplaybook.yaml'
    ds['vars'] = {'var1': 'value1', 'var2': 'value2'}
    new_ds = AnsibleMapping()
    new_ds['import_playbook'] = 'myplaybook.yaml'

# Generated at 2022-06-13 08:43:56.501508
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # test_PlaybookInclude_load_data is not made because of the following reasons
    # It uses Play which is defined in the same file.
    # It's hard to create a yaml object for use in load_data.
    #
    pass


# Generated at 2022-06-13 08:44:05.951464
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    class _loader():
        def path_dwim(self, x):
            return x
    class _variable_manager():
        def _init__(self):
            self.extra_vars = {'test_var': 1}
        def get_vars(self):
            return self.extra_vars

    pbi = PlaybookInclude()
    ds = {
        'import_playbook': 'some.yml',
        'some_other_key': 'some_other_value'
    }
    pb = pbi.load_data(ds, '.', variable_manager=_variable_manager(), loader=_loader())

# Generated at 2022-06-13 08:44:12.935865
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.playbook.play
    ansible_playbook_play = ansible.playbook.play
    reload(ansible_playbook_play)
    from ansible.playbook.play import Play
    import ansible.playbook.role
    ansible_playbook_role = ansible.playbook.role
    reload(ansible_playbook_role)
    from ansible.playbook.role import Role
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.template import Templar

    templar = Templar(loader=None)

    # Only for testing purpose, for preprocess_data function
    ds = dict(import_playbook='localhost.yml')
    new_ds = AnsibleMapping()

# Generated at 2022-06-13 08:44:24.184088
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Testing method load_data of class PlaybookInclude
    testclass = PlaybookInclude()
    # sub_dict: 
    #    import_playbook: foo.yml
    #    vars:
    #        foo: bar
    #        foo2: bar2
    #    tags:
    #        - foo
    #        - bar
    #        - baz
    #    when:
    #        - not_cond
    from ansible_collections.ansible.community.plugins.module_utils.common.collections import ImmutableDict  # noqa
    # sub_dict = ImmutableDict({'import_playbook': 'foo.yml',
    #                           'vars': {'foo': 'bar',
    #                                    'foo2': 'bar2'}, 
    #                          

# Generated at 2022-06-13 08:44:25.312869
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:44:49.792624
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    import ansible.playbook.play as play
    import ansible.playbook.task as task
    import ansible.playbook.role.role as role
    data = '''
        - import_playbook: test_playbook
          vars:
             param1: value1
          tags: test_tags
    '''
    playbook = PlaybookInclude.load(data, '.')
    assert isinstance(playbook, Playbook)
    assert len(playbook._entries) == 1
    assert isinstance(playbook._entries[0], play.Play)
    assert playbook._entries[0].vars == {'param1': 'value1'}
    assert playbook._entries[0].tags == ['test_tags']
    assert playbook._entries[0]._

# Generated at 2022-06-13 08:45:00.397887
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # default behavior
    assert PlaybookInclude.load_data({'import_playbook': 'some_playbook.yml'}, 'path/to/playbook')

    # extra options before or after playbook.yml should work
    assert PlaybookInclude.load_data({'import_playbook': 'some_playbook.yml param=ok'}, 'path/to/playbook')
    assert PlaybookInclude.load_data({'import_playbook': 'param=ok some_playbook.yml'}, 'path/to/playbook')

    # constrants on type of 'import_playbook' (string)
    assert_raises(AnsibleParserError, PlaybookInclude.load_data, {'import_playbook': 1}, 'path/to/playbook')

    # 'vars' as dict is allowed

# Generated at 2022-06-13 08:45:04.231704
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    #1. Data is dict and variable_manager is None
    #2. Data is dict and variable_manager is not None
    #3. Data is not dict
    # Expected result:
    # 1.,2.,3. AnsibleAssertionError: 'ds (ds) should be a dict but was a str'
    pass


# Generated at 2022-06-13 08:45:10.521649
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    import_playbook = {'import_playbook': 'playbook.yaml'}
    assert PlaybookInclude.preprocess_data(import_playbook) == import_playbook

    invalid_import = {'import_playbook': 123, 'another_param': 'another param'}
    try:
        PlaybookInclude.preprocess_data(invalid_import)
        assert False
    except AnsibleParserError:
        pass

    import_playbook_with_param = {'import_playbook': '/path/to/a/playbook.yaml other_param=val'}
    assert PlaybookInclude.preprocess_data(import_playbook_with_param) == {'import_playbook': '/path/to/a/playbook.yaml', 'vars': {'other_param': 'val'}}

# Generated at 2022-06-13 08:45:12.218655
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    """Test the load_data method of PlaybookInclude"""
    # This method is an alias to Playbook.load and has no implementation of its own
    # Playbook has its own test, so this one is empty
    pass

# Generated at 2022-06-13 08:45:22.026712
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    display.verbosity = 3
    data = {
        'import_playbook': 'test_play.yml',
        'vars': {
            'user': 'foo'
        },
        'tags': 'tag1,tag2',
        'when': 'ansible_os_family == "RedHat"',
        'ignore_errors': True
    }
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

    vm = VariableManager()

    # my_loader = DataLoader()
    # vm.set_vars(combine_vars(loader=my_loader, variables=data))

    pbinclude = PlaybookInclude()
    # pb = pbinclude.load_data(data

# Generated at 2022-06-13 08:45:35.282084
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import unittest

    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role

    class TestPlaybookInclude(unittest.TestCase):
        def setUp(self):
            # create a fake playbook
            self.fake_playbook = []
            self.fake_playbook_path = "/tmp/fake_playbook.yml"
            self.fake_playbook_collection_name = "mytestcollection"

            # create task1
            self.task1 = Task()

# Generated at 2022-06-13 08:45:47.390798
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.playbook import Playbook

    loader = DataLoader()

    # test variables
    vars_dict = {'vars_key1': 'vars_value1',
                 'vars_key2': 'vars_value2'}

    from_yaml = u"import_playbook: playbook_to_import.yml\n"
    from_yaml += u"vars:\n"
    from_yaml += u"  vars_key1: vars_value1\n"
    from_yaml += u"  vars_key2: vars_value2\n"

    # create PlaybookInclude object and load the yaml


# Generated at 2022-06-13 08:45:54.854827
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.parsing.dataloader import DataLoader
    import ansible.callbacks
    import os

    p = PlaybookInclude()
    l = DataLoader()
    variables = dict()
    cb = ansible.callbacks.AggregateStats()
    path = os.path.join(os.path.dirname(__file__), '../plays/library_include_playbook.yml')
    p = p.load_data(ds = l.load_from_file(path), basedir='.', variable_manager=None)
    assert isinstance(p, Playbook)
    assert p.hosts == ['localhost']

# Generated at 2022-06-13 08:46:09.292104
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Play
    playbook_include = PlaybookInclude()
    mock_play = Play()
    mock_play.vars = {"testA": "testB"}
    playbook_result = playbook_include.load_data(
        ds="test", basedir=0,
        variable_manager=0, loader=0)
    assert not playbook_result._entries
    playbook_include._entries = [mock_play]
    assert playbook_include.load_data(
        ds="test", basedir=0,
        variable_manager=0, loader=0)
    mock_play.vars = {"vars": {"testA": "testB"}}

# Generated at 2022-06-13 08:46:35.594012
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # A mock ds to be in the format of what is returned by Base.load_data
    # after being processed by preprocess_data
    ds = {}
    ds["import_playbook"] = "playbook.yml"
    ds["tags"] = ["tag1", "tag2", "tag3"]
    ds["vars"] = {"foo": "bar"}

    x = PlaybookInclude()
    d = x.load_data(ds, 'basedir', 'variable_manager', 'loader')

    assert isinstance(d, Playbook)
    for pb_entry in d._entries:
        # Check the data loaded into the new Playbook object
        assert pb_entry._included_path == 'basedir'
        assert pb_entry.vars["foo"] == "bar"
        assert p

# Generated at 2022-06-13 08:46:45.979730
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.attribute import FieldAttribute
    from ansible.playbook.play import Play

    import_relative_pb = 'import playbooks/import_pb.yml'
    import_absolute_pb = '/path/to/playbooks/import_pb.yml'
    import_relative_pb_params = 'import playbooks/import_pb.yml tags=aaa'
    import_absolute_pb_params = '/path/to/playbooks/import_pb.yml tags=aaa'
    import_relative_pb_params_vars = 'import playbooks/import_pb.yml tags=aaa vars=bbb'
    import_absolute_pb_params_vars = '/path/to/playbooks/import_pb.yml tags=aaa vars=bbb'
    import_relative_pb_vars

# Generated at 2022-06-13 08:46:46.748890
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:46:47.528984
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:47:00.361807
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Unit test playbookinclude.PlaybookInclude.load_data
    # 1- Create a variable_manager that returns some variable_data
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # Create a temporary file to be a playbook
    import tempfile
    f = tempfile.NamedTemporaryFile(delete=False, mode='wt')
    f.write(""" ---
    - hosts: all
      tasks:
        - name: bogus task
          meta: end_play
    """)
    f.close()

    # Load the file with the playbook in it
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')

# Generated at 2022-06-13 08:47:12.437404
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook

    def verify_playbook_include_obj(obj):
        assert obj.import_playbook == 'common.yml'
        assert isinstance(obj, PlaybookInclude)

    # test simple usage with no parameters
    verify_playbook_include_obj(PlaybookInclude.load({'import_playbook': 'common.yml'}, basedir='/tmp'))

    # test with the deprecated syntax of name=value parameters
    # (this is deprecated, but we should continue to support it)
    p = PlaybookInclude.load({'import_playbook': 'common.yml tags=dev vars="path=/opt"'},
                             basedir='/tmp')
    verify_playbook_include_obj(p)

# Generated at 2022-06-13 08:47:24.288732
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    playbook_include = PlaybookInclude()
    ds = AnsibleMapping({'import_playbook': {
        'playbook': 'playbook.yml',
        'vars': {'a': 1, 'b': 2}
    }})
    ds = playbook_include.preprocess_data(ds)
    assert ds['import_playbook'] == 'playbook.yml'
    assert ds['vars'] == {'a': 1, 'b': 2}

    ds = AnsibleMapping({'import_playbook': {
        'playbook': 'playbook.yml',
        'vars': 'testing vars'
    }})
    with pytest.raises(AnsibleParserError):
        ds = playbook_include.preprocess_data(ds)

    ds = Ans

# Generated at 2022-06-13 08:47:37.641328
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook, Play
    from ansible.template import Templar

    templar = Templar(loader=None, variables={})

    file_name = templar.template("include_file.yml")
    pb = PlaybookInclude.load(file_name, basedir='/etc').load_data(ds={}, basedir='/etc', variable_manager=None, loader=None)

    assert isinstance(pb, Playbook)

    assert pb._entries[0]._included_path == '/etc'
    #assert pb._entries[0]._included_file == 'include_file.yml'

    assert pb._entries[0] == pb._entries[0]._entries[0]
    assert pb._entries[0]._included_cond

# Generated at 2022-06-13 08:47:48.758891
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play

    # tests the PlaybookInclude object,
    # which is only used to wrap includes
    # before translating into a Playbook

    # one role and one play
    data = """
- hosts: all
  vars:
    role_var: role_var_value
  tasks:
    - debug: msg="{{ role_var }} {{ play_var }} {{ v }}"
"""

    # one play and one role
    data2 = """
- hosts: all
  vars:
    play_var: play_var_value
  roles:
    - include_role:
        name: include_role
  tasks:
    - debug: msg="{{ role_var }} {{ play_var }} {{ v }}"
"""

    # one play and one role with variable

# Generated at 2022-06-13 08:48:02.069819
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    '''
    PlaybookInclude.preprocess_data(ds)

    PlaybookInclude uses preprocess_data() to translate the input
    datastructure into a standard format before normal loading can
    take place.
    '''
    # import statements can be specified as a string:
    #   - import_playbook: foo.yml
    # as key=value pairs:
    #   - import_playbook: foo.yml tags=bar
    #   - import_playbook: foo.yml tags=bar,baz
    #   - import_playbook: foo.yml tags=bar extra_var=baz
    # or as a dictionary:
    #   - import_playbook:
    #       playbook: foo.yml
    #       tags: bar
    #   - import_playbook:
    #      

# Generated at 2022-06-13 08:48:56.062211
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    import builtins
    try:
        builtins.__dict__['_'] = lambda x: x
    except:
        import __builtin__
        __builtin__.__dict__['_'] = lambda x: x

    pbi = PlaybookInclude()
    pbi_ds = {
        'import_playbook': './roles/webservers/tasks/main.yml',
        'vars': {'key': 'value'}
    }
    pbi = pbi.load_data(ds=pbi_ds, basedir=os.getcwd())
    assert pbi.static is True
    assert isinstance(pbi, Playbook)
    assert len(pbi._entries) == 1

# Generated at 2022-06-13 08:49:06.961927
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.parsing.yaml.loader import AnsibleLoader

    file = 'tests/test_include.txt'
    data_str = '''
    - include: myinclude.yml
        vars:
            str_var: hello world
            int_var: 42
            bool_var: True
            dict_var:
                foo: bar
                baz: quux
                foo_file: "{{ my_var }}"
            list_var:
                - 1
                - 2
            int_list_var:
                - 3
                - 4
    '''


# Generated at 2022-06-13 08:49:07.468935
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:49:15.538193
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.parsing.dataloader
    import ansible.vars
    import ansible.template
    import ansible.inventory
    import ansible.playbook.play
    import ansible.playbook.task

    dataloader = ansible.parsing.dataloader.DataLoader()
    templar = ansible.template.Templar(loader=dataloader)

    inventory = ansible.inventory.Inventory(loader=dataloader, variable_manager=ansible.vars.VariableManager())
    variable_manager = ansible.vars.VariableManager(loader=dataloader, inventory=inventory)

    ds = dict(
        import_playbook="playbook_inc.yml",
        connect_timeout=10
    )
    pi = PlaybookInclude.load

# Generated at 2022-06-13 08:49:31.028442
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.config.manager import ConfigManager
    from ansible.playbook.play import Play

    # Load an import_tasks.yml file containing a playbook with two plays
    loader = ConfigManager()
    var_manager = ConfigManager()
    pbi = PlaybookInclude()
    playbook = pbi.load_data(
        ds=dict(
            import_playbook=loader.get_basedir() + '/test/units/fixtures/import_playbook.yml',
            tags=['test01'],
            vars=dict(
                one=1,
                two="two"
            )),
        basedir=loader.get_basedir(),
        variable_manager=var_manager,
        loader=loader
    )

    # Check the first play contains the expected values
    first_play = playbook._ent

# Generated at 2022-06-13 08:49:37.620513
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.yaml.loader import AnsibleLoader

    context = PlayContext()
    variable_manager = VariableManager()
    variable_manager.set_inventory('localhost')
    loader = AnsibleLoader(None, variable_manager=variable_manager, context=context)
    ds = {}
    ds['import_playbook'] = AnsibleLoader(None, variable_manager=variable_manager, context=context).load_from_file('test2.yml')
    ds['vars'] = {}
    ds['vars']['var1'] = 'Variable1'
    ds['tags'] = ['debug']

# Generated at 2022-06-13 08:49:42.880164
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    # Test PlaybookInclude.load_data with a conditional playlist
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.vars.reserved import Reserved
    test_list = [
        {
            'import_playbook': 'my_playbook.yml',
            'when': 'resource.status=="Error"',
            'tags':['bar','baz']
        }
    ]
    variable_manager = Reserved()
    variable_manager.data = {}
    variable_manager.update({'resource': 2})
    variable_manager.update({'resource.status': 'Error'})
    variable_manager.update({'resource.tags': 'foo'})

# Generated at 2022-06-13 08:49:54.562959
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    playbook_content = """
- hosts: localhost
  vars:
    message: "Hello World!"
  tasks:
    - command: echo "{{ message }}"
    - name: create a directory
      file:
        path: "{{ dir_path }}"
        state: directory
"""
    tmp_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
    os.makedirs(os.path.join(tmp_dir, 'playbooks', '_test', 'test_playbook.yml'))

# Generated at 2022-06-13 08:49:56.904404
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    assert False, "There's no unit test for this method yet, please do it"


# Generated at 2022-06-13 08:50:01.129772
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    fake_playbook = "/etc/ansible/playbook.yml"
    pm = PlaybookInclude.load({"import_playbook": fake_playbook}, "/etc/ansible")
    assert pm.import_playbook == fake_playbook

# Generated at 2022-06-13 08:50:42.062374
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:50:53.414183
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # initialize an instance of class PlaybookInclude
    playbookInclude = PlaybookInclude()
    # initialize an instance of class Playbook
    from ansible.playbook import Playbook
    playbook = Playbook()
    # initialize a dict
    ds = dict()
    # initialize a string
    basedir = str()
    # initialize an instance of class VariableManager
    from ansible.vars import VariableManager
    variable_manager = VariableManager()
    # initialize an instance of class DataLoader
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    # call method load_data of class PlaybookInclude
    result = playbookInclude.load_data(ds, basedir,
                          variable_manager=variable_manager, loader=loader)
    assert isinstance(result, Playbook) == True

# Generated at 2022-06-13 08:50:55.529821
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # TODO: Write a test for this class
    pass

# Generated at 2022-06-13 08:51:03.099921
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    import os

    # Create a PlaybookInclude instance
    playbookInclude = PlaybookInclude()

    file_name = os.path.expanduser('~/test_dir/test.yml')

    # Call the method load_data with the correct args
    pb = playbookInclude.load_data(file_name, '.', None, None)

    # Assert that returned object is of class Playbook
    assert isinstance(pb , Playbook)


# Generated at 2022-06-13 08:51:06.924033
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    playbook = PlaybookInclude()
    playbook.load_data({'import_playbook': '../other.yml'})
    assert playbook._import_playbook == '../other.yml'


# Generated at 2022-06-13 08:51:18.850958
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import mock

    def when_no_data():
        return None

    def when_data():
        return {}

    def when_with_data(ds=None):
        if not ds:
            ds = {}
        ds['import_playbook'] = 'playbook'
        return ds

    ds = {}
    basedir = 'basedir'
    variable_manager = 'variable_manger'
    loader = 'loader'

    pbi = PlaybookInclude()

    assert isinstance(pbi.load_data(ds, basedir, variable_manager, loader), AnsibleParserError)

    pbi.when = []
    ds = when_with_data()


# Generated at 2022-06-13 08:51:29.226706
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    import_playbook = 'your_playbook.yml'
    variable_manager = None
    loader = None

    ds = {
        'import_playbook': import_playbook,
    }

    ds_var = {
        'import_playbook': import_playbook,
        'vars': {
            'foo': 'bar'
        }
    }

    play = PlaybookInclude.load_data(ds, None, variable_manager, loader)

    assert(play.vars == {})

    play_var = PlaybookInclude.load_data(ds_var, None, variable_manager, loader)

    assert(play_var.vars == {'foo': 'bar'})

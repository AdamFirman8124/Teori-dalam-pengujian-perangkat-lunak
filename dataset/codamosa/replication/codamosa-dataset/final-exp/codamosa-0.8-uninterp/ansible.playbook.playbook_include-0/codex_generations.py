

# Generated at 2022-06-13 08:41:48.133035
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pb = PlaybookInclude.load({'import_playbook': '/path/to/playbook.yml', 'tags': 'tag1,tag2'}, '/path')
    assert pb._entries[0].tags == ['tag1', 'tag2']
    assert pb._entries[0]._included_path == '/path'

# Generated at 2022-06-13 08:41:57.054411
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    class TestPlaybookInclude(PlaybookInclude):
        def __init__(self):
            self.vars = dict()
            self.when = list()

    test_include = TestPlaybookInclude()
    test_include.load_data({'import_playbook': './test1.yml'}, '/')
    assert test_include.import_playbook == './test1.yml'

    test_include = TestPlaybookInclude()
    test_include.load_data({'import_playbook': './test1.yml', 'vars': {'test_var': 'hello'}}, '/')
    assert test_include.vars == {'test_var': 'hello'}

    test_include = TestPlaybookInclude()

# Generated at 2022-06-13 08:42:09.590188
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    import sys
    import pytest

    from ansible.plugins.loader import action_loader, module_loader
    from ansible.playbook.play import Play

    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    from ansible_collections.ansible.netcommon.playbooks.test import (
        test_PlaybookInclude_load_data as test_test_PlaybookInclude_load_data
    )

    # FIXME: This is WIP

    # TODO: Create fixture for the ansible environment and a fixture for the ansible-galaxy directory.
    #   Find

# Generated at 2022-06-13 08:42:10.070384
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:42:20.198263
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # assert playbook_include.py correctly defines PlaybookInclude class
    assert PlaybookInclude

    # assert PlaybookInclude defines load_data classmethod
    assert hasattr(PlaybookInclude, 'load_data') and callable(getattr(PlaybookInclude, 'load_data'))

    # assert PlaybookInclude defines _preprocess_import method
    assert hasattr(PlaybookInclude, '_preprocess_import') and callable(getattr(PlaybookInclude, '_preprocess_import'))

    # assert PlaybookInclude defines preprocess_data method
    assert hasattr(PlaybookInclude, 'preprocess_data') and callable(getattr(PlaybookInclude, 'preprocess_data'))

# Generated at 2022-06-13 08:42:28.603850
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.task import Task
    import ansible.constants as C
    import ansible.inventory
    import ansible.playbook.play
    import ansible.vars.manager

    def _search_loader(path):
        return None

    # Create inventory, variable_manager and loader
    inventory = ansible.inventory.Inventory("tests/unit/ansible/test_inventory")
    variable_manager = ansible.vars.manager.VariableManager(inventory)
    loader = ansible.parsing.dataloader.DataLoader()
    loader.set_basedir("tests/unit/ansible/test_playbook_include")
    loader._search_path = _search_loader
    loader.set_vault_password("test")


# Generated at 2022-06-13 08:42:35.396494
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    fp = os.path.join(os.path.dirname(__file__), '..', 'testdata', 'import_playbook_data')

    pi = PlaybookInclude.load(load_yaml(fp, 'included_playbook_data.yml'),
                              basedir=fp,
                              loader=DummyLoader())

    assert isinstance(pi, Playbook)

    assert len(pi._entries) == 3  # 3 'plays'

    assert isinstance(pi._entries[0], Play)
    assert pi._entries[0].name == 'simple play'
    assert pi._entries[0].vars == {'extra': 'param'}


# Generated at 2022-06-13 08:42:41.040771
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    try:
        PlaybookInclude.load(data='foobar', basedir='/tmp')
        raise Exception("Should have failed")
    except AnsibleParserError:
        pass  # expected


# unit test case for preprocess_data method of AnsibleBaseYAMLObject class

# Generated at 2022-06-13 08:42:45.301218
# Unit test for method preprocess_data of class PlaybookInclude

# Generated at 2022-06-13 08:42:53.445560
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    class FakeModuleUtilPath:

        @staticmethod
        def _get_collection_playbook_path(file_name):
            return "file_name"

    class FakePlaybook:

        @staticmethod
        def _load_playbook_data(**kwargs):
            return "load_playbook_data"

    class FakePlay:

        def __init__(self):
            self._included_conditional = None
            self._included_path = None
            self.pre_tasks = []
            self.roles = []
            self.tasks = []
            self.post_tasks = []
            self.tags = []
            self.vars = {}

    class FakeBase:
        def __init__(self):
            self.when = []


# Generated at 2022-06-13 08:43:08.317030
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # Define the datastructure to be used as input to preprocess_data() method
    ds = AnsibleMapping()
    ds['import_playbook']='/path/to/my/playbook.yml'
    ds['vars']={'key1': 'value1', 'key2': 'value2'}

    # Call the method
    new_ds = PlaybookInclude.preprocess_data(ds)

    # Test that the returned datastructure is correct
    assert isinstance(new_ds, AnsibleMapping)

# Generated at 2022-06-13 08:43:17.952208
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # create a PlaybookInclude object
    pi = PlaybookInclude()

    # create data
    data = dict()

    data_key = "example.yml"
    data_value = dict()
    data_value['parameter-1'] = 1
    data_value['parameter-2'] = 2

    data['import_playbook'] = data_key
    data['vars'] = data_value

    # set some local variables for load_data
    basedir = "path/to/ansible/playbook"
    variable_manager = "variable_manager"
    loader = "loader"

    # run load_data
    result = pi.load_data(data, basedir, variable_manager, loader)

    # check result
    assert isinstance(result, dict)
    assert len(result) == 1

# Generated at 2022-06-13 08:43:30.201402
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    # Testing for different format of calling import_playbook
    ds = {'import_playbook': 'test/test.yml', 'vars': {'var_a': 'abc'}, 'tags': 'tag1,tag2'}
    pib = PlaybookInclude()
    new_ds = pib.preprocess_data(ds)
    assert new_ds['import_playbook'] == 'test/test.yml'
    assert new_ds['vars'] == {'var_a': 'abc'}
    assert new_ds['tags'] == ['tag1', 'tag2']

    ds = {'import_playbook': 'test/test.yml', 'vars': {'var_a': 'abc'}, 'tags': 'tag1,tag2', 'connection': 'local'}

# Generated at 2022-06-13 08:43:38.764250
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    p = PlaybookInclude()

    # Test invalid datastructure format
    try:
        p.preprocess_data('test')
    except Exception as e:
        assert isinstance(e, AnsibleAssertionError)

    # Test mix dict and vars
    ds = dict(
        import_playbook="test",
        vars=dict(
            overlay=dict(a="a")
        )
    )
    try:
        p.preprocess_data(ds)
    except Exception as e:
        assert isinstance(e, AnsibleParserError)

    # Test tags
    ds = dict(
        import_playbook="test tags=tag1,tag2",
        vars=dict(
            overlay=dict(a="a")
        )
    )

# Generated at 2022-06-13 08:43:49.301860
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    import_playbook = 'test_import_playbook.yml'
    vars = {'key': 'value'}
    data = AnsibleMapping(dict(import_playbook=import_playbook, vars=vars))
    playbook = PlaybookInclude().load_data(data, basedir='/')
    assert playbook.__class__ == Playbook
    assert playbook._entries
    play = playbook._entries[0]
    assert play.__class__ == Play
    assert play._entries[0].action == 'include'
    assert play._included_path

# Generated at 2022-06-13 08:43:58.114047
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    """
    Test method load_data of class PlaybookInclude
    """

    import ansible.playbook
    import ansible.playbook.play

    # First test: input ds is a dict
    ds = dict()
    ds["import_playbook"] = "../user_creation_playbook.yml"
    ds["vars"] = dict()
    ds["vars"]["user"] = "john"
    ds["vars"]["uid"] = "1023"
    ds["tags"] = "user_setup"
    loader = None
    variable_manager = None
    basedir = "/home/user/gits/ansible/lib/ansible/playbook"

    # Expected result
    # user_creation_playbook.yml is located in "../user_creation_play

# Generated at 2022-06-13 08:44:13.671570
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import datetime
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.parsing.splitter import parse_kv
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy

    ds_str_1='''
    ds:
      import_playbook: playbook.yml
      when: '1 == 1'
    '''


# Generated at 2022-06-13 08:44:14.270229
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:44:24.895756
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook

    # Set up the environment
    basedir = '/tmp/some_random_dir/'
    os.makedirs('/tmp/some_random_dir/', exist_ok=True)
    os.makedirs('/collection/my_collection/roles/my_role/', exist_ok=True)
    with open('/tmp/some_random_dir/test_playbook.yml', 'w') as f:
        f.write('---\ndummy:')
    with open('/collection/my_collection/roles/my_role/main.yml', 'w') as f:
        f.write('---\ntest2')

    # Create the loader instance and set the basedir so that the include statement

# Generated at 2022-06-13 08:44:36.994843
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.playbook_include import PlaybookInclude

    # First test: basic functionality
    playbook_include = PlaybookInclude()
    data = dict(
        import_playbook=dict(
            file="filename.yml"
        )
    )
    ansible_pos = dict(
        lineno=42,
        filename="example.yml"
    )
    data = AnsibleBaseYAMLObject(data)
    data.ansible_pos = ansible_pos
    result = playbook_include.preprocess_data(data)

    assert result["import_playbook"] == "filename.yml"
    assert result["vars"] == dict()
    assert result["tags"] == list()
    assert result["when"] == list()
    assert result[Conditional.ATTRIBUTE_NAME]

# Generated at 2022-06-13 08:44:49.813286
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.vault import VaultLib

    from ansible.playbook.base import Base
    from ansible.playbook.play import Play
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task import Task

    # prepare test directory
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    top_dir = os.path.dirname(cur_dir)
    test_dir = os.path.join(top_dir, 'test', 'testdata', 'vault')

    # create playbook include object and load data
    playbook_include = PlaybookInclude()
    data = {'import_playbook': 'test_playbook.yml', 'tags': 'test_playbook_include_load_data'}
    playbook

# Generated at 2022-06-13 08:45:00.396010
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    import os
    import sys
    import tempfile
    import textwrap
    import shutil

    def get_collection_playbook_path(path):
        return _get_collection_playbook_path(path)

    def get_collection_name_from_path(path):
        return _get_collection_name_from_path(path)

    def write_dir_content(dirname, filename, content):
        f = open(os.path.join(dirname, filename), 'w')
        f.write(textwrap.dedent(content))
        f.close()

    def assert_exception(exc):
        if sys.version_info[0] == 2:
            assert isinstance(exc, AssertionError)


# Generated at 2022-06-13 08:45:11.086358
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    obj = PlaybookInclude()
    basedir = '.'
    variable_manager = None
    loader = None


# Generated at 2022-06-13 08:45:21.062571
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    print("test_PlaybookInclude_load_data")
    import unittest
    import contextlib
    from ansible.parsing.yaml.objects import AnsibleSequence

    fake_data = AnsibleMapping()
    fake_data['import_playbook'] = AnsibleMapping(data='main.yml')

    fake_data_with_vars = AnsibleMapping()
    fake_data_with_vars['import_playbook'] = AnsibleMapping(data='main.yml')
    fake_data_with_vars['vars'] = AnsibleMapping(data='roles:')

    fake_data_with_tags = AnsibleMapping()
    fake_data_with_tags['import_playbook'] = AnsibleMapping(data='main.yml')
    fake_data_

# Generated at 2022-06-13 08:45:22.172159
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # TODO: write this test
    pass

# Generated at 2022-06-13 08:45:35.334948
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # Create PlaybookInclude object
    playbook_include = PlaybookInclude()

    # Create valid yaml files
    yaml1 = '''
    import_playbook: playbook1.yml
    '''
    yaml2 = '''
    import_playbook: playbook2.yml
    var1: "value"
    '''
    yaml3 = '''
    import_playbook: playbook3.yml
    vars:
      var1: "value"
    '''
    yaml4 = '''
    import_playbook: playbook4.yml vars={"var1": "value"}
    '''
    yaml5 = '''
    import_playbook: playbook5.yml var1="value"
    '''

# Generated at 2022-06-13 08:45:47.446740
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    import sys
    import os
    from ansible.parsing.yaml.loader import AnsibleLoader

    if sys.version_info[:2] == (2, 6):
        pyyaml = None
        try:
            import yaml
        except ImportError:
            pass
        else:
            from distutils.version import LooseVersion
            if LooseVersion(yaml.__version__) >= LooseVersion('5.1.1'):
                pyyaml = yaml
    else:
        pyyaml = None

    # import here to avoid a dependency loop
    from ansible.playbook import Playbook

    basedir = 'test/playbooks/'
    file_name = 'test_import.yml'

    pb = PlaybookInclude.load(data=file_name, basedir=basedir)

# Generated at 2022-06-13 08:45:52.073998
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars import VariableManager

    playbook_include = PlaybookInclude()

    basedir = 'test/test_include'
    ds = {'import_playbook': 'included_playbook.yml'}
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'foo': 'bar'}
    loader = DataLoader()
    loader.set_basedir(basedir)
    templar = Templar(loader=loader, variables=variable_manager.get_vars())


# Generated at 2022-06-13 08:46:06.586224
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play

    pb = PlaybookInclude().load_data({'import_playbook': 'included.yml'}, basedir='.', variable_manager={}, loader={})
    assert isinstance(pb, Playbook), 'pb is not a Playbook object: %s' % pb
    assert len(pb._entries) == 1 and isinstance(pb._entries[0], Play), 'pb._entries[0] is not a Play object: %s' % pb._entries[0]
    assert pb._entries[0]._included_path == '.', 'pb._entries[0]._included_path is not ".": %s' % pb._entries[0]._included_path
    assert pb._entries[0]._included_

# Generated at 2022-06-13 08:46:15.857998
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # TODO: this is a stub, implement correctly
    x = PlaybookInclude(
        import_playbook='./test/test.yml',
        vars={'var1': 'value1'},
        conditional='True'
    )

    # when ds is a dict
    ds = {
        'import_playbook': './test/test.yml',
        'vars': {
            'var1': 'value1',
        },
        'when': 'True'
    }

    pb = x.load_data(
        ds=ds,
        basedir='./test',
        variable_manager=None,
        loader=None
    )

    assert(pb is not None)

    # when ds is a AnsibleBaseYAMLObject
    ds_mapping = Ans

# Generated at 2022-06-13 08:46:34.909237
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import shutil
    import tempfile

    from ansible.errors import AnsibleParserError

    # Create test content in a temporary directory
    tmp_dir = tempfile.mkdtemp()
    tmp_file = os.path.join(tmp_dir, 'playbook.yml')

# Generated at 2022-06-13 08:46:45.688206
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    # Create a dummy PlaybookInclude object. It will be used to load other playbooks
    ds = dict(
        import_playbook='/dummy/path/dummy_playbook.yml'
    )

    playbook_include_obj = PlaybookInclude()
    playbook_include_obj = playbook_include_obj.load_data(ds, '/dummy/basedir')

    # Check the loaded object
    assert playbook_include_obj.import_playbook == '/dummy/path/dummy_playbook.yml'

    # Create a dummy Playbook object that will be used as the 'real' playbook

# Generated at 2022-06-13 08:46:46.584394
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass # FIXME

# Generated at 2022-06-13 08:46:59.867575
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play

    class test_ds(object):
        def __init__(self):
            self.ansible_pos = 'test_PlaybookInclude_load_data'

        def get_value(self):
            return dict(vars=dict(), import_playbook='./test_data/vars_file.yml', tags=['foo'])

    class test_ds2(object):
        def __init__(self):
            self.ansible_pos = 'test_PlaybookInclude_load_data'

        def get_value(self):
            return dict(vars=dict(), import_playbook='./test_data/vars_file.yml', tags=['foo'], when=['x', 'y', 'z'])


# Generated at 2022-06-13 08:47:01.784227
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # This function is implemented in test/units/playbook_include.py
    pass


# Generated at 2022-06-13 08:47:03.363242
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass



# Generated at 2022-06-13 08:47:14.135148
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    loader = DataLoader()
    variable_manager = VariableManager()
    ds = "{% playbook test.yaml %}"
    try:
        PlaybookInclude(loader, variable_manager, ds)
        assert False
    except AnsibleParserError:
        pass
    ds = "{% playbook test.yaml 'foo=1 bar=2' %}"
    try:
        PlaybookInclude(loader, variable_manager, ds)
        assert False
    except AnsibleParserError:
        pass
    ds = "{% playbook test.yaml foo=1 bar=2 %}"

# Generated at 2022-06-13 08:47:23.730968
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    def _playbook_include_load_data(ds, loader):
        return PlaybookInclude().load_data(ds=ds, basedir='/fake/basedir', variable_manager=variable_manager, loader=loader)

    loader = DataLoader()
    variable_manager = VariableManager()

    assert _playbook_include_load_data(ds={}, loader=loader) == None
    assert _playbook_include_load_data(ds={'import_playbook': 'foo'}, loader=loader) == None



# Generated at 2022-06-13 08:47:30.331001
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    import datetime
    import dateutil.parser
    import re

    play_name = 'Test Play'
    play_hosts = 'test_hosts'
    play_tasks = [{ 'name': 'test_task', 'action': 'test_action' }]
    play_vars = { 'test': 'test_vars' }
    play_roles = [{'test': 'test_role' }]
    play_handlers = [{ 'name': 'test_handler', 'action': 'test_action' }]
    play_meta = { 'test': 'test_meta' }
    play_vault_password = 'test_vault_password'

# Generated at 2022-06-13 08:47:45.114936
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # create test playbook object
    playbook_include = PlaybookInclude()

    # create test args
    ds = "testdata/ansible_module_utils/test_playbook_include.yml"
    basedir = "testdata/ansible_module_utils"

    # test creation of playbook

    pb = playbook_include.load(ds, basedir)

    # check number of plays
    assert(len(pb._entries) == 2)

    # check vars
    assert(pb._entries[0].vars['testvar'] == 'overridden')
    assert(pb._entries[0].vars['testvar2'] == 'defined-in-playbook')
    assert(pb._entries[1].vars['testvar'] == 'defined-in-play')

# Generated at 2022-06-13 08:47:55.515213
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    collection_paths = ['collections/test.demo', 'ansible_collections/test/demo/']
    for path in collection_paths:
        assert _get_collection_name_from_path(path) == 'test.demo'

# Generated at 2022-06-13 08:48:05.931948
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook.play import Play

    import_playbook_intance = PlaybookInclude()

    # test empty params
    new_obj = {}
    with pytest.raises(AnsibleParserError) as excinfo:
        import_playbook_intance.load_data(new_obj, None)
    assert 'playbook import parameter is missing' in str(excinfo.value)

    # test empty params
    new_obj = {'import_playbook': None}
    with pytest.raises(AnsibleParserError) as excinfo:
        import_playbook_intance.load_data(new_obj, None)
    assert 'playbook import parameter is missing' in str(excinfo.value)

    # test params is not a string

# Generated at 2022-06-13 08:48:17.271873
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars import VariableManager
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    from ansible.cli import CLI
    from ansible.module_utils.common.collections import ImmutableDict

    basedir = os.path.join(os.path.dirname(__file__), 'importer')
    playbook = os.path.join(basedir, 'playbook.yml')
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[os.path.join(basedir, 'hosts')])

# Generated at 2022-06-13 08:48:29.838307
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    p_include = PlaybookInclude()
    ds = {u'import_playbook': u'example.yml vars="a=1 b=2" tags="tag_a,tag_b"', u'when': u'a == 1', u'tags': [u'tag_c']}

    playbook = p_include.load_data(ds, basedir='')

    # playbook object should be returned
    assert playbook is not None
    assert isinstance(playbook, Playbook)

    play = playbook._entries[0]
    # Play

# Generated at 2022-06-13 08:48:37.013974
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # fake_ds is just a string. It's not a AnsibleMapping.
    # fake_ds_1 is a AnsibleMapping.
    fake_ds = 'fake_ds'
    fake_ds_1 = AnsibleMapping()
    fake_ds_1.ansible_pos = 'fake_pos'
    # fake_bases is a string
    fake_basedir = 'fake_basedir'

    # test case 1: fake_ds is not a dict.
    # ansible_pos is not ready
    try:
        PlaybookInclude.load(fake_ds, fake_basedir)
        assert 'should report error but pass'
    except AnsibleAssertionError:
        assert 1 == 1

    # test case 2: fake_ds is a AnsibleMapping.
    # ansible_pos is ready


# Generated at 2022-06-13 08:48:48.733058
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Play, Playbook

    playbook_include = PlaybookInclude()

    # Test the case when playbook_import has variables
    test_ds = AnsibleMapping()
    test_ds['import_playbook'] = 'main.yml'
    test_ds['vars'] = {'test': 'success'}

    new_ds = playbook_include.preprocess_data(test_ds)
    playbook = playbook_include.load_data(new_ds, '', None, None)
    assert playbook is not None
    assert isinstance(playbook, Playbook)
    assert isinstance(playbook.entries[0], Play)
    assert playbook.entries[0].vars == {'test': 'success'}

    # Test the case when playbook_import has tags
    test_ds = Ansible

# Generated at 2022-06-13 08:48:53.027502
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    playbook_include = PlaybookInclude()
    ds = './foo.yml'
    variable_manager = None
    loader = None
    basedir = './'
    result = playbook_include.load_data(ds, basedir, variable_manager, loader)
    assert result._playbook == ds


# Generated at 2022-06-13 08:49:08.416872
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.utils.collection_loader._collection_finder import _get_collection_playbook_path

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_inventory(loader.load_from_file('tests/unit/inventory.hosts'))

    # to run test use ansible-playbook tests/unit/playbook_inlcude_test.yml --extra-vars '{"included_vars": {"test": 42}}' -i tests/unit/inventory.hosts
    # TODO: use additional playbook to test included_

# Generated at 2022-06-13 08:49:14.201040
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    obj = PlaybookInclude()
    assert isinstance(obj.load_data(ds={}, basedir='test',
                                    variable_manager=None, loader=None), Playbook)
    assert isinstance(obj.load_data(ds={'import_playbook': 'test'}, basedir='test',
                                    variable_manager=None, loader=None), Playbook)
    assert isinstance(obj.load_data(ds=[], basedir='test',
                                    variable_manager=None, loader=None), Playbook)

# Generated at 2022-06-13 08:49:14.755060
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:49:24.135914
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    p = PlaybookInclude.load({}, basedir='/tmp/')
    assert p.load_data({'import_playbook': 'this is a test'}, basedir='/tmp/')

if __name__ == '__main__':
    import pytest
    pytest.main([__file__])

# Generated at 2022-06-13 08:49:25.159974
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    playbook_include = PlaybookInclude()
    playbook_include.load_data("/tmp/test")

# Generated at 2022-06-13 08:49:33.323996
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    playbook_include = PlaybookInclude()
    # Create a sample data structure
    ds = AnsibleMapping()
    ds['import_playbook'] = '../foo/bar/baz'
    ds['vars'] = {'foo': 'bar'}
    # Pass this data structure to the method
    result = playbook_include.load_data(ds=ds, basedir='/path')
    # Check the result
    assert isinstance(result, Playbook)

# Generated at 2022-06-13 08:49:33.852343
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:49:46.708717
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import sys
    import os
    import ansible.parsing.yaml.objects
    import ansible.utils.display
    import ansible.module_utils.six
    import ansible.playbook.attribute
    import ansible.playbook.base
    import ansible.playbook.conditional
    import ansible.playbook.taggable
    import ansible.utils.collection_loader
    import ansible.utils.collection_loader._collection_finder
    import ansible.template
    import ansible.utils.display
    from ansible.playbook.play import Play

    from ansible.playbook.include import PlaybookInclude

    # test 1: execute method load_data
    # source data:
    #    - import_playbook: testplaybook.yml
    # expected result: Playbook object
    ds

# Generated at 2022-06-13 08:49:58.331266
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # Load 'include' and 'vars' fields of data structure
    ppi = PlaybookInclude()
    ds = dict(
            include = "test.yaml",
            vars = dict(
                foo = "foo-value",
                bar = "bar-value",
                dict = dict(
                    dict_key = "dict_value",
                    dict_key2 = "dict_value2",
                    ),
                list = ["list_item1", "list_item2"],
                )
            )

    # Create fake inventory and variable_manager for test
    loader = DataLoader()
    variable_manager = VariableManager()

# Generated at 2022-06-13 08:50:00.415085
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # TODO: write mock for all the mocks
    assert False

# Generated at 2022-06-13 08:50:11.948384
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # setup mock data
    import_playbook = './someplaybook.yaml'
    basedir = '.'
    datastructure = dict(
        import_playbook=import_playbook,
        tags=['tag1', 'tag2'],
        vars=dict(
            var1=1,
            var2=2,
            var3=3,
            var4=4,
        )
    )

    # setup mock objects
    import ansible.playbook.play as play
    import ansible.playbook.playbook as playbook
    import ansible.playbook.task as task
    import ansible.playbook.task_include as task_include

    mock_playbook = playbook.Playbook()

    mock_play_1 = play.Play()
    mock_play_1.post_validate()


# Generated at 2022-06-13 08:50:22.563969
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import_file = os.path.join(C.DEFAULT_LOCAL_TMP, "playbook_include.yaml")
    with open(import_file, "w") as f:
        f.write("---\n")
        f.write("- hosts: all\n")
        f.write("  tasks:\n")
        f.write("  - name: just a debug task\n")
        f.write("    debug:\n")
        f.write("      msg: test playbook_include\n")
    playbook_include = PlaybookInclude.load({
        'import_playbook': import_file
    }, os.path.dirname(import_file))

# Generated at 2022-06-13 08:50:32.242922
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    p = PlaybookInclude()
    p.load_data({'import_playbook':'test.yml'}, basedir='.')
    p.load_data({'import_playbook':'test.yml', 'vars':{'foo':1,'bar':'hello'}}, basedir='.')
    p.load_data({'import_playbook':'test.yml', 'tags':'foobar'}, basedir='.')
    p.load_data({'import_playbook':'test.yml', 'vars':{'foo':1,'bar':'hello'}, 'tags':'foobar'}, basedir='.')
    p.load_

# Generated at 2022-06-13 08:50:39.530147
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass # TODO

# Generated at 2022-06-13 08:50:52.465955
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    # Test when file_name is a collection playbook
    temp_playbook = 'ansible.builtin.test'
    file_name = 'helloworld.ansible_collections.ansible.builtin.test'
    AnsibleCollectionConfig.playbook_paths = ['fake_playbook_path']

    pb = Playbook()
    assert isinstance(pb, Playbook)

    try:
        pb._load_playbook_data(file_name, 'fake_variable_manager', {})
    except TypeError:
        assert 1

    pb._entries = [Play()]
    pb._entries[0].vars = {'tags': 'test'}

# Generated at 2022-06-13 08:51:03.137614
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # test for the method load_data of class PlaybookInclude

    # create a PlaybookInclude object instance
    PlaybookInclude_obj = PlaybookInclude()

    # create a 'ds' object manually
    ds = {"vars": {"a": 1}}

    # create a 'basedir' object manually
    basedir = "/tmp/"

    # create a 'variable_manager' object manually
    variable_manager = None

    # create a 'loader' object manually
    loader = None

    # call the method load_data
    PlaybookInclude_obj.load_data(ds, basedir, variable_manager, loader)

# Generated at 2022-06-13 08:51:15.814266
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.parsing.yaml.objects import AnsibleUnicode

    import_playbook = AnsibleUnicode('test_play.yml')
    vars = dict(test_var='test_value')

    # Create a fake 'Playbook' instance to return from load_data
    Playbook_inst = object()

    # Create a fake 'PlaybookInclude' instance to call load_data on
    # patch the _load_playbook_data method to return the fake Playbook instance
    PlaybookInclude_obj = PlaybookInclude()
    PlaybookInclude_obj._load_playbook_data = lambda *args, **kwargs: Playbook_inst

    # call load_data with our fake UserInput exceptions

# Generated at 2022-06-13 08:51:16.418700
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:51:22.733531
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    with open('./test_data/playbook_import_1.yml') as f:
        data = yaml.safe_load(f)
        from ansible.parsing.dataloader import DataLoader
        from ansible.vars import VariableManager
        variable_manager = VariableManager()
        loader = DataLoader()
        load_result = PlaybookInclude.load(data, './test_data/', variable_manager, loader)
        assert isinstance(load_result, Playbook)
        assert len(load_result._entries) == 2

# Generated at 2022-06-13 08:51:24.589602
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    print("")

# Generated at 2022-06-13 08:51:39.211509
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    import re

    import pytest

    from ansible.module_utils.common.text.converters import to_text
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.utils.collection_loader import AnsibleCollectionConfig


    AnsibleCollectionConfig.playbook_paths.append(os.path.dirname(os.path.abspath(__file__)))

    a_loader = AnsibleLoader(None, None)

    collection_name  = 'test'

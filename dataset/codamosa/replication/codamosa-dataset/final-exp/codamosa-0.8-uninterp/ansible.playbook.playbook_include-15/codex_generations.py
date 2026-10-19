

# Generated at 2022-06-13 08:41:54.433793
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    import unittest

    class TestPlaybookInclude_preprocess_data(unittest.TestCase):
        def test_default(self):
            playbook_import = PlaybookInclude.load({'import_playbook': 'foo'})
            self.assertEqual(playbook_import.import_playbook, 'foo')

        def test_vars(self):
            playbook_import = PlaybookInclude.load({
                'import_playbook': 'foo',
                'vars': {
                    'a': 'b',
                    'c': 'd',
                }
            })
            self.assertEqual(playbook_import.vars, {'a': 'b', 'c': 'd'})


# Generated at 2022-06-13 08:42:07.121241
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    test_data = """---
- import_playbook: test_playbook.yml
  vars:
    foo: true
    baz: false
  tags:
    - one
    - two
"""
    exp_data = {
        'import_playbook': 'test_playbook.yml',
        'vars': {
            'foo': True,
            'baz': False
        },
        'tags': [
            'one',
            'two'
        ]
    }
    data = AnsibleLoader(None, None, None).load(test_data)[0]

# Generated at 2022-06-13 08:42:09.457121
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    pbi = PlaybookInclude()
    pbi.load_data({},'')
    assert pbi.preprocess_data({})

# Generated at 2022-06-13 08:42:20.509510
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    ds = { "import_playbook": "site.yml" }
    pbi = PlaybookInclude()
    new_ds = pbi.preprocess_data(ds)
    assert new_ds == { "import_playbook": "site.yml" }

    ds = { "include": "site.yml" }
    pbi = PlaybookInclude()
    new_ds = pbi.preprocess_data(ds)
    assert new_ds == { "import_playbook": "site.yml" }

    ds = { "include": "site.yml", "vars": { "foo": "bar" } }
    pbi = PlaybookInclude()
    new_ds = pbi.preprocess_data(ds)

# Generated at 2022-06-13 08:42:25.073511
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    import io

    loader = AnsibleLoader(io.StringIO("""
    - hosts: localhost
      remote_user: root
      connection: local
      roles:
         - test
    """))
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='localhost,')
    variable_manager.set_inventory(inventory)

    result = PlaybookInclude.load({
        'import_playbook': 'test.yaml',
        'vars': {'test': 'test'}
    }, '.', variable_manager, loader)
    assert result._entries[0].roles[0].name

# Generated at 2022-06-13 08:42:32.467605
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import pdb; pdb.set_trace()
    #Test of PlaybookInclude._preprocess_import
    ds = PlaybookInclude()
    ds.vars = {'name': 'krishna'}
    #ds.import_file = 'file.yml'
    #ds.vars = {'name': 'krishna'}
    #print(ds.load_data())

    #PlaybookInclude.load(ds, basedir)
    #PlaybookInclude.load_data(ds, basedir)

if __name__ == '__main__':
    test_PlaybookInclude_load_data()
else:
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play

# Generated at 2022-06-13 08:42:38.259114
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    playbook = "test/test_include.yml"
    obj = PlaybookInclude()
    ds = obj.load({"import_playbook" : playbook}, os.path.dirname(playbook))
    assert ds.entries == [PlaybookInclude]


# Generated at 2022-06-13 08:42:51.344984
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.play import Play
    from ansible.parsing.yaml.constructor import AnsibleConstructor
    from ansible.parsing.yaml.loader import AnsibleLoader


# Generated at 2022-06-13 08:43:05.552525
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    YAML_DATA = """
- include_playbook: myplay.yml
    tags: tag1
- include_playbook: myplay.yml
    vars:
      x: "valuex"
      y: "valuey"
      tags: tag2
- include_playbook: myplay.yml
    tags: tag3
    vars:
      x: "valuex"
      y: "valuey"
"""

    from ansible.playbook.play import Play
    from ansible.playbook import Playbook

    p = PlaybookInclude.load(YAML_DATA, os.getcwd())
    assert isinstance(p, Playbook)
    assert p.entries[0] == PlaybookInclude._load(YAML_DATA[2:27], os.getcwd())
   

# Generated at 2022-06-13 08:43:16.874882
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    '''
    Unit test for PlaybookInclude.load_data()
    '''
    import unittest
    import tempfile
    import os.path

    # We need to create a PlaybookInclude object to call the load_data() method.
    # To create a PlaybookInclude object, we need a parent object
    import ansible.playbook.play
    import ansible.playbook.task
    parent_object = ansible.playbook.task.Task()

    # A simple set of data for the test
    playbook = '''
    ---
    - hosts: localhost
      tasks:
        - import_playbook: some.yml
    '''
    playbook_dir = os.path.dirname(tempfile.mkstemp()[1])

# Generated at 2022-06-13 08:43:33.536747
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # import here to avoid a dependency loop
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    input_ds = AnsibleMapping()
    input_ds['import_playbook'] = 'test.yml'
    input_ds['vars'] = AnsibleMapping()
    input_ds['vars']['key1'] = 'value1'
    input_ds['vars']['key2'] = 'value2'

    pbi = PlaybookInclude()
    pb = pbi.load_data(input_ds, basedir='./')
    assert(isinstance(pb, Playbook))
    assert(len(pb._entries) == 1)
    entry = pb._entries[0]
    assert(isinstance(entry, Play))

# Generated at 2022-06-13 08:43:46.000575
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.play_context import PlayContext

    pc = PlayContext()

    # Test when no k=v parameters specified.
    module = PlaybookInclude()
    ds = {'import_playbook': './test_playbook.yml'}
    module.preprocess_data(ds)
    assert(module.import_playbook == './test_playbook.yml')

    # Test when playbook file name is specified as a list
    module = PlaybookInclude()
    ds = {'import_playbook': ['./test_playbook.yml']}
    try:
        module.preprocess_data(ds)
        assert(False)
    except AnsibleParserError:
        pass

    # Test when k=v parameters are specified
    module = PlaybookInclude()
    ds

# Generated at 2022-06-13 08:43:54.162260
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    class TestLoader(object):
        def get_basedir(self):
            return 'testdir'

    class TestVariableManager():
        def get_vars(self):
            return {'testvar': 'testval'}

    import ansible.playbook
    import ansible.playbook.play

    class TestPlay(Play):
        pass

    ansible.playbook.Play = TestPlay
    ansible.playbook.Playbook = Playbook

    base = PlaybookInclude()
    base.load_data({'import_playbook': 'test.yml'}, loader=TestLoader(), variable_manager=TestVariableManager())

    assert base.import_playbook == 'test.yml'
    assert base.vars == {'testvar': 'testval'}

# Generated at 2022-06-13 08:44:04.943728
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import io
    import yaml
    from ansible.playbook.play_context import PlayContext
    pbl = PlaybookInclude.load({}, basedir='/some/basedir', variable_manager=None, loader=None)
    assert pbl.import_playbook == ''
    assert pbl.tags == []
    ds = yaml.safe_load(io.StringIO(u"""
            - import_playbook: some_playbook.yml
              tags:
                - foo
              vars:
                bar: baz
            """))
    pbl = PlaybookInclude.load(ds[0], basedir='/some/basedir', variable_manager=None, loader=None)
    assert pbl.import_playbook == 'some_playbook.yml'
    assert pbl.tags == ['foo']

# Generated at 2022-06-13 08:44:12.606422
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    playbook_include = PlaybookInclude()
    assert playbook_include.import_playbook is None

    playbook = Playbook()

    ds = dict(
        import_playbook = 'test.yml'
    )
    temp_ds = playbook_include.preprocess_data(ds)
    assert playbook_include.import_playbook == 'test.yml'
    assert isinstance(temp_ds, dict)
    result = playbook_include.load_data(temp_ds, '.')
    assert isinstance(result, Playbook)
    assert result._entries[0].vars == dict()
    assert isinstance(result._entries[0], Play)

# Generated at 2022-06-13 08:44:23.963702
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.playbook.playbook_include as playbook_include

    # create a fake datasets
    ds1 = dict(
        import_playbook='playbook/install.yaml',
        vars={
            'install_mode': 'upsert',
        },
        tags=['all'],
        when=['ansible_facts["network"]["interfaces"]["eth0"]["ipv4"]["address"] != "192.168.1.20"'],
    )

# Generated at 2022-06-13 08:44:36.687376
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    p = PlaybookInclude()

    # Strings
    assert p.preprocess_data('tests/test.yml') == {'import_playbook': 'tests/test.yml'}
    assert p.preprocess_data('tests/test.yml tags=foo,bar,batz') == {'import_playbook': 'tests/test.yml', 'tags': 'foo,bar,batz'}
    assert p.preprocess_data('tests/test.yml user=root') == {'import_playbook': 'tests/test.yml', 'vars': {'user': 'root'}}
    assert p.preprocess_data

# Generated at 2022-06-13 08:44:48.656180
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    ds = { 'include': "test.yaml", 'some_other_key': 'some_other_value' }
    expected_ds = { 'import_playbook': "test.yaml", 'some_other_key': 'some_other_value' }
    pi = PlaybookInclude()
    new_ds = pi.preprocess_data(ds)
    assert new_ds == expected_ds

    ds = { 'import_playbook': "test.yaml", 'some_other_key': 'some_other_value' }
    expected_ds = { 'import_playbook': "test.yaml", 'some_other_key': 'some_other_value' }
    pi = PlaybookInclude()
    new_ds = pi.preprocess_data(ds)
    assert new_ds == expected_ds

# Generated at 2022-06-13 08:44:59.330764
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager

    DATA = """
    - import_playbook:
        file: test.yml
        vars:
            fqdn: "{{ inventory_hostname }}"
    """
    PLAYBOOK = """
    - hosts: testhosts
      tasks:
      - debug:
          msg: "{{ fqdn }}"
      - debug:
          msg: "{{ fqdn }}"
    """
    BASEDIR = os.getcwd()

    dl = DataLoader()
    pm = VariableManager()

    # create playbook file

# Generated at 2022-06-13 08:45:01.125020
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    '''
    This test is to make sure the PlaybookInclude class load_data method works as expected.
    '''
    pass

# Generated at 2022-06-13 08:45:14.994447
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # Create a new PlaybookInclude object and load it with the provided data
    test_file = os.path.join(os.path.dirname(__file__), 'playbook_include_data.yml')
    with open(test_file) as test_data:
        playbook = PlaybookInclude.load(data=test_data.read(), basedir=os.getcwd())

    # Check that the playbook object is returned
    assert isinstance(playbook, PlaybookInclude)

    # Check that the PlaybookInclude class returned a new playbook object
    assert isinstance(playbook, Playbook)

# Generated at 2022-06-13 08:45:23.924579
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role

    # this is a test which does not correctly load PlaybookInclude, but only to test load_data
    pbi = PlaybookInclude()
    pbi.import_playbook = '../test/playbooks/playbook_include.yml'
    pbi.vars = {'var_in_include': 'value_in_include'}

    p = pbi.load_data(ds='', basedir='../test/playbooks', variable_manager=None)
    assert isinstance(p, Playbook)

# Generated at 2022-06-13 08:45:36.418185
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar

    import os
    import pytest

    file_name = 'examples/playbook.yml'
    playbook_collection = 'community.general'

    pb_obj = PlaybookInclude()
    pb_obj.import_playbook = playbook_collection + '.' + os.path.basename(file_name)
    pb_obj.tags = ['tag1']

    templar = Templar(loader=None, variables={})
    pb = pb_obj.load_data(ds=None, basedir=os.path.dirname(file_name), variable_manager=None, loader=None)
    
    assert pb is not None
    assert isinstance(pb, Playbook)


# Generated at 2022-06-13 08:45:50.517578
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    #
    # PlaybookInclude class unit tests
    #
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

    # example playbook structure

# Generated at 2022-06-13 08:45:51.213564
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    pass

# Generated at 2022-06-13 08:46:04.336535
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import unittest
    import os
    import sys

    class TestPlaybookInclude_load_data(unittest.TestCase):
        ''' PlaybookInclude load_data tests '''
        def test_load_data(self):
            # import os
            # import sys
            # import unittest
            # from test.test_playbook_include import TestPlaybookInclude_load_data
            # test_suite = unittest.TestLoader().loadTestsFromModule(TestPlaybookInclude_load_data())
            # unittest.TextTestRunner(verbosity=2).run(test_suite)
            # sys.exit(not result.wasSuccessful())
            from ansible.playbook import Playbook
            from ansible.playbook.play import Play
            import ansible.constants as C



# Generated at 2022-06-13 08:46:14.941754
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Play
    from ansible.playbook.taggable import Taggable

    playbook = "my-ansible-collection.username.my-playbook.yml"
    playbook_path = "/home/username/.ansible/collections/ansible_collections/my-ansible-collection/username/my-playbook.yml"
    ds = {'import_playbook': playbook}

    import_file = PlaybookInclude.load(ds, basedir=None)
    assert isinstance(import_file, PlaybookInclude)
    assert import_file.import_playbook == playbook_path
    assert isinstance(import_file.tags, list)
    assert isinstance(import_file.conditions, list)
    assert isinstance(import_file, Taggable)
    assert isinstance

# Generated at 2022-06-13 08:46:22.809000
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from unittest.mock import patch

    ds = {"include": "test.yml"}

    variable_manager = VariableManager()
    loader = DataLoader()
    include = PlaybookInclude.load(ds, variable_manager=variable_manager, loader=loader)
    assert include.import_playbook == "test.yml"

    # test that missing import_playbook in a data structure raises an assertion error
    ds = {"include": ""}
    try:
        PlaybookInclude.load(ds, variable_manager=variable_manager, loader=loader)
    except AnsibleParserError:
        pass
    else:
        assert False

    # test that non-string import_playbook raises an

# Generated at 2022-06-13 08:46:33.905151
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play

    # 1. PlaybookInclude.load_data
    playbook_include_obj = PlaybookInclude()
    _playbook_include_data = dict(
        import_playbook='playbook.yaml',
        tags=['all']
    )
    playbook_include_obj.load_data(ds=_playbook_include_data, basedir='/tmp')

    # 2. PlaybookInclude.load_data
    playbook_include_obj = PlaybookInclude()
    _playbook_include_data = dict(
        import_playbook='playbook.yaml',
        tags=['all']
    )
    playbook_include_obj.load_data(ds=_playbook_include_data, basedir='/tmp')

# Generated at 2022-06-13 08:46:34.518822
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass # TODO

# Generated at 2022-06-13 08:46:43.695064
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    r_PlaybookInclude = PlaybookInclude()

    with pytest.raises(AnsibleAssertionError) as exec_info:
        r_PlaybookInclude.load_data()

    assert 'ds (None) should be a dict but was a NoneType' in str(exec_info.value)

# Generated at 2022-06-13 08:46:57.430109
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    playbook_include = PlaybookInclude()

    # Run test for invalid data structure
    ds = []
    try:
        playbook_include.preprocess_data(ds)
    except AnsibleAssertionError as e:
        assert str(e) == 'ds ([]) should be a dict but was a <class \'list\'>'

    # Run test for valid data structure
    ds = AnsibleMapping({u'import_playbook': u'samples/sample.yml', u'vars': {u'var1': u'value1'}, u'when': u'var1 == value1'})
    ret = playbook_include.preprocess_data(ds)

# Generated at 2022-06-13 08:47:07.871474
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play

    yaml_doc = '''- hosts: localhost

      tasks:
        - import_playbook: test.yml vars:
            foo: bar'''

    yaml_doc2 = """
- hosts: all
  tasks:
    - debug: msg='test'

    - block:
        - debug: msg='foo'
          when: foo
      when: foo
    - import_playbook: test.yml when: foo
    - debug: msg='bar'
      when: bar
    - debug: msg='baz'
"""

    data_structure = {
        'include': yaml_doc,
        'import_playbook': yaml_doc,
    }


# Generated at 2022-06-13 08:47:16.309250
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # An example of PlaybookInclude class
    from ansible.playbook import PlaybookInclude
    from ansible.playbook.play import Play
    from ansible.playbook.base import Base

    # create item for 'test_playbook' file
    test_playbook_item = PlaybookInclude()
    test_playbook_item.ds = {'import_playbook': 'test_playbook.yml'}

    # create item for 'test_playbook_with_vars' file
    test_playbook_with_vars_item = PlaybookInclude()
    test_playbook_with_vars_item.ds = {'import_playbook': 'test_playbook_with_vars.yml'}

    # create item for 'test_playbook_with_tags' file
    test_play

# Generated at 2022-06-13 08:47:26.757792
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    class TestPlaybookInclude(PlaybookInclude):
        def __init__(self):
            super(TestPlaybookInclude, self).__init__()
            self._preprocess_data = True

    obj = TestPlaybookInclude()
    ds1 = dict(import_playbook='site.yml')
    ds2 = dict(import_playbook='site.yml vars=foo.yml')
    ds3 = dict(import_playbook='site.yml vars=foo.yml tags=foo,bar')
    ds4 = dict(import_playbook='site.yml vars=foo.yml tags=foo,bar when={{ foo | default(True) }}')
    ds5 = dict(import_playbook='site.yml tags')

# Generated at 2022-06-13 08:47:39.605558
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # mimic included play
    class Play:
        vars = dict()
        tags = list()
        _included_path = None

    # mimic playbook object
    class Playbook:
        def __init__(self):
            self._entries = list()

        def _load_playbook_data(self, file_name, variable_manager, vars):
            self._entries.append(PlaybookInclude_load_data_Play(variable_manager, vars))

    # mimic play object
    class PlaybookInclude_load_data_Play():
        def __init__(self, variable_manager, vars):
            self.vars = vars
            self.tags = list()
            self._included_path = os.path.abspath(file_name)

    # mimic variable manager

# Generated at 2022-06-13 08:47:50.144998
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # import setup_module/teardown_module
    from ansible.module_utils.basic import AnsibleModule
    import tempfile
    import os
    import shutil
    import subprocess

    AnsibleCollectionConfig.playbook_paths = None
    # setup_module(simple_class)
    tmpdir = tempfile.mkdtemp()
    fname = os.path.join(tmpdir, 'test.yml')
    collection_name = 'my_collection'
    collection_path = os.path.join(tmpdir, collection_name)
    collection_fname = os.path.join(collection_path, 'playbooks', 'test.yml')
    playbook_content = """"
- hosts: localhost
  tasks:
    - debug: msg="foo"
"""

    # Test relative path

# Generated at 2022-06-13 08:48:03.207588
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    # Test with import_playbook in various positions
    # First is the good test case with import_playbook followed by other
    # parameters.  Because we are using the same ds, we have to copy these
    # objects (dict, unicode) before we reassign them, otherwise we modify the
    # ds that the next test will use.

    ds = dict(
        import_playbook='foo',
        tags='bar',
        vars=dict(fizz='buzz'),
        when=dict(test='test')
    )

    import_playbook = 'foo'
    tags = 'bar'
    vars = dict(fizz='buzz')
    when = dict(test='test')

    playbook_include = PlaybookInclude.load({}, variable_manager=None)
    preprocessed_data = playbook_include

# Generated at 2022-06-13 08:48:14.427588
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import datetime
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.vault import VaultLib
    from ansible.vars.manager import VariableManager

    ds = AnsibleLoader(data="""- include_playbook:
        import_playbook: 'test/test_playbook_include.yml'
        vars:
          test_var: True
        tags: test_tag
      """, vault_password='test').get_single_data()
    # test_playbook_include.yml:
    # ---
    # - hosts: 127.0.0.1
    #   connection: local
    #   tasks:
    #     - debug:
    #         msg: success
    #     - debug:
    #         msg: test_var is {{ test

# Generated at 2022-06-13 08:48:15.737455
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass
    # TODO: implement

# Generated at 2022-06-13 08:48:34.774723
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.play_context import PlayContext

    # PlaybookInclude.preprocess_data raises an error when it is not a dictionary
    with pytest.raises(AnsibleAssertionError) as e:
        PlaybookInclude.preprocess_data(None, None, None)
    assert 'should be a dict ' in str(e.value)

    # PlaybookInclude.preprocess_data raises an error when it is not a dictionary
    with pytest.raises(AnsibleParserError) as e:
        PlaybookInclude.preprocess_data('test', None, None)
    assert "should be a dict but was a" in str(e.value)

    # PlaybookInclude.preprocess_data raises an error when vars are mixed with k=v parameters

# Generated at 2022-06-13 08:48:48.123936
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook

    playbook_str = """
    - import_playbook: test.yaml
    """

    collection_playbook_str = """
    - import_playbook: acme.foobar.test.yaml
    """

    collection_playbook_str_versioned = """
    - import_playbook: acme.foobar.1.9.9.test.yaml
    """

    collection_playbook_str_subdir = """
    - import_playbook: acme.foobar.test.subdir.yaml
    """

    # import here to avoid a dependency loop
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play


# Generated at 2022-06-13 08:48:53.808192
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # imports here to avoid dependency loop
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    ds = {
        'import_playbook': 'foo.yml',
        'vars': {'foo': 'bar'}
    }
    pb = PlaybookInclude().load_data(ds=ds, basedir='playbooks_path')
    assert isinstance(pb, Playbook)
    for entry in pb._entries:
        assert entry.vars['foo'] == 'bar'

# Generated at 2022-06-13 08:49:04.417168
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # Setup
    import ansible.playbook as playbook
    import ansible.playbook.play as play

    # Execute
    result = PlaybookInclude.load({'import_playbook': 'test_import_playbook.yml'}, '/home/')

    assert isinstance(result, playbook.Playbook)
    assert isinstance(result._entries[0], play.Play)
    assert result._entries[0].name == 'test_import_playbook'
    assert result._entries[0].hosts == 'test_host'
    assert result._entries[0].vars == {}
    assert result._entries[0].roles == [ { 'role': 'test_role1'}, {'role': 'test_role2'}]
    assert result._entries[0].tasks == []

# Generated at 2022-06-13 08:49:13.157346
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from unittest import TestCase
    import sys

    from ansible.module_utils._text import to_text
    from ansible.parsing.dataloader import DataLoader
    from ansible.parsing.vault import VaultLib
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.template import Templar


    class TestPlaybookInclude(TestCase):

        def setUp(self):
            self.dl = DataLoader()
            self.templar = Templar(loader=self.dl)


# Generated at 2022-06-13 08:49:23.160112
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # construct object
    ds = dict(
        import_playbook='A',
        vars=dict(
            b='B',
        ),
    )

    new_ds = AnsibleMapping()
    new_ds['import_playbook'] = 'A'
    new_ds['vars'] = dict(
        b='B',
    )

    ds_obj = PlaybookInclude()
    out_ds = ds_obj.preprocess_data(ds)
    assert new_ds == out_ds

# Generated at 2022-06-13 08:49:34.965778
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    fake_loader = DictDataLoader({
        "test1.yml": "{% include 'test2.yml' %}",
        "test2.yml": "{% include 'test3.yml' %}",
        "test3.yml": """
            ---
            - name: included play
              hosts: localhost
              gather_facts: no
              pre_tasks:
                - debug: msg="pre tasks"
              tasks:
                - debug: msg="tasks"
              post_tasks:
                - debug: msg="post tasks"
        """,
    })
    fake_variable_manager = Base()
    fake_variable_manager.extra_vars

# Generated at 2022-06-13 08:49:35.629762
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:49:36.321730
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:49:48.893440
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # code to test
    import ansible.playbook as playbook
    import ansible.playbook.play as play
    from ansible.playbook.play import Play
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.playbook_include import _preprocess_import

    # create a playbook include to test
    playbook_include = PlaybookInclude()

    # create a datastructure to load
    ds = '''
    - import_playbook: playbook_file_name
    '''

    # load uut with data ds

# Generated at 2022-06-13 08:50:18.482630
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.errors import AnsibleAssertionError
    import ansible.config
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.parsing.yaml.loader import AnsibleLoader
    import ansible.vars.manager
    import ansible.vars.hostvars
    import ansible.template
    import os
    import sys
    import yaml

    sys.path.insert(0, 'library')
    sys.path.insert(0, 'module_utils')
    sys.path.insert(0, 'plugins')
    sys.path.insert(0, 'lib')
    sys.path.insert(0, 'playbooks')


# Generated at 2022-06-13 08:50:21.455042
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    PlaybookInclude.load_data = PlaybookInclude.load
    new_obj = PlaybookInclude()

# Generated at 2022-06-13 08:50:31.809935
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    # create an instance of PlaybookInclude
    pb_include = PlaybookInclude()

    # create an instance of data structure
    ds = AnsibleMapping()
    # assign the playbook path to the import_playbook variable
    ds['import_playbook'] = 'playbook.yml'

    # create an instance of variable manager
    variable_manager = None

    # create an instance of loader
    loader = None

    # call load_data method of PlaybookInclude class
    result_pb = pb_include.load_data(ds, 'test/test_data', variable_manager, loader)

    # check if result_pb is an instance of Playbook
    assert isinstance(result_pb, Playbook)

    #

# Generated at 2022-06-13 08:50:41.759347
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    data = {'import_playbook': 'playbook.yml', 'vars': {'foo': 'bar'}}
    basedir = './'

    loader = DataLoader()
    variable_manager = VariableManager()
    target = PlaybookInclude().load_data(data, basedir, variable_manager, loader)

    assert(isinstance(target, Playbook))
    assert(len(target._entries) == 1)
    assert(isinstance(target._entries[0], Play))


# Generated at 2022-06-13 08:50:42.348796
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:50:53.506159
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Play

    yaml_ds = "{ import_playbook: foobar.yml, tags: ['foo','bar'], vars: {'baz': 'quux'}, when: {'ansible_distribution': 'RedHat'}, connection: local }"
    my_ds = AnsibleMapping.load(yaml_ds)
    my_pb = PlaybookInclude.load(my_ds)

    assert my_pb._entries[0].vars == {'baz': 'quux'}
    assert len(my_pb._entries[0].tags) == 2
    assert my_pb._entries[0].tags[0] == 'foo'
    assert my_pb._entries[0].tags[1] == 'bar'

# Generated at 2022-06-13 08:51:05.381282
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # Normal use case
    data = 'include.yaml'
    new_data = PlaybookInclude.preprocess_data(data)
    assert new_data == {'import_playbook' : 'include.yaml'}

    # Normal use case with multiple args
    data = 'include.yaml foo=bar'
    new_data = PlaybookInclude.preprocess_data(data)
    assert new_data == {'import_playbook' : 'include.yaml', 'vars' : {'foo' : 'bar'}}

    # Normal use case with args that contain special characters
    data = 'include.yaml foo="bar" baz=\'1.2.3\''
    new_data = PlaybookInclude.preprocess_data(data)

# Generated at 2022-06-13 08:51:17.913999
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    '''
    Test case for the PlaybookInclude method load_data
    '''

    try:
        PlaybookInclude.load(data={}, basedir='')
    except AnsibleParserError:
        pass
    try:
        PlaybookInclude.load(data={'import_playbook': None}, basedir='')
    except AnsibleParserError:
        pass
    try:
        PlaybookInclude.load(data={'import_playbook': [1,2,3]}, basedir='')
    except AnsibleParserError:
        pass
    try:
        PlaybookInclude.load(data={'import_playbook': 'someplay.yml', 'vars': 1}, basedir='')
    except AnsibleParserError:
        pass


# Generated at 2022-06-13 08:51:28.878287
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.task import Task
    x = PlaybookInclude()
    # with simple string parameter
    data = yaml_load("""
- import_playbook: test1.yaml

""")[0]
    res = x.preprocess_data(data)
    assert isinstance(res, AnsibleMapping)
    assert 'import_playbook' in res
    assert len(res['import_playbook']) == 1
    assert isinstance(res['import_playbook'][0], Task)
    assert res['import_playbook'][0].args.get('path') == 'test1.yaml'
    assert not res['import_playbook'][0].args.get('vars')

    # with simple string parameter and 'vars'

# Generated at 2022-06-13 08:51:42.542115
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    """
        Unit test for method load_data of class PlaybookInclude

        Make sure we get a valid Playbook() object back by checking
        for some common attributes it should have.
    """
    import ansible.playbook.play

    # TODO:
    # We should be able to just do this ...
    # from ansible.playbook import Playbook
    # but until we eliminate the module_utils import at the top of this file
    # the import loop won't let that work.

    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

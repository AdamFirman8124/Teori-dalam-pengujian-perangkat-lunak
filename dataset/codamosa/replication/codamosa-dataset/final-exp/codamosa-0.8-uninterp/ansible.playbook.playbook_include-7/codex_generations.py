

# Generated at 2022-06-13 08:41:43.654608
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass



# Generated at 2022-06-13 08:41:44.979562
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass


# Generated at 2022-06-13 08:41:53.603826
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy
    import ansible.constants as C
    playbook_include = PlaybookInclude()
    ds = {C.DEFAULT_ACTION_IMPORT_PLAYBOOK: "test.yml", "test": 1}
    new_ds = playbook_include.preprocess_data(ds)
    assert ds == new_ds


# Generated at 2022-06-13 08:42:05.368892
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    playbookPath = os.path.join(os.path.dirname(__file__), 'test_data')
    filename = os.path.join(playbookPath, 'main_playbook.yml')
    display.verbosity = 4

    loader = DataLoader()
    p = Playbook.load(filename, loader=loader, variable_manager=VariableManager())
    ds = p._entries[0]
    data = ds.preprocess_data(ds._data)

    assert 'import_playbook' in data
    assert data['import_playbook'] == os.path.join(playbookPath, 'imported_playbook.yml')

    assert 'vars' in data
    assert 'Name' in data['vars']
    assert data['vars']['Name'] == 'Jack'

    assert 'tags'

# Generated at 2022-06-13 08:42:07.076999
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    #TODO: Implement test
    pass


# Generated at 2022-06-13 08:42:12.324580
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    loader = None
    variable_manager = None
    basedir = os.path.dirname('/Users/njoshi/Projects/ansible-f5/data/my_features.yml')
    data = {
        'include': 'my_features.yml'
    }
    PlaybookInclude().load_data(ds=data, basedir=basedir, variable_manager=variable_manager, loader=loader)


# Generated at 2022-06-13 08:42:22.767425
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    yaml_obj = {
        'include': 'vars/main.yml',
        'vars': {'testvar': 'test'},
        'tags': ['tag1', 'tag2', 'tag3'],
        'when': ['test1', 'test2'],
        }
    variable_manager = 'some variable manager'
    loader = 'some loader'

    pbi = PlaybookInclude.load(yaml_obj, variable_manager=variable_manager, loader=loader)
    pbi_preprocessed = pbi.preprocess_data(yaml_obj)
    assert 'include' not in pbi_preprocessed
    assert 'import_playbook' in pbi_preprocessed
    assert 'vars' in pbi_preprocessed
    assert 'tags' in pbi_preprocessed


# Generated at 2022-06-13 08:42:30.304993
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    b = PlaybookInclude()
    ds = { 'import_playbook': 'foo.yml' }
    assert isinstance(b.preprocess_data(ds), AnsibleMapping)
    ds = { 'import_playbook': 'foo.yml', 'vars': { 'foo': 'bar' } }
    assert isinstance(b.preprocess_data(ds), AnsibleMapping)
    ds = { 'import_playbook': 'foo.yml', 'tags': 'tag1,tag2' }
    assert isinstance(b.preprocess_data(ds), AnsibleMapping)
    ds = { 'import_playbook': 'foo.yml', 'tags': 'tag1,tag2', 'vars': { 'foo': 'bar' } }

# Generated at 2022-06-13 08:42:45.015561
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    # TODO: Use a mock for ansible.parsing.yaml.objects.AnsibleMapping
    ds = AnsibleMapping()
    ds["hosts"] = "host1"
    ds["tasks"] = [{"debug": "msg=test"}]
    ds["handlers"] = [{"debug": "msg=test"}]
    pb = PlaybookInclude().load_data(ds, os.getcwd())
    assert isinstance(pb, Play)
    assert pb.hosts == "host1"
    assert isinstance(pb.tasks[0], Task)
    assert isinstance(pb.handlers[0], Task)


# Generated at 2022-06-13 08:42:53.263692
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # input data
    basedir = "/home/user/ansible"
    playbook = "tests/ansible-test-playbook.yml"
    playbook_path = os.path.join(basedir, playbook)
    data = {'import_playbook': playbook}

    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    # Loading data
    playbook_include = PlaybookInclude()
    actual_playbook = playbook_include.load_data(data, basedir)

    assert(isinstance(actual_playbook, Playbook))
    for entry in actual_playbook._entries:
        if isinstance(entry, Play):
            assert(entry._included_conditional == data['when'])
            break
    else:
        assert(False)

# Generated at 2022-06-13 08:43:08.805527
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.module_utils._text import to_text
    from ansible.utils.collection_loader import AnsibleCollectionConfig

    collection_name = 'my.collection'
    playbook = 'my_file.yml'
    base_path = '/my/collection/path'
    collection_path = '%s/%s' % (base_path, collection_name)
    playbook_path = '%s/%s/%s' % (base_path, collection_name, playbook)
    playbook_fqcn = '%s.%s.%s' % (base_path, collection_name, playbook)


# Generated at 2022-06-13 08:43:18.229447
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook import Playbook
    from ansible.playbook.playbook import PlaybookCollection
    from ansible.playbook.play import Play

    PlaybookCollection._path_cache.clear()

    pb_incl = PlaybookInclude()
    loader = DataLoader()
    inventory = Inventory('tests/test_data/hosts', loader=loader)
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    # Ensure that load_data returns a new Playbook object

# Generated at 2022-06-13 08:43:19.207590
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:43:31.404766
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Import here to avoid a dependency loop
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook

    def _key_value_pair_to_dict_list(list):
        '''
        Convert a list of key value pair, e.g.
            ['a=x', 'b=y', 'c:z']
        to a dict, e.g.
            {'a': 'x', 'b': 'y', 'c': 'z'}
        '''

        result = {}
        for item in list:
            (key, value) = item.split('=', 1)
            result[key] = value

        return result


# Generated at 2022-06-13 08:43:39.300834
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.vars.manager import VariableManager

    variable_manager = VariableManager()
    variable_manager.set_nonpersistent_facts({'test': 'dummy'})
    playbook_include = PlaybookInclude.load(data='test_file.yml', basedir='/usr/share', variable_manager=variable_manager)

    assert playbook_include.import_playbook == 'test_file.yml'
    assert playbook_include.vars == {'test': 'dummy'}
    assert playbook_include.tags == []

    playbook_include = PlaybookInclude.load(data='test_file.yml tags=tag1,tag2', basedir='/usr/share', variable_manager=variable_manager)

    assert playbook_include

# Generated at 2022-06-13 08:43:43.708193
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os, sys

    # Modify the sys.path when running unit tests
    test_module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    from ansible.module_utils._text import to_bytes
    if test_module_path not in sys.path:
        sys.path.insert(0, test_module_path)

    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task.include import Include
    from ansible.playbook.handler.include import Include as IncludeHandler
    from ansible.template import Templar

    # Load test data, use the path to the module

# Generated at 2022-06-13 08:43:56.468154
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.plugins.loader import find_plugin_filepaths, get_all_plugin_loaders

    plugin_path = find_plugin_filepaths('.')
    get_all_plugin_loaders(plugin_path)
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['/dev/null'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()


# Generated at 2022-06-13 08:44:02.218785
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    with open("tests/parsing/playbook_include.yml", "r") as f:
        file_content = f.read()
    entry = PlaybookInclude.load(data=file_content, basedir="tests/parsing")
    assert entry._entries is not None
    assert entry._entries[0].tasks[0].action == 'ping'

# Generated at 2022-06-13 08:44:02.837969
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:44:04.288806
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass


# Generated at 2022-06-13 08:44:18.083151
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.module_utils._text import to_native

    # Prepare test data
    loader = DataLoader()
    variable_manager = VariableManager()

    # Test an entry with a collections import
    # Note that this is a "molecule" collection
    # However, the collection name is "franklin"
    # This is a side effect of the test_plugins.yml file
    # TODO: 1. Move test_plugins.yml
    #       2. Create a test collection for this test called "franklin"
    #       3. Update the test to use the "franklin" collection

# Generated at 2022-06-13 08:44:26.720907
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.role import Role


# Generated at 2022-06-13 08:44:33.306498
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role_include import RoleInclude
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    ds = dict(
        import_playbook = '{basedir}/test_aj.yml',
        vars = dict(test = 'aaa', test1 = 'aaa1')
    )

    pb = PlaybookInclude().load_data(ds, '/home/user/ansible', variable_manager=VariableManager(), loader=None)
    assert isinstance(pb, PlaybookInclude)

    class DataLoader(object):
        pass

    class Playbook(object):
        pass

   

# Generated at 2022-06-13 08:44:45.738824
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    basedir      = 'test/playbooks'
    playbook_txt = '---\n- hosts: all\n  gather_facts: no\n  connection: local\n  tasks:\n    - debug: msg="This is a test"\n'
    playbook_fn  = '%s/test_playbook_include.yml' % basedir

    with open(playbook_fn, 'w') as f:
        f.write(playbook_txt)

    pb_incl = PlaybookInclude.load({'import_playbook': 'test_playbook_include.yml'}, basedir)
    d = pb_incl.preprocess_data(pb_incl.get_data())

    assert isinstance(d, AnsibleMapping)
    assert isinstance(d, AnsibleBaseYAMLObject)

# Generated at 2022-06-13 08:44:52.368175
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    import os
    basedir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_data')

    ds = dict()
    ds['import_playbook'] = './test_data/test_playbook.yaml'
    ds['vars'] = dict()
    ds['vars']['foo'] = 'bar'
    pbi = PlaybookInclude.load(data=ds, basedir=basedir, variable_manager=None, loader=None)

    assert len(pbi._entries) == 3
    assert isinstance(pbi._entries[0], PlaybookInclude)

# Generated at 2022-06-13 08:44:57.553307
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # Setup
    basedir = '.'
    file_name = './test/test_playbook_include.yml'
    data = {'import_playbook': 'test_playbook_include_load.yml'}
    loader = None
    variable_manager = None

    # Run test
    result = PlaybookInclude.load(data, basedir, variable_manager, loader)

    # Verify
    assert result._entries[0].hosts == 'localhost'

# Generated at 2022-06-13 08:44:58.163999
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass # TODO

# Generated at 2022-06-13 08:45:06.538704
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # Testcase1: import_playbook
    testcase1 = {'import_playbook': 'test.yml'}
    result1 = PlaybookInclude().load_data(testcase1,
            variable_manager=None, loader=None)
    assert result1.import_playbook == 'test.yml'
    # Testcase2: import_playbook with tags
    testcase2 = {'import_playbook': 'test.yml tags=tag1,tag2,tag3'}
    result2 = PlaybookInclude().load_data(testcase2,
            variable_manager=None, loader=None)
    assert result2.import_playbook == 'test.yml'
    assert result2.tags == ['tag1', 'tag2', 'tag3']
    # Testcase3: import_playbook with

# Generated at 2022-06-13 08:45:14.733192
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.playbook.play
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    import ansible.parsing.yaml.loader
    import os

    localhost_data = '{"hosts": {"localhost": {"vars": {"hostvars": {}}}}}'
    temp_vars = VariableManager()
    temp_vars.extra_vars = {'hostvars': {}}
    temp_templar = Templar(loader=None, variables=temp_vars)
    temp_loader = ansible.parsing.dataloader.DataLoader()

# Generated at 2022-06-13 08:45:23.783190
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    import json

    # Test case #1: use the keyword 'include'
    input_data = '''
    include: test.yml
    otherkey: othervalue
    '''
    expected_result = {
        'import_playbook': 'test.yml',
        'otherkey': 'othervalue',
    }

    yaml_obj = AnsibleLoader(None, None).load(input_data)
    actual_result = PlaybookInclude().preprocess_data(yaml_obj)
    assert actual_result == expected_result

    # Test case #2: use the keywords 'include' and 'vars'

# Generated at 2022-06-13 08:45:38.275129
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.template import Templar
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    # init
    display.verbosity = 3
    templar = Templar(loader=None, variables={})
    playbook = Playbook()
    playbook_include = PlaybookInclude()

    # test with wrong file path
    try:
        playbook_include.load_data(ds={'import_playbook': './playbook_include_test.yml'}, basedir='/', variable_manager=None, loader=None)
        assert False
    except AnsibleAssertionError:
        assert True

    # test with correct file path

# Generated at 2022-06-13 08:45:51.736473
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    print("Test load_data")
    yaml_exec = """
    - import_playbook: test.yml
      tags:
      - some_tag
      - other_tag
    """
    playbookInclude = PlaybookInclude().load(data=yaml_exec, basedir="")
    assert playbookInclude.import_playbook == "test.yml"
    assert playbookInclude.tags == ["some_tag", "other_tag"]

    yaml_exec = """
    - import_playbook: test.yml
      vars:
        foo: bar
    """
    playbookInclude = PlaybookInclude().load(data=yaml_exec, basedir="")
    assert playbookInclude.import_playbook == "test.yml"
    assert playbookInclude.vars == {"foo": "bar"}

# Generated at 2022-06-13 08:46:05.139104
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.role_include import RoleInclude
    from ansible.utils.collection_loader._collection_finder import _get_collection_name_from_path, _get_collection_playbook_path

    loader = AnsibleLoader(None, None)
    variable_manager = VariableManager()

    yaml_data = """
    - hosts: web
      tasks:
        - name: test1
          debug: msg='test1'
    """

# Generated at 2022-06-13 08:46:17.408912
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.playbook_include import PlaybookInclude

    # load playbook
    # playbook has tasks:
    play1 = Play().load({'tasks': [{'action': {'module': 'first_task'}}]})
    playbook = Playbook()
    playbook._entries = [play1]
    playbook._entries[0].name = 'play1'

    # objective:
    # - playbook_include has tasks:
    #   - included tasks:
    #     - second_task:
    #     - third_task:
    # - playbook_include has vars:
    #   - var1 = 'value1'
    #   - var2 = 'value2'

    # included playbook
    #

# Generated at 2022-06-13 08:46:29.568737
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    data = dict()
    data['include'] = 'site.yaml'
    data['vars'] = {'a': 'b'}
    data['with_items'] = 'c'
    data['tags'] = 'd'
    data['when'] = 'e'

    data2 = dict()
    data2['import_playbook'] = 'site.yaml'
    data2['vars'] = {'a': 'b'}
    data2['with_items'] = 'c'
    data2['tags'] = 'd'
    data2['when'] = 'e'

    p = PlaybookInclude()
    p._load_data(data)
    res = p.preprocess_data(data)
    assert res == data2, res


# Generated at 2022-06-13 08:46:35.813089
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    lm = AnsibleCollectionConfig()
    pbi = PlaybookInclude()
    pbi.load_data({
        "import_playbook": "blah.yml",
        "vars": {
            "a": "b",
        }
    }, lm)

    pbi.load_data({
        "import_playbook": "blah.yml",
        "vars": {
            "a": "b",
        },
        "tags": "tag1",
    }, lm)

    assert pbi.vars == {
        "a": "b",
    }


# Generated at 2022-06-13 08:46:45.980558
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    # Load a playbook with include
    playbook_include_data = """
    - import_playbook: playbook_include.yml
      vars:
        var_for_playbook_include: hello
    """

    playbook_include_pb = PlaybookInclude.load(playbook_include_data, ".", None, None)
    assert isinstance(playbook_include_pb, PlaybookInclude)
    # Load included playbook

# Generated at 2022-06-13 08:46:59.533986
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # test first use-case with JSON
    # it is a collection playbook, setup default collections
    AnsibleCollectionConfig.default_collection = 'test.col1'

    yaml_config = PlaybookInclude()
    yaml_config.load_data(
        {
            'include': {
                'import_playbook': 'path/to/playbook.yml',
            },
        },
        basedir='/my/dir',
    )
    assert yaml_config.import_playbook == 'path/to/playbook.yml',\
        "yaml_config.import_playbook != 'path/to/playbook.yml' (got: %s)" % yaml_config.import_playbook

    # test second use-case with YAML
    yaml_config = PlaybookInclude()
   

# Generated at 2022-06-13 08:47:10.722398
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # Create a fake playbook to include
    fake_playbook = "include_test.yml"
    with open(fake_playbook, "w") as f:
        f.write("""
- hosts: all
  roles:
    - test_role
""")

    loader, inventory, variable_manager = C.load_from_file('test/units/fixtures/inventory')
    script_dir = os.path.dirname(__file__)
    config = PlaybookInclude.load(
        data=[dict(playbook=fake_playbook)],
        basedir=script_dir, variable_manager=variable_manager,
        loader=loader)

    config.run()
    assert len(config.get_plays()) == 1

# Generated at 2022-06-13 08:47:11.203830
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:47:26.151152
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.utils.path import makedirs_safe, module_loader
    import ansible.constants as C

    ANSIBLE_REPO = os.path.normpath(os.path.join(os.path.dirname(__file__), '../..'))

    FIXTURES_PATH = os.path.join(ANSIBLE_REPO, 'lib/ansible/playbook/tests/fixtures/')
    PLAYBOOK_PATH = os.path.join(ANSIBLE_REPO, 'lib/ansible/playbook/tests/playbooks/')
    EXAMPLES_PATH = os.path.join(ANSIBLE_REPO, 'examples/playbooks/')

# Generated at 2022-06-13 08:47:39.345708
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    playbook_import_data = {
        "import_playbook": "../some/relative/path/to/imported.yml"
    }
    playbook_include_data = {
        "include": "../some/relative/path/to/imported.yml"
    }
    playbook_include_data_1 = {
        "include": "../some/relative/path/to/imported.yml",
        "vars": {
            "foo": "bar"
        }
    }
    playbook_include_data_2 = {
        "include": "../some/relative/path/to/imported.yml",
        "vars": {
            "foo": "bar"
        },
        "tags": "foo_tag"
    }

# Generated at 2022-06-13 08:47:40.554517
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # TODO
    return

# Generated at 2022-06-13 08:47:50.841455
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    #this is just a placeholder for the unit test
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    ####
    ########
    #
    #  The test_include_playbook_in_play function tests the inclusion of a playbook in a host.
    #  The include playbook has no tasks in it, but it has a role, so the role is included in the play.
    #
    ########
    ####

    ansible_playbook_path = "test/integration/include_playbook_in_play"
    playbook = Playbook.load(ansible_playbook_path + "/test_include_playbook_in_play.yml")

    # make sure that the playbook is a Playbook object

# Generated at 2022-06-13 08:48:03.789807
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import io

    import ansible.playbook
    import ansible.playbook.play

    playbook_include = ansible.playbook.PlaybookInclude()

    data = {'import_playbook': './myplaybook.yaml'}

    # PlaybookInclude._load_data() returns an instance of ansible.playbook.Playbook() with
    # one entry

    playbook = playbook_include.load_data(data, basedir='/path/to/playbook')

    assert isinstance(playbook, ansible.playbook.Playbook)
    assert len(playbook._entries) == 1
    assert isinstance(playbook._entries[0], ansible.playbook.play.Play)


#Unit test for method _preprocess_import of class PlaybookInclude

# Generated at 2022-06-13 08:48:05.020285
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass


# Generated at 2022-06-13 08:48:16.505425
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible import context
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    pc = PlayContext()
    templar = Templar(loader=None, variables=VariableManager())


# Generated at 2022-06-13 08:48:28.771727
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    templar = Templar(loader=loader, variables=variable_manager.get_vars())
    basedir = os.path.dirname(os.path.abspath(__file__))

    def check_playbook_included(ds, expected, basedir=''):
        playbook = PlaybookInclude().load_data(ds, basedir, variable_manager, loader)
        assert playbook._entries == expected

    # test regular playbook include

# Generated at 2022-06-13 08:48:29.648915
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass # no test needed - calling a class method causes an error

# Generated at 2022-06-13 08:48:36.879685
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import tempfile
    import shutil
    from ansible.vars.manager import VariableManager
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.removed import removed

    # Create required directories
    collection_dir = tempfile.mkdtemp()
    collection_path = os.path.join(collection_dir, 'ansible_collections', 'collection_name', 'some_namespace')
    os.makedirs(collection_path)
    playbook_path = os.path.join(collection_path, 'playbooks')
    os.makedirs(playbook_path)
    collection_playbook_path = os.path.join(playbook_path, 'playbook.yml')

    # Create empty playbook

# Generated at 2022-06-13 08:48:56.308645
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.plugins.loader import action_loader, module_loader
    from ansible.vars.manager import VariableManager
    from ansible.vars.reserved import Reserved

    ds = AnsibleMapping()
    ds["include"] = "test.yml"
    ds["tags"] = "test"
    ds["vars"] = {}

    pi = PlaybookInclude()

    result = pi.preprocess_data(ds)

    assert isinstance(result, AnsibleMapping)
    assert result["tags"] == ["test"]
    assert result["import_playbook"] == "test.yml"
    assert result["vars"] == {}



# Generated at 2022-06-13 08:49:07.235055
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import sys

    import pytest
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    # test for valid data
    fake_loader = DataLoader()
    variable_manager = VariableManager()
    tempdir = os.path.realpath(__file__)
    basedir = os.path.dirname(tempdir)
    fake_loader.set_basedir(basedir)
    ds = AnsibleMapping(dict(import_playbook=u'../../../examples/playbooks/include_playbook.yml'))
    ds = AnsibleLoader(ds, variable_manager=variable_manager).get_single_data()

    pb = PlaybookInclude.load

# Generated at 2022-06-13 08:49:17.008495
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import sys
    import pytest
    test_dir = os.path.join("test", "test_include.py")
    test_file = os.path.join("test", "test_import.yml")
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    cur_dir = os.path.dirname(__file__)
    AnsibleCollectionConfig.playbook_paths.append(os.path.join(cur_dir, "..", "test", "fixtures", "playbooks"))
    os.chdir(os.path.join(cur_dir, "..", "test", "fixtures", "playbooks"))

    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.inventory import Inventory

# Generated at 2022-06-13 08:49:32.254238
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing import DataLoader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    from ansible.constants import DEFAULT_VAULT_PASSWORD_FILE
    from ansible.module_utils.common._collections_compat import MutableMapping
    import base64
    import os
    import sys

    # create a vault secret for test purpose
    user_password = base64.b64

# Generated at 2022-06-13 08:49:44.636774
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    playbook_include_object = PlaybookInclude()
    ds = dict(
        import_playbook='import_playbook',
        parameter1='parameter1',
        when=dict(
            variable1='variable1'
        )
    )
    variable_manager = dict()

    # First, we check that a dict as ds is correctly processed
    new_ds = playbook_include_object.preprocess_data(ds=ds, variable_manager=variable_manager)
    assert new_ds == dict(
        import_playbook='import_playbook',
        parameter1='parameter1',
        when=dict(
            variable1='variable1'
        )
    )

    # Then, we check that an

# Generated at 2022-06-13 08:49:48.895307
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    playbook_include = PlaybookInclude('test_playbook_include.yml', {'vars': {}})
    playbook_include.load_data({'import_playbook': 'test_playbook_include.yml', 'vars': {}})

    pass

# Generated at 2022-06-13 08:49:59.901153
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.playbook.playbook import Playbook
    from ansible.module_utils import basic
    from ansible.parsing.dataloader import DataLoader
    from ansible.executor import playbook_executor

    display.verbosity = 4
    options = basic.options_vars_for_module([])
    loader = DataLoader()
    variable_manager = VariableManager()
    group_vars = {}
    group_vars_files = {}
    inventory = Inventory()
    inventory.variable_manager = variable_manager


# Generated at 2022-06-13 08:50:01.798083
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # TODO: Write this test once we have a mock-out for loading a Playbook object
    pass

# Generated at 2022-06-13 08:50:13.248957
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    # This is test function for method load_data of class PlaybookInclude.
    # It takes a playbook and an environment, and returns the playbook.
    # This is a stub which does nothing.

    # input for the test and expected output

# Generated at 2022-06-13 08:50:20.191460
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.parsing.yaml.dumper import AnsibleDumper
    import json

    basedir = 'basedir'
    vars = {
        'hello_playbook': 'world_playbook',
        'hello': 'world',
        'foo': 'bar'
    }
    ds = {
        'import_playbook': 'test_import_vars.yml',
        'vars': {
            'hello': 'worl'
        }
    }
    imp = PlaybookInclude.load(ds, basedir, variable_manager=vars, loader=None)

    play1 = Play()
    play1._entries = []

# Generated at 2022-06-13 08:51:02.735164
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play

    playbook_data = '''
        - import_playbook: test.yml
    '''

    playbook_data_2 = '''
        - import_playbook: test.yml
          vars:
            key1: value1
          tags: test
    '''

    playbook_data_3 = '''
        - import_playbook: test.yml
          vars:
            key1: value1
          tags:
            - test
    '''


# Generated at 2022-06-13 08:51:03.312732
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:51:10.464610
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    playbook_include = PlaybookInclude()
    playbook_include.import_playbook = "playbook.yml"
    playbook_include.vars = {}

    playbook = playbook_include.load_data({}, "")
    assert playbook_include.import_playbook == playbook.abs_file_path, "test_PlaybookInclude_load_data: error with load_data method"



# Generated at 2022-06-13 08:51:11.701504
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    PlaybookInclude.load()


# Generated at 2022-06-13 08:51:21.731656
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # import here to avoid a dependency loop
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    pb = PlaybookInclude()
    pb_data = {"import_playbook": "./myfile.yml", "vars": {'var1': 'value1', 'var2': 'value2'}}

    pb_load = Playbook()
    pb_load.vars = {'var1': 'value1', 'var2': 'value2'}
    pb_load.tags = []

# Generated at 2022-06-13 08:51:22.681197
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass


# Generated at 2022-06-13 08:51:37.653911
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.plugin import PluginLoader

    # create a dummy PlaybookInclude object
    obj = PlaybookInclude()
    basedir = '/some/path'

    # create a test config
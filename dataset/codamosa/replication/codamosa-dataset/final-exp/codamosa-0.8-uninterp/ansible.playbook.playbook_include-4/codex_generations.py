

# Generated at 2022-06-13 08:41:56.035327
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    ds = AnsibleMapping()
    ds['import_playbook'] = 'test'
    ds['vars'] = {'x': 1}
    pi = PlaybookInclude()
    new_ds = pi.preprocess_data(ds)
    assert new_ds['import_playbook'] == 'test', 'Not match import_playbook'
    assert new_ds['vars']['x'] == 1, 'Not match vars'
    ds = AnsibleMapping()
    ds['include'] = 'test'
    ds['vars'] = {'x': 1}
    pi = PlaybookInclude()
    new_ds = pi.preprocess_data(ds)
    assert new_ds['import_playbook'] == 'test', 'Not match import_playbook'
    assert new_ds

# Generated at 2022-06-13 08:42:09.000695
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    from ansible.utils.collection_loader._collection_finder import _get_collection_path

    # A real example of a play that includes another at the root of a
    # collection
    root = 'tests/fixtures/collection_include'
    collection_path = os.path.join(root, 'ansible_collections/testns/testcoll')
    _get_collection_path('testns.testcoll')
    playbook_path = os.path.join(collection_path, 'playbooks/collection_include.yml')

# Generated at 2022-06-13 08:42:19.782365
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleSequence

    # Test with no data, should return an empty AnsibleMapping
    empty_ds = PlaybookInclude.preprocess_data({})
    assert isinstance(empty_ds, AnsibleMapping)
    assert len(empty_ds) == 0

    # Test with an invalid data structure, should raise an AnsibleAssertionError
    with pytest.raises(AnsibleAssertionError):
        # noinspection PyUnresolvedReferences
        PlaybookInclude.preprocess_data(AnsibleSequence())

    # Test with a valid data structure, should return an AnsibleMapping
    import_playbook_ds = PlaybookInclude.preprocess_data({'import_playbook': '../roles/common/main.yml'})
   

# Generated at 2022-06-13 08:42:27.181608
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import io
    import os
    import unittest

    import ansible.errors
    import ansible.module_utils
    import ansible.playbook.playbook_include
    import ansible.playbook.playbook

    class AnsibleModuleUtilsPath(unittest.TestCase):

        def setUp(self):
            self.playbook_include_load_data__playbook_include_object = ansible.playbook.playbook_include.PlaybookInclude()

        def tearDown(self):
            pass

        def helper__get_file_path_of_data(self):
            return os.path.join(os.path.dirname(__file__), 'fixtures', 'test_PlaybookInclude_load_data__data.yml')


# Generated at 2022-06-13 08:42:34.533060
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    import yaml

    data = '''
---
- include: test.yml server=test01.example.com
...
'''
    playbook = PlaybookInclude.load(data, '/path/to/playbooks')
    assert playbook.import_playbook == 'test.yml'
    assert playbook.vars['server'] == 'test01.example.com'

    data = '''
---
- import_playbook: test.yml server=test01.example.com
...
'''
    playbook = PlaybookInclude.load(data, '/path/to/playbooks')
    assert playbook.import_playbook == 'test.yml'
    assert playbook.vars['server'] == 'test01.example.com'


# Generated at 2022-06-13 08:42:42.793251
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.utils.collection_loader._collection_finder import _get_collection_name_from_path, _get_collection_playbook_path
    from ansible.utils.vars import combine_vars

    # First, create a valid PlaybookInclude object
    # Then, try loading a playbook. The new object
    # should be a Playbook, but using the PlaybookInclude
    # object to build it

# Generated at 2022-06-13 08:42:55.477923
# Unit test for method preprocess_data of class PlaybookInclude

# Generated at 2022-06-13 08:43:07.820604
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    from ansible.playbook.play_context import PlayContext
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText

    # The configuration object provides some context about the
    # entire execution environment, including the current working
    # directory.
    configuration = PlayContext()

    # An inventory provides the context of what hosts to manage
    # and the host specific variables.
    inventory = None

    # An VariableManager stores the variables and manages their
    # precedence, variables are used to fill in the templates.
    variable_manager = VariableManager(loader=None, inventory=inventory)


    ############
    ## Tests for PlaybookInclude._preprocess_import_playbook
    ##   (in PlaybookInclude.preprocess_data())
    ############

    # Without any other attributes, './other-playbook.yml'

# Generated at 2022-06-13 08:43:17.796054
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    # import here to avoid a dependency loop
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    # TEST CASE 1:
    # Create playbook include with vars and tags as strings
    # ensure load_data properly converts to list
    data = """---
- import_playbook: test.yml
  vars:
    player: "John Black"
  tags: "test"
"""
    playbook_include = PlaybookInclude.load(data=data, basedir='./test/units/lib/ansible/playbook/test_data/')

    assert playbook_include.vars['player'] == "John Black"


# Generated at 2022-06-13 08:43:19.143656
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass


# Generated at 2022-06-13 08:43:35.517055
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook
    from ansible.playbook.block import Block
    from ansible.template import Templar
    from ansible.parsing.dataloader import DataLoader

    yaml_str = """
        - hosts: localhost
          tasks:
            - name: test
              import_playbook: test_import.yaml
              vars:
                name: "test_import_host"
                var_test: "test_import_var"
            - name: test
              import_playbook: test_import.yaml
              vars:
                name: "test_import_host2"
                var_test: "test_import_var2"
          roles:
            - test_import_role
    """

    yaml_str2

# Generated at 2022-06-13 08:43:48.263032
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    import ansible.parsing.yaml.loader

    data = """
    - import_playbook: 'other.yml'
      when: 1==1
    - import_playbook: 'third.yml'
      vars:
        something: 2
        somethingelse: 3
      tags: "tag1,tag2"

    """
    loader = ansible.parsing.yaml.loader.AnsibleLoader(None, None, None)
    ds = loader.load(data)
    assert type(ds) is list
    assert len(ds) == 2

    pb1 = PlaybookInclude.load(ds[0],basedir=None)
    assert pb1.import_playbook == 'other.yml'
    assert pb1.tags == []

    pb2 = PlaybookInclude

# Generated at 2022-06-13 08:43:58.523471
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # pylint: disable=unused-variable
    # pylint: disable=too-many-branches
    # pylint: disable=too-many-statements
    import os
    import tempfile
    from ansible.errors import AnsibleParserError
    from ansible.parsing.yaml.data import DataLoader

    # We are using an unusual style for regexp comparisons in all of the
    # PlaybookInclude tests. Normally, it is considered a bad practice to use
    # assertions within a test, but in this case we have no other good way to
    # get accurate test coverage of the code path through the code. So, here is
    # the justification: When a regexp is used in a condition, the condition
    # may not be true, and therefore the code that is being tested may not be
    # executed. Thus, in

# Generated at 2022-06-13 08:43:59.406867
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    assert True

# Generated at 2022-06-13 08:44:14.936897
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.parsing.yaml.objects import AnsibleUnicode


# Generated at 2022-06-13 08:44:25.130093
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Play
    from ansible.playbook.play import PlaySrc
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block


# Generated at 2022-06-13 08:44:37.089601
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # Set up a stub class so we can call this method
    class pbi(object):

        def load_data(self, ds, basedir, variable_manager=None, loader=None):
            return super(pbi, self).load_data(ds, basedir, variable_manager, loader)

    pbi = pbi()

    # Make up some data to test the method
    ds = {'a': 'b'}
    basedir = 'basedir'
    variable_manager = {'c': 'd'}
    loader = {'e': 'f'}

    # Try to call the method and check for valid output
    expected = '<ansible.playbook.playbook_include.PlaybookInclude object at 0x7f52e7ad2190>'

# Generated at 2022-06-13 08:44:48.845992
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.role.include import RoleInclude
    ds = {
        'include': 'somefile',
        'tasks': [
            dict(action='dummy', foo='bar'),
        ]
    }
    playbook = PlaybookInclude.load(ds, 'ignored')
    play = playbook._entries[0]
    assert isinstance(play, Play)
    assert play.name == 'playbook_include'
    assert len(play.tasks) == 1
    assert play.tasks[0].action == 'dummy'


# Generated at 2022-06-13 08:44:59.701930
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    import ansible.constants as C
    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'hostvars': {'testhost': {'ansible_ssh_host': '127.0.0.1', 'ansible_connection': 'local'}}}
    pbi = PlaybookInclude()
    # Test playbook with vars
    assert pbi.load_data('playbooks/test_playbook_include.yml', basedir=C.DEFAULT_BASEDIR, variable_manager=variable_manager, loader=loader).name == 'playbooks/test_playbook_include.yml'
    # Test playbook with vars
    assert pbi

# Generated at 2022-06-13 08:45:00.224574
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:45:13.811342
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    pbi = PlaybookInclude()
    # test raise of AnsibleAssertionError
    try:
        pbi.preprocess_data(ds="PlaybookInclude")
    except AnsibleAssertionError as ae:
        assert 'should be a dict' in str(ae)
    # test raise of AnsibleParserError
    try:
        pbi.preprocess_data(ds={'vars':"PlaybookInclude"})
    except AnsibleParserError as ae:
        assert 'must be specified' in str(ae)
    # test raise of AnsibleParserError
    try:
        pbi.preprocess_data(ds={'vars':{"vars": "PlaybookInclude"}})
    except AnsibleParserError as ae:
        assert 'cannot be mixed' in str(ae)
   

# Generated at 2022-06-13 08:45:14.881980
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass


# Generated at 2022-06-13 08:45:15.534371
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:45:18.094663
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    playbook_include = PlaybookInclude()
    playbook_include.load_data(ds="../../test/testdata/Test.yml")



# Generated at 2022-06-13 08:45:23.249663
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.playbook

    playbook = ansible.playbook.Playbook()
    playbook_include = ansible.parsing.dataloader.DataLoader().load_from_file(os.path.dirname(__file__) + '/../../../test/unit/data/test_playbook_include.yml')['blocks']
    playbook.load_data(playbook_include, variable_manager=None, loader=None)

# Generated at 2022-06-13 08:45:35.933603
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    '''
    Test PlaybookInclude.preprocess_data()
    '''

    import copy

    def test_data(ds):
        '''
        Test PlaybookInclude.preprocess_data() with the data in the ds

        Param ds: data to test
        '''

        # get the cleaned data
        new_ds = PlaybookInclude.load_data(None, ds, None, None).get_ds()

        check = copy.copy(ds)
        if 'vars' in check:
            check['vars'] = dict()
        if 'tags' in check:
            check['tags'] = list()
        if 'import_playbook' in check:
            check['import_playbook'] = check['import_playbook'].split()[0]

        assert new_ds == check

    #

# Generated at 2022-06-13 08:45:50.392980
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    display.verbosity = 4

# Generated at 2022-06-13 08:46:03.523837
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    # Create an instance of PlaybookInclude class
    playbook_include = PlaybookInclude()

    # Import a playbook and set a variable
    # Playbook path should be ignored as we don't
    # have any playbook here
    ds = {'import_playbook': 'playbook.yml vars:my_var="Hello world"'}
    new_ds = playbook_include.preprocess_data(ds)
    assert (type(new_ds) == AnsibleMapping)
    assert (len(new_ds) == 3)
    assert (new_ds['import_playbook'] == 'playbook.yml')
    assert (new_ds['vars'] == {'my_var': 'Hello world'})

    # Import a playbook in full ansible-playbook style

# Generated at 2022-06-13 08:46:16.428762
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    pbi = PlaybookInclude.load(data={u'import_playbook': u'hero.yml', u'vars': {u'a1': 1}}, basedir='./tests/unit/fixtures/test_playbook_include')

    assert isinstance(pbi, Playbook)

    plays = pbi.get_plays()
    assert len(plays) == 3

    assert plays[0].name == 'a'
    assert plays[1].name == 'b'
    assert plays[2].name == 'c'

    assert plays[0].vars['a1'] == 1
    assert plays[1].vars['a1'] == 1
    assert plays[2].vars['a1'] == 1


# Generated at 2022-06-13 08:46:29.556962
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook.play_context import PlayContext

    pc = PlayContext(loader=None)
    pc.remote_addr = 'a'
    pc.remote_user = 'b'
    ds = {}
    obj = PlaybookInclude()
    obj.play_context = pc

    # single playbook, no params
    ds[C._ACTION_IMPORT_PLAYBOOK] = './pb1'
    res = obj.preprocess_data(ds)
    assert res == {'import_playbook': './pb1'}

    # single playbook, with params
    ds[C._ACTION_IMPORT_PLAYBOOK] = '"./pb2" tags=a,b,c remote_addr={{ ansible_host }} remote_user={{ ansible_user }}'
    res = obj.preprocess_data

# Generated at 2022-06-13 08:46:40.826807
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    playbook_include = PlaybookInclude()
    playbook = Playbook(loader=None)
    ds = {'foobar': 'bar/baz.yml'}
    basedir = '/tmp'
    pb = playbook_include.load_data(ds=ds, basedir=basedir, variable_manager=None, loader=None)
    assert isinstance(pb, Playbook)

# Generated at 2022-06-13 08:46:54.749666
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    ds = dict( include = 'tasks/test.yml', tags = 'test', when = 'true' )
    display.deprecated("Additional parameters in import_playbook statements are deprecated. "
                       "Use 'vars' instead. See 'import_playbook' documentation for examples.", version='2.14')
    pbi = PlaybookInclude()
    newds = pbi.preprocess_data(ds)
    assert newds['import_playbook'] == 'tasks/test.yml'
    assert newds.get('vars') == {}
    assert newds.get('tags') == 'test'
    assert newds.get('when') == 'true'

    # 2.14+ only:
    # test that an error is raised if parameters are specified and 'vars' is also set.

# Generated at 2022-06-13 08:47:03.439825
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    loader = AnsibleLoader(None, dict())

# Generated at 2022-06-13 08:47:14.165999
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    from ansible.module_utils.six import b
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
    from ansible.template import Templar
    from ansible.vars import VariableManager


    ds1 = dict(import_playbook='play.yml', vars=dict(a=1, b=2))
    pl1 = PlaybookInclude()
    playbook1 = pl1.load_data(ds1, '/tmp')
    assert playbook1._entries[0].vars == dict(a=1, b=2)


    ds2 = dict(import_playbook='play.yml', tags=['test'])
    pl2 = PlaybookInclude()
    playbook2 = pl2.load_data(ds2, '/tmp')
    assert playbook2._

# Generated at 2022-06-13 08:47:14.890915
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:47:22.773322
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    command_data = dict(import_playbook='sample_playbook_1.yml')
    from ansible.playbook import Playbook
    basedir = 'path/to/basedir'
    playbook_include = PlaybookInclude()
    playbook_include.preprocess_data(command_data)
    playbook = playbook_include.load_data(playbook_include.data, 
                                          basedir=basedir)
    assert isinstance(playbook, Playbook)


# Generated at 2022-06-13 08:47:29.916951
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    pbi = PlaybookInclude()
    test_data = {
        'import_playbook': 'somefile.yaml',
    }
    new_ds = AnsibleMapping()
    pbi._preprocess_import(test_data, new_ds, 'import_playbook', test_data['import_playbook'])
    assert(new_ds['import_playbook'] == 'somefile.yaml')

    test_data = {
        'import_playbook': 'somefile.yaml vars=foo.yaml',
    }
    new_ds = AnsibleMapping()
    pbi._preprocess_import(test_data, new_ds, 'import_playbook', test_data['import_playbook'])
    assert(new_ds['import_playbook'] == 'somefile.yaml')


# Generated at 2022-06-13 08:47:44.571493
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os

    import pytest

    from ansible.errors import AnsibleParserError
    from ansible.module_utils._text import to_bytes
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.playbook_include import PlaybookInclude
    from ansible.utils.collection_loader._collection_finder import _get_collection_path_from_name

    # Make a test fixture out of this, so we can re-use it in multiple tests
    # Each test can specify the expected exception and expected exception message
    def make_playbook_include_load_data_test(file_name, data=None, loader=None, expect_exception=None, expect_exception_message=None):
        def do_test(basedir):
            loader = loader

# Generated at 2022-06-13 08:47:52.121857
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    class FakeDS(object):
        def __init__(self):
            self.ansible_pos = 'fake'

    # Create a FakeDS object and call preprocess_data
    ds = FakeDS()

    # class PlaybookInclude inherits from class Base, method preprocess_data of which
    # accepts 'ds' of type dict and returns it unchanged
    # We will check for the type of returned object
    obj = Base()

    # Call preprocess_data with a parameter of a different type
    ret = obj.preprocess_data(ds)

    assert ret == ds, 'ret (%s) is not equal to fake ds (%s)' % (ret, ds)

# Generated at 2022-06-13 08:48:01.537363
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play import Play

    playbook = PlaybookInclude.load(ds={
        'import_playbook': '../foo.yml',
        'vars': {
            'foo': True
        }
    }, basedir="../")

    assert isinstance(playbook, Play)
    assert playbook.vars == {'foo': True}
    assert playbook.task_include.import_tasks == '../foo.yml'



# Generated at 2022-06-13 08:48:19.428291
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook

    display.verbosity = 3
    try:
        pb = PlaybookInclude().load_data({'import_playbook': 'myplay.yml'}, '/home/username/ansible/playbooks')
    except Exception as e:
        print(e)
        assert False
    # The playbook that has been created must have one entry, which is a Play
    assert len(pb._entries) == 1
    assert isinstance(pb._entries[0], Play)
    assert pb._entries[0]._included_path is not None



# Generated at 2022-06-13 08:48:28.312349
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    path = "test/unit/ansible/test_playbook_include.yml"
    data = None
    with open(path) as f:
        data = f.read()
    ds = PlaybookInclude.load(data)
    ds2 = ds.preprocess_data(ds.data)
    assert ds2["import_playbook"] == "roles.yml"
    assert ds2["vars"] == {"foo": "bar"}
    assert ds2["when"] == "foo == 'bar'"

# Generated at 2022-06-13 08:48:35.997731
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    # Initialize instance
    instance = PlaybookInclude()
    ds = AnsibleMapping()

    # Set vars
    vars = AnsibleMapping()
    vars["first_var"] = "first_var_value"
    vars["second_var"] = "second_var_value"
    ds["vars"] = vars
    ds["tags"] = "test_tag"

    # Run preprocess_data method
    result = instance.preprocess_data(ds)

    # Check results
    expected_result = AnsibleMapping()
    expected_result["vars"] = vars
    expected_result["tags"] = "test_tag"
    assert result == expected_result

# Generated at 2022-06-13 08:48:48.296945
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # can be used with `python -m pytest test_playbook_include.py`
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.vars.reserved import reserved_variables

    loader = DataLoader()
    variable_manager = VariableManager(loader=loader)
    variable_manager._extra_vars = {"omg_test": True}
    variable_manager._extra_vars.update(reserved_variables)


# Generated at 2022-06-13 08:48:56.007894
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    yml_str= """
- hosts: all
  vars:
     var1: 1
     var2: 2
  tasks:
    - debug: msg="{{var1}}"
"""
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    
    from ansible.parsing.dataloader import DataLoader

    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    from ansible.executor.task_queue_manager import TaskQueueManager
    
    
    
    loader = DataLoader()
    variable_manager = VariableManager()

# Generated at 2022-06-13 08:49:08.491388
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pbi = PlaybookInclude()
    pbi.import_playbook = 'test.yml'
    pbi.vars = { 'var1': 'value1' }
    pb = pbi.load_data(ds={}, basedir=os.path.join(os.path.dirname(__file__), '..', '..', '..', 'test', 'data'))
    assert pb.get_hosts() == ['all']
    assert pb._entries[0]._included_path == os.path.join(os.path.dirname(__file__), '..', '..', '..', 'test', 'data')



# Generated at 2022-06-13 08:49:16.134641
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import re
    import sys
    import pytest

    with pytest.raises(AnsibleParserError) as excinfo:
        assert PlaybookInclude.load({'import_playbook': None}, 'basedir', None)
    assert excinfo.match('playbook import parameter is missing')

    with pytest.raises(AnsibleParserError) as excinfo:
        assert PlaybookInclude.load({'import_playbook': {}}, 'basedir', None)
    assert excinfo.match('playbook import parameter must be a string')


# Generated at 2022-06-13 08:49:31.641185
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.inventory import Inventory
    loader = DataLoader()
    variable_manager = VariableManager()
    play_context = PlayContext()
    play = Play()
    play.name = 'Test Play'
    play.playbook = 'test.yml'
    play.hosts = 'localhost'
    play.connection = 'local'
    variable_manager.extra_vars = { 'foo' : 'bar'}
    variable_manager.options_vars = { 'inventory': [ Inventory("/some/path/to/inventory"), ] }
   

# Generated at 2022-06-13 08:49:42.616215
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook

    playbook_include = PlaybookInclude()
    # playbook_include.vars = {}
    playbook_include.load_data({'import_playbook': '../../../vagrant/ubuntu16.04/playbook.yml'}, '../../../vagrant/ubuntu16.04/', None)
    # playbook_include.load_data({'import_playbook': '../../../vagrant/ubuntu16.04/playbook.yml'}, '../../../vagrant/ubuntu16.04/', None, None)
    assert isinstance(playbook_include, Playbook)
    # assert isinstance(playbook_include, PlaybookInclude)


# Generated at 2022-06-13 08:49:54.356613
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    #
    # Load the playbook
    #
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=None)

    #
    # Create the object
    #
    pi = PlaybookInclude()
    pi = pi.load_data(ds=None, basedir=None, variable_manager=variable_manager, loader=loader)
    #
    # Check the result
    #
    assert(pi.import_playbook is None)
    assert(pi.vars == {})
    assert(pi.tags == [])
    assert(pi.when == [])

# Generated at 2022-06-13 08:50:04.163099
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Test PlaybookInclude.load_data() with external data in YAML format
    # TODO
    pass

# Generated at 2022-06-13 08:50:11.449765
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.playbook.play as play
    import ansible.playbook.task as task
    import ansible.playbook.role as role
    from ansible.module_utils.six import string_types

    p = PlaybookInclude()
    p.import_playbook = "test_yaml_object.yaml"
    p.vars = {"var1" : "test_var1"}
    # todo we really need to mock this out so it does not create
    # a playbook, just for the sake of unit tests
    pb = p.load_data(ds=p.to_data(), basedir=".", variable_manager={}, loader={})

    # check that all of the parsed playbooks have the correct
    # attributes and are the expected objects
    assert isinstance(pb, play.Playbook)
    assert pb

# Generated at 2022-06-13 08:50:12.219238
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:50:23.162660
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.base import PlaybookBase
    from ansible.playbook import Playbook, Play

    from ansible.playbook.play import Play
    from ansible.playbook.tasks import Task
    from ansible.playbook.handlers import Handler

    from ansible.playbook.task_include import TaskInclude

    from ansible.vars.manager import VariableManager

    from ansible.module_utils.six import StringIO
    import yaml
    import json
    import hiss
    import difflib

    basedir = os.path.dirname(__file__)
    playbook_path = os.path.join(basedir, 'data/import_playbook.yml')
    ds_path = os.path.join(basedir, 'data/import_playbook_ds.json')


# Generated at 2022-06-13 08:50:28.771714
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.template import Templar
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    pb = PlaybookInclude()
    data = {
        'import_playbook':'test.yaml',
        'tags': 'all, notme',
        'vars': {
            'var1':'value1',
            'var2':2
        }
    }
    basedir

# Generated at 2022-06-13 08:50:39.261749
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import sys
    import json
    import shutil
    import tempfile

    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.executor.playbook_iterator import PlaybookIterator
    from ansible.template import Templar
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.utils.display import Display

    display = Display()
    display.verbosity = 4

    with tempfile.TemporaryDirectory() as tmpdir:
        collection_path = os.path.join(tmpdir, 'ansible_namespace-collection-0.1.0')
        collection_root_path = os.path.join(collection_path, 'ansible_namespace')

# Generated at 2022-06-13 08:50:49.556556
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')

    # Test with 'import_playbook' key
    ds = dict(import_playbook='../../tasks/main.yml')
    pi = PlaybookInclude.load(ds, '/some/root/path', None, loader)
    assert pi.import_playbook == '../../tasks/main.yml'

    # Test with 'include' key
    ds = dict(include='../../tasks/main.yml')
    pi = PlaybookInclude.load(ds, '/some/root/path', None, loader)

# Generated at 2022-06-13 08:51:02.781120
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.playbook.play  # import needed because of the dynamic class loading
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    import ansible.playbook  # import needed because of the dynamic class loading
    from .unit.test_loader import DictDataLoader
    from .unit.mock.loader import DictDataLoader as MockDictDataLoader
    from ansible.parsing.dataloader import DataLoader

    # when playbook is empty, playbook_include should return empty playbook
    playbook_include = PlaybookInclude.load({}, 'f')
    assert(isinstance(playbook_include, ansible.playbook.Playbook))

# Generated at 2022-06-13 08:51:03.400976
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:51:16.127825
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import tempfile
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    dl = DataLoader()
    ansible_collections_path = os.path.expanduser('~/.ansible/collections/')
    if not os.path.exists(ansible_collections_path):
        os.makedirs(ansible_collections_path)
    t = tempfile.mkdtemp(dir=ansible_collections_path)
    collection_name = t.split('/')

# Generated at 2022-06-13 08:51:39.895968
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.utils.collection_loader import AnsibleCollectionConfig
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy

    import collections
    import os

    os.environ["ANSIBLE_COLLECTIONS_PATHS"] = "/etc/ansible/collection"
    data = """
        - hosts: 127.0.0.1
          gather_facts: no
          connection: local
          tasks:
            - debug:
                msg: test
        """.strip()

    basedir = os.path.abspath(os.curdir)

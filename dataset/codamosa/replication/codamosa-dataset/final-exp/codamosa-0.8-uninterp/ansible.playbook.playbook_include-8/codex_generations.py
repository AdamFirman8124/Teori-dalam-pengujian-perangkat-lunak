

# Generated at 2022-06-13 08:41:55.042094
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = None

    # Test invalid data structures
    ds = [{'import_playbook': 'test.yml'}]
    obj = PlaybookInclude(loader=loader, variable_manager=variable_manager)
    assert not obj.preprocess_data(ds)

    ds = {'import_playbook': 'test.yml', 'vars': 'test'}
    obj = PlaybookInclude(loader=loader, variable_manager=variable_manager)
    assert not obj.preprocess_data(ds)

    # Test valid data structures
    ds = {'import_playbook': 'test.yml', 'vars': {'test': 'true'}}

# Generated at 2022-06-13 08:42:08.036600
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    import ansible.playbook.play_context
    import ansible.playbook.play
    import ansible.inventory.host
    import ansible.inventory.group
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.conditional import Conditional
    from ansible.playbook.block import Block

    def test_play_init(self, play=None, ds=None):
        self._ds = ds
        self.name = None
        self.hosts = []
        self.lazy_hosts = []
        self.roles = []
        self.combine = True
        self.local_action = None
        self.serial = None
        self.post_tasks = []
        self.pre_tasks = []
        self.pre_validate = []
        self

# Generated at 2022-06-13 08:42:15.870411
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook

    playbook = Playbook()
    playbook._load_playbook_data(file_name=os.path.join(os.path.dirname(__file__), '..', 'test_data', 'playbooks', 'include_playbook_test.yml'),
                                 variable_manager=None,
                                 vars=None)

    assert len(playbook._entries) == 3
    assert playbook._entries[0]._included_path == os.path.join(os.path.dirname(__file__), '..', 'test_data', 'playbooks')
    assert playbook._entries[0].name == 'include playbook test'
    assert playbook._entries[0].hosts == 'localhost'
    assert playbook._entries

# Generated at 2022-06-13 08:42:25.607123
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    # Assert that preprocess_data raises Exception when ds is not a dictionary.
    #
    # (make_yaml_object returns a AnsibleBaseYAMLObject from a dict and has
    # a .ansible_pos attribute which is needed for the Exception's obj)
    ds_not_dict = make_yaml_object({'a': 'test'})
    ds_not_dict.a = 'string'  # AnsibleBaseYAMLObjects are not subscriptable
    with pytest.raises(AnsibleAssertionError) as excinfo:
        PlaybookInclude.preprocess_data(ds_not_dict)
    assert "to be a dict" in str(excinfo.value)

    # Assert that preprocess_data raises Exception when an import_playbook import is
    # not in the dict

# Generated at 2022-06-13 08:42:33.411867
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    import ansible.parsing.yaml.objects
    import ansible.playbook.play
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    import collections

    Role = collections.namedtuple('Role', 'name role_path')

    # Test with no given value (should raise an error)
    test_data = {'import': None}
    test_pb = PlaybookInclude()
    try:
        test_pb.preprocess_data(test_data)
        raise AssertionError('AnsibleParserError exception not raised')
    except AnsibleParserError:
        pass

    # Test with value not being a string (should raise an error)
    test_data = {'import': 5}

# Generated at 2022-06-13 08:42:42.576577
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    import_playbook_test_data = [
       {
            'import_playbook':'test.yml',
            'vars':{'x': 'y'},
            'tags':'test1'
       },
       {
            'import_playbook':'test.yml',
            'vars':{'x': 'y'},
            'tags':['test1,test2']
       },
       {
            'import_playbook':'test.yml',
            'tags':'test1,test2'
       },
       {
            'import_playbook':'test.yml',
            'tags':['test1,test2']
       }
    ]

# Generated at 2022-06-13 08:42:55.351708
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    '''
    Test preprocess_data method of class PlaybookInclude
    '''

    # Test without any data
    data = ''
    result = PlaybookInclude.load(data=data, basedir='/tmp/')
    assert result == dict()

    # Test with simple playbook includes
    data = '''
- import_playbook: base.yml
- import_playbook: apache.yml
- import_playbook: php.yml
'''
    result = PlaybookInclude.load(data=data, basedir='/tmp/')
    assert result == dict()

    # Test with playbook include with tags

# Generated at 2022-06-13 08:43:07.763920
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from unittest.mock import MagicMock, call
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager

    ds = {
        'include': 'test.yaml',
        'vars': {
            'var1': 'value1',
            'var2': 2,
        },
        'tags': ['tag1', 'tag2'],
        'when': "inventory_hostname == 'localhost'"
    }

    mock_loader = MagicMock()
    mock_variable_manager = MagicMock()
    mock_variable_manager.get_vars.return_value = {}
    mock_playbook = MagicMock()
    mock_playbook._load_playbook_data

# Generated at 2022-06-13 08:43:08.651269
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:43:18.139296
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    variable_manager = VariableManager()
    loader = DataLoader()

    play_context = PlayContext()
    variable_manager.set_inventory(loader.load_from_file("/home/ansible/ansible/test/unit/inventory/test.inv"))


    # Test that load_data returns a Playbook object with data from the file specified by new_obj.import_playbook
    # when new_obj.import_playbook is a relative path
    new_obj = PlaybookInclude()

# Generated at 2022-06-13 08:43:34.690342
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    import yaml

    # Create a playbook
    playbook_data = '''
    - hosts: all
      remote_user: root
      gather_facts: false
      pre_tasks:
      - name: ping
        ping:
      roles:
      - role: my_role
      post_tasks:
      - name: pong
        ping:
    '''
    playbook_path = "my_playbook.yml"
    file_path = os.path.join(C.DEFAULT_LOCAL_TMP, playbook_path)
    with open(file_path, 'w') as f:
        f.write(playbook_data)

    # Create the include

# Generated at 2022-06-13 08:43:46.925070
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook import PlaybookInclude

    # helper function to verify the structure of a datastructure
    def _verify_ds(ds, expected_import, expected_vars, expected_tags):
        if ds.get('import_playbook') != expected_import:
            raise AssertionError("Unexpected import_playbook, expected %s, got %s" % (expected_import, ds.get('import_playbook')))
        if ds.get('vars') != expected_vars:
            raise AssertionError("Unexpected vars, expected %s, got %s" % (expected_vars, ds.get('vars')))

# Generated at 2022-06-13 08:43:57.483305
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # test for PlaybookInclude.load_data with conditional
    new_obj = PlaybookInclude()
    ds = dict(import_playbook="test.yml", when=dict(test="test"))
    variable_manager = dict(test="test")
    basedir = "ansible/playbooks"
    pb = new_obj.load_data(ds, basedir, variable_manager)
    assert pb._load_name == 'test.yml'
    assert pb._entries[0]._attributes['vars'] == dict()
    assert pb._entries[0]._attributes['name'] == 'test.yml'
    assert pb._entries[0]._attributes['when'] == ds['when']

# Generated at 2022-06-13 08:44:12.933856
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleMapping, AnsibleUnicode
    from ansible.parsing.yaml.loader import AnsibleLoader

    # NOTE: I think the second of these isn't valid anymore, but I don't want to delete it
    #       as it's a good test case, and preprocess_data is going to be deprecated anyway
    #       as it's just doing a lot of string parsing that's now handled by the YAML parser

# Generated at 2022-06-13 08:44:16.241496
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    p = PlaybookInclude()
    p.load_data("test1.yml")

    assert p.import_playbook == "test1.yml"

# Generated at 2022-06-13 08:44:25.960778
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.yaml.objects import AnsibleSequence
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    t = Templar()
    context = PlayContext()
    vm = dict()

    ds = dict(
        import_playbook='imported_playbook.yml',
        when=['inventory_hostname != "localhost"'],
        tags=['foo', 'bar'],
        vars=dict(
            debug='{{ debug }}{{ extra_debug }}',
            extra_debug='text',
        )
    )

    pi = PlaybookInclude().load_data(ds=ds, basedir='.', variable_manager=vm, loader=t)

# Generated at 2022-06-13 08:44:37.482372
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os

    from ansible.errors import AnsibleParserError
    from ansible.parsing.dataloader import DataLoader

    from units.mock.loader import DictDataLoader


# Generated at 2022-06-13 08:44:49.017447
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():

    import_playbook = AnsibleMapping()
    import_playbook.ansible_pos = (1,1)
    import_playbook.import_playbook = "path/to/new/playbook.yml"
    import_playbook.tags = "tag1,tag2"
    import_playbook.vars = {'key1': 'val1', 'key2': 'val2'}
    import_playbook.when = "host.hostname in groups['app_servers']"

    new_ds = PlaybookInclude.load(data=import_playbook, basedir=".")
    assert new_ds.import_playbook == "path/to/new/playbook.yml"
    assert new_ds.tags == ["tag1", "tag2"]

# Generated at 2022-06-13 08:44:57.164718
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Instantiate the class and test method load_data
    data = {'import_playbook':'file_name'}
    pb = PlaybookInclude()
    data_load = pb.load_data(ds=data, basedir='/', variable_manager='', loader='')
    # Assertions
    assert pb.import_playbook == data['import_playbook']
    assert pb.vars == {}
    assert isinstance(data_load, PlaybookInclude)
    assert isinstance(data_load.import_playbook, string_types)

# Generated at 2022-06-13 08:45:04.560719
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    result = PlaybookInclude.load(dict(import_playbook = '../../other.yml foo=bar'), '/path/to/roles/role1/tasks')
    assert result.import_playbook == '../../other.yml'
    assert result.vars == dict(foo='bar')

    # Test tags parameter
    result = PlaybookInclude.load(dict(import_playbook = '../../other.yml tags=foo,bar'), '/path/to/roles/role1/tasks')
    assert result.import_playbook == '../../other.yml'
    assert result.tags == ['foo', 'bar']


# Generated at 2022-06-13 08:45:14.650288
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.parsing.yaml.loader import AnsibleLoader
    import sys

    vars_check = dict(
        my_var='TEST1',
        my_var2='TEST2'
    )

    playbook_str = """
    - import_playbook: my_playbook.yml vars: my_var: TEST1 tags: tag1 vars: my_var2: TEST2 tags: tag2
    """
    playbook_data = AnsibleLoader(playbook_str).get_single_data()
    playbook = PlaybookInclude.load(playbook_data, '', variable_manager=None, loader=None)

# Generated at 2022-06-13 08:45:23.758499
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=[])
    play = Play.load(dict(
        name="Ansible Play",
        hosts='all',
        gather_facts='no',
        tasks=[dict(action=dict(module='shell', args='ls'), register='shell_out'),
               dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))]
    ), variable_manager=variable_manager, loader=loader)

    # test empty entry

# Generated at 2022-06-13 08:45:25.318481
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # TODO: write unit test
    pass

# Generated at 2022-06-13 08:45:37.042588
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.playbook.play
    import ansible.playbook.task

    # validate load_data function in PlaybookInclude class
    # a valid scenario
    # scenario: import play, validate it is ansible.playbook.play.Play instance
    # scenario: import role, validate it is ansible.playbook.task.Task instance (Task are used for roles)
    # scenario: import task, validate it is ansible.playbook.task.Task instance
    playbook_include = PlaybookInclude()
    playbook = playbook_include.load(data={"import_playbook": "tests/data/play.yml"}, basedir=".")
    assert playbook
    assert playbook.get_entries()
    assert len(playbook.get_entries()) == 1

# Generated at 2022-06-13 08:45:50.695385
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.module_utils.six import BytesIO

    # Ansible variables
    from ansible.vars import VariableManager
    varmgr = VariableManager()
    varmgr.extra_vars = {'ansible_host': 'this_host', 'ansible_user': 'this_user'}

    # Ansible data structures
    from ansible.parsing.loader import DataLoader
    loader = DataLoader()

    # Ansible templating engine
    from ansible.template import Templar
    templar = Templar(loader=loader, variables=varmgr.extra_vars)

    # Ansible inventory
    from ansible.inventory.manager import InventoryManager
    inventory = InventoryManager(loader=loader)
    inventory.add_group('group_a')
    inventory.add_host(host='host_a')

# Generated at 2022-06-13 08:45:51.762842
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # TODO: Write unit test
    pass

# Generated at 2022-06-13 08:46:05.902059
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from units.mock.loader import DictDataLoader
    from ansible.vars import VariableManager
    vm = VariableManager()
    loader = DictDataLoader({})
    data = {'import_playbook': '../../apps/db-server.yml', 'tags': 'database', 'vars': {'db_server_port': '3306', 'extra_params': '-p'}}
    objects = list(PlaybookInclude.load(data, '/path/to/playbooks', variable_manager=vm, loader=loader))
    assert objects[0].hosts == 'db_server'
    assert objects[0].tags == ['database']
    assert objects[0].vars == {'db_server_port': '3306', 'extra_params': '-p'}

# Generated at 2022-06-13 08:46:15.612576
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.template import Templar
    from ansible.vars import VariableManager

    DATA = AnsibleMapping({
        'import_playbook': 'test_playbook_include.yml',
        'vars': AnsibleMapping({'asd': 'qwerty'}),
        'tags': ['tag1', 'tag2'],
    })

    # test_PlaybookInclude_load_data - without conditional
    pbi = PlaybookInclude()
    pbi.load_data(DATA, basedir='/tmp')

# Generated at 2022-06-13 08:46:28.298367
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import pytest

    # test: invalid file name
    data = {u'import_playbook': u'invalid_file'}
    basedir = 'some/basedir'
    variable_manager = None
    loader = None
    with pytest.raises(AnsibleParserError):
        PlaybookInclude.load(data, basedir, variable_manager, loader)

    # test: invalid playbook
    data = {u'import_playbook': u'invalid_playbook.yml'}
    with pytest.raises(AnsibleError):
        PlaybookInclude.load(data, basedir, variable_manager, loader)

    # test: playbook with valid path but having variables

# Generated at 2022-06-13 08:46:29.508375
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # TODO: write this
    pass

# Generated at 2022-06-13 08:46:44.488601
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import tempfile
    import shutil
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play

    play_context = PlayContext()

    basedir = tempfile.mkdtemp()
    playbook_path = tempfile.mkstemp(suffix='yaml', dir=basedir)[1]

    playbook_content = '''
    - hosts: localhost
      tasks:
        - import_playbook: simple.yaml
          vars:
            key: value
          tags:
            - a
            - b
          when: condition
    '''

    with open(playbook_path, 'w') as f:
        f.write(playbook_content)


# Generated at 2022-06-13 08:46:45.254823
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:46:46.571291
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass
    # obj = PlaybookInclude()

# Generated at 2022-06-13 08:46:59.866798
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role import Role
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    import ansible.constants as C
    import os
    basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    loader = DataLoader()
    inventory = loader.load_inventory('/etc/ansible/hosts')
    variable_manager = VariableManager(loader=loader, inventory=inventory)

# Generated at 2022-06-13 08:47:11.982371
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # create a simple playbook
    p = PlaybookInclude()
    playbook_lines = [
        '- import_playbook: disk_space.yml',
        '- import_playbook: disk_utilization.yml vars:',
        '    threshold_percentage: 80',
        '- import_playbook: disk_utilization.yml vars:',
        '    threshold_percentage: 80',
        '  tags:',
        '    - disk_util',
        '- include_tasks: other.yml tags=foo',
        '- import_playbook: something_else.yml',
        '  when: zomg_condition',
        '',
    ]

# Generated at 2022-06-13 08:47:24.200111
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_variable_mapping(
        {
            'v1': 'value1',
            'v2': 'value2',
            'v3': 'value3',
            'simple': 'value'
        }
    )

    pb1 = PlaybookInclude.load(
        {
            'include': '../include.yml'
        },
        './',
        variable_manager,
        loader
    )


# Generated at 2022-06-13 08:47:37.534979
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # test_file is a "hello world" playbook
    test_file = os.path.join(os.path.dirname(__file__), 'pb_include_test_file')

    # test_file_2 is another "hello world" playbook
    test_file_2 = os.path.join(os.path.dirname(__file__), 'pb_include_test_file_2')

    # test_file_inv is a simple inventory file
    test_file_inv = os.path.join(os.path.dirname(__file__), 'test_file_inv')

    # test_file_inv_host is a simple inventory file
    test_file_inv_host = os.path.join(os.path.dirname(__file__), 'test_file_inv_host')

    # test_file_inv

# Generated at 2022-06-13 08:47:48.670777
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.include import RoleInclude

    # test loading a playbook with a single task
    data = dict(
        import_playbook = 'included.yml'
    )
    ret = PlaybookInclude.load(data, '/path/to', None, None)
    assert type(ret) is Playbook
    assert len(ret._entries) == 1
    assert type(ret._entries[0]) is Play
    assert ret._entries[0].name == 'included.yml'

    # test loading a playbook with a single task and a vars: section

# Generated at 2022-06-13 08:48:02.012770
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import sys
    import unittest
    import tempfile
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.playbook_include import PlaybookInclude

    from ansible.playbook import Playbook

    class TestPlaybookInclude(unittest.TestCase):
        def setUp(self):
            self.loader = DataLoader()

        def tearDown(self):
            pass

        def test_load_data_not_in_dir_relative(self):
            '''
            Test playbook include load_data() with a playbook.
            This test uses a playbook in the same directory as the test
            '''
            # Pretend the current directory is the test directory
            # This makes the test run independent of the current directory
            # It also makes the test work on Windows


# Generated at 2022-06-13 08:48:09.438583
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    """
    Test load_data on PlaybookInclude
    """
    import ansible.playbook.play
    # pylint: disable=unused-variable
    import ansible.playbook.tasks

    class MockPlaybookInclude(PlaybookInclude):
        """
        Mocked PlaybookInclude for testing load_data
        """
        def _load_playbook_data(self, filename, variable_manager, vars):
            """
            Mock the actual loading of data
            """
            self._entries.append(ansible.playbook.play.Play())
            self._entries.append(ansible.playbook.play.Play())
            self._entries.append(ansible.playbook.play.Play())

# Generated at 2022-06-13 08:48:16.147098
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass

# Generated at 2022-06-13 08:48:26.441669
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    playbook_include = PlaybookInclude()
    playbook = Playbook.load(
        dict(
            import_playbook=['playbook.yml'],
            vars=dict(key1='value1')
        ),
        basedir='/root/playbooks',
        variable_manager=None,
        loader=None
    )
    assert playbook_include.import_playbook == 'playbook.yml'
    assert playbook_include.vars == dict(key1='value1')
    assert isinstance(playbook, Playbook)
    assert len(playbook._entries) == 1

# Generated at 2022-06-13 08:48:35.664914
# Unit test for method preprocess_data of class PlaybookInclude
def test_PlaybookInclude_preprocess_data():
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleUnicode
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.parsing.yaml.loader import AnsibleLoader
    PlaybookInclude.add_attribute(name='vars', field=dict, default=dict, include_default=True)
    PlaybookInclude.add_attribute(name='import_playbook', field=str, include_default=True)

# Generated at 2022-06-13 08:48:48.214078
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook._compat import OrderedDict
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    import ansible.constants as C
    pb = PlaybookInclude.load(dict(import_playbook='../collection_test/test_import.yml', tags='foo,bar,baz'), basedir='tests/test_collections')
    assert isinstance(pb, Playbook)
    assert len(pb._entries) == 1
    assert isinstance(pb._entries[0], Play)
    assert pb._entries[0].vars == dict(myvar=dict(val1='foo', val2='bar'))

# Generated at 2022-06-13 08:48:55.949971
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # Import here to avoid a dependency loop
    from ansible.playbook import Playbook

    import json
    import mock

    # Create a mock variable manager
    variable_manager = mock.Mock()

    basedir = os.path.abspath('.')

    # Create and return a mock loader
    def get_loader(return_value, side_effect):
        loader = mock.Mock()
        get_basedir = mock.Mock()
        get_basedir.return_value = basedir
        loader.get_basedir = get_basedir
        loader.path_dwim = lambda path: os.path.join(basedir, path)
        loader.get_real_file = mock.Mock(return_value=return_value)
        loader.template = mock.Mock(side_effect=side_effect)

# Generated at 2022-06-13 08:49:00.784658
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    pass
# array
# list
# indexed list
# directory
# indexed directory
# list of directory
# indexed list of directory
# yaml AST
# python AST
# python AST node
# python list
# python dictionary



# Generated at 2022-06-13 08:49:11.541322
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.parsing.yaml.loader
    from ansible.parsing.dataloader import DataLoader

    dataloader = DataLoader()
    dataloader.set_basedir(VALID_PLAYBOOK_MAIN_FOLDER)

    yaml_loader = ansible.parsing.yaml.loader.AnsibleLoader(False, None, True)

    with open(VALID_PLAYBOOK_FILE, 'r') as stream:
        yaml_data = yaml_loader.load(stream)

    yaml_data = dataloader.load(VALID_PLAYBOOK_FILE, yaml_data)

    # We do not load a real playbook but we used PlaybookInclude to load the file.

# Generated at 2022-06-13 08:49:20.145056
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    include_pb = PlaybookInclude.load({'import_playbook': '../../tests/playbooks/include_test.yaml'}, basedir=basedir)
    assert len(include_pb._entries) == 3
    include_pb2 = PlaybookInclude.load({'import_playbook': '../../tests/playbooks/include_test_vars.yml', 'vars': {'vars_file': '../../tests/playbooks/include_test_vars.json'}}, basedir=basedir)
    assert len(include_pb2._entries) == 3

# Generated at 2022-06-13 08:49:33.754388
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    '''
    This will generate a PlaybookInclude object using the test_fixtures.
    Then the load_data method will be called for the same object with a
    different file name and tags. The result will be saved in the expected_results.
    '''
    from ansible.parsing.dataloader import DataLoader

    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.template import Templar
    from ansible.utils.collection_loader import AnsibleCollectionConfig

    # Load the test fixtures
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=["tests/data"])
    variable_manager.set_inventory(inventory)
   

# Generated at 2022-06-13 08:49:43.930635
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():

    # construct a playbook_include object
    import_playbook = "../../apache/tasks/main.yml"
    vars = {"myvar":"myvalue", "myvar2": "myvalue2"}
    playbook_include = PlaybookInclude()
    playbook_include.import_playbook = import_playbook
    playbook_include.vars = vars

    # load data and construct a playbook object
    playbook = playbook_include.load_data(ds={"include":import_playbook}, basedir="../test/test_playbook_include/")
    assert playbook.__class__.__name__ == "Playbook"

# Generated at 2022-06-13 08:50:02.162492
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    print('> UNIT TEST: test_PlaybookInclude_load_data()')

    print('> Passing argument: \'data\' does not contain a key of \'import_playbook\'')
    ds = 'test_data'
    basedir = None
    variable_manager = None
    loader = None
    try:
        PlaybookInclude.load(ds, basedir, variable_manager, loader)
    except AnsibleAssertionError as e:
        print('> Expected AnsibleAssertionError: %s' % str(e))
        print('> PASSED')
    else:
        print('> ERROR: Expected AnsibleAssertionError')
        return

    print('> Passing argument: \'data\' is an dict but not an AnsibleMapping')
    ds = dict()

# Generated at 2022-06-13 08:50:13.631428
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play import Play
    from ansible.playbook.role import Role

    # Unit test for method load_data of class PlaybookInclude with load_file = "tst_pb_include_1.yaml"
    pb = PlaybookInclude.load({
        'import_playbook': "tst_pb_include_1.yaml"
    }, "/tmp")
    assert isinstance(pb, Play)
    assert pb.name == "First play"
    assert pb.vars == {
        'foo': 'bar',
        'lorem': 'ipsum'
    }
    assert len(pb.roles) == 1
    assert isinstance(pb.roles[0], Role)
    assert pb.roles[0].get_name() == "test"

    # Unit

# Generated at 2022-06-13 08:50:25.683396
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # Delayed import
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play

    class FakeLoader:
        class FakeInventory:
            def __init__(self):
                self.hosts = {}
        def get_basedir(self):
            return 'tests/test/test/test'
        def get_inventory(self):
            return FakeLoader.FakeInventory()

    # Test when no parameters are passed to import_playbook:
    pbi = PlaybookInclude()
    ds = {'import_playbook': 'foo.yml'}
    try:
        pbi.load_data(ds, '', loader=FakeLoader())
    except AnsibleParserError as e:
        assert False, "Should not have raised an exception"

    # Test when a string is passed to import

# Generated at 2022-06-13 08:50:27.238190
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # TODO: implement
    return

# Generated at 2022-06-13 08:50:38.579943
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import mock
    import os

    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.playbook.role import Role
    from ansible.template import Templar

    fake_loader = mock.Mock()

    ds = AnsibleLoader(None, True, False).load('''
    - import_playbook:
        import_playbook: include_playbook.yml
        vars:
          var1: value1
          var2:
            var2_1: value2_1
    ''')

    # test load
    task = PlaybookInclude.load(ds[0], 'test_dir')
    assert isinstance(task, PlaybookInclude)

    # test load

# Generated at 2022-06-13 08:50:49.001796
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.vars import VariableManager
    from ansible.parsing.yaml.loader import AnsibleLoader

    # ds = dict(dict(import_playbook='testinclude.yml'))
    yamlstr = '''
- hosts: localhost
  gather_facts: no
  roles:
    - name: testrole
  tasks:
    - import_playbook: testinclude.yml'''
    ds = AnsibleLoader(yamlstr, file_name=None).get_single_data()
    ds = d

# Generated at 2022-06-13 08:51:02.135931
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    collection_name = 'example.collection'
    collection_config = AnsibleCollectionConfig(collection_name)
    test_playbook = [{
        'hosts': 'localhost',
        'tasks': [
            {
                'import_playbook': 'test_playbook2.yml',
                'vars': {
                    'x': 'hello',
                }
            }
        ]
    }]


# Generated at 2022-06-13 08:51:14.713202
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    # pylint: disable=redefined-outer-name
    """
    Test load_data method of class PlaybookInclude
    """
    # pylint: disable=unused-argument
    def mock_load_data(self, ds, basedir, variable_manager=None, loader=None):
        """
        Mock PlaybookInclude.load_data()
        """
        ret = PlaybookInclude()
        ret.import_playbook = 'filename'
        ret.vars = {'fake': 'fake', 'more_fake': 'more_fake'}
        return ret

    def mock_load(self, data, basedir, variable_manager=None, loader=None):
        """
        Mock PlaybookInclude.load()
        """
        ret = PlaybookInclude()
        ret.load_data = mock

# Generated at 2022-06-13 08:51:21.656955
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import ansible.playbook.play_context
    import ansible.playbook.play
    import ansible.playbook.condition
    loader=ansible.parsing.dataloader.DataLoader()
    variable_manager=ansible.vars.manager.VariableManager()
    context=ansible.playbook.play_context.PlayContext()
    p = PlaybookInclude()
    result = p.load_data({"include": "playbook.yml"}, ".", variable_manager, loader)
    print(result)

# Generated at 2022-06-13 08:51:30.505482
# Unit test for method load_data of class PlaybookInclude
def test_PlaybookInclude_load_data():
    import os
    import sys
    import shutil
    import tempfile
    import ansible.playbook.playbook as pb

    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # create a temporary directory for our 'test' magic
    test_dir = os.path.join(tempfile.gettempdir(), 'ansible_test_playbook_include_load_data')

    # create the test files
    test_data = '''
    - hosts: all
      tasks: []
    '''
    test_file = os.path.join(test_dir, 'test2.yml')
    with open(test_file, "w") as f:
        f.write(test_data)


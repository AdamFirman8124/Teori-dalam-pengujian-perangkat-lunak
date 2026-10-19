

# Generated at 2022-06-13 08:31:25.289748
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    print("Method compile_roles_handlers of class Play")
    print("No Test for this method")

# Generated at 2022-06-13 08:31:30.969014
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():

    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.role.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.template import Templar

    # append fake handlers
    tasks = [
        Handler().load(dict(
            name='test handler',
            tags=['test', 'always'],
            tasks=[
                Task().load(dict(action=dict(module='debug', args=dict(msg='{{ "handler" }}')))),
            ],
        )),
    ]
    # render all tasks
    templar = Templar(loader=None)
    for task in tasks:
        task.post_validate(templar=templar)
    # check compiled blocks
    blocks = Play().compile

# Generated at 2022-06-13 08:31:36.030429
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    import string
    import random
    import tempfile
    # Random chars
    chars = string.ascii_uppercase + string.digits
    # Random string
    random_str = ''.join(random.choice(chars) for _ in range(10))
    # Prepare data
    data = {'hosts': random_str}
    # Instantiate Play
    p = Play()
    # Preprocess data
    new_data = p.preprocess_data(data)
    assert new_data['hosts'] == random_str
    # Test that new element is added 
    assert 'remote_user' in new_data
    assert new_data['remote_user'] == random_str
    # Test that old element is removed
    assert 'user' not in new_data
    # Random string

# Generated at 2022-06-13 08:31:48.614177
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    # Setup test
    # Create a play object
    play = Play()
    # Initialize the data

# Generated at 2022-06-13 08:31:52.451127
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    play_ds = dict(
        gather_facts=True,
        force_handlers=True,
        roles=[],
        pre_tasks=[
            dict(include=None),
            dict(include_role=None)
        ]
    )
    
    play = Play()
    play.preprocess_data(play_ds)

    assert play.gather_facts == True
    assert play.force_handlers == True
    assert play.roles == []
    assert len(play.pre_tasks) == 2
    assert type(play.pre_tasks[0]) == Include
    assert type(play.pre_tasks[1]) == IncludeRole


# Generated at 2022-06-13 08:31:59.604956
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play = Play()
    host_list = ['host1', 'host2', 'host3']
    connection_type = 'ssh'
    gather_facts = 'no'
    vars = {'ansible_connection': 'ssh'}
    task_list = ['tasks', 'pre-tasks', 'post-tasks', 'handlers', 'roles']
    data = dict()
    data['name'] = 'play1'
    data['connection'] = connection_type

    play_load = Play.load(data, variable_manager=None, loader=None, vars=None)
    assert play_load.name == 'play1'


# Generated at 2022-06-13 08:32:05.542870
# Unit test for method deserialize of class Play
def test_Play_deserialize():
	obj = Play()
	data = {}
	obj.deserialize(data)
	assert obj._included_path == None
	assert obj._action_groups == {}
	assert obj._group_actions == {}


# Generated at 2022-06-13 08:32:08.895281
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play._tasks = []
    play.tasks
    play.get_tasks()
    pass

# Generated at 2022-06-13 08:32:21.357584
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    p = Play()

# Generated at 2022-06-13 08:32:25.625561
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    from ansible.constants import DEFAULT_HANDLER_LAYERS
    play = Play().load({
        'roles': [
            {
                'name': 'role_name',
            },
        ],
    }, variable_manager=None, loader=None)
    play.ROLE_CACH

# Generated at 2022-06-13 08:32:34.571162
# Unit test for method get_name of class Play
def test_Play_get_name():
    Play = Play()
    Play = Play.get_name()
    assert Play


# Generated at 2022-06-13 08:32:42.705251
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # Create play object
    p = Play()
    # Create role object
    r = Role()
    # Create handler object
    handler = Handler()
    # Create task object
    task = Task()
    # Create list of handlers
    handlers = []
    handlers.append(handler)
    # Add handlers, tasks, roles and blocks to the lists of the play
    p.handlers = handlers
    p.tasks = [task]
    p.roles = [r]
    p._compile_roles()

    # Assert that compile_roles_handlers returns a block list
    assert isinstance(p.compile_roles_handlers(), list)


# Generated at 2022-06-13 08:32:53.204120
# Unit test for method get_name of class Play
def test_Play_get_name():
    from ansiblelint.rules.TestDictKeyFormatRule import TestDictKeyFormatRule
    from ansiblelint.runner import Runner
    from ansiblelint.rules import RulesCollection
    raw = dedent('''
    - name: This is a good play name
      hosts: localhost
      tasks:
      - name: This is a task name
        debug: msg="{{ test }}"
    ''')
    plays, play_ds = get_plays(raw)
    play = plays[0]
    hosts = play_ds[0]['hosts']
    user = play_ds[0]['remote_user']
    tasks = play_ds[0]['tasks']
    roles = play_ds[0]['roles']
    rules = RulesCollection()
    rules.register(TestDictKeyFormatRule())

# Generated at 2022-06-13 08:33:01.646384
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # step 1: build Play object
    # build variable_manager
    variable_manager = VariableManager()
    
    # build loader
    loader = DataLoader()
    
    # build inventory
    inventory = Inventory(loader=loader, variable_manager=variable_manager)
    inventory.add_group("group")
    inventory.add_host("127.0.0.1", "group")
    
    # build options
    options = Options([])
    options.connection = 'local'
    options.module_path = ['modules']
    
    # build play object

# Generated at 2022-06-13 08:33:04.666219
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    play.compile_roles_handlers()

# vim: set et ts=4 sw=4

# Generated at 2022-06-13 08:33:10.269208
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    p = Play()
    p.vars_files = 'test file'
    assert p.get_vars_files() == ['test file']
    
    p.vars_files = ['test file1', 'test file2']
    assert p.get_vars_files() == ['test file1', 'test file2']



# Generated at 2022-06-13 08:33:11.595309
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    pass

# Generated at 2022-06-13 08:33:27.442221
# Unit test for method compile_roles_handlers of class Play

# Generated at 2022-06-13 08:33:30.324830
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    p = Play()
    result = p.compile_roles_handlers()
    assert result == [], "Test #1 failed: Expected result to be [], got {}".format(result)

# Generated at 2022-06-13 08:33:37.539573
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    vars = {"key": "value"}
    play.vars = vars
    vars_files = [{"key": "value"}]
    play.vars_files = vars_files
    assert vars == play.vars
    assert vars_files == play.get_vars_files()



# Generated at 2022-06-13 08:33:51.942773
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    instance = Play()
    value1 = dict()
    value2 = dict()
    value3 = dict()
    value4 = dict()
    value5 = dict()
    value6 = dict()
    value7 = dict()
    value8 = dict()
    value9 = dict()
    value10 = dict()
    value11 = dict()
    value12 = dict()
    value13 = dict()
    value14 = dict()
    value15 = dict()
    value16 = dict()
    value17 = dict()
    value18 = dict()
    value19 = dict()
    value20 = dict()
    value21 = dict()
    value22 = dict()
    value23 = dict()
    value24 = dict()
    value25 = dict()
    value26 = dict()
    value27 = dict()

# Generated at 2022-06-13 08:33:54.211545
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
   play = Play()

# Generated at 2022-06-13 08:34:05.425190
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # Test Load play
    play_path = os.path.join(os.getcwd(), 'test', 'test_data', 'play_get_tasks.yml')
    ds = DataLoader().load_from_file(play_path)
    play_ds = ds[0]

    play = Play()
    play.load_data(data=play_ds, variable_manager=VariableManager())
    assert isinstance(play, Play)

    # Test get_tasks method
    assert 42 == len(play.get_tasks())
    '''
    task_list = play.get_tasks()
    for task in task_list:
        print(type(task))
        print(task.action)
    '''

# Generated at 2022-06-13 08:34:14.571267
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    data = {'roles': [{'role': 'test'}], 'name': 'test', 'hosts': 'localhost', 'tasks': [{'action': 'debug', 'name': 'debug task'}]}
    p = Play()
    p.deserialize(data)
    assert p.name == 'test'
    assert p.hosts == 'localhost'
    assert p.get_roles()[0].get_name() == 'test'
    assert p.tasks[0].action == 'debug'
    assert p.tasks[0].name == 'debug task'

# Generated at 2022-06-13 08:34:24.133548
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play.tasks = Block(
        [
            Task(dict(action='setup')),
            Task(dict(action='run')),
        ],
        [
            Task(dict(action='rescue'))
        ],
        [
            Task(dict(action='always')),
        ]
    )
    assert play.get_tasks() == [
        Task(dict(action='setup')),
        Task(dict(action='run')),
        Task(dict(action='rescue')),
        Task(dict(action='always')),
    ]

# Generated at 2022-06-13 08:34:36.862878
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    test_obj = Play()

# Generated at 2022-06-13 08:34:39.649689
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play_instance = Play()
    assert play_instance.deserialize(data={'roles': list}) == None
    assert play_instance.serialize() == dict(roles=list)


# Generated at 2022-06-13 08:34:52.914318
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    from ansible.vars.unsafe_proxy import wrap_var
    from ansible.playbook.play_context import PlayContext

    fake_variable_manager = DictDataManager()
    fake_loader = DictDataLoader({})

# Generated at 2022-06-13 08:35:04.636884
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # test a simple play
    play_ds = dict(
        name="Ansible Play",
        hosts="all",
        gather_facts="no",
        roles=["role1"],
        tasks=[
            dict(action=dict(module="shell", args="id"), register="shell_out"),
            dict(action=dict(module="debug", var="shell_out.stdout_lines")),
        ]
    )
    
    # instantiate play and role
    play = Play().load(play_ds)
    role = Role().load(dict(name="role1",
                            tasks=[
                                dict(action=dict(module="shell", args="id"), register="shell_out1"),
                                dict(action=dict(module="debug", var="shell_out1.stdout_lines")),
                            ]))


# Generated at 2022-06-13 08:35:12.014473
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play_obj = Play()
    block_list = play_obj._load_handlers('attr', play_obj._ds['handlers'])
    block_list += play_obj._load_tasks('attr', play_obj._ds['tasks'])
    block_list += play_obj._load_pre_tasks('attr', play_obj._ds['pre_tasks'])
    block_list += play_obj._load_post_tasks('attr', play_obj._ds['post_tasks'])
    roles = play_obj._load_roles('attr', play_obj._ds['roles'])

    assert isinstance(roles, list)
    assert isinstance(roles[0], Role)
    assert hasattr(roles[0], '_role_path')

# Generated at 2022-06-13 08:35:28.661618
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    import ansible.playbook.play
    import ansible.playbook.play_context
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader
    p = Play()
    p._loader = DataLoader()
    p._tasks = []
    p.hosts = "host1"
    p.name = "test_play"
    p.vars = {}
    p.vars["a"] = 1
    p.vars["b"] = 2
    p.post_validate()

# Generated at 2022-06-13 08:35:31.894947
# Unit test for method serialize of class Play
def test_Play_serialize():
    p = Play()
    def test_method(self):
        return True
    p._serialize = test_method
    assert p.serialize() == True


# Generated at 2022-06-13 08:35:34.032610
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play.load({})
    assert play.compile_roles_handlers() == []



# Generated at 2022-06-13 08:35:39.841713
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    play.vars_files = 'a'
    assert play.get_vars_files()==['a']
    play.vars_files = None
    assert play.get_vars_files()==[]
    play.vars_files = []
    assert play.get_vars_files()==[]


# Generated at 2022-06-13 08:35:51.329422
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    assert play.get_vars_files() == []
    play = Play(vars_files="vars_files")
    assert play.get_vars_files() == ["vars_files"]
    play = Play(vars_files=["vars_files"])
    assert play.get_vars_files() == ["vars_files"]
    play = Play(vars_files=["vars_files_1", "vars_files_2"])
    assert play.get_vars_files() == ["vars_files_1", "vars_files_2"]

# Generated at 2022-06-13 08:36:02.589578
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    from units.mock.loader import DictDataLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager


# Generated at 2022-06-13 08:36:07.299337
# Unit test for constructor of class Play
def test_Play():
    play = Play.load(dict(name='test', hosts=['all'], gather_facts='yes'))
    play.vars = dict(a=1)
    play.roles = [dict(role='Foo', become=True, become_user='root')]
    assert play.name == 'test'
    assert play.hosts == ['all']
    assert play.gather_facts == 'yes'
    assert play.vars['a'] == 1
    assert len(play.roles) == 1
    assert play.roles[0].role == 'Foo'
    assert play.roles[0].name == 'Foo'
    assert play.roles[0].become == True
    assert play.roles[0].become_user == 'root'


# Generated at 2022-06-13 08:36:10.405523
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    p = mock_unittest_handler.create_play()
    result = p.compile_roles_handlers()
    assert len(result) == 1
    assert isinstance(result[0], Block)


# Generated at 2022-06-13 08:36:19.582125
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()

    tasks = [ "tasks1" , "tasks2" , "tasks3" , "tasks4"]
    pre_tasks = [ "pre_tasks1" , "tasks1" , "pre_tasks1"]
    post_tasks = [ "post_tasks1" , "tasks2" , "post_tasks1"]

    setattr(play,"tasks",tasks)
    setattr(play,"post_tasks",post_tasks)
    setattr(play,"pre_tasks",pre_tasks)
    r = play.get_tasks()
    assert r == pre_tasks + tasks + post_tasks
    print("Tested Unit Method Play.get_tasks Successfully")


# Generated at 2022-06-13 08:36:26.684848
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    vars_files = [
        "{{ playbook_dir }}/../group_vars/gluster/clients.yml",
        "{{ playbook_dir }}/../group_vars/gluster/servers.yml",
        "/etc/ansible/group_vars/test.yml"
    ]
    play = Play()
    play.vars_files = vars_files
    assert play.get_vars_files() == vars_files



# Generated at 2022-06-13 08:36:41.529665
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
  # Test with non dictionary data structure
  p = Play()
  data = []
  try:
    p.preprocess_data(ds=data)
  except AssertionError as e:
    if (str(e) != 'while preprocessing data ([])'
        ', ds should be a dict but was a list'):
      raise
  
  # Test with correct data structure
  data = {
    'user': 'bob',
  }
  p.preprocess_data(ds=data)
  del p


# Generated at 2022-06-13 08:36:51.957940
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    import os
    import tempfile
    from ansible.plugins import connection, module_loader
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.inventory import Host, Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.module_utils.common._collections_compat import Mapping
    import ansible.constants as C
    import ansible.utils.plugin_docs as plugin_docs
    from ansible.module_utils.common.text.converters import to_bytes, to_unicode
    from ansible.utils.display import Display

# Generated at 2022-06-13 08:36:52.995747
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    assert True == False

# Generated at 2022-06-13 08:36:55.750668
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    assert play.compile_roles_handlers() == []

# Generated at 2022-06-13 08:37:05.260688
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    # Only use the 'hosts' field for the Play data structure
    # For this simple test, we can just make it a list of roles
    # This should be converted back to a list of strings
    ds = {
        'hosts': [
            'role1',
            'role2',
            'role3'
        ]
    }
    # Create a play object
    p = Play()
    # Call method preprocess_data with our ds
    p.preprocess_data(ds)
    # This should have converted the 'hosts' value back to a list of strings
    assert ds['hosts'] == ['role1', 'role2', 'role3']


# Generated at 2022-06-13 08:37:08.253762
# Unit test for method compile_roles_handlers of class Play

# Generated at 2022-06-13 08:37:10.110015
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    p = Play()
    data = {'a': 1}
    p.preprocess_data(data)

# Generated at 2022-06-13 08:37:21.671656
# Unit test for method get_name of class Play
def test_Play_get_name():
    import os
    import sys
    import types
    import unittest
    import copy
    import shutil
    import tempfile
    from io import StringIO
    from unittest.mock import patch

    from ansible.module_utils.six import PY3, iteritems
    from ansible.module_utils._text import to_bytes, to_text
    if PY3:
        from io import StringIO
        StringIO = StringIO
    else:
        from StringIO import StringIO

    from collections import namedtuple
    import ansible.constants as C
    import ansible.config.manager

    from ansible import context
    from ansible.errors import AnsibleError
    import ansible.executor.task_queue_manager
    import ansible.inventory
    from ansible.inventory.host import Host

# Generated at 2022-06-13 08:37:33.092724
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    '''
    Play: test preprocess_data
    '''
    # Test 1: regular play
    p = Play()

# Generated at 2022-06-13 08:37:38.979493
# Unit test for method get_name of class Play
def test_Play_get_name():
    p = Play()
    p.name = 'test play'
    assert p.get_name() == 'test play'
    p.name = None
    p.hosts = 'test hosts'
    assert p.get_name() == 'test hosts'
    p.hosts = None
    assert p.get_name() == ''


# Generated at 2022-06-13 08:38:00.039901
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    #provide value of role_path_list and init the object of class Play
    class Test_Play_compile_roles_handlers:
        '''
           Class to test the methods in the class Play.
        '''
        play_obj = Play()
        play_obj.ROLE_CACHE = {}
        play_obj._included_path = None
        play_obj._action_groups = {}
        play_obj._group_actions = {}
        #execute compile_roles_handlers
        play_obj.compile_roles_handlers()

    # expected result
    assert_equal(Test_Play_compile_roles_handlers.play_obj.ROLE_CACHE, {})


# Generated at 2022-06-13 08:38:02.414560
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    play = Play()
    play._ds = {'user':'root'}
    play.preprocess_data(ds=play._ds)

    # assert 'user' has been replaced by 'remote_user'
    assert 'user' not in play._ds.keys()
    assert 'remote_user' in play._ds.keys()



# Generated at 2022-06-13 08:38:13.659867
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    try:
        import mock
    except ImportError:
        # mock not installed (python2.6)
        unittest.skip("mock not installed, skipping")

    # Silence pyflakes
    mock

    # Setup mock of object
    mock_loader = mock.MagicMock()
    mock_var_mgr = mock.MagicMock()
    p = Play()
    p._loader = mock_loader
    p._variable_manager = mock_var_mgr

    # Create test data
    dummy_dict = dict()

    # Call method to test
    p.preprocess_data(dummy_dict)

    # Ensure that method was called with the appropriate parameters
    self.assertEqual(mock_loader.list_templates.call_count, 1)
    mock_loader.list_templates.assert_has_

# Generated at 2022-06-13 08:38:18.448113
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play.pre_tasks = [1, 2, 3]
    play.tasks = [4, 5, 6]
    play.post_tasks = [7, 8, 9]

    assert play.get_tasks() == [
        1, 2, 3, 4, 5, 6, 7, 8, 9
    ]

# Generated at 2022-06-13 08:38:25.923710
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    '''
    Test for method get_vars_files of class Play
    '''
    print("Start Play.get_vars_files")

    try:
        import ansible
    except ImportError:
        print("Cannot import ansible")

    # Create an instance of Play
    testObject = Play()
    print("Instantiated a Play")

    # Create test data
    data = {'strategy': 'linear', 'hosts': 'test', 'roles': 'test', 'tasks': 'test', 'handlers': 'test'}
    test_dict = dict(data)

    # Create a VariableManager
    variable_manager = VariableManager()

    # Create a loader
    loader = DataLoader()

    # Load the data
    testObject.load_data(test_dict, variable_manager, loader)

# Generated at 2022-06-13 08:38:40.610492
# Unit test for method serialize of class Play
def test_Play_serialize():
    p = Play()
    p.name = 'test_play_serialize'
    p.connection = 'network_cli'
    p.hosts = 'localhost'
    p.gather_facts = 'no'
    p.serial = 1
    p.vars = {'var1': {'key1': 'value1'}}

# Generated at 2022-06-13 08:38:55.947223
# Unit test for method serialize of class Play

# Generated at 2022-06-13 08:38:58.074751
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    """ test the method get_tasks of class Play """
    # play = Play(dict(playbook=dict()))
    # assert play.get_tasks() == "get_tasks"
    pass

# Generated at 2022-06-13 08:39:08.437263
# Unit test for method get_name of class Play
def test_Play_get_name():
    def return_true():
        return True
    play_name = "play1"
    p = Play(name=play_name)
    assert p.name == play_name
    assert p.get_name() and p.get_name() == play_name
    p.only_tags = frozenset(["tag1"])
    assert p.get_name() == "tag1"
    p.only_tags = frozenset(["tag1","tag2"])
    assert p.get_name() == "tag1,tag2"
    p.skip_tags = frozenset(["skip_tag1"])
    p.only_tags = frozenset(["tag1","tag2"])
    assert p.get_name() == "tag1,tag2:skip_tag1"

# Generated at 2022-06-13 08:39:13.583788
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    play.vars_files=[]
    assert play.get_vars_files() == []
    play.vars_files=None
    assert play.get_vars_files() == []
    play.vars_files=[1,2]
    assert play.get_vars_files() == [1,2]

# Generated at 2022-06-13 08:39:35.682492
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    vars_files1 = []
    vars_files2 = ['host_vars/host_vars_file.yml', 'group_vars/group_vars_file.yml', 'host_vars/host_vars_file2.yml', 'group_vars/group_vars_file2.yml']
    play = Play()
    play.vars_files = vars_files1
    assert play.get_vars_files() == []
    play.vars_files = vars_files2

# Generated at 2022-06-13 08:39:38.060325
# Unit test for method serialize of class Play
def test_Play_serialize():
    # Test parameters:
    # Play.serialize()
    
    
    
    
    
    
    
    
    
    
    
    
    # TODO: Implement unit test for method serialize of class Play

    pass


# Generated at 2022-06-13 08:39:49.988442
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # Case: Default
    # Case: Default vars_files is None
    # Case: vars_files is str
    # Case: vars_files is list
    vars_files = None
    play = Play()
    play.vars_files = vars_files
    assert play.get_vars_files() == []

    vars_files = "/etc/ansible/var_files/file1.yml"
    play = Play()
    play.vars_files = vars_files
    assert play.get_vars_files() == [vars_files]

    vars_files = ["/etc/ansible/var_files/file1.yml", "/etc/ansible/var_files/file2.yml"]
    play = Play()
    play.vars_files = vars_

# Generated at 2022-06-13 08:40:00.991937
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    play.vars_files = "/Users/zhaoxiang/Git/ansible-dexter/test/unit/unittest_data/vars_files"
    assert play.get_vars_files() == ['/Users/zhaoxiang/Git/ansible-dexter/test/unit/unittest_data/vars_files']
    # play.vars_files = "srr"
    # assert play.get_vars_files() == ['srr']
    play.vars_files = ["srr", "srr1"]
    assert play.get_vars_files() == ["srr", 'srr1']
    play = Play()
    assert play.get_vars_files() == []

# Generated at 2022-06-13 08:40:08.682967
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
  class AnsibleAssertionError(Exception):
    pass

  class AnsibleParserError(Exception):
    pass

  class AssertionError(Exception):
    pass

  class BadHost(Exception):
    pass

  def to_native(arg):
    try:
      value = arg.__str__()
    except AttributeError:
      value = str(arg)
    return value

  class Play(object):
    _validate_hosts = _validate_hosts

    _roles = None

    _vars_files = None

    _force_handlers = None

    _post_tasks = None

    _pre_tasks = None

    _hosts = []

    _included_conditional = None

    _action_groups = None

    _group_actions = None


# Generated at 2022-06-13 08:40:16.856566
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    play_ds = dict(
        name="Test Play",
        hosts="localhost",
        vars=dict(
            ansible_connection="local"
        ),
        user="root",
        roles=dict(
            role_name="foo"
        )
    )

    p = Play().load(data=play_ds, variable_manager=VariableManager(), loader=None)

    preprocessed_ds = p.preprocess_data(play_ds)
    assert "remote_user" in preprocessed_ds
    assert "user" not in preprocessed_ds



# Generated at 2022-06-13 08:40:20.696712
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    play.tasks = [Playbook.load_file('./test/support/playbooks/test_play_tasks.yml')]
    assert play.tasks, 'Tasks cannot be empty'

# Generated at 2022-06-13 08:40:35.413013
# Unit test for method get_name of class Play
def test_Play_get_name():
    """Test get_name method of Play class"""
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    context._init_global_context(
        load_plugins=False,
    )
    loader = DictDataLoader({
        "test.yml": """
        - hosts: all
          tasks:
            - debug:
                msg: Hello World!
        """
    })
    inventory = InventoryManager(loader=loader, sources=[""])
    variable

# Generated at 2022-06-13 08:40:41.736723
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    vars_files = ['./test_vars_files.yml']
    play.vars_files = vars_files
    assert play.get_vars_files() == vars_files
    play.vars_files = None
    assert play.get_vars_files() == []
    play.vars_files = './test_vars_files.yml'
    assert play.get_vars_files() == ['./test_vars_files.yml']


# Generated at 2022-06-13 08:40:54.257866
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    my_play = Play()
    my_play.vars_files = None
    assert my_play.get_vars_files() == [],"Expected: [], Actual: {!r}".format(my_play.get_vars_files())

    my_play = Play()
    my_play.vars_files =  "test"
    assert my_play.get_vars_files() == ["test"],"Expected: ['test'], Actual: {!r}".format(my_play.get_vars_files())

    my_play = Play()
    my_play.vars_files =  ["test"]
    assert my_play.get_vars_files() == ["test"],"Expected: ['test'], Actual: {!r}".format(my_play.get_vars_files())
#
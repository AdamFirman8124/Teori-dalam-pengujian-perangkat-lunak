

# Generated at 2022-06-13 08:31:19.453172
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play = Play()
    play.deserialize({'_uuid': '1'})
    assert play._uuid == '1'

# Generated at 2022-06-13 08:31:27.565276
# Unit test for constructor of class Play
def test_Play():
    ds = dict(
        name="Test Play",
        hosts=dict(all="test12"),
        tasks=[dict(name="Test Task", action=dict(module="test"))],
    )

    p = Play()
    p.load_data(ds, variable_manager={}, loader=DictDataLoader())

    assert p.name == "Test Play"
    assert p.get_name() == "test12"

    assert isinstance(p.tasks[0], Task)
    assert p.tasks[0].name == "Test Task"



# Generated at 2022-06-13 08:31:32.434456
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    p = Play()
    assert p.get_vars_files() == []
    p.vars_files = None
    assert p.get_vars_files() == []
    p.vars_files = 'test'
    assert p.get_vars_files() == ['test']
    p.vars_files = ['test1', 'test2']
    assert p.get_vars_files() == ['test1', 'test2']

test_Play_get_vars_files()

# Generated at 2022-06-13 08:31:45.586261
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    class Mockobjects:
        def __init__(self):
            self.ansible_playbook_python = "/root/ansible/hacking/test-module -m /root/ansible/lib/ansible/modules/cloud/amazon/s3_sync.py -a"
            self.ansible_module_name = "s3_sync"
            self.ansible_module_args = ""
            self.ansible_version = dict(
                full='2.9.9',
                major=2,
                minor=9,
                revision=9,
                string='2.9.9',
            )


# Generated at 2022-06-13 08:31:54.689114
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    play = Play()

    # method _load_roles is defined in Play. It's a dynamic attribute.
    # So it will not exist until it's accessed.
    if not hasattr(play, '_load_roles'):
        setattr(play, '_load_roles', lambda attr, ds: ds)

    # Replace _load_roles with a fake one only return a list of dicts
    setattr(play, '_load_roles', lambda attr, ds: [{'name': 'role_name', 'foo': 'bar'}, {'name': 'role_name_1', 'bar': 'foo'}])

    ds = play.preprocess_data({'hosts': 'all', 'user': 'foo'})
    assert ds['remote_user'] == 'foo'

# Generated at 2022-06-13 08:31:56.476389
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    role_handler_block = play.compile_roles_handlers()
    assert role_handler_block == []

# Generated at 2022-06-13 08:32:01.920060
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    my_Play = Play()
    my_Play.vars_files = ['/path/to/first/file', '/path/to/second/file']
    assert my_Play.get_vars_files() == ['/path/to/first/file', '/path/to/second/file']

# Generated at 2022-06-13 08:32:16.696528
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    import yaml
    variable_manager = VariableManager()
    loader = DataLoader()

    data = '''
    - name: check headers
      action:
        local_action: >
          uri
          url={{ item.url }}
          return_content=yes
        register: res
        with_items:
          - { url: 'http://google.com/' }
          - { url: 'http://yahoo.com/' }
      loop_control:
        loop_var: item
    '''
    ds = yaml.load(data)
    p = Play()
    p.load_data(ds, variable_manager=variable_manager, loader=loader)
    assert p.ROLE_CACHE == {}
    assert p.get_vars_files() == []
    assert p.only_tags == set

# Generated at 2022-06-13 08:32:18.457378
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    play.compile_roles_handlers()


# Generated at 2022-06-13 08:32:25.079036
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    assert p.get_tasks() == []

    class Block1:
        def __init__(self, tasks):
            self.block = tasks

    class Block2:
        def __init__(self, tasks):
            self.rescue = tasks

    class Block3:
        def __init__(self, tasks):
            self.always = tasks

    p.tasks = [Block1([1, 2, 3]), Block2([4, 5, 6]), Block3([7, 8, 9])]
    assert p.get_tasks() == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    p.pre_tasks = [Block1([1, 2, 3]), Block2([4, 5, 6]), Block3([7, 8, 9])]

# Generated at 2022-06-13 08:32:36.760524
# Unit test for method get_name of class Play
def test_Play_get_name():
    # Method call to get_name of class Play
    try:
        p = Play()
        p.hosts = ['host1', 'host2']
        p.get_name()
        assert True
    except:
        assert False, "Should not raise exception"

# Generated at 2022-06-13 08:32:45.091018
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task.include import IncludeTask
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler


# Generated at 2022-06-13 08:32:55.065712
# Unit test for method serialize of class Play
def test_Play_serialize():
    data = {}
    data['name'] = 'test'
    data['hosts'] = 'test'
    data['connection'] = 'test'
    data['gather_facts'] = False
    data['gather_subset'] = []
    data['gather_timeout'] = 10
    data['max_fail_percentage'] = 0
    data['any_errors_fatal'] = False
    data['serial'] = 1
    data['force_handlers'] = False
    data['roles'] = []
    data['tasks'] = []
    data['pre_tasks'] = []
    data['post_tasks'] = []
    data['vars'] = {}
    data['vars_prompt'] = {}
    data['vars_files'] = []
    data['handlers'] = []

# Generated at 2022-06-13 08:33:00.988483
# Unit test for method get_name of class Play
def test_Play_get_name():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    loader = DataLoader()
    variable_manager = VariableManager()
    p = Play()
    p.vars = {}
    p.post_validate(dict(name="Test name", hosts="test_hosts"), variable_manager)
    assert p.get_name() == "Test name"
    p.post_validate(dict(hosts="test_hosts"), variable_manager)
    assert p.get_name() == "test_hosts"

# Generated at 2022-06-13 08:33:12.294066
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    def run_test(roles_list, mock_role_compiled_handlers_list, expected_handlers, expected_results):
        test_play = Play()
        test_play._roles = roles_list
        result = test_play.compile_roles_handlers() 
        assert result == expected_handlers
        for role, handler in zip(roles_list, mock_role_compiled_handlers_list):
            role.get_handler_blocks.assert_called_once_with(play=test_play)
            role.get_handler_blocks.assert_called_with(play=test_play)
            assert result == expected_results

    group_name = 'test_group'
    test_handler1 = Mock()
    test_handlers_list1 = [test_handler1]
    test_

# Generated at 2022-06-13 08:33:16.358298
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    play.vars_files = ["vars_files"]
    assert play.get_vars_files() == ["vars_files"]

# Generated at 2022-06-13 08:33:21.929498
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    data_sub = {"block": [{"block": [], "rescue": [], "always": []}, {"name": "task1", "block": []}]}
    data_sub_sub = {"block": [{"name": "subsubtask1", "block": []}, {"name": "subsubtask2", "block": []}]}
    data_sub["block"][0]["block"] = [data_sub_sub["block"][0]]
    data_sub["block"][1]["block"] = [data_sub_sub["block"][1]]

    data_task1 = {"name": "task1"}

    data_task2 = {"name": "task2", "block": [{"name": "subtask1","block": []}]}


# Generated at 2022-06-13 08:33:30.823963
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    '''
    [default]
    hosts=remote_host
    '''
    # TODO: init with play_source_path = './play'
    p = Play().load(play_source_path = './play1')
    p.get_vars_files()

    '''
    [default]
    hosts=remote_host
    
    vars_files:
     - ./somewhere/vars.yml
    '''
    # TODO: init with play_source_path = './play'
    p = Play().load(play_source_path = './play2')
    p.get_vars_files()


# Generated at 2022-06-13 08:33:40.169383
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    p=Play()
    p.vars_files=None
    assert p.vars_files is None
    p.vars_files=[]
    assert isinstance(p.get_vars_files(), list)
    p=Play()
    p.vars_files="vars/test.yaml"
    assert isinstance(p.get_vars_files(), list)
    assert isinstance(p.get_vars_files()[0], str)



# Generated at 2022-06-13 08:33:44.445011
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    v = Play()
    v.pre_tasks.append('a')
    v.tasks.append('b')
    v.post_tasks.append('c')
    assert_equal(v.get_tasks(),['a','b','c'])


# Generated at 2022-06-13 08:34:18.292377
# Unit test for method get_name of class Play
def test_Play_get_name():
    p = Play()
    assert p.get_name() == ''
    p.name = 'test'
    assert p.get_name() == 'test'
    p.name = None
    # test if get_name works correctly with a list of hosts
    p.hosts = ['localhost', '127.0.0.1']
    assert p.get_name() == 'localhost,127.0.0.1'
    p.hosts = 'localhost,127.0.0.1'
    assert p.get_name() == 'localhost,127.0.0.1'
    p.hosts = 'localhost'
    assert p.get_name() == 'localhost'
    p.hosts = None
    assert p.get_name() == ''


# Generated at 2022-06-13 08:34:22.883394
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    assert Play().get_vars_files() == []
    assert Play(vars_files=1).get_vars_files() == [1]
    assert Play(vars_files=[1]).get_vars_files() == [1]



# Generated at 2022-06-13 08:34:28.132840
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    obj = Play()
    # Test if the vars_files are set to normal variables.
    obj.vars_files = None
    test_result = obj.get_vars_files()
    assert test_result == []
    # Test if the vars_files are set to a list of variables.
    obj.vars_files = ['vars']
    test_result = obj.get_vars_files()
    assert test_result == ['vars']

# Generated at 2022-06-13 08:34:36.366815
# Unit test for method get_name of class Play
def test_Play_get_name():
    p = Play()
    p.name = "test_name"
    assert p.get_name() == "test_name"
    p.name = ""
    p.hosts = []
    assert p.get_name() == ""
    p.hosts = ["host_1", "host_2"]
    assert p.get_name() == "host_1,host_2"
    p.hosts = "host"
    assert p.get_name() == "host"

# Generated at 2022-06-13 08:34:39.804497
# Unit test for method get_name of class Play
def test_Play_get_name():
    host_list = 'localhost'
    host_list1 = ['localhost']
    host_list2 = ['localhost','host1']
    play = Play()
    play.hosts = host_list
    assert play.get_name() == 'localhost'
    play.hosts = host_list1
    assert play.get_name() == 'localhost'
    play.hosts = host_list2
    assert play.get_name() == 'localhost,host1'


# Generated at 2022-06-13 08:34:53.392522
# Unit test for method deserialize of class Play
def test_Play_deserialize():
  play = Play()
  play.deserialize(dict(
    name = 'foobar',
    connection = 'local',
    hosts = 'all',
    gather_facts = 'yes',
    tasks = [
      {
        'name': 'set some facts',
        'set_fact': {
          'first_fact': 'some_value',
          'second_fact': 'some_other_value'
        }
      },
      {
        'name': 'include_tasks',
        'include_tasks': 'tasks/foobar.yml'
      }
    ]
  ))
  assert play.name == 'foobar'
  assert play.connection == 'local'
  assert play.hosts == 'all'
  assert play.gather_facts == 'yes'

# Generated at 2022-06-13 08:35:03.730205
# Unit test for method get_name of class Play
def test_Play_get_name():
    def test(test_name, test_data, exp_value):
        with pytest.raises(Exception) as execinfo:
            play = Play()
            play.name = test_data['name']
            play.hosts = test_data['hosts']
            play.vars = test_data['vars']
            play.hosts_count = test_data['hosts_count']

            play.get_name()
            assert execinfo.value == exp_value
    test_data = {
        'name': '',
        'hosts': '',
        'vars': {},
        'hosts_count': {},
    }
    exp_value = ''
    test('Test Case 1', test_data, exp_value)


# Generated at 2022-06-13 08:35:11.361994
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    '''
    Unit test for method get_vars_files of class Play
    '''
    # test cases
    play = get_test_play()
    # play.vars_files = ['xx']
    with pytest.raises(AnsibleParserError) as e:
        play._load_vars_files('vars_files', None)
        assert 'value of vars_files must be a list' in str(e.value)
    # play.vars_files = [{'hosts': 'xx'}]
    with pytest.raises(AnsibleParserError) as e:
        play._load_vars_files('vars_files', None)
        assert 'value of vars_files must be a list' in str(e.value)
    # play.vars_files = [{

# Generated at 2022-06-13 08:35:19.576505
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # Compilation
    # Since this class is inherited from the class DataContainer,
    # it's better to test the compilation of this class with the class DataContainer
    # Since the class DataContainer has been well tested, so the testing of compiling
    # with this class is not implemented
    # One similar scenario is in the function compile_roles_handlers
    # in the class Play. This function inherits from a function of the class
    # DataContainer, so the testing of this method is also not implemented
    pass

# Generated at 2022-06-13 08:35:20.784850
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    assert False

# Generated at 2022-06-13 08:35:55.769299
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    p = Play()
    p.vars_files = 'test'
    assert p.get_vars_files() ==  ['test']
    p.vars_files = None
    assert p.get_vars_files() == []
    p.vars_files = ['test']
    assert p.get_vars_files() ==  ['test']

# Generated at 2022-06-13 08:35:59.617701
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    data = "{'cloud': 'ec2', 'roles': ['role1', 'role2']}"
    p = Play()
    p.deserialize(data)
    assert p.roles == ['role1', 'role2']

# Generated at 2022-06-13 08:36:07.062117
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # Test with no roles
    play = Play()
    play.roles = []
    assert play.compile_roles_handlers() == []

    # Test with one role
    play.roles = []
    role = mock.Mock()
    for i in range(4):
        handler = mock.Mock()
        handler.serialize = mock.Mock(return_value=i)
        role.get_handler_blocks.return_value = [handler]
        play.roles += [role]
    assert play.compile_roles_handlers() == [0, 1, 2, 3]


# Generated at 2022-06-13 08:36:11.248874
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    role = Role()
    role.name = 'test_role'
    role.hosts = 'host2'
    role._block = [{'block': [{'meta': 'flush_handlers'}], 'rescue': [], 'always': [], 'tags': [], 'when': '', 'name': 'Test handler'}]
    play.roles.append(role)
    play.compile_roles_handlers()


# Generated at 2022-06-13 08:36:22.704616
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    from ansible.playbook.task import Task
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.block import Block
    play = Play()
    play._ds['hosts'] = 'localhost'
    play._ds['roles'] = []
    role1 = RoleDefinition()
    role1._role_name = 'A'
    role1._role_path = 'A'
    role2 = RoleDefinition()
    role2._role_name = 'B'
    role2._role_path = 'B'

    handler1 = Task()
    handler1._task_action = 'handler A'
    handler1._role = role1
    handler2 = Task()
    handler2._task_action = 'handler B'
    handler2._role = role2
    handler3 = Task()
   

# Generated at 2022-06-13 08:36:27.867997
# Unit test for method get_name of class Play
def test_Play_get_name():
    p = Play()
    p.name = "my_play"
    p.hosts = "all"
    assert p.get_name() == "my_play"
    assert p.get_name() == p.name
    p.name = None
    assert p.get_name() == "all"
    p.hosts = None
    assert p.get_name() == ""

# Generated at 2022-06-13 08:36:38.371900
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():

    host_list = ['localhost']
    play = Play()
    play.hosts = host_list
    block_list = play.compile_roles_handlers()
    assert block_list == []

    host_list = ['localhost']
    play = Play()
    play.hosts = host_list
    role = Role()
    role.get_handler_blocks = lambda play: [1, 2, 3]
    play.roles = [role]
    block_list = play.compile_roles_handlers()
    assert block_list == [1, 2, 3]


# Generated at 2022-06-13 08:36:43.075971
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    with open(str(DATA_DIR)+'/play.yml') as f:
        play.load_data(f.read())
    pprint.pprint(play.get_tasks())

# Generated at 2022-06-13 08:36:47.063435
# Unit test for method get_name of class Play
def test_Play_get_name():
	# Create test data
	data = {}
	# Create test object
	p = Play()
	# Test
	assert p.get_name() == ""
	# Test
	assert repr(p) == p.get_name()

# Generated at 2022-06-13 08:37:00.720007
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play = Play()
    data = {'name': 'test_name',
            'roles': [{'name': 'test_role_name'},
                      {'name': 'test_role_name2'}]}
    play.deserialize(data)
    assert play._variable_manager == None
    assert play._loader == None
    assert play.name == 'test_name'
    assert len(play.roles) == 2
    assert play.roles[0].name == 'test_role_name'
    assert play.roles[1].name == 'test_role_name2'
    assert play._included_path == None
    assert play._action_groups == {}
    assert play._group_actions == {}

# Generated at 2022-06-13 08:37:21.358227
# Unit test for method get_name of class Play
def test_Play_get_name():
    play_data = {
        'hosts': ['host1', 'host2', 'host3'],
        'tasks': [
            {
                'action': {
                    'module': 'shell',
                    'args': 'ls'
                }
            }
        ]
    }
    play = Play.load(play_data, variable_manager=None, loader=None)
    play_name = play.get_name()
    assert play_name == 'host1,host2,host3'


# Generated at 2022-06-13 08:37:23.279952
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # Setup
    play = Play()
    blocklist = [Handler(), Handler()]
    # Test
    pla

# Generated at 2022-06-13 08:37:25.260575
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    play_name = play.get_name()
    assert play_name == ''


# Generated at 2022-06-13 08:37:29.984715
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play.tasks = [{'name':'task1'}, {'name':'task2'}]
    assert len(play.get_tasks()) == 2

if __name__ == "__main__":
    test_Play_get_tasks()

# Generated at 2022-06-13 08:37:32.235145
# Unit test for method get_name of class Play
def test_Play_get_name():
    p = Play()
    p.name = 'test'
    assert p.get_name() == 'test'


# Generated at 2022-06-13 08:37:45.012954
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    from ansible.playbook.play import Play
    from ansible.utils import plugin_docs
    from ansible.utils.display import Display
    from ansible.plugins.loader import all as all_plugins
    plugin_docs['DOCUMENTATION'] = '''
---
module: print
short_description: Print a message
version_added: "2.3"
description:
   - Prints a message from the task.
options:
  msg:
    description:
      - The message to be printed.
    required: true
author: "{{ AUTHOR }}"
'''
    plugin_docs['RETURN'] = '''
{
  "changed": false
}
'''
    display = Display()

# Generated at 2022-06-13 08:37:53.503742
# Unit test for method get_tasks of class Play

# Generated at 2022-06-13 08:37:56.976508
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    p = Play()

    if p.vars_files is None:
        assert p.get_vars_files() == []
    elif not isinstance(p.vars_files, list):
        assert p.get_vars_files() == [p.vars_files]
    else:
        assert p.get_vars_files() == p.vars_files


# Generated at 2022-06-13 08:38:08.733674
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop

    loader = DictDataLoader({
        "tasks.yml": """
        - name: "wait for the wrong thing"
          wait_for:
            host: wrong_host
            port: 80
          delegate_to: "{{ hostvars[groups['webservers'][0]].ansible_host }}"
        """,
    })
    inventory = InventoryManager(loader=loader, sources=["hosts.yml"])
    inventory.parse_sources(None, cache=False)

    play = Play()

# Generated at 2022-06-13 08:38:17.026155
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play1 = {'hosts': 'localhost', 'tasks': [{'name': 'task1', 'action': 'debug', 'args': {'msg': 'task1'}}]}
    play2 = {'hosts': 'localhost', 'handlers': [{'name': 'handler1', 'action': 'debug', 'args': {'msg': 'handler1'}}]}
    play3 = {'hosts': 'localhost', 'pre_tasks': [{'name': 'pre_task1', 'action': 'debug', 'args': {'msg': 'pre_task1'}}]}
    play4 = {'hosts': 'localhost', 'post_tasks': [{'name': 'post_task1', 'action': 'debug', 'args': {'msg': 'post_task1'}}]}

# Generated at 2022-06-13 08:38:53.736657
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    p = Play()
    p.ROLE_CACHE = {}
    p._included_conditional = None
    p._included_path = None
    p._action_groups = {}
    p._group_actions = {}
    p.ROLE_CACHE = {}
    p._included_conditional = None
    p._included_path = None
    p._action_groups = {}
    p._group_actions = {}
    p.roles = []
    p.roles = []
    return p.compile_roles_handlers()

# Generated at 2022-06-13 08:39:04.012330
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()

    # Verify the case where there is no roles
    block_list = play.compile_roles_handlers()
    assert block_list == []

    # Verify the case where there is one role with handler
    role = Role()

# Generated at 2022-06-13 08:39:06.389142
# Unit test for method get_name of class Play
def test_Play_get_name():
    p = Play()
    p.name = 'playbook 1'

    assert p.get_name() == 'playbook 1'

# Generated at 2022-06-13 08:39:13.206983
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    assert play.get_name() == ''
    play.name = 'test'
    assert play.get_name() == 'test'
    play.hosts = ['server1', 'server2']
    assert play.get_name() == 'test'
    play.name = None
    assert play.get_name() == 'server1,server2'
    play.hosts = None
    assert play.get_name() == ''


# Generated at 2022-06-13 08:39:25.640619
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # setup
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory import Inventory
    variable_manager = VariableManager()
    loader=DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=['localhost:1234'])
    play = Play.load(dict(
        name="Ansible Play name",
        hosts=inventory,
        remote_user="root",
        gather_facts='no',
        become='no',
        become_method='sudo',
        become_user='root',
        become_ask_pass=False,
        serial=0,
        roles=[],
        vars=[],
    ), loader=loader, variable_manager=variable_manager)
    # test

# Generated at 2022-06-13 08:39:35.581239
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    from ansible.playbook.block import Block
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    import mock

    # AnsiblePlaybookContext
    apc = mock.create_autospec(AnsiblePlaybookContext)
    apc.vault_password = None
    apc.new_vault_password = None
    apc.ask_vault_pass = False
    apc.ask_new_vault_pass = False
    apc.vault_ids = []
    apc.become_pass = None
    apc.verbosity = 0

# Generated at 2022-06-13 08:39:40.456253
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    p = Play()
    p.name = 'declare'
    assert p.name == 'declare'
    p.preprocess_data({"name": "execute"})
    assert p.name == "execute"


# Generated at 2022-06-13 08:39:49.521354
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    variable_manager = VariableManager()
    play_ds1 = dict(
        name="Ansible Play 1",
        hosts="test",
        gather_facts="no",
        vars=[dict(a=1, b=2, c=3)],
        tasks=[dict(action=dict(module="debug", args=dict(msg="Hello World!"))),
               dict(action=dict(module="debug", args=dict(msg="Hello World!")))],
    )
    play1 = Play.load(play_ds1, variable_manager=variable_manager, loader=loader)
    assert play1.preprocess_data(play_ds1) is not None
    assert play1

# Generated at 2022-06-13 08:39:57.859906
# Unit test for method get_name of class Play
def test_Play_get_name():
    """
    Test case for Play.get_name.

    """
    p = Play()
    p.name = None
    p.hosts = "192.168.0.0"
    
    # Expected result
    assert p.get_name() == "192.168.0.0"

    p = Play()
    p.name = "192.168.0.0"
    p.hosts = "192.168.0.0"
    
    # Expected result
    assert p.get_name() == "192.168.0.0"

# Generated at 2022-06-13 08:40:06.669457
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    test_play = Play()
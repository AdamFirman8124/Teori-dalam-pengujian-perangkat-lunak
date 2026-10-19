

# Generated at 2022-06-13 08:31:28.631847
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    play = Play()
    ds = {"user":"a", "hosts":"a", "roles": [{"role":"test"}]}
    ds_1 = play.preprocess_data(ds)

    assert isinstance(ds_1, dict)
    assert ds_1["remote_user"] == "a"
    assert "user" not in ds_1
    assert ds_1["roles"][0]["role"] == "test"


# Generated at 2022-06-13 08:31:31.940660
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    playname = 'test play'
    play.name = playname
    assert play.get_name() == playname, f"Failed to get play name"


# Generated at 2022-06-13 08:31:41.110801
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    fake_loader = DictDataLoader({})
    fake_inventory = Inventory(loader=fake_loader, variable_manager=VariableManager(), host_list=[])
    fake_variable_manager = VariableManager()
    play_source = dict(
        name = "Ansible Play",
        hosts = 'all',
        gather_facts = 'no',
        tasks = [
            {"action": {"module": "shell", "args": "ls"}, "async": 123, "poll": 0},
            {"action": {"module": "shell", "args": "ls"}, "async": 123, "poll": 0}
        ]
    )
    p = Play().load(play_source, fake_variable_manager, fake_loader)
    p.check_privilege_escalation_allowed()
    p.check_tasks_not_root_system

# Generated at 2022-06-13 08:31:48.384723
# Unit test for method get_name of class Play
def test_Play_get_name():
  play = Play()
  assert play.get_name() == None
  play.name = 'test'
  assert play.get_name() == 'test'
  play.hosts = ['host1', 'host2']
  play.name = ''
  assert play.get_name() == 'host1,host2'
  play.name = None
  assert play.get_name() == 'host1,host2'


# Generated at 2022-06-13 08:31:49.002608
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass



# Generated at 2022-06-13 08:31:54.611742
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    # preprocess_data test data
    data = [
        # General test with data
        {
            # Input
            'input': {
                'hosts': 'all',
                'user': 'root',
                'roles': [{'role': 'WebServers', 'vars': {}}],
            },
            # Expected output
            'expected': {
                'hosts': 'all',
                'remote_user': 'root',
                'roles': [{'role': 'WebServers', 'vars': {}}],
            }
        }
    ]
    # Iterate through the test data
    for item in data:
        # Get the test input and expected output
        input = item['input']
        expected = item['expected']

        # Create the play object
        p = Play()
        # Preprocess

# Generated at 2022-06-13 08:32:00.702512
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    set_loader()
    # Test with vars.
    p = Play()
    p.load_data({'hosts': 'localhost', 'vars': { 'foo': 'bar' }})
    assert 'foo' in p.vars
    # Test without vars.
    p = Play()
    p.load_data({'hosts': 'localhost'})
    assert not hasattr(p, 'vars')

# Generated at 2022-06-13 08:32:14.062959
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude

    p = Play()
    p.pre_tasks = [1]
    p.tasks = [2, 3]
    p.post_tasks = [TaskInclude({}, play=p)]

    b = Block.load(
        data={'block': [4], 'rescue': [5], 'always': [6]},
        play=p,
    )
    p.post_tasks.append(b)

    assert p.get_tasks() == [1, 2, 3, 4, 5, 6]



# Generated at 2022-06-13 08:32:22.897802
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():

    #playbook = Playbook('/home/sux/Desktop/playbooks/test_playbook1.yaml')
    #play = playbook.get_plays()[0]
    play = Play()
    play.vars_files = None

    assert play.get_vars_files() == []

    #playbook = Playbook('/home/sux/Desktop/playbooks/test_playbook1.yaml')
    #play = playbook.get_plays()[0]
    play = Play()
    play.vars_files = 'a.yml'

    assert play.get_vars_files() == ['a.yml']

    #playbook = Playbook('/home/sux/Desktop/playbooks/test_playbook1.yaml')
    #play = playbook.get_plays()[0]


# Generated at 2022-06-13 08:32:24.890194
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    v = Play()
    v.compile_roles_handlers()

# Generated at 2022-06-13 08:32:38.183932
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    play_dict={
        "name": "test_play", 
        "user": "test_user", 
        "hosts": ["all"]
    }
    play_obj = Play()
    new_play_dict = play_obj.preprocess_data(play_dict)
    assert "user" not in new_play_dict
    assert new_play_dict["remote_user"] == play_dict["user"]

# Generated at 2022-06-13 08:32:40.501754
# Unit test for method get_name of class Play
def test_Play_get_name():
  assert Play().get_name() == ''
  obj = Play()
  obj.name = 'test'
  assert obj.get_name() == 'test'


# Generated at 2022-06-13 08:32:52.191604
# Unit test for method serialize of class Play
def test_Play_serialize():
    # Load a test play and make sure we get back a dict
    p = Play.load(dict(
        name="test",
        hosts='localhost',
        gather_facts='no'
    ))
    data = p.serialize()
    assert isinstance(data, dict)
    # We do not expect the following in the serialized dict
    assert not data.get('ROLE_CACHE')
    assert not data.get('_included_conditional')
    assert not data.get('_included_path')
    assert not data.get('_action_groups')
    assert not data.get('_group_actions')
    # We only expect two dicts with the roles
    assert len(data.get('roles')) == 2

# Generated at 2022-06-13 08:33:00.885031
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
  "Test Play.get_tasks()"
  # Create a fake Play inventory
  inventory = Mock(spec=Inventory)
  # Create a fake loader
  loader = Mock(spec=DataLoader)
  # Create a fake variablemanager, no need to mock default values
  variable_manager = Mock(spec=VariableManager, host_vars={}, group_vars={}, extra_vars={}, all_hosts=[], meta_hostvars={})
  
  # Set attributes for the fake Play

# Generated at 2022-06-13 08:33:11.397310
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()

    # vars_files has the value None
    play.vars_files = None
    assert play.get_vars_files() == []

    # vars_files is a value of type list
    play.vars_files = ['/etc/ansible/group_vars/windows.yml']
    assert play.get_vars_files() == ['/etc/ansible/group_vars/windows.yml']

    # vars_files is a value of type string
    play.vars_files = "/home/ansible/playbook.yml"
    assert play.get_vars_files() == ["/home/ansible/playbook.yml"]

# Generated at 2022-06-13 08:33:27.293937
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    p._ds = dict(
            name='callee',
            hosts='webservers',
            tasks=[
                {'name': 'awesome', 'action': ['something'], 'notify': 'handler'},
                {'block': [
                    {'name': 'webservers', 'action': ['something'], 'notify': 'handler'},
                    {'name': 'others', 'action': ['something'], 'notify': 'handler'},
                ]},
            ],
            handlers=[
                {'name': 'handler', 'action': ['something']},
            ]
        )
    p._load_data()
    p.compile()
    tasks =  p.get_tasks()
    assert len(tasks) == 6

# Generated at 2022-06-13 08:33:39.952515
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    p = Play() 
    var_files = []
    # case-1 : vars_files attribute is not set
    # result : [] is returned
    assert p.get_vars_files() == []

    # case-2 : vars_files attribute is set as a string
    p.vars_files = 'abc'
    # result : the string is wrapped in a list and returned 
    assert p.get_vars_files() == ['abc']

    # case-3 : vars_files attribute is set as a list
    var_files = ['abc', 'xyz']
    p.vars_files = var_files
    # result : the list itself is returned
    assert p.get_vars_files() == var_files

# Generated at 2022-06-13 08:33:54.514906
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play = Play()
    data = {
        'roles': [
            {
                'role_name': 'saltstack.salt',
                'role_path': '/home/myuser/myproject/roles/saltstack.salt',
                'role_params': {},
                'role_vars': {},
                'role_tasks': None,
                'role_handlers': None,
            }
        ],
        'included_path': './roles/saltstack.salt/meta/main.yml',
    }
    play.deserialize(data)
    assert isinstance(play.roles[0], Role)
    assert play.included_path == './roles/saltstack.salt/meta/main.yml'

# Generated at 2022-06-13 08:33:56.010704
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    p = Play()

    # TODO, add unit tests here
    return True

# Generated at 2022-06-13 08:34:08.783212
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    role1 = Role()
    role1.role_name = 'testRole'
    role1.role_path = './testRole'
    role1.tasks = [Block( tasks=[Task(action='testtask', async_val=1)], handlers=[Handler(action='testhandler', async_val=1)] )] # FIXME: action is not a valid attribute for Handler, only tasks

    role2 = Role()
    role2.role_name = 'testRole2'
    role2.role_path = './testRole2'
    role2.tasks = [Block( tasks=[Task(action='testtask2', async_val=2)], handlers=[Handler(action='testhandler2', async_val=2)] )] # FIXME: action is not a valid attribute for Handler, only tasks

    role3 = Role()

# Generated at 2022-06-13 08:34:26.889487
# Unit test for method serialize of class Play
def test_Play_serialize():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.template import Templar
    def test_serialize(module_words, is_new_play = None, loader = None , variable_manager = None, variable_manager_obj = None, templar = None, play = None, new_stdin = None):
        if loader is None:
            loader = DataLoader()
        if variable_manager is None:
            variable_manager = VariableManager()
        if variable_manager_obj is None:
            variable_manager_obj = dict()

# Generated at 2022-06-13 08:34:30.890608
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    play.vars_files = ['foo', 'bar']
    assert play.get_vars_files() == ['foo', 'bar']


# Generated at 2022-06-13 08:34:39.938566
# Unit test for method get_name of class Play
def test_Play_get_name():
    from ansible.playbook import Play
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory import Inventory
    from collections import namedtuple
    from ansible.vars.manager import VariableManager
    from ansible.utils.hosts import Host, Inventory
    from ansible.module_utils._text import to_bytes
    import unittest

    # Function to be tested
    def get_name():
        return self.name

    # Setup
    p = Play()
    p._name = "Test Play"

    # Compare
    assert p.get_name() == "Test Play"



# Generated at 2022-06-13 08:34:53.632771
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    import os
    import sys
    import unittest
    import lib.ansible_module as ansible_module
    import ansible.constants as C
    from ansible.utils.vars import combine_vars
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    fake_loader = DataLoader()
    fake_inventory = InventoryManager(loader=fake_loader, sources='')
    fake_variable

# Generated at 2022-06-13 08:34:55.477736
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play_obj = Play()
    ret = play_obj.get_vars_files()
    assert(not ret)


# Generated at 2022-06-13 08:35:04.909718
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    play.name = 'testname'
    assert play.get_name() == 'testname'

    play.name = None
    play.hosts = None
    assert play.get_name() == ''

    play.hosts = ['host1']
    assert play.get_name() == 'host1'

    play.hosts = ['host1', 'host2', 'host3']
    assert play.get_name() == 'host1,host2,host3'

    play.hosts = ['host1', 'host2,host3']
    assert play.get_name() == 'host1,host2,host3'



# Generated at 2022-06-13 08:35:07.104301
# Unit test for method get_name of class Play
def test_Play_get_name():
    myPlay = Play()
    myPlay._ds = dict(name="myName")
    assert myPlay.get_name() == "myName"


# Generated at 2022-06-13 08:35:09.554478
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    data = {'user': 'root'}
    data_e = {'remote_user': 'root'}
    p = Play()
    p.preprocess_data(data)
    assert data == data_e


# Generated at 2022-06-13 08:35:13.944740
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    data = dict(
        name="test",
        hosts="hostname",
        pre_tasks=[dict(
            name="foobar",
            action="command",
            args=dict(
                cmd="echo 1"
            )
        )],
    )
    p = Play()
    p.load_data(data)
    tasks = p.get_tasks()
    assert len(tasks) == 1
    assert isinstance(tasks[0], Task)
    assert tasks[0].action == "command"



# Generated at 2022-06-13 08:35:14.784989
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
   pass

# Generated at 2022-06-13 08:35:33.160033
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    name = "localhost"
    playbook = "playbook.yml"
    _play = Play.load(
        dict(
            name=name,
            hosts=name,
            vars_files=["/tmp/vars_files.yml"],
            vars=dict(
                a=1,
                b=dict(
                    c=2
                )
            )
        ),
        variable_manager=BaseVariableManager(
            loader=DictDataLoader({}),
            variables=dict(a=1, b=dict(c=2))
        ),
        loader=BaseLoader()
    )
    _play.vars_files = _play.get_vars_files()
    assert len(_play.vars_files) == 1


# Generated at 2022-06-13 08:35:41.524952
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    play.vars_files = 'test'
    res = play.get_vars_files()
    assert res == ['test'], 'get_vars_files: should be ["test"] but returned %s' % res
    play.vars_files = ['test1', 'test2']
    res = play.get_vars_files()
    assert res == ['test1', 'test2'], 'get_vars_files: should be ["test1", "test2"] but returned %s' % res

# Generated at 2022-06-13 08:35:51.337080
# Unit test for method get_name of class Play
def test_Play_get_name():
    p = Play()
    p.name = 'testname'
    assert(p.get_name() == 'testname')
    p.name = ''
    p.hosts = ['testhost']
    assert(p.get_name() == 'testhost')
    p.hosts = []
    assert(p.get_name() == '')
    p.hosts = ['testhost1', 'testhost2', 'testhost3']
    assert(p.get_name() == 'testhost1,testhost2,testhost3')
    p.hosts = ['testhost1', None, 'testhost3']
    p.name = ''
    assert('Hosts list contains an invalid host value' in p.get_name())
    p.hosts = [123]
    p.name = ''

# Generated at 2022-06-13 08:35:55.360759
# Unit test for constructor of class Play
def test_Play():
    import json

    with open('../../test/sanity/json_yaml/pm.json') as f:
        play_data = json.load(f)
    pm = Play.load(data=play_data)
    assert pm.name == 'test'



# Generated at 2022-06-13 08:35:57.461500
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # TODO: Write tests for method get_vars_files of class Play
    pass


# Generated at 2022-06-13 08:36:04.083748
# Unit test for method get_name of class Play
def test_Play_get_name():
    def do_test(hosts, name):
        p = Play()
        p.hosts = hosts
        p.name = name
        p.post_validate()
        return p.get_name()
    assert do_test("host", None) == "host"
    assert do_test(["host1", "host2"], None) == "host1,host2"
    assert do_test("host", "testName") == "testName"


# Generated at 2022-06-13 08:36:14.323148
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    #Arguments for method compile_roles_handlers of class Play
    play = Play()
    play.ROLE_CACHE = {'name':'value'}
    play._included_conditional = 'value'
    play._included_path = 'value'
    play._action_groups = {'name':'value'}
    play._group_actions = {'name':'value'}

    #result is a list of Handlers
    result = play.compile_roles_handlers()

    play.ROLE_CACHE = {'key':'value'}
    play._included_conditional = 'value'
    play._included_path = 'value'
    play._action_groups = {'name':'value'}
    play._group_actions = {'name':'value'}

# Generated at 2022-06-13 08:36:18.803433
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    play._load_roles = MagicMock()
    play._load_roles.return_value = []
    block_list = play.compile_roles_handlers()
    assert block_list == []


# Generated at 2022-06-13 08:36:29.378370
# Unit test for method preprocess_data of class Play

# Generated at 2022-06-13 08:36:41.885836
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    class MockJSONFile(object):
        def __init__(self, data):
            self._data = data

        def read_json(self):
            return self._data

    class MockLoader(object):
        def __init__(self, data):
            self._mocks = {}
            for path in data:
                self._mocks[path] = MockJSONFile(data[path])

        def path_dwim(self, path):
            return os.path.abspath(path)

        def get_basedir(self, path):
            return os.path.abspath(os.path.dirname(path))

        def load_from_file(self, path, **kwargs):
            if path not in self._mocks:
                raise AnsibleFileNotFound("Could not find or access %s" % path)

# Generated at 2022-06-13 08:36:50.719395
# Unit test for method get_name of class Play
def test_Play_get_name():
    expected = '0.20.10'
    actual = __version__
    assert expected == actual, 'Test failed: {} != {}'.format(expected, actual)


# Generated at 2022-06-13 08:36:57.346526
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    tasks = [ { 'name': 'test1', 'action': {'module':'debug', 'msg': 'msg'} },
              { 'action': {'module':'debug', 'msg': 'msg2'} },
              { 'action': {'module':'debug', 'msg': 'msg3'} },
              { 'name': 'test4', 'action': {'module':'debug', 'msg': 'msg4'} } ]
    roles = [ { 'name': 'test1', 'tasks': [{ 'name': 'test1', 'action': {'module':'debug', 'msg': 'msg'} }] } ]
    post_tasks = [ { 'name': 'test2', 'action': {'module':'debug', 'msg': 'msg2'} } ]

# Generated at 2022-06-13 08:37:01.994611
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    play.vars_files = 1
    play.get_vars_files()
    play.vars_files = [1,2,3]
    play.get_vars_files()

# Generated at 2022-06-13 08:37:09.144416
# Unit test for method get_name of class Play
def test_Play_get_name():
    p = Play()
    p.name = 'DummyName'
    assert p.get_name() == 'DummyName'
    p.name = None
    p.hosts = ['localhost']
    assert p.get_name() == 'localhost'
    p = Play()
    p.hosts = ['localhost']
    assert p.name == 'localhost'
    p = Play()
    p.hosts = 'localhost'
    assert p.name == 'localhost'
    p = Play()
    p.hosts = None
    p.name = None
    assert p.get_name() == ''

# Syntax test for method get_vars_files of class Play

# Generated at 2022-06-13 08:37:12.919107
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    """
    Test Play.get_vars_files()
    """
    play = Play()
    play.vars_files = ['varsfile']
    assert play.get_vars_files() == ['varsfile']


# Generated at 2022-06-13 08:37:22.115140
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    play_obj = Play()
    play_obj._ds = None
    play_obj._ds = 'a'
    #Test except case
    try:
        play_obj.preprocess_data('a')
    except AnsibleAssertionError:
        pass
    play_obj._ds = 'a'
    play_obj.preprocess_data({'user': 'ansible', 'roles': [{'role': 'nagios'}, {'role': 'apache'}]})
    assert 'remote_user' in play_obj._ds
    assert play_obj._ds['user'] == 'ansible'


# Generated at 2022-06-13 08:37:22.821990
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass

# Generated at 2022-06-13 08:37:26.932899
# Unit test for method get_name of class Play
def test_Play_get_name():
    # Setup
    p = Play()
    hosts = ['host1', 'host2']
    p.hosts = hosts

    # Testing
    result = p.get_name()

    # Verifying
    assert(result == ','.join(hosts))

# Generated at 2022-06-13 08:37:29.820472
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    """
    # TODO: it is not not clear what is the goal of this method
    # the returned value of this method is never used,
    # and the code seems a bit complicated
    # I am going to leave this test as it is to avoid introducing further
    # uncertainty of the code
    """
    # TODO: implement unit test
    pass


# Generated at 2022-06-13 08:37:35.326764
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
	if not sys.argv[1] or not sys.argv[2]:
		print("Please enter the path to play.yaml as first argument and the expected output as the second argument")
		exit()
	f = open(sys.argv[1],'r')
	ds = yaml.load(f)
	play = Play()
	play.preprocess_data(ds)
	play_yaml = yaml.dump(ds)
	expected_output = open(sys.argv[2],'r').read()
	if play_yaml == expected_output:
		print("Success")
	else:
		print("Fail")
		d = difflib.Differ()

# Generated at 2022-06-13 08:37:50.290460
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # We can't really test this method as there are no concrete methods to call it yet
    pass

# Generated at 2022-06-13 08:37:54.843730
# Unit test for method serialize of class Play
def test_Play_serialize():
    test_data = {"free_form_tags": [], "groups": [], "no_log": [], "when": [], "gather_facts": "yes", "vars": {}, "name": "test play book"}
    play = Play.load(test_data)
    play_serialize = play.serialize()
    assert play_serialize ==  test_data


# Generated at 2022-06-13 08:38:05.960027
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    load_call_count = [0]
    p = Play()
    p.roles = [{"include": "name", "role": "role1"}]
    p.resolve_roles = lambda roles: [Role.load(preprocess_role_spec("role1"), play=p)]
    p.find_role = lambda role, use_role_paths=False: Role.load(preprocess_role_spec("role1"), play=p)
    p.handlers = [{"include": "name", "handler": "handler1"}, {"include": "name", "handler": "handler2"}]
    p.resolve_roles_handlers = lambda handlers: [Handler.load({'name': 'handler1'}, play=p), Handler.load({'name': 'handler2'}, play=p)]
    p.find_handler

# Generated at 2022-06-13 08:38:06.798825
# Unit test for method serialize of class Play
def test_Play_serialize():
    pass

# Generated at 2022-06-13 08:38:15.130827
# Unit test for method get_name of class Play
def test_Play_get_name():
    from ansible.module_utils.six import PY3

    assert isinstance(Play().get_name(), text_type)
    assert Play().get_name() == ''
    assert Play(dict(name='testPlay')).get_name() == 'testPlay'
    assert Play(dict(hosts='localhost')).get_name() == 'localhost'
    assert Play(dict(hosts=['localhost'])).get_name() == 'localhost'
    assert Play(dict(hosts=['localhost', 'localhost'])).get_name() == 'localhost,localhost'
    assert isinstance(Play(dict(hosts=['localhost', 'localhost'])).get_name(), text_type)


# Generated at 2022-06-13 08:38:23.915978
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play.load(dict(
        name = 'Testing Play',
        hosts = 'all',
        gather_facts = 'no',
        tasks=[
            dict(action=dict(module='debug', args=dict(msg='{{testing_variable}}')), register='debug_result')
        ]
    ), variable_manager=VariableManager(), loader=DataLoader())
    role = Role()
    role.deserialize(dict(
        name='Testing Role',
        handlers=dict(
            tasks=[
                dict(action=dict(module='debug', args=dict(msg='Testing handler')))
            ]
        )
    ))
    play.roles.append(role)

    handler_list = play.compile_roles_handlers()
    assert len(handler_list) == 1
    assert handler_list[0].block

# Generated at 2022-06-13 08:38:32.539768
# Unit test for method get_name of class Play
def test_Play_get_name():
    p = Play()
    assert p.get_name() == ''
    p.name = 'test_name'
    assert p.get_name() == 'test_name'
    p.name = None
    p.hosts = ['test_host']
    assert p.get_name() == 'test_host'
    p.hosts = ['test_host1', 'test_host2']
    assert p.get_name() == 'test_host1,test_host2'

# Generated at 2022-06-13 08:38:36.875758
# Unit test for method get_name of class Play
def test_Play_get_name():
    assert Play().get_name() == ''
    assert Play(name="test").get_name() == "test"
    assert Play(hosts="test").get_name() == "test"


# Generated at 2022-06-13 08:38:39.879184
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    play.name = 'my test play'
    assert play.get_name() == 'my test play'

play = Play()
play.name = 'my test play'


# Generated at 2022-06-13 08:38:41.355677
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    assert play.compile_roles_handlers() == []


# Generated at 2022-06-13 08:39:49.885235
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass

# Generated at 2022-06-13 08:40:00.903760
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    test_data = [
        ([], []),
        (['./test/test_data/vars1.yml'], ['./test/test_data/vars1.yml']),
        (['../test/test_data/vars1.yml'], ['../test/test_data/vars1.yml']),
        (['test_data/vars1.yml'], ['test_data/vars1.yml']),
        (['test_data/vars1.yml', 'test_data/vars2.yml'], ['test_data/vars1.yml', 'test_data/vars2.yml'])
    ]

# Generated at 2022-06-13 08:40:05.777859
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    assert play.get_name() == ''

    play.name = 'test play name'
    assert play.get_name() == 'test play name'

    play.hosts = 'hosts string'
    assert play.get_name() == 'test play name'

    play.hosts = ['hosts', 'list']
    assert play.get_name() == 'test play name'



# Generated at 2022-06-13 08:40:07.414534
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    raise NotImplementedError

# Generated at 2022-06-13 08:40:18.549476
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    from ansible.vars.manager import VariableManager

    variable_manager = VariableManager()

    paths = [ './test/test_play.yml', './test/test_play2.yml', './test/test_play3.yml' ]

# Generated at 2022-06-13 08:40:22.851576
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    p = Play()
    p.vars_files = ["hello"]
    assert p.get_vars_files() == ["hello"]
    p.vars_files = None
    assert p.get_vars_files() == []
    p.vars_files = ["test", "test2"]
    assert p.get_vars_files() == ["test", "test2"]

# Generated at 2022-06-13 08:40:29.362323
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    play.vars_files = None
    assert play.get_vars_files() == []
    play = Play()
    play.vars_files = "test"
    assert play.get_vars_files() == ['test']
    play = Play()
    play.vars_files = [1, 2]
    assert play.get_vars_files() == [1, 2]



# Generated at 2022-06-13 08:40:34.621699
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # Creating play and defining attributes
    play = Play()
    # Running method compile_roles_handlers and testing results
    assert play.compile_roles_handlers() == [], "Incorrect result for method compile_roles_handlers"


# Generated at 2022-06-13 08:40:40.389274
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    play.roles = [Role(), Role()]
    play.roles[0].handlers = [Handler()]
    play.roles[1].handlers = [Handler(), Handler()]
    assert play.compile_roles_handlers() == [Handler(), Handler(), Handler(), Handler()]
    assert play.roles[0].handlers == [Handler()]
    assert play.roles[1].handlers == [Handler(), Handler()]


# Generated at 2022-06-13 08:40:47.320814
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler

    block_list = []

    # create a block containing a single flush handlers meta
    # task, so we can be sure to run handlers at certain points
    # of the playbook execution
    flush_block = Block.load(
        data={'meta': 'flush_handlers'},
        play=None,
        variable_manager=None,
        loader=None
    )

    for task in flush_block.block:
        task.implicit = True

    block_list.append(flush_block)
    block_list.extend(flush_block)

    print(block_list)
    print([b.serialize() for b in block_list])


    role = Role()

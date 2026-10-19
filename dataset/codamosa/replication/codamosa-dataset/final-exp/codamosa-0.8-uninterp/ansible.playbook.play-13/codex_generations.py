

# Generated at 2022-06-13 08:31:25.413805
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    pass

# Generated at 2022-06-13 08:31:26.415374
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass


# Generated at 2022-06-13 08:31:33.202098
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    _variable_manager = VariableManager()
    _loader = DataLoader()
    play = Play()
    data = {
      'hosts': 'localhosts',
      'name': 'test_play',
      'pre_tasks': [],
      'roles': [
        {
          'role': 'test_role'
        }
      ],
      'tasks': [
        {
          'name': 'test_task',
          'command': 'echo "test"'
        }
      ]
    }
    play.preprocess_data(data)
    assert play.name == 'test_play'
    assert play.hosts == 'localhosts'
    assert play.tasks[0].name == 'test_task'
    assert isinstance(play.tasks[0], Task)

# Generated at 2022-06-13 08:31:34.024636
# Unit test for method deserialize of class Play
def test_Play_deserialize():
	pass

# Generated at 2022-06-13 08:31:42.169587
# Unit test for method get_name of class Play
def test_Play_get_name():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    p = Play()
    p.name = 'test'
    assert p.get_name() == 'test'
    p.name = None
    assert p.get_name() == ''

    p.hosts = 'test'
    assert p.get_name() == 'test'

    p.hosts = ['test']
    assert p.get_name() == 'test'

    p.hosts = None
    assert p.get_name() == ''

    p.hosts = []
    assert p.get_name() == ''



# Generated at 2022-06-13 08:31:48.615031
# Unit test for method serialize of class Play
def test_Play_serialize():
    pl = Play.load(dict(hosts='hosts', roles=['role1', 'role2']), [])

    serialized = pl.serialize()
    assert serialized['hosts'] == 'hosts'
    assert serialized['roles'][0]['name'] == 'role1'
    assert serialized['roles'][1]['name'] == 'role2'



# Generated at 2022-06-13 08:31:52.240399
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play = Play() 
    data = {'tasks': [
        {'include': 'test.yml'}, 
        {'action': {'module': 'test.yml'}}, 
        {'continue': 'on'}], 
            'hosts': 'test.yml'}
    play.deserialize(data)

    assert data == play.serialize()
    assert data == play.deserialize(play.serialize())


# Generated at 2022-06-13 08:32:00.405262
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # Import data
    data = ast.literal_eval("{'handlers': [], 'vars': {}, 'tasks': [], 'post_tasks': [], 'roles': [], 'pre_tasks': [], 'vars_files': ['/mnt/x/ansible/cicd/ansible/ansible-meta-generator/main.yml'], 'hosts': 'localhost', 'hosts_vars': {}, 'host_vars': {}, 'meta': {}, 'name': 'localhost'}")

    # Create a new Play object
    p = Play.load(data)

    # Unit test:
    assert p.get_vars_files() == ['/mnt/x/ansible/cicd/ansible/ansible-meta-generator/main.yml']



# Generated at 2022-06-13 08:32:02.779985
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play = Play()
    play.deserialize({'roles': []})
    assert play.roles == []

# Generated at 2022-06-13 08:32:07.968349
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    # Params
    data = dict()

    # Execution
    try:
        p = Play()
        p.deserialize(data)
    except Exception as e:
        print(e)
        assert False, 'Raises error'
    else:
        assert True



# Generated at 2022-06-13 08:32:26.043825
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    test_Play = Play()
    test_Play.vars_files = "vars_files"
    test_get_vars_files = test_Play.get_vars_files()
    assert (test_get_vars_files==["vars_files"])

# Generated at 2022-06-13 08:32:39.800707
# Unit test for method preprocess_data of class Play

# Generated at 2022-06-13 08:32:43.180881
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    # Construct arguments
    data = None
    
    
    
    
    # Assertion
    raise AssertionError('Test is not implemented !')

# Generated at 2022-06-13 08:32:48.027624
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play.pre_tasks = ["Pre-tasks"]
    play.post_tasks = ["Post-tasks"]
    play.tasks = ["Tasks"]
    assert play.get_tasks() == ["Pre-tasks", "Tasks", "Post-tasks"]


# Generated at 2022-06-13 08:32:56.790582
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    # call the method to test
    p = Play()
    try:
        p.preprocess_data(33)
    except AnsibleAssertionError as e:
        assert str(e) == 'while preprocessing data (33), ds should be a dict but was a <class \'int\'>'
    else:
        assert False, "AnsibleAssertionError not raised"

    # test the user deprecation
    data = dict(user="root", remote_user="admin")
    try:
        p.preprocess_data(data)
    except AnsibleParserError as e:
        assert str(e) == "both 'user' and 'remote_user' are set for this play. The use of 'user' is deprecated, and should be removed"
    else:
        assert False, "AnsibleParserError not raised"

# Generated at 2022-06-13 08:33:00.057627
# Unit test for method get_name of class Play
def test_Play_get_name():
    # Play creation
    Play_get_name = Play()
    Play_get_name.name = 'play'

    # Testing method get_name of class Play
    assert Play_get_name.get_name() == 'play'

# Generated at 2022-06-13 08:33:11.875745
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    assert p.get_tasks() == []
    p.tasks = ['foo', 'bar']
    assert p.get_tasks() == ['foo', 'bar']
    p.pre_tasks = ['foo']
    assert p.get_tasks() == ['foo', 'foo', 'bar']
    p.post_tasks = ['bar']
    assert p.get_tasks() == ['foo', 'foo', 'bar', 'bar']
    p.tasks = ['foo', 'bar']
    p = Play()
    assert p.get_tasks() == []
    p.tasks = ['foo', 'bar']
    assert p.get_tasks() == ['foo', 'bar']
    p.pre_tasks = ['foo']

# Generated at 2022-06-13 08:33:15.347211
# Unit test for constructor of class Play
def test_Play():
    p=Play()
    print(p.name)

if __name__ == "__main__":
    test_Play()

# Generated at 2022-06-13 08:33:18.811433
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    play.hosts = 'localhost'
    name = play.get_name()
    assert name == 'localhost'

# Generated at 2022-06-13 08:33:32.887696
# Unit test for method preprocess_data of class Play

# Generated at 2022-06-13 08:33:51.626758
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play_data = {
        "name": "Ansible Play",
        "hosts": "all",
        "roles": [{
            "role": "file_example_role"
        }]
    }
    p = Play()
    p._load_data(play_data)

    handlers = p.compile_roles_handlers()
    assert len(handlers) == 1
    for handler in handlers:
        for task in handler.tasks:
            assert task.get_name() == "/usr/bin/touch /tmp/{{ansible_date_time.date_time_iso8601_micro}}"


# Generated at 2022-06-13 08:33:52.859472
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    play.compile_roles_handlers()



# Generated at 2022-06-13 08:33:57.745946
# Unit test for method get_name of class Play
def test_Play_get_name():
    host = 'localhost'
    name = 'mockTest'
    p = Play()
    p.vars = {"name": name}
    p.hosts = host
    result = p.get_name()
    assert result == host


if __name__ == '__main__':
    test_Play_get_name()

# Generated at 2022-06-13 08:34:00.875333
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    play.name = "name"
    assert play.get_name() == "name"
    assert play.name == "name"

# Generated at 2022-06-13 08:34:05.816462
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    p = Play()
    p.deserialize({'roles': [{'file': 'file'}]})
    assert p.roles[0].file == 'file'
    assert p._included_path == None


# Generated at 2022-06-13 08:34:16.755953
# Unit test for method get_name of class Play
def test_Play_get_name():
    '''
    Unit test for method get_name of class Play
    '''
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    import os
    import json

    class Args(object):
        def __init__(self):
            self.listhosts = None
            self.listtasks = None
            self.listtags = None
            self.syntax = None
            self.connection = None
            self.module_path = None
            self.forks = None
            self.remote_user = None
            self.private_key_file = None
            self.ssh

# Generated at 2022-06-13 08:34:25.408586
# Unit test for method get_name of class Play
def test_Play_get_name():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    my_variable_manager = VariableManager()
    my_loader = DataLoader()
    my_inventory = InventoryManager(loader=my_loader, sources=['localhost,'])
    my_play = Play.load(dict(name='test_play'), variable_manager=my_variable_manager, loader=my_loader)
    assert (my_play.get_name() == 'test_play')


# Generated at 2022-06-13 08:34:26.089489
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass

# Generated at 2022-06-13 08:34:28.152235
# Unit test for method get_name of class Play
def test_Play_get_name():
    p = Play()
    assert p.get_name() == ''

# Generated at 2022-06-13 08:34:34.805819
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    vars_files = [
        '/Users/towas/Documents/ansible-module-gcp/devel/ansible/test/vars1.yaml',
        '/Users/towas/Documents/ansible-module-gcp/devel/ansible/test/vars2.yaml',
    ]
    vars_files_list = [
        '/Users/towas/Documents/ansible-module-gcp/devel/ansible/test/vars1.yaml',
        '/Users/towas/Documents/ansible-module-gcp/devel/ansible/test/vars2.yaml',
    ]
    play = Play()
    play.vars_files = vars_files
    assert play.get_vars_files() == vars_files_list
#

# Generated at 2022-06-13 08:34:47.260545
# Unit test for method get_name of class Play
def test_Play_get_name():
	play = Play()
	play.hosts = ['host1']
	play.name = 'test_Play_get_name'
	assert play.name == 'test_Play_get_name'
	
	play.name = None
	assert play.name == 'host1'


# Generated at 2022-06-13 08:34:50.685076
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    from ansible.playbook.play import Play
    play = Play()

# Generated at 2022-06-13 08:34:52.188194
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    pass

# Generated at 2022-06-13 08:34:56.972960
# Unit test for method get_name of class Play
def test_Play_get_name():
    test_play = Play()
    test_play.hosts = ""
    assert test_play.get_name() == ""
    test_play.hosts = "a b c"
    assert test_play.get_name() == "a b c"

# Generated at 2022-06-13 08:35:07.501930
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    p = Play()
    p.ROLE_CACHE = {}
    p._included_conditional = None
    p._included_path = None
    p._action_groups = {}
    p._group_actions = {}
    p.ROLE_CACHE = {}
    p.only_tags = set(context.CLIARGS.get('tags', [])) or frozenset(('all',))
    p.skip_tags = set(context.CLIARGS.get('skip_tags', []))
    p.handlers = []
    p.roles = []
    p.tasks = []
    p._included_conditional = None
    p._included_path = None
    p._removed_hosts = []
    p.name = None

# Generated at 2022-06-13 08:35:14.001728
# Unit test for method get_name of class Play
def test_Play_get_name():
    print("testing get_name")
    inventory = Inventory(loader=C.DEFAULT_LOADER, variable_manager=None, host_list=['localhost'])
    play_source = dict(
        name="Ansible Play",
        hosts='localhost',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        ]
    )
    play = Play().load(play_source, variable_manager=None, loader=C.DEFAULT_LOADER)
    name = play.get_name()
    assert(name == "Ansible Play")
    print("test done")


# Generated at 2022-06-13 08:35:15.921253
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    p = Play()
    assert p.compile_roles_handlers() == []

# Generated at 2022-06-13 08:35:27.001683
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader

    def get_play_ds():
        return {'name': 'test_play',
                'hosts': 'localhost',
                'vars': {'val1': 'OK'},
                'gather_facts': 'no',
                'connection': 'local',
                'roles': [{'name': 'test_role'}],
                'tasks': [{'name': 'task1'}, {'name': 'task2'}]}


# Generated at 2022-06-13 08:35:30.106407
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    temp_obj = Play()
    temp_obj._ds = {'vars_files': ['/etc/ansible/user.yml', ['/etc/ansible/user.yml', '/etc/ansible/group.yml']]}
    temp_obj._load_vars_files(attr='vars_files', ds=temp_obj._ds)
    temp_obj.get_vars_files()



# Generated at 2022-06-13 08:35:37.073177
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    pl = Play()
    pl.pre_tasks = [1, 2, 3]
    pl.tasks = [4, 5, 6]
    pl.post_tasks = [7, 8, 9]
    
    expected_tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert pl.get_tasks() == expected_tasks

# Generated at 2022-06-13 08:35:53.745778
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    data = {
        'hosts': 'localhost',
        'roles': [],
        'tasks': [
            {'name': 'A'},
            {'name': 'B'},
            {'name': 'C'},
        ]
    }
    p = Play.load(data, variable_manager=VariableManager(), loader=DictDataLoader())
    print(p.get_tasks())

# Generated at 2022-06-13 08:35:59.064225
# Unit test for method serialize of class Play
def test_Play_serialize():
    Play.load(data=dict(
        name='My play',
        hosts=['localhost', '127.0.0.1']
    ), variable_manager=VariableManager(), loader=DummyLoader())

if __name__ == '__main__':
    # Unit test for method serialize of class Play
    test_Play_serialize()

# Generated at 2022-06-13 08:36:00.236623
# Unit test for constructor of class Play
def test_Play():
    assert Play().name == ''

# Generated at 2022-06-13 08:36:02.173006
# Unit test for method get_name of class Play
def test_Play_get_name():
    result = Play.get_name(self)
    assert isinstance(result, object)


# Generated at 2022-06-13 08:36:08.298059
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    # create and populate a dict
    data = {'user': 'bob'}
    # create instance of play and populate with data
    play = Play()
    play.load_data(data)
    # run preprocess_data
    play.preprocess_data(data)
    # verify success
    assert data['remote_user'] == 'bob'

# Compile play with pre_tasks and post_tasks attributes

# Generated at 2022-06-13 08:36:08.884187
# Unit test for constructor of class Play
def test_Play():
    pass

# Generated at 2022-06-13 08:36:16.272643
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    play.vars_files = [
        '../../../../tests/mock_playbooks/play_vars_files_1.yml',
        '../../../../tests/mock_playbooks/play_vars_files_2.yml'
    ]
    play_vars_files = play.get_vars_files()
    assert play_vars_files[0] == '../../../../tests/mock_playbooks/play_vars_files_1.yml'
    assert play_vars_files[1] == '../../../../tests/mock_playbooks/play_vars_files_2.yml'

# Generated at 2022-06-13 08:36:25.539777
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    # With no vars_files should return empty list
    assert play.get_vars_files() == []
    assert type(play.get_vars_files()) is list
    # With a list of files
    play.vars_files = ['/path1', '/path2']
    assert play.get_vars_files() == ['/path1', '/path2']
    # With a single file
    play.vars_files = '/path1'
    assert play.get_vars_files() == ['/path1']


# Generated at 2022-06-13 08:36:33.351225
# Unit test for method get_name of class Play
def test_Play_get_name():
    # Test function get_name of class Play with
    # The three cases:
    # 1. When the name is set
    # 2. When the name is not set but hosts is a list
    # 3. When the name is empty
    # And a case, when the hosts is empty
    # 4. When the name is empty and hosts is empty

    # Case 1. When name is set
    play = Play()
    play.name = 'name_of_play'
    assert play.get_name() == 'name_of_play'

    # Case 2. When the name is not set but hosts is a list
    play = Play()
    play.hosts = ['1.1.1.1', '2.2.2.2', '3.3.3.3']

# Generated at 2022-06-13 08:36:37.889195
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # ------------------------------
    # Variables
    play = Play()
    play.handlers = []
    # ------------------------------

    # Tests
    assert play.compile_roles_handlers() == []

Play()

# Generated at 2022-06-13 08:36:55.374049
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    test_play = Play()
    test_play.vars_files = ["/path/to/vars1", "/path/to/vars2"]
    assert test_play.get_vars_files() == ["/path/to/vars1", "/path/to/vars2"]
    test_play.vars_files = "/path/to/vars"
    assert test_play.get_vars_files() == ["/path/to/vars"]



# Generated at 2022-06-13 08:37:05.995025
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # Test for default value attribute vars_files of class Play
    my_play = Play()
    assert my_play.vars_files is None

    # Test for assignment attribute vars_files of class Play
    my_play.vars_files = Play.vars_files._default
    assert my_play.vars_files is Play.vars_files._default
    my_play.vars_files = 'test_value'
    assert my_play.vars_files == 'test_value'
    my_play.vars_files = ['test_value', 'test_value']
    assert my_play.vars_files == ['test_value', 'test_value']
    my_play.vars_files = None
    assert my_play.vars_files is None

    # Test for method get_vars

# Generated at 2022-06-13 08:37:08.939001
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    """Test the Play object's compile_roles_handlers method"""
    p = Play()
    p.roles = [Role()]
    assert p.compile_roles_handlers() == []


# Generated at 2022-06-13 08:37:15.645685
# Unit test for method get_name of class Play
def test_Play_get_name():
  p = Play()
  assert p.get_name() == ''
  p.name = 'foo'
  assert p.get_name() == 'foo'
  p.name = None
  p.hosts = 'bar'
  assert p.get_name() == 'bar'
  p.hosts = ['bar', 'baz']
  assert p.get_name() == 'bar,baz'


# Generated at 2022-06-13 08:37:20.266000
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():

    # This is the Play object we want to test
    play = Play()
    
    # We first create the roles that the Play object will contain
    role1 = Role()
    role1.name = 'role1'
    role2 = Role()
    role2.name = 'role2'
    
    # We create the handler objects that we want to put in the role handler
    # blocks
    handlers1 = []
    handlers1.append(Handler())
    handlers1[0].action = 'action1'
    handlers1.append(Handler())
    handlers1[1].action = 'action2'
    handlers2 = []
    handlers2.append(Handler())
    handlers2[0].action = 'action3'
    handlers2.append(Handler())
    handlers2[1].action = 'action4'
    
    # We use

# Generated at 2022-06-13 08:37:24.061047
# Unit test for method get_name of class Play
def test_Play_get_name():
    p = Play()
    p.name = 'test_name'
    assert p.get_name() == 'test_name'
    p = Play()
    assert p.get_name() == ''
    p.hosts = ['test_host1']
    assert p.get_name() == 'test_host1'

# Generated at 2022-06-13 08:37:34.722759
# Unit test for constructor of class Play
def test_Play():
    instance = Play()
    assert isinstance(instance, Play)
    assert instance._play_hosts == 'all'
    assert instance.hosts is None
    assert instance.connection == 'smart'
    assert instance.port is None
    assert instance.remote_user is None
    assert instance.timeout is None
    assert instance.remote_pass is None
    assert instance.sudo is None
    assert instance.sudo_user is None
    assert instance.become is None
    assert instance.become_method is None
    assert instance.become_user is None
    assert instance.become_pass is None
    assert instance.become_expire is None
    assert instance.vars is None
    assert instance.vars_files is None
    assert instance.tags is None
    assert instance.skip_tags is None
    assert instance.g

# Generated at 2022-06-13 08:37:47.822807
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    import copy
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler

    # NOTE: THIS FUNCTION IS DUPLICATED IN DOCUMENTATION.PY
    # TODO: Move this function to a common place
    def create_handler(**kwargs):
        handler = Handler()
        handler.name = 'test handler'
        handler.notify_list.append('test task')

        for attr, value in kwargs.items():
            setattr(handler, attr, value)

        return handler

    # NOTE: THIS FUNCTION IS DUPLICATED IN DOCUMENTATION.PY
    # TODO: Move this function to a common place
    def create_task(tags=None):
        task = Task()
        task.name = 'test task'

# Generated at 2022-06-13 08:37:49.265557
# Unit test for method get_name of class Play
def test_Play_get_name():
    assert True

# Generated at 2022-06-13 08:37:57.254900
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    p.ROLE_CACHE = {}
    p._included_conditional = None
    p._included_path = None
    p._action_groups = {}
    p._group_actions = {}

    p.pre_tasks = ([])
    p.tasks = ([])
    p.post_tasks = ([])

    tasklist = []
    for task in p.pre_tasks + p.tasks + p.post_tasks:
        if isinstance(task, Block):
            tasklist.append(task.block + task.rescue + task.always)
        else:
            tasklist.append(task)
    assert p.get_tasks() == tasklist


# Generated at 2022-06-13 08:38:20.757960
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    #play1 = dict(test_play)
    play1 = {
             'hosts': 'localhost',
             'vars': {'var1': 'value of var1'},
             'pre_tasks': [
                 {'name': 'task1'},
                 {'name': 'task2'},
                 {'name': 'task3'}
             ],
             'tasks': [
                 {'name': 'task4'},
                 {'name': 'task5'},
                 {'name': 'task6'}
             ],
             'post_tasks': [
                 {'name': 'task7'},
                 {'name': 'task8'},
                 {'name': 'task9'}
             ]
    }
    play = Play.load(play1)
    tasklist = play.get

# Generated at 2022-06-13 08:38:27.390822
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    from ansible.playbook.play_context import PlayContext

    p = Play.load(
        dict(
            name="dummy play",
            hosts="localhost",
            gather_facts="no",
            vars=dict(
                a=1, b="2"
            ),
            vars_files=[
                "/path/to/file1",
                "/path/to/file2",
                "/path/to/file3",
                "file4",
                dict(
                    value=["file5", "file6"],
                    basedir="/"
                )
            ],
            connection="local"
        ),
        variable_manager=VariableManager(),
        loader=DictDataLoader()
    )

    p.variable_manager.set_inventory(Inventory("localhost"))
    pc = PlayContext(p)

# Generated at 2022-06-13 08:38:33.405583
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    play.roles = []
    role = Role()
    role.from_include = False
    role.compile(play=play)
    role.get_handler_blocks(play=play)
    play.roles.append(role)
    assert play.compile_roles_handlers()


# Generated at 2022-06-13 08:38:43.645536
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.role.include import RoleInclude
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager)
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 08:38:46.264016
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    play.roles = ['test']
    play.compile_roles_handlers()


# Generated at 2022-06-13 08:38:51.704078
# Unit test for method serialize of class Play
def test_Play_serialize():
    p = Play()
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager()
    p._tqm = tqm
    p_s = p.serialize()
    assert p_s is not None


# Generated at 2022-06-13 08:39:01.092678
# Unit test for method get_name of class Play
def test_Play_get_name():
  play = Play()
  assert play.get_name() == ''

  play.name = 'test_Play_get_name_name'
  assert play.get_name() == 'test_Play_get_name_name'

  play.hosts = 'test_Play_get_name_hosts'
  assert play.get_name() == 'test_Play_get_name_hosts'

  play.hosts = 'test_Play_get_name_hosts_1,test_Play_get_name_hosts_2'
  assert play.get_name() == 'test_Play_get_name_hosts_1,test_Play_get_name_hosts_2'


# Generated at 2022-06-13 08:39:06.664283
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()

    b1 = Block(play=p)
    b2 = Block(play=p)

    t1 = Task(play=p)
    t2 = Task(play=p)
    t3 = Task(play=p)

    b1.block = [t1]
    b1.rescue = [t2]
    b1.always = [t3]
    b2.block = [t3]

    p.pre_tasks = [t1, b1]
    p.tasks = [b1, b2, t3]
    p.post_tasks = [t2]

    assert p.get_tasks() == [t1, t2, t3, t1, t3, t3, t2]


# Generated at 2022-06-13 08:39:11.685196
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play.tasks = 10
    assert play.get_tasks() == 10


# Generated at 2022-06-13 08:39:17.596114
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    # Test empty Play
    assert play.compile_roles_handlers() == []
    
    # Test Play with a single role but no handlers
    play.roles = [Mock(return_value=Role())]
    assert play.compile_roles_handlers() == []
    
    # Test Play with one role with handlers
    block_list = Block()
    block_list.block = [Task()]
    play.roles = [Mock(return_value=Role(handler_blocks=(block_list,)))]
    assert play.compile_roles_handlers() == [block_list]
    
    # Test Play with two roles with handlers

# Generated at 2022-06-13 08:39:54.374405
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()

    assert play.get_tasks() == []

    play.pre_tasks = [1,2,3]
    play.tasks = ["a", "b"]
    play.post_tasks = [4,5]
    assert play.get_tasks() == [1,2,3, "a", "b", 4,5]

    def get_block_tasks(block):
        return block.block + block.rescue + block.always

    block = Block()
    block.block = [1,2]
    block.rescue = [3,4]
    block.always = [5,6]

    play.pre_tasks = [block]

    assert play.get_tasks() == [get_block_tasks(block), "a", "b", 4,5]

# Generated at 2022-06-13 08:40:04.470125
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    module_utils_mock = MagicMock()
    module_utils_mock_action_plugin = MagicMock()

    mock_loader = DictDataLoader({
        'test_directory/test_role/tasks/main.yaml': '',
        'test_directory/test_role_2/tasks/main.yaml': '',
    })

    mock_block_list = [MagicMock(get_handler_blocks=MagicMock(return_value=[MagicMock()]))]
    
    play_mock = Play()


# Generated at 2022-06-13 08:40:06.176409
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    play.name = 'test'
    assert play.get_name() == 'test'


# Generated at 2022-06-13 08:40:10.216654
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play.pre_tasks = ["a", "b"]
    play.tasks = ["c", "d"]
    play.post_tasks = ["e", "f"]
    tasklist = play.get_tasks()
    assert tasklist == ["a", "b", "c", "d", "e", "f"]
    tasklist = play.get_tasks()
    assert tasklist == ["a", "b", "c", "d", "e", "f"]

# Generated at 2022-06-13 08:40:21.045364
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play.tasks = []
    play.tasks.append(dict(action=dict(module='debug', args=dict(msg='Gift of Gab'))))
    play.tasks.append(dict(action=dict(module='debug', args=dict(msg='Chief Xcel'))))
    play.tasks.append('not a task')
    play.tasks.append(dict(action=dict(module='debug', args=dict(msg='Lyrics Born'))))
    play.tasks.append(dict(action=dict(module='debug', args=dict(msg='Lateef The Truthspeaker'))))
    tasks = play.get_tasks()
    assert tasks[0]['action']['args']['msg'] == 'Gift of Gab'

# Generated at 2022-06-13 08:40:32.917199
# Unit test for constructor of class Play
def test_Play():
    p = Play()
    assert p._attributes['name'] is None, 'Play() should have a name of None, but name is %s' % p._attributes['name']
    assert p.roles is not None, 'Play() should have a roles list'
    assert p.roles == [], 'Play() should have an empty roles list, but roles list is %s' % p.roles
    assert p.tags is not None, 'Play() should have a tags set'
    assert p.tags == ['all'], 'Play() should have a tags set of [\'all\'] by default, but tags value is %s' % p.tags
    assert p._variable_manager is None, 'Play() should have a _variable_manager of None, but _variable_manager value is %s' % p._variable_manager

# Generated at 2022-06-13 08:40:43.964167
# Unit test for method get_name of class Play
def test_Play_get_name():
    # fixtures
    from ansible.playbook.play_context import PlayContext
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import fragment_loader

    loader = DataLoader()
    context = PlayContext()
    inventory = InventoryManager(loader, sources=[], vault_password=None, fragmentation_plugin=fragment_loader)
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # test
    play = Play()
    play._variable_manager = variable_manager
    play.hosts = ['host1']

    assert play.hosts == ['host1']
    assert play.name == 'host1'


# Generated at 2022-06-13 08:40:44.789347
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
  pass

# Generated at 2022-06-13 08:40:53.138723
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play.pre_tasks = [Block(block=['task1', 'task2'], rescue=[], always=[])]
    play.tasks = [Block(block=['task3', 'task4'], rescue=[], always=[])]
    print(play.get_tasks())
    assert set(play.get_tasks()) == set([['task3', 'task4'], ['task1', 'task2']])
    print(play.get_tasks())


# Generated at 2022-06-13 08:40:59.319876
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # Testing Preconditions
    #1. Instantiating role
    role = Role()
    role.name = "demo_role"
    role.collection = "demo_collection"
    role.tasks_path = "/home/tasks/demo_task"
    role.default_vars = "/home/default/vars/demo_vars"
    role.default_vars_files = "/home/default/vars/demo_vars_file"
    role.role_vars = "/home/tasks/demo_role_var"
    role.role_vars_files = "/home/tasks/demo_role_var_file"
    role.metadata_files = "/home/tasks/demo_meta_file"
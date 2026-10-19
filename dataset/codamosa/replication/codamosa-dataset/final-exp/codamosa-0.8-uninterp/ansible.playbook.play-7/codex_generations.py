

# Generated at 2022-06-13 08:31:32.126322
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    def get_host_list(with_children=True):
        ret = []
        for i in range(3):
            host = Host(self.hostname)
            host.vars = self.get_vars()
            host.groups = self.get_groups()
            host.set_variable('foo', 'bar')
            children = [Group(child) for child in self.get_groups()]
            host.set_variable('child_groups', children if with_children else [])
            ret.append(host)
        return ret

    def get_vars():
        return dict(a=dict(b=dict(c='test')))

    def get_groups():
        return ['all', 'ungrouped1']

    def _gen_play(play):
        play.load_data(self.play_source)


# Generated at 2022-06-13 08:31:41.250796
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    play_vars_prompt = {u'vars_prompt': [{u'name': u'foo', u'prompt': u'bar', u'private': False, u'unsafe': True}]}
    play = Play()
    play.load(play_vars_prompt)
    fake_loader = DictDataLoader({})
    fake_variable_manager = VariableManager()
    play.set_loader(fake_loader)
    play.set_variable_manager(fake_variable_manager)
    play.post_validate()
    assert play.vars_prompt[0]['unsafe'] == True
    play_vars_prompt = {u'vars_prompt': [{u'name': u'foo', u'prompt': u'bar', u'confirm': False}]}
    play

# Generated at 2022-06-13 08:31:44.116916
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play = Play()
    data = play.serialize()
    play.deserialize(data)


# Generated at 2022-06-13 08:31:53.826852
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    from ansible.parsing.dataloader import DataLoader

    ldr = DataLoader()
    p = Play()
    p.deserialize({'hosts': 'localhost', 'roles': [{'name': 'test_role'}], '_included_path': '/path/to/playbook.yml'})

    assert isinstance(p.vars, dict)
    assert isinstance(p.roles, list)
    assert isinstance(p.roles[0], Role)
    assert p._included_path == '/path/to/playbook.yml'
    assert p._variable_manager is not None
    assert p._loader is not None

    # make sure loader is passed on during init
    p = Play(loader=ldr)
    assert p._loader is ldr


# Generated at 2022-06-13 08:31:59.753853
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    play = Play()
    data = dict(
        name="Test",
        hosts="localhost",
        roles=[
            dict(
                role=dict(
                    name="Test",
                    tasks=[
                        dict(
                            name="Test"
                        )
                    ]
                )
            )
        ]
    )
    play.deserialize(data)
    ansible_play = Play.load(data)
    assert play.serialize() == ansible_play.serialize()

# Generated at 2022-06-13 08:32:15.841573
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    #
    # Create a sample of data structure
    #
    data = {
        "name": "test play",
        "hosts": "test_hosts",
        "user": "test_user",
        "tasks": [
            { "name": "test task", "local_action": {"module": "test_module"} },
            { "name": "test task", "local_action": {"module": "test_module"} },
        ],
    }
    #
    # Create a play object
    #
    p = Play()
    #
    # Test preprocess_data
    #
    try:
        result = p.preprocess_data(data)
    except:
        assert False


# Generated at 2022-06-13 08:32:20.772987
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    ## Test that when 'user' is in the data structure, it is converted
    ## to 'remote_user'.
    play = Play()
    play.preprocess_data({'user': 'testuser'})

    ## Test that when 'user' is not in the data structure, it is not
    ## added, but no error is raised.
    play = Play()
    play.preprocess_data({})

# Generated at 2022-06-13 08:32:22.796804
# Unit test for method deserialize of class Play
def test_Play_deserialize():
    data = {}
    p = Play(data)
    assert p.deserialize(data) == None

# Generated at 2022-06-13 08:32:37.989522
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    p = Play()
    p._load_roles(None, [{'name': u'role1', 'tasks': [{'include_role': {'name': u'role2'}}, {'include_role': {'name': u'role3'}}]}])
    ret = p.compile_roles_handlers()
    assert ret == [[Block(parent_block=None, role=p.ROLE_CACHE['role1'], task_include=None, use_handlers=True, always_run=False, use_tags=None, fail_fast=False, fail_on_skip=False, block=None, rescue=None, always=None)]]

# Generated at 2022-06-13 08:32:45.953966
# Unit test for constructor of class Play
def test_Play():

    p = Play()
    assert p.name is None
    assert p.hosts == 'all'
    assert p.remote_user == C.DEFAULT_REMOTE_USER
    assert p.connection == C.DEFAULT_TRANSPORT
    assert p.port == C.DEFAULT_REMOTE_PORT
    assert not p.any_errors_fatal
    assert p.max_fail_percentage == 0
    assert p.gather_facts == 'all'
    assert p.serial == 1
    assert p.sudo is False
    assert p.sudo_user == C.DEFAULT_SUDO_USER
    assert not p.sudo_pass
    assert not p.authorize
    assert not p.remote_pass
    assert not p.su
    assert not p.su_user
    assert not p.su_pass


# Generated at 2022-06-13 08:33:01.550641
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    class Role(object):
        pass
    class Block(object):
        pass
    class Play(object):
        def __init__(self):
            self.roles = []
    p1 = Play()
    r1 = Role()
    b1 = Block()
    r1.get_handler_blocks = lambda play: [b1]
    p1.roles = [r1]
    assert p1.compile_roles_handlers() == [b1]     
    # Accepts as input Compiled Play object

# Generated at 2022-06-13 08:33:02.463837
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass

# Generated at 2022-06-13 08:33:04.891557
# Unit test for method get_name of class Play
def test_Play_get_name():
    test_obj = Play()
    assert test_obj.get_name() == ''



# Generated at 2022-06-13 08:33:09.407673
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    pl = Play()
    test_data = {'roles': 'roles'}
    ret = pl.preprocess_data(test_data)
    assert (ret['roles'] == 'roles')


# Generated at 2022-06-13 08:33:14.882885
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # test with good and base inputs
    test_play = Play()
    assert test_play.compile_roles_handlers() == []
    assert type(test_play.compile_roles_handlers()) == list


# Generated at 2022-06-13 08:33:20.163224
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    print("Testing get_tasks of class Play:")
    play = Play()
    def test_file():
        print("\tTesting get_tasks() with file as input:")
        play.pre_tasks=list(tasks(file='./test/tasks/get_tasks/tasks.yml'))
        play.tasks=list(tasks(file='./test/tasks/get_tasks/tasks.yml'))
        play.post_tasks=list(tasks(file='./test/tasks/get_tasks/tasks.yml'))
        if len(play.get_tasks()) == 9:
            print('\t\tTest passed: get_tasks() returned all tasks')

# Generated at 2022-06-13 08:33:32.580022
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    my_vars_files = ['my_vars_files-a','my_vars_files-b']
    loader = DataLoader()
    variable_manager = VariableManager()
    p = Play()
    p.vars_files = my_vars_files
    assert p.get_vars_files() == my_vars_files
    p = Play()
    p.deserialize({'vars_files':my_vars_files,'handler_tags':[]})
    assert p.get_vars_files() == my_vars_files


# Generated at 2022-06-13 08:33:39.741005
# Unit test for constructor of class Play
def test_Play():
    play = Play()
    assert play._play_hosts == 'all'
    assert play._play_hosts is not None
    assert play._play_name is None
    assert play._role_names == []
    assert play.ROLE_CACHE == {}
    play_roles = play.get_roles()
    assert play_roles == []

# Generated at 2022-06-13 08:33:40.462974
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass

# Generated at 2022-06-13 08:33:55.232298
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    loader = DictDataLoader({
        'test.yml': """
- hosts: localhost
  connection: local
  pre_tasks:
  - name: Task 1
    debug:
      msg: Task 1
  tasks:
  - name: Task 2
    debug:
      msg: Task 2
  post_tasks:
  - name: Task 3
    debug:
      msg: Task 3
- hosts: localhost
  connection: local
  pre_tasks:
  - name: Task 4
    debug:
      msg: Task 4
  tasks:
  - name: Task 5
    debug:
      msg: Task 5
  post_tasks:
  - name: Task 6
    debug:
      msg: Task 6
"""
    })

# Generated at 2022-06-13 08:34:12.482689
# Unit test for method get_name of class Play
def test_Play_get_name():
    # Test the case when name is set and the result value is the same as the value of 'name'
    test_instance = Play()
    test_instance.name = 'Foo'
    assert test_instance.get_name() == 'Foo'
    # Test the case when name is not set, but hosts is a sequence
    test_instance = Play()
    test_instance.name = None
    test_instance.hosts = ['Bar']
    assert test_instance.get_name() == 'Bar'
    # Test the case when name is not set and hosts is not a sequence
    test_instance = Play()
    test_instance.name = None
    test_instance.hosts = None
    assert test_instance.get_name() == ''


# Generated at 2022-06-13 08:34:20.485859
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    Play._loader = DictDataLoader({"/playbook.yml": """
    ---
    - hosts: localhost
      gather_facts: no
      tasks:
      - shell: "uname -a"
      - name: copy some files
        copy:
          src: /usr/bin/nohup
          dest: /usr/bin/nohup
          owner: root
          group: root
          mode: 0755
      post_tasks:
      - shell: "uname -a"

    """})
    p = Play().load('/playbook.yml')
    p.preprocess_data(p.get_data_for_included_file())

    assert len(p.tasks) == 2
    assert len(p.post_tasks) == 1

# Generated at 2022-06-13 08:34:23.210614
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # Test is trivial at the moment, will expand
    assert type(Play().get_vars_files()) is list

# Generated at 2022-06-13 08:34:28.887385
# Unit test for method get_name of class Play
def test_Play_get_name():
    # get_name of the class Play
    # data = {"hosts": "all", "name": "Test", "vars": {"var1": "value1"}}
    # ds = Play.load(data, variable_manager=None, loader=None)
    # assert ds.get_name() == "Test"
    pass

# Generated at 2022-06-13 08:34:40.063790
# Unit test for method get_name of class Play
def test_Play_get_name():
    import ansible.parsing.dataloader
    import ansible.vars
    import ansible.inventory
    import ansible.playbook.play
    loader = ansible.parsing.dataloader.DataLoader()
    variable_manager = ansible.vars.VariableManager()
    inventory = ansible.inventory.Inventory(loader=loader, variable_manager=variable_manager, host_list='localhost')
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 08:34:48.289135
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    ansible_vars_files_path = mylib.get_project_root() + "/ansible/vars/main.yml"
    play = Play()
    play.vars_files = ansible_vars_files_path
    assert play.get_vars_files() == [ansible_vars_files_path]
    #assert play.get_vars_files() == ansible_vars_files_path



# Generated at 2022-06-13 08:35:00.300540
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    block = Block()
    task = Task()
    task1 = Task()
    task2 = Task()
    play.pre_tasks.append(block)
    play.pre_tasks.append(task1)
    play.tasks.append(task2)
    block.block.append(task)

    tasks = play.get_tasks()
    assert tasks[0] == [task1]
    assert tasks[1] == [task2]
    assert tasks[2] == [task]

    play = Play()
    block1 = Block()
    block2 = Block()
    block3 = Block()
    task1 = Task()
    task2 = Task()
    task3 = Task()
    task4 = Task()
    task5 = Task()
    task6 = Task()

# Generated at 2022-06-13 08:35:09.245508
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    from ansiblelint import RulesCollection
    from ansiblelint.rules.UseShellInsteadOfCommandRule import UseShellInsteadOfCommandRule
    collection = RulesCollection()
    collection.register(UseShellInsteadOfCommandRule())

    filename = 'testPlay.yml'
    p = Play()

    # get_tasks() returns empty list if tasks are not set
    assert p.get_tasks() == []

    # get_tasks() returns list of tasks
    with open(filename, 'r') as stream:
        p.load_data(yaml.safe_load(stream), variable_manager=None, loader=None)
    assert type(p.get_tasks()) == list

    # set_tasks() sets tasks
    t = Task()
    p.set_tasks([t])
    assert p.get_tasks

# Generated at 2022-06-13 08:35:15.276102
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='unit_tests/ansible_unit_tests.yml')
    play = Play.load("unit_tests/test_plays/test_get_tasks_play.yml", variable_manager=variable_manager, loader=loader)
    assert isinstance(play, Play)
    play.populate_variable_manager(play_context=PlayContext(), variable_manager=variable_manager, all_vars=dict())

    tasks = play.get_tasks()
    assert len(tasks) == 7

    assert tasks[0].action == 'debug'
    assert tasks[1].action == 'debug'
    assert tasks[2].action == 'debug'
    assert tasks[3].action

# Generated at 2022-06-13 08:35:26.736767
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # init play
    play = Play()

    # append to tasks list
    play.tasks = list()
    # adding to tasks list
    play.tasks.append(Task())
    play.tasks.append(Task())
    play.tasks.append(Block())
    play.tasks.append(Task())
    play.tasks[-1].block = list()
    play.tasks[-1].block.append(Task())
    play.tasks[-1].rescue = list()
    play.tasks[-1].rescue.append(Task())
    play.tasks[-1].always = list()
    play.tasks[-1].always.append(Task())

    play.post_tasks = list()
    # adding to tasks list

# Generated at 2022-06-13 08:35:39.473482
# Unit test for constructor of class Play
def test_Play():
    p = Play()
    assert p.name is None
    assert isinstance(p, Play)


# Generated at 2022-06-13 08:35:47.312793
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play_ = Play()

    # Test schema of field 'tasks'
    assert play_.tasks is None

    # Test schema of field 'pre_tasks'
    assert play_.pre_tasks is None

    # Test schema of field 'post_tasks'
    assert play_.post_tasks is None

    # Test if it can run
    assert play_.get_tasks() is None


# Test class Play

# Generated at 2022-06-13 08:36:00.088656
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    # Test scenario: when vars_files is None, an empty list should be returned.
    p1 = Play()
    p1.vars_files = None
    ans1 = p1.get_vars_files()
    assert type(ans1) is list
    assert ans1 == []
    # Test scenario: when vars_files is not a list, a list containing vars_files should be returned.
    p2 = Play()
    p2.vars_files = './test_Play_get_vars_files'
    ans2 = p2.get_vars_files()
    assert type(ans2) is list
    assert ans2[0] == './test_Play_get_vars_files'
    # Test scenario: when vars_files is a list, a new list containing vars_files should be

# Generated at 2022-06-13 08:36:02.874608
# Unit test for method get_name of class Play
def test_Play_get_name():
    data = dict(
        name='test',
    )
    p = Play.load(data)
    assert p.get_name() == 'test'

 

# Generated at 2022-06-13 08:36:10.842703
# Unit test for method get_name of class Play
def test_Play_get_name():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    loader = DataLoader()

    context = PlayContext()

    ######################################################################################################
    #Initializing play object
    p = Play()
    p._loader = loader
    p._variable_manager = VariableManager()
    p._inventory = InventoryManager(loader=loader, sources='localhost,')
    p._tqm = None
    p._context = context
    p._ds = dict(hosts='localhost', name="Test")
    ######################################################################################################


# Generated at 2022-06-13 08:36:13.052204
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    p.compile()
    assert p.get_tasks() is not None

# Generated at 2022-06-13 08:36:24.951116
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    p = Play()
    data = dict(user='bob')
    processed_data = p.preprocess_data(data)
    assert 'user' not in processed_data
    assert processed_data['remote_user'] == 'bob'
    assert isinstance(processed_data, dict)

    # Error case 1
    data = []
    with pytest.raises(AnsibleAssertionError) as e:
        p.preprocess_data(data)
    assert 'while preprocessing data' in to_text(e.value)

    # Error case 2
    data = dict(user='bob')
    p._ds = dict(remote_user='joe')
    with pytest.raises(AnsibleParserError) as e:
        p.preprocess_data(data)

# Generated at 2022-06-13 08:36:33.040550
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    assert play.get_tasks() == []
    play.pre_tasks = [1, 2, 3]
    play.tasks = [4, 4, 4]
    play.post_tasks = [5, 6, 7]
    result = play.get_tasks()
    assert result == [1, 2, 3, 4, 4, 4, 5, 6, 7]
    play.tasks.append(Block())
    play.tasks[-1].block = [8, 9, 10]
    play.tasks[-1].rescue = [11, 11, 11]
    play.tasks[-1].always = [13, 14, 15, 16]
    result = play.get_tasks()

# Generated at 2022-06-13 08:36:44.375778
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    p = Play()
    play_roles_list = [
        {
            "roles": [
                {
                    "tasks": [
                        {"include_role": { "name": "my_role", "tasks_from": "main"}},
                        {"include_role": { "name": "my_role", "tasks_from": "handlers"}}
                    ]
                },
                {
                    "tasks": [
                        {"name": "check_fs_size", "include": "fs_size.yml"},
                        {"include_role": { "name": "my_role", "tasks_from": "main"}},
                        {"include_role": { "name": "my_role", "tasks_from": "handlers"}}
                    ]
                }
            ]
        }
    ]
    p._

# Generated at 2022-06-13 08:36:50.720593
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play_instance = Play()
    play_instance.pre_tasks = [Task(), Task(), Task()]
    play_instance.tasks = [Block(), Block(), Block()]
    play_instance.post_tasks = [Task(), Task(), Task()]
    actual = play_instance.get_tasks()
    expected = [Task(), Task(), Task(), Block(), Block(), Block(), Task(), Task(), Task()]
    assert_equal(actual, expected)

# Generated at 2022-06-13 08:37:09.378686
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    # Create a play using the Play.load() method, using a small subset of the example.yml file
    play_data = '''
---
    - hosts: local
      roles:
        - role: webserver
          name: ngix
          vars:
            - /var/log/nginx/nginx.log
          handlers:
            - name: restart webserver
              tags: restart
              service: name=nginx state=restarted
            - name: restart php
              tags: restart
              service: name=php state=restarted
          tasks:
            - name: install aptitude
              apt: pkg=aptitude state=present
            - name: install nginx
              apt: pkg=nginx state=present
              notify:
                - restart webserver
                - restart php
    '''
    play = Play.load

# Generated at 2022-06-13 08:37:20.984888
# Unit test for method compile_roles_handlers of class Play

# Generated at 2022-06-13 08:37:25.822620
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    # test with hosts as list
    play.hosts = ['127.0.0.1']
    assert play.get_name()=='127.0.0.1'
    # test with hosts as str
    play.hosts = '127.0.0.1'
    assert play.get_name()=='127.0.0.1'
    # test with no hosts
    play.hosts = ''
    assert play.get_name()==''

# Generated at 2022-06-13 08:37:32.104604
# Unit test for method get_name of class Play
def test_Play_get_name():
    play = Play()
    play.name = "test_play_name"
    assert play.get_name() == "test_play_name"
    play.name = None
    play.hosts = ["test_host"]
    assert play.get_name() == "test_host"
    play.hosts = ["test_host1", "test_host2"]
    assert play.get_name() == "test_host1,test_host2"

# Generated at 2022-06-13 08:37:35.373548
# Unit test for method get_name of class Play
def test_Play_get_name():
    # create Play
    play = Play()

    # set name
    play.name = 'testPlay'

    # check name
    assert play.get_name() == 'testPlay'


# Generated at 2022-06-13 08:37:41.944697
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    assert p.get_tasks() == []

    p.pre_tasks = [1,2,3]
    p.tasks = [4,5,6]
    p.post_tasks = [7,8,9]
    assert p.get_tasks() == [1,2,3,4,5,6,7,8,9]

# Generated at 2022-06-13 08:37:53.749173
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    import ansible.playbook.task as task
    import ansible.playbook.block as block
    testPlay = Play()
    t1 = task.Task()
    t2 = task.Task()
    t3 = task.Task()
    t4 = task.Task()
    b1 = block.Block()
    b2 = block.Block()
    b3 = block.Block()
    b4 = block.Block()
    b1.block = [t1]
    b2.block = [t2]
    b3.block = [t3, b4]
    b4.block = [t4]
    testPlay.pre_tasks = [t1, b1]
    testPlay.tasks = [t2, b2]
    testPlay.post_tasks = [t3, b3]


# Generated at 2022-06-13 08:38:04.586704
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    '''
    First creating a Play instance and specifying the roles. Next initializing the
    handlers for each role and adding the handlers to Play.handlers. Then the
    handlers are retrieved using the function and the handlers are compared
    with the expected handlers in a dictionary
    '''
    p = Play()
    role1 = Role()
    role2 = Role()
    role3 = Role()
    role4 = Role()
    role5 = Role()
    role1._role_name = 'role1'
    role2._role_name = 'role2'
    role3._role_name = 'role3'
    role4._role_name = 'role4'
    role5._role_name = 'role5'
    handlers =  ['handler1', 'handler2', 'handler3', 'handler4']
    role1.handlers = handlers

# Generated at 2022-06-13 08:38:09.701046
# Unit test for method preprocess_data of class Play
def test_Play_preprocess_data():
    play_obj = Play()
    data_obj = [{'name': 'ttt'}]
    result = play_obj.preprocess_data(data_obj)
    dict_result = dict(result)
    assert dict_result == {'name': 'ttt'}


# Generated at 2022-06-13 08:38:11.789802
# Unit test for method get_name of class Play
def test_Play_get_name():
    p = Play()
    p.name = 'play1'
    assert p.get_name() == 'play1'

# Test for method load

# Generated at 2022-06-13 08:38:37.283689
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    play.tasks = [{'name': 'No meta'}]
    play.post_tasks = [{'name': 'No meta'}]
    play.pre_tasks = [{'name': 'No meta'}]
    assert len(play.get_tasks()) == 3
    play.tasks = [{'name': 'No meta'}]
    play.post_tasks = [
        {
            'name': 'Meta',
            'meta': {
                'args': {}
            }
        }
    ]
    play.pre_tasks = [{'name': 'No meta'}]
    assert len(play.get_tasks()) == 4
    play.tasks = [{'name': 'No meta'}]

# Generated at 2022-06-13 08:38:44.782461
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    import builtins
    from ansiblelint.playbook.Playbook import Playbook

    # create a Play instance
    play = Play()

    # import the data to be used for the test
    play_data = """
    - hosts: localhost
      roles:
      - test_role
      tasks:
      - debug: var=hostvars[inventory_hostname]
    """

    # import the data to be used for the test
    role_data = """
    ---
    # Test Role
    - name: block one
      debug:
        msg: "block one"
      handlers:
        - name: handler one
          debug:
            msg: "handler one"
    """

    # convert the data to YAML using the built-in safe_load

# Generated at 2022-06-13 08:38:46.437796
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    pass

# Generated at 2022-06-13 08:38:49.442928
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    p = Play()
    assert p.get_tasks() == []
    assert p.get_tasks() == p.get_tasks()



# Generated at 2022-06-13 08:38:52.142063
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    play = Play()
    assert play.compile_roles_handlers() == []



# Generated at 2022-06-13 08:39:02.352035
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    from ansible.playbook.task import Task, TaskInclude
    from ansible.playbook.block import Block

    p = Play()
    iTask = TaskInclude()
    iTask.load({'name': 'include'})
    t = Task()
    t.load({'name': 'task'})
    b = Block()  # Block should be ignored

    # Get empty tasks
    result = p.get_tasks()
    assert not result

    # Pre tasks
    p.pre_tasks = [iTask, t]
    result = p.get_tasks()
    assert len(result) == 2
    assert isinstance(result[0], TaskInclude)
    assert isinstance(result[1], Task)

    # Main tasks
    p.tasks = [iTask, t]

# Generated at 2022-06-13 08:39:11.368214
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    play = Play()
    assert play.get_vars_files() == []
    # set vars_files to only one value
    play.vars_files = 'test1'
    assert play.get_vars_files() == ['test1']
    # set vars_files to multiple values
    play.vars_files = ['test1', 'test2']
    assert play.get_vars_files() == ['test1', 'test2']
    # set vars_files to None
    play.vars_files = None
    assert play.get_vars_files() == []


# Generated at 2022-06-13 08:39:12.578029
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    p = Play()
    p.compile_roles_handlers()

# Generated at 2022-06-13 08:39:15.275783
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    variable_manager = VariableManager()
    loader = DataLoader()
    play = Play(variable_manager, loader)
    play.vars_files = [
      'vars1.yml',
      'vars2.yml',
      'vars3.yml'
    ]
    expected_return = play.vars_files
    actual_return = play.get_vars_files()
    assert actual_return == expected_return



# Generated at 2022-06-13 08:39:16.090316
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    pass

# Generated at 2022-06-13 08:39:42.633206
# Unit test for method compile_roles_handlers of class Play
def test_Play_compile_roles_handlers():
    p = Play()
    p.load_data('roles:\n- test_role\n')
    result = p.compile_roles_handlers()
    assert result == [], result


# Generated at 2022-06-13 08:39:43.703226
# Unit test for method get_name of class Play
def test_Play_get_name():
    assert Play().get_name() == ''

# Generated at 2022-06-13 08:39:48.469873
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play.load(dict(
        name="test get tasks",
        hosts="localhost",
        become=False,
        become_user=None,
        gather_facts=False,
        tasks=[
            dict(name="show system", action=dict(module="shell", args="uname -a"))
        ]
    ))
    assert(len(play.get_tasks()) == 1)

# Generated at 2022-06-13 08:39:55.726594
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    play = Play()
    #play.tasks = [{"name":"test task1"},{"name":"test task2"}]
    play.pre_tasks = [{"name":"test pretask1"},{"name":"test pretask2"}]
    play.post_tasks = [{"name":"test posttask1"},{"name":"test posttask2"}]
    play.tasks = [{"name":"test task1"},{"name":"test task2"}]
    play.handlers = [{"name":"test handler1"},{"name":"test handler2"}]

    play.roles = [{"name":"test role1"},{"name":"test role2"}]
    #Test case 1: play object with non-empty task list should return tasks
    print("input: \n%s" % play.get_vars())

# Generated at 2022-06-13 08:39:59.363736
# Unit test for method get_name of class Play
def test_Play_get_name():
    """
    Test method get_name of class Play
    """
    test_obj = Play()
    test_obj.name = 'test'

    assert test_obj.get_name() == 'test'


# Generated at 2022-06-13 08:40:03.628671
# Unit test for method get_name of class Play
def test_Play_get_name():
    # Create a mock play object.
    config = {
        'name': 'test',
        'hosts': 'localhost',
        'roles': [],
        'tasks': [],
        'vars': [],
    }
    play = Play.load(config)
    assert play.get_name() == 'test'

# Generated at 2022-06-13 08:40:15.089239
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    variable_manager = VariableManager()

    play = Play()
    play.pre_tasks = [
        Task(dict(action='my_pre_task'))
    ]
    play.tasks = [
        Task(dict(action='my_task'))
    ]
    play.post_tasks = [
        Task(dict(action='my_post_task'))
    ]
    play.vars = dict(my_var='my_value')
    play.handlers = [
        Task(dict(action='my_handler'))
    ]
    play.roles = []
    play._variable_manager = variable_manager
    play.vars_files = []
    play.role_params = {}
    play.default_vars = {}
    play.session_vars = {}
    play.host_

# Generated at 2022-06-13 08:40:24.216879
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
    # test_Play_get_tasks_without_tasks_with_blocks
    test_play = Play()
    test_play.pre_tasks = [Block()]
    assert test_play.get_tasks() == [Block()]

    # test_Play_get_tasks_without_tasks_without_blocks
    test_play = Play()
    test_play.pre_tasks = []
    assert test_play.get_tasks() == []

    # test_Play_get_tasks_with_tasks_with_blocks
    test_play = Play()
    test_play.pre_tasks = [Block()]
    test_play.tasks = [Task()]
    assert test_play.get_tasks() == [Block(), Task()]

    # test_Play_get_tasks

# Generated at 2022-06-13 08:40:35.809435
# Unit test for method get_vars_files of class Play
def test_Play_get_vars_files():
    from ansible import errors

# Generated at 2022-06-13 08:40:39.343766
# Unit test for method get_tasks of class Play
def test_Play_get_tasks():
  play = get_Fixture_Play()
  play.tasks = [1,2,3]
  expected = [1,2,3]
  actual = play.get_tasks()
  assert expected == actual

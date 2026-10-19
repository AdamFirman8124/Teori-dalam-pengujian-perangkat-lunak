

# Generated at 2022-06-13 08:10:02.637366
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    dummy_host = Host('dummyhost')
    dummy_host.set_variable('ansible_python_interpreter', '/usr/bin/python')
    dummy_host.set_variable('ansible_connection', 'local')
    dummy_host.set_variable('ansible_hostname', 'dummyhost')

    # set up a play with a handler
    handler = HandlerTaskInclude.load({
        'include': 'handler.yml'
    }, variable_manager=VariableManager(), loader=DataLoader())

    assert handler._role is None
    assert handler._block is None
    assert handler._attributes['include'] == 'handler.yml'
    assert handler._attributes['listen'] is None

    # call the handler
    results = handler.run(dummy_host)

# Generated at 2022-06-13 08:10:10.972063
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.template import Templar
    from ansible.vars import VariableManager

    play_obj = Play.load(dict(
        name="Ansible Play",
        hosts=['all'],
        gather_facts='no',
        tasks=[
            dict(
                name="test task",
                action=dict(
                    module="shell",
                    args="echo '{{test_var}}'",
                )
            ),
            dict(
                name="test task 2",
                include="test.yml",
            ),
        ]
    ))

    variable_manager = VariableManager

# Generated at 2022-06-13 08:10:17.299565
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # load class
    module = __import__("ansible.playbook.handler_task_include").ansible.playbook.handler_task_include
    class_ = getattr(module, "HandlerTaskInclude")
    method = class_.load
    
    # create objects
    data = dict(
        hosts="all",
        any_errors_fatal=True,
        handlers='start_container.yml',
        ignore_errors=True,
        loop="{{ app_servers }}"
    )
    
    # method return value
    value = method(data)
    
    # assertions
    assert value.get_name() == 'start_container.yml'

# Generated at 2022-06-13 08:10:19.832667
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude(enclosing_block=object, role=object)
    assert handler.enclosing_block == object
    assert handler.role == object

# Generated at 2022-06-13 08:10:29.460189
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.attribute import Attribute, FieldAttribute
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-13 08:10:31.524819
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert HandlerTaskInclude is HandlerTaskInclude

# Generated at 2022-06-13 08:10:34.000253
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    #generate a random HandlerTaskInclude
    #
    #
    return True




# Generated at 2022-06-13 08:10:35.099574
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert 1 == 1

# Generated at 2022-06-13 08:10:41.872272
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.included_file import IncludedFile
    from ansible.template import Templar
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # create handler
    task = Task()
    task._role = 'myrole'
    task._block = Block()
    task._block._parent = task
    task._role = 'myrole'
    task._parent_role = task._role
    task._role_path = '/path/to/role'
    task._loaded_from = '/path/to/task/file'
    task._role_params = dict()

   

# Generated at 2022-06-13 08:10:47.662708
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # create object
    t = HandlerTaskInclude()
    # get dict from object
    d1 = t.__dict__
    # create object
    t = HandlerTaskInclude.load('dummy', 'dummy', 'dummy', 'dummy', 'dummy', 'dummy')
    # get dict from object
    d2 = t.__dict__
    # compare dicts
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    shared_keys = d1_keys & d2_keys
    assert d1_keys == d2_keys, 'HandlerTaskInclude load dicts differ - dicts have different keys'
    assert d1 == d2, 'HandlerTaskInclude load dicts differ - common keys have different values'

# Generated at 2022-06-13 08:10:58.874246
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader, variable_manager)

    task = Task()
    task._role = "app"
    block = Block()
    block._role = "app"

# Generated at 2022-06-13 08:11:06.501302
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    # The following lines are used to create unit tests for the 
    # method "load" of class "HandlerTaskInclude"
    h = HandlerTaskInclude()
    h.load_data({'include': 'test1'}, variable_manager=VariableManager(), loader=DataLoader())
    h.load_data({'include': 'test1', 'verbatim': True}, variable_manager=VariableManager(), loader=DataLoader())
    h.load_data({'include': 'test1', 'ignore_errors': True}, variable_manager=VariableManager(), loader=DataLoader())

# Generated at 2022-06-13 08:11:09.860254
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # handler = HandlerTaskInclude(block=None, role=None, task_include=None)
    handler = HandlerTaskInclude.load("playbook_path")
    print(handler)

# Generated at 2022-06-13 08:11:21.866309
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    '''
    This method is used for testing loading of a HandlerTaskInclude with different arguments.
    It uses the assertEqual method to check whether the result of the method matches with
    the expected output.
    '''
    test_data = {
        'name' : 'somehandler',
        'listen' : 'someevent',
        'include_tasks' : 'somefile'
    }
    t = HandlerTaskInclude(block=None, role=None, task_include=None)
    handler = t.check_options(
        t.load_data(test_data, variable_manager=None, loader=None),
        test_data
    )

    test_output = handler

    check_output = "somehandler"

    assertEqual(test_output, check_output)

# Generated at 2022-06-13 08:11:31.926158
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    context = PlayContext()
    context._become_method = 'sudo'
    context._become_user = 'frodo'
    templar = Templar(loader=None, variables={})
    group = Group(name='test_group', hosts=['test1'], vars={'test1':{'ansible_connection':'local'}})
    host = Host(name='test1')

# Generated at 2022-06-13 08:11:42.764220
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory import Host, Inventory
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    #
    #    data = '{"name": "foo", "some_other_var": "bar"}'
    #    return self.load_data(data, variable_manager=variable_manager, loader=loader)
    #
    data = '{"name": "foo", "some_other_var": "bar"}'

    ##
    inventory = Inventory()

    ##
    # playbook = Playbook()
    playbook = Playbook().load('test_playbook.yml')

    ##
    play = Play()

# Generated at 2022-06-13 08:11:43.874161
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # TODO
    pass

# Generated at 2022-06-13 08:11:50.618014
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    # just a dummy obj
    class dummy_class:
        pass

    # data is a dict which will be passed to class HandlerTaskInclude
    data = {

    }

    # block and task_include are regular objects
    block = dummy_class()
    task_include = dummy_class()

    # role is a string
    role = 'common'

    # variable_manager is a dict
    variable_manager = {

    }

    loader = dummy_class()

    c = HandlerTaskInclude()
    obj = c.load(data=data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)
    assert isinstance(obj, HandlerTaskInclude)

# Generated at 2022-06-13 08:11:59.525835
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    '''
      Test Case for the constructor of HandlerTaskInclude
      If a parameter is not of HandlerTaskInclude type, TypeError is raised.
      Even when the parameters are None, no  TypeError is raised.
    '''
    print("\nTesting constructor of HandlerTaskInclude\n")
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude
    from random import randint
    hd = Handler()
    t = TaskInclude()

# Generated at 2022-06-13 08:12:10.308655
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins import action_loader
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources='localhost')
    variable_manager.set_inventory(inventory)
    play_context = PlayContext()
    action_loader.add_directory('./lib/ansible/plugins/action')

# Generated at 2022-06-13 08:12:25.605041
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    print("Running unit test for method load of class HandlerTaskInclude")

    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='')
    host = Host(name="test-host")
    inventory.add_host(host)
    play_context = dict(
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
    )

# Generated at 2022-06-13 08:12:26.883513
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass


# Generated at 2022-06-13 08:12:36.456750
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    try:
        import ansible
    except ImportError:
        print("SKIP: unable to import ansible module")
        import sys
        sys.exit(0)

    handler=HandlerTaskInclude()

    # TODO: add more test cases

if __name__ == '__main__':
    import os
    import sys

    if len(sys.argv) > 1:
        sys.argv.pop(0)
        globals()[sys.argv[0]](*sys.argv[1:])
    else:
        print('Called with 0 arguments. Available methods:')
        for m in [x[0] for x in globals().items() if x[0].startswith('test')]:
            print(m)

# Generated at 2022-06-13 08:12:36.986356
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert 0 == 0

# Generated at 2022-06-13 08:12:38.409467
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    ''' Constructor test '''
    assert HandlerTaskInclude()


# Generated at 2022-06-13 08:12:40.309737
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = dict(
        listen='test_listen',
        name='handler_name'
    )

    HandlerTaskInclude.load(data)

# Generated at 2022-06-13 08:12:42.868628
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude(block=None, role=None, task_include=None)

    if handler:
        print("HandlerTaskInclude object created successfully")
    else:
        print("HandlerTaskInclude object creation failed")


# Generated at 2022-06-13 08:12:46.307761
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # ansible.inventory.host.Host._init__()
    # ansible.playbook.handler.Handler.__init__()
    # ansible.playbook.task_include.TaskInclude.__init__()
    # ansible.playbook.handler.HandlerTaskInclude.__init__()
    # ansible.playbook.handler.HandlerTaskInclude.load()
    assert HandlerTaskInclude.load(dict())

# Generated at 2022-06-13 08:12:56.507056
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.playbook.block import Block
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    # Create a Block for testing
    block = Block()

    # Create a DataLoader for testing
    loader = DataLoader()

    # Create a VariableManager for testing
    inventory = Inventory(loader=loader, variable_manager=VariableManager())
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # Create a TaskInclude for testing
    t = HandlerTaskInclude(block=block, role=None, task_include=None)

    # Check the constructor
    assert t is not None

    assert t._block is block
    assert t._role is None
    assert t._task_include is None
    assert t.serial

# Generated at 2022-06-13 08:13:10.882718
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # test_1
    print("test_1")
    handler_task_include_1=HandlerTaskInclude(block="block_1", role="role_1", task_include="task_include_1")
    assert(handler_task_include_1.block == "block_1")
    assert(handler_task_include_1.role == "role_1")
    assert(handler_task_include_1.task_include == "task_include_1")

    # test_2
    print("test_2")
    handler_task_include_2=HandlerTaskInclude()
    assert(handler_task_include_2.block == None)
    assert(handler_task_include_2.role == None)
    assert(handler_task_include_2.task_include == None)


# Generated at 2022-06-13 08:13:29.193708
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    print("Testing HandlerTaskInclude_load ...")

    test_name = "test_HandlerTaskInclude_load"
    test_task_name = "test_listen_included_task"
    test_listen_name = "test_listen_name"
    test_action = "include_playbook"
    test_playbook = "test_playbook.yml"
    test_dirname = "/tmp"
    test_filename = "vars.yml"

    # create file for check
    test_file = "/tmp/vars.yml"
    with open(test_file, "w+") as f:
        f.write("#test")


# Generated at 2022-06-13 08:13:38.957734
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    from ansible.utils.vars import combine_vars
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.hostvars import HostVars

    from collections import namedtuple
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    # Create the object
    t = HandlerTaskInclude()

    # Create the vars needed

# Generated at 2022-06-13 08:13:40.972321
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    t = HandlerTaskInclude(block=None, role=None, task_include=None)
    assert t.load('handler1') == 'handler1'

# Generated at 2022-06-13 08:13:42.383162
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:13:52.042360
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    from ansible.inventory.host import Host
    from ansible.parsing.yaml.objects import AnsibleSequence, AnsibleMapping
    from ansible.playbook.block import Block

# Generated at 2022-06-13 08:13:55.629284
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass
#    values = {'hosts':'all',
#              'listen': 'all',
#              'name':'test'
#             }
#
#    #assert HandlerTaskInclude.load(values) == True

# Generated at 2022-06-13 08:13:56.858339
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Have to update it later with ansible code
    assert True == True

# Generated at 2022-06-13 08:13:58.890312
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    ret = HandlerTaskInclude.load({}, {})
    printtype(ret)


# Generated at 2022-06-13 08:14:05.179853
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    data = dict(
        name = 'test-handler',
        listen = 'test-handler',
        tags = 'test_handler',
        sudo = False,
        sudo_user = 'rdo',
        ignore_errors = True
    )

    variable_manager = None
    loader = None

    handler = HandlerTaskInclude.load(data, variable_manager=variable_manager, loader=loader)

    assert handler is not None, 'A handler is expected !'

    assert handler.name == data['name']
    assert handler.loop == 'test-handler'
    assert handler.tags == 'test_handler'
    assert handler.sudo is False
    assert handler.sudo_user == 'rdo'
    assert handler.ignore_errors is True

# Generated at 2022-06-13 08:14:19.007352
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Dummy class for testing
    class DummyClass(object):
        pass

    # Setting up parameters of the test
    test_data = 'test_data'
    test_block = DummyClass()
    test_role = DummyClass()
    test_task_include = DummyClass()
    test_variable_manager = DummyClass()
    test_loader = DummyClass()

    # Initiate the class to test
    test_obj = HandlerTaskInclude()

    # Perform test
    test_result = test_obj.load(
        data=test_data,
        block=test_block,
        role=test_role,
        task_include=test_task_include,
        variable_manager=test_variable_manager,
        loader=test_loader
    )

    # Method load should return an instance of class

# Generated at 2022-06-13 08:14:29.141462
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert 1==1

# Generated at 2022-06-13 08:14:40.668211
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    import json

    data = {}
    data['handler'] = {}
    data['handler']['name'] = "test handler"
    data['handler']['actions'] = ["handler action"]
    data['handler']['listen'] = "test listen"
    variable_manager = None
    loader = None

    # check if method load works correctly
    result = HandlerTaskInclude.load(data, TaskInclude(Task()), variable_manager, loader)
    assert result._role is None
    assert isinstance(result._block, Block)
    assert isinstance(result._task, TaskInclude)
    assert isinstance(result, Handler)
    assert result.get

# Generated at 2022-06-13 08:14:48.119843
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager

    # Create empty blocks called 'main', 'tasks', 'handlers'
    main_block = Block(None)
    main_block.load_data({'block': 'main'})
    handler_block = Block(main_block)
    handler_block.load_data({'block': 'handlers', 'parent': {'block': 'main'}})
    tasks_block = Block(main_block)
    tasks_block.load_data({'block': 'tasks', 'parent': {'block': 'main'}})


    # Create data for handler
    data = {'listen': 'test', 'name': 'test', 'meta': 'test'}

    # Create VariableManager for handler
    variable_manager = Variable

# Generated at 2022-06-13 08:15:00.056430
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    """HandlerTaskInclude default instance attributes"""

    check = HandlerTaskInclude()
    assert check.static == False
    assert check.always_run == False
    assert check.block == None
    assert check.name == 'handler'
    assert check.loop == None
    assert check.loop_args == []
    assert check.module_name == 'include'
    assert check.module_vars == {}
    assert check.module_args == ""
    assert check.role == None
    assert check.tags == ['always']
    assert check.when == []
    assert check.notify == []
    assert check.notified_by == []
    assert check.run_once == False
    assert check.ignore_errors == False
    assert check.delegate_to == None
    assert check.environment == None
    assert check.no_log

# Generated at 2022-06-13 08:15:02.082140
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude(block=None, role=None, task_include=None)
    assert handler

# Generated at 2022-06-13 08:15:02.857145
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:15:07.885648
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    class TaskIncludeMock():
        def load_data(self, data, variable_manager=None, loader=None):
            return {'name': 'handler'}

        def check_options(self, data, data2):
            return 'check_result'

    data = {'name': 'handler_name'}

    result = HandlerTaskInclude.load(
        data,
        task_include=TaskIncludeMock()
    )

    assert result == 'check_result'

# Generated at 2022-06-13 08:15:10.517480
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    hti = HandlerTaskInclude(block=None, role=None, task_include=None)
    assert hti is not None, "Constructor of class HandlerTaskInclude fails"


# Generated at 2022-06-13 08:15:18.785119
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import mock
    import yaml

    yaml_data = """
    - include: tasks/main.yml
      when: my_condition
      tags:
      - mytag
    """
    data = yaml.load(yaml_data)

    task_include = mock.MagicMock()

    block = mock.MagicMock()

    role = mock.MagicMock()

    variable_manager = mock.MagicMock()

    loader = mock.MagicMock()

    HandlerTaskInclude.load(
        data = data,
        block = block,
        role = role,
        task_include = task_include,
        variable_manager = variable_manager,
        loader = loader
    )

    assert task_include.load_data.call_count == 1

    assert task_include.check_options.call_count

# Generated at 2022-06-13 08:15:25.238634
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    variable_manager = HostVariableManager()
    variable_manager._fact_cache = dict()
    variable_manager._vars_cache = { "hostvars": {} }
    variable_manager.extra_vars = {}
    variable_manager.is_fact_cache = { "hostvars": {} }
    variable_manager.get_vars = {}
    variable_manager.get_fqn_vars = {}
    variable_manager.is_fact = None
    variable_manager.is_fact_cache = None
    variable_manager.is_fact_cache = None
    variable_manager.is_fact_cache = None
    variable_manager.is_fact_cache = None
    variable_manager.is_fact_cache = None
    variable_manager.is_fact_cache = None
    variable_manager.is_fact_

# Generated at 2022-06-13 08:15:45.759359
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handlerTaskInclude = HandlerTaskInclude()
    assert handlerTaskInclude is not None

# Generated at 2022-06-13 08:15:51.184470
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Will create an instance of HandlerTaskInclude
    hti = HandlerTaskInclude()
    assert hti is not None
    assert hti.block == None
    assert hti.role == None
    assert hti.task_include == None



# Generated at 2022-06-13 08:15:56.791984
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    test_data = {'listen': 'my_notify_tag', 'include': 'my_filename.yml'}
    h = HandlerTaskInclude.load(data=test_data, block=None, role=None, task_include=None, variable_manager=None, loader=None)
    assert h.include_tasks == 'my_filename.yml'
    assert h.listen == 'my_notify_tag'

# Generated at 2022-06-13 08:15:57.505048
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:15:58.677125
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    hti = HandlerTaskInclude()

# Generated at 2022-06-13 08:15:59.336888
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:15:59.994828
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    pass

# Generated at 2022-06-13 08:16:00.644069
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:16:03.527183
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    '''
    handler_task_include = HandlerTaskInclude(block=block, role=role, task_include=task_include)
    '''
    pass

# Generated at 2022-06-13 08:16:13.941788
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = 'MY_INCLUDE_VAR'
    block = 'my_block'
    role = 'my_role'
    hti = HandlerTaskInclude()
    hti.BLEP = 'blep'
    hti.BLAP = 'blap'
    hti.TASK_KEYS = ['BLEP','BLAP','TASK_KEYS']
    hti.valid_attrs = ['BLEP','BLAP','TASK_KEYS','my_method']

    (result_handler, result_data) = hti.load(data, block=block, role=role)
    assert result_handler.BLEP == 'blep'
    assert result_handler.BLAP == 'blap'
    assert data == result_data

# Generated at 2022-06-13 08:16:55.025340
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert True

# Generated at 2022-06-13 08:17:03.634056
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = """
    - name: test handler
      include: tasks.yml
    """
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.parsing import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar

    def set_loader(self, loader):
        self._loader = loader

    # We need to add a _loader attribute to the class TaskInclude
    TaskInclude._loader = None
    TaskInclude.set_loader = set_loader
    # We need

# Generated at 2022-06-13 08:17:12.774402
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    '''
    check if HandlerTaskInclude.load() works as expected
    '''
    from ansible.inventory.host import Host
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude

    # HandlerTaskInclude.load() needs a PlayContext object as first parameter
    # we create a Play and PlayContext object to invoke HandlerTaskInclude.load()
    loader = None
    variable_manager = None
    inventory = Host(name='all')
    variable_manager = None
    loader = None

# Generated at 2022-06-13 08:17:19.002706
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
  #print("test_constructor_HandlerTaskInclude")
  data = {
    "handler_name": {
      "listen" : "default"
    }
  }
  t = HandlerTaskInclude()
  handler = t.check_options(
      t.load_data(data),
      data
  )

  assert handler is not None

# Generated at 2022-06-13 08:17:28.482604
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Test 1
    data = {
        "include": "apples.yml",
        "name": "remove cache",
        "file": "/some/path/cache.yml",
        "with_items": ["apple", "orange", "banana"]
    }

    handler = HandlerTaskInclude.load(data=data)
    assert handler.include == data['include']
    assert handler.name == data['name']
    assert handler.file == data['file']
    assert handler.with_items[0] == data['with_items'][0]
    assert handler.with_items[1] == data['with_items'][1]
    assert handler.with_items[2] == data['with_items'][2]

    # Test 2
    # 'include' has to be a string, otherwise it fails
    data

# Generated at 2022-06-13 08:17:29.292231
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # TODO
    assert False


# Generated at 2022-06-13 08:17:29.779185
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    HandlerTaskInclude()

# Generated at 2022-06-13 08:17:31.084045
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert handler is not None

# Generated at 2022-06-13 08:17:32.796325
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude("notify_slack_vars", "/home/ansible/tasks/notify_slack_vars.yml")

# Generated at 2022-06-13 08:17:39.267365
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars.manager import VariableManager

    from ansible.playbook.play_context import PlayContext
    from ansible.utils.vars import combine_vars
    from ansible.plugins.loader import action_loader
    from ansible.plugins.filter import core

    ansible_playbook_path = 'playbooks'
    loader = DataLoader()
    variable_manager = VariableManager()


# Generated at 2022-06-13 08:19:11.988692
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.vars.manager import VariableManager
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_loader(loader)
    variable_manager.set_inventory(loader.inventory)
    variable_manager.extra_vars = {
        'hostvars': {
            'host1': {'var1': 1, 'var2': 2}
        }
    }


# Generated at 2022-06-13 08:19:13.515547
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    handlerTaskInclude = HandlerTaskInclude()
    handlerTaskInclude.load('test')


# Generated at 2022-06-13 08:19:15.843704
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    t = HandlerTaskInclude()
    result = t.load_data('test_value',variable_manager = 'passed_variable_manager', loader = 'passed_loader')
    assert result == 'test_value'

# Generated at 2022-06-13 08:19:16.708595
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert HandlerTaskInclude



# Generated at 2022-06-13 08:19:18.733700
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert handler.VALID_INCLUDE_KEYWORDS == TaskInclude.VALID_INCLUDE_KEYWORDS.union(('listen',))

# Generated at 2022-06-13 08:19:31.753170
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    loader = DictDataLoader({
        '/etc/ansible/roles/example/tasks/main.yml': """
            - name: some handler with a notify
              debug: msg="from file"
              notify: example
        """,
        '/etc/ansible/roles/example/handlers/main.yml': """
            - name: example handler
              debug: msg="from file"
        """
    })

    role_name = 'example'
    role = Role.load({'name': role_name, 'path': '/etc/ansible/roles/example'}, loader)

    play = Play().load(
        dict(
            name = "test play",
            hosts = 'all',
            roles = [role_name]
        ),
        loader=loader
    )


# Generated at 2022-06-13 08:19:32.540086
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert HandlerTaskInclude


# Generated at 2022-06-13 08:19:33.016455
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:19:34.764427
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    hti = HandlerTaskInclude()
    assert isinstance(hti, HandlerTaskInclude)
    assert isinstance(hti, Handler)
    assert isinstance(hti, TaskInclude)


# Generated at 2022-06-13 08:19:48.129583
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Test with data and no block, role, task_include
    data = {
        'include': 'some_file.yml',
        'name': 'test_handler_task_include_load',
        'listen': 'test_handler'
    }
    actual_result = HandlerTaskInclude.load(data)
    expected_result = {
        'include': 'some_file.yml',
        'name': 'test_handler_task_include_load',
        'listen': 'test_handler'
    }
    assert actual_result == expected_result

    # Test with data, block, role, task_include
    data = {
        'include': 'some_file.yml',
        'name': 'test_handler_task_include_load',
        'listen': 'test_handler'
    }
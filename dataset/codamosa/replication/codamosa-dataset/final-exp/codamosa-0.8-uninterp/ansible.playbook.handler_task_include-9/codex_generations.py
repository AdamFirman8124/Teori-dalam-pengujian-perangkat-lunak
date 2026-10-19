

# Generated at 2022-06-13 08:10:09.456743
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Import test module
    import ansible.parsing.yaml.objects

    # Create an instance of class AnsibleLoader
    loader = ansible.parsing.dataloader.DataLoader()

    # Create an instance of class VariableManager
    variable_manager = ansible.vars.manager.VariableManager()

    # Create an instance of class TaskInclude
    task_include = ansible.playbook.task_include.TaskInclude()

    # Create a dictionary
    data = dict(
        include='test'
    )

    # Create an instance of class HandlerTaskInclude
    handler_task_include = HandlerTaskInclude.load(
        data=data,
        task_include=task_include,
        variable_manager=variable_manager,
        loader=loader
    )

    # Create an instance of class Ansible

# Generated at 2022-06-13 08:10:17.193187
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    class TestHandlerTaskInclude(HandlerTaskInclude):

        def __init__(self, *args, **kwargs):
            self.data = None
            self.args = args
            self.kwargs = kwargs

        def load_data(self, data, *args, **kwargs):
            self.data = data
            self.args = args
            self.kwargs = kwargs
            return data

        def _load_tasks(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            return dict()

        def _load_handlers(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            return dict()

        def get_vars(self, *args, **kwargs):
            return

# Generated at 2022-06-13 08:10:19.017034
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data={'include': 'bar.yml'}
    assert HandlerTaskInclude.load(data) is not None

# Generated at 2022-06-13 08:10:22.904950
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    data = {
        'name': 'test handler',
        'listen': 'test handler'
    }
    assert HandlerTaskInclude.load(data)

# Generated at 2022-06-13 08:10:23.996768
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    '''
    Loader tests should produce handlers, not just check that they work, and not just check that they fail.
    '''
    assert(False)


# Generated at 2022-06-13 08:10:24.699474
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Load function in HandlerTaskInclude class

# Generated at 2022-06-13 08:10:35.449820
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    import os
    import sys

    # load the test data
    # test_data_dir = os.path.dirname(os.path.realpath(__file__)) + '/../../lib/ansible/inventory/'
    test_data_dir = os.path.dirname(os.path.realpath(__file__)) + '/../../lib/ansible/plugins/callback/'
    data = yaml.load(open(test_data_dir + '/disk.yml').read())

    # make a dictionary (ansible expects it to be a dictionary)
    variables = dict()
    variables['hosts'] = 'localhost'

    # creates a task include object
    task_include = HandlerTaskInclude(block=None, role=None, task_include=None)

# Generated at 2022-06-13 08:10:43.641399
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    task_include = None
    data = {
        'file': 'boobies',
        'tags': ['one', 'two'],
    }

    handler = HandlerTaskInclude.load(data, task_include)
    assert handler.task_blocks == ['boobies']
    assert handler.tags == ['one', 'two']
    assert handler.any_errors_fatal == False
    assert handler.first_available_file == True

    data = {
        'files': ['boobies', 'boobies2'],
        'tags': ['one', 'two'],
        'any_errors_fatal': True,
        'first_available_file': True,
    }

    handler = HandlerTaskInclude.load(data, task_include)

# Generated at 2022-06-13 08:10:44.334371
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass


# Generated at 2022-06-13 08:10:53.187415
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['inventory_hosts'])
    variable_manager.set_inventory(inventory)

    handler_task_include_instance = HandlerTaskInclude(block=None, role=None, task_include=None)

    handler_task_include_instance.load(data='handler_file', variable_manager=variable_manager, loader=loader)
    # handler_task_include_instance.load(data='handler_file', variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 08:11:05.106270
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    block = Block(
        role=None,
        tasks=[],
        handlers=[],
        always_run=False,
        vars_prompt=None,
        variability=None,
        name=None,
        parent_block=None,
        run_once=False,
        task_include=None,
        rescue=None,
        always=None,
    )

# Generated at 2022-06-13 08:11:08.729692
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude(block=None, role=None, task_include=None)
    assert isinstance(handler, HandlerTaskInclude)
    return handler

# Generated at 2022-06-13 08:11:20.077824
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    w_data = dict(
        name="name",
        action=dict(
            module='debug',
            args=dict(
                a1=1,
                a2=2
            ),
        ),
    )
    w_handler = HandlerTaskInclude(
        block=None,
        role=None,
        task_include=None
    )
    handler = HandlerTaskInclude.load(
        data=w_data,
        block=None,
        role=None,
        task_include=None,
        variable_manager=None,
        loader=None
    )
    assert handler.__dict__ == w_handler.__dict__

# Generated at 2022-06-13 08:11:28.723988
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory import Inventory
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.extra_vars = {'ini_path': 'tests/unit/inventory/'}
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=['localhost'])
    play = Play.load(dict(
        name="Ansible Play",
        hosts='localhost',
        gather_facts='no',
        tasks=[
            dict(name="Task 1", debug=dict(var='hostvars')),
            dict(action=dict(module="setup"), register="setup_results")
        ]
    ), variable_manager=variable_manager, loader=loader)
   

# Generated at 2022-06-13 08:11:30.565802
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    t = HandlerTaskInclude()
    assert t is not None

# Generated at 2022-06-13 08:11:41.383456
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager

    loader = None

    host = Host(
        name='localhost',
        port=22,
        variables={'foo': 1, 'bar': 2}
    )

    variable_manager = VariableManager(
        loader=loader,
        inventory=Inventory(hosts=[host])
    )


# Generated at 2022-06-13 08:11:46.094772
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_include = HandlerTaskInclude(block=None, role=None, task_include=None)
    assert handler_include._task is None
    assert handler_include._block is None
    assert handler_include._role is None
    assert handler_include._static is False
    assert handler_include._metadata is None
    assert handler_include._ds is None



# Generated at 2022-06-13 08:11:53.303612
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # Call class HandlerTaskInclude with just one argument , for the list of
    # arguments and types see HandlerTaskInclude.load
    h = HandlerTaskInclude()
    # Check that HandlerTaskInclude has the attributes of
    # its parent class Handler
    assert h.__dict__.has_key('_block')
    assert h.__dict__.has_key('_role')
    assert h.__dict__.has_key('_task_include')
    assert h.__dict__.has_key('_attributes')
    assert h.__dict__.has_key('_notified_by')
    assert h.__dict__.has_key('_listening_to')
    assert h.__dict__.has_key('_loop')
    assert h.__dict__.has_key('_loop_args')


# Generated at 2022-06-13 08:12:06.223547
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.playbook.handler import Handler
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.template import Templar
    from ansible.vars import VariableManager

    # We need to set a host for the VariableManager
    variable_manager = VariableManager()
    variable_manager.set_inventory(Host(name='dummy'))
    templar = Templar(loader=None, variables=variable_manager)
    handler_task_include = TaskInclude.load(None, block=None, role=None, task_include=None,
                                            variable_manager=variable_manager, loader=None)
    assert isinstance(handler_task_include, HandlerTaskInclude)

# Generated at 2022-06-13 08:12:07.944572
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():

    task_include = HandlerTaskInclude(block=None, role=None, task_include=None)
    assert task_include is not None

# Generated at 2022-06-13 08:12:12.446517
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # load method of HandlerTaskInclude class is tested in test_playbook.py
    # test the 'load' method unique to the HandlerTaskInclude class
    pass

# Generated at 2022-06-13 08:12:22.062872
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()
    hosts = ['localhost']
    variable_manager = VariableManager()
    inventory = [Group('all', hosts)]
    variable_manager.set_inventory(inventory)
    block = {'block': 'block'}
    role = {'role': 'role'}
    handler_data = {'hosts': 'all', 'listen': 'all'}

    handler = HandlerTaskInclude.load(
        handler_data,
        block,
        role,
        variable_manager=variable_manager,
        loader=loader,
    )

    # class of object handler and attributes

# Generated at 2022-06-13 08:12:25.736285
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    test_handler_task_include = HandlerTaskInclude(block='block', role='role', task_include='task_include')
    assert test_handler_task_include.block == 'block'
    assert test_handler_task_include.role == 'role'
    assert test_handler_task_include.task_include == 'task_include'


# Generated at 2022-06-13 08:12:35.021213
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.playbook.task_include import TaskInclude
    assert issubclass(HandlerTaskInclude, TaskInclude) == True

    from ansible.playbook.handler import Handler
    assert issubclass(HandlerTaskInclude, Handler) == True

    #Variables from TaskInclude
    from ansible.playbook.task import Task
    assert issubclass(TaskInclude, Task) == True

    VALID_INCLUDE_KEYWORDS = Task.VALID_TASK_KEYWORDS.union(('listen',))
    assert HandlerTaskInclude.VALID_INCLUDE_KEYWORDS == VALID_INCLUDE_KEYWORDS

# Generated at 2022-06-13 08:12:43.445092
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    h = HandlerTaskInclude.load({
            'include': 'include_playbook.yml',
            'name': 'This is a handler'
        }
    )

    assert h.get_name() == 'This is a handler'
    assert isinstance(h.static_tasks(), list)
    assert h.static_tasks()[0].get_name() == 'This is a handler'
    assert isinstance(h.static_tasks()[0].get_action(), str)
    assert h.static_tasks()[0].get_action() == 'include_playbook.yml'

    h = HandlerTaskInclude.load({
            'include': 'include_playbook.yml',
            'name': 'This is a handler',
            'listen': 'handlers'
        }
    )

   

# Generated at 2022-06-13 08:12:44.579826
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = {'name': 'test'}
    task_include = HandlerTaskInclude.load(data)
    assert task_include.name == 'test'

# Generated at 2022-06-13 08:12:45.286095
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:12:55.713908
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    import pytest
    import os

    grp = Group()
    grp.hosts.add(Host(name='host1.example.com', port=22))
    grp.hosts.add(Host(name='host2.example.com', port=22))
    groups = { 'all' : grp}

    data = dict()
    data['listen'] = 'all'
    data['tasks'] = [{
        'name': 'Task 1',
        'debug': 'msg=My first task with ansible'
    }]

    task_include = dict()
    v = VariableManager()

# Generated at 2022-06-13 08:13:10.034633
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inject import InventoryScript
    from ansible.parsing.dataloader import DataLoader

    play_source =  dict(
            name = "Ansible Play 0",
            hosts = 'webservers',
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module='debug', args=dict(msg='Hello World!'))),
                dict(action=dict(module='shell', args='echo "goodbye"'))
                ]
            )


# Generated at 2022-06-13 08:13:10.890088
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert 0

# Generated at 2022-06-13 08:13:25.234263
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Test for method load of class HandlerTaskInclude with parameters and
    # attributes:
    data = {'tags': ['foo', 'bar'], 'include': 'myplay.yml'}
    t = HandlerTaskInclude(block=None, task_include=None)
    handler = t.check_options(t.load_data(data, variable_manager=None, loader=None), data)
    assert handler._attributes['tags'] == ['foo', 'bar']
    assert handler._attributes['include'] == 'myplay.yml'



# Generated at 2022-06-13 08:13:31.855901
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # Args of constructor
    block = 'dummy'
    role = 'dummy'
    task_include = 'dummy'

    # Create an object of HandlerTaskInclude class
    obj = HandlerTaskInclude(block, role, task_include)

    # Check if the object is an instance of HandlerTaskInclude class
    assert isinstance(obj, HandlerTaskInclude)

    # Select an arbitrary attribute of HandlerTaskInclude class
    assert obj._attribute == None

# Generated at 2022-06-13 08:13:40.256277
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    hti = HandlerTaskInclude()
    t = hti.load_data({"include": "abcd.yml"})
    assert t.name == 'abcd.yml'
    t = hti.load_data({"include": "role1, role2"})
    assert t.name == 'role1, role2'
    t = hti.load_data({"include": "role1, role2, role3, role4"})
    assert t.name == 'role1, role2, role3, role4'

# Generated at 2022-06-13 08:13:40.800891
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:13:48.077544
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # constructor (task_include.py)
#     def __init__(self, block=None, role=None, task_include=None):
#         self._task = None
#         TaskInclude.__init__(self, block=block, role=role, task_include=task_include)
    handler_task_include = HandlerTaskInclude()
    assert handler_task_include._task == None
    assert handler_task_include._parent == None
    assert handler_task_include._role == None



# Generated at 2022-06-13 08:13:50.695281
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass
#    include = HandlerTaskInclude()
#    assert include.load(
#        {
#            'name': 'test_HandlerTaskInclude_load'
#        }
#    )

# Generated at 2022-06-13 08:13:52.339887
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert HandlerTaskInclude.load("test_HandlerTaskInclude_load") == None


# Generated at 2022-06-13 08:13:52.830934
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:14:02.026217
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    inv_mgr = InventoryManager(loader=loader, sources=None)
    var_mgr = VariableManager(loader=loader, inventory=inv_mgr)
    handler = HandlerTaskInclude.load({"include": "foobar.yml"},
                                      task_include=TaskInclude.load({"include": "foobar.yml"}, block=None, role=None, task_include=None),
                                      variable_manager=var_mgr)
    assert isinstance(handler, HandlerTaskInclude)


# Generated at 2022-06-13 08:14:09.441662
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = [{
        'name' : 'foo',
        'include' : 'otherfile.yaml'
    }]

    t = HandlerTaskInclude(block=None, role=None, task_include=None)

    handler = t.check_options(
        t.load_data(data, variable_manager=None, loader=None),
        data
    )

    assert(handler.name == 'foo')
    assert(handler.static_include == 'otherfile.yaml')

# Generated at 2022-06-13 08:14:28.544247
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible import constants as C
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext

    inventory = InventoryManager(loader=DataLoader(), sources="tests/inventory")
    variable_manager = inventory.get_variable_manager()

    play_context = PlayContext()

    data = {}
    data['action'] = 'notify'
    data['name'] = 'handler_name'
    data['listen'] = 'task_name'

    block = Block([], play_context=play_context)
    block.name = 'TestBlock'
    task_include = HandlerTaskInclude()

# Generated at 2022-06-13 08:14:39.756937
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.playbook.hosts import Hosts
    from ansible.playbook.play import Play
    from ansible.playbook.included_file import IncludedFile

    host_vars = {'ansible_python_interpreter':"/usr/bin/python"}
    host = Host(
        name="test-host",
        vars=host_vars,
        groups=['group1']
    )
    host.set_variable_manager(VariableManager(loader=DictDataLoader()))

    host_vars1 = {'ansible_python_interpreter':"/usr/bin/python1"}

# Generated at 2022-06-13 08:14:47.637121
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    #Initialization of Ansible inventory object for unit test
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.init import Inventory

    group1 = Group('host1_group')
    group2 = Group('host2_group')
    h1 = Host('host1', groups=[group1, group2])
    h2 = Host('host2', groups=[group1])
    h3 = Host('host3', groups=[group2])
    h4 = Host('host4', groups=[group1])
    h5 = Host('host5', groups=[group2])

    inv = InventoryManager([])
    inv.add_group(group1)
    inv.add_group(group2)

# Generated at 2022-06-13 08:14:57.298509
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    # Create a sample task include
    task_include = {
        'name' : 'test_name',
        'hosts' : 'test_hosts',
        'tasks' : 'test_tasks',
        'listen' : 'test_listen'
    }

    # Initialize the handler
    handler = HandlerTaskInclude.load(
        task_include,
        variable_manager=None,
        loader=None
    )

    # Validate the task_include
    assert isinstance(handler, HandlerTaskInclude)
    assert handler.name == 'test_name'
    assert handler.tasks == 'test_tasks'
    assert handler._static is True

# Generated at 2022-06-13 08:15:01.417486
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.inventory.host import Host
    host = Host(name="testHost")
    handler = HandlerTaskInclude(host=host, task=TaskInclude(0,0))
    assert handler.name == "testHost"

# Generated at 2022-06-13 08:15:05.040675
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    try:
        t = HandlerTaskInclude()
    except NameError:
        print ("Constructor does not exist")
    else:
        print ("Constructor exists")


# Generated at 2022-06-13 08:15:07.644329
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import yaml
    data = yaml.load("""
        - include: test_include.yml
          tags: included
        """)
    handler = HandlerTaskInclude.load(data)
    assert isinstance(handler, HandlerTaskInclude)

# Generated at 2022-06-13 08:15:11.869697
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    task_include = TaskInclude.load(data={'include': 'playbook'})
    handler = Handler.load(
        data={'listen': 'test-handler'},
        block=None,
        role=None,
        task_include=task_include,
        variable_manager=None,
        loader=None
    )
    assert handler.get_name() == 'test-handler'

# Generated at 2022-06-13 08:15:12.863145
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    handler = HandlerTaskInclude({})
    assert handler

# Generated at 2022-06-13 08:15:18.913830
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar

    # Create a valid list of included tasks
    included_tasks = []
    for i in range(10):
        task = Task()
        task._role_name = 'TEST_ROLE'
        task._task_name = 'TEST_TASK_' + str(i)
        included_tasks.append(task)

    # Create a valid included file
    included_file = Ansible

# Generated at 2022-06-13 08:15:41.801732
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    _data = {'include': 'apache_conf.yml'}
    _loader = "dummy"
    _variable_manager = "dummy"
    t = HandlerTaskInclude()
    h = t.load(_data, loader=_loader, variable_manager=_variable_manager)
    assert h is not None

# Generated at 2022-06-13 08:15:43.646083
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude(block=None, role=None, task_include=None)

# Generated at 2022-06-13 08:15:45.918550
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-13 08:15:57.300822
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inventory_manager = InventoryManager()

    # Create main group
    main_group = Group(inventory=inventory_manager.inventory,
                       name='main_group')

    # Add main group to inventory
    inventory_manager.inventory.add_group(main_group)

    # Create child group
    child_group = Group(inventory=inventory_manager.inventory,
                        name='child_group',
                        parents=[main_group])

    # Add child group to inventory
    inventory_manager.inventory.add_group(child_group)

    # Create host in child group
    host = inventory_manager.inventory.get_host('localhost')

# Generated at 2022-06-13 08:15:59.390368
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    task_t = HandlerTaskInclude()
    assert isinstance(task_t,HandlerTaskInclude)

# Generated at 2022-06-13 08:16:01.846588
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert issubclass(HandlerTaskInclude, Handler)
    assert issubclass(HandlerTaskInclude, TaskInclude)


# Generated at 2022-06-13 08:16:12.784310
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.template import Templar
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.role import Role
    from ansible.errors import AnsibleParserError
    from ansible.plugins.loader import find_plugin
    loader = DataLoader()


# Generated at 2022-06-13 08:16:13.522353
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:16:15.582714
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = {'name':'test', 'tags': {'name': 'test'}}
    handler = HandlerTaskInclude.load(data=data)
    print(handler)

# Generated at 2022-06-13 08:16:20.153397
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    h = HandlerTaskInclude()

    class FakeVm(object):
        def set_host_variable(self, host, var_name, var_value):
            pass

    v = FakeVm()

    h.load({
        'listen': 'failed',
        'name': 'test',
        'include': 'main.yml'
    }, variable_manager=v)
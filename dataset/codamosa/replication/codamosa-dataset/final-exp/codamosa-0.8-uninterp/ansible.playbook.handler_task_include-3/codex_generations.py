

# Generated at 2022-06-13 08:10:07.094676
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(),
            include_vars=dict(aliases=['include_var']),
            include_tasks=dict(aliases=['include_task']),
            include_with=dict(aliases=['include_when']),
            include_role=dict(aliases=['include_rol']),
        )
    )
    result = HandlerTaskInclude.load(data=module.params)
    module.exit_json(ansible_facts=result)



# Generated at 2022-06-13 08:10:09.048531
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    hti = HandlerTaskInclude()
    hti.valid_attrs = HandlerTaskInclude.VALID_INCLUDE_KEYWORDS
    hti.register = False

# Generated at 2022-06-13 08:10:16.883569
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    import ansible.playbook
    import ansible.inventory
    import ansible.template
    import ansible.vars

    # Prepare mocked objects
    p = ansible.playbook.PlayBook(
        playbook='test.yml',
        host_list='test/integration/ansible_hosts',
        callbacks=playbook_cb,
        runner_callbacks=None,
        stats=None,
        inventory=ansible.inventory.Inventory(host_list='test/integration/ansible_hosts')
    )
    t = ansible.playbook.Task(block=None)
    i = ansible.template.Template(
        basedir='.',
        variable_manager=ansible.vars.VariableManager()
    )

# Generated at 2022-06-13 08:10:26.059625
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.plugins.loader import load_plugin
    from ansible.inventory.host import Host
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager

    host = Host('www.example.com')
    inventory = InventoryManager(loader=DataLoader(), sources='')
    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory)
    variable_manager.set_host_variable(host=host, varname='listen', value='True')
    variable_manager.set_host_variable(host=host, varname='ansible_connection', value='winrm')
    variable

# Generated at 2022-06-13 08:10:36.217013
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    #import logging
    #logging.basicConfig(filename="logs/test_HandlerTaskInclude.log", level=logging.DEBUG)

    # init inventory
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources="inventory")
    group_all = Group("all")
    group_all.vars = {"var1": "value1"}
    inventory.add_group(group_all)


# Generated at 2022-06-13 08:10:43.462708
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    constant = dict(
        foo='bar'
    )

    # Create a HandlerTaskInclude named 'myHandler'
    myHandler = HandlerTaskInclude(
        name='myHandler',
        task_include=constant
    )

    # Create a dict named 'dict' composed by a name 'myHandler' and a dict 'tasks'
    dict = {
        'myHandler': {
            'tasks': {}
        }
    }

    # Return handler myHandler
    assert myHandler.load(
        dict,
        block=None,
        role=None,
        task_include=constant,
        variable_manager=None,
        loader=None
    ) is myHandler



# Generated at 2022-06-13 08:10:44.868480
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_task_include = HandlerTaskInclude()
    assert type(handler_task_include) == HandlerTaskInclude


# Generated at 2022-06-13 08:10:46.069605
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    hr=HandlerTaskInclude.load()
    print(hr)

# Generated at 2022-06-13 08:10:54.528163
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
	from ansible.vars import VariableManager
	from ansible.inventory import Inventory
	from ansible.parsing.dataloader import DataLoader
	from ansible.playbook.task import Task

	variable_manager = VariableManager()
	loader = DataLoader()
	
	t = Task()

	# variable_manager, loader=None, path_options=None, variable_manager=None, loader=None
	hti = HandlerTaskInclude(t, variable_manager=variable_manager, loader=loader)

# Generated at 2022-06-13 08:11:05.107746
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    variable_manager = '''VariableManager'''
    loader = '''loader'''
    data = dict(
        include = '''include''',
        include_role = '''include_role''',
        include_tasks = '''include_tasks''',
        files = '''files''',
        name = '''name'''
    )
    block = dict(
        name = '''name'''
    )
    role = dict(
        name = '''name'''
    )
    task_include = dict(
        name = '''name''',
        include_vars = '''include_vars''',
        files = '''files''',
        include_tasks = '''include_tasks''',
        include_role = '''include_role'''
    )
    handler = HandlerTaskIn

# Generated at 2022-06-13 08:11:08.223787
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:11:21.412872
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role import Role
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager.set_inventory(
        InventoryManager(loader=loader, sources=['/Users/kumseokhan/ansible/inventory'])
    )

    # Data definition

# Generated at 2022-06-13 08:11:23.620510
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert handler.block
    assert handler.role
    assert handler.task_include
    assert handler.VALID_INCLUDE_KEYWORDS

# Generated at 2022-06-13 08:11:24.713278
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert handler is not None

# Generated at 2022-06-13 08:11:34.130104
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        'include': 'test.yml',
        'listen': 'test'
    }
    h = HandlerTaskInclude.load(data)
    assert h.get_name() == "TASK-INCLUDE-test.yml"
    assert h.data == None
    assert h.block == None
    assert h.role == None
    assert h.notify == []
    assert h.loop == None
    assert h.tags == None
    assert h.only_if == None
    assert h.run_once == None
    assert h.when == None
    assert h.failed_when == None
    assert h.changed_when == None

# Generated at 2022-06-13 08:11:36.012012
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert HandlerTaskInclude(block=None, role=None, task_include=None)



# Generated at 2022-06-13 08:11:46.134579
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    class Loader:
        def __init__(self, variable_manager, loader, path_list):
            self.variable_manager = variable_manager
            self.loader = loader
            self.path_list = path_list
            
        def load_from_file(self, path):
            return "%s: %s" % (self.__class__.__name__, path)

    class VariableManager:
        hosts = None

    hti = HandlerTaskInclude()
    loader = Loader(VariableManager(), {}, {})
    result = hti.load({
        'include': 'my_include_file',
        'listen': 'my_handler',
        'name': 'my_name'
    }, loader=loader)

# Generated at 2022-06-13 08:11:55.379354
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import ansible.plugins.loader as plugins
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader

    # Dummy handler data
    data = { 'name': 'my_task_name',
             'include': 'my_task.yml',
             'listen': 'my_event'
           }

    # Dummy variables
    variables = { 'var_name': 'var_value'}

    # Dummy inventory
    inventory = InventoryManager(loader=DataLoader())
    host = Host('test_host', variables=variables)
    inventory._hosts = {'test_host': host}

    # Dummy loader
    loader = plugins.PluginLoader()

   

# Generated at 2022-06-13 08:11:56.128745
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert False

# Generated at 2022-06-13 08:11:58.089472
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    print('Test Function: test_HandlerTaskInclude_load')

# Generated at 2022-06-13 08:12:09.987770
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    print('\nUnit test for method load of class HandlerTaskInclude')
    data = {'test': 'test'}
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None

    handler = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)
    assert handler.__class__.__name__ == 'HandlerTaskInclude'
    assert handler.task_include == task_include
    assert handler.block == block
    assert handler.role == role
    assert handler.tags == set()
    assert handler.when == 'always'
    assert handler.static == False
    assert handler.changed_when == 'True'
    assert handler.failed_when == 'False'
    assert handler._name == None

# Generated at 2022-06-13 08:12:12.057187
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    HandlerTaskInclude.load({'name':'my_handler','listen':'notify','tags':'always','include':'./watcher.yml'})

# Generated at 2022-06-13 08:12:18.032181
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    HandlerTaskInclude.load({})
    HandlerTaskInclude.load(data={}, block=None, role=None, task_include=None, variable_manager=None, loader=None)
    print(HandlerTaskInclude.load(data={'name': 'task-name'}, block=None, role=None, task_include=None, variable_manager=None, loader=None))


# Generated at 2022-06-13 08:12:23.143689
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    data = {
        'name': 'handler name',
        'include': 'no'
    }
    assert HandlerTaskInclude.load(data, block=None, role=None, task_include=None, variable_manager=None, loader=None) is not None

# Generated at 2022-06-13 08:12:33.521207
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role import Role
    from ansible.playbook.role.tasks import Task
    from ansible.vars.manager import VariableManager
    from ansible.template import Templar
    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.context import CLIContext

    class LoaderModule(object):
        def __init__(self):
            pass


# Generated at 2022-06-13 08:12:34.086654
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:12:42.616981
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    from ansible.playbook.task import Task

    handler = HandlerTaskInclude()

    data = {
        'handlers': [
            {'handler1': 'handler1.yml'}
        ],
        'roles': [
            {'rolename1': 'role1.yml'}
        ],
        'tasks': [
            {'task1': 'task1.yml'}
        ]
    }

    t = Task()
    h = Host(name="test1")
    g = Group(name="test2")


# Generated at 2022-06-13 08:12:43.593263
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_task_include = HandlerTaskInclude()
    assert isinstance(handler_task_include, HandlerTaskInclude)


# Generated at 2022-06-13 08:12:53.226955
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {}
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.host import Host

    block = Block()
    role = None
    task_include = task_include = TaskInclude()
    variable_manager = VariableManager()
    loader = None
    host = Host(name="127.0.0.1")
    templar = Templar(loader=loader, variables=variable_manager)

    play_context = PlayContext()
    play_context._task = "TASK"
    play_context._play = "PLAY"
    play_context._handler = "HANDLER"
    block._play_context = play_context


# Generated at 2022-06-13 08:12:54.566891
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()



# Generated at 2022-06-13 08:13:13.298594
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    variable_manager = VariableManager()
    loader = None
    host = '127.0.0.1'
    port = '22'
    user = 'test'
    passwd = 'test123'
    ssh_key = 'test-ansible-ssh-key'
    inventory = Inventory([host, ])
    variable_manager.set_inventory(inventory)

    fname = 'test-handler.yml'
    data = '''
        - name: Test handler
          listen: Test handler
          debug: msg="test handler debug message"
    '''
    block = None
    role = None
    task_include = None

    HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)

# Unit

# Generated at 2022-06-13 08:13:19.341148
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    dct = dict()
    dct['name'] = dict()
    dct['name']['include'] = dict()
    dct['name']['include']['file'] = 'file'
    # dct['name']['include']['tasks'] = ['a']

    handler = HandlerTaskInclude.load(dct)
    assert handler.get_name() == 'name'
    assert handler.get_action() == 'include'
    assert handler.all_vars == dict()

# Generated at 2022-06-13 08:13:26.684656
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.errors import AnsibleError
    from ansible.plugins.loader import action_loader

    hti = HandlerTaskInclude(block=None, role=None, task_include=None)

    # Catch an exception if the wrong 2nd argument is passed for the method
    # check_options(self, data, all_vars) of class TaskInclude.
    try:
        hti.check_options('', '')
    except AnsibleError:
        pass
    else:
        assert False

    # Catch an exception if the wrong 3rd argument is passed for the method
    # check_options(self, data, all_vars) of class TaskInclude.
    try:
        hti.check_options('', {}, '')
    except AnsibleError:
        pass
    else:
        assert False

    # Catch

# Generated at 2022-06-13 08:13:28.948137
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    host = Host(name="testhost")
    t = HandlerTaskInclude(host=host)

# Generated at 2022-06-13 08:13:32.179574
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    handler = HandlerTaskInclude.load(data={}, block=None, role=None, task_include=None)
    assert handler.tasks == []

# Generated at 2022-06-13 08:13:32.695146
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert True

# Generated at 2022-06-13 08:13:37.436632
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    """
        ansible.playbook.handler.HandlerTaskInclude.load data
    """
    data = ({
        u'include': u'include_me',
        u'name': u'test name',
        u'vars': {u'var1': u'val1', u'var2': u'val2'}
    }, {})
    assert HandlerTaskInclude.load(data)

# Generated at 2022-06-13 08:13:44.196528
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Create a handler task include class
    handler_task_include = HandlerTaskInclude
    # Assert handler_task_include class exists
    msg = "Expected that the handler_task_include class exists"
    assert handler_task_include, msg
    # Assert handler_task_include class is an instance of 'HandlerTaskInclude'
    msg = "Expected that the handler_task_include class is an instance of 'HandlerTaskInclude'"
    assert isinstance(handler_task_include, HandlerTaskInclude), msg
    # Assert handler_task_include class has the property 'VALID_INCLUDE_KEYWORDS'
    msg = "Expected that the handler_task_include class has the property 'VALID_INCLUDE_KEYWORDS'"

# Generated at 2022-06-13 08:13:44.989497
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass


# Generated at 2022-06-13 08:13:55.223227
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block

    def get_data(**kwargs):
        def fake_load_data(data, variable_manager, loader):
            return data

        data = dict(
            name="dummy",
            tags=["dummy"],
            when=["dummy"]
        )
        data.update(kwargs)
        return data

    def fake_check_options(options, data):
        return Handler(**options)

    class HandlerTaskInclude:
        VALID_INCLUDE_KEYWORDS = TaskInclude.VALID_INCLUDE_KEYWORDS

    block = Block()

# Generated at 2022-06-13 08:14:18.686657
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.included_file import IncludedFile
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task

    # hosts_file = os.path.join(os.path.dirname(__file__), "../../../test/inventory/test_hosts")
    hosts_file = os.path.join(os.path.dirname(__file__), "../../../test/inventory/test_hosts")

    # Initialize variables
    block = Block()
    role = None
    task_include = None

    variable_manager = VariableManager()



# Generated at 2022-06-13 08:14:28.064869
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager

    Host.add_group("group-a")
    Group("group-a").add_host("127.0.0.1")
    Group("group-a").add_host("127.0.0.2")
    Group("group-a").add_host("127.0.0.3")
    Group("group-a").set_variable("test_var", "group_var")

    data = {
        "name": "test_name",
        "include": "test_include",
        "listen": "group-a",
        "connection": "smart"
    }

    variable_manager = VariableManager()
    variable_manager.set_inventory(Host.get_inventory())

# Generated at 2022-06-13 08:14:32.976105
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block

    dataloader = DataLoader()
    variable_manager = VariableManager()
    inventory = dataloader.load_inventory(variable_manager, 'localhost,')
    variable_manager._inventory = inventory

# Generated at 2022-06-13 08:14:33.612313
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:14:43.871091
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    print ("Testing load method of class HandlerTaskInclude")
    import ansible.template
    import ansible.vars
    import ansible.inventory
    import ansible.playbook.block

    host1 = ansible.inventory.host.Host("foo")
    host2 = ansible.inventory.host.Host("bar")
    host1.port = 2222
    host2.port = 2222
    host1.set_variable('ansible_ssh_host','127.0.0.1')
    host1.set_variable('ansible_ssh_user','vagrant')
    host2.set_variable('ansible_ssh_host','127.0.0.1')
    host2.set_variable('ansible_ssh_user','vagrant')

    group = ansible.inventory.group.Group("test group")
   

# Generated at 2022-06-13 08:14:54.274908
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Prepare test objects
    block = None
    role = None
    task_include = None
    data = [
        {
            'include': 'playbooks/roles/role2/tasks/main.yml',
            'listen': 'notify_test',
        }
    ]
    variable_manager = None
    loader = None

    # Call the method under test
    handler = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)

    # Check the result
    if handler is None:
        raise AssertionError('handler is None')

    print(handler.include_tasks.keys())
    print([ 'notify_test' ])


# Generated at 2022-06-13 08:14:55.390064
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass


# Generated at 2022-06-13 08:14:59.877589
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    '''
    Given a HandlerTaskInclude object with a known set of values
    When I execute the code to load an include(s) into that object
    Then I expect to get back the same object with the values in the include(s) added
    '''

    pass

# Generated at 2022-06-13 08:15:00.965804
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # handler = HandlerTaskInclude()
    pass

# Generated at 2022-06-13 08:15:04.328289
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    t = HandlerTaskInclude()

    assert t.load(data=None, block=None, role=None, task_include=None,
                  variable_manager=None, loader=None) == None


# Generated at 2022-06-13 08:15:33.156434
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from collections import namedtuple
    options = namedtuple('Options', ['listtags', 'listtasks', 'listhosts', 'syntax', 'connection','module_path', 'forks', 'remote_user', 'private_key_file', 'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args', 'scp_extra_args', 'become', 'become_method', 'become_user', 'verbosity', 'check'])

# Generated at 2022-06-13 08:15:42.462379
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    inventory = InventoryManager(loader=None, sources=['localhost,127.0.0.1'])
    variable_manager = VariableManager(loader=None, inventory=inventory)

    data = {
        "hosts": 'localhost'
    }

    #self.assertIsInstance(HandlerTaskInclude.load(data, inventory=inventory, variable_manager=variable_manager), Handler)
    #assert isinstance(HandlerTaskInclude.load(data, inventory=inventory, variable_manager=variable_manager), Handler)
    assert isinstance(HandlerTaskInclude.load(data, variable_manager=variable_manager), Handler)

# Generated at 2022-06-13 08:15:43.279691
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    pass

# Generated at 2022-06-13 08:15:49.723061
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    import os
    import sys
    import tempfile
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.vars import VariableManager

    # Define a temp path
    test_dir = tempfile.mkdtemp()
    sample_task_yaml = os.path.join(test_dir, 'sample_task.yml')


# Generated at 2022-06-13 08:15:56.276513
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # pylint: disable=unused-variable

    # Parameter initialization
    # data = "test"
    # block = None
    # role = None
    # task_include = None
    # variable_manager = None
    # loader = None

    # Test all defined cases
    # handler = HandlerTaskInclude(block=block, role=role, task_include=task_include)
    handler = HandlerTaskInclude()

    # Test return of function
    handler.load

# Generated at 2022-06-13 08:15:59.279348
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # data = Host(loader=None, variable_manager=None)
    # handler = HandlerTaskInclude.load(data)
    # assert handler is not None
    return

# Generated at 2022-06-13 08:16:10.047329
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # -----------
    # Load handler with filename and tags
    handler_data = {
        'tags': {'tag_item': 'tag_value'},
        'handlers': [
            'handler_file.yml'
        ]
    }
    handler = HandlerTaskInclude.load(
        handler_data,
        variable_manager={},
        loader={},
        )
    assert handler._role
    assert handler._block
    assert handler._task._role
    assert handler._task._block
    assert handler._task._load
    assert handler._task._include
    assert not handler._task._conditional
    assert not handler._task._notify
    assert not handler._task._when


# Generated at 2022-06-13 08:16:10.877180
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # TODO
    pass

# Generated at 2022-06-13 08:16:12.554629
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_taskinclude = HandlerTaskInclude()
    print(handler_taskinclude)
    # handler_taskinclude.load()


# Generated at 2022-06-13 08:16:13.374646
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    pass

# Generated at 2022-06-13 08:16:53.500323
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:16:56.250853
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    HandlerTaskInclude.load(
    {
    'name': 'apache',
    'listen': "restart apache",
    'local_action': "service apache2 restart"
    }
    )

# Generated at 2022-06-13 08:17:04.280919
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    # Set up mock objects
    class MockVariableManager:
        pass
    class MockLoader:
        pass
    class MockBlock:
        pass
    class MockRole:
        name = "role_name"
    class MockTaskInclude:
        name = "task_include_name"

    # Set up input data
    handler_input_data = {
        'include': 'my_tasks.yml',
        "listen": "all",
        "name": "handler_name"
    }

    # Execute method under test
    result = HandlerTaskInclude.load(
        handler_input_data,
        block=MockBlock,
        role=MockRole,
        task_include=MockTaskInclude,
        variable_manager=MockVariableManager,
        loader=MockLoader
    )

    #

# Generated at 2022-06-13 08:17:13.255006
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import find_plugin
    from ansible.plugins.callback.default import CallbackModule
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block
    from ansible.plugins.strategy.linear import LinearStrategy
    from ansible.playbook.role import Role
    from ansible.template.template import AnsibleTemplate
    from ansible.plugins.cache import FactCache
    import ansible.constants as C


# Generated at 2022-06-13 08:17:14.823706
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert HandlerTaskInclude is not None

# Generated at 2022-06-13 08:17:27.470144
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # HandlerTaskInclude.load()

    data = dict(
        action='debug',
        args=dict(
            msg='{{unhandled_error}}'
        ),
    )

    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()

    inventory = Inventory(loader=loader, variable_manager=variable_manager,  host_list='localhost')
    variable_manager.set_inventory(inventory)

    h = HandlerTaskInclude.load(data, variable_manager=variable_manager, loader=loader)

    assert h.block == None
    assert h.role == None
    assert h.task_include == None

    assert h.action == 'debug'
    assert h

# Generated at 2022-06-13 08:17:34.696779
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    handler_task_include = HandlerTaskInclude()
    handler = handler_task_include.load(
        {
            'include': 'test_HandlerTaskInclude_load.yml',
            'listen': 'something',
        },
        block=None,
        role=None,
        task_include=None,
        variable_manager=None,
        loader=None,
    )
    task_include = TaskInclude('include', 'test_HandlerTaskInclude_load.yml', None)
    assert handler is not None
    assert handler.__class__.__name__ == 'HandlerTaskInclude'
    assert handler._name == task_include._name
    assert handler._filename == task_include._filename

# Generated at 2022-06-13 08:17:35.957932
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert handler.__class__.__name__ == 'HandlerTaskInclude'

# Generated at 2022-06-13 08:17:41.582006
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group

    from optparse import Values

    from ansible.playbook.block import Block
    from ansible.playbook.role import Role

    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager

    from ansible.vars.hostvars import HostVars
    from ansible.vars.unsafe_proxy import UnsafeProxy

    from ansible.inventory.manager import InventoryManager

    from ansible.template.template import AnsibleTemplate
    from ansible.playbook.task import Task
    from ansible.plugins.loader import find_plugin, get_all_plugin_loaders

    from ansible.utils.listify import listify_lookup_plugin_terms


# Generated at 2022-06-13 08:17:49.610509
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import os,sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    os.environ['ANSIBLE_CONFIG'] = '../ansible.cfg'
    os.environ['ANSIBLE_HOSTS'] = '../hosts'

    from ansible.utils.display import Display
    from ansible.utils import plugin_docs

    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    display = Display()
    plugin_docs.verbose = True
    inventory = InventoryManager(loader=DataLoader(), sources='../hosts')

    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    ##

# Generated at 2022-06-13 08:19:18.365047
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    data = {"test": "1"}
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None

    obj = HandlerTaskInclude(block=block, role=role, task_include=task_include)

    obj.check_options = check_options_mock
    obj.load_data = load_data_mock

    def check_options_mock(arg1, arg2): pass
    def load_data_mock(arg1, arg2=None, arg3=None, arg4=None): pass

    HandlerTaskInclude.load(
        data=data,
        block=block,
        role=role,
        task_include=task_include,
        variable_manager=variable_manager,
        loader=loader
    )

# Generated at 2022-06-13 08:19:21.482160
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    h = HandlerTaskInclude()
    assert h.block == None
    assert h.role == None
    assert h.task_include == None

# Generated at 2022-06-13 08:19:22.668727
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # TODO: implement me
    pass

# Generated at 2022-06-13 08:19:33.203944
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.conditional import Conditional
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext
    from ansible.cliconf.rconf.rconf import Rconf
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugins import terminal_loader

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    play_context = PlayContext()
    play_context.rconf = Rconf(loader=loader)
    play_context.terminal = terminal_loader.TerminalLoader()

# Generated at 2022-06-13 08:19:37.873832
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.vars.variable import Variable
    from ansible.parsing.yaml.objects import AnsibleUnicode, AnsibleSequence
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    host = Host('localhost')
    host.vars_plugin_set(Variable(name='foo', value=AnsibleUnicode('bar')))
    host.vars_plugin_set(Variable(name='foobar', value=AnsibleUnicode('barfoo')))
    group = Group('all')

# Generated at 2022-06-13 08:19:48.470085
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        'listen': 'all',
        'include': 'handlers/all.yml',
    }

    handler = HandlerTaskInclude.load(data)

    assert handler is not None
    assert handler.block is None
    assert handler.role is None
    assert handler.task_include is None
    assert handler.listen == 'all'
    assert handler.loop is None
    assert handler.loop_args is None
    assert handler.static is None
    assert handler.tags == ['all']
    assert handler.when is None
    assert handler.include == 'handlers/all.yml'
    assert handler._load_name is None
    assert handler._task is None

# Generated at 2022-06-13 08:19:56.954415
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Load modules needed for testing
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    import pytest

    # Create objects needed for testing
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager.set_inventory(inventory)
    variable_manager.extra_vars = {'hostvars': {'localhost': {}}}

    # Create object to test
    test_object = HandlerTaskInclude(block=None, role=None, task_include=None)

    # Create test input data

# Generated at 2022-06-13 08:20:02.768738
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    myHost = Host(name="myhost", port=22)
    myHost.set_variable("ansible_ssh_host", "127.0.0.1")
    myHost.set_variable("ansible_ssh_port", 22)
    myHost.set_variable("ansible_ssh_user", "root")
    myHost.set_variable("ansible_ssh_pass", "pass")
    myHost.set_variable("ansible_ssh_private_key_file", "/root/.ssh/id_rsa")
    myHost.set_variable("ansible_ssh_extra_args", "-o StrictHostKeyChecking=no")

    myHost2 = Host(name="myhost2", port=22)
    myHost2.set_variable("ansible_ssh_host", "127.0.0.1")
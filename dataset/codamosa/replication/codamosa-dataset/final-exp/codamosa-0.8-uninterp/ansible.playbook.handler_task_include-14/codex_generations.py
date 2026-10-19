

# Generated at 2022-06-13 08:09:59.353079
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert handler

# Generated at 2022-06-13 08:10:07.581426
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.vars import VariableManager
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.inventory.host import Host

    # Create variables
    try:
        h = HandlerTaskInclude()
        h._check_keywords = TaskInclude._check_keywords.__func__
    except:
        h = TaskInclude()

    data = AnsibleUnicode(u'name')
    block = AnsibleUnicode(u'block')
    role = AnsibleUnicode(u'role')
    task_include = AnsibleUnicode(u'include')
    h._load_items = TaskInclude._load_items.__func__
    h.get_name = TaskInclude.get_name.__func__
    h.load_data = TaskInclude

# Generated at 2022-06-13 08:10:10.562002
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    include_str = 'tasks/test.yml'
    task_include = HandlerTaskInclude(block=None, role=None, task_include=None)
    task_include.include = include_str
    assert task_include.include == include_str


# Generated at 2022-06-13 08:10:12.121988
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    task = HandlerTaskInclude.load({"include":"main.yml"})
    assert task.static

# Generated at 2022-06-13 08:10:18.838841
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.errors import AnsibleError

    try:
        x = HandlerTaskInclude.load(data=dict(name='test'), block=dict(name='test', parent=dict(name='test')), role=dict(name='test', tasks=dict(handlers=dict(name='test'))))
        if x is not None:
            raise AssertionError('Expected a value of None from load')
    except AnsibleError:
        pass

    try:
        x = HandlerTaskInclude.load(data=dict(name='test'), block=dict(name='test', parent=dict(name='test')), role=dict(name='test', handlers=dict(name='test')))
        if x is not None:
            raise AssertionError('Expected a value of None from load')
    except AnsibleError:
        pass

# Generated at 2022-06-13 08:10:19.662054
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # TODO
    pass



# Generated at 2022-06-13 08:10:29.280475
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    from ansible.errors import AnsibleError

    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude

    from ansible.template import Templar
    # from ansible.vars.manager import VariableManager

    # TODO: Replace with appropriate 'mock' objects.
    b = Block()
    r = Role()
    t = Task()
    ti = TaskInclude()
    v = ''
    d = {}
    # vm = VariableManager()

    hti = HandlerTaskInclude()
    # TODO: Add additional tests to check error handling of function load.

# Generated at 2022-06-13 08:10:43.659243
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    '''
    # [ DEMO - HandlerTaskInclude - load() ]
    #
    # #### HandlerTaskInclude - load()
    #
    # ```python
    # data = {'listen': '<some task>'}
    # handler = HandlerTaskInclude.load(
    #     data = data,
    #     block = None,
    #     role = None,
    #     task_include = None,
    #     variable_manager = None,
    #     loader=None
    # )
    # ```
    #
    # Outputs:
    #
    # ```python
    # handler
    # ```
    '''
    data = {'listen': '<some task>'}

# Generated at 2022-06-13 08:10:46.899269
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    t = Task('Task')
    b = Block()
    b.block  = [t]
    b.parent = t
    r = Role('Role')
    r.task_blocks = b
    handler = HandlerTaskInclude(role=r)
    assert handler._name == 'Role'

# Generated at 2022-06-13 08:10:48.083998
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # test HandlerTaskInclude
    assert True

# Generated at 2022-06-13 08:10:50.165302
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:11:03.016576
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    include = HandlerTaskInclude(block=None, role=None, task_include=None)
    assert include
    # assert isinstance(include, Handler)
    # assert isinstance(include, TaskInclude)
    assert include.VALID_INCLUDE_KEYWORDS == {"freeform", "no_log", "ignore_errors", "delegate_to", "connection", "tags", "run_once", "register", "remote_user", "sudo", "sudo_user", "when", "always_run", "become", "become_user", "any_errors_fatal", "serial", "vars", "listen"}

    # test_include_from_role

# Generated at 2022-06-13 08:11:09.438269
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
  t = HandlerTaskInclude(block=None, role=None, task_include=None)
  if t.VALID_INCLUDE_KEYWORDS != Handler.VALID_HANDLER_KEYWORDS.union({'listen'}):
    raise Exception('Validation of include keyword failed.')

# Generated at 2022-06-13 08:11:11.556583
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    import pytest
    with pytest.raises(NotImplementedError):
        HandlerTaskInclude()

# Generated at 2022-06-13 08:11:22.688382
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    def _init_inventory(inventory):
        # Add groups
        groups = ['development', 'development:child', 'production', 'production:child']
        for group in groups:
            new_group = Group(name=group)
            inventory.add_group(new_group)
        # Add hosts
        new_host = Host(name="testhost")
        inventory.add_host(new_host)

    # Instantiate needed objects
    variable_manager = VariableManager()
    loader = None
    inventory = InventoryManager(loader=loader, sources=[])
    _init_inventory(inventory)
    variable_manager.set_inventory(inventory)

    #

# Generated at 2022-06-13 08:11:32.733632
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.inventory import Inventory
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.block import Block

    block = Block()
    host = Inventory()
    variable_manager = VariableManager()
    loader = DataLoader()

    data = dict(
        name = "listen_handler_name",
        ignore_errors = True,
        listen = "listen_handler_name"
    )

    handler = HandlerTaskInclude.load(data, block=block, variable_manager=variable_manager, loader=loader)

    assert handler._name == "listen_handler_name"
    assert handler._ignore_errors == True
    assert handler._listen == "listen_handler_name"



# Generated at 2022-06-13 08:11:38.268531
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = dict()
    data["name"] = "Test HandlerTaskInclude_load"
    data["listen"] = "localhost"
    handler = HandlerTaskInclude.load(data)
    assert handler._attributes['name'] == "Test HandlerTaskInclude_load"
    assert handler._attributes['listen'] == "localhost"
    assert handler.validate()

# Generated at 2022-06-13 08:11:42.600821
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    h = Host(name="h0001")
    b = Block(
        parent_block=h,
        role=None,
        task_include=None,
        use_handlers=True,
        always_run=False,
    )
    h.set_variable_manager(VariableManager())
    h.set_loader(DataLoader())
    data = {
        'include': 'handlers/main.yml',
        'listen': 'foobar',
    }


# Generated at 2022-06-13 08:11:50.593911
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Pre-requisite : creation of object handler
    data = dict(
        name = 'name',
        tasks = [dict()]
    )
    variable_manager = dict()
    loader = dict()
    handler = HandlerTaskInclude.load(data, variable_manager=variable_manager, loader=loader)

    assert handler.static is False
    assert handler.name == 'name'
    assert handler.notify == []
    assert handler._role is None
    assert handler.block is None
    assert handler.include is None
    assert handler.tags == {'always'}
    assert handler.skip_tags == set()
    assert handler.run_once is False
    assert handler.handlers == [{'name': 'name', 'tasks': [{}]}]
    assert handler.run is False

    # Pre-requisite : creation of

# Generated at 2022-06-13 08:11:52.012138
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():

    handler = HandlerTaskInclude()
    assert handler is not None

# Generated at 2022-06-13 08:11:55.243636
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:11:59.175038
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    fake_data = '{"listen": "hello"}'

    handler = HandlerTaskInclude.load(fake_data, variable_manager=None, loader=None)

    assert handler.listen == "hello"

# Generated at 2022-06-13 08:12:10.149191
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    try:
        from ansible.inventory.group import Group
    except ImportError:
        from ansible.inventory.group import Group  # noqa

    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role

    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import lookup_loader
    from ansible.inventory.manager import InventoryManager
    import ansible.constants as C
    from ansible.parsing.vault import VaultLib
    from ansible.vars import VariableManager
    from ansible.inventory.host import Host
    from ansible.module_utils.six import string_types
    import os


# Generated at 2022-06-13 08:12:13.067859
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Programmer might add new keywords in the future
    # This Unit test is for notifying any failure when execute the code
    assert set(HandlerTaskInclude.VALID_INCLUDE_KEYWORDS) >= HandlerTaskInclude.VALID_INCLUDE_KEYWORDS

# Generated at 2022-06-13 08:12:19.679819
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    obj = HandlerTaskInclude()
    assert obj.VALID_INCLUDE_KEYWORDS == set(['static', 'dynamic', 'with_items']), "class HandlerTaskInclude: def __init__(): VALID_INCLUDE_KEYWORDS = %s" % repr(obj.VALID_INCLUDE_KEYWORDS)


# Generated at 2022-06-13 08:12:27.792853
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        'handler': 'main',
        'listen': 'network_changed',
        'block': 'network',
        'notify': {
            'name': 'reboot',
            'when': 'network_changed'
        },
        'include': {
            'name': 'tasks/reboot.yml',
            'vars': {'reboot_timeout': 10}
        }
    }

    block = 'network'
    role = None
    task_include = None
    variable_manager = None
    loader = None

    t = HandlerTaskInclude(block=block, role=role, task_include=task_include)
    handler = t.check_options(
        t.load_data(data, variable_manager=variable_manager, loader=loader),
        data
    )


# Generated at 2022-06-13 08:12:37.626535
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import sys, os
    import tempfile
    import pytest
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.flexible import Inventory as FlexInventory
    import ansible.parsing.dataloader
    from ansible.vars.manager import VariableManager

    inv_file = tempfile.mktemp()
    f = open(inv_file, 'w+')
    f.write("[localhost]\nlocalhost")
    f.close()

    group = Group("all")
    inventory = FlexInventory(host_list=inv_file)
    inventory.add_group(group)
    loader_obj = ansible.parsing.dataloader.DataLoader()
    variable_manager = Variable

# Generated at 2022-06-13 08:12:39.089923
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    pass

if __name__ == "__main__":
    test_HandlerTaskInclude()

# Generated at 2022-06-13 08:12:43.550512
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    a = TaskInclude()
    assert isinstance(a, TaskInclude)
    b = HandlerTaskInclude()
    assert isinstance(b, HandlerTaskInclude)
    assert isinstance(b, Handler)
    assert isinstance(b, TaskInclude)
    c = HandlerTaskInclude(block=None, role=None, task_include=None)
    assert isinstance(c, HandlerTaskInclude)


# Generated at 2022-06-13 08:12:53.149176
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    h = Host('localhost')
    variable_manager = VariableManager()
    loader = DataLoader()
    d=dict(
        name='test',
        include='include.yml',
        include_tasks='include.yml',
        include_role='include.yml',
        include_vars='include.yml',
        include_tasks_from='include.yml',
        include_role_from='include.yml',
        include_vars_from='include.yml'
    )

# Generated at 2022-06-13 08:13:12.354816
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.host import Host

    task_data = dict(
        name='test',
        action='shell',
        args='uname -a',
        include=dict(
            file='./include_tasks.yml',
            tasks='first_task'
        ),
        listen='include_tasks'
    )

    playbook = dict(
        roles = [
            dict(
                handlers=[task_data]
            )
        ]
    )

    inventory = dict(
        hosts = ['localhost']
    )


# Generated at 2022-06-13 08:13:14.704817
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():

    # Create a new HandlerTaskInclude instance with block and role
    hti = HandlerTaskInclude(block='dummy_block', role='dummy_role')
    assert hti

# Generated at 2022-06-13 08:13:20.972598
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    test_include_str = 'test include in handler'
    data = dict(
        include=test_include_str
    )
    handler = HandlerTaskInclude.load(data)

    assert handler is not None
    assert handler._task_include is not None
    assert handler._ds is None

    assert handler.name == test_include_str

# Generated at 2022-06-13 08:13:27.221779
# Unit test for method load of class HandlerTaskInclude

# Generated at 2022-06-13 08:13:32.809724
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # create a fake handler and run the test
    class _fake_handler(HandlerTaskInclude):
        def load_data(self, data, variable_manager=None, loader=None):
            return data

    data = {
        'include': 'some_file_to_include'
    }

    fake_handler = _fake_handler()
    loaded_handler = fake_handler.load(data)

    # assert test results
    assert loaded_handler['_include'] == 'some_file_to_include'

# Generated at 2022-06-13 08:13:34.140135
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert HandlerTaskInclude.load({'include': 'foo'}) is not None

# Generated at 2022-06-13 08:13:37.442564
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    hti = HandlerTaskInclude()
    with pytest.raises(AttributeError) as excinfo:
        hti.load(data=None)
    assert "unsupported operand type(s) for =: 'NoneType' and 'str'" in str(excinfo.value)

# Generated at 2022-06-13 08:13:48.202003
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Instanciate the task
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import plugin_loader
    from ansible.playbook.play_iterator import PlayIterator
    from ansible.playbook.included_file import IncludedFile
    block = Block(None)
    block.vars = dict()
    variable_manager = VariableManager(loader=DataLoader())
    variable_manager._extra_vars = dict()

# Generated at 2022-06-13 08:13:50.512488
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler1 = HandlerTaskInclude()
    handler2 = HandlerTaskInclude()

    print(handler1.__dict__)
    print(HandlerTaskInclude.__dict__)

# Generated at 2022-06-13 08:13:58.340036
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role

    block = Block()
    role = Role()
    task_include = TaskInclude()
    data = dict(task_include.load(data=dict(), block=block, role=role, task_include=task_include))
    handler = HandlerTaskInclude.load(data=data, block=block, role=role, task_include=task_include)
    assert handler.get_name() == 'handler'
    assert handler.block == block
    assert handler.role == role
    assert handler.task_include == task_include

# Generated at 2022-06-13 08:14:10.486287
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():

    t = HandlerTaskInclude(block=None, role=None, task_include=None)

    pass

# Generated at 2022-06-13 08:14:21.274104
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.plugins.loader import callback_loader
    from ansible.template.template import AnsibleTemplate
    import os
    import tempfile
    import yaml

    # Create a temporary directory
    tmp_dir = tempfile.mkdtemp()

    # Create the YAML file
    (fd, path) = tempfile.mkstemp(dir=tmp_dir, prefix='yaml_test_file')
    print(path)
    os.close(fd)


# Generated at 2022-06-13 08:14:26.074218
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():

    handler_task_include = HandlerTaskInclude()

    # test default attributes
    assert handler_task_include.block is None
    assert handler_task_include.role is None
    assert handler_task_include.task_include is None

    # test load function
    handler_task_include.load(None, None, None, None, None, None)

# Generated at 2022-06-13 08:14:31.612956
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    """
    Ansible.Tests.unit.test_utils.test_data.test_HandlerTaskInclude
    Load method test (HandlerTaskInclude)
    """

    # Try to load a Handler.
    options = {'include': 'test_include'}
    handler = HandlerTaskInclude.load(data=options, variable_manager=None)

    # Check if the handler is a valid HandlerTaskInclude.
    assert isinstance(handler, HandlerTaskInclude)

# Generated at 2022-06-13 08:14:38.459244
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    a = dict(a=1)
    c = dict(a=1, c=2)
    assert HandlerTaskInclude.load(a) == a
    assert HandlerTaskInclude.load(a) != c
    assert HandlerTaskInclude.load(c) == c
    assert HandlerTaskInclude.load(a) == dict(a=1)
    assert HandlerTaskInclude.load(c) == dict(a=1, c=2)

# Generated at 2022-06-13 08:14:43.334118
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    handler_task_include = HandlerTaskInclude()
    handler = handler_task_include.load('handler.yml')

    assert type(handler) is HandlerTaskInclude
    assert handler.name == 'handler'
    assert handler.task == 'handler'
    assert handler.include == 'handler.yml'
    assert handler.block == None
    assert handler.role == None
    assert handler.task_include == None

# Generated at 2022-06-13 08:14:46.104859
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    try:
        # Instantiation without argument, should raise exception
        assert HandlerTaskInclude() is None
    except TypeError as e:
        # Expected exception
        print(e)


# Generated at 2022-06-13 08:14:46.537622
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:14:54.210852
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    obj = {'hosts': 'all', 'listen': 'test', 'name': 'test'}
    obj_ = HandlerTaskInclude()
    assert isinstance(obj_, Handler)
    assert isinstance(obj_, TaskInclude)
    assert obj_._role is None
    assert obj_._task_include is None
    assert isinstance(obj_._valid_attrs, set)
    assert obj_._valid_attrs == obj_.VALID_INCLUDE_KEYWORDS
    assert isinstance(obj_._invalid_attrs, dict)
    assert obj_._invalid_attrs == {}
    assert isinstance(obj_._attributes, dict)
    assert obj_._attributes == {}
    assert obj_._block is None
    assert obj_._loop is None

# Generated at 2022-06-13 08:14:54.942666
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:15:15.923706
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # print("Testing HandlerTaskInclude constructor")
    pass

# Generated at 2022-06-13 08:15:17.912712
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {'listen': 'rebooted'}
    handler = HandlerTaskInclude.load(data)
    assert handler.listen == 'rebooted'

# Generated at 2022-06-13 08:15:24.579098
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    host1 = Host(name='host1')
    host2 = Host(name='host2')
    group1 = Group(name='group1')
    group1.add_host(host1)
    group1.add_host(host2)
    group2 = Group(name='group2')
    group2.add_host(host1)
    group3 = Group(name='group3')
    group3.add_child_group(group1)
    group3.add_child_group(group2)
    group3.add_host(host2)

# Generated at 2022-06-13 08:15:33.202756
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    import ansible.playbook.block as block
    import ansible.playbook.role.include as role_include
    import ansible.playbook.task_include as task_include
    import ansible.playbook.task as task

    play = Play().load({
        'hosts': 'localhost',
        'tasks': [
            {
                'action': 'test',
                'listen': 'foo'
            }
        ]
    }, variable_manager=VariableManager(), loader=False)


# Generated at 2022-06-13 08:15:41.140801
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    loader = DataLoader()
    variable_manager = VariableManager()
    variable_manager.set_inventory(InventoryManager(loader=loader))

    data = '{"include":"test.yml", "tags":["test", "test2"], "when": "test"}'
    handler = HandlerTaskInclude.load(
        data,
        variable_manager=variable_manager,
        loader=loader,
    )
    assert handler._task_include.only_tags == set(['test', 'test2'])

# Generated at 2022-06-13 08:15:43.521591
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert HandlerTaskInclude

if __name__ == '__main__':
    test_HandlerTaskInclude()

# Generated at 2022-06-13 08:15:49.811474
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    
    # import os
    import sys

    # import ansible.inventory.host
    # import ansible.playbook.block
    import ansible.playbook.role
    # import ansible.playbook.task_include
    import ansible.playbook.task
    import ansible.parsing.yaml.objects
    import ansible.template

    # from ansible.playbook.task_include import TaskInclude
    # from ansible.playbook.handler import Handler
    from ansible.template import Templar

    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader


    # VariableManager = ansible.vars.VariableManager
    # Loader = ansible.parsing.dataloader.DataLoader

# Generated at 2022-06-13 08:15:54.449718
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():

    hti = HandlerTaskInclude(block=None, role=None, task_include=None)
    # print(hti.VALID_INCLUDE_KEYWORDS)


if __name__ == "__main__":
    test_HandlerTaskInclude()

# Generated at 2022-06-13 08:15:58.788413
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.vars import VariableManager
    variable_manager = VariableManager()
    data = {'include': 'test.yml'}
    load = HandlerTaskInclude.load(data, variable_manager=variable_manager)

# Generated at 2022-06-13 08:16:10.693090
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    
    # Load ansible.cfg file
    ansible_cfg_path = os.path.abspath("ansible.cfg")
    config = ConfigParser.SafeConfigParser()
    config.read(ansible_cfg_path)
    
    # Load default section from ansible.cfg
    default_section = "defaults"
    configuration = {}    
#     if config.has_section(default_section):
#         
#         configuration = dict(config.items(default_section))

    # Load variable_manager
    variable_manager = VariableManager(loader=loader, inventory=inventory, variable_manager=variable_manager)
    
    # Load handler
    handler = HandlerTaskInclude.load(data, block=block, task_include=task_include, variable_manager=variable_manager, loader=loader)



# Generated at 2022-06-13 08:16:56.459072
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager
    from ansible.errors import AnsibleParserError
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    data = """
    - import_tasks: include_role.yml
      include_vars: varfile.yml
      register: result
      fail: false
      ignore_errors: false
      when: ansible_os_family == 'RedHat'
    """
    variable_manager=VariableManager()
    loader=AnsibleLoader(data, variable_manager=variable_manager)
    data=loader.get_single_data()
   

# Generated at 2022-06-13 08:16:57.218656
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    pass

# Generated at 2022-06-13 08:16:59.276048
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    HandlerTaskInclude.load({
        'include': 'test/test1.yml'
    })

# Generated at 2022-06-13 08:17:04.090924
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    sample = """
- name: Without keyword listen
  include: foo.yml
  tags:
    - no-listen
"""
    # Create an instance of class HandlerTaskInclude
    t = HandlerTaskInclude.load(data=sample, block=None, role=None, task_include=None)
    assert t._task.get_name() == 'Without keyword listen'
    # assert t.loops == "{{inventory_hostname}}"
    assert t.tags.get('no-listen') is not None

# Generated at 2022-06-13 08:17:07.191107
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    def __init__():
        # test 1
        handler_task_include = HandlerTaskInclude()
        return handler_task_include

    handler_task_include = __init__()


# Generated at 2022-06-13 08:17:08.317348
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    return handler

# Generated at 2022-06-13 08:17:12.774250
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = [{'include': 'test'}]
    h = HandlerTaskInclude.load(data)
    assert isinstance(h, HandlerTaskInclude)
    data = [{'include': 'test', 'static': 'teststatic', 'tags': ['tag1', 'tag2']}]
    h = HandlerTaskInclude.load(data)
    assert isinstance(h, HandlerTaskInclude)

# Generated at 2022-06-13 08:17:26.033878
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude

    host = Host(name="test")
    group = Group(name="test")
    inventory = Inventory(loader=DataLoader(), sources="localhost")
    inventory.add_host(host)
    inventory.add_group(group)
    task = Task()
    role = Role()
    block = Block()
    play_

# Generated at 2022-06-13 08:17:27.693735
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    obj = HandlerTaskInclude()
    assert obj is not None


# Generated at 2022-06-13 08:17:29.075772
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {"listen": "all"}
    handler = HandlerTaskInclude.load(data)

# Generated at 2022-06-13 08:18:51.893133
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    pass #TODO

# Generated at 2022-06-13 08:18:59.417081
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    variable_manager = 'variable_manager'
    loader = 'loader'
    data = 'data'
    block = 'block'
    role = 'role'
    task_include = 'task_include'
    handler = 'handler'
    ret = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)
    assert data == handler.load_data.call_args_list[0][0][0]
    assert variable_manager == handler.load_data.call_args_list[0][1]['variable_manager']
    assert loader == handler.load_data.call_args_list[0][1]['loader']
    assert handler.load_data.return_value == handler.check_options.call_args_list[0][0][0]
    assert data == handler.check_options

# Generated at 2022-06-13 08:19:04.123435
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    HandlerTaskInclude.load(data={'include': 'test.yml', 'listen': 'test.yml'}, block={'handlers': 'test.yml'}, role={'tasks': 'test.yml'}, task_include= {'tasks': 'test.yml'}, variable_manager=None, loader=None)

# Generated at 2022-06-13 08:19:05.393772
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # TODO
    pass

# Generated at 2022-06-13 08:19:07.563633
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    obj = HandlerTaskInclude(block=None, role=None, task_include=None)
    assert isinstance(obj, HandlerTaskInclude)

# Generated at 2022-06-13 08:19:08.111456
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert HandlerTaskInclude

# Generated at 2022-06-13 08:19:09.586673
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    """
    HandlerTaskInclude: tests for the load method
    """
    pass

# Generated at 2022-06-13 08:19:14.660292
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    class MyClass():
        def __init__(self):
            pass
    handler = HandlerTaskInclude(block="", role=MyClass(), task_include=MyClass())
    handler.load_data({'hosts': ''})
    assert handler.static_play is False
    assert handler.block is ''
    assert isinstance(handler.role, MyClass)
    assert isinstance(handler.task_include, MyClass)
    assert handler.tags is None

# Generated at 2022-06-13 08:19:15.183319
# Unit test for method load of class HandlerTaskInclude

# Generated at 2022-06-13 08:19:20.589233
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    """
    Test for loading a handler with task includes.

    In the handler file there is 'notify' keyword with a
    task includes. Here we load that 'notify' and check
    whether it is loaded or not.
    """

    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext

    # This is the path of file which contains the task includes
    handlers_path = "/root/.ansible_galaxy/roles/ansible-role-apach/handlers/main.yml"
    my_loader = DataLoader()
    my_inv = InventoryManager(loader=my_loader, sources=[])
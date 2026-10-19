

# Generated at 2022-06-13 08:10:11.279484
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import yaml

    data = yaml.load("""
name: go
- hosts: localhost
  tasks:
  - include: other.yml
  handlers:
    - myhandler
    - include: handlers/additional_handler.yml
""")

    import ansible.playbook.handler
    check = ansible.playbook.handler.HandlerTaskInclude.load
    result = check(data, block=None, role=None, task_include=None, variable_manager=None, loader=None)

    # Test import
    assert result == result

    assert data["handlers"][1]["tasks"] == result.block

    assert data["handlers"][1]["tags"] == None
    assert result.tags == []

    assert data["handlers"][1]["when"] == None
    assert result.when

# Generated at 2022-06-13 08:10:19.244567
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.role_include import RoleInclude
    from ansible.plugins.loader import add_all_plugin_dirs
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    #import inspect
    #print("\n".join(inspect.getmembers(HostVars)))

    # Inhalt der Datei "play.yml":
    # 
    # ---
    # name: Play run example
    # hosts: all
    # become:

# Generated at 2022-06-13 08:10:19.833177
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert False

# Generated at 2022-06-13 08:10:23.023181
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    d = { 'import_tasks': 'main.yml', 'listen': 'fake_listen'}
    t = HandlerTaskInclude(None, None, None)
    t.check_options(t.load_data(d), d)



# Generated at 2022-06-13 08:10:25.121419
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        'include': './include_this.yml',
        'name': 'test'
    }

    HandlerTaskInclude.load(data)

# Generated at 2022-06-13 08:10:35.797291
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import sys, os
    sys.path.append('./lib')
    sys.path.append('./hacking')
    import ansible.inventory
    import ansible.playbook
    import ansible.vars.manager

    # create an object of class Host
    h = ansible.inventory.host.Host(name="server01")

    # create an object of class Block
    b = ansible.playbook.block.Block(hosts=[h])

    # create an object of class VariableManager
    vm = ansible.vars.manager.VariableManager()

    # create an object of class Playbook
    p = ansible.playbook.Playbook.load(playbook_path='playbook.yml', variable_manager=vm)

    # create an object of class Play
    pl = p.get_plays()[0]

# Generated at 2022-06-13 08:10:47.934415
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.groupvars import GroupVars
    from ansible.vars.vars import Variable
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager(loader=loader, inventory=None)

    task = Task()
    task.block = None

    host = Host(name="some.host")
    host.vars = HostVars(name="some.host")
    host.vars['var1'] = "val1"

# Generated at 2022-06-13 08:11:01.017401
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = dict()
    data['name'] = 'test_include_task'
    data['tags'] = 'test_include_task'
    data['listen'] = 'mytask'

    t = HandlerTaskInclude(block=None, role=None, task_include=None)
    handler = t.check_options(
        t.load_data(data, variable_manager=None, loader=None),
        data
    )

    assert handler.name == 'test_include_task'
    assert handler.tags[0] == 'test_include_task'


# Generated at 2022-06-13 08:11:07.202359
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # case 1, data1, HandlerTaskInclude.load(data1) works properly
    data1 = {}
    data1['name'] = 'test'
    data1['listen'] = 'test'
    data1['tags'] = ['a', 'b', 'c']
    handler1 = HandlerTaskInclude.load(data1)
    assert handler1.include.name == 'test'
    assert handler1.listen == 'test'
    assert handler1.include.tags == ['a', 'b', 'c']

#   # case 2, data2, HandlerTaskInclude.load(data2) works properly
    data2 = {}
    data2['name'] = 'echo'
    data2['listen'] = 'echo'
    data2['args'] = {'msg': 'Hello World'}

# Generated at 2022-06-13 08:11:08.944165
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    c = HandlerTaskInclude()  # TODO: Add proper test arguments

# Generated at 2022-06-13 08:11:11.481115
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # TODO
    return

# Generated at 2022-06-13 08:11:16.104848
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass
#        data = {
#            'include': 'some_play',
#            'tags': 'test_tag'
#        }
#        handler = HandlerTaskInclude.load(data)
#        assert(handler is not None)

# Generated at 2022-06-13 08:11:21.410783
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    taskInclude = HandlerTaskInclude()
    try:
        taskInclude.load(
            data = {},
            block = None,
            role = None,
            task_include = None,
            variable_manager = None,
            loader = None
        )
    except SystemExit:
        pass

# Generated at 2022-06-13 08:11:22.647450
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    task_include = HandlerTaskInclude()
    assert task_include is not None

# Generated at 2022-06-13 08:11:32.655489
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.playbook.playbook import Playbook
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from mutable_test_case import MutableTestCase
    import os

    class MockLoader(DataLoader):
        def __init__(self, base_path):
            self._base_path = base_path

        def get_basedir(self, path):
            return self._base_path


# Generated at 2022-06-13 08:11:33.662026
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:11:44.252061
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {u'include': u'copy_files.yml', u'listen': u'copy_files'}
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None

    t = HandlerTaskInclude(block=block, role=role, task_include=task_include)
    handler = t.check_options(
        t.load_data(data, variable_manager=variable_manager, loader=loader),
        data
    )

    # args
    assert handler._args == {u'listen': u'copy_files', u'include': u'copy_files.yml'}

    # block
    assert handler._block == None

    # delegate_to
    assert handler._delegate_to == None

    # delay
    assert handler._delay == None

# Generated at 2022-06-13 08:11:51.396890
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    import pprint

    from ansible.playbook.play_context import PlayContext
    from ansible.inventory import Host, Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars import VariableManager

    # Create a play context
    play_context = PlayContext()

    # Create a variable manager
    variable_manager = VariableManager()

    # Create a data loader
    loader = DataLoader()

    file_name = 'file_name'
    hosts = ['host_1', 'host_2']
    variable_manager.set_inventory(Inventory(loader=loader, variable_manager=variable_manager, host_list=hosts))

    host_1 = Host(name='host_1')
    host_2 = Host(name='host_2')
    variable_manager.set_host_

# Generated at 2022-06-13 08:11:52.077324
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:11:53.950423
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    HandlerTaskInclude.load(dict(include='test_include.yml'))

# Generated at 2022-06-13 08:11:58.313843
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    test = HandlerTaskInclude()
    assert test.__class__.__name__ == "HandlerTaskInclude"

# Generated at 2022-06-13 08:12:09.714116
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    print ('Test Method HandlerTaskInclude.load ...',)
    # Setup
    # FUNC load(
    #   self,
    #   handler_data,
    #   block=None,
    #   role=None,
    #   task_include=None,
    #   variable_manager=None,
    #   loader=None
    # )

# Generated at 2022-06-13 08:12:12.701034
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = dict(
        handler=dict(
            tasks=[
                dict(debug=dict(msg='Hello World')),
                dict(debug=dict(msg='Goodbye World')),
            ]
        )
    )
    assert HandlerTaskInclude.load(data)

# Generated at 2022-06-13 08:12:13.420682
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:12:25.838600
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    h1 = Host("localhost", port=22)
    h2 = Host("ansible.com", port=22)

    inventory = InventoryManager(loader=None, sources=[])
    inventory.add_group("ungrouped")
    inventory.add_host(h1, group="ungrouped")
    inventory.add_host(h2, group="ungrouped")

    variable_manager = VariableManager()
    variable_manager.set_inventory(inventory)

    data = """
    - hosts: all
      tasks:
      - shell: echo hello

    - hosts: localhost
      tasks:
      - shell: echo hello
    """


# Generated at 2022-06-13 08:12:30.993015
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    print("Test load of class HandlerTaskInclude")
    #Verify if a list is returned
    result = HandlerTaskInclude.load("data")

    assert type(result) == list, "HandlerTaskInclude.load return incorrect value"
    print("Test passed")


if __name__ == '__main__':
    test_HandlerTaskInclude_load()

# Generated at 2022-06-13 08:12:34.250422
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    #  A dict containing constructor info
    data = dict()

    #  The constructor object
    handler = HandlerTaskInclude(data)

    #  Assertions
    assert isinstance(handler, HandlerTaskInclude)

# Generated at 2022-06-13 08:12:42.760807
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import ansible.playbook.role.include as ri
    from ansible.playbook.task import Task
    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    assert TaskInclude.load.__doc__.startswith('Make sure all keywords are valid')

    ## Try 1 
    # First test with an empty dict as input 
    # assert TaskInclude.load({}) == None

    ## Try 2
    # Second test with a dict with a non-valid include keyword as input 
    # assert TaskInclude.load({'test': {'test':'test'}}) == None

    ## Try 3
    # an invalid handler include

# Generated at 2022-06-13 08:12:45.384500
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    obj = HandlerTaskInclude()
    assert obj.VALID_INCLUDE_KEYWORDS == frozenset([
            'when',
            'name',
            'first_available_file',
            'with_first_found',
            'tags',
            'free-form',
            'static',
            'listen',
        ])

# Generated at 2022-06-13 08:12:55.824258
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory import groups
    from ansible.inventory.host import Host
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.vars.reserved import Reserved


# Generated at 2022-06-13 08:13:09.232631
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.play import Play
    data = {
        'include': 'file-name',
        'name': 'and this is the task name',
        'with_items': [1, 2, 3],
        'ignore_errors': True,
        'when': False
    }
    p = Play.load(dict(hosts='hosts', name='test'), loader=None, variable_manager=None)
    h = HandlerTaskInclude.load(data, block=None, role=None, task_include=None, variable_manager=None, loader=None)
    assert h.name == 'and this is the task name'
    assert h.loop_with == 'items'
    assert h.ignore_errors == True
    assert h.when is False

# Generated at 2022-06-13 08:13:13.904847
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    handler = HandlerTaskInclude.load({'tasks': [], 'listen': 'test_pattern', 'handler': 'test_handler'})
    assert handler['tasks'] == []
    assert handler['listen'] == 'test_pattern'
    assert handler['notify'] == ['test_handler']

# Generated at 2022-06-13 08:13:21.215808
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_task_include = HandlerTaskInclude(block=[], task_include=[])
    assert handler_task_include != None
    # At present, the following assertion is not guaranteed
    # assert handler_task_include.VALID_INCLUDE_KEYWORDS == ['listen', 'tasks', 'vars', 'pre_tasks', 'post_tasks', 'tags', 'when']

# Generated at 2022-06-13 08:13:27.233904
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import ansible.playbook.task_include
    assert HandlerTaskInclude.load(
        data={'include': ['./foo'], 'include_vars': ['./foo'], 'include_role': ['./foo'], 'listen': 'foobar'},
        loader=ansible.playbook.task_include.include_loader
    )

# Generated at 2022-06-13 08:13:29.024384
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert handler is not None

# Generated at 2022-06-13 08:13:37.037689
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # Constructor test
    # since the parent class is declared abstract, we will always get an exception by simply calling the constructor.
    #   That's why we use a try block below
    try:
        HandlerTaskInclude(block=None, role=None, task_include=None)
        assert False
    except TypeError:
        assert True
    # We are only testing the initialization functionality of the class--which is what we wanted to test
    # Since the class is abstract, there is no way to instantiate it
    #   That's why we use try/except block--to test the exception
    #   The test was a success

# Generated at 2022-06-13 08:13:40.302809
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    t = HandlerTaskInclude.load({"name": "TEST", "include": {"role": [{"name":"mock_role"}]}}, variable_manager=None, loader=None)
    print(t.include_args)
    assert t.include_args["role"] == [{"name":"mock_role"}]

# Generated at 2022-06-13 08:13:50.658624
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handlerTaskInclude = HandlerTaskInclude()

# Generated at 2022-06-13 08:14:00.575866
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    v = VariableManager()
    l = DataLoader()
    r = HandlerTaskInclude.load(data={}, block=None, role=None, task_include=None, variable_manager=v, loader = l)
    assert (r.has_triggered == False)
    r = HandlerTaskInclude.load(data={'listen': 'toto'}, block=None, role=None, task_include=None, variable_manager=v, loader = l)
    assert (r.has_triggered == True)
    assert (r.listen == 'toto')

# Generated at 2022-06-13 08:14:04.407229
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = dict(
        name='cowsay',
        local_action=dict(module='command', args='/usr/games/cowsay "hello world"'),
    )

    t = HandlerTaskInclude()
    handler = t.load(data)

    # from pprint import pprint
    # pprint(vars(handler))


if __name__ == '__main__':
    test_HandlerTaskInclude()
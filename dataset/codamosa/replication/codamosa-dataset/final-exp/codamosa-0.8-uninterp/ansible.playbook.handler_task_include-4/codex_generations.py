

# Generated at 2022-06-13 08:10:07.446608
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    # Mock objects
    variable_manager = VariableManager()
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources='localhost,')
    host = Host(name='localhost')
    host.vars = dict()
    group = Group(name='all')
    group.vars = dict()
    group.hosts.append(host)
    inventory.groups.append(group)
    variable_manager.set_inventory(inventory)

    # Preparing data

# Generated at 2022-06-13 08:10:08.825920
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler=HandlerTaskInclude(block,role,task_include)
    return handler


# Generated at 2022-06-13 08:10:10.601213
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    """
    Test to see if you can make an instance of HandlerTaskInclude
    """
    a = HandlerTaskInclude()
    assert a is not None

# Generated at 2022-06-13 08:10:11.069839
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()

# Generated at 2022-06-13 08:10:16.659200
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # TaskInclude._get_local_role_path = get_local_role_path
    data = dict(
        name=dict(
            file="../../../../../../../../../../../../../../../../../etc/shadow"
        )
    )
    task = HandlerTaskInclude(block=None,
                              role=None,
                              task_include=None)
    # If a file is included with a relative path that goes
    # outside of the role, it will not be loaded.
    handler = task.load(data)
    assert handler is None

# Generated at 2022-06-13 08:10:19.055181
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # test the HandlerTaskInclude class constructor
    h = HandlerTaskInclude(block=None, role=None, task_include=None)
    assert(h is not None)

# Generated at 2022-06-13 08:10:28.654446
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # unittest.TestCase.assertEquals(first, second, msg=None)
    # unittest.TestCase.assertTrue(expr, msg=None)

    # for function load(), parameter data should be a dict, 
    # and return a HandlerTaskInclude object 
    t = HandlerTaskInclude(block=block, role=role, task_include=task_include)
    dict_data = { 'name': 'test_HandlerTaskInclude_load', 'listen': 'test_HandlerTaskInclude_load_listen' }
    handler = t.load(dict_data)
    if handler:
        assert handler.name == dict_data['name'] and handler.listen == dict_data['listen'], "Error running test_HandlerTaskInclude_load()"

# unit test for:
# * check_

# Generated at 2022-06-13 08:10:43.032200
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars

    hvars = HostVars({'inventory_hostname': 'localhost', 'ansible_ssh_user': 'root', 'ansible_ssh_pass': 'password', 'ansible_sudo_pass': 'password'})
    inv_group = Group('localhost')
    inv_group.add_host(Host('localhost'))
    inv_manager = InventoryManager(loader=DataLoader())

# Generated at 2022-06-13 08:10:44.175082
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude(block=None, role=None, task_include=None)
    assert handler

# Generated at 2022-06-13 08:10:44.625114
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert True

# Generated at 2022-06-13 08:10:55.708326
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    from ansible.inventory.host import Host
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.vars import VariableManager

    block = Block(
        role=Role(
            name='testrole',
            tasks=[
                Task(
                    name='task1'
                )
            ]
        ),
        task_include=Task(
            name='task_include',
            handler='true'
        )
    )

    host = Host(
        name='testhost'
    )

    empty_variable_manager = VariableManager()

    handler_task_include = HandlerTaskInclude(
        block=block,
        role=block.role,
        task_include=block.task_include
    )

    handler

# Generated at 2022-06-13 08:11:05.525165
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    block = None
    role = None
    task_include = None
    data = {
        "include_tasks": "test_include.yml"
    }
    variable_manager = None
    loader = None

    handler_task_include = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)
    assert handler_task_include.get_name() == "Include tasks"
    assert handler_task_include.get_actionable_task_names() == ['test_include.yml']
    assert handler_task_include.get_all_task_names() == ['test_include.yml']
    assert handler_task_include.get_actionable_task_tags() == []
    assert handler_task_include.get_all_task_tags() == []
    assert handler_

# Generated at 2022-06-13 08:11:07.546365
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():

    assert HandlerTaskInclude(block=None, role=None, task_include=None)

# Generated at 2022-06-13 08:11:19.146526
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    print('Testing HandlerTaskInclude()')
    # Define necessary inputs
    from ansible.inventory.manager import InventoryManager
    inventory_manager = InventoryManager()
    from ansible.vars.manager import VariableManager
    variable_manager = VariableManager(inventory=inventory_manager)
    import copy
    data = copy.deepcopy(HandlerTaskInclude.VALID_INCLUDE_KEYWORDS)
    # Add function tests here
    try:
        handler_task_include = HandlerTaskInclude(data, variable_manager)
    except:
        print('Error: HandlerTaskInclude() constructor')
    else:
        print('Constructor OK: HandlerTaskInclude()')


# Generated at 2022-06-13 08:11:20.357987
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass



# Generated at 2022-06-13 08:11:25.720120
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # test data
    data = dict(
        include = dict(
            name = '',
            tasks = dict(
                item = '',
            )
        )
    )

    # instantiate object
    handler = HandlerTaskInclude()

    # call method
    result = handler.load(data)

    # test
    assert isinstance(result, Handler)

    # test
    assert len(data) == 1
    assert set(data.keys()) == HandlerTaskInclude.VALID_INCLUDE_KEYWORDS

# Generated at 2022-06-13 08:11:27.010989
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # TODO
    pass

# Generated at 2022-06-13 08:11:28.152741
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # create an instance of class HandlerTaskInclude
    # assert True
    assert True

# Generated at 2022-06-13 08:11:39.236000
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # We don't load anything into the search path but leave that to callers to do as needed.
    # TODO: Actually, we could use a search path based on the loader.
    assert Loader is not None
    loader = Loader()


# Generated at 2022-06-13 08:11:41.648409
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert handler is not None

if __name__ == "__main__":
    test_HandlerTaskInclude()
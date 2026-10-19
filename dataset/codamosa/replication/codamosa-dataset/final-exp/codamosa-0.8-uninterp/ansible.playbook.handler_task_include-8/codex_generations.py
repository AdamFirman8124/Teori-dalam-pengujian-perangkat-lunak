

# Generated at 2022-06-13 08:10:04.961219
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert False, "Unit tests for method load of class HandlerTaskInclude not implemented"

# Generated at 2022-06-13 08:10:09.161481
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {'name': 'test_inc', 'include': 'test_inc.yml'}
    block = ['block1', 'block2']
    role = object()
    task_include = object()
    variable_manager = object()
    loader = object()
    assert HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader) is not None

# Generated at 2022-06-13 08:10:11.048541
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    my_H = HandlerTaskInclude()
    # test if the object was created correctly
    assert my_H.VALID_INCLUDE_KEYWORDS

# Generated at 2022-06-13 08:10:12.201044
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    validate_class(HandlerTaskInclude)


# Generated at 2022-06-13 08:10:12.884625
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # TODO: add unit test
    pass

# Generated at 2022-06-13 08:10:13.725270
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    return None


# Generated at 2022-06-13 08:10:14.257622
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:10:20.001090
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.manager import InventoryManager
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible import context

    host = Host(name='10.0.0.26')
    group = Group(name='test')
    group.add_host(host)
    inventory = InventoryManager(loader=DataLoader(), sources='')
    inventory.add_group(group)
    variable_manager = VariableManager(loader=DataLoader(), inventory=inventory)

    module_name = 'setup'
    module_args = {}
    module_vars = {}


# Generated at 2022-06-13 08:10:20.696198
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert HandlerTaskInclude

# Generated at 2022-06-13 08:10:23.436692
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    class data(object):
        class block(HandlerTaskInclude):
            pass
    class variable_manager(object):
        pass

    ret = HandlerTaskInclude.load(data, "block", variable_manager)
    assert ret

# Generated at 2022-06-13 08:10:26.230763
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import json

    with open('tests/unit/playbook/test_event_handler_include.json') as data_file:    
        data = json.load(data_file)

    assert HandlerTaskInclude.load(data)

# Generated at 2022-06-13 08:10:36.300175
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.manager import VariableManager
    from ansible.vars.cleaner import VarsCleaner
    from ansible.vars.resolver import VarsResolver
    from ansible.vars.manager import VariableManager
    from ansible.utils.vars import combine_vars
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play_context import PlayContext

# Generated at 2022-06-13 08:10:37.785975
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {}
    handler = HandlerTaskInclude.load(data)
    assert isinstance(handler, HandlerTaskInclude)

# Generated at 2022-06-13 08:10:39.874477
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
   pass
   # handler = HandlerTaskInclude()
   # assert handler is not None



# Generated at 2022-06-13 08:10:42.947035
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    hti = HandlerTaskInclude()
    # Test __init__() calling super(TaskInclude, self).__init__()
    assert hti.notify == None
    assert hti.block == None
    assert hti.role == None
    assert hti.task_include == None


# Generated at 2022-06-13 08:10:45.711147
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = dict(
        name="handler-name",
        notify=["handler-notify"],
        listen=["handler-listen"],
    )
    handler = HandlerTaskInclude.load(data)
    print(handler)
    assert isinstance(handler, HandlerTaskInclude)
    assert handler.get_name() == "handler-name"

# Generated at 2022-06-13 08:10:54.968440
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    # The data that will be used to create the HandlerTaskInclude object.
    data = dict(
        name="test_handler_task",
        tasks=["task_one","task_two"],
        notify=["handler_one","handler_two"]
    )

    # Create a HandlerTaskInclude object and test the object.
    handler_task_include = HandlerTaskInclude.load(data)

    assert handler_task_include.get_name() == 'test_handler_task'
    assert handler_task_include.get_action() == 'task'

    assert handler_task_include.is_handler() == True
    assert handler_task_include.is_task() == False
    assert handler_task_include.is_role() == False

# Generated at 2022-06-13 08:11:02.912526
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    data = {'include': {'file': '../main.yml', 'vars': {'a': 'b'}, 'notify': {'handler1': {'name': 'restart'}, 'handler2': {'name': 'restart'}, 'handler3': {'name': 'restart'}, 'handler4': {'name': 'restart'}, 'handler5': {'name': 'restart'}, 'handler6': {'name': 'restart'}}}}

    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None

    handler = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)
    if handler is None:
        raise Exception("handler is None")

# Generated at 2022-06-13 08:11:09.316332
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():

    # This scenario is for testing the constructor of class HandlerTaskInclude
    # block and task_include are both None
    # Expecting success

    handler_task_include = HandlerTaskInclude(block=None, role=None, task_include=None)

    assert handler_task_include is not None


# Generated at 2022-06-13 08:11:10.475188
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert handler

# Generated at 2022-06-13 08:11:22.155400
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {'include':
            {'name': 'include', 'listen': 'service_restarted'}}
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None
    hti = HandlerTaskInclude(block=block, role=role, task_include=task_include)
    handler = hti.check_options(
        hti.load_data(data, variable_manager=variable_manager, loader=loader),
        data
    )

    assert(handler.get_name() == 'include')
    assert(handler.get_tasks()[0].get_name() == 'include')

# Generated at 2022-06-13 08:11:24.025058
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    pb = HandlerTaskInclude()
    assert pb.__class__.__name__ == "HandlerTaskInclude"


# Generated at 2022-06-13 08:11:32.462553
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    variable_manager = "foo"
    loader = "bar"
    data = {'tasks': None,
           'vars': None,
           'local_action': None,
           'notify': None,
           'listen': None}
    handler = HandlerTaskInclude.load(data=data, variable_manager=variable_manager, loader=loader)
    assert handler.get_vars() == None
    assert handler.get_tasks() == None
    assert handler.notify == None
    assert handler.listen == None
    assert handler.get_variable_manager() == variable_manager
    assert handler.get_loader() == loader

# Generated at 2022-06-13 08:11:43.599469
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Test: load HandlerTaskInclude with no handler
    # Exception: KeyError('include')
    data = {}
    block = None
    role = None
    task_include = None
    variable_manager = {}
    loader = None
    try:
        HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)
    except Exception as error:
        assert error.args[0] == 'include'
    else:
        print("Fail!")

    # Test: load HandlerTaskInclude with keys not in VALID_INCLUDE_KEYWORDS
    # Exception: KeyError('include')
    data = {
        'name': 'mysql',
        'not_valid_key': 'included.yml'
    }
    block = None
    role = None
    task_include

# Generated at 2022-06-13 08:11:51.055539
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    test_var_manager = mock.Mock()
    test_loader = mock.Mock()
    test_data = {
        'name': 'Test Task',
        'action': 'shell echo hi'
    }
    test_obj = HandlerTaskInclude.load(test_data, variable_manager=test_var_manager, loader=test_loader)
    assert test_obj._role is None
    assert test_obj._block is None
    assert test_obj._task_include is None
    assert test_obj.name == 'Test Task'
    assert test_obj.action == 'shell echo hi'
    assert test_obj._parent is None
    assert test_obj._play_context is None
    assert test_obj._loader is test_loader
    assert test_obj._variable_manager is test_var_manager
    assert test_

# Generated at 2022-06-13 08:11:55.749267
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert HandlerTaskInclude.load(
        {
            'hosts': 'localhost',
            'tasks': [
                {
                    'include': 'some-file.yml'
                }
            ],
            'post_tasks': [
                {
                    'include': 'some-file.yml'
                }
            ]
        }
    )

# Generated at 2022-06-13 08:12:01.129324
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    task = HandlerTaskInclude()
    data = dict(
        name = 'test-handler',
        trigger = 'include_role',
    )
    task.load(data)
    assert task.task_include.name == 'test-handler'
    assert task.task_include.args['name'] == 'include_role'

# Generated at 2022-06-13 08:12:04.004288
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    t = HandlerTaskInclude(block=None, role=None, task_include=None)
    assert isinstance(t, HandlerTaskInclude)

test_HandlerTaskInclude()

# Generated at 2022-06-13 08:12:04.701396
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    pass

# Generated at 2022-06-13 08:12:13.412767
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import os
    import sys
    import unittest
    import warnings

    from ansible.module_utils.six import StringIO
    from ansible import constants as C
    from ansible.errors import AnsibleError
    from ansible.playbook.play_context import PlayContext

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop
    from units.mock.vars import MockVarsModule
    from units.mock.vm import mock_all_is_dict
    from jinja2.environment import Environment

    from ansible.inventory.manager import InventoryManager
    from ansible.plugins.loader import find_plugin

    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task.include import TaskInclude



# Generated at 2022-06-13 08:12:18.870738
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert False

# Generated at 2022-06-13 08:12:27.581842
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.helpers import load_list_of_blocks

    variable_manager = 'variable_manager'
    loader = 'loader' 

    t = HandlerTaskInclude()

    block_parent = {
        'type': 'notify',
        'name': 'notify',
        'handlers': ['debug'],
        'when': 'foo',
    }

    import ansible.playbook.task_include as task_include
    block_child = {
        'type': 'notify',
        'name': 'debug',
        'listen': 'foo',
    }

    handler = HandlerTaskInclude.load(block_child, block=block_parent, variable_manager=variable_manager, loader=loader)


# Generated at 2022-06-13 08:12:29.107025
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert handler is not None

# Generated at 2022-06-13 08:12:29.744663
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert False

# Generated at 2022-06-13 08:12:36.053859
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    # Arrange
    data = {'include': 'handler_tasks', 'with_items': '3'}
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None

    # Act
    handler = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)

    # Assert
    assert handler.__class__.__name__ == 'Handler'
    assert handler.name == data['include']

# Generated at 2022-06-13 08:12:36.619985
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    pass

# Generated at 2022-06-13 08:12:38.371027
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    HandlerTaskInclude.load('localhost', 'test', 'main', 'test', 'variable_manager', 'loader')

# Generated at 2022-06-13 08:12:45.799150
# Unit test for method load of class HandlerTaskInclude

# Generated at 2022-06-13 08:12:49.437523
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = {}
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None
    handler = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)
    assert handler is not None

# Generated at 2022-06-13 08:12:50.920515
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # TODO: implement
    pass

# Generated at 2022-06-13 08:13:13.641211
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    host = MagicMock(
        get_name=Mock(return_value='testHost'),
        get_variable=Mock(return_value=dict()),
        get_vars=Mock(return_value=dict()),
        get_groups=Mock(return_value=list()),
        get_group_vars=Mock(return_value={})
    )

# Generated at 2022-06-13 08:13:15.168799
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:13:28.455576
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import HostVars
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    inv_data = {'ldap': {'hosts': ['ldap']}, 'test': {'hosts': ['test']}}
    inv_manager = InventoryManager(loader=None, sources=['localhost'])
    inv_manager.hosts_patterns = ['*']
    inv_manager.hosts = {'ldap': Host(name='ldap'), 'test': Host(name='test')}
    inv_manager.groups = {'ldap': {'hosts': ['ldap']},'test': {'hosts': ['test']}}
    variable_manager

# Generated at 2022-06-13 08:13:38.524061
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role
    from ansible.playbook.play import Play
    from ansible.variable_manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VarsManager
    from ansible.vars.include_vars import IncludeVars
    import os

    task_listen = {
        "listen": "copy_rsyslog_files",
        "name": "Copy rsyslog configuration files to client(s)",
        "include": "./rsyslog_files.yml",
        "notify": "restart_rsyslog"
    }
    block_

# Generated at 2022-06-13 08:13:39.283116
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler_task_include = HandlerTaskInclude()

# Generated at 2022-06-13 08:13:48.500895
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    '''HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)
    Loads a handler from a dictionary'''

    Handler.load = Handler.load(data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)
    Handler.load = Handler.load(data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)
    Handler.load = Handler.load(data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)


# Generated at 2022-06-13 08:13:49.447898
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert HandlerTaskInclude() != None

# Generated at 2022-06-13 08:13:58.628703
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskIncludeLoader
    from ansible.playbook.role import Role
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager

    block = Block()
    role = Role()
    task = Task()
    task_include = TaskIncludeLoader()
    variable_manager = VariableManager()
    data = dict()

    handler = HandlerTaskInclude.load(
        data=data,
        block=block,
        role=role,
        task_include=task_include,
        variable_manager=variable_manager,
        loader=None
    )

# Generated at 2022-06-13 08:14:05.403870
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.task import Task
    from ansible.playbook.attribute import FieldAttribute

    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.playbook.role_include import RoleInclude

    import os
    import yaml
    from ansible.vars.unsafe_proxy import UnsafeProxy


# Generated at 2022-06-13 08:14:19.247512
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    variable_manager = VariableManager()
    loader = variable_manager.loader
    inventory = Inventory(loader=loader, variable_manager=variable_manager)
    host = inventory.get_host('test')
    block_1 = Block()
    task_1 = Task()
    task_include_1 = TaskInclude()

    handler_1 = HandlerTaskInclude(block=block_1, role=task_1, task_include=task_include_1)
    handler_1.task = task_1
    handler_1.task.role = task_include_1
    handler_1

# Generated at 2022-06-13 08:14:46.151966
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    #
    print('\nTESTING HandlerTaskInclude.load(data, block=None, role=None, task_include=None, variable_manager=None, loader=None):')
    #
    data = [{
        "include": {
            "role": {
                "name": "foo"
            },
            "tasks": "bar.yml"
        }
    }]
    handler = HandlerTaskInclude.load(data)
    #
    assert handler.__class__.__name__ == 'HandlerTaskInclude'
    assert handler.task_include.name == 'foo'
    assert handler.task_include.tasks == 'bar.yml'
    assert handler.task_include.static is False
    assert handler.handler_block.name == 'foo'
    assert handler.handler_block.v

# Generated at 2022-06-13 08:14:47.605873
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        "include": "foo.yml"
    }
    handler = HandlerTaskInclude.load(data)
    assert handler

# Generated at 2022-06-13 08:14:58.833837
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    # Note: 'dict' type name is taken from VariableManager._vars
    # 'hosts' is taken from Hosts.pattern
    data = {
        'hosts': 'all',
        'name': 'handler',
        'listen': 'all',
        'include': {'dict': {'var': 'value'}}
    }

    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()

    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    handler = HandlerTaskInclude.load(data, variable_manager=variable_manager, loader=loader)


# Generated at 2022-06-13 08:15:06.768930
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # get parameter data
    file_name = "".join((os.path.dirname(os.path.realpath(__file__)), "/../../tests/data/handlertaskinclude.yml"))
    data = yaml.load(open(file_name).read())
    # get data processed with the static method load
    obj_handler = HandlerTaskInclude.load(data)
    # catch the data we want
    handler = {
        'name': obj_handler.name,
        'include': obj_handler.include
    }
    # here we compare the data got with expected data
    assert handler == data


# Generated at 2022-06-13 08:15:08.019319
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Test with no data.
    assert HandlerTaskInclude.load(None) is None

# Generated at 2022-06-13 08:15:12.380560
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = dict(
        include='hi.yml',
    )
    t = HandlerTaskInclude(block=None, role=None, task_include=None)
    handler = t.check_options(
        t.load_data(data, variable_manager=None, loader=None),
        data
    )
    assert isinstance(handler, HandlerTaskInclude)

# Generated at 2022-06-13 08:15:20.006141
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import os
    import pprint
    import sys
    sys.path.append(os.path.join(os.getcwd(), 'lib'))
    import ansible.playbook.task_include as task_include
    import ansible.playbook.handler as handler
    task = task_include.TaskInclude.load(
        dict(include='other.yml'),
        loader=dict(
            get_basedir=lambda self: '.',
            path_dwim=lambda self, p: '/tmp/' + p,
            _search_path=lambda self, d, p: '/tmp/' + p
        )
    )
    assert isinstance(task, task_include.TaskInclude)


# Generated at 2022-06-13 08:15:21.185572
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    # @todo: write tests for `HandlerTaskInclude.load`
    pass

# Generated at 2022-06-13 08:15:31.599717
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # As of ansible 2.2, HandlerTaskInclude.check_options expects
    # a dict as input
    data = {'include': 'other_handlers.yml'}
    h = HandlerTaskInclude.load(data)

    assert h._block is None
    assert h._role is None
    assert h._task is None
    assert h._invalid_attrs == set()
    assert h._attributes == {}
    assert h._loop == []
    assert h._when == []
    assert h._notify == []
    assert h._changed_when == []
    assert h._failed_when == []
    assert h._run_once is False
    assert h._metadata == []
    assert h._always_run is False
    assert h._local_action is False
    assert h._delegate_to == ''
   

# Generated at 2022-06-13 08:15:41.015932
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = dict(
        headers=dict(
            foo='bar',
        ),
        options=dict(
            foo='bar',
            _terms='foo bar',
        ),
        host_pattern='host',
    )

    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None

    hti = HandlerTaskInclude.load(
        data=data,
        block=block,
        role=role,
        task_include=task_include,
        variable_manager=variable_manager,
        loader=loader,
    )

    with_items = None
    with_dict = None
    with_file = None
    with_sequence = None
    with_subelements = None
    with_first_found = None
    always_run = None


# Generated at 2022-06-13 08:16:20.425144
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # handler = HandlerTaskInclude()
    # assert handler is not None
    assert True


# Generated at 2022-06-13 08:16:29.392023
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():

    # Test HandlerTaskInclude() construct
    # host1 = Host(name="192.168.0.59")
    # host2 = Host(name="192.168.0.67")
    # host3 = Host(name="192.168.0.68")
    # print(host1.__dict__)
    # print(host2.__dict__)
    # print(host3.__dict__)

    # Construct a Host object with name 192.168.0.59
    # host = Host(name="192.168.0.59")
    # print(host.name)

    # Construct a TaskInclude object
    # task_include = TaskInclude()

    # Construct a Task object
    # task = Task()

    # Construct a HandlerTaskInclude object
    handler_task_include = HandlerTaskInclude()


# Generated at 2022-06-13 08:16:31.883180
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    block = 'block'
    role = 'role'
    task_include = 'task_include'

    handlerTaskIncludeObj = HandlerTaskInclude(block=block, role=role, task_include=task_include)
    assert handlerTaskIncludeObj is not None

# Generated at 2022-06-13 08:16:33.261044
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    assert HandlerTaskInclude.load({"include": "test.yml"}, task_include={"key1": "val1"})

# Generated at 2022-06-13 08:16:38.706201
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    block_mock = "block_mock"
    role_mock = "role_mock"
    task_include_mock = "task_include_mock"
    variable_manager_mock = "variable_manager_mock"
    data_mock = "data_mock"
    loader_mock = "loader_mock"
    dict_mock = dict({"key": "value"})
    h = HandlerTaskInclude.load(
        dict_mock,
        block_mock,
        role_mock,
        task_include_mock,
        variable_manager_mock,
        loader_mock
    )

    assert h.block == block_mock
    assert h.role == role_mock
    assert h.load_name == "key"

# Generated at 2022-06-13 08:16:46.490409
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    test_HandlerTaskInclude = HandlerTaskInclude()
    data = {
        'name': 'handler',
        'include': [ 'playbook.yml' ],
        'tags': [ 'always' ]
    }
    result = test_HandlerTaskInclude.load(data)
    assert  result is not None
    assert result._attributes['name'] == 'handler'
    assert result._attributes['include'] == [ 'playbook.yml' ]
    assert result._attributes['tags'] == [ 'always' ]

    data = {
        'include': [ 'playbook.yml' ],
        'tags': [ 'always' ]
    }
    result = test_HandlerTaskInclude.load(data)
    assert  result is not None

# Generated at 2022-06-13 08:16:52.066291
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    from ansible.parsing.yaml.objects import AnsibleMapping
    from ansible.template import Templar
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play_context import PlayContext

    block = AnsibleMapping()
    role = AnsibleMapping()
    task_include = AnsibleMapping()

    variable_manager = VariableManager()
    variable_manager.set_inventory(InventoryManager(loader=None, sources=['localhost']))


# Generated at 2022-06-13 08:17:02.126342
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    '''
    Unit test for method load of class HandlerTaskInclude
    '''
    from ansible.inventory.vars_plugins.yaml import VarsModule as YamlInventory
    from ansible.plugins.loader import loader as plugin_loader  # module_utils
    from ansible.utils.display import Display
    module_utils= plugin_loader.get_all_plugin_loaders('module_utils')
    display = Display()
    data = dict(
        include='main.yml',
    )
    block=None
    role=None
    task_include=None
    # Use empty parameter for function load, don't know how to initialize
    # variable_manager, loader

# Generated at 2022-06-13 08:17:06.384960
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    h = HandlerTaskInclude(block=None, role="test", task_include=None)
    assert h.role == "test"
    assert h.block == None
    assert h.task_include == None
    assert h.VALID_INCLUDE_KEYWORDS == set([u'static', u'name', u'roles', u'recursive'])

# Generated at 2022-06-13 08:17:11.152433
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude()
    assert handler.__class__.__name__ == 'HandlerTaskInclude'
    assert handler.VALID_INCLUDE_KEYWORDS == set(['delegate_to', 'freeze_variables', 'loop', 'loop_control', 'name', 'tags', 'vars', 'when', 'with_', 'listen'])

# Generated at 2022-06-13 08:18:32.709498
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    taskInclude = HandlerTaskInclude(block=None, role=None, task_include=None)
    # HandlerTaskInclude.load has been statically included into the class's namespace, so it's not an instance method
    # but it's still callable
    print(taskInclude.load)
    print(type(taskInclude.load))
    print(taskInclude.VALID_INCLUDE_KEYWORDS)

# Generated at 2022-06-13 08:18:47.131120
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.inventory.host import Host
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.vars.manager import VariableManager
    from ansible.plugins.loader import action_loader
    from ansible.template import Templar
    _host = Host(name="127.0.0.1")
    play_context = PlayContext()
    templar = Templar(loader=None, variables={})
    import os
    class _loader:
        def get_basedir(self, *args, **kwargs): return os.getcwd()
    loader = _loader()
    action_result = object()
    task = Task()
    block = Block()

# Generated at 2022-06-13 08:18:47.936972
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    HandlerTaskInclude()


# Generated at 2022-06-13 08:18:57.228675
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {
        'include': 'my_tasks.txt', 
        'include_role': 'my_role',
        'include_vars': 'my_host.yml',
        'include_tasks': 'my_tasks.txt',
        'import_playbook': 'include_me.yml',
        'import_role': 'my_role2',
        'import_tasks': 'my_tasks.txt' 
    }

    handler = HandlerTaskInclude.load(data)
    print (handler)

if __name__ == '__main__':
    test_HandlerTaskInclude_load()

# Generated at 2022-06-13 08:19:07.229328
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    import os
    import yaml

    # instantiate the required objects
    loader      = DataLoader()
    inventory   = InventoryManager(loader=loader, sources=os.path.join(os.path.dirname(__file__), '../../../test/unit/ansible/inventory/test_hosts'))
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # read the test data

# Generated at 2022-06-13 08:19:07.903144
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:19:11.323114
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # Check with variable_manager as None
    assert HandlerTaskInclude.load(data=dict(), variable_manager=None)
    # Check with variable_manager as <dict>
    assert HandlerTaskInclude.load(data=dict(), variable_manager=dict())

# Generated at 2022-06-13 08:19:18.966239
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.task_include import TaskInclude

    # Create a host
    host = Host(name="test")

    # Create a variable manager for the host
    variable_manager = VariableManager()
    variable_manager.set_inventory(InventoryManager(loader=DataLoader(), sources=''))
    variable_manager.set_host_variable(host, 'ansible_ssh_host', "localhost")

    # load the host with the given data

# Generated at 2022-06-13 08:19:31.938105
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import sys
    import os
    import imp
    file, pathname, description = imp.find_module('ansible.playbook')
    playbook_path = os.path.join(os.path.split(pathname)[0], 'playbook')
    sys.path.append(playbook_path)
    from ansible.playbook.handler import Handler
    from ansible.inventory.host import Host
    from ansible.playbook.task_include import TaskInclude
    from ansible.variable_manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    variable_manager = VariableManager()
    loader = DataLoader()
    data = {}
    data['listen'] = None
    data['name'] = 'test-handler'

# Generated at 2022-06-13 08:19:33.492316
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # HandlerTaskInclude(self, block=None, role=None, task_include=None):
    pass

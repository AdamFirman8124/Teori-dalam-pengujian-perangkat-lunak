

# Generated at 2022-06-13 08:10:01.929942
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    task_include = TaskInclude()
    t = HandlerTaskInclude(block=["vars"], role=["role"], task_include=task_include)

# Generated at 2022-06-13 08:10:06.480344
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # Some constants for the unit test
    host = "host"
    path = 'handler.yml'
    name = 'myname'

    obj = HandlerTaskInclude.load(host=host, path=path, name=name)

    assert(obj is not None)
    assert(obj.name == name)
    assert(obj.path == path)
    assert(obj.host == host)

# Generated at 2022-06-13 08:10:14.443783
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    import ansible.inventory.host
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.utils import context_objects as co
    from ansible.utils.vars import combine_vars

    host = ansible.inventory.host.Host('test_host')
    variable_manager = VariableManager()
    loader = DataLoader()
    inv = InventoryManager(loader, variable_manager, 'test_host')
    variable_manager.set_inventory(inv)


# Generated at 2022-06-13 08:10:20.088608
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    class Block:
        def __init__(self):
            self.parent = None
            self.vars = {
                'foo': 'bar',
                'vars_file': '/tmp/foo.yml',
                'vars_dir': '/tmp/foo.yml',
                'vars_prompt': [
                    {'name': 'foo1'},
                    {'name': 'foo2', 'prompt': 'p1'}
                ],
                'vars_files': ['/tmp/foo1.yml', '/tmp/foo2.yml'],
                'vars_files_0': '/tmp/foo1.yml',
                'vars_files_1': '/tmp/foo2.yml',
                'include': {
                    'listen': True
                }
            }


# Generated at 2022-06-13 08:10:21.418402
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():

    """
    handler = HandlerTaskInclude(block, role, task_include)
    """

# Generated at 2022-06-13 08:10:23.753649
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    t = HandlerTaskInclude()
    assert t.handler_vars == dict()
    assert t._task_includes == list()
    assert t._block is None
    assert t._role is None
    assert t.static is False
    assert t.include_role is None
    assert t.include_file is None
    assert t.include_vars is None
    assert t.include_tasks is None
    assert t.include is None

# Generated at 2022-06-13 08:10:27.198904
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible import inventory
    from ansible.inventory.host import Host
    from ansible.playbook.task import Task

    host = inventory.Inventory()
    host.get_hosts()
    host_vars = host.get_host('127.0.0.1').get_vars()

    block = Task()
    handler = HandlerTaskInclude.load(
        {'include': 'include_task.yml', 'tags': 'tag'},
        block,
        role=None,
        task_include=None,
        variable_manager=None,
        loader=None
    )

# Generated at 2022-06-13 08:10:31.302521
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    expected_handler = HandlerTaskInclude()
    response = HandlerTaskInclude.load(data={
        'include': 'foo.yml'
    })
    assert type(response) == type(expected_handler)
    assert response._role == None
    assert response._block == None

# Generated at 2022-06-13 08:10:32.586379
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    HandlerTaskInclude(None)

# Generated at 2022-06-13 08:10:46.207927
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    handler = Handler.load({'name': 'handler', 'listen': '{{ TEST }}'})
    assert isinstance(handler, Handler)
    assert handler.name == 'handler'
    assert handler._listen == '{{ TEST }}'
    assert isinstance(handler, Handler)

    handler = Handler.load({'name': 'handler', 'listen': '{{ TEST }}'}, block=Block('block_name'))
    assert isinstance(handler, Handler)
    assert handler.name == 'handler'
    assert handler._listen == '{{ TEST }}'
    assert isinstance(handler, Handler)


# Generated at 2022-06-13 08:10:48.808591
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass



# Generated at 2022-06-13 08:11:00.827914
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    '''
        HandlertaskInclude class load method returns the handler
    '''
    # creating mock variables for test
    data = 'test_data'
    variable_manager = 'test variable_manager'
    loader = 'test loader'
    block = 'test block'
    role = 'test role'
    task_include = 'test task_include'
    # creating the mock object
    obj = HandlerTaskInclude(block=block, role=role, task_include=task_include)
    # run
    result = obj.load(data, block=block, role=role, task_include=task_include, variable_manager=variable_manager, loader=loader)
    # assert
    assert(result.__class__.__name__ == 'Handler')

# Generated at 2022-06-13 08:11:07.145545
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleParserError
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.role import Role

    variable_manager = VariableManager()
    loader = DataLoader()

    host = Host(name="testhost")
    group = Group(name="testgroup")
    group.hosts = [host]

    task = Task()
    task._role = Role()

    host.set_variable('ansible_host', '127.0.0.1')
    host.set_variable('ansible_user', 'remote_user')

# Generated at 2022-06-13 08:11:20.662597
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from units.mock.loader import DictDataLoader

    data_loader = DictDataLoader({
        "main_playbook.yml": """
            - hosts: localhost
            - include: other_playbook.yml
              listen: "{{ first_output_var }}"

            - hosts: otherhost
              tasks:
              - debug:
                  var: ansible_play_batch
        """,
        "other_playbook.yml":
            """
            - hosts: localhost
              tasks:
              - debug:
                  msg: "This will be the first output_var"
                  var: echo_hello
                  set_fact:
                    first_output_var: "{{ echo_hello.stdout }}"
            """
    })

    from ansible.vars import VariableManager
    variable_manager = VariableManager()

# Generated at 2022-06-13 08:11:21.454729
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass


# Generated at 2022-06-13 08:11:21.968968
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:11:32.073390
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    # pylint: disable=no-name-in-module,import-error
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    # pylint: enable=no-name-in-module,import-error
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    block = Block(
        parent=Task(),
        role=None,
        task_include='some_task',
        vars=dict()
    )

# Generated at 2022-06-13 08:11:34.180233
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    tasks = ['a','b','c']
    handler = HandlerTaskInclude(tasks=tasks)



# Generated at 2022-06-13 08:11:38.903104
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    # use a set because order is not important
    assert HandlerTaskInclude.VALID_INCLUDE_KEYWORDS == {'include', 'ignore_errors', 'tags', 'when', 'static', 'tasks', 'listen'}

# Generated at 2022-06-13 08:11:41.335586
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    data = {'hosts': 'host_file','tasks': ['foo','bar','baz']}
    HandlerTaskInclude.load(data)

# Generated at 2022-06-13 08:11:45.108792
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    x = HandlerTaskInclude()
    assert x is not None

# Generated at 2022-06-13 08:11:52.227011
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    import json
    import pytest
    #from ansible.plugins.loader import action_loader
    #from ansible.plugins.loader import module_loader
    #from ansible.errors import AnsibleParserError
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    #from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.callback import CallbackBase

    from units.mock.loader import DictDataLoader
    from units.mock.path import mock_unfrackpath_noop


# Generated at 2022-06-13 08:12:05.205267
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from collections import namedtuple
    from ansible.template import Templar
    from ansible.constants import DEFAULT_VAULT_ID_MATCH
    from ansible.parsing.vault import VaultLib
    import six


# Generated at 2022-06-13 08:12:06.076130
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    HandlerTaskInclude.load()

# Generated at 2022-06-13 08:12:10.214673
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = '''
---
- include: ../../tests/handler_tasks/handler_tasks_include2.yml
'''
    h = HandlerTaskInclude()
    handler = h.load(data)
    print(handler)
    assert handler is not None

# --- end of test_HandlerTaskInclude_load ---


# Generated at 2022-06-13 08:12:16.396811
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.parsing.yaml.objects import AnsibleBaseYAMLObject
    from ansible.playbook.attribute import Attribute, FieldAttribute
    from ansible.playbook.attribute import FieldAttribute
    from ansible.playbook.block import Block 
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    import os
    import yaml
    import json
    script_dir = os.path.dirname(__file__)
    rel_path = "HandlerTaskInclude_load_data.yml"
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path, "r") as file:
        data = yaml.load(file)

# Generated at 2022-06-13 08:12:26.858580
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    # mock class for the handler
    class MockHandler:
        def __init__(self):
            self._attributes = dict()
            self._block = None
            self._role = None
            self._task_include = None

        def set_loader(self, loader):
            self._loader = loader

        def load_data(self, ds, variable_manager=None, loader=None):
            return dict()

        def check_options(self, ds, data):
            return dict()

    # mock class for the task include
    class MockTaskInclude:

        VALID_INCLUDE_KEYWORDS = dict()

        def __init__(self):
            self._attributes = dict()
            self._handler = None
            self._role = None
            self._task_include = None


# Generated at 2022-06-13 08:12:34.781405
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    data = {}
    block = Block()
    role = Role()
    task_include = None
    loader = None
    variable_manager = None
    handler = HandlerTaskInclude.load(data, block, role, task_include, variable_manager, loader)

    assert isinstance(handler, HandlerTaskInclude)
    assert isinstance(handler, TaskInclude)
    assert isinstance(handler, Handler)
    assert handler._task_include is None
    assert handler._role == role

# Generated at 2022-06-13 08:12:38.575345
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    file_path='/path/to/handlers.yml'
    variable_manager = None
    loader = None

    handler = HandlerTaskInclude.load(file_path, variable_manager=variable_manager, loader=loader)
    assert handler.__class__.__name__ == 'HandlerTaskInclude'

# Generated at 2022-06-13 08:12:45.253622
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # Test for empty dict
    handler = HandlerTaskInclude()
    assert isinstance(handler, HandlerTaskInclude)
    # Test for key 'name'
    handler = HandlerTaskInclude(name='test-name')
    assert handler.name == 'test-name'
    # Test for key 'action'
    handler = HandlerTaskInclude(action='test-action')
    assert handler.action == 'test-action'
    # Test for key 'args'
    handler = HandlerTaskInclude(args='test-args')
    assert handler.args == 'test-args'
    # Test for key 'static'
    handler = HandlerTaskInclude(static='test-static')
    assert handler.static == 'test-static'

# Generated at 2022-06-13 08:12:55.787430
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = '''
    - debug:
        msg: "This is a handler."
    '''
    import pprint
    handler_task_include = HandlerTaskInclude.load(data)
    pprint.pprint(handler_task_include.__dict__)

if __name__ == '__main__':
    test_HandlerTaskInclude_load()

# Generated at 2022-06-13 08:12:56.472256
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    HandlerTaskInclude()

# Generated at 2022-06-13 08:13:10.812406
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    _loader = 'fake_loader'
    _variable_manager = 'fake_variable_manager'
    _block = 'fake_block'
    _role = 'fake_role'
    _task_include = 'fake_task_include'

    _data = {
        'when': 'fake_when',
        'include': {},
    }

    _validated_data = {
        'when': 'fake_when',
    }

    _task = HandlerTaskInclude(
        block=_block,
        role=_role,
        task_include=_task_include
    )

    _task.check_options = MagicMock()

    _task.load_data = MagicMock(return_value=_validated_data)


# Generated at 2022-06-13 08:13:12.900280
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    #TODO(Nishant): Write test cases for method load of class HandlerTaskInclude
    pass

# Generated at 2022-06-13 08:13:19.589080
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # data for test
    data = {
      "include" : "some_file"
    }
    block = None
    role = None
    task_include = None
    variable_manager = None
    loader = None

    # method test
    obj = HandlerTaskInclude(block=block, role=role, task_include=task_include)
    handler = obj.check_options(
            obj.load_data(data, variable_manager=variable_manager, loader=loader),
            data
        )
    
    # assert result
    # assert handler.do_include()

# Generated at 2022-06-13 08:13:21.057982
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():

    print()
    # TODO: implement unit test


# Generated at 2022-06-13 08:13:22.436837
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    assert TaskInclude.load
    assert TaskInclude.VALID_INCLUDE_KEYWORDS

# Generated at 2022-06-13 08:13:32.834609
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader


# Generated at 2022-06-13 08:13:41.103900
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, sources=['test/unit/lib/ansible/inventory/test_data/host_vars/'])
    variable_manager.set_inventory(inventory)

    task_include_data = dict(
        name='test',
        static='yes',
        delegate_to='test_delegate_to',
        when='test_when',
        with_items='test_with_items'
    )

    handler_data = dict(
    )


# Generated at 2022-06-13 08:13:42.411195
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    pass

# Generated at 2022-06-13 08:13:52.718181
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    pass

# Generated at 2022-06-13 08:13:54.454784
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    # assert one == 1
    assert True == True


# Generated at 2022-06-13 08:13:57.249483
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    my_class = HandlerTaskInclude()
    assert (HandlerTaskInclude.VALID_INCLUDE_KEYWORDS == my_class.VALID_INCLUDE_KEYWORDS)

# Generated at 2022-06-13 08:14:00.131737
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    handler = HandlerTaskInclude.load({
        'include': 'test.yml',
        'listen': 'test_event'
    })

    assert handler.task_include is not None
    assert handler.task_include.include == 'test.yml'
    assert 'listen' not in handler.task_include.include_vars

# Generated at 2022-06-13 08:14:03.027653
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = {}
    h = HandlerTaskInclude.load(data)

    assert isinstance(h,HandlerTaskInclude)
    assert h._task_blocks == []
    assert h._included_files == []
    assert h._block is None
    assert h._role is None

# Generated at 2022-06-13 08:14:14.627351
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    '''
    Unit test for constructor of class HandlerTaskInclude
    '''
    t = HandlerTaskInclude(block=None, role=None, task_include=None)
    handler = t.load(data={
        'include': 'some_file.yml',
    })

    assert handler.get_name() == 'some_file.yml'
    assert handler.get_parent_block() is None
    assert handler.get_role() is None
    assert handler.is_handler()
    assert handler.always_run == False
    assert handler.only_if == None

    assert handler.get_include_params() == {}
    assert handler.get_tasks() == []

# Generated at 2022-06-13 08:14:21.473587
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    yaml_data = """
- name: "This is a task"
  shell: "this is some command"
  notify:
  - handler1
  - handler2
"""
    handler_data1 = """
- name: handler1
  command: handler1 command
"""
    handler_data2 = """
- name: handler2
  command: handler2 command
"""
    h1 = Handler.load(handler_data1)
    h2 = Handler.load(handler_data2)

    assert not h1.name == h2.name, "Name of handler is incorrect"



# Generated at 2022-06-13 08:14:22.310793
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    pass

# Generated at 2022-06-13 08:14:23.386433
# Unit test for constructor of class HandlerTaskInclude
def test_HandlerTaskInclude():
    # TODO
    pass

# Generated at 2022-06-13 08:14:30.442028
# Unit test for method load of class HandlerTaskInclude
def test_HandlerTaskInclude_load():
    data = dict()
    data["name"] = "name"
    data["include"] = "include"
    data["ignore_errors"] = True
    data["tags"] = "tags"
    data["register"] = "register"
    data["freeze_variables"] = True
    data["when"] = "True"
    data["loop"] = "loop"
    data["listen"] = "listen"

    block = list()

    role = dict()
    role["name"] = "name"
    role["filename"] = "filename"
    role["metadata"] = "metadata"

    task_include = dict()
    task_include["action"] = "action"
    task_include["args"] = "args"
    task_include["listen"] = "listen"

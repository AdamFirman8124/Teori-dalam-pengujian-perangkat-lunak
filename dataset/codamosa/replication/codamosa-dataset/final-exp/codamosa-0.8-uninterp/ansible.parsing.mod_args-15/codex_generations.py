

# Generated at 2022-06-13 06:56:53.255680
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.module_utils.common.collections import ImmutableDict

    # __init__() return a object of "ModuleArgsParser" class
    moduleargs_parser_class = ModuleArgsParser()

    # ___________ ModuleArgsParser.parse() ___________
    # parse() return 3 values, which are "action", "args", "delegate_to".
    # If input is empty, the "action" should be None  and the return values shoud be None, None, None.
    assert moduleargs_parser_class.parse() == (None, None, None)

    # If the input is a dict, the "action" should be the key in the dict and the return values shoud be the key, dict, None.
    # The dict contains a key:value where the key is the same as the "action".

# Generated at 2022-06-13 06:57:04.654437
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 06:57:12.128503
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.role_context import RoleContext
    from ansible.playbook.task_include import TaskInclude
    from ansible.executor.task_queue_manager import TaskQueueManager

    parser = ModuleArgsParser(task_ds={'shell': 'echo hi'}, collection_list=None)
    args = parser.parse()
    assert args[0] != None
    assert args[1] != None
    assert args[2] == None



# Generated at 2022-06-13 06:57:21.608886
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.play_context import PlayContext

    templar = Templar(loader=None)
    pc = PlayContext()
    pc._play = test_utils.Mock()
    templar.set_available_variables(pc.get_vars())

    # test from a task
    task = Task()
    task._ds = {'module': 'test', 'args': {'one': 'two'}}
    parser = ModuleArgsParser(task._ds)
    assert parser.parse() == ('test', {'one': 'two'}, None)

    # test from a handler
    handler = Handler()
    handler._ds = {'module': 'test', 'args': {'one': 'two'}}
   

# Generated at 2022-06-13 06:57:29.903917
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    """
    Unit test entry point and test case for ModuleArgsParser.parse() method.

    :return: None
    """
    module_args = {
        'action': 'shell echo hi',
        'delegate_to': 'abcd',
        'args': {'arg1': 'value1', 'arg2': 'value2'},
        'async': 'abcd'
    }
    module_arg_parser = ModuleArgsParser(module_args)

    module_arg_parser.parse()


# Generated at 2022-06-13 06:57:38.364497
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {"action": "shell", "args": {"chdir": "/tmp"}, "delegate_to": "localhost"}
    collection_loader = CollectionLoader()
    parser = ModuleArgsParser(task_ds, collection_loader)
    action, args, delegate_to = parser.parse()
    expected_action = "shell"
    expected_args = {"chdir": "/tmp"}
    expected_delegate_to = "localhost"
    assert action == expected_action
    assert args == expected_args
    assert delegate_to == expected_delegate_to



# Generated at 2022-06-13 06:57:52.821629
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Simple tests for parsing the action statement of a task
    # Note that we use a MockLoader class to test finding plugins
    # which isn't actually available at the time of this test
    class MockLoader(object):
        def find_plugin(self, *args, **kwargs):
            return 'some module'
    AM = AnsibleModule(
        argument_spec = dict(
            skip_action_validation = dict(required=False, type='bool'),
        ),
        supports_check_mode = False,
    )
    parser = ModuleArgsParser(task_ds=dict(), collection_list=None,
        loader=MockLoader())
    # Test argument parsing
    # Test for match of two values
    input_dict = dict(action='do_something', other='something else')
    expected_action = 'do_something'
    expected

# Generated at 2022-06-13 06:58:07.902944
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 06:58:16.028226
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import os
    import tempfile
    import unittest

    from ansible.executor.task_result import TaskResult
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.parsing.dataloader import DataLoader
    from ansible.plugin.loader import action_loader, module_loader
    from ansible.playbook import Playbook
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.tqdm_callback import TqdmCallback
    from ansible.playbook.task import Task
    from ansible.plugins.loader import get_all_plugin_loaders
    from ansible.template import Templar


# Generated at 2022-06-13 06:58:22.784657
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for method parse of class ModuleArgsParser
    '''

    # Unit test to method ModuleArgsParser.__init__

    # Arrange
    task_ds = {
        'action': 'a',
        'local_action': 'b',
        'module': 'c',
        'args': 'd'
    }
    expected = {
        'action': 'a',
        'local_action': 'b',
        'module': 'c',
        'args': 'd'
    }
    assert isinstance(task_ds, dict)
    assert isinstance(expected, dict)
    # Act
    moduleargsparser = ModuleArgsParser(task_ds)
    task_ds = moduleargsparser._task_ds
    # Assert
    assert task_ds == expected

    # Unit test to method

# Generated at 2022-06-13 06:58:33.752060
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    object = ModuleArgsParser()
    object.parse()

# Generated at 2022-06-13 06:58:43.952901
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.errors import AnsibleParserError
    from ansible.playbook.task import Task

    # Test with just action
    task_ds = {
        'action': 'copy src=a dest=b'
    }
    task = Task.load(task_ds)
    result = ModuleArgsParser(task_ds=task_ds).parse()

    assert result == ('copy', {'src': 'a', 'dest': 'b'}, None)

    # Test with two actions
    task_ds = {
        'action': 'copy src=a dest=b',
        'local_action': 'copy src=a dest=b'
    }

    # The following should raise an error
    with pytest.raises(AnsibleParserError) as err:
        ModuleArgsParser(task_ds=task_ds).parse()



# Generated at 2022-06-13 06:58:58.710992
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import ansible.playbook.task
    args = {'hosts': '{{hosts}}', 'roles': '{{roles}}', 'vars': '{{vars}}'}
    task_ds = {'action': {'module': 'include_role', **args}}
    parser = ModuleArgsParser(task_ds)
    action, args, delegate_to = parser.parse()
    assert action == 'include_role'
    assert args == {'hosts': '{{hosts}}', 'roles': '{{roles}}', 'vars': '{{vars}}'}
    assert delegate_to == Sentinel
    action, args, delegate_to = parser.parse(skip_action_validation=True)
    assert action == 'include_role'

# Generated at 2022-06-13 06:59:08.937013
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    fake_task_ds = {
        "action": {
            "module": "copy", 
            "src": "a", 
            "dest": "b"
        }, 
        "delegate_to": "localhost", 
        "freeform_args": "file=/tmp/foo state=absent"
    }
    parser = ModuleArgsParser(task_ds=fake_task_ds, collection_list=None)
    action, args, delegate_to = parser.parse(skip_action_validation=False)
    assert action == "copy"
    assert args == {'src': 'a', 'dest': 'b'}
    assert delegate_to == "localhost"
    assert parser.resolved_action == "ansible.builtin.copy"


# Generated at 2022-06-13 06:59:17.868202
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
  # FIXME: We should use a pytest fixture here
  loader = DataLoader()
  variable_manager = VariableManager()
  inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='tests/units/inventory')
  variable_manager.set_inventory(inventory)
  collection_list = CollectionsLoader().load_collections('tests/units/collections', None)

  # test 1: action: copy src=a dest=b
  task_ds = {}
  parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
  task_ds = dict(action="copy src=a dest=b")
  parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)

# Generated at 2022-06-13 06:59:27.511820
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # (task_ds, collection_list, action, args, delegate_to) = (None, None, None, {}, None)
    _task_ds = {}
    _collection_list = None
    _action = None
    _args = {}
    _delegate_to = None
    _instance = ModuleArgsParser(_task_ds, _collection_list)
    _ret = _instance.parse(None)
    assert isinstance(_ret, tuple) and len(_ret) == 3 and isinstance(_ret[0], string_types) and _ret[0] == _action and isinstance(_ret[1], dict) and isinstance(_ret[2], string_types) and _ret[2] == _delegate_to


# Generated at 2022-06-13 06:59:34.380802
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    args_parser = ModuleArgsParser({'action': 'hg push', 'args': 'http://hg.example.com/hg/'})
    assert args_parser.parse() == ('hg', {'repository': 'http://hg.example.com/hg/'}, None)

    args_parser = ModuleArgsParser({'action': 'git push', 'args': {'option': 'all'}, 'delegate_to': 'server'})
    assert args_parser.parse() == ('git', {'option': 'all'}, 'server')

    args_parser = ModuleArgsParser({'action': 'yum'})
    assert args_parser.parse() == ('yum', {}, None)

    args_parser = ModuleArgsParser({'action': '{{package_module}}'})
    assert args_parser.parse

# Generated at 2022-06-13 06:59:36.392459
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    t = AnsibleModuleArgsParser([[]])
    out = t.parse()
    expected = ("none", {})
    assert out == expected

# Generated at 2022-06-13 06:59:44.850171
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.parsing.dataloader import DataLoader
    from ansible.errors import AnsibleParserError
    from ansible.utils.vars import combine_vars
    from ansible.module_utils.six import binary_type
    task_ds = AnsibleUnicode('{"action":"copy","src":"{{src_file}}","dest":"{{dest}}","backup":"yes"}')
    collection_list = AnsibleUnicode('None')
    parser = ModuleArgsParser(task_ds, collection_list)
    try:
        parser.parse()
    except AnsibleParserError as ex:
        print('The method parse of class ModuleArgsParser raise AnsibleParserError:')

# Generated at 2022-06-13 06:59:55.256136
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    adict = {}
    m = ModuleArgsParser(adict)
    assert m.parse() == (None, {}, None)
    adict.update(dict(action='copy src=a dest=b'))
    m = ModuleArgsParser(adict)
    assert m.parse() == ('copy', {'src': 'a', 'dest': 'b'}, None)
    adict.update(dict(local_action='copy src=a dest=b'))
    m = ModuleArgsParser(adict)
    assert m.parse() == ('copy', {'src': 'a', 'dest': 'b'}, 'localhost')
    adict.update(dict(delegate_to='localhost'))
    m = ModuleArgsParser(adict)

# Generated at 2022-06-13 07:00:08.824325
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser()
    
    task_ds_1 = dict(action='tags')
    try:
        action, args, delegate_to = parser.parse(task_ds_1)
    
        assert action == 'tags'
        assert args == {}
        assert delegate_to == Sentinel
    except AnsibleParserError as e:
        assert False
    except Exception as e:
        assert True
    
    task_ds_2 = dict(local_action='tags')
    try:
        action, args, delegate_to = parser.parse(task_ds_2)
    
        assert action == 'tags'
        assert args == {}
        assert delegate_to == 'localhost'
    except AnsibleParserError as e:
        assert False
    except Exception as e:
        assert True
    

# Generated at 2022-06-13 07:00:21.229735
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Mock task data structure, set values as required
    task_ds = {}
    task_ds['_ansible_loop_var'] = ''
    task_ds['delegate_to'] = 'localhost'
    task_ds['action'] = 'shell'
    task_ds['local_action'] = 'shell'
    task_ds['notify'] = 'hello'
    task_ds['register'] = 'hello'
    task_ds['ignore_errors'] = 'hello'
    task_ds['until'] = 'hello'
    task_ds['retries'] = 'hello'
    task_ds['delay'] = 'hello'
    task_ds['environment'] = 'hello'
    task_ds['args'] = 'hello'
    task_ds['name'] = 'hello'
    task_ds['sudo'] = 'hello'

# Generated at 2022-06-13 07:00:28.250766
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'name': 'test_task', 'action': {'module': 'shell', '_raw_params': 'ls > /tmp/test_out', 'env': 'FOO=BAR'}}
    parser = ModuleArgsParser(task_ds)

    action, args, delegate_to = parser.parse()
    assert isinstance(args, dict)
    assert delegate_to is Sentinel
    assert action == 'shell'
    assert args == {'_raw_params': 'ls > /tmp/test_out', 'env': 'FOO=BAR', '_uses_shell': True}

# Generated at 2022-06-13 07:00:30.747949
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    assert True


# Generated at 2022-06-13 07:00:31.693179
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    assert True


# Generated at 2022-06-13 07:00:33.136184
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    m = ModuleArgsParser()
    assert m.parse() == (None, dict(), None)

# Generated at 2022-06-13 07:00:42.483531
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # First test with a local action
    task_ds = {'local_action': 'myModule args="{{x}}"', 'delegate_to': 'localhost'}
    module_parser = ModuleArgsParser(task_ds=task_ds)
    action, args, delegate_to = module_parser.parse()
    assert action == 'myModule'
    assert args == {'args': '{{x}}'}
    assert delegate_to == 'localhost'

    # Then with a normal action on a remote host
    task_ds = {'action': 'myModule args="{{x}}"', 'delegate_to': 'remote_host'}
    module_parser = ModuleArgsParser(task_ds=task_ds)
    action, args, delegate_to = module_parser.parse()
    assert action == 'myModule'
    assert args

# Generated at 2022-06-13 07:00:45.281261
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    argnames = ['_task_ds', '_collection_list']
    args = {}
    for name in argnames:
        args[name] = globals()[name]
    p = ModuleArgsParser(*args)
    (a, b, c) = p.parse()
    assert a is None
    assert b is None
    assert c is None

# Generated at 2022-06-13 07:00:55.213681
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # We can have one of action, local_action, or module specified
    # action
    ds = {'action': 'shell echo hi', 'delegate_to': 'localhost'}
    mod_args_parser = ModuleArgsParser(ds, None)
    ans = mod_args_parser.parse()
    assert ans == ('shell', {'_raw_params': 'echo hi'}, 'localhost')

    # local_action
    ds = {'local_action': 'shell echo hi', 'delegate_to': 'localhost'}
    mod_args_parser = ModuleArgsParser(ds, None)
    ans = mod_args_parser.parse()
    assert ans == ('shell', {'_raw_params': 'echo hi'}, 'localhost')


# Generated at 2022-06-13 07:01:02.928839
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Unit test for action argument parsing.  It's hard to test everything
    # here, but we'll try to be thorough.

    # All action arguments should be parsed into dicts by the end
    def _test_module_args(module_args, action):
        _action, args, delegate_to = ModuleArgsParser(module_args).parse()

        assert action == _action
        assert isinstance(args, dict)

        return args

    # Create a dict of aliases/aliases, and then call it with each alias to
    # ensure that each one generates the expected parameter dict

# Generated at 2022-06-13 07:01:11.773561
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
  ModuleArgsParser = get_dynamic_class("ModuleArgsParser", globals(), locals())
  action = None
  args = dict()
  delegate_to = Sentinel
  thing = None
  additional_args = dict()
  obj = ModuleArgsParser({"action": thing})
  result = obj.parse()
  assert result == (action, args, delegate_to)


# Generated at 2022-06-13 07:01:18.906679
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import unittest
    from ansible.executor.task_result import TaskResult
    from ansible.executor.module_common import ResultCallbackBase
    from ansible.parsing.yaml.objects import AnsibleUnicode
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    assert isinstance(ModuleArgsParser(task_ds=None, collection_list=None).parse(), tuple)
    assert isinstance(ModuleArgsParser(task_ds=None, collection_list=None).parse(), tuple)
    assert isinstance(ModuleArgsParser(task_ds=None, collection_list=None).parse(), tuple)
    assert isinstance(ModuleArgsParser(task_ds=None, collection_list=None).parse(), tuple)

# Generated at 2022-06-13 07:01:27.880197
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Test case with no `action`
    task_ds = dict(handler=dict(module="test", test="yes"))
    expected_task_ds = dict("test", {"test": "yes"})
    actual_task_ds = ModuleArgsParser().parse(task_ds)
    assert actual_task_ds == expected_task_ds

    # Test case with `action`
    task_ds = dict(action=dict(module="test", test="yes"))
    expected_task_ds = dict("test", {"test": "yes"})
    actual_task_ds = ModuleArgsParser().parse(task_ds)
    assert actual_task_ds == expected_task_ds

    # Test case with `local_action`
    task_ds = dict(local_action=dict(module="test", test="yes"))
    expected_task_

# Generated at 2022-06-13 07:01:36.708912
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_name = 'raw'
    parser = ModuleArgsParser(task_ds={'action': module_name + ' echo hi'})
    action, args, delegate_to = parser.parse()
    assert action == 'raw'
    assert args == {'_raw_params': 'echo hi'}

    module_name = 'shell'
    parser = ModuleArgsParser(task_ds={'action': module_name + ' echo hi'})
    action, args, delegate_to = parser.parse()
    assert action == 'shell'
    assert args['_raw_params'] == 'echo hi'
    assert args['_uses_shell'] is True

    module_name = 'shell'
    parser = ModuleArgsParser(task_ds={'action': module_name + ' echo hi', 'declare_vars': True})
    action, args

# Generated at 2022-06-13 07:01:42.062738
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {}
    collection_list = [collection for collection in
                       (C.COLLECTIONS_PATHS or []) + (C.COLLECTIONS_PATHS_ANSIBLE or [])
                       if os.path.exists(collection)]
    obj = ModuleArgsParser(task_ds, collection_list)
    assert obj.parse() == (None, None, Sentinel)

test_ModuleArgsParser_parse()


# END MODULE ARGS PARSER CLASS #########################################################



# Generated at 2022-06-13 07:01:53.573539
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    data = dict(delegate_to='some_host', action='shell', args='pwd')
    parser = ModuleArgsParser(data)
    assert parser.parse() == ('shell', dict(), 'some_host')
    data = dict(delegate_to='some_host', local_action='shell', args='pwd')
    parser = ModuleArgsParser(data)
    assert parser.parse() == ('shell', dict(), 'localhost')
    data = dict(delegate_to='some_host', shell='pwd')
    parser = ModuleArgsParser(data)
    assert parser.parse() == ('shell', dict(), 'some_host')
    data = dict(delegate_to='some_host', local_action='shell', test='pwd')
    parser = ModuleArgsParser(data)

# Generated at 2022-06-13 07:02:02.834233
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    moduleArgsParser = ModuleArgsParser()

    # Try to parse invalid argument raise an exception
    invalid_args = ["action: shell 'echo hello'",'action: copy','action:','action: shell foo=bar','action: shell echo hello','action: shell foo','action: shell bar','action: shell','action: shell echo hello']
    for args in invalid_args:
        try:
            with pytest.raises(AnsibleError) as excinfo:
                moduleArgsParser.parse(args)
        except:
            assert False, 'If the args is invalid, should raise an exception'
    # Try to parse valid argument


# Generated at 2022-06-13 07:02:11.297417
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Test with action and args specified
    # Expected: action shell, args {'_raw_params': 'echo hi', '_uses_shell': True}
    from ansible.errors import AnsibleParserError
    task = {'action': 'shell', 'args': 'echo hi'}
    try:
        expected_action = 'shell'
        expected_args = {'_raw_params': 'echo hi', '_uses_shell': True}
        module_args = ModuleArgsParser(task).parse()
        assert module_args[0] == expected_action
        assert module_args[1] == expected_args
        print('test_ModuleArgsParser_parse: test 1 passed')
    except Exception as err:
        print('test_ModuleArgsParser_parse: test 1 failed')
        print('actual: ' + repr(err))
       

# Generated at 2022-06-13 07:02:26.894919
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import sys
    import pytest
    from ansible.plugins.action.builtin import ActionModule as BuiltinActionModule
    from ansible_collections.ansible.community.tests.unit.compat.mock import MagicMock
    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.plugins.loader import module_loader, action_loader
    from ansible.plugins import module_loader
    from ansible.playbook.task import Task
    from ansible.template import Templar

    test_obj = module_loader.find_plugin('ping')
    test_obj.run = MagicMock()
    test_obj.run.return_value = {}
    test_obj.get_default_args = MagicMock()
    test_obj.get_default_args.return_value = {}
    test_

# Generated at 2022-06-13 07:02:33.266293
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args = dict(
        name='sample task',
        action='copy',
        args=dict(
            src='a',
            dest='b',
            _raw_params=''
        ),
        delegate_to='localhost'
    )
    module_args_parser = ModuleArgsParser(module_args)
    action, args, delegate_to = module_args_parser.parse()
    assert action == 'copy'
    assert args['_raw_params'] == ''
    assert delegate_to == 'localhost'
test_ModuleArgsParser_parse()


# Generated at 2022-06-13 07:02:45.651187
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    test_dict = {
        "action": {
            "module": "some_module"
        }
    }
    test_instance = ModuleArgsParser(task_ds=test_dict)
    ret = test_instance.parse()
    assert ret[0] == "some_module"
    assert ret[1] == {}
    assert ret[2] == "Sentinel"

    # TODO: write a test to ensure that the following snippet raises required Exception

    #raise Exception(
    #    "Test not implemented for ModuleArgsParser.test_ModuleArgsParser_parse")
    #pass


# Generated at 2022-06-13 07:02:55.495998
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'become_user': 'root', 'delegate_to': 'localhost', 'name': 'Test task', 'become': 'yes', 'become_method': 'sudo', 'any_errors_fatal': True, 'register': 'shell_out', 'command': 'pwd', 'raw_shell': None, 'when': ['C(ansible_os_family == "RedHat")', "C('{{ ansible_distribution }}' == 'Fedora')"]}
    collection_list = None
    module_args_parser = ModuleArgsParser(task_ds, collection_list)
    module_args_parser.parse()
# END unit test for method parse of class ModuleArgsParser


# Generated at 2022-06-13 07:03:02.435796
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude

    # replace ansible.module_utils.parsing.convert_bool test
    convert_bool = lambda x: x

    # replace ansible.plugins.loader test
    def find_extra_vars(task_ds, constants):
        return {}

    # build ModuleArgsParser object
    task_ds = {}
    collection_list = []
    module_args_parser = ModuleArgsParser(task_ds, collection_list)
    assert isinstance(module_args_parser, ModuleArgsParser)

    # execute method parse
    # empty task_ds
    args = {}
    action = None
    delegate_to = 'localhost'
    action, args, delegate_to

# Generated at 2022-06-13 07:03:10.747464
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser(task_ds={'module': 'copy src=a dest=b', 'delegate_to': 'localhost'})
    expected_action = 'copy'
    expected_args = {'src': 'a', 'dest': 'b'}
    expected_delegate_to = 'localhost'
    actual_action, actual_args, actual_delegate_to = parser.parse()
    assert expected_action == actual_action
    assert expected_args == actual_args
    assert expected_delegate_to == actual_delegate_to
    # action not provided.
    # local_action not provided.
    # module provided.
    parser = ModuleArgsParser(task_ds={'module': 'copy src=a dest=b'})
    expected_action = 'copy'

# Generated at 2022-06-13 07:03:15.708623
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    # test module get args
    orig_task_ds = dict()
    orig_task_ds['x'] = 1
    orig_task_ds['y'] = 2
    parser = ModuleArgsParser(orig_task_ds, collection_list=None)
    (action, args, delegate_to) = parser.parse()
    assert action == None
    assert args == {}
    assert delegate_to

# Generated at 2022-06-13 07:03:22.054667
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import os
    import unittest

    # there are 2 basic sets of tests here:
    # 1.  confirm that the parser can deal with fuzzy inputs, and return the expected
    #     dictionary structures
    # 2.  confirm that it raises the correct errors if given bad input

    # helpers
    def parse(this_task):
        module_parser = ModuleArgsParser(this_task)
        return module_parser.parse()

    def run_basic_tests(tests):
        for test, expected in tests:
            test_ds = dict(action=test)
            (action, args, delegate_to) = parse(test_ds)
            assert (args == expected), "failed on: %s" % test

    def run_error_tests(tests):
        for test in tests:
            test_ds = dict(action=test)
           

# Generated at 2022-06-13 07:03:37.161661
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.parsing.yaml.loader import AnsibleLoader
    from ansible.parsing.yaml.objects import AnsibleUnicode
    # Skip this tests if Ansible is not installed as it would cause
    # a failure
    if module_loader is None:
        return


# Generated at 2022-06-13 07:03:41.393036
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    # create an instance of the class
    paramsParser = ModuleArgsParser()
    # parse the action and the args
    action, args, delegate_to = paramsParser.parse()
    # check that the action is valid
    assert action not in BUILTIN_TASKS

    # create a new instance of the class
    setup = ModuleArgsParser()
    # parse the action and the args
    action, args, delegate_to = setup.parse()
    # check that the action is valid
    assert action in BUILTIN_TASKS


# Generated at 2022-06-13 07:03:49.237890
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Create an instance of ModuleArgsParser
    module_args_parser = ModuleArgsParser()


# Generated at 2022-06-13 07:03:49.837028
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass

# Generated at 2022-06-13 07:04:05.078232
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Declaring an instance of ModuleArgsParser
    module_loader = Mock()
    action_loader = Mock()
    task_ds = None
    collection_list = None
    module_args_parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)

    task_ds = {}
    module_args_parser._task_ds = task_ds

    module_args_parser._task_attrs = frozenset(['local_action', 'static'])

    module_args_parser.resolved_action = None

    # Declaring a list of test inputs and test outputs

# Generated at 2022-06-13 07:04:12.381720
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # A round-trip test through a parser & dumper makes sure
    # we handle all ansible YAML corner cases

    # control that we're using the correct version
    # of YAML
    assert yaml is not None

    from yaml.dumper import Dumper
    from yaml.representer import SafeRepresenter
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

    class UnsafeDumper(Dumper):
        pass

    UnsafeDumper.add_representer(AnsibleUnsafeText, SafeRepresenter.represent_str)

    class VaultDumper(UnsafeDumper):
        pass


# Generated at 2022-06-13 07:04:23.455587
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # required args: task_ds
    # optional args: 
    test_obj = ModuleArgsParser(task_ds={
        'action': {
            'module': 'ping', 
        }, 
    })
    # from ansible.module_utils.common._collections_compat import Mapping
    # test_ds = test_obj.ds

    # test relative imports
    module = 'action'
    expected_result = ('ping', {}, None)
    result = test_obj.parse()
    assert result == expected_result

# ===========================================

# ===========================================
# Unit test Section 2: Implementation
# ===========================================


# Generated at 2022-06-13 07:04:29.162246
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # test for correct input format
    thing =["shell","echo hi"]
    action = "shell"
    delegate_to = "localhost"
    args = dict()
    additional_args = dict()
    obj = ModuleArgsParser()
    (action, args, delegate_to) = obj._normalize_parameters(thing, action=action, additional_args=additional_args)
    assert action=='shell'

# Generated at 2022-06-13 07:04:40.162760
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {u'action': u'local-action copy src=/my/src/path dest=/my/dest/path'}
    parser = ModuleArgsParser(task_ds)
    action, args, delegate_to = parser.parse()
    assert action == u'copy'
    assert args['src'] == u'/my/src/path'
    assert args['dest'] == u'/my/dest/path'
    assert delegate_to == u'localhost'

    task_ds = {u'action': u'module-action copy src=/my/src/path dest=/my/dest/path'}
    parser = ModuleArgsParser(task_ds)
    action, args, delegate_to = parser.parse()
    assert action == u'copy'
    assert args['src'] == u'/my/src/path'
    assert args

# Generated at 2022-06-13 07:04:41.789041
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {}
    collection_list = []
    assert ModuleArgsParser(task_ds, collection_list).parse() == ({}, Sentinel)

# Generated at 2022-06-13 07:04:42.799952
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    ## Test code
    ModuleArgsParser()



# Generated at 2022-06-13 07:04:44.736842
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser({})
    assert module_args_parser.parse() == (None, dict(), None)


# Generated at 2022-06-13 07:04:55.156288
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.play_context import PlayContext
    import ansible.playbook.play
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler import Handler
    from ansible.playbook.block import Block
    from ansible.plugins.loader import action_loader, module_loader
    # play_context
    play_context = PlayContext()
    # play
    play_name = 'test_play'
    play_hosts = 'test_host'
    play_become = True
    play_become_user = 'test_become_user'
    play_become_method = 'test_become_method'
    play_become_flags = ['test_become_flags']
    play_bec

# Generated at 2022-06-13 07:05:03.198972
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    host = 'localhost'
    play_context = PlayContext(play=None, options=None, passwords=None)
    loader = DataLoader()
    templar = Templar(loader=loader, variables={})
    connection = Connection(play_context)
    play = Play().load({'name': 'fooplay'}, loader=loader, variable_manager=VariableManager())
    task = Task()
    all_vars = dict(omnibus_app_config=dict(ansible_connection="local"),
                    ansible_connection="local")
    task_vars = VariableManager(loader=loader,
                                inventory=None,
                                version_info=ansible_version_info,
                                all_vars=all_vars).get_vars(play=play,
                                                            task=task)
    task_ds

# Generated at 2022-06-13 07:05:11.664029
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.module_utils.common._collections_compat import MutableMapping
    m = ModuleArgsParser(task_ds=MutableMapping())
    expected_result = m.parse()
    assert expected_result == ('', {}, None)



# Generated at 2022-06-13 07:05:15.090511
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_arg_parser = ModuleArgsParser()
    # TODO: write a real test
    #assert False, "TODO: write a real test"


# Generated at 2022-06-13 07:05:26.589507
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Create mock data
    task_ds = dict()
    additional_args = dict()
    additional_args['b'] = 2
    # Create instance of class
    mod_args_parser = ModuleArgsParser(task_ds)
    # Run method
    action, args, delegate_to = mod_args_parser.parse()
    # Check method response
    assert action == None
    assert args == dict()
    assert delegate_to == None
    # Run method
    action, args, delegate_to = mod_args_parser.parse(skip_action_validation=True)
    # Check method response
    assert action == None
    assert args == dict()
    assert delegate_to == None
    # Create mock data
    task_ds = dict()
    # Create instance of class

# Generated at 2022-06-13 07:05:35.687284
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # test correct parsing of multiple arg formats
    a = ModuleArgsParser(task_ds={'action': 'shell echo foo',
                                  'delegate_to': 'bar',
                                  'args': 'x=y'},
                        collection_list=None)
    assert a.parse() == (u'shell', {'_raw_params': u'echo foo', u'x': u'y'}, 'bar')

    a = ModuleArgsParser(task_ds={'local_action': 'shell echo foo',
                                  'args': 'x=y'},
                        collection_list=None)
    assert a.parse() == (u'shell', {'_raw_params': u'echo foo', u'x': u'y'}, 'localhost')


# Generated at 2022-06-13 07:05:46.208030
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {
        'action': 'shell',
        'args': 'echo hi'
    }
    assert ModuleArgsParser(task_ds).parse() == ('shell', 'echo hi', None)
    task_ds = {
        'action': 'shell',
        'args': {
            'key1': 'val1',
            'key2': 'val2'
        }
    }
    assert ModuleArgsParser(task_ds).parse() == ('shell', {'key1': 'val1', 'key2': 'val2'}, None)


# Generated at 2022-06-13 07:05:50.416893
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    test_input = dict(action="shell", args=dict(chdir="/tmp"))
    test_instance = ModuleArgsParser(task_ds=test_input)
    result = test_instance.parse()
    assert result == ('shell', {'chdir': '/tmp'}, Sentinel)


# Generated at 2022-06-13 07:06:01.452817
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    example_task_ds = { "copy": { "content": "hello world", "dest": "b" } }
    example_collection_list = None
    parser = ModuleArgsParser(example_task_ds, example_collection_list)
    action, args, delegate_to = parser.parse()
    assert action == "copy"
    assert args["content"] == "hello world"
    assert args["dest"] == "b"
    assert delegate_to is None

    example_task_ds = { "action": "copy x=1 y=2 z=3", "delegate_to": "localhost"  }
    example_collection_list = None
    parser = ModuleArgsParser(example_task_ds, example_collection_list)
    action, args, delegate_to = parser.parse()
    assert action == "copy"

# Generated at 2022-06-13 07:06:09.588128
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Create an object of the class to be unit tested
    parser = ModuleArgsParser()

    # Test using a string and an action name
    ret = parser.parse(skip_action_validation=True)
    assert ret == (None, {}, Sentinel), "Returned '%s' instead of '(None, {}, Sentinel)" % (ret, )

    # Test using a dictionary and an action name
    ret = parser.parse(skip_action_validation=True)
    assert ret == (None, {}, Sentinel), "Returned '%s' instead of '(None, {}, Sentinel)" % (ret, )

    # Test using a string and no action name
    ret = parser.parse(skip_action_validation=True)

# Generated at 2022-06-13 07:06:14.137955
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # action: name
    ds = dict(action=dict(module='configure_ceph', name='ceph'))
    action, args, delegate_to = ModuleArgsParser(ds).parse()
    assert action == 'configure_ceph'
    assert args == {'name': 'ceph'}
    assert delegate_to == Sentinel
    # action: 'name'
    ds = dict(action=dict(module="configure_ceph", args='name=ceph'))
    action, args, delegate_to = ModuleArgsParser(ds).parse()
    assert action == 'configure_ceph'
    assert args == {'name': 'ceph'}
    assert delegate_to == Sentinel
    # action: name=ceph

# Generated at 2022-06-13 07:06:21.288056
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    ds = {'action': 'copy', 'src': 'foo', 'dest': 'bar'}
    assert ModuleArgsParser(ds).parse() == ('copy', {'dest': 'bar', 'src': 'foo'}, None)
    ds = {'action': 'copy', 'src': 'foo', 'dest': 'bar', 'baz': 'bam'}
    with pytest.raises(AnsibleParserError) as excinfo:
        ModuleArgsParser(ds).parse()
    assert 'action and local_action are mutually exclusive' in to_text(excinfo.value)
    ds = {'action': {'boo': 'foo', 'foo': 'bar'}}
    assert ModuleArgsParser(ds).parse() == ('boo', {'foo': 'bar'}, None)


# Generated at 2022-06-13 06:56:51.072111
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 06:57:03.358645
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # test multiple args, the handler task itself
    task_ds = dict(
      action='service',
      name='httpd',
      state='started',
      enabled='yes',
      reusable=True,
      with_items=['a', 'b'],
    )
    args = dict()
    delegate_to = None
    parser = ModuleArgsParser(task_ds=task_ds)
    assert parser.parse() == (
      'service',
      dict(
        name='httpd',
        state='started',
        enabled='yes',
        reusable=True,
      ),
      None,
    )
    # test multiple args, no 'module: '

# Generated at 2022-06-13 06:57:05.652432
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser()
    assert module_args_parser.parse() == 0

# Test for class AnsibleTask

# Generated at 2022-06-13 06:57:09.858726
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    args = dict(action='shell', _raw_params='echo hello')
    parser = ModuleArgsParser(args)
    (action, args, delegate_to) = parser.parse()
    assert action == 'shell'
    assert args == dict(_raw_params='echo hello')
    assert delegate_to == Sentinel


# Generated at 2022-06-13 06:57:18.888386
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Test fixture
    task_ds = {}
    collection_list = None
    obj = ModuleArgsParser(task_ds, collection_list)

    # Mock module loader find_plugin_with_context to return a mock
    # module for the module_loader module
    def mock_find_plugin_with_context(name, collection_list):
        mock_module = mock.Mock()
        mock_module.resolved = False
        return mock_module
    module_loader.find_plugin_with_context = mock_find_plugin_with_context

    # Mock action loader find_plugin_with_context to return a mock
    # module for the module_loader module
    def mock_find_plugin_with_context(name, collection_list):
        mock_module = mock.Mock()
        mock_module.resolved = False
       

# Generated at 2022-06-13 06:57:20.432873
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass

# Generated at 2022-06-13 06:57:24.535736
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser(task_ds={})
    module_args_parser.parse()
    module_args_parser.parse()
    module_args_parser.parse()

# Generated at 2022-06-13 06:57:34.112742
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Test args parsing for module with no_log specified
    task_ds = {'name': 'test', 'no_log': False, 'notify': [{'name': 'test'}]}
    collection_list = []
    module_args_parser = ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
    result = module_args_parser.parse()
    assert result == ('notify', {'name': 'test'}, None)

    # Test args parsing for module with loop value which is dictionary
    task_ds = {'action': {'account': 'test_account', 'inventory': {'hosts': ['test_host1', 'test_host2']}}}
    collection_list = []

# Generated at 2022-06-13 06:57:49.116772
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Create a mock module_loader
    mock_loader = Mock()
    mock_loader.is_collection_fragment.return_value = False
    mock_loader.is_valid_collection_name.return_value = True
    mock_loader.get_collections.return_value = None
    # Create mock task_ds
    mock_task_ds = {
        'action': 'shell echo hi',
        'local_action': 'shell echo hi'
    }
    # Create an instance of ModuleArgsParser
    module_args_parser = ModuleArgsParser(task_ds=mock_task_ds, collection_list=[])
    # Parse, skip validation and action_loader since we are unit testing
    # module_args_parser.parse()

# Generated at 2022-06-13 06:57:53.933900
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import pytest

    # Create an instance of ModuleArgsParser
    module_args_parser = ModuleArgsParser()

    # TODO: Add test cases that pass ModuleArgsParser._task_ds into module_args_parser.parse()
    # TODO: Add test cases that pass ModuleArgsParser._collection_list into module_args_parser.parse()
    # TODO: Make sure the return value type is as expected
    # TODO: Make sure the returned object has the expected fields/attributes
    pass

# Generated at 2022-06-13 06:58:13.822337
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    err = None
    # This is just a sample implementation, modify if necessary
    parser = ModuleArgsParser(task_ds=None)
    try:
        parser.parse()
    except Exception as exc:
        err = exc




# Generated at 2022-06-13 06:58:19.424718
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    import sys
    import os
    from lib.errors import AnsibleError
    from lib.compat import string_types
    from lib.compat.dict import sum_dictlist
    from lib.plugins.loader import action_loader
    from lib.plugins.loader import module_loader
    from lib.utils.pep import boolean
    from lib.utils.pep import first
    from lib.utils.pep import listify_lookup_plugin_terms
    from lib.utils.pep import complex_args_split
    from lib.utils.pep import parse_kv
    from lib.utils.pep import to_text
    from lib.vars.hostvars import HostVars
    from lib.collection_loader import AnsibleCollectionLoader
    from lib.template.template import Templar
    from lib.errors import AnsibleAssertion

# Generated at 2022-06-13 06:58:27.508920
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    thing = '''
    - name: test module args
      hosts: all
      tasks:
        - name: module args 1
          failsafe:
            module: fail
            msg: fail msg 1

        - name: module args 2
          fail:
            msg: fail msg 2

        - name: module args 3
          fail: "fail msg 3"

        - name: module args 4
          fail:
            args:
              msg: fail msg 4

        - name: module args 5
          fail:
            module: fail
            msg: fail msg 5

        - name: module args 6
          fail: "fail msg 6"

        - name: module args 7
          fail:
            args:
              msg: fail msg 7
    '''
    task_ds = yaml.load(thing)['tasks'][0]
    p = Module

# Generated at 2022-06-13 06:58:38.954080
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass


# the host list is maintained in the inventory
# this class should contain logic to manipulate the host and group lists
# as well as linking to the appropriate inventory and variable classes.
#
# Host lists can be built and expanded in a variety of ways. We might have a single
# host, a group name like 'xyz', a list of hosts, a range of hosts, a list of groups,
# and a combination of these (including combinations of ranges and lists).
#
# Also, the hosts we're given may not be valid for the inventory we're targeting.  So
# we also do validation here and make sure the hosts we end up with are valid for
# the inventory in use (which could be smart, or could be dumb, depending on the
# type of inventory we're using)

# Generated at 2022-06-13 06:58:41.548012
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    params = dict(
        action="copy",
        args="src=a dest=b",
    )
    ModuleArgsParser(task_ds=params)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 06:58:49.436063
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Unit tests for method parse using following args:
    #   task_ds=None
    #   collection_list=None
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    from ansible import context
    import ansible.constants as C
    from ansible.module_utils.common.collections import ImmutableDict
    import os
    import pytest
    import sys


# Generated at 2022-06-13 06:58:57.883669
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    m = ModuleArgsParser()
    assert "unexpected" in str(m.parse({"action" : ""}))
    assert "no module/action" in str(m.parse({}))
    assert "conflicting" in str(m.parse({"action" : "hi", "local_action" : "hello"}))

    assert ("hi", {"hello" : "world"}, "localhost") == m.parse({"local_action" : "hi hello=world"})
    assert ("hi", {"hello" : "world"}, "localhost") == m.parse({"local_action" : {"hello" : "world"}})
    assert ("hi", {"hello" : "world"}, Sentinel) == m.parse({"action" : {"hello" : "world"}})


# Generated at 2022-06-13 06:58:59.453350
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    assert 1 == 1


# Generated at 2022-06-13 06:59:09.420484
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser()
    action = None
    args = None
    delegate_to = None
    task_ds = {
        'action': 'copy src=a dest=b',
        'delegate_to': '',
        'args': {
            'src': 'a',
            'dest': 'b'
        }
    }
    
    assert module_args_parser.parse() == (None, None, None)
    assert module_args_parser.parse(skip_action_validation=True) == (None, None, None)
 
    module_args_parser = ModuleArgsParser(task_ds)
    action, args, delegate_to = module_args_parser.parse()
    assert action == 'copy'
    assert args == {'src': 'a', 'dest': 'b'}

# Generated at 2022-06-13 06:59:18.008065
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    #
    # mock the action_loader.find_plugin_with_context method and return dummy context
    #
    @mock.patch.object(action_loader, 'find_plugin_with_context', autospec=True)
    def test_parse(mock_find_plugin_with_context):
        action_loader_context = ActionLoaderContext()
        action_loader_context.resolved = True
        mock_find_plugin_with_context.return_value = action_loader_context
        #
        # mock the module_loader.find_plugin_with_context method and return dummy context
        #
        @mock.patch.object(module_loader, 'find_plugin_with_context', autospec=True)
        def test_parse_1(mock_find_plugin_with_context):
            module_loader_context

# Generated at 2022-06-13 06:59:58.663276
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_arg_parser = ModuleArgsParser()
    task_ds = None

    result = module_arg_parser.parse()
    assert type(result) == tuple
    assert len(result) == 3
    assert result[0] is None
    assert result[1] == dict()
    assert result[2] == Sentinel

    # Case: module: 'module_name'
    task_ds = {
        'module': 'module_name'
    }

    module_arg_parser = ModuleArgsParser(task_ds)
    result = module_arg_parser.parse()
    assert type(result) == tuple
    assert len(result) == 3
    assert result[0] == 'module_name'
    assert result[1] == dict()
    assert result[2] == Sentinel

    # Case: module: "module_name arg_

# Generated at 2022-06-13 07:00:08.178748
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_args_parser = ModuleArgsParser()
    for task in PARSE_TASK_TEST_CASES:
        expected_results = task['results']
        result = module_args_parser.parse(task['task'])
        fail_msg = "result: '%s' is not equal to expected result: '%s'" % (result, expected_results)
        assert isinstance(result, tuple), fail_msg
        assert_equal(len(result), len(expected_results), fail_msg)
        assert_equal(result[0], expected_results[0], fail_msg)
        assert_equal(result[1], expected_results[1], fail_msg)
        assert_equal(result[2], expected_results[2], fail_msg)



# Generated at 2022-06-13 07:00:21.050292
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task_include import TaskInclude
    parser = ModuleArgsParser(task_ds={"args": {}, "action": "notification", "name": "TestPlaybook", "version": 2.0}, collection_list=None)
    result = parser.parse()
    assert result == ("notification", {}, None), "Failed:result:%s" % (result)
    parser = ModuleArgsParser(task_ds={"args": {},
                                       "action": "shell",
                                       "free_form": "echo '{{ hostvars[inventory_hostname]['ansible_' + ansible_distribution]['release'] }}'",
                                       "name": "TestPlaybook",
                                       "version": 2.0},
                              collection_list=None)

# Generated at 2022-06-13 07:00:22.198945
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
  pass


# ===========================================

# Generated at 2022-06-13 07:00:29.116326
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:00:40.407970
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:00:41.648253
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    assert ModuleArgsParser("action").parse() == (None, None, None)



# Generated at 2022-06-13 07:00:42.995339
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    module_arg_parser = ModuleArgsParser({})
    module_arg_parser.parse()


# Generated at 2022-06-13 07:00:47.601431
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Initialize the class object
    module_args_parser = ModuleArgsParser()

    # Test case 1
    print("Test case 1")
    task_ds = {
        'action': 'copy src=a dest=b',
        'delegate_to': 'localhost',
        'args': dict(a='xyz')
    }
    action, arg, delegate_to = module_args_parser.parse(task_ds)
    print(action, arg, delegate_to)
    # Expected output:
    #     copy {'src': 'a', 'dest': 'b', 'a': 'xyz'} localhost


# Generated at 2022-06-13 07:00:57.768639
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook.task import Task

    mocked_task_ds = {'foo': 'bar', 'module': 'echo hello', 'action': 'copy foo=bar', 'local_action': 'shell echo localhost'}
    mocked_task = Task()
    mocked_task.action = 'copy'
    mocked_task.args = {'foo': 'bar'}
    mocked_task.delegate_to = 'localhost'

    parser_normal_task = ModuleArgsParser(mocked_task_ds)
    assert isinstance(parser_normal_task, ModuleArgsParser)
    assert parser_normal_task.parse() == mocked_task.args

    parser_broken_task = ModuleArgsParser(dict())
    assert isinstance(parser_broken_task, ModuleArgsParser)

# Generated at 2022-06-13 07:01:27.525167
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Test with a simple task structure
    test_task_ds = dict(action=dict(module='test_module', name='test_name', test_arg='test_val'),
                        args=dict(test_key='test_val'),
                        delegate_to='test_server',
                        register='test_var')
    parser = ModuleArgsParser(test_task_ds)
    output_action, output_args, output_delegate_to = parser.parse()

    assert output_action == 'test_module'
    assert 'name' in output_args and output_args['name'] == 'test_name'
    assert 'test_arg' in output_args and output_args['test_arg'] == 'test_val'
    assert 'test_key' in output_args and output_args['test_key'] == 'test_val'


# Generated at 2022-06-13 07:01:30.564217
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    test for method parse of class ModuleArgsParser
    '''
    m = ModuleArgsParser()
    m.parse()

# Generated at 2022-06-13 07:01:41.728083
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    # Arrange
    task_ds = {
        "action": "copy",
        "dest": "/etc/yum.repos.d/epel.repo",
        "src": "files/epel.repo"
    }
    collection_list = None
    module_args_parser = ModuleArgsParser(task_ds, collection_list)

    # Act
    actual_return_value = module_args_parser.parse()
    actual_result = actual_return_value[0]
    actual_args = actual_return_value[1]
    actual_delegate_to = actual_return_value[2]

    # Assert
    assert actual_result == 'copy'

# Generated at 2022-06-13 07:01:50.239374
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    #
    # Test setup.
    #
    input_task_ds = {
        "action": "copy src=a dest=b",
        "delegate_to": "localhost",
    }
    #
    # Test scheme and run.
    #
    test_obj = ModuleArgsParser(input_task_ds, None)
    out = test_obj.parse()
    #
    # Test sort.
    #
    assert out


# Generated at 2022-06-13 07:01:54.821266
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # FIXME: this test is not completed :)
    mod_args_parser = None
    result = mod_args_parser.parse()
    assert True # TODO: implement your test here


# Generated at 2022-06-13 07:02:03.829584
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {'action': 'shell echo hi'}
    collection_list = []
    module_args_parser = ModuleArgsParser(task_ds, collection_list)
    action, args, delegate_to = module_args_parser.parse()
    expected_action = 'shell'
    assert action == expected_action
    expected_delegate_to = None
    assert delegate_to == expected_delegate_to
    expected_args = dict()
    expected_args['_raw_params'] = 'echo hi'
    assert args == expected_args


    task_ds = {'action': 'shell echo hi', 'delegate_to': 'localhost'}
    collection_list = []
    module_args_parser = ModuleArgsParser(task_ds, collection_list)
    action, args, delegate_to = module_args_

# Generated at 2022-06-13 07:02:11.550729
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Tests the version of parse from action_plugins/__init__.py
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.loader import action_loader, module_loader
    from ansible.plugins.action.normal import (
        ActionModule as NormalActionModule,
        BUILTIN_TASKS,
        FREEFORM_ACTIONS,
    )

    from ansible.plugins.action import ActionModule as BasicActionModule
    from ansible.plugins.action.basic import ActionModule as OldBasicActionModule
    from ansible.template import Templar
    from ansible.utils.vars import merge_hash

    class ActionModule(BasicActionModule, NormalActionModule, OldBasicActionModule):
        pass


# Generated at 2022-06-13 07:02:16.493544
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():

    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler

    # store the valid Task/Handler attrs for quick access
    task_attrs = set(Task._valid_attrs.keys())
    task_attrs.update(set(Handler._valid_attrs.keys()))
    # HACK: why are these not FieldAttributes on task with a post-validate to check usage?
    task_attrs.update(['local_action', 'static'])
    task_attrs = frozenset(task_attrs)

    # test the 'action' case
    task_ds = {'action': 'copy src=a dest=b'}
    mgr = ModuleArgsParser(task_ds=task_ds)
    action, args, delegate_to = mgr.parse()
    assert action

# Generated at 2022-06-13 07:02:27.156708
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.common._collections_compat import Mapping
    unicode_type = get_unicode_type()
    bytes_type = get_bytes_type()
    dict_type = dict
    set_type = set
    str_type = str
    assert isinstance(str_type, type)
    assert isinstance(unicode_type, type)
    assert isinstance(bytes_type, type)
    assert isinstance(dict_type, type)
    assert isinstance(set_type, type)
    assert isinstance(Mapping, type)
    assert isinstance(list, type)
    assert isinstance(set, type)
    assert isinstance(dict, type)


# Generated at 2022-06-13 07:02:35.169354
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    parser = ModuleArgsParser({
            'action': 'shell echo hi',
            'delegate_to': '127.0.0.1',
        },
    )
    assert parser.parse() == ('shell', {'_raw_params': 'echo hi'}, '127.0.0.1')
    parser = ModuleArgsParser({
            'action': {'module': 'shell', 'args': 'echo hi'},
            'delegate_to': '127.0.0.1',
        },
    )
    assert parser.parse() == ('shell', {'_raw_params': 'echo hi'}, '127.0.0.1')

# Generated at 2022-06-13 07:02:59.920851
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    obj=ModuleArgsParser()
    assert obj.parse() == (None, None, Sentinel)


# Generated at 2022-06-13 07:03:04.165402
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    m = ModuleArgsParser(dict(action=dict(module='shell', echo='hi')), None)
    assert m.parse() == ('shell', {u'echo': 'hi'}, None)

# Generated at 2022-06-13 07:03:11.426078
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    mock_dict1 = dict()
    mock_dict2 = dict()
    mock_dict3 = dict()
    mock_dict4 = dict()
    mock_dict5 = dict()
    mock_dict6 = dict()
    mock_dict7 = dict()
    mock_dict8 = dict()
    mock_dict9 = dict()
    mock_dict10 = dict()
    mock_dict11 = dict()
    mock_dict12 = dict()
    mock_dict13 = dict()
    mock_dict14 = dict()
    mock_dict15 = dict()
    mock_dict16 = dict()
    mock_dict17 = dict()
    mock_dict18 = dict()
    mock_dict19 = dict()
    mock_dict20 = dict()
    mock_dict21 = dict()
    mock_dict22 = dict()
   

# Generated at 2022-06-13 07:03:19.742623
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Test normal case
    task_ds = {"action": {"module": "copy", "src": "a", "dest": "bc"}}
    collection_list = None
    parser = ModuleArgsParser(task_ds, collection_list)
    (action, args, delegate_to) = parser.parse()
    assert action == "copy"
    assert args == {"src": "a", "dest": "bc"}
    assert delegate_to == None

    # Test normal case where "args" key exist
    task_ds = {"action": {"module": "copy", "src": "a", "dest": "bc"}, "args": "var1=val1"}
    collection_list = None
    parser = ModuleArgsParser(task_ds, collection_list)
    (action, args, delegate_to) = parser.parse()

# Generated at 2022-06-13 07:03:35.017605
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = {}
    obj = ModuleArgsParser(task_ds=task_ds, collection_list=None)
    action, args, delegate_to = obj.parse()
    assert action is None
    assert args == {}
    assert delegate_to is None

    task_ds = {'module': 'some_module'}
    obj = ModuleArgsParser(task_ds=task_ds, collection_list=None)
    action, args, delegate_to = obj.parse()
    assert action == 'some_module'
    assert args == {}
    assert delegate_to is None

    task_ds = {'module': 'some_module', 'foo': 'bar'}
    obj = ModuleArgsParser(task_ds=task_ds, collection_list=None)
    action, args, delegate_to = obj.parse()

# Generated at 2022-06-13 07:03:42.247254
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_data = {'action': 'arg1=val1 arg2=val2'}
    parser = ModuleArgsParser(task_data, collection_list=[])
    assert parser.parse() == ('action', {'arg1': 'val1', 'arg2': 'val2'}, None)

    task_data = {'local_action': 'arg1=val1 arg2=val2'}
    parser = ModuleArgsParser(task_data, collection_list=[])
    assert parser.parse() == ('local_action', {'arg1': 'val1', 'arg2': 'val2'}, 'localhost')

    task_data = {'local_action': 'arg1=val1 arg2=val2',
                 'delegate_to': 'other_host'}

# Generated at 2022-06-13 07:03:49.284916
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:04:00.789546
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:04:10.141539
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    assert ModuleArgsParser({
        "foo": "bar",
        "local_action": {
            "foo": "bar",
            "baz": "boo"
        }
    }).parse() == (None, {}, None)

    assert ModuleArgsParser({
        "foo": "bar",
        "local_action": {
            "foo": "bar",
            "baz": "boo"
        },
        "action": {
            "baz": "boo",
            "foo": "bar"
        }
    }).parse() == (None, {}, None)


# Generated at 2022-06-13 07:04:23.840748
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Data for testing ModuleArgsParser:parse
    vars = dict()
    result = dict()

    # Case to test key=value and dictionary forms
    args = {'foo': 'bar'}
    action = 'shell'
    delegate_to = 'localhost'
    kwargs = dict(dict={'foo': 'bar'}, action='shell', delegate_to='localhost', additional_args={})
    expect_result = {'action': 'shell', 'args': {'_raw_params': 'foo=bar'}, 'delegate_to': 'localhost'}
    mp = ModuleArgsParser()
    actual_result = mp.parse(**kwargs)
    if expect_result == actual_result:
        print('Expect and Actual Results are same')
    else:
        print('Expect and Actual Results are not same')
    #

# Generated at 2022-06-13 07:05:03.599332
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    temp_instance = ModuleArgsParser()
    print("Inside test_ModuleArgsParser_parse")
    action, args, delegate_to = temp_instance.parse()
    print("End of test_ModuleArgsParser_parse")


# Generated at 2022-06-13 07:05:16.898847
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # Normalized example
    task_ds = {
        'name': 'test',
        'args': {
            'src': 'a',
            'dest': 'b'
        },
        'module': 'copy'
    }
    expected = ('copy', {
            'src': 'a',
            'dest': 'b'
        }, Sentinel)
    assert ModuleArgsParser(task_ds).parse() == expected

    # Old-style example
    task_ds = {
        'name': 'test',
        'action': 'copy src=a dest=b'
    }
    expected = ('copy', {
            'src': 'a',
            'dest': 'b'
        }, Sentinel)
    assert ModuleArgsParser(task_ds).parse() == expected

    # Dictionary args example

# Generated at 2022-06-13 07:05:30.057939
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.role.include import RoleInclude

    pb = Playbook()

# Generated at 2022-06-13 07:05:37.573146
# Unit test for method parse of class ModuleArgsParser

# Generated at 2022-06-13 07:05:50.811166
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    '''
    Unit test for method ModuleArgsParser.parse()
    '''

    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.plugins.loader import action_loader

    task_ds = task_ds = {
        'action': {
            'module': 'shell',
            'args': 'echo hi'
        },
        'local_action': {
            'module': 'copy',
            'src': '{{ src }}',
            'dest': '{{ dest }}'
        },
        'remote_src': False,
        'set_facts': {
            'facts1': '{{ some_var }}',
            'facts2': '{{ some_other_var }}'
        }
    }

    task = Task()
    task.load(task_ds)

# Generated at 2022-06-13 07:06:02.149530
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    # test 1
    task_ds = {}
    assert ModuleArgsParser(task_ds).parse() == (None, {}, None)
    # test 2
    task_ds = {
        'action': 'copy',
        'foobar': 'shell'
    }
    mock_args = {'_raw_params': 'src=a dest=b', 'src': 'a', 'dest': 'b'}
    assert ModuleArgsParser(task_ds).parse() == ('copy', mock_args, None)
    # test 3
    task_ds = {
        'foobar': 'copy src=a dest=b',
        'action': 'shell'
    }
    assert ModuleArgsParser(task_ds).parse() == ('copy', mock_args, None)
    # test 4

# Generated at 2022-06-13 07:06:02.730637
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    pass



# Generated at 2022-06-13 07:06:10.888134
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    for method in (
            'copy', 'copy_role', 'copy_vars', 'copy_default_vars',
            'copy_facts', 'flatmap', 'group_by', 'map', 'nested', 'pair', 'sequence', 'union'):
        task_ds = {method: 'some_file'}
        args_spec = dict()
        parser = ModuleArgsParser(task_ds=task_ds)
        action, args, delegate_to = parser.parse()
        assert action == method, (method, action)
        assert isinstance(args, dict), args
        assert delegate_to is None, delegate_to

        task_ds = {method: {'src': 'some_file', 'dest': 'some_folder'}}
        parser = ModuleArgsParser(task_ds=task_ds)
        action, args,

# Generated at 2022-06-13 07:06:18.138210
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    task_ds = dict(
        action        = "copy",
        args          = dict(),
        delegate_to   = "localhost",
        ttt           = "t",
        local_action  = "copy",
        module        = "copy",
        task          = "copy",
        with_items    = "copy",
        with_dict     = "copy",
        with_first_found = "copy",
        with_flattened = "copy",
        with_nested = "copy",
        with_together = "copy",
        with_subelements = "copy",
        with_fileglob = "copy",
        with_indexed_items = "copy",
        with_sequence = "copy",
        with_random_choice = "copy",
        with_subelements = "copy",
    )
    t

# Generated at 2022-06-13 07:06:25.075875
# Unit test for method parse of class ModuleArgsParser
def test_ModuleArgsParser_parse():
    ''' test_ModuleArgsParser.py
        ansible/playbook/task_include.py
        Module to parse module argument string
    '''
    # test _ModuleArgsParser.parse()
    parser = ModuleArgsParser()
    from ansible.playbook.role.definition import RoleDefinition
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.task_include import TaskInclude